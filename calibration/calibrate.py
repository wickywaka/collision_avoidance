# File for calibrating usb camera by waqar rashid
# waqarrashid33@gmail.com
# 13 Nov 2016
# Collision avoidance project

import cv2
import numpy as np
import time


#Termination Criteria
criteria = (cv2.TERM_CRITERIA_EPS+ cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)


# Prepare objec points like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
# READ MORE ABOUT THIS PIECE
objp = np.zeros((6*9,3),np.float32) # 9x6 grid 
objp [:,:2] = np.mgrid[0:9,0:6].T.reshape(-1,2)


# Arrays to store object points amd image points for all the images
objpoints =  [] # 3d points in readl world space
imgpoints =[] # 2d points in image place


# To calibrate another camera, change the parameter here
camera1 = cv2.VideoCapture(1)
good_images = 0;
print("Device openend")


while good_images < 10:

    ret1, frame1 = camera1.read()   # TODO: We get old frames often here, try to solve this issue 
                                    # otherwise it will mess up the whole system later as we will be using
                                    # in our main program image acquisition as well.

    gray = cv2.cvtColor(frame1,cv2.COLOR_BGR2GRAY)
    # Find the chess board corners
    cv2.imshow('image', gray)
    #time.sleep(3)
    start = time.time()
    ret, corners = cv2.findChessboardCorners(gray, (9,6),None)
    print(ret)

    # If found add object points, image points (after refining them)
    if ret == True:
        good_images +=1
        objpoints.append(objp)
        
        corners2 = cv2.cornerSubPix(gray, corners, (11,11), (-1,-1), criteria)
        imgpoints.append(corners2)
        
        #Draw and display the corners
        img = cv2.drawChessboardCorners(frame1,(9,6), corners2, ret)
        cv2.imshow('image', img)
        cv2.waitKey()

    print(time.time()-start)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
print("Enough data for calibration.. finding mappings for undistrotions..")

ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1],None,None)

h,  w = img.shape[:2]
newcameramtx, roi=cv2.getOptimalNewCameraMatrix(mtx,dist,(w,h),1,(w,h))

# undistort Method 2
mapx,mapy = cv2.initUndistortRectifyMap(mtx,dist,None,newcameramtx,(w,h),5)

# Code for saving mapx and mapy to disk so that we don't have to compute them again and again. see pickles
print("Writing mapx and mpay to disk")
mapx.dump("mapx.param")
mapy.dump("mapy.param")

print(" Wirint done, for loading use numpy.load(\"mapx.param\")")

#camera0.release()
camera1.release()




cv2.destroyAllWindows()
cv2.waitKey(1)
cv2.waitKey(1)
cv2.waitKey(1)
cv2.waitKey(1)
