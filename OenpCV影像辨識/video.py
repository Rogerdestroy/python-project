import cv2

cap = cv2.VideoCapture('2022-05-11 12-31-24.mkv')

while True:
    ret, frame = cap.read() #下一偵成功?ret / 下一偵圖片frame
    frame = cv2.resize(frame, (0,0), fx=0.5, fy=0.5) #換大小
    if ret:
        cv2.imshow('video', frame)
    else:
        break
    if cv2.waitKey(2) == ord('q'):     #按q結束影片
        cv2.destroyWindow('video')     #關閉視窗
        break
     
    