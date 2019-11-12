import cv2
import video
import numpy as np


if __name__ == '__main__':
    # create window with name 'original'
    cv2.namedWindow('original')

    # create object 'cap' to grab frame to camera
    cap = video.create_capture(0)

    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    
    while True:
        # take currently frame to var 'flag'
        flag, img = cap.read()

        low_blue = np.array((90, 70, 70), np.uint8)
        high_blue = np.array((150, 255, 255), np.uint8)
        
        try:
            img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
            mask_blue = cv2.inRange(img_hsv, low_blue, high_blue)

            # result = cv2.bitwise_and(img_hsv, img_hsv, mask=mask_blue)
            # result = cv2.cvtColor(result, cv2.COLOR_HSV2BGR)

            (x, y, w, h) = cv2.boundingRect(img)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            
            cv2.imshow('original', img)
        
        except:
            cap.release()
            raise

        ch = cv2.waitKey(5)
        if ch == 27:
            break
    cap.release()
    cv2.destroyAllWindow()