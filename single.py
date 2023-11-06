import numpy as np
from npy2obj import numpy_array_to_obj
import nibabel as nib

path = 'BraTS20_Validation_001/BraTS20_Validation_001_t1.nii'

image = nib.load(path)
images = image.get_fdata()

# print(type(images))
print(np.unique(images))
numpy_array_to_obj(images,"out.obj")