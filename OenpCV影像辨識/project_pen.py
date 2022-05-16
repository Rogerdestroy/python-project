import cv2
import numpy as np
kernel = np.ones((6,6), np.uint8)

def empty(v):
    pass
  

cap = cv2.VideoCapture(0)

#G B O
penColorHSV = [[44,92,138,97,255,255],
               [99,184,210,113,255,255],
               [10,79,255,79,255,255]]

penColorBGR = [[0,255,0],
               [255,0,0],
               [10,153,255]]

#[x, y, color[id]]
drawPoints = []

def findPen(img):

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    for i in range(len(penColorHSV)):
        lower = np.array(penColorHSV[i][:3])
        upper = np.array(penColorHSV[i][3:6])
        
        mask = cv2.inRange(hsv, lower, upper)
    
        # result = cv2.bitwise_and(img, img, mask=mask)
        
        penx, peny = findContour(mask)
        cv2.circle(img2, (penx, peny), 6, penColorBGR[i], cv2.FILLED)
        
        if peny!=-1:
            drawPoints.append([penx, peny, penColorBGR[i]])
        
    # cv2.imshow('result', result)

def findContour(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    x, y, w, h = -1, -1 , -1, -1
    
    for cnt in contours:
        # cv2.drawContours(img2,cnt,-1,(255,0,0),4)
        area = cv2.contourArea(cnt)
        if area >200:
            peri = cv2.arcLength(cnt, True)
            vertices = cv2.approxPolyDP(cnt, peri * 0.02 , True)
            x, y, w, h = cv2.boundingRect(vertices)
    return x+w//2, y

def draw(drawpoint):
    for point in drawpoint:
        cv2.circle(img2, (point[0], point[1]), 6, (point[2]), cv2.FILLED)
    
while True: 
    ret, frame = cap.read() #下一偵成功?ret / 下一偵圖片frame
    frame = cv2.resize(frame, (0,0), fx=0.8, fy=0.8)
    frame = cv2.flip(frame,1) #左右顛倒
    
    if ret:
        img2  = frame.copy()
        cv2.imshow('len', frame)
        findPen(frame)
        draw(drawPoints)
        cv2.imshow('contour', img2)
    else:
        break
    
    if  cv2.waitKey(1) == ord('q'or'Q'):
        cap.release()               
        cv2.destroyAllWindows()    


"""
cap = cv2.VideoCapture(0)

cv2.namedWindow('TrackBar') #創建視窗
cv2.resizeWindow('TrackBar' , 640, 320) #視窗大小

cv2.createTrackbar('Hue MIN', 'TrackBar', 0, 179, empty)#(名稱, 所在視窗, 初始直 , 最大值 , 呼叫函式)
cv2.createTrackbar('Hue MAX', 'TrackBar', 179, 179, empty)
cv2.createTrackbar('Sat MIM', 'TrackBar', 0, 255, empty)
cv2.createTrackbar('Sat MAX', 'TrackBar', 255, 255, empty)
cv2.createTrackbar('Val MIN', 'TrackBar', 0, 255, empty)
cv2.createTrackbar('Val MAX', 'TrackBar', 255, 255, empty)



while True:
    h_min = cv2.getTrackbarPos('Hue MIN', 'TrackBar')#取得trackbar值
    h_max = cv2.getTrackbarPos('Hue MAX', 'TrackBar')
    s_min = cv2.getTrackbarPos('Sat MIM', 'TrackBar')
    s_max = cv2.getTrackbarPos('Sat MAX', 'TrackBar')
    v_min = cv2.getTrackbarPos('Val MIN', 'TrackBar')
    v_max = cv2.getTrackbarPos('Val MAX', 'TrackBar')
    print(h_min, h_max, s_min, s_max, v_min, v_max)
    
   
    ret,img = cap.read()
        
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])
    
    mask = cv2.inRange(hsv, lower, upper)

    result = cv2.bitwise_and(img, img, mask=mask)
    
    cv2.imshow('img', img)
    cv2.imshow('mask', mask)
    cv2.imshow('result', result)
    
    if cv2.waitKey(1) == ord('q'):
        cv2.destroyAllWindows()
        cap.release()
""" 