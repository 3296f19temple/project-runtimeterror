#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import bs4 as bs
import urllib.request
import pandas as pd
import pickle
import threading
import requests
import os
import random
import time

def get_contents(page, proxies, user_agents):
    got_contents = False

    #Get a proxy from the pool
    #proxy = random.choice(proxies)
    #agent = random.choice(user_agents)
    agent = "Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)"
    try:            
        #print("Getting Response from " + proxy + " using "+ agent)
        #            response = requests.get(page, proxies={"https": proxy}, headers={"User-Agent" : agent})
        #response = requests.get(page, headers={"User-Agent" : agent})
        response = requests.get(page, headers={"User-Agent" : agent})
        
    except:
        print("Connnection error")

    if(response.status_code != 200):
        return False
    else:
        return response

def grab_page(page, proxies, user_agents):
    source = get_contents(page, proxies, user_agents)
    if(source == False):
        print("Error: Failed to get contents")
        return

    source = source.content
    soup = bs.BeautifulSoup(source, 'lxml')
    return soup
    
# generates a set of proxy ip addresses
def get_proxies():
    url = 'https://free-proxy-list.net/'
    response = requests.get(url).content
    soup = bs.BeautifulSoup(response, 'lxml')

    proxies = []
    for tr in soup.find_all("tr"):
        proxy=[]
        is_elite = False
        for td in tr:
            proxy.append(td.text)
            if(td.text == "elite proxy"):
                is_elite = True
            if(td.text == "yes" and is_elite):
                proxies.append(proxy[0] + ":" + proxy[1])
    return proxies

# generates a set of fake user agents
def get_user_agents():
    url = "https://developers.whatismybrowser.com/useragents/explore/software_name/chrome/"

    response = requests.get(url).content
    soup = bs.BeautifulSoup(response, 'lxml')

    user_agents = []

    for tbody in soup.find_all("tbody"):
        for tr in tbody.find_all("tr"):
            user_agents.append(tr.find("a").text)

    return user_agents

if __name__ == "__main__":
    main_page = 'https://www.coursicle.com/robots.txt'

    proxies = []#get_proxies()
    user_agents = get_user_agents()

#    with open("user_agents.txt", "wb") as agentFile:
#        pickle.dump(user_agents, agentFile)
#
#    with open("user_agents.txt", "rb") as agentFile:
#        user_agents = pickle.load(agentFile)

    page = grab_page(main_page, proxies, user_agents)

    print("Page Contents")
    print(page)

    print("Done")
