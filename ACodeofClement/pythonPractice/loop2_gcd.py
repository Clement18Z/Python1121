#!/usr/bin/python
# -*- coding: UTF-8 -*-




#x="True" if 'a'=='a' else "False"  
#print x  
#result: True


a1 = raw_input("Please input an integer as 'a':")
a=int(a1)
while a<0: 
  print "Error,please input again!"
  a1 = raw_input("Please input an integer as 'a':")
  a=int(a1)
  
b1 = raw_input("Please input an integer as 'b':")
b=int(b1)
while b<0: 
  print "Error,please input again."
  b1 = raw_input("Please input an integer as 'b':")
  b=int(b1)

print "a=%d,b=%d"%(a,b)

'''
if a>=b:
  a,b=a,b
else:
  a,b=b,a #let a is the bigger one.
#print "after opreation,a=%d,b=%d"%(a,b)
'''

'''
def gcd(x,y): #for x>y(int)
  while x%y>=1:
    if x%y>1 :
      x,y=y,x%y
    elif x%y==1:
      return 1
    elif x%y==0:
      return float(x)/float(y)
result=gcd(a,b)
print str(result)
'''

def gcd(a,b): 
  while b:
    a,b=b,a%b
  return a     

print "gcd(%d,%d) = %d"%(a,b,gcd(a,b))





  