import cv2


img = cv2.imread('test_image_6.jpeg')

def viewImage(image, name_of_window):
    cv2.namedWindow(name_of_window, cv2.WINDOW_NORMAL)
    cv2.imshow(name_of_window, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# rectangle on image
output = img.copy()
cv2.rectangle(output, (240, 250), (450, 100), (0, 255, 255), 2)
viewImage(output, 'Rectangle on image')