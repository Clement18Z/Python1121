#!/usr/bin/python


import mysql.connector
from mysql.connector import errorcode
#connect
config ={
	'host':'localhost',
	'user':'root',
	'passwd':'1234',
	'database':'mydatabase' 
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

	cursor.execute("DROP TABLE IF EXISTS inventory")
	print "Finish dropping table."

	#create table 
	cursor.execute("CREATE TABLE inventory (id serial PRIMARY KEY ,name VARCHAR(50),quantity INT)")
	print "Finish create table."

	#insert some data into table
	cursor.execute("INSERT INTO inventory (name,quantity) VALUES (%s,%s)",("banana",155))
	cursor.execute("INSERT INTO inventory (name,quantity) VALUES (%s,%s)",("apple",200))
	cursor.execute("INSERT INTO inventory (name,quantity) VALUES (%s,%s)",("orange",80))
	print "Insert" , cursor.rowcount , "row(s) of data."
	conn.commit()

	#clean up 
	cursor.close()
	conn.close()

	print "Done!"




