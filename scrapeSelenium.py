import sys
import requests
import bs4 as bs
import os
import time
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from tkinter import messagebox
from selenium.webdriver.support import expected_conditions as ec
import pandas as pd

# Finds all categories respective apps
def get_page(webPage):
    f = open("Scraped.txt","w")
    print("Obtaining " + webPage + "...")
    
    # create a chrome instance
    driver = webdriver.Chrome()

    
    # get landing page of category
    driver.get(webPage)
    # wait for javascript
    res = driver.execute_script("return document.documentElement.outerHTML")
    driver.find_element_by_xpath('//*[@id="classSearchLink"]/span').click()
    driver.find_element_by_xpath('//*[@id="select2-chosen-1"]').click()
    value = driver.find_element_by_xpath('//*[@id="s2id_autogen1_search"]')#.send_keys('2020 Spring')
    value.send_keys('2020 Spring')
    WebDriverWait(driver, 10)
    #messagebox.showinfo(title='2-step verification', message='Finish on screen 2-step verification, and then click OK.')    
    
    x = WebDriverWait(driver, 10).until(ec.title_is("Banner"))
   
    #y = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.ID,"search-go")))
    s = WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.ID,"search-go")))
    s.click()
    for i in range(2):
        WebDriverWait(driver, 10)
        html = driver.page_source
        soup = bs.BeautifulSoup(html,'lxml')
        print(soup.body.find('table', attrs={'class':'ui-widget-content resizable KeyTable draggable footable footable-loaded default grid'}).text)
        #list = pd.read_html(html)
        #parse the data on each page:
        #courseList = soup.find('table')[0]
        #f.write(str(soup))
        #print(list[0])
        #driver.find_element_by_xpath('//*[@id="searchResultsTable"]/div[2]/div/button[3]').click()
    # print("course name is "+ courseNames)
    print("Obtained " + webPage)
    f.close()
    return res

if __name__ == "__main__":
    webPage = "https://prd-xereg.temple.edu/StudentRegistrationSsb/ssb/classSearch/classSearch"#"https://prd-xereg.temple.edu/StudentRegistrationSsb/ssb/classSearch/classSearch"
    page = get_page(webPage)

    # print(page)