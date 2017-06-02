import cv2
import numpy as np

cap=cv2.VideoCapture(0)

while True:
    ret,frame=cap.read()
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    lower_red=np.array([0,100,100])
    upper_red=np.array([255,255,255])

    kernel=np.ones((15,15),np.float32)/225
    

    mask=cv2.inRange(hsv,lower_red,upper_red)
    res=cv2.bitwise_and(frame,frame,mask=mask)
    smoothed=cv2.filter2D(res,-1,kernel)

    cv2.imshow('res',res)
    cv2.imshow('smoothed',smoothed)

    
    k=cv2.waitKey(5) & 0xFF
    if(k==27):
        break

cv2.destroyAllWindows()
cap.release()            

        
    
    
