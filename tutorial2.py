import cv2
import numpy as np #為解開三維矩陣而引入
import random #亂數

img = cv2.imread('123.jpg')
print(type(img)) #取得img的資料型態
# print(img.shape) #取得陣列的大小
# 影像的資料型態為多維陣列
# 在opencv中顏色的順序為B G R

# img = np.empty((300,300,3),np.uint8) 
# 第一個陣列(參數):指定陣列有幾個維度，每個維度的大小
# 第二個參數:每個值的大小是多少 0~255

for row in range(300): #row 長，col 寬
    for col in range(img.shape[1]): #取得圖片寬度
        img[row][col] = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]

cv2.imshow('img',img)
cv2.waitKey(0)
