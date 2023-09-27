import cv2
import numpy as np
import random 

kernel =np.ones((5,5),np.uint8)
kernel1 =np.ones((5,5),np.uint8)
img = cv2.imread("C:\\Users\\ryan0\\OneDrive\\For GitHub\\PYTHON\\images\\02.jpg")
img = cv2.resize(img,(0,0),fx=0.25,fy=0.25)

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(img,(5,5),0)
canny = cv2.Canny(img,400,150)
dilate = cv2.dilate(canny,kernel,iterations=1)
erode = cv2.erode(dilate,kernel1,iterations=1)
ret, threshold = cv2.threshold(gray,120,255,cv2.THRESH_BINARY)

cv2.imshow('img',img)
# cv2.imshow('gray',gray)
cv2.imshow('blur',blur)
cv2.imshow('canny',canny)
cv2.imshow('threshold',threshold)
# cv2.imshow('dilate',dilate)
# cv2.imshow('erode',erode)
cv2.waitKey(0)
#載入摸型
cv2.CascadeClassifier('')





















#BGR

# print(img)
# print(img.shape)
# img = np.empty((300,300,3),np.uint8)

# for row in range(300):
#     for col in range(img.shape[1]):
#         img[row][col]=[255,0,0]
# newImg = img[:300,:200]
# cv2.imshow('img',img)
# cv2.imshow('newImg',newImg)
# cv2.waitKey(0)