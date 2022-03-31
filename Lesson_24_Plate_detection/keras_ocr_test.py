import keras_ocr
import matplotlib.pyplot as plt


pipeline = keras_ocr.pipeline.Pipeline()

images = [
  keras_ocr.tools.read(url) for url in [
    'img_input/simple_text.jpg'
    ]
]
# img = 'simple_text.jpg'

prediction_groups = pipeline.recognize(images)
# print(prediction_groups)
fig, axs = plt.subplots(nrows=len(images), figsize=(20, 20))
for ax, image, predictions in zip(axs, images, prediction_groups):
    keras_ocr.tools.drawAnnotations(image=image, predictions=predictions, ax=ax)
