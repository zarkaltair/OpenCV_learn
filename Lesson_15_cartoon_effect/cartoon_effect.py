import cv2
import numpy as np


# load image
img = cv2.imread('test_01.jpg')

# get edges
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.medianBlur(gray, 5)
edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)

# get color
color = cv2.bilateralFilter(img, 9, 300, 300)

# get cartoon
cartoon = cv2.bitwise_and(color, color, mask=edges)

cv2.imwrite('cartoon.jpg', cartoon)
cv2.imwrite('edges.jpg', edges)

cv2.imshow('Image', img)
cv2.imshow('Cartoon', cartoon)
cv2.imshow('Color', color)
cv2.imshow('egdes', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()