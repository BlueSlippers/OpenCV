import cv2
import numpy as np

img=cv2.imread('C:\Users\Prongs\Downloads\watch.jpg',cv2.IMREAD_COLOR)

pts=np.array([[10,5],[20,25],[70,80],[50,20]],np.int32)
cv2.polylines(img,[pts],True,(125,128,148),4)

font=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'OpenCV',(0,100),font,1,(120,200,56),1,cv2.LINE_AA)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
