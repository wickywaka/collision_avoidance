# Wed 02 Nov 2016 10:39:36 PM CET 
# Waqar Rashid

# Libraries
import socket
import sys
import numpy as np
import cv2
from functions import recvimage

# Important variables
header_size = 10



##################################

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("test print")

# Bind the socket to the port
sock.bind(('localhost',10000))

while True:
    
    # Listen for incoming connections, put the socket into server mode
    sock.listen(1)

    while True:
        # Wait for a connection, connection is actually different socket
        # on another port ( assigned by the kernel).
        connection, client_address = sock.accept()
        print("Connection from ")
        print(client_address)
        try:
            image = recvimage(connection)
            cv2.imshow("received image", image)
            cv2.waitKey()
            cv2.destroyAllWindows()
            cv2.waitKey(1)
            cv2.waitKey(1)
            cv2.waitKey(1)
            cv2.waitKey(1)
            break
        finally:
            # Clean up the connection
            connection.close()
