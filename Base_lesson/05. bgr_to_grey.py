import cv2


img = cv2.imread('test_image_4.jpeg')

def viewImage(image, name_of_window):
    cv2.namedWindow(name_of_window, cv2.WINDOW_NORMAL)
    cv2.imshow(name_of_window, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# image to grey gradient
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, threshold_image = cv2.threshold(img, 127, 255, 0)
viewImage(gray_image, "Dog in grey gradient")
viewImage(threshold_image, "Dog in other colors")