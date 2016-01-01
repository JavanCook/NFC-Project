# Scan for cards
  (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)

  # If a card is found
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
