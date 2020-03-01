import cv2


# download xml file from github/opencv
face = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cat = cv2.CascadeClassifier('haarcascade_frontalcatface.xml')

# start video recording
video = cv2.VideoCapture(0)

# font 
font = cv2.FONT_HERSHEY_SIMPLEX
# org 
org = (50, 50) 
  
# fontScale 
fontScale = 0.5
   
# Blue color in BGR 
color = (255, 0, 0) 
  
# Line thickness of 1 px
thickness = 1
# while video capturing remains open
while video.isOpened():
    # read image frame from video
    success, image = video.read()

    # change your image to gray from BGR color mode
    gray_converted = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # detectMiltiScale() Detects objects of different sizes in the input image
    # with ScaleFactor=1.2 and minNeighbors=4
    human_face = face.detectMultiScale(gray_converted, 1.2, 4)
    cat_face = cat.detectMultiScale(gray_converted, 1.2, 4)

    for (x, y, w, h) in human_face:
        # create a rectangle from return 4 values tuple of thickness 2
        cv2.rectangle(image, (x,y), (x+w, y+h), (255, 255, 0), 2)
        cv2.putText(image, 'This is a human face', org, font, fontScale, color, thickness, cv2.LINE_AA)

    for (x, y, w, h) in cat_face:
        # create a rectangle from return 4 values tuple of thickness 2
        cv2.rectangle(image, (x,y), (x+w, y+h), (255, 255, 0), 2)
        cv2.putText(image, 'This is a cat face', org, font, fontScale, color, thickness, cv2.LINE_AA)

    # and show frame into window with Detection title
    cv2.imshow('Detection', image)
    key = cv2.waitKey(1)
    if key == 27:
        break

video.release()
cv2.destroyAllWindows()