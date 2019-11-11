import cv2
import video
import numpy as np


if __name__ == '__main__':
    # create window with name 'original'
    cv2.namedWindow('original')

    # create object 'cap' to grab frame to camera
    cap = video.create_capture(0)
    kernel = np.array([[-1, -1, -1],
                       [-1, 9, -1],
                       [-1, -1, -1]])
    
    while True:
        # take currently frame to var 'flag'
        flag, img = cap.read()
        try:
            # dst = cv2.GaussianBlur(img, (15, 15), 2)
            # dst = cv2.filter2D(img, -1, kernel)
            dst = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
            cv2.imshow('original', dst)
        except:
            cap.release()
            raise

        ch = cv2.waitKey(5)
        if ch == 27:
            break
    cap.release()
    cv2.destroyAllWindow()