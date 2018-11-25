#!/usr/bin/python
# -*- coding: utf-8 -*

from flask import Flask, render_template
from flask import request, url_for

import mysql.connector
from mysql.connector import errorcode

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'hello world'

@app.route('/add_data', methods=['GET','POST'])
def add_data():
	if request.method == 'GET':
		name = str(request.args.get('name'))
		quantity = str(request.args.get('quantity'))
	else:
		name = str(request.form['name'])
		quantity = str(request.form['quantity'])

	print name
	print quantity
	#return "OK"	


	# Obtain connection string information from the portal
	config = {
	  'host':'localhost',
	  'user':'root',
	  'password':'1234',
	  'database':'mydatabase'
	}


	# Construct connection string
	try:
	   conn = mysql.connector.connect(**config)
	   print("Connection established")
	except mysql.connector.Error as err:
	  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
	    print("Something is wrong with the user name or password")
	  elif err.errno == errorcode.ER_BAD_DB_ERROR:
	    print("Database does not exist")
	  else:
	    print(err)
	else:
	  cursor = conn.cursor()
	sql_query = ("INSERT INTO inventory (name, quantity) VALUES (%s, %s)")
	cursor.execute(sql_query, (name, quantity))
	conn.commit()
  	print("Inserted",cursor.rowcount,"row(s) of data.")
	#Cleanup
  	cursor.close()
  	conn.close()
  	print("Done.")
	return 'insert_ok!'






if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')