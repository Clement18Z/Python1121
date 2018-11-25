class Person:
	def __init__(self,name,age):
		self.name = name
		self.age = age
	def myfunction(self):
		print "Hello,my name is "+self.name		

p1 = Person("jack",100)

print p1.name
print p1.age	
p1.myfunction()