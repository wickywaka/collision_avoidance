# collision_avoidance
The development repository for my collision avoidance project, these are just the initial files.
This example reads an image from hard drive using opencv and then call the dumps method of nparray to pickle (serialize) the data of this image. It then calls the function sendimage in client to send this image to server. Servers receives the image and calls the mothod numpy.loads to convert the string back to image and dispaly it.

The message is of format: size+image_string
size of 10 bytes and represents the size of image_string in bytes.

## Usage:
First start the server by typing python server.py in command line (linux)
then start the client by typing python client.py in command line (linux)

## Caution
It is important that you use python3 on both sides, otherwise it will throw errors


## OUTPUT


waqar@waqar-HP:~/workspace/git/collision_avoidance$ python server.py 
test print
Connection from 
('192.168.1.45', 33688)
0.8325252532958984
0000230613
The size of image is:
230613
0.20682668685913086
Time for recvimage is:
recimage time is :
1.040318250656128
function finished




pi@pi1:~/workspace/git/collision_avoidance $ python3 client.py 
Function Ended

