#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import datetime

class Course:
    def __init__(self, class_a):
        try:
            self.CRN = class_a[0]
            self.subject = class_a[1][0]
            self.course_section = class_a[1][1]
            self.campus = class_a[2]
            self.hours = class_a[3]
            self.title = class_a[4]
            self.week_day = class_a[5][0].strip()


            start_time, end_time = class_a[5][1].split("-")
            start_time = start_time.strip()
            end_time = end_time.strip()

            self.start_time = self.parse_time(start_time)
            self.end_time = self.parse_time(end_time)
            self.type_a = class_a[5][2]
            self.building = class_a[5][3]
            self.room = class_a[5][4]

            start = class_a[5][5]
            start = start.split("/")
            end = class_a[5][6]
            end = end.split("/")
            
            self.start_date = datetime.datetime(int(start[2]), int(start[0]), int(start[1]))
            self.end_date = datetime.datetime(int(end[2]), int(end[0]), int(end[1]))
            self.seat_availability = class_a[6][0]
            self.waitlist_availability = class_a[6][1]
            self.professor = class_a[7]
            self.part_of_term = class_a[8]
            self.isValid = True
        except:
            self.isValid = False

    def get_title(self):
        return self.title
    
    def parse_time(self, time_a):
        time_a, section = time_a.split()
        section = section.strip()
        time_a = time_a.strip()
        hours = 0
        if(section == "PM"):
            hours = 12

        hour, minute = time_a.split(":")
        if(int(hour) == 12 and section == "PM"):
            hours += 0
        else:
            hours+= int(hour)
        minute = int(minute)

        time_a = datetime.time(hours,minute, 0)

        return time_a

    def get_times(self):
        return(self.start_time, self.end_time, self.week_day, self.part_of_term)

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
