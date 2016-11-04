##################################################################################################
# Libraries
##################################################################################################

import socket
import sys
import numpy as np
import io
import picamera

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
    data_ = connection.recv(size_header)
    # decode these bytes back to strings, counterpart to client side encoding
    size = data_.decode()
    if size.isdecimal(): # Check wether the first 4 bytes are decimal
        print("The size of image is:");
        size_ = int(size)
        print(size_)
        data =  connection.recv(4096)
        while len(data)< size_:
            data +=  connection.recv(4096) # Receive the data specified by first <header_size> bytes
        print("Data received")
        print(len(data))
        r_image = np.loads(data)
        return r_image
    else:
        return -1
# End of recvimage Function

# Start of take image function
# Help from 
def takeimage():
    " Function to capture image from raspberry pi camera moduel"
    #Create a memory stream so photos doesn't need to be saved in a file
    stream = io.BytesIO()

    #Get the picture (low resolution, so it should be quite fast)
    #Here you can also specify other parameters (e.g.:rotate the image)
    with picamera.PiCamera() as camera:
        camera.resolution = (320, 240)
        camera.capture(stream, format='jpeg')

    #Convert the picture into a numpy array
    buff = np.fromstring(stream.getvalue(), dtype=np.uint8)

    #Now creates an OpenCV image
    image = cv2.imdecode(buff, 1)
    return image


##################################################################################################    
# End of Functions
##################################################################################################

