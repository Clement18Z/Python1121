#!/usr/bin/python


import mysql.connector

#connect
mydb = mysql.connector.connect(
	host = "localhost",
	user = "root",
	passwd = "1234",
	database = "mydatabase" 
	)





#close
mydb.close()


