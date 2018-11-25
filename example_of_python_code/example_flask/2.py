#!/usr/bin/env python
# -*- coding: UTF-8 -*-


def print_my_name(name):
	print "I am %s" %(name())

@print_my_name
def my_name():
	return "Hans"

