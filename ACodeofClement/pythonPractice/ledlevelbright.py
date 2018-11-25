#!/usr/bin/python
# -*- coding: UTF-8 -*-


import time
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
LED_R,LED_G=12,32
GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED_R,GPIO.OUT)
GPIO.setup(LED_G,GPIO.OUT)

############### 1 sloution
pwm1=GPIO.PWM(LED_R,100)
pwm2=GPIO.PWM(LED_G,100)
#100-> 1/100=0.01

pwm1.start(0)
pwm2.start(0)

try:
	while True:
	    dc = raw_input("Please input pwm level(1-100):")
	    print str(dc)+" level"
	    
	    pwm1.ChangeDutyCycle(int(dc))
	    print "Set red light as "+dc+" level."

	    pwm2.ChangeDutyCycle(int(dc))
	    print "Set green light as "+dc+" level."
    
    
except KeyboardInterrupt:
	GPIO.cleanup()


###################### 2 sloution

"""
try:
  while True:
	dc = raw_input("Please input pwm level(1-100):")
	print dc+" pwm level."
	for i in range(0,401,1):
  		GPIO.output(LED_G,GPIO.HIGH) 
  		GPIO.output(LED_R,GPIO.HIGH)
  		time.sleep(float(dc)/10000)
  		GPIO.output(LED_G,GPIO.LOW)
  		GPIO.output(LED_R,GPIO.LOW)
  		time.sleep((100-float(dc))/10000)
        if i%100==0:
        	print str(i/100)+" sec."
except KeyboardInterrupt:
	GPIO.cleanup()
 """
                                        
