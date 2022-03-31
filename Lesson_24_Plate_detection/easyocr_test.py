import cv2
import easyocr
from PIL import Image


img = cv2.imread('img_input/simple_l_p.jpeg')
# img_path = 'img_input/simple_text.jpg'
# img = Image.open(img_path)
reader = easyocr.Reader(['en'], gpu=False)
result = reader.readtext(img, detail=0)
# print(123)
print(result)

# cv2.imshow('Image', img)
# cv2.waitKey(0)
