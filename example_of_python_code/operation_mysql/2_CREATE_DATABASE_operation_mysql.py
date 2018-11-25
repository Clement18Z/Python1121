#!/usr/bin/python


import mysql.connector

#connect
mydb = mysql.connector.connect(
	host = "localhost",
	user = "root",
	passwd = "1234"
	)
	
mycoursor = mydb.cursor()

mycoursor.execute("CREATE DATABASE mydatabase CHARACTER SET utf8 COLLATE utf8_general_ci")

#close
mydb.close()


