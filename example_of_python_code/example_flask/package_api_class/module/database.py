import mysql.connector
from mysql.connector import errorcode
import json


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