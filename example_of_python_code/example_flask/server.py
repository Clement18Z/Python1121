#!/usr/bin/python
# -*- coding: UTF-8 -*-


from flask import Flask,redirect,url_for,request

app=Flask(__name__)

@app.route('/')
def index():
	return "HELLO~"

@app.route('/success/<name>')
def success(name):
	return "Welcome %s" % name


@app.route('/login',methods=['POST','GET'])
def login():
	if request.method == "POST":
		user = request.form['username']
		#print user
		#return "POST"
		print "POST  ",user
		return redirect(url_for('success',name = user))
		
	else:
		user = request.args.get('username')
		#print str(user)
		#return "GET"
		print "GET  ",user
		return redirect(url_for('success',name = user))
		
		



if __name__ == '__main__':
	app.run(debug=True,host='0.0.0.0')
