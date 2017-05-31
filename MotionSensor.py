import cv2

def diffimg(a,b,c):
    t0=cv2.absdiff(a,b)
    t1=cv2.absdiff(b,c)
    t3=cv2.bitwise_and(t0,t1)
    return t3

cap=cv2.VideoCapture(0)
t=cap.read()[1]
tx=cap.read()[1]
ty=cap.read()[1]

t=cv2.cvtColor(t,cv2.COLOR_BGR2GRAY)
tx=cv2.cvtColor(tx,cv2.COLOR_BGR2GRAY)
ty=cv2.cvtColor(ty,cv2.COLOR_BGR2GRAY)

while True:
    img=diffimg(t,tx,ty)
    cv2.imshow("Motion Detect",img)
    res,img=cap.read() 
    t=tx
    tx=ty
    ty=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    key=cv2.waitKey(10)

    if(key==27):
        cap.release()
        cv2.destroyAllWindows()
        break
