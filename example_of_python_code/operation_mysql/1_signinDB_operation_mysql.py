#!/usr/bin/python
# -*- coding: UTF-8 -*-

import mysql.connector

#connect
mydb = mysql.connector.connect(
	host = "localhost",
	user = "root",
	passwd = "1234"
	)
	
print(mydb)

#close
mydb.close()


