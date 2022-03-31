import cv2
import easyocr
import matplotlib.pyplot as plt


cascade = cv2.CascadeClassifier('haarcascade_russian_plate_number.xml')
reader = easyocr.Reader(['ru'], gpu=False)

# cars = cv2.imread('img_input/car1.png')
# cars = cv2.imread('img_input/car2.png')
cars = cv2.imread('img_input/car3.jpg')
# cars = cv2.imread('img_input/car4.jpg')

gray = cv2.cvtColor(cars, cv2.COLOR_BGR2GRAY)

cars_detected = cascade.detectMultiScale(
    gray,
    scaleFactor=1.2,
    minNeighbors=5,
    minSize=(20, 20)
)

print('Found Numbers:', len(cars_detected))

for (x, y, w, h) in cars_detected:
    cv2.rectangle(cars, (x, y), (x + w, y + h), (0, 255, 0), 3)
    crop = gray[y:y+h,x:x+w]
    result = reader.readtext(crop, detail=0)
    # print(result)
    cv2.putText(cars, result[0], (x, y), cv2.FONT_HERSHEY_COMPLEX, 1.5, (0, 255, 0), 3)
    plt.imshow(cars)
    plt.show()
    # cv2.imshow('Image', crop)
    # cv2.waitKey(0)
    # cv2.imwrite('img_output/Detected_car2.jpg', cars)
