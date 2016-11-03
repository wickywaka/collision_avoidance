# collision_avoidance
The development repository for my collision avoidance project, these are just the initial files.
This example reads an image from hard drive using opencv and then call the dumps method of nparray to pickle (serialize) the data of this image. It then calls the function sendimage in client to send this image to server. Servers receives the image and calls the mothod numpy.loads to convert the string back to image and dispaly it.

The message is of format: size+image_string
size of 10 bytes and represents the size of image_string in bytes.

## Usage:
First start the server by typing python server.py in command line (linux)
then start the client by typing python client.py in command line (linux)
