#!/usr/local/bin/python
"""
Fix .ics files from thetrainline.com

Modify .ics files downloaded from thetrainline.com for input to calendar. The
standard .ics files contain marketing stuff and less useful information in the
most accessible places.
"""
# Author: Andy Holt
# Date: Wed 09 Sep 2015 11:23
# Usage: tlicsfix.py [filename]

from icalendar import Calendar
import sys
from datetime import timedelta

for ics in sys.argv[1:]:
    # open ics file and extract the event and the alarm
    cal = Calendar.from_ical(open(ics).read())
    event = cal.walk('vevent')[0]
    alarm = event.walk('valarm')[0]

    # rewrite a more helpful summary
    stn_start = event['location'].encode('utf-8').split()[2:-2]
    stn_end = event['summary'].encode('utf-8').split()[2:-2]
    departure_time = event['location'].encode('utf-8').split()[-1]

    event['summary'] = 'Train: %s to %s' % (stn_start, stn_end)


    # set alarm to 15 minutes before departure
    alarm['trigger'].dt = timedelta(minutes=-15)
    alarm['description'] = 'Train from %s at %s' % (stn_start, departure_time)

    # write changes back to original file
    f = open(ics, 'w')
    f.write(cal.to_ical())
    f.close()
