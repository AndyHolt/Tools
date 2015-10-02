#!/usr/local/bin/python
"""
Convert trainline confirmation to ics for calendar

Trainline sends booking confirmation emails with details of train journey, but
ics calendar events offered don't put useful information in useful places for
the calendar event. DIY fix to make these.
"""
# Author: Andy Holt
# Date: Fri 02 Oct 2015 10:40

from icalendar import Calendar, Event
import sys
import re
from datetime import timedelta

# get journey information from provided file or stdin
# [todo] - add option to get info from stdin
for txt in sys.argv[1:]:
    # open txt file and extract journeys
    file = open(txt).read()
    journeys = re.split('Journey [0-9]+:', file)

    # setup icalendar
    cal = Calendar()

    # process journey info into useful bits
    for jrn in journeys[1:]:
        # extract the line with the date on
        full_date = re.search((r'Travel on '
          '(Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday) '
          '([0-9]+) '
          '(January|February|March|April|May|June|July|'
          'August|September|October|November|December) ([0-9]{4})'), jrn)

        # get the date components
        day = full_date.group(2)
        month = full_date.group(3)
        year = full_date.group(4)

        # convert month from word to number
        month_names = ['January', 'February', 'March', 'April', 'May', 'June',
                       'July', 'August', 'September', 'October', 'November',
                       'December']
        month_no = month_names.index(month) + 1

        # zero pad date and month numbers
        if day <= 9:
            day = '0%s' % (day)

        if month_no <= 9:
            month_no = '0%s' % (month_no)

        # extract list of trains
        train_block = re.search(r'Departs(.*\n)+Ticket details', jrn)

        train_lines = train_block.group(0).split('\n')[1:-1]
        trains = [re.split(' - |\t', field) for field in train_lines]

        # for each train, get the travelling details
        for train in trains:
            stn_start = train[1]
            stn_end = train[3]
            depart_time = train[0]
            arrive_time = train[2]
            seat_rev = train[5]
            train_details = train[4]

            depart_time_list = depart_time.split(':')
            arrive_time_list = arrive_time.split(':')

            print 'Travelling on %s/%s/%s from %s to %s' % (day, month_no, year,
                                                            stn_start, stn_end)

            # create event with the info detailed
            event = Event()
            event['SUMMARY'] = 'Train: %s to %s' % (stn_start, stn_end)
            event['DTSTART'] = '%s%s%sT%s%s00' % (year, month_no, day,
                                                  depart_time_list[0],
                                                  depart_time_list[1])
            event['DTEND'] = '%s%s%sT%s%s00' % (year, month_no, day,
                                                arrive_time_list[0],
                                                arrive_time_list[1])
            event['DESCRIPTION'] = train_details
            event['LOCATION'] = seat_rev

            cal.add_component(event)

            
    # write .ics file(s) containing info
    filename = '%s-%s-%s_%sTo%s.ics' % (year, month_no, day,
                                        stn_start.replace(" ", ""),
                                        stn_end.replace(" ", ""))
    f = open(filename, 'w')
    f.write(cal.to_ical())
    f.close()
