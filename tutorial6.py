#輪廓檢測與形狀辨識
import cv2
img = cv2.imread('shape.jpg')
imgConder = img.copy()
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #轉為灰階
canny = cv2.Canny(img,150,200) #檢測邊緣
contours,hierarchy = cv2.findContours(canny,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE) #檢測輪廓
#參數順序 1.圖片 2.輪廓檢索模式(內輪廓或外輪廓) 3.輪廓近似方法
#contours 輪廓 hierarchy 階層

for cnt in contours:
    cv2.drawContours(imgConder,cnt,-1,(255,0,0),4)
    #參數順序 1.圖片 2.輪廓本身(cnt) 3.繪製輪廓list中的哪條輪廓 -1代表畫出所有輪廓
    #4.線條顏色 5.線條粗細
    # print(cv2.contourArea(cnt)) #畫出輪廓的面積
    # print(cv2.arcLength(cnt,True)) #取得輪廓的邊長
    # 參數順序 1.輪廓 2.輪廓是否為閉合的

    area = cv2.contourArea(cnt) #畫出輪廓的面積
    if area > 500:
        peri = cv2.arcLength(cnt,True)
        vertices = cv2.approxPolyDP(cnt,peri*0.02,True)
        #回傳多邊形的頂點
        #參數順序 1.輪廓 2.近似值 3.輪廓是否為閉合的

        #print(len(vertices)) #印出頂點數量
        corners = len(vertices) #頂點
        x,y,w,h = cv2.boundingRect(vertices)
        # x:方形左上角的x座標 y:方形左上角的y座標
        # w:方形的寬度 h:方形的高度

        cv2.rectangle(imgConder,(x,y),(x+w,y+h),(0,255,0),4)
        # 參數順序 1.要畫在的圖片 2.方形的左上角座標 3.方形的右下角座標
        # 4.顏色 5.粗度

        if corners == 3:
            cv2.putText(imgConder,'triangle',(x,y-5),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)
            #參數順序 1.圖片 2.文字 3.座標 4.字體 5.字體大小 6.字體顏色 7.字體粗度
        elif corners == 4:
            cv2.putText(imgConder,'rectangle',(x,y-5),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)
        elif corners == 5:
            cv2.putText(imgConder,'pentagon',(x,y-5),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)
        elif corners >= 6:
            cv2.putText(imgConder,'circle',(x,y-5),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)

cv2.imshow('img',img)
cv2.imshow('canny', canny)
cv2.imshow('imgContour',imgConder)
cv2.waitKey(0)