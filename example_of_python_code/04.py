#!/usr/bin/python
#coding=utf-8


list1=["aa",22,3.2,"dd"]
list2=[123,'asdfg']

print list1
print list1[0]
print list1[1:3]
print list1[2:]
print list1*2
print list1+list2


##
#update
list1[2]="update"
print list1

#delete
del list1[2]
print"delete"
print list1


##append
print "append"
list1.append("2.22")
print "append 2.22 in list1"
print list1

#count
print "count 2.22 for list1:",list1.count("2.22")

#sort
list1.sort()
print"sort:",list1



