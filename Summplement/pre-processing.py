
import os
import numpy as np
from skimage import io

cwd = os.getcwd()
imsave_folder = 'F:/Reut/230504_Reut_storm/mito_1/mito_1_br/'  # folder for images with bg removal
count = 1  # image count for naming images
num_bg = 100  # the number of images for background removal


# %% the first image sequence folder
image_stack_file_name = 'F:/Reut/230504_Reut_storm/mito_1/001/'
im_list = os.listdir(image_stack_file_name)
im_start = 0
for i in range(len(im_list)//num_bg):
    ims = []
    for j in range(num_bg):
        im = io.imread(image_stack_file_name+im_list[im_start])
        im_start = im_start+1
        # im = im[808-685-1: 808+685, 780-685-1:780+685]  # no cropping in this case
        ims.append(im)
    ims = np.array(ims)
    ims = ims - ims.min(axis=0, keepdims=True)  # background removal
    for j in range(num_bg):
        io.imsave(imsave_folder + str(count).zfill(5) + '.tif', ims[j, :, :], check_contrast=False)
        count = count + 1
ims = []
for j in range(num_bg):
    im = io.imread(image_stack_file_name+im_list[-(j+1)])
    # im = im[808-685-1: 808+685, 780-685-1:780+685]
    ims.append(im)
ims = np.array(ims)
im_min = ims.min(axis=0)  # background removal
while im_start < len(im_list):
    im = io.imread(image_stack_file_name + im_list[im_start])
    im_start = im_start + 1
    # im = im[808 - 685 - 1: 808 + 685, 780 - 685 - 1:780 + 685]
    im = im-im_min
    io.imsave(imsave_folder + str(count).zfill(5) + '.tif', im, check_contrast=False)
    count = count + 1

# %%
image_stack_file_name = 'F:/Reut/230504_Reut_storm/mito_1/003/'
im_list = os.listdir(image_stack_file_name)
im_start = 0
for i in range(len(im_list)//num_bg):
    ims = []
    for j in range(num_bg):
        im = io.imread(image_stack_file_name+im_list[im_start])
        im_start = im_start+1
        # im = im[808-685-1: 808+685, 780-685-1:780+685]
        ims.append(im)
    ims = np.array(ims)
    ims = ims - ims.min(axis=0, keepdims=True)  # background removal
    for j in range(num_bg):
        io.imsave(imsave_folder + str(count).zfill(5) + '.tif', ims[j, :, :], check_contrast=False)
        count = count + 1
ims = []
for j in range(num_bg):
    im = io.imread(image_stack_file_name+im_list[-(j+1)])
    # im = im[808-685-1: 808+685, 780-685-1:780+685]
    ims.append(im)
ims = np.array(ims)
im_min = ims.min(axis=0)  # background removal
while im_start < len(im_list):
    im = io.imread(image_stack_file_name + im_list[im_start])
    im_start = im_start + 1
    # im = im[808 - 685 - 1: 808 + 685, 780 - 685 - 1:780 + 685]
    im = im-im_min
    io.imsave(imsave_folder + str(count).zfill(5) + '.tif', im, check_contrast=False)
    count = count + 1

# %% the second image sequence folder
image_stack_file_name = 'F:/Reut/230504_Reut_storm/mito_1/002/'
im_list = os.listdir(image_stack_file_name)
im_start = 0
for i in range(len(im_list)//num_bg):
    ims = []
    for j in range(num_bg):
        im = io.imread(image_stack_file_name+im_list[im_start])
        im_start = im_start+1
        # im = im[808-685-1: 808+685, 780-685-1:780+685]
        ims.append(im)
    ims = np.array(ims)
    ims = ims - ims.min(axis=0, keepdims=True)  # background removal
    for j in range(num_bg):
        io.imsave(imsave_folder + str(count).zfill(5) + '.tif', ims[j, :, :], check_contrast=False)
        count = count + 1
ims = []
for j in range(num_bg):
    im = io.imread(image_stack_file_name+im_list[-(j+1)])
    # im = im[808-685-1: 808+685, 780-685-1:780+685]
    ims.append(im)
ims = np.array(ims)
im_min = ims.min(axis=0)  # background removal
while im_start < len(im_list):
    im = io.imread(image_stack_file_name + im_list[im_start])
    im_start = im_start + 1
    # im = im[808 - 685 - 1: 808 + 685, 780 - 685 - 1:780 + 685]
    im = im-im_min
    io.imsave(imsave_folder + str(count).zfill(5) + '.tif', im, check_contrast=False)
    count = count + 1

# %%
image_stack_file_name = 'F:/Reut/230504_Reut_storm/mito_1/003/'
im_list = os.listdir(image_stack_file_name)
im_start = 0
for i in range(len(im_list) // num_bg):
    ims = []
    for j in range(num_bg):
        im = io.imread(image_stack_file_name + im_list[im_start])
        im_start = im_start + 1
        # im = im[808-685-1: 808+685, 780-685-1:780+685]
        ims.append(im)
    ims = np.array(ims)
    ims = ims - ims.min(axis=0, keepdims=True)  # background removal
    for j in range(num_bg):
        io.imsave(imsave_folder + str(count).zfill(5) + '.tif', ims[j, :, :], check_contrast=False)
        count = count + 1
ims = []
for j in range(num_bg):
    im = io.imread(image_stack_file_name + im_list[-(j + 1)])
    # im = im[808-685-1: 808+685, 780-685-1:780+685]
    ims.append(im)
ims = np.array(ims)
im_min = ims.min(axis=0)  # background removal
while im_start < len(im_list):
    im = io.imread(image_stack_file_name + im_list[im_start])
    im_start = im_start + 1
    # im = im[808 - 685 - 1: 808 + 685, 780 - 685 - 1:780 + 685]
    im = im - im_min
    io.imsave(imsave_folder + str(count).zfill(5) + '.tif', im, check_contrast=False)
    count = count + 1

# %% the second image sequence folder
image_stack_file_name = 'F:/Reut/230504_Reut_storm/mito_1/004/'
im_list = os.listdir(image_stack_file_name)
im_start = 0
for i in range(len(im_list) // num_bg):
    ims = []
    for j in range(num_bg):
        im = io.imread(image_stack_file_name + im_list[im_start])
        im_start = im_start + 1
        # im = im[808-685-1: 808+685, 780-685-1:780+685]
        ims.append(im)
    ims = np.array(ims)
    ims = ims - ims.min(axis=0, keepdims=True)  # background removal
    for j in range(num_bg):
        io.imsave(imsave_folder + str(count).zfill(5) + '.tif', ims[j, :, :], check_contrast=False)
        count = count + 1
ims = []
for j in range(num_bg):
    im = io.imread(image_stack_file_name + im_list[-(j + 1)])
    # im = im[808-685-1: 808+685, 780-685-1:780+685]
    ims.append(im)
ims = np.array(ims)
im_min = ims.min(axis=0)  # background removal
while im_start < len(im_list):
    im = io.imread(image_stack_file_name + im_list[im_start])
    im_start = im_start + 1
    # im = im[808 - 685 - 1: 808 + 685, 780 - 685 - 1:780 + 685]
    im = im - im_min
    io.imsave(imsave_folder + str(count).zfill(5) + '.tif', im, check_contrast=False)
    count = count + 1

# %%
image_stack_file_name = 'F:/Reut/230504_Reut_storm/mito_1/003/'
im_list = os.listdir(image_stack_file_name)
im_start = 0
for i in range(len(im_list) // num_bg):
    ims = []
    for j in range(num_bg):
        im = io.imread(image_stack_file_name + im_list[im_start])
        im_start = im_start + 1
        # im = im[808-685-1: 808+685, 780-685-1:780+685]
        ims.append(im)
    ims = np.array(ims)
    ims = ims - ims.min(axis=0, keepdims=True)  # background removal
    for j in range(num_bg):
        io.imsave(imsave_folder + str(count).zfill(5) + '.tif', ims[j, :, :], check_contrast=False)
        count = count + 1
ims = []
for j in range(num_bg):
    im = io.imread(image_stack_file_name + im_list[-(j + 1)])
    # im = im[808-685-1: 808+685, 780-685-1:780+685]
    ims.append(im)
ims = np.array(ims)
im_min = ims.min(axis=0)  # background removal
while im_start < len(im_list):
    im = io.imread(image_stack_file_name + im_list[im_start])
    im_start = im_start + 1
    # im = im[808 - 685 - 1: 808 + 685, 780 - 685 - 1:780 + 685]
    im = im - im_min
    io.imsave(imsave_folder + str(count).zfill(5) + '.tif', im, check_contrast=False)
    count = count + 1

# %% the second image sequence folder
image_stack_file_name = 'F:/Reut/230504_Reut_storm/mito_1/005/'
im_list = os.listdir(image_stack_file_name)
im_start = 0
for i in range(len(im_list) // num_bg):
    ims = []
    for j in range(num_bg):
        im = io.imread(image_stack_file_name + im_list[im_start])
        im_start = im_start + 1
        # im = im[808-685-1: 808+685, 780-685-1:780+685]
        ims.append(im)
    ims = np.array(ims)
    ims = ims - ims.min(axis=0, keepdims=True)  # background removal
    for j in range(num_bg):
        io.imsave(imsave_folder + str(count).zfill(5) + '.tif', ims[j, :, :], check_contrast=False)
        count = count + 1
ims = []
for j in range(num_bg):
    im = io.imread(image_stack_file_name + im_list[-(j + 1)])
    # im = im[808-685-1: 808+685, 780-685-1:780+685]
    ims.append(im)
ims = np.array(ims)
im_min = ims.min(axis=0)  # background removal
while im_start < len(im_list):
    im = io.imread(image_stack_file_name + im_list[im_start])
    im_start = im_start + 1
    # im = im[808 - 685 - 1: 808 + 685, 780 - 685 - 1:780 + 685]
    im = im - im_min
    io.imsave(imsave_folder + str(count).zfill(5) + '.tif', im, check_contrast=False)
    count = count + 1


print('done!')




