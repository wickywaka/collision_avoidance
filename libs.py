##################################################################################################
# Libraries
##################################################################################################
import cv2
import socket
import sys
import numpy as np
import time
import cProfile#, pstats#, StringIO # For profiling

##################################################################################################
# Variables
##################################################################################################

size_header = 10 # Number of bytes representing size of incoming data


##################################################################################################
# Functions
##################################################################################################




####### recvimage function##########
# Thu 03 Nov 2016 04:51:28 AM CET  #
###### Waqar Rashid ################
def recvimage(connection):
    "This function take connection socket as parameter and do the rest of work, returns the image as numpy array, in case of failure returns ()"
    # The first <size_header> bytes contain the size, e.g for 10 it would be b'0010'
    start = time.time()
    data_ = connection.recv(size_header)
    # decode these bytes back to strings, counterpart to client side encoding
    size = data_.decode()
    print(time.time() - start)
    start = time.time()
    print(size)
    if size.isdecimal(): # Check wether the first 4 bytes are decimal
        print("The size of image is:");
        size_ = int(size)
        print(size_)
        data =  connection.recv(4096)
        #end = 0
        while len(data)< size_:
            data +=  connection.recv(4096) # Receive the data specified by first <header_size> bytes)
        print(time.time() - start)
        #print("Data received")
        #print(len(data))
        r_image = np.loads(data)
        return r_image
    else:
        return -1
# End of recvimage Function



##################################################################################################    
# End of Functions
##################################################################################################

