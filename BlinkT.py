import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(16,GPIO.OUT)
GPIO.setup(19,GPIO.OUT)

for i in range(0,10000):
            for i in range(0,2):
                GPIO.output(18,GPIO.HIGH)
                GPIO.output(16,GPIO.HIGH)
                GPIO.output(13,GPIO.HIGH)
                GPIO.output(19,GPIO.HIGH)
                time.sleep(0.05)
                GPIO.output(18,GPIO.LOW)
                GPIO.output(16,GPIO.LOW)
                GPIO.output(13,GPIO.LOW)
                GPIO.output(19,GPIO.LOW)
                time.sleep(0.3)
                
            for i in range(0,20):
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

                GPIO.output(19,GPIO.HIGH)
                time.sleep(0.05)
                GPIO.output(19,GPIO.LOW)
                time.sleep(0.05)
                GPIO.output(13,GPIO.HIGH)
                time.sleep(0.05)
                GPIO.output(13,GPIO.LOW)
                time.sleep(0.05)
                GPIO.output(16,GPIO.HIGH)
                time.sleep(0.05)
                GPIO.output(16,GPIO.LOW)
                time.sleep(0.05)
                GPIO.output(18,GPIO.HIGH)
                time.sleep(0.05)
                GPIO.output(18,GPIO.LOW)

            for i in range(0,2):
                GPIO.output(18,GPIO.HIGH)
                GPIO.output(16,GPIO.HIGH)
                GPIO.output(13,GPIO.HIGH)
                GPIO.output(19,GPIO.HIGH)
                time.sleep(0.05)
                GPIO.output(18,GPIO.LOW)
                GPIO.output(16,GPIO.LOW)
                GPIO.output(13,GPIO.LOW)
                GPIO.output(19,GPIO.LOW)
                time.sleep(0.3)

            for i in range(0,10):
                GPIO.output(16,GPIO.HIGH)
                GPIO.output(13,GPIO.HIGH)
                time.sleep(0.05)
                GPIO.output(16,GPIO.LOW)
                GPIO.output(13,GPIO.LOW)
                time.sleep(0.05)
                GPIO.output(18,GPIO.HIGH)
                GPIO.output(19,GPIO.HIGH)
                time.sleep(0.05)
                GPIO.output(18,GPIO.LOW)
                GPIO.output(19,GPIO.LOW)

                GPIO.output(18,GPIO.HIGH)
                GPIO.output(19,GPIO.HIGH)
                time.sleep(0.05)
                GPIO.output(18,GPIO.LOW)
                GPIO.output(19,GPIO.LOW)
                time.sleep(0.05)
                GPIO.output(16,GPIO.HIGH)
                GPIO.output(13,GPIO.HIGH)
                time.sleep(0.3)

