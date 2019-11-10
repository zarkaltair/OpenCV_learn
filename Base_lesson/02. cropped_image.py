import cv2


image = cv2.imread('test_image.png')

def viewImage(image, name_of_window):
    cv2.namedWindow(name_of_window, cv2.WINDOW_NORMAL)
    cv2.imshow(name_of_window, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# cropped
cropped = image[:, 500:]
viewImage(cropped, 'Dog after cropping')

# write image to file
cv2.imwrite('output.png',cropped)