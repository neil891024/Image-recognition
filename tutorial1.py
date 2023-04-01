# import cv2 
#讀取圖片
# img = cv2.imread('123.jpg')
# img = cv2.resize(img,(300,300)) #圖片 #括號內數字為像素
# img = cv2.resize(img,(0,0), fx=0.5, fy=0.5) #調整影像高度及寬度，fx寬度 fy高度
# cv2.imshow('img',img) #檔名 參數
# cv2.waitKey(0) #圖片顯示的時間，需按下任意鍵才會結束

#讀取影片
import cv2
cap = cv2.VideoCapture('test0306.mp4')
#cap = cv2.VideoCapture(0) #取得攝像頭的影像
while True:
    ret,frame = cap.read() #會回傳兩個值

# ret=取得影片的下一張，圖片是否有取得成功，為布林值，
# frame=回傳取得到的下一張圖片
    if ret: #取得圖片成功
        frame = cv2.resize(frame,(0,0), fx=0.4, fy=0.4) #改變影片視窗大小
        cv2.imshow('video',frame)
    else: #取得圖片失敗
        break
    if cv2.waitKey(10) ==ord('q'): #waitKey等待鍵盤上某個鍵被按下
        break