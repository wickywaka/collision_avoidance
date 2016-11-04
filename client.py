##################################################################################################
# Libraries and functions
##################################################################################################
import cv2
import numpy as np
import socket # imported for function sendimage
import sys
from functions import sendimage
from functions import takeimage
#import time
#from picamera.array import PiRGBArray
#from picamera import PiCamera


##################################################################################################
# Important variables
##################################################################################################


##################################################################################################
# Code
##################################################################################################

# Create a TCP/IP socket and connect to ip and port
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('192.168.1.5', 10000))

try:
    # Initialize camera and grab a reference to the raw camera capture
    #camera = PiCamera()
    #rawCapture = PiRGBArray(camera)

    # Allow the camera to warmup
    #time.sleep(0.1)

    # grab an image from the camera
    #camera.capture(rawCapture, format="bgr")
    #image = rawCapture.array
    image = takeimage()

    # Send the image
    #image = cv2.imread('1.jpg')
    sendimage(image, sock)
    print("Function Ended")
finally:
    sock.close()



##################################################################################################
# End of File
##################################################################################################
