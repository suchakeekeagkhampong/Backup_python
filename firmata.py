try:
   from pyfirmata import Arduino, util
except:
    import pip
    pip.main(['install','pyfirmata'])
    from pyfirmata import Arduino, util
import time

board = pyfirmata.Arduino('/dev/ttyUSB0')
pin13 = board.get_pin('d:13:o')

while True:
    time.sleep(1)
    print("on")
    pin13.write(1)
    time.sleep(1)
    print("off")
    pin13.write(0 )    
