#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pickle
import numpy as np
from course import Course
from schedule import Schedule
import itertools
import random
class makeSchedule:
    def get_classes(self, classes, x):
        l = [random.randint(0,len(classes)-1) for i in range(x)]

        des_class = []
        for index, key in enumerate(classes):
            if index in l:
                des_class.append(key)
                l.remove(index)

        return des_class

    def get_des(self, classes, courses_desired):
        temp = []
        for key in courses_desired:
            if(key in classes):
                temp.append(classes[key])
        
        return temp

    def get_permutations(self, des):
        return list(itertools.product(*des))

    def create_schedule(self, classList):
        classes = {}
        with open("course_map.txt", "rb") as logFile:
            classes = pickle.load(logFile)

        courses_desired = classList

        des = self.get_des(classes, courses_desired)

        course_perm = self.get_permutations(des)

        schedules = []

        for schedule in course_perm:
            isValid = True
            sched = Schedule()

            for class_a in schedule:
                # must still check if time conflict occurs
                isValid = sched.add_class(class_a)
                if(not isValid):
                    break
                
            if(isValid):
                schedules.append(sched)

        for schedule in schedules:
            schedule.display_schedule()

        print("Total schedules: " + str(len(schedules)))
        return schedules
