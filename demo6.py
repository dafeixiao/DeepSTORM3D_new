
# reduce computation burden through cropping and stitching when applying the network

from DeepSTORM3D.Testing_Localization_Model import test_model
import matplotlib.pyplot as plt
import os

# pre-trained weights on simulations
path_curr = os.getcwd()
path_results = path_curr + '/Demos/Results_Tetrapod_demo2/'

# path to experimental images
path_exp_data = path_curr + '/Experimental_Data/Tetrapod_demo2_crop/'

# postprocessing parameters
postprocessing_params = {'thresh': 40, 'radius': 4}

# test the model by comparing the regenerated image alongside the 3D positions
xyz_rec, conf_rec = test_model(path_results, postprocessing_params, path_exp_data, stitch_flag=True)

# show all plots
plt.show()

