import bentoml
import torch

import os
import tensorflow as tf
import nibabel as nib
import tensorflow_io as tfio


# define the folder containing the .fii files
folder_path = "BraTS20_Validation_001/"

# get a list of all the .fii files in the folder
os.chdir(folder_path)
file_list = os.listdir()
print(file_list)

# create an empty list to store the image arrays
image_list = []

# loop through each file and convert it to a numpy array
for file_path in file_list:
    # read the file contents
    file_contents = tf.io.read_file(file_path)

    # decode the image using TensorFlow IO
    image = nib.load(file_path)
    images = image.get_fdata()

    # append the image array to the list
    image_list.append(images)

# stack the image arrays into a single numpy array
image_array = tf.stack(image_list)

# print(image_array.shape)







# assume that your PyTorch model is stored in a variable called `my_model`
my_model = 'best_metric_model.pth'

# move the model to the GPU
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

print(torch.cuda.get_device_name(0))
# make some predictions using the model
inputs = image_array
inputs = inputs.to(device)
outputs = my_model(inputs)

# move the outputs back to the CPU if necessary
if device.type == 'cuda':
    outputs = outputs.cpu()