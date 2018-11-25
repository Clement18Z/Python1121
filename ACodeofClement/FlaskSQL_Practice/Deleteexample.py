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

	#update data
	#cursor.execute("DELETE FROM inventory WHERE name=%(param1)s;", {'param1':'123'} )
	Temp = "DELETE FROM inventory WHERE name='%s';"%('123')
	print Temp
	cursor.execute(Temp)
	print "Delete "+str(cursor.rowcount)+" row(s) of data"
	conn.commit()
	#clean up 
	cursor.close()
	conn.close()

	print "Done!"




