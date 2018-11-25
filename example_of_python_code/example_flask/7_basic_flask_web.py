#!/usr/bin/python
# -*- coding: UTF-8 -*-


from flask import Flask

app=Flask(__name__)

@app.route('/')
def index():
	return "HELLO~"


if __name__ == "__main__":
	app.run(debug=True,host='0.0.0.0')
