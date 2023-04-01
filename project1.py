#虛擬筆 步驟 1.取得鏡頭影像 2.做顏色偵測 3.偵測筆的輪廓
import cv2
import numpy as np

cap = cv2.VideoCapture(0) #開啟攝像頭，取得攝像頭的影像

#紫 紅 藍
penColorHSV = [[124,95,90,157,153,166], 
               [0,196,150,10,255,255],
               [101,145,53,179,255,255]]

penColorBGR = [[128,0,128], #設定筆尖顏色
               [0,0,255],
               [255,0,0]]

#[x,y,colorID]
drawPoints = []

def findPen(img): #做顏色偵測
    hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV) #將每幀的圖片轉為hsv

    for i in range(len(penColorHSV)): #抓取不同的顏色
        lower = np.array([penColorHSV[i][0:3]]) 
        upper = np.array([penColorHSV[i][3:6]])

        mask = cv2.inRange(hsv,lower,upper) #定義顏色範圍的參數
        result = cv2.bitwise_and(img, img, mask=mask)

        penx,peny = findContour(mask) 
        cv2.circle(imgContour,(penx,peny),10,penColorBGR[i],cv2.FILLED) #畫出筆尖
        if peny != -1: #紀錄座標
            drawPoints.append([penx,peny,i])

        findContour(mask)
        #cv2.imshow('result',result)

def findContour(img): #偵測筆的輪廓
    contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE) #檢測輪廓
    x,y,w,h = -1,-1,-1,-1 #讓總面積能大於500

    for cnt in contours:
        #cv2.drawContours(imgContour,cnt,-1,(255,0,0),4)
        area = cv2.contourArea(cnt) #畫出輪廓的面積
        if area > 500:
            peri = cv2.arcLength(cnt,True)
            vertices = cv2.approxPolyDP(cnt,peri*0.02,True)
            #回傳多邊形的頂點
            x,y,w,h = cv2.boundingRect(vertices) 

    return x+w//2,y #回傳筆尖座標

def draw(drawpoints):
    for point in drawpoints:
        cv2.circle(imgContour,(point[0],point[1]),10,penColorBGR[point[2]],cv2.FILLED) #畫出筆尖


while True:
    ret,frame = cap.read() #會回傳兩個值
    if ret: #取得圖片成功
        imgContour = frame.copy()
        cv2.imshow('video',frame)
        findPen(frame) #傳入每一幀
        draw(drawPoints)
        cv2.imshow('contour',imgContour) 

    else: #取得圖片失敗
        break
    if cv2.waitKey(1) ==ord('q'): #waitKey等待鍵盤上某個鍵被按下
        break
