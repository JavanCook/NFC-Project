#Import necessary modules
import socket
from time import gmtime, strftime
import os
import sys

#Allows multiple connects/disconnects
while True:
    #Setup TCP server
    bindIP = '192.168.1.65'
    bindport = 9231
    packetsize = 70
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((bindIP, bindport))
    s.listen(1)

    #Receive and acknowledge remote connection
    conn, addr = s.accept()
    print(addr , 'connected', strftime("%a, %d, %b %Y %H:%M:%S", gmtime()))
    ackn = conn.recv(packetsize)
    conn.send(ackn)

    #Input loop
    while True:
        try:
            #Recieves check in and updates webpage
            if ackn.decode() == 'in':
                data = conn.recv(packetsize)
                conn.send(data)
                decoded = data.decode()
                print(data)
                fd = open('/home/pi/Website/log.md','a')
                old_stdout = sys.stdout
                sys.stdout = fd
                print(decoded, '\tChecked In\t', strftime("%a, %d, %b %Y %H:%M:%S", gmtime()),'\n')
                sys.stdout=old_stdout
                print(decoded, '\tChecked In\t', strftime("%a, %d, %b %Y %H:%M:%S", gmtime()),'\n')
                fd.close()
                os.chdir('/home/pi/Website')
                os.system('./script.sh')
                os.chdir('/home/pi/NFC')
                print(addr , 'disconnected', strftime("%a, %d, %b %Y %H:%M:%S", gmtime()))
                s.close()
                break
            #Recieves check out and updates webpage
            if ackn.decode() == 'out':
                data = conn.recv(packetsize)
                conn.send(data)
                decoded = data.decode()
                print(data)
                fd = open('/home/pi/Website/log.md','a')
                old_stdout = sys.stdout
                sys.stdout = fd
                print(decoded, '\tChecked Out\t', strftime("%a, %d, %b %Y %H:%M:%S", gmtime()),'\n')
                sys.stdout=old_stdout
                print(decoded, '\tChecked Out\t', strftime("%a, %d, %b %Y %H:%M:%S", gmtime()),'\n')
                fd.close()
                os.chdir('/home/pi/Website')
                os.system('./script.sh')
                os.chdir('/home/pi/NFC')
                print(addr , 'disconnected', strftime("%a, %d, %b %Y %H:%M:%S", gmtime()))
                s.close()
                break

        #Handles disconnect by peer error
        except socket.error as e:
            if e.errno == 104:
                print(addr , 'disconnected', strftime("%a, %d, %b %Y %H:%M:%S", gmtime()))
                break
