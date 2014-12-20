meetup-attendance-graph
=======================

### Description

An interactive d3.js powered graph of Meetup attendance using data from the [Meetup API](http://www.meetup.com/meetup_api/).

Data is collected from the meetup API using a python script in an offline process to save bandwidth to meetup.com.


### Usage

To obtain data files, first choose a list of meetup names by editing **data/groups.json**.  

Create a file **data/meetupapikey.py** as follows:  

    def getKey():
        return "PASTE_YOUR_KEY_HERE"

Then edit **get_meetup_attendance.py** line 58 to go live, and run  

    python get_meetup_attendance.py


View the graph locally by running the following from the repo root:  

    python -m SimpleHTTPServer 8000

and point your browser(Chrome for best results) to [http://127.0.0.1:8000/attendance.html](http://127.0.0.1:8000/attendance.html).  

