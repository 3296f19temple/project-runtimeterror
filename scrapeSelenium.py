#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import bs4 as bs
import os
import time
import datetime
from selenium import webdriver
import pickle

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
    # writes the key into the scroll page
    driver.find_element_by_xpath('//*[@id="s2id_autogen1_search"]').send_keys('2020 Spring')
    # allows user to manually click the drop down box option
    time.sleep(10)
    #everything is automated after this
    driver.find_element_by_xpath('/html/body/main/div[3]/div/div/div/div/div[1]/div[2]/div[2]/button').click()
    time.sleep(10)
    classes = []
    for x in range(202):
        print("PROCESSING PAGE " + str(x))
        time.sleep(5)
        try:
            html = driver.page_source
            soup = bs.BeautifulSoup(html,'lxml')
            table = soup.find("tbody")
            for index, row in enumerate(table.find_all("tr"), 1):
                try:
                    class_a = []
                    for item in row.find_all("td"):
                        class_a.append(item.text)

                    classes.append(class_a)
                    print("\tClass [" + str(index) + "] : ", end="")

                    for item in class_a:
                        print(str(item) + "|", end="")
                    print()
                    print()
                except:
                    print("ERROR PROCESSING CLASS : Skipping Class " + str(index))
        except:
            print("ERROR PROCESSING PAGE: Skipping page " + str(x))
        driver.find_element_by_xpath('//*[@id="searchResultsTable"]/div[2]/div/button[3]').click()
    # print("course name is "+ courseNames)

    with open("scraped.txt", "wb") as logFile:
        pickle.dump(classes, logFile)
    return res

if __name__ == "__main__":
    webPage = "https://prd-xereg.temple.edu/StudentRegistrationSsb/ssb/classSearch/classSearch"
    get_page(webPage)
    print("DONE")
