#!/usr/bin/python
# -*- coding: utf-8 -*

import mysql.connector
from mysql.connector import errorcode
from flask import Flask, redirect, url_for, request


def connectiontomysql(user,value):    
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

      # Drop previous table of same name if one exists
      #cursor.execute("DROP TABLE IF EXISTS inventory;")
      #print "Finished dropping table (if existed)."

      # Create table
      #cursor.execute("CREATE TABLE inventory (id serial PRIMARY KEY, name VARCHAR(50), quantity VARCHAR(20));")
      #print("Finished creating table.")


      sql = "INSERT INTO inventory (name, quantity) VALUES (%s, %s)"
      val = (user, value)
      cursor.execute(sql, val)
      print("WRITE IN Database")
      conn.commit()

      # Cleanup
      cursor.close()
      conn.close()

      print("Done.")





app=Flask(__name__)

@app.route('/')
def hello():
  return "HELLO!"


@app.route('/login',methods = ['POST', 'GET'])
def login():
  if request.method == 'POST':
    user = str(request.form['username'])
    value = str(request.form['Valueofuser'])
    connectiontomysql(user,value)
      #print user
      #return "post"
    print "POST"
    return "OKKKK POST"
  else:
    user = str(request.args.get('username'))
    value = str(request.args.get('Valueofuser'))
    #print user
    #return "get"
    connectiontomysql(user,value)
    print "GET"
    return "okkkk GET"
     

if __name__=='__main__':
  app.run(debug=True,host='0.0.0.0')


