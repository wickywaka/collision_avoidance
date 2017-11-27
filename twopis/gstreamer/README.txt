required: apt-get install v4l-utils

sudo modprobe v4l2loopback

////////////////////////////////////////////////////////////////////////////////////
//Waqar notes   :
================

It requires Kernel headers which can be done by:
sudo apt-get update
sudo apt-get upgrade
uname -r
4.4.26-v7+
sudo apt-get install raspberrypi-kernel-headers

// from v4l2loopback github repo
wget "https://github.com/umlaeute/v4l2loopback/archive/v0.10.0.tar.gz"
tar -xvzf v0.10.0.tar.gz
cd v4l2loopback-0.10.0/
sudo make
sudo make install

sudo modprobe v4l2loopback


sudo apt-get install gstreamer1.0-tools \
  gstreamer1.0-plugins-base \
  gstreamer1.0-plugins-good \
  gstreamer1.0-plugins-bad \
  gstreamer1.0-plugins-ugly

// Now to test the gstream execute the following command, it will generate and display the test video on same system:
gst-launch-1.0 videotestsrc ! autovideosink

// IMPORTANT: DUE TO SOME REASONS THE DISPLAY DOESN'T WORK ON pi1, find out why.
// Now to send this testvideo on network to another system do the following:(Sender)
gst-launch-1.0 videotestsrc ! jpegenc ! rtpjpegpay !udpsink host=target_ip port=5200

// And to display this video on receiver:
gst-launch-1.0 udpsrc port=5200 ! application/x-rtp,encoding-name=JPEG,payload=26 ! rtpjpegdepay ! jpegdec ! autovideosink

// TODO: GET THE OUTPUT FROM RASPBERRPI CAMERA AND FEED IT INTO GSTREAM
Example1:

Sender:
raspivid -n -t 0 -rot 270 -w 960 -h 720 -fps 30 -b 6000000 -o - | gst-launch-1.0 -e -vvvv fdsrc ! h264parse ! rtph264pay pt=96 config-interval=5 ! udpsink host=10.42.0.20 port=5000

Receiver:
gst-launch-1.0 -e -v udpsrc port=5000 ! application/x-rtp, payload=96 ! rtpjitterbuffer ! rtph264depay ! avdec_h264 ! fpsdisplaysink sync=false text-overlay=false
    


////////////////////////////////////////////////////////////////////////////////////

gst-launch-1.0 udpsrc address=127.0.0.1 port=5000 ! application/x-rtp, encoding-name=H264, payload=96 ! rtph264depay ! h264parse ! avdec_h264 ! autovideosink

gst-launch-1.0 v4l2src device=/dev/video1 !  video/x-raw,width=720,height=576 !  x264enc tune=zerolatency byte-stream=true  bitrate=500 threads=2 !  h264parse config-interval=1 !  rtph264pay ! udpsink host=192.168.10.102 port=5000

gst-launch-1.0 v4l2src device=/dev/video1 ! video/x-raw,width=720,height=576 ! jpegenc ! rtpjpegpay ! udpsink host=192.168.10.100 port=5200



Video4Linux Control
v4l2-ctl

--list-devices
> -d /dev/video1		(usbtv)
--list-inputs
> --set-input=0			(Composite)
--list-standards
> --set-standard=5   	(PAL)



---------- TEST ----------------
# stream to video dummy device
clear && gst-launch-1.0 udpsrc address=192.168.10.70 port=5000 ! application/x-rtp, encoding-name=H264, payload=96 ! rtph264depay ! h264parse ! avdec_h264 ! v4l2sink device=/dev/video2

# start server
clear && gst-launch-1.0 udpsrc address=192.168.10.70 port=5000 ! application/x-rtp, encoding-name=H264, payload=96 ! rtph264depay ! h264parse ! avdec_h264 ! v4l2sink device=/dev/video2

# start client
clear && python client.py

---------- LINKS ---------------
https://petersopus.wordpress.com/tag/v4l2/
http://ivtvdriver.org/index.php/V4l2-ctl
http://www.linuxtv.org/downloads/legacy/video4linux/API/V4L2_API/spec-single/v4l2.htm
http://www.z25.org/static/_rd_/videostreaming_intro_plab/
https://developer.ridgerun.com/wiki/index.php/Introduction_to_network_streaming_using_GStreamer
http://cgit.freedesktop.org/~slomo/gst-sdk-tutorials/

http://web.archive.org/web/*/https://developer.android.com/tools/sdk/ndk/index.html
https://dl.google.com/android/ndk/android-ndk-r9d-linux-x86.tar.bz2
