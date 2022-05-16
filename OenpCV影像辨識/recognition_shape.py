import cv2

"""
img = cv2.imread('GoogleBook.png')
img = cv2.resize(img, (0,0), fx=0.5, fy=0.5)   
"""

img  = cv2.imread('shape02.jpg')
img = cv2.resize(img, (0,0), fx=0.8, fy=0.8)   
img2 = img.copy()
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
canny = cv2.Canny(img, 150, 180)
contours, hierarchy = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
#邊緣偵測(圖片,內外輪廓, 壓縮)
#回傳 1. 輪廓 2. 階層

"""
for cnt in contours:
    print(cnt) #輸出陣列在終端機
"""

for cnt in contours:
    #cv2.drawContours(img2,cnt,-1,(255,0,0),4)  #畫出來(位置,輪廓,輪廓編號,顏色,粗度)
    area = cv2.contourArea(cnt)
    print(cv2.contourArea(cnt))     #輪廓面積
    print(cv2.arcLength(cnt, True), end='\n')    #輪廓邊長(輪廓,是否閉合)
    
    if area >500:
        peri = cv2.arcLength(cnt, True)
        vertices = cv2.approxPolyDP(cnt, peri * 0.02 , True)
        # 近似多邊形(輪廓, 近似值(越大 邊長越多), 是否閉合)
        #回傳近似多邊形頂點
        print(len(vertices), end='\n\n')
        ##print(vertices, end='\n\n-----------------\n\n')
        
        x,y,w,h = cv2.boundingRect(vertices)
        # 外接矩形(回傳1.x 2.y 3.寬 4.高)
        
        cv2.rectangle(img2, (x,y), (x+w,y+h), (0,255,255), 4)     #畫外接矩形
        #劃出外接矩形(畫在,左上角座標,右下角座標,顏色,粗度)
        
        corners = len(vertices)
        
        if corners == 3:
            cv2.putText(img2, 'triganle', (x,y-10) , cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)
            #文字(圖片,文字,左下位置,字體,大小,顏色,粗度)
        elif corners == 4:
            cv2.putText(img2, 'rectangle', (x,y-10) , cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)
        elif corners == 5:
            cv2.putText(img2, 'pentagon', (x,y-10) , cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)
        elif corners >= 6:
            cv2.putText(img2, 'circle', (x,y-5) , cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)


#cv2.imshow('img', img)
#cv2.imshow('canny', canny)
cv2.imshow('img2', img2)
cv2.waitKey(0)
