import cv2
import numpy as np


# capturing video through webcam
cap = cv2.VideoCapture(0)
while True:
    _, img = cap.read()

    # convert frame from BGR to HSV
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # define the range of yellow color
    yellow_low = np.array([25, 80, 150])
    yellow_high = np.array([75, 255, 255])
    yellow = cv2.inRange(hsv, yellow_low, yellow_high)

    # morphological transformation, dilation
    kernel = np.ones((5, 5))
    blue = cv2.dilate(yellow, kernel)
    res = cv2.bitwise_and(img, img, mask=yellow)

    # tracking yellow color
    contours, hierarchy = cv2.findContours(yellow, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if area > 300:
            x, y, w, h = cv2.boundingRect(contour)
            img = cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

    # display results
    img = cv2.flip(img, 1)
    cv2.imshow('Yellow', res)
    cv2.imshow('Color tracking', img)
    if cv2.waitKey(10) & 0xFF == 27:
        cap.release()
        cv2.destroyAllWindows()
        break