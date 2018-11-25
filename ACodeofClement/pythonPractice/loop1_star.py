#!/usr/bin/python
# -*- coding: UTF-8 -*-


level = raw_input("input your level:")
level = int(level)

print "your pyrmid level is %d."%level  
for i in range(level):
  levelresult="" 
  for j in range(level-i-1,0,-1):
    levelresult+=" "
  for j in range(i+1):
    levelresult+="* "
  print levelresult
  
end=""
for i in range(level-1):   
  end+="-"
end+="end"
for i in range(level-1):   
  end+="-" 
print end  
  
  
  
