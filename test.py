import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)

red = 36
green = 33
blue = 35
GPIO.setup([red, green, blue], GPIO.OUT)

GPIO.output(red, 1)
sleep(2)
GPIO.output(red, 0)
sleep(1)
GPIO.output(green, 1)
sleep(2)
GPIO.output(green, 0)
sleep(1)
GPIO.output(blue, 1)
sleep(2)
GPIO.output([red, green, blue], 0)

GPIO.cleanup()
