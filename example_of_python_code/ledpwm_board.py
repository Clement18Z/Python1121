#!/usr/bin/python
#coding=utf-8

import time
import RPi.GPIO as GPIO

LED_PIN=12
GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED_PIN,GPIO.OUT)
pwm=GPIO.PWM(LED_PIN,50)
#50-> 1/50=0.02
pwm.start(0)

try:
  while True:
    for dc in range(0,101,5):
     print dc
     pwm.ChangeDutyCycle(dc)
     time.sleep(0.2)
     
    for dc in range(100,-1,-5):
     print dc
     pwm.ChangeDutyCycle(dc)
     time.sleep(0.2)
     
except KeyboardInterrupt:
  pwm.stop()
  GPIO.cleanup()
     
  