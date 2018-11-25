#!/usr/bin/python
# -*- coding: UTF-8 -*-


from flask import Flask

app=Flask(__name__)

@app.route('/')
def index():
	return "HELLO~"

@app.route('/hello/<name>')
def HELLO(name):
	return "Hello~  %s !" % name


if __name__ == "__main__":
	app.run(debug=True,host='0.0.0.0',port=9000)
