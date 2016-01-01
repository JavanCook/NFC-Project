#!/usr/bin/env python
# -*- coding: utf8 -*-

import RPi.GPIO as GPIO
import MFRC522
import Adafruit_CharLCD
import signal
from time import sleep

continue_reading = True

#Setup LED
red = 36
green = 33
blue = 35
GPIO.setup([red, green, blue], GPIO.OUT)

#Setup Buttons
switch1in = 31
switch2in = 37
switch1out = 32
switch2out = 38
GPIO.setup([switch1out, switch2out], GPIO.OUT)
GPIO.output([switch1out, switch2out], 1)
GPIO.setup([switch1in, switch2in], GPIO.IN)

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
print "Welcome to the MFRC522 data read example"
print "Press Ctrl-C to stop."

# This loop keeps checking for chips. If one is near it will get the UID and authenticate
while continue_reading:
    #Initializes the screen
    lcd = Adafruit_CharLCD.Adafruit_CharLCD()
    lcd.clear()
    lcd.message("Awaiting\nInput")
    GPIO.output(blue, 1)

    #Check In Loop
    if GPIO.input(switch1in) == False:
        print("Button 1 Pressed")
        sleep(0.3)
        GPIO.output(blue, 0)
        GPIO.output(red, 1)
        lcd.message("Check In")
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
                joined = "{tag}\nBroers Building".format(tag=nfctag)
                print joined
                lcd.clear()
                lcd.message(joined)
                sleep(3)
        else:
            for time1 in range(1, 6)
                lcd.message(time1)
                sleep(1)
            lcd.clear()
            lcd.message("Check In\nCancelled")
            sleep(2)
            lcd.clear()
    #Check Out Loop
    elif GPIO.input(switch2in) == False:
        print("Button 2 Pressed")
        sleep(0.3)
        GPIO.output(blue, 0)
        GPIO.output(green, 1)
        lcd.message("Check Out")
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
                joined = "{tag}\nOutgoing".format(tag=nfctag)
                print joined
                lcd.clear()
                lcd.message(joined)
                sleep(3)
        else:
            for time1 in range(1, 6)
                lcd.message(time1)
                sleep(1)
            lcd.clear()
            lcd.message("Check Out\nCancelled")
            sleep(2)
            lcd.clear()

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
