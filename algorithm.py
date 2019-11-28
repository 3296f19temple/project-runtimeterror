import pandas as pd
import numpy as np
import sys
import os
import time
import datetime
import re
import pickle
from course import Course

def getAllClasses(fileName):
	classes = None
	with open(fileName, "rb") as File:
	    classes = pickle.load(File)
	return classes
def getUserClasses(courseNameList, classes):
	classCatalog = []
	for courses in courseNameList:
		for cls in classes:
			if cls == courses:
				classCatalog.append(cls)
	return classCatalog

def displaySelectedCourses(catalog, schedules):
	for key in schedules:
		value = schedules[key]
		print("Schedule #", str(key))
		for items in catalog:
			print(value[items].display_course())

def makeSchedule(catalog, classes):
	schedules = {}
	key = 0
	for j in range(len(classes[catalog[0]])):
		count = 0
		tempSchedule = {}
		classFlag = 1
		#print("j: \n",j)
		for cls in catalog:
			#print("Cls: \n", cls)
			for i in range(len(classes[cls])):
				#print("Count: ", count)
				if(count == 0):
					#print("Count 0: ",classes[cls][j].display_course())
					tempSchedule[cls] = classes[cls][key]
					count = count+1
					break
				if(i == len(classes[cls]) -1 ):
					print("Class could not be added", cls)
					tempSchedule.clear()
					count = 0
					classFlag = 0
				if (isNoTimeConflict(tempSchedule, classes[cls][i])):
					tempSchedule[cls] = (classes[cls][i])
					#print("No Time conflict: ",classes[cls][i].display_course())
					break
				else:
					continue

		if(classFlag == 1):
			print("Adding to mainschedule", key)
			schedules[key] = tempSchedule
			key += 1
	return schedules

def isNoTimeConflict(tempSchedule,cls):
	for key in tempSchedule:
		clsValue = tempSchedule[key]
		if(cls.week_day == clsValue.week_day):
			if((cls.start_time >= clsValue.start_time and
			 cls.start_time <= clsValue.end_time) or (cls.end_time >= clsValue.start_time and
			 cls.end_time <= clsValue.end_time)):
				return False
	return True


def __main__():
	classes = getAllClasses("course_map.txt")
	listClasses = ["The Art of Acting","Understanding Urban Communities", 
	"Financial Accounting", "Managerial Accounting", 
	"Why care about College: Higher Education in American Life"]

	catalog = getUserClasses(listClasses, classes)
	
	schedules = makeSchedule(catalog, classes)
	displaySelectedCourses(catalog, schedules)
if __name__ == "__main__":
	__main__()