#!/usr/bin/python
# -*- coding: UTF-8 -*-


userinput = raw_input("Please input some number string:")
output=""
for i in range(len(userinput)-1,-1,-1):
	output+=userinput[i]
		
print "After reverse,the string is :"+output


