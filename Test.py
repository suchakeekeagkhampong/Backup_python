# -*- coding: utf-8 -*-
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(16,GPIO.OUT)
GPIO.setup(19,GPIO.OUT)

pwm18 = GPIO.PWM(18,50)
pwm16 = GPIO.PWM(16,50)
pwm13 = GPIO.PWM(13,50)
pwm19 = GPIO.PWM(19,50)
pwm18.start(0)
pwm16.start(0)
pwm13.start(0)
pwm19.start(0)

while True:
        # Blink LED 4 หลอดพร้อมกัน 5 ครั้ง
        for i in range(0,10):
                GPIO.output(18,GPIO.HIGH)
                GPIO.output(13,GPIO.HIGH)
                GPIO.output(16,GPIO.HIGH)
                GPIO.output(19,GPIO.HIGH)
                time.sleep(0.2)
                GPIO.output(18,GPIO.LOW)
                GPIO.output(13,GPIO.LOW)
                GPIO.output(16,GPIO.LOW)
                GPIO.output(19,GPIO.LOW)
                
    
        #Blink  LED 4 เรียงลำดับจากหลอดที่ 1-4 5 ครั้ง
        for i in range(0,10):
                GPIO.output(18,GPIO.HIGH)
                time.sleep(0.2)
                GPIO.output(18,GPIO.LOW)
                time.sleep(0.2)
                GPIO.output(16,GPIO.HIGH)
                time.sleep(0.2)
                GPIO.output(16,GPIO.LOW)
                time.sleep(0.2)
                GPIO.output(13,GPIO.HIGH)
                time.sleep(0.2)
                GPIO.output(13,GPIO.LOW)
                time.sleep(0.2)
                GPIO.output(19,GPIO.HIGH)
                time.sleep(0.2)
                GPIO.output(19,GPIO.LOW)
                
    
        # Fade LED 4 หลอดพร้อมกัน 5 ครั้ง
        for i in range (0,5):
            for i in range(100):
                pwm18.ChangeDutyCycle(i)
                pwm16.ChangeDutyCycle(i)
                pwm13.ChangeDutyCycle(i)
                pwm19.ChangeDutyCycle(i)
                time.sleep(0.01)
            for i in range(100):
                pwm18.ChangeDutyCycle(100-i)
                pwm16.ChangeDutyCycle(100-i)
                pwm13.ChangeDutyCycle(100-i)
                pwm19.ChangeDutyCycle(100-i)
                time.sleep(0.01)
        
        
        # Fade LED 4 เรียงลำดับจากหลอดที่ 1-4 5 ครั้ง
        for i in range (0,5):
            for i in range(100):
                pwm18.ChangeDutyCycle(i)
                time.sleep(0.01)
            for i in range(100):
                pwm18.ChangeDutyCycle(100-i)
                time.sleep(0.01)
            for i in range(100):
                pwm16.ChangeDutyCycle(i)
                time.sleep(0.01)
            for i in range(100):
                pwm16.ChangeDutyCycle(100-i)
                time.sleep(0.01)
            for i in range(100):
                pwm13.ChangeDutyCycle(i)
                time.sleep(0.01)
            for i in range(100):
                pwm13.ChangeDutyCycle(100-i)
                time.sleep(0.01)
            for i in range(100):
                pwm19.ChangeDutyCycle(i)
                time.sleep(0.01)
            for i in range(100):
                pwm19.ChangeDutyCycle(100-i)
                time.sleep(0.01)

        

            
