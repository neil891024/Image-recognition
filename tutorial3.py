#影像處理常用函式
import cv2
import numpy as np
 
kernel = np.ones((1,1),np.uint8) #kernel越大，膨脹效果越好
kernel1 = np.ones((10,10),np.uint8) 

img = cv2.imread('123.jpg')
img = cv2.resize(img,(0, 0),fx=0.5,fy=0.5)
#調整影像的大小(長寬比)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #將圖片轉為灰階圖片
blur = cv2.GaussianBlur(img,(11,11),0) #高斯模糊
#第一個參數:圖片
#第二個參數:高斯核內的數(1,1)只能為奇數，數字越大圖片越模糊
#第三個參數:標準差

canny = cv2.Canny(img,20,200) #找出圖片的邊緣
#第一個參數:圖片 第二個參數:最低門檻值 第三個參數:最高門檻值
#門檻值越低，找到的邊緣會更多

dilate = cv2.dilate(canny,kernel,iterations=1) #膨脹，線條變粗
#第一個參數:圖片 第二個參數:二維陣列 第三個參數:膨脹幾次

erode = cv2.erode(dilate,kernel,iterations=1) #侵蝕，線條變細
#第一個參數:圖片 第二個參數:二維陣列 第三個參數:侵蝕幾次

# cv2.imshow('img',img)
# cv2.imshow('gray',gray)
# cv2.imshow('blur',blur)
# cv2.imshow('canny',canny)
# cv2.imshow('dilate',dilate)
# cv2.imshow('erode',erode)
cv2.waitKey(0)