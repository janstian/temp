import RPi.GPIO as GPIO
import time


def blink():
 GPIO.output(11, True)
 time.sleep(1)
 GPIO.output(11, False)
 time.sleep(1)



GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)

while 1:
	blink()



