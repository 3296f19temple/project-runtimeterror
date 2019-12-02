#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from course import Course

class Schedule:
    # initialize empty schedule
    def __init__(self):
        self.class_list = []

    # add a nonconflicting class to schedule
    def add_class(self, class_a):
        # get classes times
        new_start, new_end, new_week, new_term = class_a.get_times()

        # parse all days
        new_week = new_week.split(",")

        # loop through our schedule
        for course_a in self.class_list:
            # get the old times
            old_start, old_end, old_week, old_term = course_a.get_times()
            old_week = old_week.split(",")

            time_conflict = False
            # must check if time conflict occurs
            for index,day in enumerate(new_week,0):
            	for i, oldDay in enumerate(old_week,0):
                    # if one of the days match
                    if (day == oldDay):
                        # check for time conflict
                	if((new_start >= old_start and new_start <= old_end)or(new_end >= old_start and new_end <= old_end)or(old_start>= new_start and old_start<=new_end)):
                            # if time conflict, note it
                	    time_conflict = True
            time_conflict = False
            # if time conflict occurs, return false
            if(time_conflict):
                return False

        # append non conflicting class to schedule
        self.class_list.append(class_a)
        
        return True

    # display the schedule
    def display_schedule(self):
        print("-------------")
        print("SCHEDULE")
        for class_a in self.class_list:
            class_a.display_course()
        print("Total Courses: " + str(len(self.class_list)))
        print("-------------")

    # get the current schedule
    def get_courses(self):
        return self.class_list
