#從tutorial5做更改 功能:偵測筆的顏色 project1
import cv2
import numpy as np

def empty(v):
    pass

# img = cv2.imread('789.jpg')
# img = cv2.resize(img,(0,0),fx=0.3,fy=0.3)
cap = cv2.VideoCapture(0)

cv2.namedWindow('TrackBar') #建立新的視窗
cv2.resizeWindow('TrackBar',640,320) #設定視窗大小
#參數順序:1.圖片 2.圖片大小

#建立hsv控制條
cv2.createTrackbar('Hue Min', 'TrackBar',0,179,empty) 
cv2.createTrackbar('Hue Max', 'TrackBar',179,179,empty) #建立色調控制條
cv2.createTrackbar('Sat Min', 'TrackBar',0,255,empty) 
cv2.createTrackbar('Sat Max', 'TrackBar',255,255,empty) #建立飽和度控制條
cv2.createTrackbar('Val Min', 'TrackBar',0,255,empty) 
cv2.createTrackbar('Val Max', 'TrackBar',255,255,empty) #建立亮度控制條
#參數順序 1.控制條名稱 2.在哪個視窗 3.初始值 4.最大值 5.函式

while True: #即時取得控制條的改變
    h_min = cv2.getTrackbarPos('Hue Min','TrackBar')
    h_max = cv2.getTrackbarPos('Hue Max','TrackBar')
    s_min = cv2.getTrackbarPos('Sat Min','TrackBar')
    s_max = cv2.getTrackbarPos('Sat Max','TrackBar')
    v_min = cv2.getTrackbarPos('Val Min','TrackBar')
    v_max = cv2.getTrackbarPos('Val Max','TrackBar')
    print(h_min,h_max,s_min,s_max,v_min,v_max)

    ret, img =cap.read() #讀取每幀的圖片
    hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV) #將每幀的圖片轉為hsv
    
    lower = np.array([h_min,s_min,v_min]) 
    upper = np.array([h_max,s_max,v_max])

    mask = cv2.inRange(hsv,lower,upper) #定義顏色範圍的參數
    #lower,upper需要為陣列 
    result = cv2.bitwise_and(img, img, mask=mask)
    #參數順序: 1.圖片 2.圖片 3.過濾出的圖片
    
    cv2.imshow('img',img)
    # cv2.imshow('hsv',hsv)
    cv2.imshow('mask',mask)
    cv2.imshow('result',result)
    cv2.waitKey(1)