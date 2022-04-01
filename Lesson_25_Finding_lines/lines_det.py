import cv2
import numpy as np


video = cv2.VideoCapture("input/road.mp4")
out = cv2.VideoWriter('output/output.avi', cv2.VideoWriter_fourcc('M','J','P','G'), 24, (640, 360))

while True:
    ret, orig_frame = video.read()
    if not ret:
        break

    frame = cv2.GaussianBlur(orig_frame, (5, 5), 0)

    low_white = np.array([50, 50, 50])
    up_white = np.array([255, 255, 255])
    mask = cv2.inRange(frame, low_white, up_white)

    mask[:270, :] = 0

    edges = cv2.Canny(mask, 75, 150)

    condition = np.stack((edges,) * 3, axis=-1) > 0.2
    back = np.zeros(frame.shape, dtype=np.uint8)

    output_image = np.where(np.stack((mask,) * 3, axis=-1), np.stack((edges,) * 3, axis=-1), back)
    output_image[mask > 0] = (0, 255, 0)

    output_image = np.where(np.stack((mask,) * 3, axis=-1), output_image, frame)
    out.write(output_image)

    cv2.imshow("frame", frame)
    cv2.imshow("final_frame", output_image)

    key = cv2.waitKey(1)
    if key == 27:
        break
video.release()
cv2.destroyAllWindows()
