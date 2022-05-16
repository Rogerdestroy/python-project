import cv2

img = cv2.imread('manyface.jpg')
img = cv2.resize(img, (0,0), fx=0.5, fy=0.5)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faceCascade = cv2.CascadeClassifier('face_default.xml')
#載入人臉辨識模型

faceRect = faceCascade.detectMultiScale(gray, 1.1, 3)
#偵測(辨識的圖片,縮小倍數,辨識物要被框到幾次才有結果)
#回傳矩形
print(len(faceRect))

for (x,y,w,h) in faceRect:
    cv2.rectangle(img, (x,y), (x+w,y+h), (255,255,0), 4)

cv2.imshow('img', img)
cv2.imshow('gray', gray)
cv2.waitKey(0)
