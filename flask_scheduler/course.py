#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import datetime

class Course:
    # instantiate our course object
    def __init__(self, class_a):
        try:
            # save crn
            self.CRN = class_a[0]

            # save course subject
            self.subject = class_a[1][0]

            # save section
            self.course_section = class_a[1][1]

            # save campus
            self.campus = class_a[2]

            # save course hours
            self.hours = class_a[3]

            # save the course title
            self.title = class_a[4]

            # save the week day of the course
            self.week_day = class_a[5][0].strip()

            # parse the start and end times
            start_time, end_time = class_a[5][1].split("-")
            start_time = start_time.strip()
            end_time = end_time.strip()

            # save the start time
            self.start_time = self.parse_time(start_time)

            # save the end time
            self.end_time = self.parse_time(end_time)

            # save the course type
            self.type_a = class_a[5][2]

            # store the building
            self.building = class_a[5][3]

            # store the room location
            self.room = class_a[5][4]

            # parse the start date and end dates
            start = class_a[5][5]
            start = start.split("/")
            end = class_a[5][6]
            end = end.split("/")

            # create a date object for start date
            self.start_date = datetime.datetime(int(start[2]),
                                                int(start[0]), int(start[1]))

            # create a date object for end date
            self.end_date = datetime.datetime(int(end[2]),
                                              int(end[0]), int(end[1]))
            # store the seat availability
            self.seat_availability = class_a[6][0]

            # store the waitlist availability
            self.waitlist_availability = class_a[6][1]

            # store the professor
            self.professor = class_a[7]

            # store the part of term
            self.part_of_term = class_a[8]

            # boolean to track successful parsing
            self.isValid = True
        except:
            # if something fails, set the course to invalid
            self.isValid = False

    # return the courses title
    def get_title(self):
        return self.title

    # parse the time string into a inbuilt python time object
    def parse_time(self, time_a):
        # split the time item by whitespace
        time_a, section = time_a.split()

        # remove whitespace
        section = section.strip()
        time_a = time_a.strip()
        hours = 0

        # convert time to 24 hour format
        if(section == "PM"):
            hours = 12

        # split by hours and minutes
        hour, minute = time_a.split(":")

        # ensure we dont get 24 for 12 pm
        if(int(hour) == 12 and section == "PM"):
            hours += 0
        else:
            hours+= int(hour)

        # conver minute to integer 
        minute = int(minute)

        # create a time object
        time_a = datetime.time(hours,minute, 0)

        return time_a

    # returns the start and end times
    def get_times(self):
        return(self.start_time, self.end_time, self.week_day, self.part_of_term)

    # display the course information
    def display_course(self):
        print("CRN : " + str(self.CRN))
        print("\tSubject : " + str(self.subject))
        print("\tCourse Section : " + str(self.course_section))
        print("\tCampus : " + str(self.campus))
        print("\tHourse : " + str(self.hours))
        print("\tTitle : " + str(self.title))
        print("\tDay of Week : " + str(self.week_day))
        print("\tStart Time : " + str(self.start_time))
        print("\tend Time : " + str(self.end_time))
        print("\tType : " + str(self.type_a))
        print("\tBuilding : " + str(self.building))
        print("\tRoom : " + str(self.room))
        print("\tStart Date : " + str(self.start_date))
        print("\tEnd Date : " + str(self.end_date))
        print("\tSeat Availability : " + str(self.seat_availability))
        print("\tWaitlist Availability : " + str(self.waitlist_availability))
        print("\tProfessor : " + str(self.professor))
        print("\tPart of Term : " + str(self.part_of_term))
