#!/usr/bin/python
#coding=utf-8

flag = False
name = raw_input("Enter your name:")

if(name == "bill"):
 flag = True
 print "Welcome boss"
else:
 flag = False
 print name
 
if(flag):
 print name,"is my family"
else:
 print "Who are you?"  
   
 