import cv2
import numpy as np


video = cv2.VideoCapture("input/road_car_view.mp4")
# output = cv2.VideoWriter('output/output.avi', cv2.VideoWriter_fourcc('M','J','P','G'), 24, (640, 360))

while True:
    ret, orig_frame = video.read()
    if not ret:
        break

    frame = cv2.GaussianBlur(orig_frame, (5, 5), 0)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    low_red = np.array([3, 98, 80])
    up_red = np.array([3, 97, 56])
    mask = cv2.inRange(hsv, low_red, up_red)
    edges = cv2.Canny(mask, 75, 150)
    lines = cv2.HoughLinesP(edges, 1, np.pi/180, 80, np.array([]), maxLineGap=50, minLineLength=10)
    
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            cv2.line(frame, (x1+100, y1+250), (x2+100, y2+250), (0, 255, 0), 10)

    cv2.imshow("frame", edges)

    key = cv2.waitKey(1)
    if key == 27:
        break
video.release()
cv2.destroyAllWindows()
