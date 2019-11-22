#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pickle
import numpy as np
from course import Course

# CONSTANTS
CRN = 0
SUBJECT_COURSE_SECTION = 1
CAMPUS = 2
HOURS = 3
TITLE = 4
MEETING_TIMES = 5
CAPACITY = 6
INSTRUCTOR = 7
PART_OF_TERM = 8    

def getData(scrapeFile):
    classes = None
    with open(scrapeFile, "rb") as logFile:
        classes = pickle.load(logFile)

    classes = removeEmpty(classes)    
    return classes

def removeEmpty(classes):
    classes_new = []

    for line in classes:
        class_a = []
        for index, item in enumerate(line, 1):
            if(item == "View Course Materials"):
                continue
            
            if item.strip():
                class_a.append(item)
        classes_new.append(class_a.copy())
    return classes_new

def prettify(classes):
    bad_indices = []
    for i, line in enumerate(classes):
        for j, item in enumerate(line):
            try:
                if(j == SUBJECT_COURSE_SECTION):
                    temp = item.split(',')
                    for k, val in enumerate(temp):
                        temp[k] = val.strip()
                    classes[i][j] = temp
                elif(j == MEETING_TIMES):
                    hold_class = []
                    temp = item.split("SMTWTFS")
                    hold_class.append(temp[0])
                    temp = temp[1]

                    temp = temp.split("Type:\xa0")
                    hold_class.append(temp[0])
                    temp = temp[1]

                    temp = temp.split("Building:")
                    hold_class.append(temp[0])
                    temp = temp[1]


                    temp = temp.split("Room:")
                    hold_class.append(temp[0])
                    temp = temp[1]

                    temp = temp.split("Start Date:")
                    hold_class.append(temp[0])
                    temp = temp[1]

                    temp = temp.split("End Date:")
                    hold_class.append(temp[0])
                    temp = temp[1]
                    
                    hold_class.append(temp)
                    
                    for k in range(len(hold_class)):
                        hold_class[k] = hold_class[k].strip()

                    classes[i][j] = hold_class

                elif(j == CAPACITY):
                    classes[i][j] = classes[i][j].split(".")[0:2]
                else:
                    classes[i][j] = classes[i][j].strip()

            except:
                bad_indices.append(i)

    for count, index in enumerate(bad_indices):
        index -= count
        del(classes[index])

    return classes

if __name__ == "__main__":
    scrapeFile = "scraped.txt"
    postFile = "post.txt"
    classes = getData(scrapeFile)
    
    classes = prettify(classes)

    courses = []
    for i, class_a in enumerate(classes,1):
        course = Course(class_a)
        if(course.isValid):
            courses.append(course)

    print(str(len(classes)-len(courses)) + " Classes have been lost. Total complete classes : "
          + str(len(courses)))

    # initialize course dictionary
    course_dict = {}
    for class_a in courses:
        title = class_a.get_title()
        if(not(title in course_dict)):
            course_dict[title] = []

        course_dict[title].append(class_a)

    with open("course_map.txt", "wb") as mapfile:
        pickle.dump(course_dict, mapfile)
