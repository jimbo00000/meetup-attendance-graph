# calculate_totals.py

import json
import datetime
from collections import defaultdict

# http://stackoverflow.com/questions/6999726/how-can-i-convert-a-datetime-object-to-milliseconds-since-epoch-unix-time-in-p
def unix_time(dt):
    epoch = datetime.datetime.utcfromtimestamp(0)
    delta = dt - epoch
    return delta.total_seconds()

def unix_time_millis(dt):
    return unix_time(dt) * 1000



event_rsvps = defaultdict(int)
event_counts = defaultdict(int)
json_objects = []

with open('groups.json') as group_json:
    group_data = json.load(group_json)

# Accumulate totals by month
for g in group_data[0]["groups"]:
    mfile = "meetup_history_" + g +".json"
    #print(mfile)

    with open(mfile) as mjson:
        dat = json.load(mjson)
        for d in dat:
            msepoch = d['time']
            #print(msepoch, d['yes_rsvp_count'])
            x = datetime.date.fromtimestamp(msepoch/1000)
            monthdate = datetime.datetime(x.year, x.month, 1)
            #print(monthdate)
            event_rsvps[monthdate] += d['yes_rsvp_count']
            event_counts[monthdate] += 1

# Assemble into a json object
for k,v in sorted(event_rsvps.iteritems()):
    #print(k,v, event_counts[k])
    millis = unix_time_millis(k)
    #print('%f' % millis)
    #print('{0:f}'.format(millis))
    #print(int(millis))
    jo = {}
    jo['time'] = int(millis)
    jo['yes_rsvp_count'] = v
    #print(jo)
    json_objects.append(jo)

#print json_objects
with open('meetup_history_total.json', 'w') as tots:
    json.dump(json_objects, tots)
