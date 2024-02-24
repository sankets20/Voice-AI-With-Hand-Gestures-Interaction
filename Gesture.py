import cv2
import time
import os
import numpy as np
import HandTrackingModule as htm
import pyautogui as auto
import sys
import math
import pyautogui
import pygetwindow as gw


def hand_track():
    wCam, hCam = 500, 500
    cap = cv2.VideoCapture(0)
    cap.set(3, wCam)
    cap.set(4, hCam)
    pTime = 0

    frameR = 60
    wScr, hScr = auto.size()

    detector = htm.handDetector(detectionCon=0.75)

    tipIds = [4, 8, 12, 16, 20]
    i, j, k,l,m,n,o,p,q,r= 0, 0, 0,0,0,0,0,0,0,0
    while True:
        success, img = cap.read()
        img = detector.findHands(img)
        lmList = detector.findPosition(img, draw=False)
        img = cv2.flip(img, 1)

        if len(lmList) != 0:
            fingers = []

            if lmList[tipIds[0]][1] > lmList[tipIds[0] - 1][1]:
                fingers.append(1)
            else:
                fingers.append(0)
            for id in range(1, 5):
                if lmList[tipIds[id]][2] < lmList[tipIds[id] - 2][2]:
                    fingers.append(1)
                else:
                    fingers.append(0)

            totalFingers = fingers.count(1)

            cv2.rectangle(img, (frameR, frameR), (wCam - frameR, hCam - frameR), (255, 0, 150), 2)
            if lmList[tipIds[1]][2] < lmList[tipIds[1] - 2][2] and lmList[tipIds[4]][2] < lmList[tipIds[4] - 2][2] and \
                    lmList[tipIds[2]][2] > lmList[tipIds[2] - 2][2] and lmList[tipIds[3]][2] > lmList[tipIds[3] - 2][2]:
                print(i)
                i += 1
                if i > 15:
                    cv2.putText(img, f"New Tab Created", (175, 450), cv2.FONT_HERSHEY_PLAIN, 2, (245, 200, 50), 3)
                    if i > 20:
                        i = 0
                        auto.hotkey('ctrl', 't')# thumb index pink

            elif lmList[tipIds[1]][2] > lmList[tipIds[1] - 2][2] and lmList[tipIds[4]][2] > lmList[tipIds[4] - 2][2] and \
                    lmList[tipIds[2]][2] < lmList[tipIds[2] - 2][2] and lmList[tipIds[3]][2] < lmList[tipIds[3] - 2][2]:
                print(j)
                j += 1
                if j > 15:
                    cv2.putText(img, f"This Tab Closed", (175, 450), cv2.FONT_HERSHEY_PLAIN, 2, (245, 200, 50), 3)
                    if j > 20:
                        j = 0
                        auto.hotkey('ctrl','w')# close window thumb middle ring

    
            elif lmList[tipIds[0]][2] < lmList[tipIds[0] - 2][2] and lmList[tipIds[1]][2] > lmList[tipIds[1] - 2][2] and lmList[tipIds[4]][2] > lmList[tipIds[4] - 2][2] and \
                    lmList[tipIds[2]][2] > lmList[tipIds[2] - 2][2] and lmList[tipIds[3]][2] > lmList[tipIds[3] - 2][2]:
                print(k)
                k += 1
                if k > 15:
                    cv2.putText(img, f"Scroll up", (175, 450), cv2.FONT_HERSHEY_PLAIN, 2, (245, 200, 50), 3)
                    if k > 20:
                        k = 0
                        auto.scroll(200) # upwared thumb 

            elif lmList[tipIds[1]][2] > lmList[tipIds[1] - 2][2] and lmList[tipIds[4]][2] < lmList[tipIds[4] - 2][2] and \
                    lmList[tipIds[2]][2] > lmList[tipIds[2] - 2][2] and lmList[tipIds[3]][2] < lmList[tipIds[3] - 2][2]:
                print(l)
                l += 1
                if l > 15:
                    cv2.putText(img, f"Scroll  down", (175, 450), cv2.FONT_HERSHEY_PLAIN, 2, (245, 200, 50), 3)
                    if l > 20:
                        l = 0
                        auto.scroll(-200) # ring  and pink

            elif lmList[tipIds[1]][2] > lmList[tipIds[1] - 2][2] and lmList[tipIds[4]][2] > lmList[tipIds[4] - 2][2] and \
                    lmList[tipIds[2]][2] < lmList[tipIds[2] - 2][2] and lmList[tipIds[3]][2] > lmList[tipIds[3] - 2][2]:
                print(l)
                m += 1
                if m > 15:
                    cv2.putText(img, f"Paly Pause", (175, 450), cv2.FONT_HERSHEY_PLAIN, 2, (245, 200, 50), 3)
                    if m > 20:
                        m = 0
                        auto.hotkey('space') # thumb index and middle 

            elif lmList[tipIds[1]][2] < lmList[tipIds[1] - 2][2] and lmList[tipIds[4]][2] > lmList[tipIds[4] - 2][2] and \
                    lmList[tipIds[2]][2] < lmList[tipIds[2] - 2][2] and lmList[tipIds[3]][2] < lmList[tipIds[3] - 2][2]:
                print(n)
                n += 1
                if n > 15:
                    cv2.putText(img, f"upward", (175, 450), cv2.FONT_HERSHEY_PLAIN, 2, (245, 200, 50), 3)
                    if n > 20:
                        n = 0
                        auto.hotkey('up') #  tumb index and middle ring 
            
            elif lmList[tipIds[0]][2] > lmList[tipIds[0] - 2][2] and lmList[tipIds[1]][2] < lmList[tipIds[1] - 2][2] and lmList[tipIds[4]][2] < lmList[tipIds[4] - 2][2] and \
                    lmList[tipIds[2]][2] < lmList[tipIds[2] - 2][2] and lmList[tipIds[3]][2] < lmList[tipIds[3] - 2][2]:
                print(o)
                o += 1
                if o > 15:
                    cv2.putText(img, f"Enter", (175, 450), cv2.FONT_HERSHEY_PLAIN, 2, (245, 200, 50), 3)
                    if o > 20:
                        o = 0
                        auto.hotkey('enter') 

            elif lmList[tipIds[0]][2] < lmList[tipIds[0] - 2][2] and lmList[tipIds[1]][2] < lmList[tipIds[1] - 2][2] and lmList[tipIds[4]][2] < lmList[tipIds[4] - 2][2] and \
                    lmList[tipIds[2]][2] < lmList[tipIds[2] - 2][2] and lmList[tipIds[3]][2] < lmList[tipIds[3] - 2][2]:
                print(p)
                p += 1
                if p > 15:
                    cv2.putText(img, f"close", (175, 450), cv2.FONT_HERSHEY_PLAIN, 2, (245, 200, 50), 3)
                    if p > 20:
                        p = 0
                        auto.hotkey('q') 

            elif lmList[tipIds[0]][2] < lmList[tipIds[0] - 2][2] and lmList[tipIds[1]][2] < lmList[tipIds[1] - 2][2] and lmList[tipIds[4]][2] > lmList[tipIds[4] - 2][2] and \
                    lmList[tipIds[2]][2] < lmList[tipIds[2] - 2][2] and lmList[tipIds[3]][2] > lmList[tipIds[3] - 2][2]:
                print(q)
                q += 1
                if q > 15:
                    cv2.putText(img, f"Volume Up", (175, 450), cv2.FONT_HERSHEY_PLAIN, 2, (245, 200, 50), 3)
                    if q > 20:
                        q = 0
                        auto.hotkey('VolumeUp') 
            

            elif lmList[tipIds[0]][2] > lmList[tipIds[0] - 2][2] and lmList[tipIds[1]][2] < lmList[tipIds[1] - 2][2] and lmList[tipIds[4]][2] > lmList[tipIds[4] - 2][2] and \
                    lmList[tipIds[2]][2] < lmList[tipIds[2] - 2][2] and lmList[tipIds[3]][2] > lmList[tipIds[3] - 2][2]:
            
                print(r)
                r += 1
                if r > 15:
                    cv2.putText(img, f"Volume Down", (175, 450), cv2.FONT_HERSHEY_PLAIN, 2, (245, 200, 50), 3)
                    if r > 20 :  # Adjust the multiplier to control the speed
                        r = 0
                        auto.hotkey('VolumeDown')
                        time.sleep(0.1) 

            
            else:
                i, j = 0, 0

            thumbx, thumby, thumbex = lmList[4][1], lmList[4][2], lmList[2][1]
            indx, indy = lmList[8][1], lmList[8][2]
            midx, midy = lmList[12][1], lmList[12][2]
            ringx, ringy = lmList[16][1], lmList[16][2]
            pinkx, pinky = lmList[20][1], lmList[20][2]

            disIndThumb = math.hypot(thumbx - indx, thumby - indy)
            disMidThumb = math.hypot(thumbx - midx, thumby - midy)
            disRingThumb = math.hypot(thumbx - ringx, thumby - ringy)
            disPinkThumb = math.hypot(thumbx - pinkx, thumby - pinky)
            disindex=math.hypot(indx,indy)

            auto.FAILSAFE = False

            if lmList[12][2] > lmList[10][2] and lmList[16][2] > lmList[14][2] and lmList[20][2] > lmList[18][2] and \
                    thumbx > thumbex:
                convx = np.interp(indx, (frameR, wCam - frameR), (0, wScr))
                convx = 1920 - convx
                convy = np.interp(indy, (frameR, hCam - frameR), (0, hScr))
                auto.moveTo(convx, convy, 0, auto.easeInQuad)

            elif disIndThumb < 20 and lmList[12][2] < lmList[10][2] and lmList[16][2] < lmList[14][2] and \
                    lmList[20][2] < lmList[18][2]:
                auto.leftClick()
            elif disMidThumb < 20 and lmList[8][2] < lmList[6][2] and lmList[16][2] < lmList[14][2] and \
                    lmList[20][2] < lmList[18][2]:
                auto.rightClick()
            elif disRingThumb < 20 and lmList[12][2] < lmList[10][2] and lmList[8][2] < lmList[6][2] and \
                    lmList[20][2] < lmList[18][2]:
                auto.hotkey('ctrl', 'tab')
            elif disPinkThumb < 20 and lmList[12][2] < lmList[10][2] and lmList[16][2] < lmList[14][2] and \
                    lmList[8][2] < lmList[6][2]:
                auto.hotkey('alt','F4')

    # ... (remaining code)


        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime

        cv2.putText(img, f"FPS :{int(fps)}", (420, 60), cv2.FONT_HERSHEY_COMPLEX, 1, (250, 50, 170), 3)

        cv2.imshow("Counter", img)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
