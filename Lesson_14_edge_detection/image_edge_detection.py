import cv2
import numpy as np


# load image
img = cv2.imread('panda.jpg', cv2.IMREAD_GRAYSCALE)
# add blure
img = cv2.GaussianBlur(img, (11, 11), 0)

# create filters
sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0)
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1)
laplacian = cv2.Laplacian(img, cv2.CV_64F, ksize=5)
canny = cv2.Canny(img, 100, 150)

# output image
cv2.imshow('Image', img)
cv2.imshow('SobelX', sobelx)
cv2.imshow('SobelY', sobely)
cv2.imshow('Lapacian', laplacian)
cv2.imshow('Canny', canny)

cv2.waitKey(0)
cv2.destroyAllWindows()