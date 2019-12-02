#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from course import Course

class Schedule:
    def __init__(self):
        self.class_list = []

    def add_class(self, class_a):
        new_start, new_end, new_week, new_term = class_a.get_times()

        new_week = new_week.split(",")
        
        for course_a in self.class_list:
            old_start, old_end, old_week, old_term = course_a.get_times()
            old_week = old_week.split(",")

            time_conflict = False
            # must check if time conflict occurs
            for index,day in enumerate(new_week,0):
            	for i, oldDay in enumerate(old_week,0):
                    if (day == oldDay):
                	    if((new_start >= old_start and new_start <= old_end)or(new_end >= old_start and new_end <= old_end)or(old_start>= new_start and old_start<=new_end)):
                		    time_conflict = True
            time_conflict = False
            if(time_conflict):
                return False
                        
            
        self.class_list.append(class_a)
        
        return True
        
    def display_schedule(self):
        print("-------------")
        print("SCHEDULE")
        for class_a in self.class_list:
            class_a.display_course()
        print("-------------")

