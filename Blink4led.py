import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(16,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(19,GPIO.OUT)

#1
GPIO.output(18,GPIO.HIGH)
time.sleep(0.05)
GPIO.output(18,GPIO.LOW)
time.sleep(0.05)
GPIO.output(16,GPIO.HIGH)
time.sleep(0.05)
GPIO.output(16,GPIO.LOW)
time.sleep(0.05)
GPIO.output(13,GPIO.HIGH)
time.sleep(0.05)
GPIO.output(13,GPIO.LOW)
time.sleep(0.05)
GPIO.output(19,GPIO.HIGH)
time.sleep(0.05)
GPIO.output(19,GPIO.LOW)

time.sleep(1)

#2

GPIO.output(18,GPIO.HIGH)
time.sleep(0.05)
GPIO.output(18,GPIO.LOW)
time.sleep(0.05)
GPIO.output(16,GPIO.HIGH)
time.sleep(0.05)
GPIO.output(16,GPIO.LOW)
time.sleep(0.05)
GPIO.output(13,GPIO.HIGH)
time.sleep(0.05)
GPIO.output(13,GPIO.LOW)
time.sleep(0.05)
GPIO.output(19,GPIO.HIGH)
time.sleep(0.05)
GPIO.output(19,GPIO.LOW)

time.sleep(1)

#3

GPIO.output(18,GPIO.HIGH)
time.sleep(0.05)
GPIO.output(18,GPIO.LOW)
time.sleep(0.05)
GPIO.output(16,GPIO.HIGH)
time.sleep(0.05)
GPIO.output(16,GPIO.LOW)
time.sleep(0.05)
GPIO.output(13,GPIO.HIGH)
time.sleep(0.05)
GPIO.output(13,GPIO.LOW)
time.sleep(0.05)
GPIO.output(19,GPIO.HIGH)
time.sleep(0.05)
GPIO.output(19,GPIO.LOW)

time.sleep(1)

#4

GPIO.output(18,GPIO.HIGH)
time.sleep(0.05)
GPIO.output(18,GPIO.LOW)
time.sleep(0.05)
GPIO.output(16,GPIO.HIGH)
time.sleep(0.05)
GPIO.output(16,GPIO.LOW)
time.sleep(0.05)
GPIO.output(13,GPIO.HIGH)
time.sleep(0.05)
GPIO.output(13,GPIO.LOW)
time.sleep(0.05)
GPIO.output(19,GPIO.HIGH)
time.sleep(0.05)
GPIO.output(19,GPIO.LOW)

time.sleep(1)

#5

GPIO.output(18,GPIO.HIGH)
time.sleep(0.05)
GPIO.output(18,GPIO.LOW)
time.sleep(0.05)
GPIO.output(16,GPIO.HIGH)
time.sleep(0.05)
GPIO.output(16,GPIO.LOW)
time.sleep(0.05)
GPIO.output(13,GPIO.HIGH)
time.sleep(0.05)
GPIO.output(13,GPIO.LOW)
time.sleep(0.05)
GPIO.output(19,GPIO.HIGH)
time.sleep(0.05)
GPIO.output(19,GPIO.LOW)
