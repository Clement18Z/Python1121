# -*- coding: UTF-8 -*-
from flask import Flask, render_template
from flask import request, url_for

import mysql.connector
from mysql.connector import errorcode
import json

app = Flask(__name__)

###########################################################################
#class 
class Database:
	def connect(self):
		# Obtain connection string information from the portal
		config = {
		'host':'localhost',
		'user':'root',
		'password':'1234',
		'database':'mydatabase'
		}
		try:
			print("Connection established")
			return mysql.connector.connect(**config)
		except mysql.connector.Error as err:
			if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
				print("Something is wrong with the user name or password")
			elif err.errno == errorcode.ER_BAD_DB_ERROR:
				print("Database does not exist")
			else:
				print(err)


	def execute(self,sql_query,parameter):
		print "execute."
		conn = Database.connect(self)
		cursor = conn.cursor()

		cursor.execute(sql_query,parameter)
		conn.commit()

		cursor.close()
		conn.close()

	def execute_select(self,sql_query):
		print "execute_select."
		conn = Database.connect(self)
		cursor = conn.cursor(dictionary=True)

		try:
			cursor.execute(sql_query)
			rows =cursor.fetchall()
		
			#Cleanup
		  	cursor.close()
		  	conn.close()
			dataString = json.dumps(rows)
			return dataString
		except:
			conn.close()
			return "ERROR"






###########################################################################
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
	db = Database()
	sql_query = ("INSERT INTO inventory (name, quantity) VALUES (%s, %s)")
	db.execute(sql_query,(name,quantity))
	return "Insert OK!<br>name="+name+"<br>quantity="+quantity


@app.route('/update_data', methods=['GET','POST'])
def update_data():
	if request.method == 'GET':
		user_id = str(request.args.get('id'))
		name = str(request.args.get('name'))
		quantity = str(request.args.get('quantity'))
	else:
		user_id = str(request.form['id'])
		name = str(request.form['name'])
		quantity = str(request.form['quantity'])

	db = Database()
	sql_query = ("UPDATE inventory SET quantity = %s , name = %s WHERE id = %s;")
	db.execute(sql_query,(quantity, name,user_id))
	return "UPDATE OK!<br>name="+name+"<br>quantity="+quantity+"<br>user_ID="+user_id


@app.route('/delete_data', methods=['GET','POST'])
def delete_data():
	if request.method == 'GET':
		user_id = str(request.args.get('id'))

	else:
		user_id = str(request.form['id'])


	db = Database()
	sql_query = "DELETE FROM inventory WHERE id=%s;"
	db.execute(sql_query,(user_id,))
	return "DELETE OK!<br>ID="+user_id


@app.route('/select_data', methods=['GET','POST'])
def select_data():	
	if request.method == 'GET':
		user_id = str(request.args.get('id'))
	else:
		user_id = str(request.form['id'])

	db = Database()
	#sql_query = ("SELECT * FROM inventory;")
	sql_query = ("SELECT * FROM inventory WHERE id=%s;")%(user_id)

	
	dataString  = db.execute_select(sql_query)
	return dataString


if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')