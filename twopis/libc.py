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


