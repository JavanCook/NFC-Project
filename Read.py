#!/usr/bin/env python
# -*- coding: utf8 -*-

#Import necessary modules
import RPi.GPIO as GPIO
import MFRC522
import Adafruit_CharLCD
import signal
import socket
from time import sleep
import os

continue_reading = True

#Setup LED
red = 36
green = 33
blue = 35
GPIO.setmode(GPIO.BOARD)
GPIO.setup([red, green, blue], GPIO.OUT)

#Setup Buttons
switch1in = 31
switch2in = 37
switch1out = 32
switch2out = 38
switch3in = 40
switch3out = 29
GPIO.setup([switch1out, switch2out, switch3out], GPIO.OUT)
GPIO.output([switch1out, switch2out, switch3out], 1)
GPIO.setup([switch1in, switch2in, switch3in], GPIO.IN)

# Capture SIGINT for cleanup when the script is aborted
def end_read(signal,frame):
    global continue_reading
    print "Ctrl+C captured, ending read."
    continue_reading = False
    lcd = Adafruit_CharLCD.Adafruit_CharLCD()
    lcd.clear()
    GPIO.cleanup()

# Hook the SIGINT
signal.signal(signal.SIGINT, end_read)

# Create an object of the class MFRC522
MIFAREReader = MFRC522.MFRC522()

# Welcome message
print "Welcome to the MFRC522 data read script"
print "Press Ctrl-C to stop."

# This loop keeps checking for chips. If one is near it will get the UID and authenticate
while continue_reading:
    #Initializes the screen
    lcd = Adafruit_CharLCD.Adafruit_CharLCD()
    lcd.clear()
    lcd.message("Awaiting\nInput")
    GPIO.output([red, green, blue], 0)
    GPIO.output(blue, 1)

    #Check In Loop
    if GPIO.input(switch1in) == False:
        print("Button 1 Pressed")
        GPIO.output(blue, 0)
        GPIO.output(red, 1)
        sleep(0.3)
        lcd.message("Check In")
        # Scan for cards
        for time1 in range(1, 7):
            number1 = (6 - time1)
            timer1 = "Check In\n{tag}".format(tag=number1)
            lcd.clear()
            lcd.message(timer1)
            sleep(1)
            (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)
            if status == MIFAREReader.MI_OK:
                lcd.clear()
                lcd.message("Card detected")
                print "Card detected"
                sleep(1)
                # Get the UID of the card
                (status,uid) = MIFAREReader.MFRC522_Anticoll()
                # If we have the UID, continue
                if status == MIFAREReader.MI_OK:
                    # This is the default key for authentication [0xFF,0xFF,0xFF,0xFF,0xFF,0xFF]
                    # Select the scanned tag
                    MIFAREReader.MFRC522_SelectTag(uid)
                    # Read the tag and convert to string
                    (nfcbits) = MIFAREReader.MFRC522_Read(7)
                    translated = []
                    for x in range(2,11):
                        translated.append(chr(nfcbits[x]))
                    nfctag = ''.join(translated)
                    joined = "{tag}\nLocation".format(tag=nfctag)
                    web = "{tag}\tLocation".format(tag=nfctag)
                    print joined
                    lcd.clear()
                    lcd.message(joined)
                    sleep(3)
                    #Setup TCP communication
                    connectIP = 'IP to connect to'
                    connectport = 22
                    packetsize = 32
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    attemptlist = []
                    #Check connection to server
                    for x in range(1,6):
                        try:
                            s.connect((connectIP, connectport))
                            s.send('in')
                            ack = s.recv(packetsize)
                            if len(ack) > 1:
                                print 'Connected to server.'
                                lcd.clear()
                                lcd.message('Connection\nEstablished')
                                sleep(2)
                        #Handles refused connection error
                        except socket.error as d:
                            if d.errno == 111:
                                print 'No connection to server, attempt number.', x
                                #attempt connection five times with two second intervals
                                sleep(2)
                                attemptlist.append(x)
                    #Cancels connection if it reaches the limit
                    if len(attemptlist) == 5:
                        print 'Connection failed, please try again.'
                        lcd.clear()
                        lcd.message('Connection\nFailed')
                        sleep(2)
                        break
                    #Send data to host
                    print web
                    s.send(web)
                    lcd.clear()
                    lcd.message('Data\nUploaded')
                    sleep(2)
                    break
            #Cancels check in if tag not found
            elif number1 == 0:
                lcd.clear()
                lcd.message("Check In\nCancelled")
                sleep(2)
                lcd.clear()

    #Check Out Loop
    elif GPIO.input(switch2in) == False:
        print("Button 2 Pressed")
        GPIO.output(blue, 0)
        GPIO.output(green, 1)
        sleep(0.3)
        lcd.message("Check Out")
        # Scan for cards
        for time2 in range(1, 7):
            number2 = (6 - time2)
            timer2 = "Check Out\n{tag}".format(tag=number2)
            lcd.clear()
            lcd.message(timer2)
            sleep(1)
            (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)
            if status == MIFAREReader.MI_OK:
                lcd.clear()
                lcd.message("Card detected")
                print "Card detected"
                sleep(1)
                # Get the UID of the card
                (status,uid) = MIFAREReader.MFRC522_Anticoll()
                # If we have the UID, continue
                if status == MIFAREReader.MI_OK:
                    # This is the default key for authentication [0xFF,0xFF,0xFF,0xFF,0xFF,0xFF]
                    # Select the scanned tag
                    MIFAREReader.MFRC522_SelectTag(uid)
                    # Read the tag and convert to string
                    (nfcbits) = MIFAREReader.MFRC522_Read(7)
                    translated = []
                    for x in range(2,11):
                        translated.append(chr(nfcbits[x]))
                    nfctag = ''.join(translated)
                    joined = "{tag}\nOutgoing".format(tag=nfctag)
                    web = "{tag}\tOutgoing".format(tag=nfctag)
                    print joined
                    lcd.clear()
                    lcd.message(joined)
                    sleep(3)
                    #Setup TCP communication
                    connectIP = 'IP to connect to'
                    connectport = 22
                    packetsize = 32
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    attemptlist = []
                    #Check connection to server
                    for x in range(1,6):
                        try:
                            s.connect((connectIP, connectport))
                            s.send('out')
                            ack = s.recv(packetsize)
                            if len(ack) > 1:
                                print 'Connected to server.'
                                lcd.clear()
                                lcd.message('Connection\nEstablished')
                                sleep(2)
                        #Handles refused connection error
                        except socket.error as d:
                            if d.errno == 111:
                                print 'No connection to server, attempt number.', x
                                #attempt connection five times with two second intervals
                                sleep(2)
                                attemptlist.append(x)
                    #Cancels connection if it reaches the limit
                    if len(attemptlist) == 5:
                        print 'Connection failed, please try again.'
                        lcd.clear()
                        lcd.message('Connection\nFailed')
                        sleep(2)
                        break
                    #Sends data to the host
                    print web
                    s.send(web)
                    lcd.clear()
                    lcd.message('Data\nUploaded')
                    sleep(2)
                    break
            #Cancels check out if tag not found in time limit
            elif number2 == 0:
                lcd.clear()
                lcd.message("Check Out\nCancelled")
                sleep(2)
                lcd.clear()
    #Initiates pi shutdown shutdown
    elif GPIO.input(switch3in) == False:
        print("Button 3 Pressed")
        GPIO.output(blue, 0)
        sleep(0.3)
        print("Shutting Down")
        lcd.clear()
        lcd.message("Shutting\nDown")
        sleep(3)
        lcd.clear()
        os.system('sudo shutdown -h now')

    #Tag Check
    else:
        # Scan for cards
        (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)
        if status == MIFAREReader.MI_OK:
            lcd.clear()
            lcd.message("Card detected")
            print "Card detected"
            sleep(1)
        # Get the UID of the card
        (status,uid) = MIFAREReader.MFRC522_Anticoll()
        # If we have the UID, continue
        if status == MIFAREReader.MI_OK:
            # This is the default key for authentication [0xFF,0xFF,0xFF,0xFF,0xFF,0xFF]
            # Select the scanned tag
            MIFAREReader.MFRC522_SelectTag(uid)
            # Read the tag and convert to string
            (nfcbits) = MIFAREReader.MFRC522_Read(7)
            translated = []
            for x in range(2,11):
                translated.append(chr(nfcbits[x]))
            nfctag = ''.join(translated)
            joined = "Box Number:\n{tag}".format(tag=nfctag)
            print joined
            lcd.clear()
            lcd.message(joined)
            sleep(3)
