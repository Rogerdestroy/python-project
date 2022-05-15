import cv2
import numpy as np
kernel = np.ones((6,6), np.uint8)

def empty(v):
    pass

img = cv2.imread('minip.jpg')
img = cv2.resize(img, (0,0), fx=1.2, fy=1.2)    

img = cv2.erode(img, kernel, iterations=1) 
img = cv2.dilate(img , kernel , iterations=1)

cv2.namedWindow('TrackBar') #創建視窗
cv2.resizeWindow('TrackBar' , 640, 320) #視窗大小

cv2.createTrackbar('Hue MIN', 'TrackBar', 0, 179, empty)
#(名稱, 所在視窗, 初始直 , 最大值 , 呼叫函式)
cv2.createTrackbar('Hue MAX', 'TrackBar', 179, 179, empty)
cv2.createTrackbar('Sat MIM', 'TrackBar', 0, 255, empty)
cv2.createTrackbar('Sat MAX', 'TrackBar', 255, 255, empty)
cv2.createTrackbar('Val MIN', 'TrackBar', 0, 255, empty)
cv2.createTrackbar('Val MAX', 'TrackBar', 255, 255, empty)

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)   #HSV 色調、飽和度；亮度

while True:
    h_min = cv2.getTrackbarPos('Hue MIN', 'TrackBar')
    #取得trackbar值
    h_max = cv2.getTrackbarPos('Hue MAX', 'TrackBar')
    s_min = cv2.getTrackbarPos('Sat MIM', 'TrackBar')
    s_max = cv2.getTrackbarPos('Sat MAX', 'TrackBar')
    v_min = cv2.getTrackbarPos('Val MIN', 'TrackBar')
    v_max = cv2.getTrackbarPos('Val MAX', 'TrackBar')
    print(h_min, h_max, s_min, s_max, v_min, v_max)
    
    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])
    
    mask = cv2.inRange(hsv, lower, upper)
    #過濾顏色(圖片,最小值,最大值)

    
    result = cv2.bitwise_and(img, img, mask=mask)
    #(原圖,原圖,過濾後=過濾後)
    #白色保留 黑色去除
    """
    會把兩張圖片同個位置坐and運算
    再套入mask遮罩
    => img套上mask遮罩 白色的部分顯示出來
    """
    
    cv2.imshow('img', img)
    cv2.imshow('hsv', hsv)
    cv2.imshow('mask', mask)
    cv2.imshow('result', result)
    
    if cv2.waitKey(1) == ord('q'):
        cv2.destroyAllWindows()

"""
cv2.imshow('img', img)
cv2.imshow('hsv', hsv)
cv2.imshow('mask', mask)

cv2.waitKey(0)
"""