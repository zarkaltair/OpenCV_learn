import numpy as np
import cv2

# Path to image
path_img = 'test_image.png'
# Read image
img = cv2.imread(path_img)
# Convert image from BGR to HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# define range of blue color in HSV
lower_blue = np.array([20, 180, 180])
upper_blue = np.array([40, 255, 255])

# Threshold the HSV image to get only blue colors
mask = cv2.inRange(hsv, lower_blue, upper_blue)
# Find contours
contours, hierarchy = cv2.findContours(mask, 
                                       cv2.RETR_TREE, 
                                       cv2.CHAIN_APPROX_SIMPLE)
for contour in contours:
   rect = cv2.boundingRect(contour)
   x, y, w, h = rect
   area = w * h

   epsilon = 0.08 * cv2.arcLength(contour, True)
   approx = cv2.approxPolyDP(contour, epsilon, True)

   if area > 20000:
      cv2.drawContours(img, [approx], -1, (0, 0, 255), 2)
      cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
      # print('approx', approx)
      for x in range(0, len(approx)):
         cv2.circle(img, (approx[x][0][0], approx[x][0][1]), 10, (0, 0, 255), -1)

cv2.drawContours(img, contours, -1, (0, 255, 0), 2)

# cv2.imwrite('output.png',img)

cv2.imshow('image',img)
# cv2.imshow('hsv',hsv)
cv2.waitKey(0)
cv2.destroyAllWindows()