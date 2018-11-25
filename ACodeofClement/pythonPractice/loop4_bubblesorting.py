#!/usr/bin/python
# -*- coding: UTF-8 -*-

List1 = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
 
print "At first,List1="+str(List1) 

 
for i in range(len(List1),0,-1):
	for j in range(0,i-1,1):
		if List1[j]>=List1[j+1]:
			temp=List1[j+1]
			List1[j+1]=List1[j]
			List1[j]=temp
 
print "After bubble sorting,List1="+str(List1)