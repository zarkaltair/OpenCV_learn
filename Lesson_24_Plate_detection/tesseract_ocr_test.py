import cv2
import pytesseract
from PIL import Image


cascade = cv2.CascadeClassifier('haarcascade_russian_plate_number.xml')
# conf = r'--oem 3 --psm 6 outputbase digits'
# conf = r'--oem 3 --psm 9')
# img = cv2.imread('img_input/simple_text.jpg')
# img = cv2.imread('img_input/simple_l_p.jpeg')
img = cv2.imread('img_input/car3.jpg')
# img = cv2.imread('img_input/taiwan73.jpg')
# cv2.imshow('image', img)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# cv2.imshow('image', gray)
# thresh, b_w_img = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)
# cv2.imshow('image', b_w_img)

# inverted_bin = cv2.bitwise_not(b_w_img)
# cv2.imshow('image', b_w_img)
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
# cv2.waitKey(0)


# thresh, blackAndWhiteImage = cv2.threshold(crop, 100, 255, cv2.THRESH_BINARY)
# inverted_bin = cv2.bitwise_not(blackAndWhiteImage)
# kernel = np.ones((2, 2), np.uint8)
# processed_img = cv2.erode(inverted_bin, kernel, iterations=1)
# processed_img = cv2.dilate(processed_img, kernel, iterations=1)
# processed_img = cv2.bitwise_not(processed_img)

cars_detected = cascade.detectMultiScale(
    gray,
    scaleFactor=1.2,
    minNeighbors=5,
    minSize=(20, 20)
)

# print('Found Numbers:', len(cars_detected))

# for (x, y, w, h) in cars_detected:
#     cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
#     crop = gray[y:y+h, x:x+w]
#     _, b_w_img = cv2.threshold(crop, 100, 255, cv2.THRESH_BINARY)
#     # _, b_w_img = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)
#     processed_img = cv2.bitwise_not(b_w_img)

#     h_img, w_img = gray.shape
#     boxes = pytesseract.image_to_data(processed_img)
#     for ind, box in enumerate(boxes.splitlines()):
#         if ind != 0:
#             box = box.split()
#             print(box)
#             if len(box) == 12:
#                 x, y, w, h = int(box[6]), int(box[7]), int(box[8]), int(box[9])
#                 cv2.rectangle(img, (x, y), (w + x, h + y), (0, 0, 255), 1)
#                 cv2.putText(img, box[11], (x, y), cv2.FONT_HERSHEY_COMPLEX, 1, (50, 50, 255), 2)


    # result = pytesseract.image_to_string(b_w_img)
    # cv2.imshow('Image', img)
# cv2.putText(img, result[0], (x, y), cv2.FONT_HERSHEY_COMPLEX, 1.5, (0, 255, 0), 3)


_, b_w_img = cv2.threshold(img, 79, 255, cv2.THRESH_BINARY)
processed_img = cv2.bitwise_not(b_w_img)
processed_img = cv2.bitwise_not(processed_img)
h_img, w_img = gray.shape
boxes = pytesseract.image_to_data(processed_img, lang='rus')
for ind, box in enumerate(boxes.splitlines()):
    if ind != 0:
        box = box.split()
        if len(box) == 12:
            print(box)
            x, y, w, h = int(box[6]), int(box[7]), int(box[8]), int(box[9])
            cv2.rectangle(img, (x, y), (w + x, h + y), (0, 0, 255), 1)
            cv2.putText(img, box[11], (x, y), cv2.FONT_HERSHEY_COMPLEX, 1, (50, 50, 255), 2)

# cv2.imshow('Image', img)
cv2.imshow('Image', processed_img)
cv2.waitKey(0)
