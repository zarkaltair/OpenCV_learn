import cv2


# function which withdrow image
def viewImage(image, name_of_window):
    cv2.namedWindow(name_of_window, cv2.WINDOW_NORMAL)
    cv2.imshow(name_of_window, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# image path
# image_path = 'test_image_7.jpeg'
# image_path = 'photo_2019-10-27_12-43-09.jpg'
image_path = 'photo_2019-10-27_13-15-57.jpg'
# image_path = 'photo_2019-10-27_13-22-34.jpg'
# base function to detecting faces
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# read image
image = cv2.imread(image_path)
# convert image bgr to gray
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# detecting faces
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1,
									  minNeighbors=5, minSize=(4, 4))

# faces detected
faces_detected = 'Faces detecting : ' + format(len(faces))
print(faces_detected)

# drow rectangle near faces
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (255, 255, 0), 2)

# write image to file
cv2.imwrite('detecting_faces_1.jpg', image)

# image show
viewImage(image,faces_detected)