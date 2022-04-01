import cv2
import numpy as np
import matplotlib.pyplot as plt


def make_coordinates(img, line_parameters):
    slope, intercept = line_parameters
    y1 = int(img.shape[0])
    y2 = int(y1 * 4 / 7)
    x1 = int((y1 - intercept)/slope)
    x2 = int((y2 - intercept)/slope)
    return [[x1, y1, x2, y2]]

def average_slope_intercept(img, lines):
    left_fit = []
    right_fit = []
    if lines is None:
        return None
    for line in lines:
        for x1, y1, x2, y2 in line:
            fit =  np.polyfit((x1, x2), (y1, y2), 1)
            slope = fit[0]
            intercept = fit[1]
            if slope < 0:
                left_fit.append((slope, intercept))
            else:
                right_fit.append((slope, intercept))
    left_fit_average = np.average(left_fit, axis=0)
    right_fit_average = np.average(right_fit, axis=0)
    left_line = make_coordinates(img, left_fit_average)
    right_line = make_coordinates(img, right_fit_average)
    return [left_line, right_line]

def canny(img):
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    canny = cv2.Canny(blur, 100, 150)
    return canny

def display_lines(img, lines):
    line_image = np.zeros_like(img)
    if lines is not None:
        for line in lines:
            for x1, y1, x2, y2 in line:
                cv2.line(line_image, (x1, y1), (x2, y2), (0, 255, 0), 10)
    return line_image

def region_of_interest(canny):
    height = canny.shape[0]
    width = canny.shape[1]
    mask = np.zeros_like(canny)
    
    polygons = np.array([[
        (100, height), 
        (600, 180),
        (900, height),]], np.int32) 

    cv2.fillPoly(mask, polygons, 255)
    masked_img = cv2.bitwise_and(canny, mask)
    return masked_img


# image = cv2.imread('input/road.jpg')
# image = cv2.imread('input/road1.jpg')
# image = cv2.imread('input/road2.jpg')
# image = cv2.imread('input/road3.jpeg')
image = cv2.imread('input/road4.jpg')
# image = cv2.imread('input/road5.jpg')
# image = cv2.imread('input/road6.jpg')
# image = cv2.imread('input/road7.jpg')
# image = cv2.imread('input/test_image.png')
images = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
lane_image = np.copy(image)
lane_canny = canny(lane_image)
cropped_canny = region_of_interest(lane_canny)
lines = cv2.HoughLinesP(cropped_canny, 2, np.pi/180, 100, np.array([]), minLineLength=40, maxLineGap=5)
averaged_lines = average_slope_intercept(image, lines)
line_image = display_lines(lane_image, averaged_lines)
combo_image = cv2.addWeighted(images, 0.8, line_image, 1, 1)
plt.imshow(combo_image)
plt.show()
