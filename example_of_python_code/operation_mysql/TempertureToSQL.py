#!/usr/bin/python
#coding=utf-8

import mysql.connector
from mysql.connector import errorcode
import time,datetime
from time import strftime



'''
##create database for temperture senor
mydb = mysql.connector.connect(
	host = "localhost",
	user = "root",
	passwd = "1234"
	)
	
coursor = mydb.cursor()

cursor.execute("CREATE DATABASE IOT CHARACTER SET utf8 COLLATE utf8_general_ci")
cursor.execute("CREATE TABLE temperature_DB (userid INT,temperature float,datetime datetime);")





#close
mydb.close()

########CREATE DATABASE IOT↑


mydb = mysql.connector.connect(
	host = "localhost",
	user = "root",
	passwd = "1234",
	database = "IOT" 
	)
	
cursor = mydb.cursor()

cursor.execute("ALTER TABLE temperature_DB ADD COLUMN ID INT AUTO_INCREMENT PRIMARY KEY;")

#close
mydb.close()



'''

########for first time run↑


now = strftime("%Y/%m/%d %H:%M:%S")
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
	 
print "now time is:"+ str(now) + "  temperature=" + str(temp)







#connect
config ={
	'host':'localhost',
	'user':'root',
	'passwd':'1234',
	'database':'IOT' 
	}


try:
	conn = mysql.connector.connect(**config)
	print "connection established"

	
except mysql.connector.Error as err:
	if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
		print "something is wrong with user name or password"
	elif err.errno == errorcode.ER_BAD_DB_ERROR:
		print "Database is not exist"
	else:
		print err
else:
	cursor = conn.cursor()

	
	


	#insert some data into table
	cursor.execute("INSERT INTO temperature_DB (userid,datetime,temperature) VALUES (%s,%s,%s)",(14,now,temp))
	print "Insert" , cursor.rowcount , "row(s) of data."
	conn.commit()

	#clean up 
	cursor.close()
	conn.close()

	print "Done!"




