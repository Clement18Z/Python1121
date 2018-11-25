#!/usr/bin/python
#coding=utf-8

import time,datetime
from time import strftime
'''
temperature = file("temp.txt","w")

for num in range(5):
	now = strftime("%H:%M:%S")
	#print now
	 
	file = open("/sys/bus/w1/devices/28-0317237e61ff/w1_slave")
	text=file.read()
	file.close
	#print text
	 
	secondline=text.split("\n")[1]
	#print secondline
	 
	tempdata=secondline.split(" ")[9]
	#print tempdata
	temp=float(tempdata[2:])
	#print temp
	temp=temp/1000
	#print temp
	 
	print "now time is:"+ now + "temperature=" + str(temp)
	temperature.write(str(now)+"    "+str(temp))
	temperature.write("\n")
	time.sleep(1)
temperature.close  
'''


temperature = file("temp.txt","w")

#for num in range(5):
now = strftime("%H:%M:%S")
#print now
	 
file = open("/sys/bus/w1/devices/28-0317237e61ff/w1_slave")
text=file.read()
file.close
#print text
	 
secondline=text.split("\n")[1]
#print secondline
	 
tempdata=secondline.split(" ")[9]
#print tempdata
temp=float(tempdata[2:])
#print temp
temp=temp/1000
#print temp
	 
print "now time is:"+ now + "temperature=" + str(temp)
temperature.write(str(now)+"    "+str(temp))
temperature.write("\n")
#time.sleep(1)
temperature.close  