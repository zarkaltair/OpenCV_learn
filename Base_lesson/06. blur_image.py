import cv2


img = cv2.imread('test_image_5.jpeg')

def viewImage(image, name_of_window):
    cv2.namedWindow(name_of_window, cv2.WINDOW_NORMAL)
    cv2.imshow(name_of_window, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# blur image
blurred = cv2.GaussianBlur(img, (51, 51), 0)
viewImage(blurred, 'Dog in blur')