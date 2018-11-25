#!/usr/bin/python
# -*- coding: utf-8 -*

import urllib2,urllib
import json

print "ok"
# response = urllib2.urlopen('http://192.168.63.40:5000/select_id_data')
response = urllib2.urlopen('http://192.168.137.236:5000/select_id_data')
decode = json.load(response)
print "response,decode OK!"
print type(decode)
print decode

