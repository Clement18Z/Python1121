#!/usr/bin/python
# -*- coding: utf-8 -*

import mysql.connector
from mysql.connector import errorcode
from flask import Flask, redirect, url_for, request

global TempforreturnWeb 
TempforreturnWeb = ""
def connectiontomysql(user,value,Mode):    
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
      
      if Mode=="INSERT_INTO":
        sql = "INSERT INTO inventory (name, quantity) VALUES (%s, %s);"
        val = (user, value)
        cursor.execute(sql, val)
      elif Mode=="DELETE_FROM":
        sql = "DELETE FROM `inventory` WHERE name='%s';"
        #Temp = "DELETE FROM inventory WHERE name='%s';"%('123')
        #print user
        #val = "("+user+",)"
        val =user
        #print val
        temp = (sql%val)
        #print temp
        cursor.execute(sql%val)
      elif Mode=="UPDATE":
        sql = "UPDATE inventory SET quantity=%s WHERE name=%s;"
        val = (value,user)
        cursor.execute(sql, val)
      elif Mode=="SELECT_FROM":
        #read data
        cursor.execute("SELECT * FROM inventory;")
        rows = cursor.fetchall()
        print "Read "+str(cursor.rowcount)+" row(s) of data"

        #print type(rows)
        #print rows

        #print all rows
        global TempforreturnWeb
        TempforreturnWeb = "\n<br>/  id  |  name  |  quantity  /"
        for row in rows:
        	#print "Data row = (%s,%s,%s)"%(str(row[0]),str(row[1]),str(row[2]))
        	TempforreturnWeb+= "\n<br>/  %s  |  %s  |  %s  /" %(str(row[0]),str(row[1]),str(row[2]))
      print "TempforreturnWeb : "+TempforreturnWeb
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
'''
@app.route('/showselect')
def showselect():
  return '''

@app.route('/login',methods = ['POST', 'GET'])
def login():
  if request.method == 'POST':
    Mode = str(request.form['userMode'])
    user = str(request.form['username'])
    value = str(request.form['Valueofuser'])
    print "POST"
  else:
    user = str(request.args.get('username'))
    value = str(request.args.get('Valueofuser'))
    Mode = str(request.args.get('userMode')) 
    print "GET"

  connectiontomysql(user,value,Mode)  
	#return "OKKKK "+Mode 
  T = "OK ,%s,%s  \n"%(Mode,TempforreturnWeb)
  print "T=",T
  if Mode =="SELECT_FROM":
    return T
  else:
    return "OKKKK "+Mode     	

     

if __name__=='__main__':
  app.run(debug=True,host='0.0.0.0')


