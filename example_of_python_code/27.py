#!/usr/bin/python
#coding=utf-8

def add(x,y):
 return x+y

def minus(x,y):
  return x-y
  
def multiply(x,y):
  return x*y
  
def divide(x,y):
  x=float(x)
  y=float(y)
  return x/y
 
def operation(x,y):
  add=x+y
  minus=x-y
  multiply=x*y
  divide=float(x)/float(y)
  return [add,minus,multiply,divide]
 
######################
a,b=2,3
print "a,b=2,3"
num1=add(a,b)
print "add:"+str(num1)
#############
print "*************"
num1=add(2,3)
print "add:"+str(num1)
num2=minus(2,3)
print "minus:"+str(num2)
num3=multiply(2,3)
print "multiply:"+str(num3)
num4=divide(2,3)
print "divide:"+str(num4)
num5=operation(2,3)
print "$$$$$$$$$$$$$$$$$$"
for x in num5:
 print x