# -*- coding: utf-8 -*-
"""
###DEMO of deepCINAC###

We're going to guide you on how using deepCINAC to train either a cell type or an activity classifier from your
calcium imaging data. Most of the code is similar and in both case you will need to produce labeled data using our GUI.

This notebook has been conceived in order to be run on google colab.
A [python](https://gitlab.com/cossartlab/deepcinac/tree/master/demos/general/demo_deep_cinac_cell_type_training.py) file
is available to be run localy.

Here is a link to our [gitlab page](https://gitlab.com/cossartlab/deepcinac) for more information about our package.

So far, to run this code, you will need some calcium imaging data to work on (in tiff format) and some segmentation data
(ROIs) indicating the contours or pixels that compose your cells
(compatible format are Caiman, suite2p, Fiji or NWB outputs). You will need to open those data using our GUI
(see the [tutorial](https://deepcinac.readthedocs.io/en/latest/tutorial_gui.html))
in order to annotate it (either with the cell type and/or activity) and to produce .cinac files
that will be used to train the classifier.

"""

"""A few packages need to be installed"""

from deepcinac.cinac_model import *
from deepcinac.cinac_predictor import *

if __name__ == '__main__':
    """Change the paths according to your environment"""
    root_path = "/content/deepcinac/"

    data_path = os.path.join(root_path, "data/")
    results_path = os.path.join(root_path, "results")
    time_str = datetime.now().strftime("%Y_%m_%d.%H-%M-%S")
    results_path = os.path.join(results_path, time_str)
    os.mkdir(results_path)

    # indicate if you want to train a classifier to infer neuronal activity or cell type.
    train_activity_classifier = True

    if train_activity_classifier:
        cinac_dir_name = os.path.join(data_path, "cinac_ground_truth/for_training")
    else:
        cinac_dir_name = os.path.join(data_path,
                                      "cinac_cell_type_ground_truth/for_training")

    if not train_activity_classifier:
        """TO PREPARE CELL TYPE CLASSIFIER"""

        """
          To start training from a full saved model from another training, it is necessary to:
          - During the previous training, to put as argument: save_only_the_weitghs=False
          - then specify the .h5 containing the model using partly_trained_model
          - finally setting the learning rate so it is the same as the last epoch trained, using learning_rate_start
        """

        partly_trained_model = os.path.join(root_path, "")
        # yaml_file = os.path.join(data_path, "cell_type_categories_default.yaml")
        cinac_model = CinacModel(results_path=results_path, n_epochs=10, verbose=1,
                                 batch_size=4,
                                 cell_type_classifier_mode=True,
                                 max_width=10, max_height=10,
                                 window_len=1000, max_n_transformations=1,
                                 n_windows_len_to_keep_by_cell=2,
                                 conv_filters=(32, 32, 64, 64),
                                 lstm_layers_size=[32], bin_lstm_size=32,
                                 overlap_value=0.5,
                                 # frames_to_avoid_for_cell_type=[2500, 5000, 7500, 10000],
                                 # partly_trained_model=partly_trained_model,
                                 #  learning_rate_start = 0.001,
                                 save_only_the_weitghs=False
                                 # cell_type_categories_yaml_file=yaml_file
                                 )
    else:
        """TO PREPARE CELL ACTIVITY CLASSIFIER"""

        """
            To start training from a full saved model from another training, it is necessary to:
            - During the previous training, to put as argument: save_only_the_weitghs=False
            - then specify the .h5 containing the model using partly_trained_model
            - finally setting the learning rate so it is the same as the last epoch trained, using learning_rate_start
        """

        # partly_trained_model = os.path.join(root_path, "")
        cinac_model = CinacModel(results_path=results_path, n_epochs=20, verbose=1,
                                 batch_size=8,
                                 cell_type_classifier_mode=False,
                                 window_len=100,
                                 lstm_layers_size=[128, 256], bin_lstm_size=256,
                                 conv_filters=(64, 64, 128, 128),
                                 save_only_the_weitghs=False
                                 # partly_trained_model=partly_trained_model,
                                 #  learning_rate_start = 0.001,
                                 )

    # adding all cinac file in a directory
    cinac_model.add_input_data_from_dir(dir_name=cinac_dir_name, verbose=1)

    # cinac files can also be added individually or as a list
    # using the method add_input_data()
    # cinac_model.add_input_data(cinac_file_names=path_to_file)

    cinac_model.prepare_model(verbose=1)

    """TO START THE TRAINING"""

    cinac_model.fit()
