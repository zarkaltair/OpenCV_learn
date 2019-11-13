# import libraries
import cv2

# load image and convert to gray
image = cv2.imread('test_set/test_10.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (13, 13), 0)
# _, gray = cv2.threshold(gray, 115, 200, 1)
cv2.imwrite('gray.jpg', gray)

# detection contours
edged = cv2.Canny(gray, 10, 250)
cv2.imwrite('edged.jpg', edged)

# create and apply closing
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7,7))
closed = cv2.morphologyEx(edged, cv2.MORPH_CLOSE, kernel)
cv2.imwrite('closed.jpg', closed)

# fine contours on image and count his
cnts, _ = cv2.findContours(closed.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
total = 0

# create cycle
for c in cnts:
    # approx contours
    peri = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.02 * peri, True)

    # if contour have 4 edge approx this is book
    if len(approx) == 4:
        cv2.drawContours(image, [approx], -1, (0, 255, 0), 4)
        total += 1

# show results image
print(f'I fined {total} books on this image')
cv2.imwrite('output.jpg', image)