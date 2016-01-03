#Import socket, itertools, GPIO and time
import socket
from time import gmtime, strftime

#Allows multiple connects/disconnects
while True:
    #Setup TCP server
    bindIP = '192.168.1.65'
    bindport = 9235
    packetsize = 70
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((bindIP, bindport))
    s.listen(1)

    #Receive and acknowledge remote connection
    conn, addr = s.accept()
    print('connected')
    print(addr , 'connected', strftime("%a, %d, %b %Y %H:%M:%S", gmtime()))
    ackn = conn.recv(packetsize)
    conn.send(ackn)

    #Control input loop
    while True:
        try:
            data = conn.recv(packetsize)
            conn.send(data)
            print(data)

        #Handles disconnect by peer error
        except socket.error as e:
            if e.errno == 104:
                print(addr , 'disconnected', strftime("%a, %d, %b %Y %H:%M:%S", gmtime()))
                break
