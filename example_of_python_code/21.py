#!/usr/bin/python
#coding=utf-8

for num in range(10,21):
  for i in range(2,num/2+1):
    if(num%i==0):
     print "%d is not a prime,%d=%d * %d"%(num,num,i,num/i)
     break
  else:
   print "%d is prime."%num      