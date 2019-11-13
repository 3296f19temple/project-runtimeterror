#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import bs4 as bs
import os
import time
import datetime
from selenium import webdriver

# Finds all categories respective apps
def get_page(webPage):
    print("Obtaining " + webPage + "...")

    # create a chrome instance
    driver = webdriver.Chrome()

    
    # get landing page of category
    driver.get(webPage)
    # wait for javascript
    res = driver.execute_script("return document.documentElement.outerHTML")
    courseNames = driver.find_elements_by_class_name('section-details-link')
    courseTimes = driver.find_elements_by_class_name('meeting')
    # print("course name is "+ courseNames)
    print("Obtained " + webPage)
    return res

if __name__ == "__main__":
    webPage = "https://prd-xereg.temple.edu/StudentRegistrationSsb/ssb/classSearch/classSearch"
    page = get_page(webPage)

    # print(page)
