#切割圖片
import cv2
import numpy as np #為解開三維矩陣而引入
import random #亂數

img = cv2.imread('123.jpg')
print(type(img)) #取得img的資料型態

newImg = img[400:150,200:400] #第一個值:高度 #第二個值:寬度
cv2.imshow('img',img)
cv2.imshow('newImg',newImg)
cv2.waitKey(0)