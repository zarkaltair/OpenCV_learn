import cv2


# download xml file from github/opencv
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

# start video recording
video = cv2.VideoCapture(0)
# while video capturing remains open
while video.isOpened():
    # read image frame from video
    success, image = video.read()

    # change your image to gray from BGR color mode
    gray_converted = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # detectMiltiScale() Detects objects of different sizes in the input image
    # with ScaleFactor=1.2 and minNeighbors=4
    eye_ = eye_cascade.detectMultiScale(gray_converted, 1.2, 4)

    for (x, y, w, h) in eye_:
        # create a rectangle from return 4 values tuple of thickness 2
        cv2.rectangle(image, (x,y), (x+w, y+h), (255, 255, 0), 2)

    # and show frame into window with Detection title
    cv2.imshow('Detection', image)
    key = cv2.waitKey(1)
    if key == 27:
        break

video.release()
cv2.destroyAllWindows()


'''
import cv2
import video


if __name__ == '__main__':
    # create window with name 'original'
    # cv2.namedWindow('original')

    # download xml file from github/opencv
    eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
    
    # create object 'cap' to grab frame to camera
    cap = video.create_capture(0)

    while True:
        # take currently frame to var 'flag'
        flag, image = cap.read()
        
        # change your image to gray from BGR color mode
        gray_converted = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # detectMiltiScale() Detects objects of different sizes in the input image
        # with ScaleFactor=1.2 and minNeighbors=4
        eye_ = eye_cascade.detectMultiScale(gray_converted, 1.2, 4)

        for (x, y, w, h) in eye_:
            # create a rectangle from return 4 values tuple of thickness 2
            cv2.rectangle(image, (x,y), (x+w, y+h), (255, 255, 0), 2)

        # and show frame into window with Detection title
        cv2.imshow('Detection', image)
    #     cv2.waitKey()

    # cap.release()
    # cv2.destroyAllWindows()

        ch = cv2.waitKey(5)
        if ch == 27:
            break
    cap.release()
    cv2.destroyAllWindow()
'''