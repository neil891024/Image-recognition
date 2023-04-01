#畫圖形、寫字
import cv2
import numpy as np

img = np.zeros((600,600,3),np.uint8) #顯示出黑色 np.uint8每個值為幾個bit
# cv2.line(img,(0,0),(400,300),(0,255,0),2)
#參數順序 1.圖片 2.起始點 3.結束點 4.顏色 5.線條粗細

cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),2) #畫直線
#img.shape[1] 圖片的寬度 img.shape[0] 圖片的高度

cv2.rectangle(img,(0,0),(400,300),(0,0,255),cv2.FILLED) #畫方形
cv2.circle(img,(300,400),30,(255,0,0),cv2.FILLED)
#參數順序 1.圖片 2.中心點 3.半徑 4.顏色 5.線條粗細
cv2.putText(img,'Hello',(100,500),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
#參數順序 1.圖片 2.文字 3.文字的座標(文字左下角) 4.文字字體 
# 5.字體大小 6.字體顏色 7.文字粗度
# putText函式不支援中文

cv2.imshow('img',img)
cv2.waitKey(0)
