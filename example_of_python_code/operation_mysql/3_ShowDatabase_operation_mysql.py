#!/usr/bin/python


import mysql.connector

#connect
mydb = mysql.connector.connect(
	host = "localhost",
	user = "root",
	passwd = "1234"
	)
	
mycoursor = mydb.cursor()

mycoursor.execute("SHOW DATABASES")

for x in mycoursor:
	print x

#close
mydb.close()


