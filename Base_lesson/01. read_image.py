import cv2


# read image
image = cv2.imread('test_img.jpeg')
cv2.imshow('Image', image)
cv2.waitKey(0)
cv2.destroyAllWindow()


# cropped
cropped = image[10:500, 500:2000]
viewImage(cropped, 'Dog after cropped')