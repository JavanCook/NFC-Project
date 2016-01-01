<<<<<<< HEAD
MFRC522-python
==============

A small class to interface with the NFC reader Module MFRC522 on the Raspberry Pi.

This is a Python port of the example code for the NFC module MF522-AN.

##Requirements
This code requires you to have SPI-Py installed from the following repository:
https://github.com/lthiery/SPI-Py

##Examples
This repository includes a couple of examples showing how to read, write, and dump data from a chip. They are thoroughly commented, and should be easy to understand.

## Pins
You can use [this](http://i.imgur.com/y7Fnvhq.png) image for reference.

| Name | Pin # | Pin name   |
|------|-------|------------|
| SDA  | 24    | GPIO8      |
| SCK  | 23    | GPIO11     |
| MOSI | 19    | GPIO10     |
| MISO | 21    | GPIO9      |
| IRQ  | None  | None       |
| GND  | Any   | Any Ground |
| RST  | 22    | GPIO25     |
| 3.3V | 1     | 3V3        |

##Usage
Import the class by importing MFRC522 in the top of your script. For more info see the examples.
=======
SPI-Py: Hardware SPI as a C Extension for Python
======

COPYRIGHT (C) 2012 Louis Thiery. All rights reserved. Further work by Connor Wolf.

This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License V2 as published by the Free Software Foundation.

LIABILITY  
This program is distributed for educational purposes only and is no way suitable for any particular application,
especially commercial. There is no implied suitability so use at your own risk!
>>>>>>> 155a23f364e4d5c2fc8c54ff504a2bd1497ba4c7
