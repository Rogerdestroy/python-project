import cv2
import numpy as np

kernel = np.ones((6,6), np.uint8)

img = cv2.imread('pet_annotations.jpg')

img = cv2.resize(img, (600,300))    #改圖片大小
img = cv2.resize(img, (0,0) , fx=0.7 , fy=0.7)

gray   = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)    #RGB改灰階      
blur   = cv2.GaussianBlur(img, (15,15), 3)   #高斯模糊
canny  = cv2.Canny(img, 150, 200)   #找邊緣 
dilate = cv2.dilate(img , kernel , iterations=2)  #膨脹
erode  = cv2.erode(img, kernel, iterations=1)     #侵蝕

cv2.imshow('img',img)
cv2.imshow('gray',gray)
cv2.imshow('blur',blur)
cv2.imshow('canny',canny)
cv2.imshow('dilate',dilate)
cv2.imshow('erode',erode)

while True:
    if cv2.waitKey(0) == ord('q'):     #按q結束影片
        cv2.destroyAllWindows()    #關閉視窗
