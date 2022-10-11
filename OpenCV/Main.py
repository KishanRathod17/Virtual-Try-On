import cv2
import numpy as np
# x1=int(input("Enter first pixels : "))
# y1=int(input("Enter first pixels : "))
# x2=int(input("Enter first pixels : "))
# y2=int(input("Enter first pixels : "))


image=cv2.imread(r"C:\Users\ratho\OneDrive\Documents\GitHub\Virtual-Try-On\Software Group Project - I\Images\Man 1.jpg")
cv2.imshow("Main",image)

shirt=cv2.imread(r"C:\Users\ratho\OneDrive\Documents\GitHub\Virtual-Try-On\Software Group Project - I\Images\Shirt 1.jpg")
# shirt=cv2.resize(shirt,(x2-x1,y2-y1))    #51 32 439 427 #56 09 420 401
shirt=cv2.resize(shirt,(401-9,420-56))
print(shirt.shape)

#Getting the ROI
r,c,ch=shirt.shape
roi=image[9:r+9,56:c+56]
#cv2.imshow("ROI",roi)
print(roi.shape)



#Creating grayscale image of shirt
shirt_gray=cv2.cvtColor(shirt,cv2.COLOR_BGR2GRAY)
cv2.imshow("1.Gray Shirt",shirt_gray)

#Creating a mask using threshold
#_, mask=cv2.threshold(shirt_gray,50,255,cv2.THRESH_BINARY)
mask=cv2.adaptiveThreshold(shirt_gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
kernel=np.ones((5,5),np.uint8)
cv2.imshow("2.Mask",mask)
#Removing background
mask_inverse=cv2.bitwise_not(mask)
cv2.imshow("3.Mask inverse",mask_inverse)

#Putting mask in image
#image_roi=cv2.bitwise_and(roi,roi,mask = mask_inverse)
#cv2.imshow("Image ROI",image_roi)

#Take only the shirt from the shirt image
only_shirt = cv2.bitwise_and(shirt,shirt,mask = mask_inverse)
cv2.imshow("4.Mask=MaskInv",only_shirt)

# Put logo in ROI and modify the main image
res = cv2.add(roi,only_shirt)
final_output=image


final_output[32:r+32,51:c+51]=res
cv2.imshow("Final Output",final_output)
cv2.imshow("Shirt",shirt)


cv2.waitKey()
cv2.destroyAllWindows()