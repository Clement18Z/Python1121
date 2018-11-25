#!/usr/bin/python
# -*- coding: UTF-8 -*-


from flask import Flask,redirect,url_for

app=Flask(__name__)


@app.route('/admin')
def hello_admin():
	return "HELLO~ Admin"

@app.route('/guest/<guest>')
def hello_guest(guest):
	return "HELLO~ guest : %s"%guest

@app.route('/user/<name>')
def hello_user(name):
	if name == "admin" :
		return redirect(url_for("hello_admin"))
	else:
		return redirect(url_for("hello_guest",guest =name))




@app.route('/')
def index():
	return "HELLO~"

if __name__ == "__main__":
	app.run(debug=True,host='0.0.0.0')
