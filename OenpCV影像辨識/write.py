import cv2
import numpy as np

img = np.zeros((600,600,3), np.uint8) #創建黑色圖片
cv2.line(img, (0,0), (400,500), (255,0,0), 10) #畫線
#(圖片,起始點,結束點,顏色,粗度)

cv2.line(img, (0,0), ((img.shape[1]),(img.shape[0])), (0,255,0), 10) 
#畫線
#(圖片,起始點,(圖片寬度,圖片高度),顏色,粗度)

cv2.rectangle(img, (50,50), (300,300), (0,0,255), 15) 
#畫正方形

cv2.rectangle(img, (50,50), (200,200), (0,125,125), cv2.FILLED)
#填滿正方形

cv2.circle(img, (300,350), 50, (120,200,98), 8)
#圓形(圖片,圓心,半徑,顏色,粗度)

cv2.circle(img, (400,350), 50, (100,150,208), cv2.FILLED)
#填滿圓形

cv2.putText(img, 'HELLO', (100,500), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 4, (125,125,125), 10)
#文字(圖片,文字,左下位置,字體,大小,顏色,粗度)
#不支援中文

cv2.imshow('img', img)
cv2.waitKey(0)