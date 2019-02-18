from gpiozero import LED
import time

led = LED(18)

for i in range(10):
                    led.on(i)
                    time.sleep(0.2)
                    led.off(i)
