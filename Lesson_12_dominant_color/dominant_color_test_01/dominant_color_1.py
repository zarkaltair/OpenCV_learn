import cv2
import numpy as np
from sklearn.cluster import KMeans
from collections import Counter


# define function for get dominant color
def get_dominant_color(image, k=4):
    image = image.reshape((image.shape[0] * image.shape[1], 3))
    
    # clusterization image with k clusters
    clt = KMeans(n_clusters=k)
    labels = clt.fit_predict(image)

    # labeling clusters
    label_counts = Counter(labels)

    # count number clucters
    dominant_color = clt.cluster_centers_[label_counts.most_common(1)[0][0]]
    return list(dominant_color)

# load image
bgr_image = cv2.imread('test_04.jpg')
# convert image from BGR to HSV
hsv_image = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2HSV)
# def dominant color
dom_color = get_dominant_color(hsv_image)
# fill shape of origin image dominant color
dom_color_hsv = np.full(bgr_image.shape, dom_color, dtype='uint8')
# return convert to BGR
dom_color_bgr = cv2.cvtColor(dom_color_hsv, cv2.COLOR_HSV2BGR)
# stack both image together
output_image = np.hstack((bgr_image, dom_color_bgr))
# show image and dominant color
cv2.imshow('Dominant color', output_image)
cv2.waitKey(0)