#-*- coding: utf-8 -*-
class Person:
	age1 = 1 #類別屬性
	age2 = 2


	#建構子
	def __init__(self,name):
		self.name = name #實例屬性/資料屬性
		self.age1 = 111

	def print_name(self):
		global age3	 #全域變數
		age3 = 40
		name = "bill"  #區域變數
		print "function variable name is "+name
		print "實例屬性:"+self.name


	def print_age(self):
		age3=80
		print "age3 is "+str(age3)
		print "實例屬性 age1 is"+str(self.age1)
		print "類別屬性 age2 is "+str(self.age2)
		
		

#########################
p1 = Person("CCCCCC")
p1.print_name()
p1.print_age()





