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
