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

####### sendimage function##########
# Thu 03 Nov 2016 03:31:40 AM CET  #
# Waqar Rashid #####################

# EDIT: edit this function so that we need to provide a connected socket and an image and it sends it on its own. So we would be able to use one socket and program would get a bit clean.

def sendimage( image, sock ):
    "This function sends image through socket to localhost:10000."
    message = image.dumps()    
    # Making sure the size_header is of correct size
    size = str(len(message))
    if len(size)>size_header:
        raise NameError('Size too big')
    else:
        size = size.zfill(size_header)  # Left fill with zeros to make it of correct size
    # size is string so we need to encode it to bytes    
    sock.sendall(size.encode())         # Default str.encode(encoding="utf-8", errors="strict")
    sock.sendall(message)               # No need to encode message as it is already of type bytes here,
    return
# End of sendimage Function




####### recvimage function##########
# Thu 03 Nov 2016 04:51:28 AM CET  #
###### Waqar Rashid ################
def recvimage(connection):
    "This function take connection socket as parameter and do the rest of work, returns the image as numpy array, in case of failure returns ()"
    # The first <size_header> bytes contain the size, e.g for 10 it would be b'0010'
    #pr = cProfile.Profile()
    #pr.enable()
    start = time.time()
    #data_ = connection.recv(size_header)
    data = connection.recv(4096)
    # decode these bytes back to strings, counterpart to client side encoding
    #size = data_.decode()
    print(time.time() - start)
    start = time.time()    
    #if size.isdecimal(): # Check wether the first 4 bytes are decimal
    #print("The size of image is:");
    #size_ = int(size)
    size_ = 77013
    #print(size_)
    #data =  connection.recv(4096)
    end = 0
    while len(data)< size_:
        data +=  connection.recv(4096) # Receive the data specified by first <header_size> bytes)
    print(time.time() - start)
    print("Data received")
    print(len(data))
    r_image = np.loads(data)
    #pr.disable()
    #pr.dump_stats('profiler.profil')
    return r_image
    #else:
    #    return -1
# End of recvimage Function



##################################################################################################    
# End of Functions
##################################################################################################

