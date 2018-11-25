#!/usr/bin/env python
# -*- coding: UTF-8 -*-

def print_my_name(name):
	print "I am %s" %(name())

def my_name():
	return "Hans"

my_name = print_my_name(my_name)


