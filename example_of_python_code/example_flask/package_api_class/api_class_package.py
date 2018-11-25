# -*- coding: UTF-8 -*-
from flask import Flask, render_template
from flask import request, url_for
from module.database import Database


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