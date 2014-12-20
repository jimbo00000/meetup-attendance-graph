# Based on Mike Dewar's excellent d3talk:
# https://github.com/mikedewar/d3talk

import json
import urllib
from operator import itemgetter
import time

from meetupapikey import getKey
"""
# The meetupapikey.py file should look like this:
def getKey():
    return "PASTE_YOUR_KEY_HERE"
"""

def get_data(endpoint, params):
    
    url = endpoint + urllib.urlencode(params) + "&offset=%s"
    
    data = []
    offset= 0

    while True:
        print url%offset
        response = urllib.urlopen(url%offset)
        s = unicode(response.read(), errors="ignore")
        try:
            results = json.loads(s)['results']
        except KeyError:
            print s
            raise IOError("something went wrong...")
        if len(results) == 0:
            print "no more results returned"
            break
        data.extend(results)
        offset += 1
    return data

params = {
    "key": getKey(),
    "group_urlname": "Boston-Virtual-Reality",
    "status":"past"
}


endpoint = 'https://api.meetup.com/2/events?' 

with open('groups.json') as group_json:
    group_data = json.load(group_json)

groups = group_data[0]["groups"]
for g in groups:
    print(g)
    params["group_urlname"] = g
    print(params)
    outfile = "meetup_history_" + g +".json"
    print(outfile)
    if False: # True for live API calls
        time.sleep(5)
        meetups = get_data(endpoint, params)
        meetups.sort(key=itemgetter('time'))
        json.dump(meetups, open(outfile,'w'))
