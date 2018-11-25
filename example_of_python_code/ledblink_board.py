#!/usr/bin/python
#coding=utf-8

import time
import RPi.GPIO as GPIO

LED_PIN=12
GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED_PIN,GPIO.OUT)

try:
  while True:
    print "LED is on"
    GPIO.output(LED_PIN,GPIO.HIGH)
    time.sleep(1)
    print "LED is off"
    GPIO.output(LED_PIN,GPIO.LOW)
    time.sleep(1)
except KeyboardInterrupt:
  GPIO.cleanup()
     
  