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
from skimage import measure

from flask import Flask, redirect, url_for, request, render_template
from werkzeug.utils import secure_filename
from gevent.pywsgi import WSGIServer
from flask_ngrok import run_with_ngrok
app = Flask(__name__)



with CustomObjectScope({"dice_coef": dice_coef, "dice_loss": dice_loss}):
    model = tf.keras.models.load_model("C:/Users/gssan/OneDrive/Desktop/models/200 epoch/files/model.h5")

@app.route('/',methods=['POST','GET'])
def do_prediction():
    if request.method == 'GET':
        return "helllo world"
    else:

        data = request.get_json()
        img = data['input']
        # img = request.path['']
        # print(np.shape(img))
        W = 256
        H = 256
        image = cv2.imread(img, cv2.IMREAD_COLOR)  ## [H, w, 3]
        image = cv2.resize(image, (W, H))  ## [H, w, 3]
        x = image / 255.0  ## [H, w, 3]
        x = np.expand_dims(x, axis=0)


        pred = model.predict(x)

        pred = np.squeeze(pred,axis=0)

        gray_img = np.mean(pred, axis=2)
        contours = measure.find_contours(gray_img, 0.5)


        contours_mean = np.mean([np.mean(contour, axis=0) for contour in contours], axis=0)


        if contours_mean[1] > 150:
            # print('right')
            return 'right'
        elif contours_mean[1] == 150:
            # print('center')
            return 'center'
        else:
            # print('left')
            return 'left'


if __name__ == '__main__':
    app.run(host='192.168.1.103', port=5000)

#
# img = "C:/Users/gssan/Downloads/archive/images/2.png"
# # print(np.shape(img))
# W = 256
# H = 256
# image = cv2.imread(img, cv2.IMREAD_COLOR)  ## [H, w, 3]
# image = cv2.resize(image, (W, H))  ## [H, w, 3]
# x = image / 255.0  ## [H, w, 3]
# x = np.expand_dims(x, axis=0)
#
# print(x.shape)
#
# pred = model.predict(x)
# print(pred)
# pred = np.squeeze(pred,axis=0)
# print(pred.shape)
# print(pred.dtype)
# gray_img = np.mean(pred, axis=2)
# contours = measure.find_contours(gray_img, 0.5)
# print(np.mean(contours[0]))
#
# contours_mean = np.mean([np.mean(contour, axis=0) for contour in contours], axis=0)
# print(contours_mean)
# print(contours_mean[1])
#
# if contours_mean[1] > 150:
#     print('right')
# elif contours_mean[1] == 150:
#     print('center')
# else:
#     print('left')
#
# plt.imshow(pred, interpolation='nearest')
# plt.show()
