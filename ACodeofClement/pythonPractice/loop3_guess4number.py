#!/usr/bin/python
# -*- coding: UTF-8 -*-


guesstime=1
answer="1234"
print "HOW TO PLAY:"
print "B : The number you guess is in the answer,but not in the right place"
print "A : Both place and number is right."
print "For example : "
print "answer = 9876 , guess 9267"
print "Then the output message is '1A2B'."
print "\n"
print "Input 'H' to get -HOW TO PLAY-"
print "Input 'show' to get the guessing history."
print "\n"
print "**********************************************************" 
print "This is the 1 times guessing."
userguess=raw_input("Please guess a number with 4 units.(ex:7524) :")
guessinghistory="--------------history-------------\n"
guessinghistory+= "******times*******|yourguess|result\n"


while True:
  if(userguess==answer):
    if(guesstime==1):
      print "After "+str(guesstime)+" time guessing,you got the answer! The answer is '"+answer+"'. " 
      print "*****************************end**************************" 
    else:
      print "After "+str(guesstime)+" times guessing,you got the answer! The answer is '"+answer+"'. " 
      print "*****************************end**************************" 
    break;
  else: 
    while True:
            
      if len(userguess)!=4:
        if(userguess=="H"):
          print "\n"
          print "-----HOW TO PLAY:-----"
          print "B : The number you guess is in the answer,but not in the right place"
          print "A : Both place and number is right."
          print "For example : "
          print "answer = 9876 , guess 9267"
          print "Then the output message is '1A2B'."
          print "\n"
          
          userguess=raw_input("Please guess a number with 4 units.(ex:7524) :")
          break
        print "Error! Your input is not a 4 units string."
        print "\n"
        userguess=raw_input("Please enter a number with 4 units again.(ex:7524) :")
        break
      
      else: 
        
        numberflag=0
        for i in range(len(userguess)):
          for j in range(10):
            if(str(j) in userguess[i]):
              numberflag+=1 
        if numberflag!=4 :
          if(userguess=="show"):
            print guessinghistory
            print "\n"
            userguess=raw_input("Please guess a number with 4 units.(ex:7524) :")
            break
          print "Error! Your input has some element is not 1-9."
          print "\n"
          userguess=raw_input("Please enter a number with 4 units(1-9) again.(ex:7524) :")
          break      
          #test whether the element in userguess is number of 1-9. 
        countA,countB=0,0
        for i in range(len(userguess)):
          if(userguess[i]==answer[i]):
            countA+=1
          if(userguess[i] in answer):
            countB+=1
        countB-=countA
        print "The result message is %d times of guessing."%guesstime
        print "Your input is :"+userguess+" ,and the message of answer is %dA%dB"%(countA,countB)
        print "**********************************************************"   
        if guesstime==1:
          guessinghistory+="1 time guessing.  |   "+userguess+"  | %dA%dB"%(countA,countB)
        else:
          guessinghistory+="\n"+str(guesstime)+" times guessing. |   "+str(userguess)+"  | "+str(countA)+"A"+str(countB)+"B"  
        guesstime+=1
        
        if guesstime%5==0:
          s=""
          for i in range(52):
            s+="*"
          print "\n\n" 
          print s  
          print "********Maybe input H to get -HOW TO PLAY-?*********"
          print "*****Or input show to get the guessing history.*****"
          print s
          print "\n"     
        print ("\nGuess wrong!This is the %d times guessing.")%guesstime
        userguess=raw_input("Please guess a number with 4 units again.(ex:7524) :")
        break
        
   
   

'''
a = 10
b = 20
list = [1, 2, 3, 4, 5 ];

if ( a in list ):
   print "Line 1 - a is available in the given list"
else:
   print "Line 1 - a is not available in the given list"

if ( b not in list ):
   print "Line 2 - b is not available in the given list"
else:
   print "Line 2 - b is available in the given list"

a = 2
if ( a in list ):
   print "Line 3 - a is available in the given list"
else:
   print "Line 3 - a is not available in the given list"
'''   
