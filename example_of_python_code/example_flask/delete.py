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

@app.route('/delete_data', methods=['GET','POST'])
def delete_data():
	if request.method == 'GET':
		user_id = str(request.args.get('id'))

	else:
		user_id = str(request.form['id'])


	print user_id
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
	  #cursor.execute("UPDATE inventory SET quantity = %s , name = %s WHERE id = %s;", (quantity,name ,user_id))
	  #sql_query = "UPDATE inventory SET quantity = %s , name = %s WHERE id = %s;"
	  sql_query = "DELETE FROM inventory WHERE id=%s;"
	  cursor.execute(sql_query, (user_id,))
	  conn.commit()
  	  
	  #Cleanup
  	  cursor.close()
  	  conn.close()
  	  print("Done.")
	  return "delete  ok!"






if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')