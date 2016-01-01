import RPi.GPIO as GPIO
from time import sleep

switch1in = 31
switch2in = 37
switch1out = 32
switch2out = 38

GPIO.setmode(GPIO.BOARD)
GPIO.setup([switch1out, switch2out], GPIO.OUT)
GPIO.output([switch1out, switch2out], 1)
GPIO.setup([switch1in, switch2in], GPIO.IN)

while True:
  if GPIO.input(switch1in) == False:
    print("Button 1 Pressed")
    sleep(0.3)
  elif GPIO.input(switch2in) == False:
    print("Button 2 Pressed")
    sleep(0.3)
  else:
    pass
