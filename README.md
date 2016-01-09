NFC Tag Reader with LCD Screen
==============

A headless NFC tag reader with LCD screen using the [MFRC522-python module](https://github.com/mxgxw/MFRC522-python) and the [Adafruit LCD python module](https://github.com/adafruit/Adafruit-Raspberry-Pi-Python-Code) run by a Raspberry Pi.
Can also be used to update a log file hosted on a separate Raspberry Pi and upload the file to Github for Github Pages access.
Features three buttons, one for checking tags in, one for checking tags out and the final button for shutting the Raspberry Pi down, and finally a RGB LED to indicate which state the Reader is in.

## Pins Used

|   Name  | Pin # | Pin Name   |
|---------|-------|------------|
| Check In Button in |  31   | GPIO06      |
| Check In Button out |  32   | GPIO12      |
| Check Out Button in |  37   | GPIO26      |
| Check Out Button out |  38   | GPIO20      |
| Off Button in |  40   |   GPIO21    |
| Off Button out |  29   |   GPIO05    |
| LED Red |   36  | GPIO16      |
| LED Green |   33  | GPIO13      |
| LED Blue |   35  | GPIO19      |
| LED Ground |   34  | Ground      |
| MFRC522 SDA  | 24    | GPIO8      |
| MFRC522 SCK  | 23    | GPIO11     |
| MFRC522 MOSI | 19    | GPIO10     |
| MFRC522 MISO | 21    | GPIO9      |
| MFRC522 IRQ  | None  | None       |
| MFRC522 GND  | 25   | Ground |
| MFRC522 RST  | 22    | GPIO25     |
| MFRC522 3.3V | 17    | 3V3        |
| LCD GND  | 9  | Ground      |
| LCD 5V  | 4    | 5V     |
| LCD Contrast  |  1   |   3V3   |
| LCD RS | 7    | GPIO04     |
| LCD RW |  14   | Ground      |
| LCD E  | 11  | GPIO17       |
| LCD D4  | 12   | GPIO18 |
| LCD D5  | 13    | GPIO27     |
| LCD D6 | 15     | GPIO22        |
| LCD D7  | 16   | GPIO23 |
| LCD LED +ve  | 2  | 5V     |
| LCD LED -ve  | 6    | Ground       |

## Usage
1. Setup SPI-Py and enable the spi_bcm2708 module in raspi-config.
If a different SPI module loads try uncommenting the "spi" parts of /boot/config.txt and rebooting.
2. Wire up the Raspberry Pi as detailed in the table above.
3. Add your internet settings to /etc/networks/interfaces.
4. Add "sudo python /file location/Read.py" to /etc/rc.local to run the Python script at startup.
5. Add script.sh and log.md to the folder where you want log.md to be stored and modify Host.py to reflect this.
6. Update script.sh to push to the desired location.
7. Configure the IPs and ports correctly for Read.py and Host.py and run Host.py on a separate device.

## Requirements
This code requires you to have the [SPI-Py module](https://github.com/lthiery/SPI-Py) installed for the MFRC522 NFC tag reader to work.
