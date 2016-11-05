##################################################################################################
# Libraries and functions
##################################################################################################
import cv2
import numpy as np
import socket # imported for function sendimage
import sys
from libc import sendimage
import io
import picamera
###################################################################################################



##################################################################################################
# Important variables
##################################################################################################

##################################################################################################



##################################################################################################
# Other Functions: functions the doesn't fall into categories of other function files are kept
# here. Other reasons for them being here is because of them creating some problems when they
# are in other files. See each functions for explanation why is it here
##################################################################################################

# Start of take image function
# Help from http://rpihome.blogspot.de/2015/03/face-detection-with-raspberry-pi.html
# Why Here: server.py goes crazy on PC when this function is added to functions.py
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
####################################################################################################



##################################################################################################
# Code
##################################################################################################

# Create a TCP/IP socket and connect to ip and port
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('192.168.1.5', 10000))

# Send welcome message, this is just dummy message as first message of socket seems to take longer so just doing it here
sock.sendall('Welcome!!!'.encode())

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

