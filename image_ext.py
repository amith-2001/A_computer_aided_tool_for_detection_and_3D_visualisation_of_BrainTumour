import os
import tensorflow as tf
import nibabel as nib
import tensorflow_io as tfio
from npy2obj import numpy_array_to_obj


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

print(image_array.shape)

# numpy_array_to_obj(image_array,"example1.obj")
# print('done')