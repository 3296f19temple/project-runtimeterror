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

# load the pickle object and remove empty columns
def getData(scrapeFile):
    classes = None

    # load our scraped classes
    with open(scrapeFile, "rb") as logFile:
        classes = pickle.load(logFile)

    # remove empty elements
    classes = removeEmpty(classes)    
    return classes

# removes empty/unneccessary elements
def removeEmpty(classes):
    classes_new = []

    # loop through each class
    for line in classes:
        class_a = []
        # for each item in the class
        for index, item in enumerate(line, 1):
            # remove the view course materials item
            if(item == "View Course Materials"):
                continue

            # remove empty / whitespace elements
            if item.strip():
                class_a.append(item)
        # append the processed class
        classes_new.append(class_a.copy())
    return classes_new

# loop through each class in classes and parse into workable elements
def prettify(classes):
    bad_indices = []

    # for each class
    for i, line in enumerate(classes):
        # for each item in each class
        for j, item in enumerate(line):
            # attempt to parse the class
            try:
                # parse the subject course section element
                if(j == SUBJECT_COURSE_SECTION):
                    temp = item.split(',')
                    for k, val in enumerate(temp):
                        temp[k] = val.strip()
                    classes[i][j] = temp
                # parse the meeting time elements
                elif(j == MEETING_TIMES):
                    # parse the day section
                    hold_class = []
                    temp = item.split("SMTWTFS")
                    hold_class.append(temp[0])
                    temp = temp[1]

                    # parse the type section
                    temp = temp.split("Type:\xa0")
                    hold_class.append(temp[0])
                    temp = temp[1]

                    # find the building
                    temp = temp.split("Building:")
                    hold_class.append(temp[0])
                    temp = temp[1]

                    # get the room number
                    temp = temp.split("Room:")
                    hold_class.append(temp[0])
                    temp = temp[1]

                    # get the start date
                    temp = temp.split("Start Date:")
                    hold_class.append(temp[0])
                    temp = temp[1]

                    # get the end date
                    temp = temp.split("End Date:")
                    hold_class.append(temp[0])
                    temp = temp[1]

                    hold_class.append(temp)

                    # remove whitespace from parsed elements
                    for k in range(len(hold_class)):
                        hold_class[k] = hold_class[k].strip()

                    # store the parsed elements
                    classes[i][j] = hold_class

                # parse the capacity column
                elif(j == CAPACITY):
                    classes[i][j] = classes[i][j].split(".")[0:2]
                else:
                    # remove whitespace from final elements
                    classes[i][j] = classes[i][j].strip()

            except:
                # on failure to parse, track the errorr so we may skip the class
                bad_indices.append(i)

    # remove classes that had error during parsing
    for count, index in enumerate(bad_indices):
        index -= count
        del(classes[index])

    return classes

if __name__ == "__main__":
    scrapeFile = "scraped.txt"
    postFile = "post.txt"

    # load data and remove unnecessary columns
    classes = getData(scrapeFile)

    # parse data into intuitive items for each class
    classes = prettify(classes)

    # convert each class into a course object
    courses = []
    for i, class_a in enumerate(classes,1):
        course = Course(class_a)

        # if course object was successfully created, track the course
        if(course.isValid):
            courses.append(course)

    # display the number of courses that are not tracked
    print(str(len(classes)-len(courses)) + " Classes have been lost. Total complete classes : "
          + str(len(courses)))

    # initialize course dictionary
    course_dict = {}

    # create a dictionary that maps the course_title to every course section
    for class_a in courses:
        # get the course title
        title = class_a.get_title()

        # add the key to our dictionary if it DNE
        if(not(title in course_dict)):
            course_dict[title] = []

        # add the course to our list
        course_dict[title].append(class_a)

    # save the course mapping
    with open("course_map.txt", "wb") as mapfile:
        pickle.dump(course_dict, mapfile)
