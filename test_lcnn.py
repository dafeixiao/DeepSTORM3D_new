
# apply the trained network in inference stage

from DeepSTORM3D.Testing_Localization_Model import test_model, test_model_stitching
import matplotlib.pyplot as plt
import os
import torch

# pre-trained weights on simulations
path_curr = os.getcwd()
path_results = path_curr + '/Training_Results/Results3/'  # trained network
path_exp_data = 'C:/Users/dafei.xiao/Desktop/DeepSTORM3D-new/Experimental_Data/example/'  # image folder
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")  # which GPU

# postprocessing parameters
postprocessing_params = {'thresh': 20, 'radius': 4}

# test the model by comparing the regenerated image alongside the 3D positions
# xyz_rec, conf_rec = test_model(path_results, postprocessing_params, device)  # simulation
# xyz_rec, conf_rec = test_model(path_results, postprocessing_params, device, path_exp_data)

xyz_rec, conf_rec = test_model_stitching(path_results, postprocessing_params, device,
                                         exp_imgs_path=path_exp_data, seed=66)

# show all plots
plt.show()