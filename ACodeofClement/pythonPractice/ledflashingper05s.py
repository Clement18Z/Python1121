#!/usr/bin/python
# -*- coding: UTF-8 -*-


import time
import RPi.GPIO as GPIO

GPIO.setwarnings(False) 
LED_G,LED_R=12,32
GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED_G,GPIO.OUT)
GPIO.setup(LED_R,GPIO.OUT)


                                        
try:
  for i in range(10):
    print "LED is on"
    GPIO.output(LED_G,GPIO.HIGH) 
    GPIO.output(LED_R,GPIO.HIGH)
    time.sleep(0.5)
    print "LED is off"
    GPIO.output(LED_G,GPIO.LOW)
    GPIO.output(LED_R,GPIO.LOW)
    time.sleep(0.5)
    
except KeyboardInterrupt:
  GPIO.cleanup()