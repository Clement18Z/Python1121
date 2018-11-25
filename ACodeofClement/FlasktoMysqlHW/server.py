#!/usr/bin/python
#coding=utf-8

from flask import Flask, redirect, url_for, request
#from flask import Flask, redirect, url_for, request
app=Flask(__name__)


@app.route('/')
def index():
	return "Hello world"

@app.route('/success/<name>')
def success(name):
	return "welcome %s" % name


@app.route('/login',methods = ['POST', 'GET'])
def login():
	if request.method == 'POST':
		user = request.form['username']
		return redirect(url_for('success',name = user))
		#print user
		#return "post"
	else:
		user = request.args.get('username')
		#print user
		#return "get"
		return redirect(url_for('success',name = user))

if __name__=='__main__':
	app.run(debug=True,host='0.0.0.0')