import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(16,GPIO.OUT)
GPIO.setup(19,GPIO.OUT)

while 1:
        #1
        GPIO.output(18,GPIO.HIGH)
        GPIO.output(13,GPIO.HIGH)
        GPIO.output(16,GPIO.HIGH)
        GPIO.output(19,GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(18,GPIO.LOW)
        GPIO.output(13,GPIO.LOW)
        GPIO.output(16,GPIO.LOW)
        GPIO.output(19,GPIO.LOW)
        time.sleep(0.5)

        #2
        GPIO.output(18,GPIO.HIGH)
        GPIO.output(13,GPIO.HIGH)
        GPIO.output(16,GPIO.HIGH)
        GPIO.output(19,GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(18,GPIO.LOW)
        GPIO.output(13,GPIO.LOW)
        GPIO.output(16,GPIO.LOW)
        GPIO.output(19,GPIO.LOW)
        time.sleep(0.5)

        #3
        GPIO.output(18,GPIO.HIGH)
        GPIO.output(13,GPIO.HIGH)
        GPIO.output(16,GPIO.HIGH)
        GPIO.output(19,GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(18,GPIO.LOW)
        GPIO.output(13,GPIO.LOW)
        GPIO.output(16,GPIO.LOW)
        GPIO.output(19,GPIO.LOW)
        time.sleep(0.5)

        #4
        GPIO.output(18,GPIO.HIGH)
        GPIO.output(13,GPIO.HIGH)
        GPIO.output(16,GPIO.HIGH)
        GPIO.output(19,GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(18,GPIO.LOW)
        GPIO.output(13,GPIO.LOW)
        GPIO.output(16,GPIO.LOW)
        GPIO.output(19,GPIO.LOW)
        time.sleep(0.5)

        #5
        GPIO.output(18,GPIO.HIGH)
        GPIO.output(13,GPIO.HIGH)
        GPIO.output(16,GPIO.HIGH)
        GPIO.output(19,GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(18,GPIO.LOW)
        GPIO.output(13,GPIO.LOW)
        GPIO.output(16,GPIO.LOW)
        GPIO.output(19,GPIO.LOW)
        time.sleep(0.5)

        #6
        GPIO.output(18,GPIO.HIGH)
        GPIO.output(13,GPIO.HIGH)
        GPIO.output(16,GPIO.HIGH)
        GPIO.output(19,GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(18,GPIO.LOW)
        GPIO.output(13,GPIO.LOW)
        GPIO.output(16,GPIO.LOW)
        GPIO.output(19,GPIO.LOW)
        time.sleep(0.5)

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
        time.sleep(0.05)

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
        time.sleep(0.05)

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
        time.sleep(0.05)

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
        time.sleep(0.05)

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
        time.sleep(0.05)

        #6
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
        time.sleep(0.05)