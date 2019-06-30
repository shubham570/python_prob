#!usr/bin/python3

import cv2

# starting camera 
capt= cv2.VideoCapture(0)
#                      first camera


# to check camera is started or not
print(capt.isOpened())


if capt.isOpened() :
    print("Camera is ready to take pictures")
else :
    print("check your web cam drivers ")

# now we can take read input from camera
print(capt.read())  # it will take first picture

status,img = capt.read()
# now showing
cv2.imshow('liveimage',img)
cv2.waitKey(0)


#to close camera
capt.release()
