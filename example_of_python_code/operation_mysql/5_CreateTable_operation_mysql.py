#!/usr/bin/python


import mysql.connector

#connect
mydb = mysql.connector.connect(
	host = "localhost",
	user = "root",
	passwd = "1234",
	database = "mydatabase" 
	)

mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE customers (name VARCHAR(255),address VARCHAR(255))")




#close
mydb.close()


