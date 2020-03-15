import cv2
import numpy as np


# Create a black image
img = np.zeros((512, 512, 3), np.uint8)

# Write some Text
font                   = cv2.FONT_HERSHEY_SIMPLEX
bottomLeftCornerOfText = (5, 25)
fontScale              = 1
fontColor              = (255, 255, 255)
lineType               = 2

cv2.putText(img,'Hello World!', 
    bottomLeftCornerOfText, 
    font, 
    fontScale,
    fontColor,
    lineType)

# Display the image
cv2.imshow("img",img)

# Save image
cv2.imwrite("out.jpg", img)

# Close image
cv2.waitKey(0)
