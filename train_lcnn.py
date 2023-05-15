import os

# import the data generation and localization net learning functions
from DeepSTORM3D.GenerateTrainingExamples import gen_data
from DeepSTORM3D.Training_Localization_Model import learn_localization_cnn
from parameter_sets import parameter_set1, parameter_set2
import pickle
import os

# specified training parameters
setup_params = parameter_set2()

# generate training data, add more parameters to setup_params dict
gen_data(setup_params)

# learn a localization cnn
learn_localization_cnn(setup_params)