# Wed 02 Nov 2016 10:39:36 PM CET
# Waqar Rashid

# Libraries
import socket
import sys
import numpy as np
import cv2
from libs import recvimage
import time

# Important variables
header_size = 10



##################################

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("test print")

# Bind the socket to the port
sock.bind(('',10000)) # localhost doesn't work here, it makes listening to otherhost impossible somehow

while True:

    # Listen for incoming connections, put the socket into server mode
    sock.listen(1)

    while True:
        # Wait for a connection, "connection" is actually a different socket
        # on another port ( assigned by the kernel).
        connection, client_address = sock.accept()
        print("Connection from ")
        print(client_address)
        #print(connection.recv(10))
        try:
            start = time.time()
            image = recvimage(connection)
            print("Time for recvimage is:")
            end = time.time()
            #print("recimage time is :")
            print(end-start)
            cv2.imshow("image",image)
            cv2.waitKey()
            cv2.destroyAllWindows()	
            cv2.waitKey(1)
            cv2.waitKey(1)
            cv2.waitKey(1)
            cv2.waitKey(1)
            print("function finished\n\n\n")
            break
        finally:
            # Clean up the connection
            connection.close()
            
# refernece commands            
#sock.setsockopt(socket.SOL_TCP, socket.TCP_NODELAY, 1)
#>>> sock.getsockopt(socket.SOL_TCP, socket.TCP_NODELAY)
