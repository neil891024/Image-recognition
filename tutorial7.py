#人臉辨識
import cv2

img = cv2.imread("qq.jpg")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #轉為灰階
faceCascade = cv2.CascadeClassifier('face_detect.xml') #載入人臉辨識模型
faceRect = faceCascade.detectMultiScale(gray, 1.1, 5) #辨識人臉
#參數順序 1.圖片 2.圖片縮放的比例 3.針對目標進行檢測的次數
#影片 opencv 2小時初學者教學 1:47:12 (辨識人臉原理)
print(len(faceRect)) #偵測到幾張臉

for (x,y,w,h) in faceRect:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

cv2.imshow('img',img)
cv2.waitKey(0)
