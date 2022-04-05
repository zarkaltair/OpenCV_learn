import cv2
import torch
import numpy as np


model_type = "DPT_Large"     # MiDaS v3 - Large     (highest accuracy, slowest inference speed)
# model_type = "DPT_Hybrid"   # MiDaS v3 - Hybrid    (medium accuracy, medium inference speed)
# model_type = "MiDaS_small"  # MiDaS v2.1 - Small   (lowest accuracy, highest inference speed)

midas = torch.hub.load("intel-isl/MiDaS", model_type)

device = torch.device("cuda") if torch.cuda.is_available() else torch.device("cpu")
midas.to(device)
midas.eval()

midas_transforms = torch.hub.load("intel-isl/MiDaS", "transforms")

if model_type == "DPT_Large" or model_type == "DPT_Hybrid":
    transform = midas_transforms.dpt_transform
else:
    transform = midas_transforms.small_transform

filename = 'img_input/dog.jpg'
# filename = 'img_input/cat.jpg'
# filename = 'img_input/city2.jpg'
# filename = 'img_input/city.jpg'
# filename = 'img_input/mountain.jpg'
# filename = 'img_input/street.jpg'
img = cv2.imread(filename)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

input_batch = transform(img).to(device)

with torch.no_grad():
    prediction = midas(input_batch)

    prediction = torch.nn.functional.interpolate(
        prediction.unsqueeze(1),
        size=img.shape[:2],
        mode="bicubic",
        align_corners=True,
    ).squeeze()

depth_map = prediction.cpu().numpy()

depth_map = cv2.normalize(depth_map, None, 0, 1, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_64F)

depth_map = (depth_map*255).astype(np.uint8)

depth_map = cv2.applyColorMap(depth_map , cv2.COLORMAP_MAGMA)
# depth_map = cv2.applyColorMap(depth_map , cv2.COLORMAP_INFERNO)
# depth_map = cv2.applyColorMap(depth_map , cv2.COLORMAP_TURBO)
# depth_map = cv2.applyColorMap(depth_map , cv2.COLORMAP_HSV)

img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
cv2.imshow('Image', img)
cv2.imshow('Depth Map', depth_map)
cv2.waitKey(0)
