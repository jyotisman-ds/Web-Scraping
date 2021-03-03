#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 21:58:35 2021

@author: jyotisman
"""

"""
Challenge :
    
    - open sdsclub.com
    - click on 'learning paths'
    - click on 'become an ai engineer'
    - return the 3 pieces : 'x courses', 'x hours in total', 'x case studies'
    - return text from market and career opportunity
    - finally return names of instructors
"""



import time 
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from bs4 import BeautifulSoup


"""
To disable pop-ups:
    
useful link : https://www.browserstack.com/docs/automate/selenium/enable-pop-ups#python

"""
caps = DesiredCapabilities.CHROME
caps["chromeOptions"] = {}
caps["chromeOptions"]["excludeSwitches"] = ["disable-popup-blocking"]

driver = webdriver.Chrome(desired_capabilities=caps) # already in system path, so need to provide path


def all_tasks():
    
    driver.get('https://sdsclub.com/')
    time.sleep(5)
    
    # links to visit
    driver.find_element_by_xpath('//*[@id="menu-item-456"]/a').click()
    time.sleep(5)
    
    driver.find_element_by_xpath('//*[@id="category-career"]/div/div[2]/div[4]/div/figure/a').click()
    time.sleep(10)
    
    # time to scrape with BeatifulSoup
    soup = BeautifulSoup(driver.page_source, 'lxml')

    course_info = [x.find('span').text for x in soup.find_all('div', class_ = 'path-meta-item')]
    
    #opp_info = [x.find('p').text for x in soup.find_all('div', class_ = 'single-path-article-content')]
    
    opp_info_class = soup.find('div', class_ = 'single-path-articles')

    opp_info = [x.find('p').text for x in opp_info_class.find_all('div', class_ = 'single-path-article-content')]
    
    instructor_info_class = soup.find('div', class_ = 'instructors-list pt-1 mb-n1')
    
    instructor_info = [x.find('div', class_ = 'content').find('div').find('p', class_ = 'name').text for x in instructor_info_class.find_all('div', class_ = 'instructors-list-item')]
    

    print("Course_info : ", course_info)
    print()
    print("Opportunity_info : ", opp_info)
    print()
    print("Instructor_info : ", instructor_info)


all_tasks()
time.sleep(5)

driver.quit()