import cv2

cap = cv2.VideoCapture(0) #數字為鏡頭編號

while True:
    ret, frame = cap.read() #下一偵成功?ret / 下一偵圖片frame
    frame = cv2.resize(frame, (0,0), fx=0.8, fy=0.8) #換大小
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  #轉換為灰階
    frame = cv2.flip(frame,1) #左右顛倒
    if ret:
        cv2.imshow('len', frame)
    else:
        break
    if cv2.waitKey(2) == ord('q'):  #按q結束鏡頭
        cap.release()               #關閉鏡頭
        cv2.destroyWindow('len')    #關閉視窗
        break
     
    