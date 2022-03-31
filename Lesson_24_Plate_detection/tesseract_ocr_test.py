import cv2
import pytesseract
from PIL import Image


# conf = r'--oem 3 --psm 6 outputbase digits'
# conf = r'--oem 3 --psm 9')
# img = cv2.imread('img_input/simple_text.jpg')
# img = cv2.imread('img_input/simple_l_p.jpeg')
img = cv2.imread('img_input/taiwan73.jpg')
# cv2.imshow('image', img)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# cv2.imshow('image', gray)
thresh, b_w_img = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)
# cv2.imshow('image', b_w_img)

# inverted_bin = cv2.bitwise_not(b_w_img)
# cv2.imshow('image', inverted_bin)
# print(img.shape)

# h_img, w_img, _ = img.shape
# boxes = pytesseract.image_to_boxes(b_w_img)
# for box in boxes.splitlines():
#     box = box.split(' ')
#     x, y, w, h = int(box[1]), int(box[2]), int(box[3]), int(box[4])
#     cv2.rectangle(b_w_img, (x, h_img - y), (w, h_img - h), (0, 0, 255), 3)
#     cv2.putText(b_w_img, box[0], (x, h_img - y + 25), cv2.FONT_HERSHEY_COMPLEX, 1, (50, 50, 255), 2)

# cv2.imshow('image', b_w_img)

# kernel = np.ones((2, 2), np.uint8)
# processed_img = cv2.erode(inverted_bin, kernel, iterations=1)
# processed_img = cv2.dilate(processed_img, kernel, iterations=1)
# processed_img = cv2.bitwise_not(processed_img)



# print(pytesseract.image_to_string((Image.open('Sample-for-test.jpg'))))
# print(pytesseract.image_to_string(b_w_img, config=conf))
# print(pytesseract.image_to_string(b_w_img))
cv2.waitKey(0)


# thresh, blackAndWhiteImage = cv2.threshold(crop, 100, 255, cv2.THRESH_BINARY)
# inverted_bin = cv2.bitwise_not(blackAndWhiteImage)
# kernel = np.ones((2, 2), np.uint8)
# processed_img = cv2.erode(inverted_bin, kernel, iterations=1)
# processed_img = cv2.dilate(processed_img, kernel, iterations=1)
# processed_img = cv2.bitwise_not(processed_img)
