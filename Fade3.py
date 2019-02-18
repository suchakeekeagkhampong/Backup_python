import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
#GPIO.setmode(GPIO.BOARD)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(16,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(19,GPIO.OUT)

pwm18 = GPIO.PWM(18,50)
pwm16 = GPIO.PWM(16,50)
pwm13 = GPIO.PWM(13,50)
pwm19 = GPIO.PWM(19,50)
pwm18.start(0)
pwm16.start(0)
pwm13.start(0)
pwm19.start(0)

for i in range(0,100000):

            for i in range(0,1):
                for i in range(100):
                    pwm16.ChangeDutyCycle(i)
                    pwm13.ChangeDutyCycle(i)
                    time.sleep(0.01)
                for i in range(100):
                    pwm16.ChangeDutyCycle(100-i)
                    pwm13.ChangeDutyCycle(100-i)
                    time.sleep(0.01)
                for i in range(100):
                    pwm18.ChangeDutyCycle(i)
                    pwm19.ChangeDutyCycle(i)
                    time.sleep(0.01)
                for i in range(100):
                    pwm18.ChangeDutyCycle(100-i)
                    pwm19.ChangeDutyCycle(100-i)
                    time.sleep(0.01)

            for i in range(0,1):
                for i in range(100):
                    pwm18.ChangeDutyCycle(i)
                    pwm19.ChangeDutyCycle(i)
                    time.sleep(0.01)
                for i in range(100):
                    pwm18.ChangeDutyCycle(100-i)
                    pwm19.ChangeDutyCycle(100-i)
                    time.sleep(0.01)
                for i in range(100):
                    pwm13.ChangeDutyCycle(i)
                    pwm16.ChangeDutyCycle(i)
                    time.sleep(0.01)
                for i in range(100):
                    pwm13.ChangeDutyCycle(100-i)
                    pwm16.ChangeDutyCycle(100-i)
                    time.sleep(0.01)
            
            for i in range (0,3):
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

            for i in range (0,1):
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

            for i in range (0,1):
                for i in range(100):
                    pwm19.ChangeDutyCycle(i)
                    time.sleep(0.01)
                for i in range(100):
                    pwm19.ChangeDutyCycle(100-i)
                    time.sleep(0.01)
                for i in range(100):
                    pwm13.ChangeDutyCycle(i)
                    time.sleep(0.01)
                for i in range(100):
                    pwm13.ChangeDutyCycle(100-i)
                    time.sleep(0.01)
                for i in range(100):
                    pwm16.ChangeDutyCycle(i)
                    time.sleep(0.01)
                for i in range(100):
                    pwm16.ChangeDutyCycle(100-i)
                    time.sleep(0.01)
                for i in range(100):
                    pwm18.ChangeDutyCycle(i)
                    time.sleep(0.01)
                for i in range(100):
                    pwm18.ChangeDutyCycle(100-i)
                    time.sleep(0.01)

            for i in range (0,3):
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

GPIO.cleanup()
