import cv2

img = cv2.imread('pet_annotations.jpg')

img = cv2.resize(img, (600,300))    #改圖片大小
img = cv2.resize(img, (0,0) , fx=2 , fy=2) #依比例改大小
cv2.imshow('img' , img)  #顯示
cv2.waitKey(1000)   #毫秒
cv2.waitKey(0)