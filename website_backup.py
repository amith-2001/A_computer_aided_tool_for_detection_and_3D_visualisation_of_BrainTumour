import flask
from tensorflow.keras.utils import load_img
import tensorflow as tf
from tensorflow.keras.utils import CustomObjectScope
from metrics import dice_loss, dice_coef
import numpy as np
import cv2
from matplotlib import pyplot as plt
from keras.models import load_model
from skimage.color import rgb2gray
import cv2
from skimage import measure
with CustomObjectScope({"dice_coef": dice_coef, "dice_loss": dice_loss}):
    model = tf.keras.models.load_model("C:/Users/gssan/OneDrive/Desktop/models/200 epoch/files/model.h5")


#
img = "C:/Users/gssan/Downloads/archive/images/4.png"
# img = "C:/Users/gssan/Downloads/archive/images/333.png"
# print(np.shape(img))
W = 256
H = 256
image = cv2.imread(img, cv2.IMREAD_COLOR)  ## [H, w, 3]
image = cv2.resize(image, (W, H))  ## [H, w, 3]
x = image / 255.0  ## [H, w, 3]
x = np.expand_dims(x, axis=0)

print(x.shape)

pred = model.predict(x)
print(pred)
pred = np.squeeze(pred,axis=0)
print(pred.shape)
print(pred.dtype)
gray_img = np.mean(pred, axis=2)
contours = measure.find_contours(gray_img, 0.5)

# contours_arr = np.array(contours)
# contours_arr = contours_arr.astype(np.float32)
# print(type(contours_arr))
# area = cv2.contourArea(contours_arr)
# print("area is",area)
# areas = []

# for contour in contours:
#     # Convert contour to integer coordinates
#     contour = np.round(contour)
#     # Calculate area of contour using regionprops
#     props = measure.regionprops(pred)
#     areas.append(props[0].area)
#
# total_area = sum(areas)
# print("Total area of contours:", total_area)
# print(contours)
print(np.mean(contours[0]))
print(np.shape(contours))
print("contours length is ",len(contours[:]))

contours_mean = np.mean([np.mean(contour, axis=0) for contour in contours], axis=0)
print(contours_mean)
print(contours_mean[0])

if contours_mean[1] > 150:
    print('right')
elif contours_mean[1] == 150:
    print('center')
else:
    print('left')


plt.imshow(pred, interpolation='nearest')
plt.show()

