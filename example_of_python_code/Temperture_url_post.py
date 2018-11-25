#!/usr/bin/python
#coding=utf-8

import time,datetime
from time import strftime
import urllib


def fetch_data(url,parametric,methon):
	parametric = urllib.urlencode(parametric)
	if methon=="POST":
		f = urllib.urlopen(url,parametric)
	else:
		f = urllib.urlopen(url+"?"+parametric)	
	return(f.read(),f.code)	


file = open("/sys/bus/w1/devices/28-0317237e61ff/w1_slave")
text=file.read()
file.close
secondline=text.split("\n")[1]
tempdata=secondline.split(" ")[9]
temp=float(tempdata[2:])
#print temp
temp=temp/1000
#print temp
	 
print temp

content,response_code = fetch_data(
	"http://192.168.63.6:5000/add_data", #target web server
	{"name":"Clement14","quantity":temp},
	"POST"
	)











