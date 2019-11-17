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
    driver.find_element_by_xpath('//*[@id="classSearchLink"]/span').click()
    driver.find_element_by_xpath('//*[@id="select2-chosen-1"]').click()
    
    driver.find_element_by_xpath('//*[@id="s2id_autogen1_search"]').send_keys('2020 Spring')
    time.sleep(10)
    driver.find_element_by_xpath('//*[@id="term-go"]').click()
    time.sleep(20)
    driver.find_element_by_xpath('//*[@id="search-go"]').click()
    time.sleep(10)
    for x in range(1010):
        driver.find_element_by_xpath('//*[@id="searchResultsTable"]/div[2]/div/button[3]').click()
        time.sleep(5)
    # print("course name is "+ courseNames)
    print("Obtained " + webPage)
    return res

if __name__ == "__main__":
    webPage = "https://prd-xereg.temple.edu/StudentRegistrationSsb/ssb/classSearch/classSearch"
    page = get_page(webPage)

    # print(page)
