import os
import cv2
import time

from HandTrackingModule import HandDetector


wCam, hCam = 640, 480

detector = HandDetector(detectionCon=0.7)

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

tip_ids = [4, 8, 12, 16, 20]

while True:
    success, img = cap.read()
    img = detector.find_hands(img)
    lm_list = detector.find_position(img, draw=False)

    if len(lm_list) != 0:
        fingers = []

        # thumb
        # print(lm_list[tip_ids[0]][1], lm_list[tip_ids[0] - 1][1])
        if lm_list[17][1] > lm_list[tip_ids[0]][1] > lm_list[5][1] - 50:
            fingers.append(0)
        elif lm_list[17][1] < lm_list[tip_ids[0]][1] < lm_list[5][1] + 50:
            fingers.append(0)
        else:
            fingers.append(1)

        # 4 finger
        for id in range(1, 5):
            if lm_list[tip_ids[id]][2] < lm_list[tip_ids[id] - 2][2]:
                fingers.append(1)
            else:
                fingers.append(0)

        total_fingers = fingers.count(1)

        cv2.putText(img, str(total_fingers), (45, 375), cv2.FONT_HERSHEY_PLAIN, 10, (255, 0, 0), 25)

    cv2.imshow('Img', img)

    # if the `q` key was pressed, break from the loop
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break
