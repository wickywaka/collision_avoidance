import cv2
import numpy as np
import time
import calibration

# important variables
rows = 6
columns = 9
square_size = 2.85
index = 0
camera0 = cv2.VideoCapture(0)
camera1 = cv2.VideoCapture(1)


print("Device openend")

# Loop for taking pictures and detecting corners
while index<20:

    # Taking pictures
    ret0, frame0 = camera0.read()
    ret1, frame1 = camera1.read()
    #height0, width0, channels0 = frame0.shape
    #height1, width1, channels1 = frame1.shape
    cv2.imshow('picture from camera 0', frame0)
    cv2.imshow('picture from camera 1', frame1)

    # StereoCalibration part Press "c" to activate this part
    if cv2.waitKey(1) & 0xFF == ord('c'):
        # Write these into variables
        print("Performing Calibration")
        # Create calibrator object
        calibrator = calibration.StereoCalibrator(rows, columns, square_size, (480,640))
        calibrator.add_corners((frame1,frame0), show_results=True)  #Bug: dcon't increment index if corners are not found.
                                                                    # It throws an error if corners are not found.
        print("Calibration Function returned")
        index +=1
        print(index)
    #time.sleep(3)
    elif cv2.waitKey(1) & 0xFF == ord('q'):
        break
# Actual Calibration
calibration =calibrator.calibrate_cameras()

print("Average Error is:")
print(calibrator.check_calibration(calibration))
calibration.export("result")
print("Result saved...")


camera0.release()
camera1.release()
cv2.destroyAllWindows()
cv2.waitKey(1)
cv2.waitKey(1)
cv2.waitKey(1)
cv2.waitKey(1)
cv2.waitKey(1)
cv2.waitKey(1)
cv2.waitKey(1)
cv2.waitKey(1)
