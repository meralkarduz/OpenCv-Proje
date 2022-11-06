#Konu: Kamera goruntusunu dorde bolerek parca parca fotograf ceken uygulama

import cv2                                              
import time
import numpy as np

kamera = cv2.VideoCapture(0,cv2.CAP_DSHOW)             
TIMER = int(3)                                          
TIMER2 = int(12)                                        
prev = time.time()                                      
timerkordinat=(120,160)                                
i = 0                                                   

while (True):
    ret, videoGoruntu = kamera.read()                                               
    ret2, videoGoruntu2 = kamera.read()                                             
    videoGoruntu = cv2.flip(videoGoruntu,1)
    videoGoruntu2 = cv2.flip(videoGoruntu2, 1)
    cv2.line(videoGoruntu, (320, 0), (320, 480), (204, 255, 255), 4)                
    cv2.line(videoGoruntu, (0, 240), (640, 240), (204, 255, 255), 4)

    if TIMER2 == 9 :                                                                
        kesit1 = videoGoruntu2[0:240,0:320]                                         
        if TIMER2 != 0: TIMER = int(3)                                              
        timerkordinat=(440,160)                                                     
        cv2.rectangle(videoGoruntu,(0,0), (320,240), (255, 255, 255), -1)           
    if TIMER2 < 9:videoGoruntu[0:240,0:320]=kesit1                                 
                                                                                    
    if TIMER2 == 6:
        kesit2 = videoGoruntu2[0:240,320:640]
        if TIMER2 != 0: TIMER = int(3)
        timerkordinat = (120, 400)
        cv2.rectangle(videoGoruntu, (320, 0), (640, 240), (255, 255, 255), -1)
    if TIMER2 < 6: videoGoruntu[0:240,320:640]=kesit2

    if TIMER2 == 3:
        kesit3 = videoGoruntu2[240:480,0:320]
        if TIMER2 != 0: TIMER = int(3)
        timerkordinat = (440, 400)
        cv2.rectangle(videoGoruntu, (0, 240), (320, 480), (255, 255, 255), -1)
    if TIMER2 < 3: videoGoruntu[240:480,0:320]=kesit3

    if TIMER2 == 0:
        kesit4 = videoGoruntu2[240:480,320:640]
        i = 1
        if TIMER2 != 0: TIMER = int(3)
        cv2.rectangle(videoGoruntu, (320, 240), (640, 480), (255, 255, 255), -1)
    if TIMER2 < 0: videoGoruntu[240:480,320:640]=kesit4

    if i == 0 :cv2.putText(videoGoruntu,str(TIMER), timerkordinat, cv2.FONT_HERSHEY_DUPLEX, 5, (255, 255, 255, 255), 2, cv2.LINE_4);     
    cv2.imshow("Bilgisayar Kamerasi", videoGoruntu)                         
    if cv2.waitKey(1) & 0xFF == 27:                                        
        break
    if cv2.waitKey(1) & 0xFF == ord('s'):                              
        cv2.imwrite('outout.png',videoGoruntu)
        print("resim kaydedildi")
    cur = time.time()                                                      
    if cur - prev >= 1 :                                                     
        prev = cur                                                           
        TIMER = TIMER - 1                                                    
        TIMER2 = TIMER2 - 1

cv2.destroyAllWindows()
