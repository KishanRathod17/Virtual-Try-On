
#Function which tell shte coordinates of any pixel and its color

import numpy as np
import cv2



def mouse_event(event,x,y,flags,param):

    font=cv2.FONT_HERSHEY_COMPLEX

    if event==cv2.EVENT_LBUTTONDOWN:
        X="X : "+str(x)
        Y="Y : "+str(y)
        cv2.putText(img,X,(x,y),font,0.5,(15,12,155),1)
        cv2.putText(img,Y,(x,15+y),font,0.5,(15,12,155),1)


cv2.namedWindow(winname="res")
img=cv2.imread(r"C:\Users\ratho\OneDrive\Desktop\Software Group Project - I\Images\Man 2.jpg")
cv2.setMouseCallback("res",mouse_event)

while True:
   # img=cv2.resize(img,(820,900))
    cv2.imshow("res",img)
    if cv2.waitKey(1) & 0xFF == ord('e'):
        break

cv2.destroyAllWindows()