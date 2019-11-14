import cv2
import numpy as np


# create function for showing images
def viewImage(image):
    cv2.namedWindow('Display', cv2.WINDOW_NORMAL)
    cv2.imshow('Display', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# read image
image = cv2.imread('01_test_image_1.jpg')

# convert image from BGR to HSV
hsv_img = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
# first image
viewImage(hsv_img)
cv2.imwrite('02_hsv_image.jpg', hsv_img)

# convert image to HSV with other color level
green_low = np.array([45, 100, 50])
green_high = np.array([75, 255, 255])
curr_mask = cv2.inRange(hsv_img, green_low, green_high)
hsv_img[curr_mask > 0] = ([75, 255, 200])
# second image
viewImage(hsv_img)
cv2.imwrite('03_hsv_image_1.jpg', hsv_img)

# converting the HSV image to Gray inorder to be able to apply contouring
RGB_again = cv2.cvtColor(hsv_img, cv2.COLOR_HSV2RGB)
gray = cv2.cvtColor(RGB_again, cv2.COLOR_RGB2GRAY)
# third image
viewImage(gray)
cv2.imwrite('04_gray_image.jpg', gray)

# convert gray image with threshold in black and white image
ret, threshold = cv2.threshold(gray, 75, 255, 0)
# fourth image
viewImage(threshold)
cv2.imwrite('05_threshold_image.jpg', threshold)

# find contours on image
contours, hierarchy = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(image, contours, -1, (0, 0, 255), 3)
# fifth image
viewImage(image)
cv2.imwrite('06_image_with_contours.jpg', image)