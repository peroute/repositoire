from tkinter import Image
import cv2
import numpy as np
import cvzone
import imutils
from PIL import Image

video = cv2.VideoCapture(0)
#video = cv2.VideoCapture(0)
#Set the dimentions of the video
video.set(3, 1280)
video.set(4, 720)
x= True
#loop so that the video can be captured
while x:
    success, img = video.read()

    # blur the image
    image = cv2.blur(img, (20,20))
    #get lenght and witdth of the video
    lenght, width= image.shape[:2]
    
        
    cv2.imshow("image", image)
    
    image_gray= cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    #define the region of intrest
    region_of_interest_image = image[(lenght//10)*3:(lenght//10)*7, (width//10)*3:(width//10)*7]
    
    
    #show the region of interest
    cv2.imshow('Region of Interest', region_of_interest_image)
    
    # convert to HSV
    hsv= cv2.cvtColor(region_of_interest_image, cv2.COLOR_BGR2HSV)
    
    low_black = np.array([0,0,0])
    
    up_black = np.array([500,500,80])
    
    
    # apply the mask
    mask = cv2.inRange(hsv,low_black,up_black,)
    # find contours in the thresholded image
    thresh = cv2.threshold(mask, 60, 255, cv2.THRESH_BINARY)[1]
    
    edges = cv2.Canny(mask,100,200,)
    
    lines = cv2.HoughLinesP(edges,1,np.pi/180,200)

    
    # show mask
    cv2.imshow('mask',mask)
    
    cv2.waitKey(20)
    
    for c in cnts:
        # know the center of the line
        M = cv2.moments(c)
        #if division by zero occur the car will stop
        try:
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])
        except ZeroDivisionError:
            print('stop')
            continue
        
        # draw the contour and center of the shape on the img
        cv2.drawContours(region_of_interest_image, [c], -1, (0, 255, 0), 2)
        cv2.circle(region_of_interest_image, (cx, cy), 7, (0, 0, 555), -1)
        cv2.putText(region_of_interest_image, "center", (cx - 50, cy - 20),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
        # show the image
        cv2.imshow("imga", region_of_interest_image)
        
        
        #command the car witch direction will it go
        if cx => (lenght//10)*4.5 and cx <= (lenght//10)*5.5
            print('go straight')
        elif cx => (lenght//10)*3 and cx <= (lenght//10)*4.5
            print('turn right')
        elif cx => (lenght//10)*5.5 and cx <= (lenght//10)*7
            print('turn left')
    
            

    
    
    