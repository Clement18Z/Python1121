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
mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")




#close
mydb.close()


