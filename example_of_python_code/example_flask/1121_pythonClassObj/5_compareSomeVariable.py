#!/usr/bin/python
# -*- coding: UTF-8 -*-

class lists: 
	class_variable = [] #類別變數 
	def __init__(self): 
		self.instance_variable = [] #是實例變數 

# 建立 instance a 與 b 
a = lists()
b = lists() 

# 給類別變數值 
a.class_variable.extend([1,2,3,4,5]) 

# 呼叫 instance a 與 b 
print("call a", a.class_variable) 
print("call b", b.class_variable)



print "#########################"


# 建立 instance c 與 d 
c = lists() 
d = lists()

# 給實例變數值 
c.instance_variable.extend(["a","b","c","d","e"]) 

# 呼叫 instance c 與 d 
print("call c", c.instance_variable) 
print("call d", d.instance_variable) 









