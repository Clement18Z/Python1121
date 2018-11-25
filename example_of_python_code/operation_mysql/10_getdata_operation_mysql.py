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

	#read data
	cursor.execute("SELECT * FROM inventory;")
	rows = cursor.fetchall()
	print "Read "+str(cursor.rowcount)+" row(s) of data"

	print type(rows)
	print rows

	#print all rows
	for row in rows:
		print "Data row = (%s,%s,%s)" %(str(row[0]),str(row[1]),str(row[2]))

	#clean up 
	cursor.close()
	conn.close()

	print "Done!"




