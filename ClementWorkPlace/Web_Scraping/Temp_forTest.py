#!/usr/bin/env python3

# coding=utf-8
# -*- coding: utf8 -*-

from urllib.request import urlopen
from bs4 import BeautifulSoup
import time,datetime
#from time import strftime

res = urlopen("https://www.104.com.tw/jobs/search/?ro=0&jobcat=2007000000&area=6001001010&order=2&asc=0&page=7&mode=s&jobsource=joblist_a_date")
soup = BeautifulSoup(res, features="html.parser")
#print(soup.select(".js-job-link"))
#print(soup.select(".js-job-item")) not good for used

'''
input = soup.select(".js-job-link")
temp = open("temp.txt",mode='w')
temp.write(str(input))


temp.close  '''
'''
count = 1
for item in soup.select(".b-block__left "):
    print('======[',count,']=========')
    job_title = item.select(".js-job-link")[0].get_text()#.find('a')
    job_url = item.select(".js-job-link")[0].find('a')['herf']
    print(job_title)
    print("http:") 
    print(job_url)

    print("\n")
    
    count += 1'''



count = 1
for item in soup.select(".b-block__left "):
    print('======[',count,']=========')
    #print(item.select(".js-job-link"))
    tempForItem = str(item.select(".js-job-link"))
    #print(type(tempForItem))    <class 'list'>
    #print(tempForItem)		'''[<a class="js-job-link " href="//www.104.com.tw/job/?jobno=6apc8&amp;jobsource=joblist_a_date" target="_blank">IP CAM/NVR 通訊協定/應用程式工程師</a>]'''
    iteminfor = BeautifulSoup(tempForItem,features="html.parser")
    tempjob_title = iteminfor.get_text()
    print(tempjob_title)
    job_title = tempjob_title[1:len(tempjob_title)-1]
    #tempJob_url = item.find('href')
    #print(tempJob_url['href'])


    print("Job name : ",job_title)  #used!!
    print("\n")
    
    count += 1










