
import cv2
import numpy as np
import matplotlib.pyplot as plt
cap = cv2.VideoCapture('./test.mp4')
object_detector = cv2.createBackgroundSubtractorMOG2(history=100, varThreshold=40)

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame,(900,600))
    cv2.rectangle(frame,(10,10),(100,100),(255,0,0),3)
    blur = cv2.blur(frame,(5,5))
    cv2.imshow('blur',blur)
    
    first_frame = None
    subtract = cv2.subtract(frame,blur)

    first_frame = frame
    frame = cv2.subtract(subtract,first_frame)
    mask = object_detector.apply(first_frame)
    kernel = np.ones((5,5),np.uint8)
    opening = cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernel,iterations=2)
    cv2.imshow('opening',opening)
    
    # first_frame = cv2.addWeighted(subtract,0.5,frame,1,0)
    # first_frame = cv2.addWeighted(first_frame,1,frame,0.5,0)
    # first_frame = cv2.subtract(subtract,first_frame)
    # first_frame = cv2.addWeighted(first_frame,0.5,subtract,1,0)

    # cv2.imshow('frame',first_frame)

    # cv2.imshow('blur',subtract)
    # cv2.imshow('a',frame)
    # if not ret:
    #     break
    # cv2.imshow('video', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()