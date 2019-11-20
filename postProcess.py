#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pickle
import numpy as np


def getData(scrapeFile):
    classes = None
    with open(scrapeFile, "rb") as logFile:
        classes = pickle.load(logFile)

    classes = removeEmpty(classes)    
    return classes

def removeEmpty(classes):
    for lineIndex, line in enumerate(classes):
        for index, item in enumerate(line):
            if not item:
                del(classes[lineIndex][index])
    return classes

if __name__ == "__main__":
    scrapeFile = "scraped.txt"
    postFile = "post.txt"
    classes = getData(scrapeFile)

    with open(postFile, "w") as postLog:
        for line in classes:
            for index, item in enumerate(line, 1):
                if(item == "View Course Materials"):
                    continue
            
                if item.strip():
                    postLog.write(item)
                    if(index != 10):
                        postLog.write("|")
            postLog.write("\n")

