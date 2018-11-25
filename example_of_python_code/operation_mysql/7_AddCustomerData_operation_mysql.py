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

sql = "INSERT INTO customers(name,address)VALUES(%s,%s)"
val = ("John","highway 88")

mycursor.execute(sql,val)
mydb.commit()



#close
mydb.close()


