"""
File that contains methods use to fit the data to the model and train it.
"""

import tensorflow as tf

TF_VERSION = tf.__version__
print(f"TF_VERSION {TF_VERSION}")

# depending on the TF version installed
if TF_VERSION[0] == "2":
    # from https://github.com/tensorflow/tensorflow/issues/25138
    from tensorflow.compat.v1 import ConfigProto
    from tensorflow.compat.v1 import InteractiveSession

    config = ConfigProto()
    # config.gpu_options.per_process_gpu_memory_fraction = 0.75
    config.gpu_options.allow_growth = True
    session = InteractiveSession(config=config)

    from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Bidirectional, BatchNormalization
    from tensorflow.keras.layers import Input, LSTM, Dense, TimeDistributed, Activation, Lambda, Permute, RepeatVector
    from tensorflow.keras.models import Model, Sequential
    from tensorflow.keras.models import model_from_json
    from tensorflow.keras.optimizers import RMSprop, Adam, SGD
    from tensorflow.keras import layers
    from tensorflow.keras.callbacks import ReduceLROnPlateau, ModelCheckpoint, EarlyStopping
    from tensorflow.keras import backend as K
    from tensorflow.keras.models import load_model
    from tensorflow.keras.utils import get_custom_objects, multi_gpu_model
    from alt_model_checkpoint.tensorflow import AltModelCheckpoint
else:
    import keras
    from keras.layers import Conv2D, MaxPooling2D, Flatten, Bidirectional, BatchNormalization
    from keras.layers import Input, LSTM, Dense, TimeDistributed, Activation, Lambda, Permute, RepeatVector
    from keras.models import Model, Sequential
    from keras.models import model_from_json
    from keras.optimizers import RMSprop, Adam, SGD
    from keras import layers
    from keras.callbacks import ReduceLROnPlateau, ModelCheckpoint, EarlyStopping
    from keras import backend as K
    from keras.models import load_model
    from keras.utils import get_custom_objects, multi_gpu_model
    from alt_model_checkpoint.keras import AltModelCheckpoint

from deepcinac.cinac_movie_patch import MoviePatchGeneratorMaskedVersions, MoviePatchData, \
    DataGenerator, MoviePatchGeneratorForCellType
from deepcinac.cinac_stratification import neuronal_activity_encoding, StratificationCamembert, \
    StratificationDataProcessor, StratificationCellTypeDataProcessor, StratificationCellTypeCamembert
from deepcinac.cinac_structures import CinacRecording, CinacDataMovie, CinacSplitedTiffMovie, CinacFileReaderMovie
from deepcinac.utils.cinac_file_utils import CinacFileReader, read_cell_type_categories_yaml_file
from deepcinac.utils.utils import check_one_tiff_file_by_frame_exists
import numpy as np
import time
import scipy.signal
import yaml

import os




def attention_3d_block(inputs, time_steps, use_single_attention_vector=False):
    """
    from: https://github.com/philipperemy/keras-attention-mechanism
    :param inputs:
    :param use_single_attention_vector:  if True, the attention vector is shared across
    the input_dimensions where the attention is applied.
    :return:
    """
    # inputs.shape = (batch_size, time_steps, input_dim)
    # print(f"inputs.shape {inputs.shape}")
    input_dim = int(inputs.shape[2])
    a = Permute((2, 1))(inputs)
    # a = Reshape((input_dim, time_steps))(a)  # this line is not useful. It's just to know which dimension is what.
    a = Dense(time_steps, activation='softmax')(a)
    if use_single_attention_vector:
        a = Lambda(lambda x: K.mean(x, axis=1))(a)  # , name='dim_reduction'
        a = RepeatVector(input_dim)(a)
    a_probs = Permute((2, 1))(a)  # , name='attention_vec'
    if TF_VERSION[0] == "2":
        output_attention_mul = tf.keras.layers.multiply([inputs, a_probs])
    else:
        output_attention_mul = keras.layers.multiply([inputs, a_probs])
    return output_attention_mul

# from: http://www.deepideas.net/unbalanced-classes-machine-learning/
def sensitivity(y_true, y_pred):
    true_positives = K.sum(K.round(K.clip(y_true * y_pred, 0, 1)))
    possible_positives = K.sum(K.round(K.clip(y_true, 0, 1)))
    return true_positives / (possible_positives + K.epsilon())


# from: http://www.deepideas.net/unbalanced-classes-machine-learning/
def specificity(y_true, y_pred):
    true_negatives = K.sum(K.round(K.clip((1 - y_true) * (1 - y_pred), 0, 1)))
    possible_negatives = K.sum(K.round(K.clip(1 - y_true, 0, 1)))
    return true_negatives / (possible_negatives + K.epsilon())


def precision(y_true, y_pred):
    true_positives = K.sum(K.round(K.clip(y_true * y_pred, 0, 1)))
    predicted_positives = K.sum(K.round(K.clip(y_pred, 0, 1)))
    return true_positives / (predicted_positives + K.epsilon())

# ------------------------------------------------------------
# needs to be defined as activation class otherwise error
# AttributeError: 'Activation' object has no attribute '__name__'
# From: https://github.com/keras-team/keras/issues/8716
class Swish(Activation):

    def __init__(self, activation, **kwargs):
        super(Swish, self).__init__(activation, **kwargs)
        self.__name__ = 'swish'


def swish(x):
    """
    Implementing a the swish activation function.
    From: https://www.kaggle.com/shahariar/keras-swish-activation-acc-0-996-top-7
    Paper describing swish: https://arxiv.org/abs/1710.05941

    :param x:
    :return:
    """
    return K.sigmoid(x) * x
    # return Lambda(lambda a: K.sigmoid(a) * a)(x)

class CinacModel:
    """
    Model used to train a classifier.
    First add data using add_input_data() method
    Second prepare_model()
    And a last fit()
    """

    def __init__(self, **kwargs):
        # TODO: Describe each argument

        # give the code associated to a cell_type, will be filled by load_cell_type_categories_from_yaml_file()
        self.cell_type_to_code_dict = dict()
        # give the cell_type associated to a code, will be filled by load_cell_type_categories_from_yaml_file()
        self.cell_type_from_code_dict = dict()

        # allows to give a .h5 file representing a partly trained model
        # the training will be resumed from there
        # Caution: the learning rate should be the same as used in the last epoch
        self.partly_trained_model = kwargs.get("partly_trained_model", None)
        # if False, save the full model
        self.save_weigths_only = kwargs.get("save_only_the_weitghs", True)

        # if "tiffs_dirname" not in kwargs:
        #     raise Exception("You need to pass tiffs_dirname as an argument. That the folder in which "
        #                     "the individual frame tiffs will be created")
        self.tiffs_dirname = kwargs.get("tiffs_dirname", None)

        self.n_gpus = kwargs.get("n_gpus", 1)
        self.using_multi_class = kwargs.get("using_multi_class", 1)  # 1 or 3 so far
        if self.using_multi_class not in [1, 3]:
            raise Exception(f"using_multi_class can take only 1 or 3 as value. "
                            f"Value passed being {self.using_multi_class}")

        # indicate if the classifier is made to classify cell_type
        # if False, then we use the classifier to classifier cell activity
        # so far it works just a 1 class classifier, and give the probably that a cell is an interneuron
        self.cell_type_classifier_mode = kwargs.get("cell_type_classifier_mode", False)
        if self.cell_type_classifier_mode:
            my_path = os.path.abspath(os.path.dirname(__file__))
            yaml_file = kwargs.get("cell_type_categories_yaml_file",
                                   os.path.join(my_path, "cell_type_categories_default.yaml"))
            self.load_cell_type_categories_from_yaml_file(yaml_file=yaml_file)
            # if cell_type_classifier mode sor no multi class mode available
            # self.using_multi_class = 1
        # used only for cell type classifier
        self.n_windows_len_to_keep_by_cell = kwargs.get("n_windows_len_to_keep_by_cell", 2)

        # used to avoid that a given frame is not added in segments used to learn cell type
        # could be useful if movies are concatenated. Another method is to use doubtful_frames
        # when creating cinac files using the GUI.
        self.frames_to_avoid_for_cell_type = kwargs.get("frames_to_avoid_for_cell_type", [])

        self.n_epochs = kwargs.get("n_epochs", 30)
        # multiplying by the number of gpus used as batches will be distributed to each GPU
        self.batch_size = kwargs.get("batch_size", 8) * self.n_gpus

        self.window_len = kwargs.get("window_len", 100)
        self.max_width = kwargs.get("max_width", 25)
        self.max_height = kwargs.get("max_height", 25)
        self.max_n_transformations = kwargs.get("max_n_transformations", 6)  # TODO: 6
        self.pixels_around = kwargs.get("pixels_around", 0)
        self.with_augmentation_for_training_data = kwargs.get("with_augmentation_for_training_data", True)
        self.buffer = kwargs.get("buffer", 1)
        # between training, validation and test data So far test data is not taking in consideration
        self.split_values = kwargs.get("split_values", (0.8, 0.2, 0))
        if self.using_multi_class > 1:
            self.loss_fct = 'categorical_crossentropy'
        else:
            self.loss_fct = 'binary_crossentropy'

        self.with_learning_rate_reduction = kwargs.get("with_learning_rate_reduction", True)
        self.learning_rate_reduction_patience = kwargs.get("learning_rate_reduction_patience", 2)
        # first learning rate value, could be decreased later if with_learning_rate_reduction is set to True
        self.learning_rate_start = kwargs.get("learning_rate_start", 0.001)
        self.with_model_check_point = kwargs.get("with_model_check_point", True)

        self.verbose = kwargs.get("verbose", 2)

        # ---------------------------
        # Model related (used to build the model)
        # ---------------------------
        self.overlap_value = kwargs.get("overlap_value", 0.9)  # TODO: 0.9
        self.dropout_value = kwargs.get("dropout_value", 0.5)
        self.dropout_value_rnn = kwargs.get("dropout_value_rnn", 0.5)
        self.dropout_at_the_end = kwargs.get("dropout_at_the_end", 0)
        self.with_batch_normalization = kwargs.get("with_batch_normalization", False)
        self.optimizer_choice = kwargs.get("optimizer_choice", "RMSprop")  # "SGD"  used to be "RMSprop"  "Adam", SGD
        self.activation_fct = kwargs.get("activation_fct", "swish")
        self.without_bidirectional = kwargs.get("without_bidirectional", False)
        # the dimensionality of the output space (i.e. the number of filters in the convolution)
        # sequence of 4 integers, representing the filters of the 4 convolution layers
        self.conv_filters = kwargs.get("conv_filters", (64, 64, 128, 128))
        if len(self.conv_filters) != 4:
            raise Exception(f"conv_filters should be of length 4, you gave {self.conv_filters}")
        # TODO: try 256, 256, 256
        self.lstm_layers_size = kwargs.get("lstm_layers_size", (128, 256)) # TODO: 128, 256 # 128, 256, 512
        self.bin_lstm_size = kwargs.get("bin_lstm_size", 256)
        self.use_bin_at_al_version = kwargs.get("use_bin_at_al_version", True)  # TODO: True
        self.apply_attention = kwargs.get("apply_attention", True)  # TODO: True
        self.apply_attention_before_lstm = kwargs.get("apply_attention_before_lstm", True)
        self.use_single_attention_vector = kwargs.get("use_single_attention_vector", False)

        self.with_early_stopping = kwargs.get("with_early_stopping", True)
        self.early_stop_patience = kwargs.get("early_stop_patience", 15)  # 10
        self.model_descr = kwargs.get("model_descr", "")
        self.with_shuffling = kwargs.get("with_shuffling", True)
        self.seed_value = kwargs.get("seed_value", 42)  # use None to not use seed
        # main_ratio_balance = (0.6, 0.2, 0.2)
        self.main_ratio_balance = kwargs.get("main_ratio_balance", (0.7, 0.2, 0.1))
        self.crop_non_crop_ratio_balance = kwargs.get("crop_non_crop_ratio_balance", (-1, -1)) # (0.8, 0.2)
        self.non_crop_ratio_balance = kwargs.get("non_crop_ratio_balance", (-1, -1))  # (0.85, 0.15)
        # Maximum number of processes to spin up when using process-based threading
        self.workers = kwargs.get("workers", 10)

        self.results_path = kwargs.get("results_path", None)
        if self.results_path is None:
            raise Exception("You must set a results_path to indicate where to save the network files")

        # will be set in self.prepare_model()
        self.parallel_model = None

        if self.cell_type_classifier_mode:
            self.movie_patch_generator = \
                MoviePatchGeneratorForCellType(window_len=self.window_len, max_width=self.max_width,
                                               max_height=self.max_height,
                                               pixels_around=self.pixels_around,
                                               buffer=self.buffer,
                                               using_multi_class=self.using_multi_class,
                                               with_all_pixels=False,
                                               cell_type_classifier_mode=self.cell_type_classifier_mode)
        else:
            self.movie_patch_generator = \
                MoviePatchGeneratorMaskedVersions(window_len=self.window_len, max_width=self.max_width,
                                                  max_height=self.max_height,
                                                  pixels_around=self.pixels_around,
                                                  buffer=self.buffer, with_neuropil_mask=True,
                                                  using_multi_class=self.using_multi_class,
                                                  cell_type_classifier_mode=self.cell_type_classifier_mode)
        # number of inputs that take our model
        self.n_inputs = self.movie_patch_generator.n_inputs

        # data (instances of MoviePatchData) used for training and validating the classifier
        # will be split between training and data according to self.split_values when running the model
        self.inputs_list = []
        # list of tuple containing an instance of cinac_file_reader and a segment (tuple of 3 int)
        # to use to build training and validation data
        self.cinac_file_readers_and_segments = []
        self.cinac_file_readers_cells_dict = dict()
        # should be the same length of self.cinac_file_readers_and_segments or empty
        # associate to each cinac_file an ID. An ID can be common to several cinac_file
        # will be used to segregate the data, so the ID with less data will be more augmented
        self.session_ids = []
        # keep the count of frames in ground truth data
        self.total_frames_as_ground_truth = 0
        self.train_data_list = []
        self.validation_data_list = []
        self.input_shape = None
        self.training_generator = None
        self.validation_generator = None

        # Set a learning rate annealer
        # from: https://www.kaggle.com/shahariar/keras-swish-activation-acc-0-996-top-7
        self.learning_rate_reduction = ReduceLROnPlateau(monitor='val_acc',
                                                    patience=self.learning_rate_reduction_patience,
                                                    verbose=1,
                                                    factor=0.5,
                                                    mode='max',
                                                    min_lr=1e-8)  # used to be: 1e-4 and before 1e-5

        # callbacks to be execute during training
        # A callback is a set of functions to be applied at given stages of the training procedure.
        self.callbacks_list = []

    def load_cell_type_categories_from_yaml_file(self, yaml_file):
        """
        Load cell type names from a yaml file. If more than 2 type cells are given, then a multi-class
        classifier will be used. If 2 type cells are given, then either it could be multi-class or binary classifier,
        then this choice should be given in the parameters of CinacModel.
        If 2 cell-type are given, for binary classifier, it should be precised which cell type should be predicted
        if we get more than 0.5 probability.
        Args:
            yaml_file:

        Returns:

        """

        cell_type_from_code_dict, cell_type_to_code_dict, multi_class_arg = \
            read_cell_type_categories_yaml_file(yaml_file=yaml_file, using_multi_class=self.using_multi_class)

        self.cell_type_from_code_dict = cell_type_from_code_dict
        self.cell_type_to_code_dict = cell_type_to_code_dict
        n_cell_categories = len(cell_type_from_code_dict)

        if n_cell_categories < 2:
            raise Exception(f"You need at least 2 cell_type categories, you provided {n_cell_categories}: "
                            f"{list(self.cell_type_from_code_dict.values())}")

        if multi_class_arg is not None:
            if multi_class_arg or (n_cell_categories > 2):
                self.using_multi_class = n_cell_categories
            else:
                self.using_multi_class = 1
        else:
            if n_cell_categories > 2:
                self.using_multi_class = n_cell_categories
            else:
                self.using_multi_class = 1

        # print(f"n_cell_categories {n_cell_categories}")
        # print(f"self.cell_type_from_code_dict {self.cell_type_from_code_dict}")
        # print(f"self.cell_type_to_code_dict {self.cell_type_to_code_dict}")
        # print(f"self.using_multi_class {self.using_multi_class}")

    def add_input_data_from_dir(self, dir_name, verbose=0):
        """
        Add input data loading all .cinac file in dir_name
        If a (UTF-8 encoded) txt file is in the dir, it is parsed in order to give to each cinac_file an id
        the format is for each line:
        cinac_file_name: id
        Args:
            dir_name: str, path + directory from which to load .cinac files
            verbose: 0 no print, 1 informations are printed

        Returns:

        """

        cinac_path_w_file_names = []
        frames_to_keep_dict = None
        cinac_file_names = []
        text_file = None
        # look for filenames in the fisrst directory, if we don't break, it will go through all directories
        for (dirpath, dirnames, local_filenames) in os.walk(dir_name):
            cinac_path_w_file_names = [os.path.join(dirpath, f) for f in local_filenames if f.endswith(".cinac")]
            cinac_file_names = [f for f in local_filenames if f.endswith(".cinac")]
            text_files = [os.path.join(dirpath, f) for f in local_filenames if f.endswith(".txt")]
            if len(text_files) > 0:
                text_file = text_files[0]
            break

        session_ids = None
        if text_file is not None:
            if "frames" in text_file:
                frames_to_keep_dict = dict()
                with open(text_file, "r", encoding='UTF-8') as file:
                    for line_index, line in enumerate(file):
                        line_list = line.split(':')
                        if len(line_list) < 2:
                            continue
                        frames = line_list[1].strip()
                        cinac_file = line_list[0].strip()
                        frames_list = frames.split()
                        first_frame = int(frames_list[0])
                        last_frame = int(frames_list[1])
                        frames_to_keep_dict[cinac_file] = (first_frame, last_frame)
            else:
                session_ids_dict = dict()
                with open(text_file, "r", encoding='UTF-8') as file:
                    for line_index, line in enumerate(file):
                        line_list = line.split(':')
                        if len(line_list) < 2:
                            continue
                        session_id = line_list[1].strip()
                        cinac_file = line_list[0].strip()
                        session_ids_dict[cinac_file] = session_id

                if len(session_ids_dict) > 0:
                    session_ids = []
                    for file_name in cinac_file_names:
                        if file_name in session_ids_dict:
                            session_ids.append(session_ids_dict[file_name])
                        else:
                            # by default we could put None, then all the cinac segment with None will have the same id
                            # here we give the name of the file
                            session_ids.append(file_name)

        if len(cinac_path_w_file_names) > 0:
            self.add_input_data(cinac_file_names=cinac_path_w_file_names, session_ids=session_ids,
                                frames_to_keep_dict=frames_to_keep_dict, verbose=verbose)

    def add_input_data(self, cinac_file_names, session_ids=None, frames_to_keep_dict=None, verbose=0):
        """
        Add input data.
        Args:
            cinac_file_name: str or list of str, represents the files .cinac
            session_ids: None if no session_id otherwise a tuple, list or just a string (or int) representing the
            id of each cinac_file (one id can be common to several cinac_file)
            frames_to_keep_dict: key is cinac_file_name, and value a tuple of 2 int representing the first and last frame
            to keep. Only valid if all segment have the same indices. Useful to vary the number of frames given to cell
            type classifier. If the dict is None, then all the frames are being used.
            verbose: 0 no print, 1 informations are printed

        Returns:

        """
        if isinstance(cinac_file_names, str):
            cinac_file_names = [cinac_file_names]
        if session_ids is not None:
            if (not isinstance(session_ids, list)) and (not isinstance(session_ids, tuple)):
                session_ids = [session_ids]
            if len(session_ids) != len(cinac_file_names):
                session_ids = None
        for index_file, cinac_file_name in enumerate(cinac_file_names):
            if verbose > 0:
                print(f"Creating CinacFileReader for {os.path.basename(cinac_file_name)}")
            frames_to_keep = None
            if frames_to_keep_dict is not None:
                if cinac_file_name in frames_to_keep_dict:
                    base_name = os.path.basename(cinac_file_name)
                    frames_to_keep = frames_to_keep_dict[base_name]
            cinac_file_reader = CinacFileReader(file_name=cinac_file_name, frames_to_keep=frames_to_keep)
            segments_list = cinac_file_reader.get_all_segments()

            # a segment represent a cell and given frames with their corresponding ground truth
            # segment is a tuple of 3 int (cell, first_frame, last_frame)
            for segment in segments_list:
                if self.cell_type_classifier_mode:
                    # then we first make sure cell_type is available for the given segment
                    if cinac_file_reader.get_segment_cell_type(segment=segment) is None:
                        continue
                self.cinac_file_readers_and_segments.append((cinac_file_reader, segment))

                # using file_name + cell to ID every cell, in order to split cell between training and validation
                # set when cell_type_classifier_mode
                if cinac_file_name + str(segment[0]) not in self.cinac_file_readers_cells_dict:
                    self.cinac_file_readers_cells_dict[cinac_file_name + str(segment[0])] = []
                self.cinac_file_readers_cells_dict[cinac_file_name + str(segment[0])].append((cinac_file_reader,
                                                                                              segment))
                if session_ids is not None:
                    self.session_ids.append(session_ids[index_file])
                raster_dur = cinac_file_reader.get_segment_raster_dur(segment=segment)
                # keeping the count of the number of frames available,
                # useful for splitting in training and validation

                self.total_frames_as_ground_truth += len(raster_dur)

    def __build_model(self):
        """

        Returns:

        """

        """
        Attributes used:
        :param input_shape:
        :param lstm_layers_size:
        :param n_inputs:
        :param using_multi_class:
        :param bin_lstm_size:
        :param activation_fct:
        :param dropout_at_the_end: From Li et al. 2018 to avoid disharmony between batch normalization and dropout,
        if batch is True, then we should add dropout only on the last step before the sigmoid or softmax activation
        :param dropout_value:
        :param dropout_value_rnn:
        :param without_bidirectional:
        :param with_batch_normalization:
        :param apply_attention:
        :param apply_attention_before_lstm:
        :param use_single_attention_vector:
        :param use_bin_at_al_version:
        :param conv_filters
        :return:
        """

        # n_frames represent the time-steps
        n_frames = self.input_shape[0]

        ##########################################################################
        #######################" VISION MODEL ####################################
        ##########################################################################
        # First, let's define a vision model using a Sequential model.
        # This model will encode an image into a vector.
        # TODO: Try dilated CNN
        # VGG-like convnet model
        vision_model = Sequential()
        get_custom_objects().update({'swish': Swish(swish)})
        # to choose between swish and relu

        # TODO: Try dilation_rate=2 argument for Conv2D
        # TODO: Try changing the number of filters like 32 and then 64 (instead of 64 -> 128)
        vision_model.add(Conv2D(self.conv_filters[0], (3, 3), padding='same', input_shape=self.input_shape[1:]))
        if self.activation_fct != "swish":
            vision_model.add(Activation(self.activation_fct))
        else:
            vision_model.add(Lambda(swish))
        if self.with_batch_normalization:
            vision_model.add(BatchNormalization())
        vision_model.add(Conv2D(self.conv_filters[1], (3, 3)))
        if self.activation_fct != "swish":
            vision_model.add(Activation(self.activation_fct))
        else:
            vision_model.add(Lambda(swish))
        if self.with_batch_normalization:
            vision_model.add(BatchNormalization())
        # TODO: trying AveragePooling
        vision_model.add(MaxPooling2D((2, 2)))

        vision_model.add(Conv2D(self.conv_filters[2], (3, 3), padding='same'))
        if self.activation_fct != "swish":
            vision_model.add(Activation(self.activation_fct))
        else:
            vision_model.add(Lambda(swish))
        vision_model.add(Conv2D(self.conv_filters[3], (3, 3)))
        if self.activation_fct != "swish":
            vision_model.add(Activation(self.activation_fct))
        else:
            vision_model.add(Lambda(swish))
        if self.with_batch_normalization:
            vision_model.add(BatchNormalization())
        vision_model.add(MaxPooling2D((2, 2)))

        # vision_model.add(Conv2D(256, (3, 3), activation=activation_fct, padding='same'))
        # vision_model.add(Conv2D(256, (3, 3), activation=activation_fct))
        # vision_model.add(Conv2D(256, (3, 3), activation=activation_fct))
        # vision_model.add(MaxPooling2D((2, 2)))
        # TODO: see to add Dense layer with Activation
        vision_model.add(Flatten())
        # size 2048
        # vision_model.add(Dense(2048))
        # if activation_fct != "swish":
        #     vision_model.add(Activation(activation_fct))
        # else:
        #     vision_model.add(Lambda(swish))
        # vision_model.add(Dense(2048))
        # if activation_fct != "swish":
        #     vision_model.add(Activation(activation_fct))
        # else:
        #     vision_model.add(Lambda(swish))

        if self.dropout_value > 0:
            vision_model.add(layers.Dropout(self.dropout_value))

        ##########################################################################
        # ######################" END VISION MODEL ################################
        ##########################################################################

        ##########################################################################
        # ####################### BiDirectionnal LSTM ############################
        ##########################################################################
        # inputs are the original movie patches
        inputs = []
        # encoded inputs are the outputs of each encoded inputs after BD LSTM
        encoded_inputs = []

        for input_index in np.arange(self.n_inputs):
            video_input = Input(shape=self.input_shape, name=f"input_{input_index}")
            inputs.append(video_input)
            # This is our video encoded via the previously trained vision_model (weights are reused)
            encoded_frame_sequence = TimeDistributed(vision_model)(video_input)  # the output will be a sequence of vectors

            if self.apply_attention and self.apply_attention_before_lstm:
                # adding attention mechanism
                encoded_frame_sequence = attention_3d_block(inputs=encoded_frame_sequence, time_steps=n_frames,
                                                            use_single_attention_vector=self.use_single_attention_vector)

            for lstm_index, lstm_size in enumerate(self.lstm_layers_size):
                if lstm_index == 0:
                    rnn_input = encoded_frame_sequence
                else:
                    rnn_input = encoded_video

                return_sequences = True
                # if apply_attention and (not apply_attention_before_lstm):
                #     return_sequences = True
                # elif use_bin_at_al_version:
                #     return_sequences = True
                # elif using_multi_class <= 1:
                #     return_sequences = (lstm_index < (len(lstm_layers_size) - 1))
                # else:
                #     return_sequences = True
                if self.without_bidirectional:
                    encoded_video = LSTM(lstm_size, dropout=self.dropout_value_rnn,
                                         recurrent_dropout=self.dropout_value_rnn,
                                         return_sequences=return_sequences)(rnn_input)
                    # From Bin et al. test adding merging LSTM results + CNN representation then attention
                    if self.use_bin_at_al_version:
                        encoded_video = layers.concatenate([encoded_video, encoded_frame_sequence])
                else:
                    # there was a bug here, recurrent_dropout was taking return_sequences as value
                    encoded_video = Bidirectional(LSTM(lstm_size, dropout=self.dropout_value_rnn,
                                                       recurrent_dropout=self.dropout_value_rnn,
                                                       return_sequences=return_sequences), merge_mode='concat', )(rnn_input)
                    # From Bin et al. test adding merging LSTM results + CNN represnetation then attention
                    if self.use_bin_at_al_version:
                        encoded_video = layers.concatenate([encoded_video, encoded_frame_sequence])

            # TODO: test if GlobalMaxPool1D +/- dropout is useful here ?
            # encoded_video = GlobalMaxPool1D()(encoded_video)
            # encoded_video = Dropout(0.25)(encoded_video)
            # We can either apply attention a the end of each LSTM, or do it after the concatenation of all of them
            # it's the same if there is only one encoded_input
            # if apply_attention and (not apply_attention_before_lstm):
            #     # adding attention mechanism
            #     encoded_video = attention_3d_block(inputs=encoded_video, time_steps=n_frames,
            #                                        use_single_attention_vector=use_single_attention_vector)
            #     if using_multi_class <= 1:
            #         encoded_video = Flatten()(encoded_video)
            encoded_inputs.append(encoded_video)

        if len(encoded_inputs) == 1:
            merged = encoded_inputs[0]
        else:
            # TODO: try layers.Average instead of concatenate
            merged = layers.concatenate(encoded_inputs)
        # From Bin et al. test adding a LSTM here that will take merged as inputs + CNN represnetation (as attention)
        # Return sequences will have to be True and activate the CNN representation
        if self.use_bin_at_al_version:
            # next lines commented, seems like it didn't help at all
            # if with_batch_normalization:
            #     merged = BatchNormalization()(merged)
            # if dropout_rate > 0:
            #     merged = layers.Dropout(dropout_rate)(merged)

            merged = LSTM(self.bin_lstm_size, dropout=self.dropout_value_rnn,
                          recurrent_dropout=self.dropout_value_rnn,
                          return_sequences=True)(merged)
            # print(f"merged.shape {merged.shape}")
            if self.apply_attention and (not self.apply_attention_before_lstm):
                # adding attention mechanism
                merged = attention_3d_block(inputs=merged, time_steps=n_frames,
                                            use_single_attention_vector=self.use_single_attention_vector)
            if self.using_multi_class <= 1 or self.cell_type_classifier_mode:
                merged = Flatten()(merged)

        # TODO: test those 7 lines (https://www.kaggle.com/amansrivastava/exploration-bi-lstm-model)
        # number_dense_units = 1024
        # merged = Dense(number_dense_units)(merged)
        # merged = Activation(activation_fct)(merged)
        if self.with_batch_normalization:
            merged = BatchNormalization()(merged)
        if self.dropout_value > 0:
            merged = (layers.Dropout(self.dropout_value))(merged)
        elif self.dropout_at_the_end > 0:
            merged = (layers.Dropout(self.dropout_at_the_end))(merged)
        # dropout_at_the_end: From Li et al. 2018 to avoid disharmony between batch normalization and dropout,
        # if batch is True, then we should add dropout only on the last step before the sigmoid or softmax activation

        # if we use TimeDistributed then we need to return_sequences during the last LSTM
        if self.using_multi_class <= 1:
            # if use_bin_at_al_version:
            #     outputs = TimeDistributed(Dense(1, activation='sigmoid'))(merged)
            # else:
            if self.cell_type_classifier_mode:
                outputs = Dense(1, activation='sigmoid')(merged)
            else:
                outputs = Dense(n_frames, activation='sigmoid')(merged)
            # outputs = TimeDistributed(Dense(1, activation='sigmoid'))(merged)
        else:
            if self.cell_type_classifier_mode:
                outputs = Dense(self.using_multi_class, activation='softmax')(merged)
            else:
                outputs = TimeDistributed(Dense(self.using_multi_class, activation='softmax'))(merged)
        if len(inputs) == 1:
            print(f"len(inputs) {len(inputs)}")
            inputs = inputs[0]

        # print("Creating Model instance")
        video_model = Model(inputs=inputs, outputs=outputs)
        # print("After Creating Model instance")

        return video_model

    def _split_and_stratify_cell_type_mode_data(self, seed_value=None, verbose=0):
        """
        Split (between validation and training) and stratify the data, should be
        used when self.cell_type_classifier_mode is True
        Args:
            seed_value:

        Returns:

        """
        # we want don't want a same cell to be both in validation and training
        # also we want an equivalent number of frames of both cell types in each side
        # now we need to split the data between training and validation

        # how many frames to add for each cell, as a multiplier of window_len
        n_windows_len_to_keep_by_cell = self.n_windows_len_to_keep_by_cell

        # key is a string representing the cell type, value is the number of frames
        cell_type_frame_count_dict = dict()
        for key, data_list in self.cinac_file_readers_cells_dict.items():
            for data_cell in data_list:
                cinac_file_reader, segment = data_cell
                cell_type = cinac_file_reader.get_segment_cell_type(segment=segment)
                cell_type = cell_type.lower().strip()
                # raster_dur = cinac_file_reader.get_segment_raster_dur(segment=segment)
                # n_frames_segment = len(raster_dur)
            cell_type_frame_count_dict[cell_type] = cell_type_frame_count_dict.get(cell_type, 0) + \
                                                    (n_windows_len_to_keep_by_cell * self.window_len)

        cell_segments_keys = list(self.cinac_file_readers_cells_dict.keys())
        n_cells = len(cell_segments_keys)
        cells_order = np.arange(n_cells)
        if seed_value is not None:
            np.random.seed(seed_value)
        # randomising the order in which we put cells in training or validation training
        np.random.shuffle(cells_order)
        # counting how many frames should be added for training
        # key is cell_type, value is an int representing the number of frames for each cell_type
        n_frames_for_training_dict = dict()
        n_frames_added_so_far_dict = dict()
        for cell_type, frame_count in cell_type_frame_count_dict.items():
            n_frames_for_training_dict[cell_type] = int(self.split_values[0] * frame_count)
            n_frames_added_so_far_dict[cell_type] = 0

        cell_types = list(cell_type_frame_count_dict.keys())

        cell_types_code = set()
        for cell_type in cell_types:
            if cell_type.lower().strip() not in self.cell_type_to_code_dict:
                raise Exception(f"'{cell_type}' is not a valid cell type, cell type should be one of those: "
                                f"{list(self.cell_type_to_code_dict.keys())}")
            cell_types_code.add(self.cell_type_to_code_dict[cell_type.lower().strip()])
        # if len(cell_types_code) > 2:
        #     raise Exception(f"The maximum number of different cell types is 2 for now, "
        #                     f"you have {len(cell_types_code)} types, "
        #                     f"which are: {[self.cell_type_from_code_dict[code] for code in cell_types_code]} ")

        using_splitted_tiff_cinac_movie = False

        if using_splitted_tiff_cinac_movie:
            if self.tiffs_dirname is None:
                raise Exception("You need to pass an argument named 'tiffs_dirname' to CinacModel when instantiating it. "
                                "It represents the path where to save the tiffs as individual tiff for each frame. ")
            # we're having a first loop to make sure the cinac file movie frames have already been
            # created in the hardrive has separeted file in order to save memory
            all_already_loaded = True
            for cell_segments_key in cell_segments_keys:
                for data_cell in self.cinac_file_readers_cells_dict[cell_segments_key]:
                    cinac_file_reader, segment = data_cell
                    identifier = f"{cinac_file_reader.base_name}_{segment[0]}_{segment[1]}_{segment[2]}"
                    cinac_recording = CinacRecording(identifier=identifier)
                    is_created = check_one_tiff_file_by_frame_exists(identifiers=[identifier],
                                                                     results_path=self.tiffs_dirname)
                    if not is_created:
                        movie_data = cinac_file_reader.get_segment_ci_movie(segment=segment)
                        if movie_data is None:
                            continue
                        cinac_movie = CinacSplitedTiffMovie(identifier=identifier,
                                                            already_normalized=True,
                                                            tiffs_dirname=self.tiffs_dirname, tiff_movie=movie_data)
                        all_already_loaded = False
            if not all_already_loaded:
                raise Exception("All calcium movie in cinac files were not available as single frame tiffs. "
                                "Those have been created, you to relaunch the code now. ")

        for cell_segments_key in cell_segments_keys:
            # we use this variable to make a sure a same cell is added to training or validation but not both
            # the count of total number of frames added is updated only after each cell segments have been added
            n_frames_for_this_cell = 0
            cell_type = None
            for data_cell in self.cinac_file_readers_cells_dict[cell_segments_key]:
                cinac_file_reader, segment = data_cell

                identifier = f"{cinac_file_reader.base_name}_{segment[0]}_{segment[1]}_{segment[2]}"
                cinac_recording = CinacRecording(identifier=identifier)
                # movie_data = cinac_file_reader.get_segment_ci_movie(segment=segment)
                # if movie_data is None:
                #     continue
                # cinac_movie = CinacDataMovie(movie=movie_data, already_normalized=True)
                if using_splitted_tiff_cinac_movie:
                    if self.tiffs_dirname is None:
                        raise Exception(
                            "You need to pass an argument named 'tiffs_dirname' to CinacModel when instantiating it. "
                            "It represents the path where to save the tiffs as individual tiff for each frame. ")
                    cinac_movie = CinacSplitedTiffMovie(identifier=identifier,
                                                        tiffs_dirname=self.tiffs_dirname)
                else:
                    cinac_movie = CinacFileReaderMovie(cinac_file_reader=cinac_file_reader,
                                                       segment=segment)
                cinac_recording.set_movie(cinac_movie)

                coords_data = cinac_file_reader.get_segment_cells_contour(segment=segment)
                coords_data = [np.vstack((coord_data[0], coord_data[1])) for coord_data in coords_data]
                invalid_cells = cinac_file_reader.get_segment_invalid_cells(segment=segment)
                # invalid_cells binary array same length as the number of cell, 1 if the cell is invalid
                # invalid cells allows to remove contours, so the classifier don't take it in consideration
                if np.sum(invalid_cells) > 0:
                    new_coords_data = []
                    for cell_index, cell_coord in enumerate(coords_data):
                        if invalid_cells[cell_index] > 0:
                            continue
                        new_coords_data.append(cell_coord)
                    coords_data = new_coords_data
                cinac_recording.set_rois_2d_array(coord=coords_data, from_matlab=False)

                raster_dur = cinac_file_reader.get_segment_raster_dur(segment=segment)
                doubtful_frames = cinac_file_reader.get_segment_doubtful_frames(segment=segment)
                if len(self.frames_to_avoid_for_cell_type) > 0:
                    # we update doubtful_frames
                    if doubtful_frames is None:
                        doubtful_frames = np.zeros(raster_dur.shape, dtype="int8")
                    for frame_to_avoid in self.frames_to_avoid_for_cell_type:
                        if frame_to_avoid < len(doubtful_frames):
                            doubtful_frames[frame_to_avoid] = 1
                cell_type = cinac_file_reader.get_segment_cell_type(segment=segment)
                smooth_traces = cinac_file_reader.get_segment_smooth_traces(segment=segment)
                # raw_traces = cinac_file_reader.get_segment_raw_traces(segment=segment)
                n_frames = len(raster_dur)
                if n_frames < self.window_len:
                    # making sure the segment has the minimum number of frames
                    continue

                cell_type = cell_type.lower().strip()
                cinac_recording.cell_type = cell_type

                # allow to split the data between training and validation
                if n_frames_added_so_far_dict[cell_type] < n_frames_for_training_dict[cell_type]:
                    # then we add data to training
                    frames_step = int(np.ceil(self.window_len * (1 - self.overlap_value)))
                    data_list_to_use = self.train_data_list
                else:
                    # not temporal overlap for validation data, we don't want to do data augmentation
                    frames_step = self.window_len
                    data_list_to_use = self.validation_data_list

                # temporal overlap for data augmentation
                indices_movies = np.arange(0, n_frames, frames_step)

                # list of  int representing the first_frame possible candidate
                # for moviepatch to add for training or validation. We want to keep for each cell only the most active
                # one
                first_frames_to_filter = []

                for i, index_movie in enumerate(indices_movies):
                    break_it = False
                    first_frame = index_movie
                    if (index_movie + self.window_len) == n_frames:
                        break_it = True
                    elif (index_movie + self.window_len) > n_frames:
                        # in case the number of frames is not divisible by sliding_window_len
                        first_frame = n_frames - self.window_len
                        break_it = True
                    # if some frames have been marked as doubtful, we remove them of the training dataset
                    if doubtful_frames is not None:
                        if np.sum(doubtful_frames[np.arange(first_frame, first_frame + self.window_len)]) > 0:
                            continue
                    first_frames_to_filter.append(first_frame)
                    if break_it:
                        break

                # we want to select at least a first_frame to create a moviePatch
                # the idea is to sort the first_frame and the segment that goes with (adding self.window_len)
                # according to the activity of the cell, we're looking for the segment with the highest amplitude peaks
                first_frames_selected = []
                # will contain a score representing the avg amplitude of the highest peaks
                avg_peaks_amplitudes = []

                peaks, properties = scipy.signal.find_peaks(x=smooth_traces, distance=2)
                peak_nums = np.zeros(n_frames, dtype="int8")
                peak_nums[peaks] = 1
                for first_frame in first_frames_to_filter:
                    peaks = np.where(peak_nums[first_frame:first_frame+self.window_len])[0] + first_frame
                    if len(peaks) == 0:
                        # no peaks found
                        avg_peaks_amplitudes.append(0)
                    amplitudes = smooth_traces[peaks]
                    # print(f"len(amplitudes) {len(amplitudes)}")
                    # print(f"amplitudes {amplitudes}")
                    amplitude_threshold = np.percentile(amplitudes, 90)
                    highest_amplitudes = amplitudes[amplitudes >= amplitude_threshold]
                    # print(f"len(highest_amplitudes) {len(highest_amplitudes)}, "
                    #       f"mean {np.round(np.mean(highest_amplitudes), 2)}")
                    avg_peaks_amplitudes.append(np.mean(highest_amplitudes))
                first_frames_order = np.argsort(avg_peaks_amplitudes)
                # from highest to the smallest
                first_frames_order = first_frames_order[::-1]
                # print(f"avg_peaks_amplitudes ordered {np.array(avg_peaks_amplitudes)[first_frames_order]}")
                n_first_frames_to_peak = min(len(first_frames_order), n_windows_len_to_keep_by_cell)
                for index_first_frame in first_frames_order[:n_first_frames_to_peak]:
                    first_frames_selected.append(first_frames_to_filter[index_first_frame])
                n_frames_added = 0
                for first_frame in first_frames_selected:
                    # the cell of interest in the segment is always the cell 0
                    movie_data = MoviePatchData(cinac_recording=cinac_recording, cell=0, index_movie=first_frame,
                                                window_len=self.window_len, session_id=None,
                                                max_n_transformations=self.max_n_transformations,
                                                with_info=None,
                                                cell_type_classifier_mode=self.cell_type_classifier_mode,
                                                encoded_frames=None, decoding_frame_dict=None,
                                                # TODO: see if we can mark which cinac_file to keep absolutely
                                                to_keep_absolutely=False,
                                                ground_truth=self.cell_type_to_code_dict[cell_type.lower().strip()])

                    # adding the data to the training or validation list
                    data_list_to_use.append(movie_data)
                    n_frames_added += self.window_len


                n_frames_for_this_cell += n_frames_added
            if cell_type is not None:
                n_frames_added_so_far_dict[cell_type] += n_frames_for_this_cell


        # in case self.validation_data_list would be empty, we take from training to fill it
        # if enough data are given for training, this shouldn't happen
        if len(self.validation_data_list) == 0:
            raise Exception("self.validation_data_list is empty, probably not enough data has been added as inputs")

        # just to display stat, doesn't modify the data
        if verbose == 1:
            print(f"VALIDATION DATA")
            StratificationCellTypeCamembert(data_list=self.validation_data_list,
                                            description="VALIDATION DATA",
                                            n_max_transformations=6,
                                            debug_mode=True)

        n_max_transformations = self.train_data_list[0].n_available_augmentation_fct

        print("TRAINING DATA")
        # using StratificationDataProcessor in order to stratify the data, so we balance it
        strat_process = StratificationCellTypeDataProcessor(data_list=self.train_data_list,
                                                            n_max_transformations=n_max_transformations,
                                                            description="TRAINING DATA",
                                                            debug_mode=False)
        self.train_data_list = strat_process.get_new_data_list()

    def _split_and_stratify_data(self, seed_value=None, verbose=0):
        """
        Split (between validation and training) and stratify the data
        Args:
            seed_value:

        Returns:

        """
        if self.cell_type_classifier_mode:
            self._split_and_stratify_cell_type_mode_data(seed_value=seed_value, verbose=verbose)
            return

        using_splitted_tiff_cinac_movie = False

        if using_splitted_tiff_cinac_movie:
            if self.tiffs_dirname is None:
                raise Exception(
                    "You need to pass an argument named 'tiffs_dirname' to CinacModel when instantiating it. "
                    "It represents the path where to save the tiffs as individual tiff for each frame. ")
            # we're having a first loop to make sure the cinac file movie frames have already been
            # created in the hardrive has separeted file in order to save memory
            all_already_loaded = True
            for cinac_file_index, data in enumerate(self.cinac_file_readers_and_segments):
                cinac_file_reader, segment = data
                identifier = f"{cinac_file_reader.base_name}_{segment[0]}_{segment[1]}_{segment[2]}"
                # cinac_recording = CinacRecording(identifier=identifier)
                is_created = check_one_tiff_file_by_frame_exists(identifiers=[identifier],
                                                                 results_path=self.tiffs_dirname)
                if not is_created:
                    movie_data = cinac_file_reader.get_segment_ci_movie(segment=segment)
                    if movie_data is None:
                        continue
                    cinac_movie = CinacSplitedTiffMovie(identifier=identifier,
                                                        already_normalized=True,
                                                        tiffs_dirname=self.tiffs_dirname, tiff_movie=movie_data)
                    all_already_loaded = False
            if not all_already_loaded:
                raise Exception("All calcium movie in cinac files were not available as single frame tiffs. "
                                "Those have been created, you to relaunch the code now. ")

        # now we need to split the data between training and validation
        n_segments = len(self.cinac_file_readers_and_segments)
        segments_order = np.arange(n_segments)
        if seed_value is not None:
            np.random.seed(seed_value)
        np.random.shuffle(segments_order)
        # counting how many frames should be added for training
        n_frames_for_training = int(self.split_values[0]*self.total_frames_as_ground_truth)
        n_frames_added_so_far = 0
        for cinac_file_index, data in enumerate(self.cinac_file_readers_and_segments):
            cinac_file_reader, segment = data
            # raster_dur represents the ground truth, a binary 1d array, 1 for each frame during
            # which the cell is active
            if self.session_ids is None or (len(self.session_ids) == 0):
                session_id = None
            else:
                session_id = self.session_ids[cinac_file_index]
            raster_dur = cinac_file_reader.get_segment_raster_dur(segment=segment)
            smooth_traces = cinac_file_reader.get_segment_smooth_traces(segment=segment)
            raw_traces = cinac_file_reader.get_segment_raw_traces(segment=segment)
            doubtful_frames = cinac_file_reader.get_segment_doubtful_frames(segment=segment)

            # identifier is base on file_nae, then cell, first and last frame of the segment
            identifier = f"{cinac_file_reader.base_name}_{segment[0]}_{segment[1]}_{segment[2]}"
            cinac_recording = CinacRecording(identifier=identifier)
            if using_splitted_tiff_cinac_movie:
                if self.tiffs_dirname is None:
                    raise Exception(
                        "You need to pass an argument named 'tiffs_dirname' to CinacModel when instantiating it. "
                        "It represents the path where to save the tiffs as individual tiff for each frame. ")
                cinac_movie = CinacSplitedTiffMovie(identifier=identifier,
                                                    tiffs_dirname=self.tiffs_dirname)
            else:
                cinac_movie = CinacFileReaderMovie(cinac_file_reader=cinac_file_reader,
                                                   segment=segment)

            cinac_recording.set_movie(cinac_movie)

            coords_data = cinac_file_reader.get_segment_cells_contour(segment=segment)
            coords_data = [np.vstack((coord_data[0], coord_data[1])) for coord_data in coords_data]
            invalid_cells = cinac_file_reader.get_segment_invalid_cells(segment=segment)
            # invalid_cells binary array same length as the number of cell, 1 if the cell is invalid
            # invalid cells allows to remove contours, so the classifier don't take it in consideration
            if np.sum(invalid_cells) > 0:
                new_coords_data = []
                for cell_index, cell_coord in enumerate(coords_data):
                    if invalid_cells[cell_index] > 0:
                        continue
                    new_coords_data.append(cell_coord)
                coords_data = new_coords_data
            cinac_recording.set_rois_2d_array(coord=coords_data, from_matlab=False)

            n_frames = len(raster_dur)
            if n_frames < self.window_len:
                # making sure the segment has the minimum number of frames
                continue

            # allow to split the data between training and validation
            if n_frames_added_so_far < n_frames_for_training:
                # then we add data to training
                frames_step = int(np.ceil(self.window_len * (1 - self.overlap_value)))
                data_list_to_use = self.train_data_list
            else:
                # not temporal overlap for validation data, we don't want to do data augmentation
                frames_step = self.window_len
                data_list_to_use = self.validation_data_list

            n_frames_added_so_far += n_frames

            # temporal overlap for data augmentation
            indices_movies = np.arange(0, n_frames, frames_step)

            for i, index_movie in enumerate(indices_movies):
                break_it = False
                first_frame = index_movie
                if (index_movie + self.window_len) == n_frames:
                    break_it = True
                elif (index_movie + self.window_len) > n_frames:
                    # in case the number of frames is not divisible by sliding_window_len
                    first_frame = n_frames - self.window_len
                    break_it = True
                # if some frames have been marked as doubtful, we remove them of the training dataset
                if doubtful_frames is not None:
                    if np.sum(doubtful_frames[np.arange(first_frame, first_frame + self.window_len)]) > 0:
                        continue
                encoded_frames, decoding_frame_dict = neuronal_activity_encoding(raw_traces=raw_traces,
                                                                                 smooth_traces=smooth_traces,
                                                                                 raster_dur=raster_dur)
                # the cell of interest in the segment is always the cell 0
                movie_data = MoviePatchData(cinac_recording=cinac_recording, cell=0, index_movie=first_frame,
                                            window_len=self.window_len, session_id=session_id,
                                            max_n_transformations=self.max_n_transformations,
                                            with_info=True, encoded_frames=encoded_frames,
                                            cell_type_classifier_mode=self.cell_type_classifier_mode,
                                            decoding_frame_dict=decoding_frame_dict,
                                            # TODO: see if we can mark which cinac_file to keep absolutely
                                            to_keep_absolutely=False,
                                            ground_truth=raster_dur[first_frame:first_frame+self.window_len])

                # adding the data to the training or validation list
                data_list_to_use.append(movie_data)
                # self.total_frames_as_ground_truth += self.window_len

                if break_it:
                    break

        # in case self.validation_data_list would be empty, we take from training to fill it
        # if enough data are given for training, this shouldn't happen
        if len(self.validation_data_list) == 0:
            n_patches_in_training = len(self.train_data_list)
            patches_order = np.arange(n_patches_in_training)
            if seed_value is not None:
                np.random.seed(seed_value)
            np.random.shuffle(patches_order)
            n_patches_for_training = int(self.split_values[0] * n_patches_in_training)
            n_patches_for_validation = n_patches_in_training - n_patches_for_training
            for index in np.arange(n_patches_for_validation):
                self.validation_data_list.append(self.train_data_list[patches_order[index]])
            new_train_list = []
            for index in np.arange(n_patches_for_validation, n_patches_in_training):
                new_train_list.append(self.train_data_list[patches_order[index]])
            self.train_data_list = new_train_list

        # just to display stat, doesn't modify the data
        if verbose == 1:
            StratificationCamembert(data_list=self.validation_data_list,
                                    description="VALIDATION DATA",
                                    n_max_transformations=6,
                                    debug_mode=True)

        n_max_transformations = self.train_data_list[0].n_available_augmentation_fct

        # using StratificationDataProcessor in order to stratify the data, so we balance it
        strat_process = StratificationDataProcessor(data_list=self.train_data_list,
                                                    n_max_transformations=n_max_transformations,
                                                    description="TRAINING DATA",
                                                    debug_mode=False, main_ratio_balance=self.main_ratio_balance,
                                                    crop_non_crop_ratio_balance=self.crop_non_crop_ratio_balance,
                                                    non_crop_ratio_balance=self.non_crop_ratio_balance)
        self.train_data_list = strat_process.get_new_data_list()

    def prepare_model(self, verbose=0):
        """
        Will build the model that will be use to fit the data.
        Should be called only after the data has been set.
        Returns:

        """

        if self.total_frames_as_ground_truth == 0:
            print("No input data has been added, use add_input_data() method")
            return

        # splitting the data in train_data_list and validation_data_list and stratifying it
        self._split_and_stratify_data(verbose=verbose)
        # first building the generator that will allow the generate the data for each batch during network iterations
        params_generator = {
            'batch_size': self.batch_size,
            'window_len': self.window_len,
            'max_width': self.max_width,
            'max_height': self.max_height,
            'pixels_around': self.pixels_around,
            'buffer': self.buffer,
            'is_shuffle': True}

        self.training_generator = DataGenerator(self.train_data_list,
                                                with_augmentation=self.with_augmentation_for_training_data,
                                                movie_patch_generator=self.movie_patch_generator,
                                                **params_generator)
        self.validation_generator = DataGenerator(self.validation_data_list, with_augmentation=False,
                                                  movie_patch_generator=self.movie_patch_generator,
                                                  **params_generator)
        self.input_shape = self.training_generator.input_shape

        if self.using_multi_class > 1:
            dependencies = dict()
        else:
            dependencies = {
                'sensitivity': sensitivity,
                'specificity': specificity,
                'precision': precision
            }
            # dependencies = {
            #     'sensitivity': tf.keras.metrics.Recall(),
            #     'specificity': tf.keras.metrics.SpecificityAtSensitivity(sensitivity=0.5),
            #     'precision': tf.keras.metrics.Precision()
            # }
            # tf.keras.metrics.Recall(), tf.keras.metrics.Precision()
        if self.input_shape is None:
            raise Exception("prepare_model() cannot be called before the data has been provided to the model")
        if self.n_gpus == 1:
            print("Building the model on 1 GPU")
            if self.partly_trained_model is not None:
                model = load_model(self.partly_trained_model, custom_objects=dependencies)
            else:
                model = self.__build_model()
        else:
            print(f"Building the model on {self.n_gpus} GPU")
            # We recommend doing this with under a CPU device scope,
            # so that the model's weights are hosted on CPU memory.
            # Otherwise they may end up hosted on a GPU, which would
            # complicate weight sharing.
            # https://www.tensorflow.org/api_docs/python/tf/keras/utils/multi_gpu_model
            with tf.device('/cpu:0'):
                if self.partly_trained_model is not None:
                    model = load_model(self.partly_trained_model, custom_objects=dependencies)
                else:
                    model = self.__build_model()
        print(model.summary())

        if self.n_gpus > 1:
            self.parallel_model = multi_gpu_model(model, gpus=self.n_gpus)
        else:
            self.parallel_model = model

        # Save the model architecture
        classifier_name = "cell_type" if self.cell_type_classifier_mode else "transient"
        with open(f'{self.results_path}/{classifier_name}_classifier_model_architecture_{self.model_descr}.json', 'w') as f:
            f.write(model.to_json())

            # Define the optimizer
            # from https://www.kaggle.com/shahariar/keras-swish-activation-acc-0-996-top-7
        if self.optimizer_choice == "Adam":
            optimizer = Adam(lr=self.learning_rate_start, epsilon=1e-08, decay=0.0)
        elif self.optimizer_choice == "SGD":
            # default parameters: lr=0.01, momentum=0.0, decay=0.0, nesterov=False
            optimizer = SGD(lr=self.learning_rate_start, momentum=0.0, decay=0.0, nesterov=False)
        elif self.optimizer_choice == "radam":
            optimizer = RAdam(total_steps=10000, warmup_proportion=0.1, min_lr=1e-5)
        else:
            # default parameters: lr=0.001, rho=0.9, epsilon=None, decay=0.0
            # print("Before RMSprop")
            optimizer = RMSprop(lr=self.learning_rate_start, rho=0.9, epsilon=None, decay=0.0)
            # print("After RMSprop")
            # keras.optimizers.SGD(lr=0.01, momentum=0.0, decay=0.0, nesterov=False)
            # optimizer = 'rmsprop'

            # precision = PPV and recall = sensitiviy but in our case just concerning the active frames
            # the sensitivity and specificity otherwise refers to non-active and active frames classifier
        if self.using_multi_class > 1:
            metrics_to_use = ['acc']
        else:
            metrics_to_use = ['acc', sensitivity, specificity, precision]
            # metrics_to_use = ['acc', tf.keras.metrics.Recall(), tf.keras.metrics.SpecificityAtSensitivity(0.5),
            #                   tf.keras.metrics.Precision()]

        # print(f"Before self.parallel_model.compile")
        self.parallel_model.compile(optimizer=optimizer,
                                    loss=self.loss_fct,
                                    metrics=metrics_to_use)
        # print(f"After self.parallel_model.compile")

        if self.with_learning_rate_reduction:
            self.callbacks_list.append(self.learning_rate_reduction)

        if self.with_early_stopping:
            self.callbacks_list.append(EarlyStopping(monitor="val_acc", min_delta=0,
                                                patience=self.early_stop_patience, mode="max",
                                                restore_best_weights=True))

        # not very useful to save best only if we use EarlyStopping
        if self.with_model_check_point:
            # end_file_path = f"_{param.time_str}.h5"
            if self.save_weigths_only:
                if self.cell_type_classifier_mode:
                    # file_path = os.path.join(self.results_path,
                    #                          "cell_type_classifier_weights_{epoch:02d}-{val_accuracy:.4f}.h5")
                    file_path = os.path.join(self.results_path,
                                             "cell_type_classifier_weights_{epoch:02d}.h5")
                else:
                    # file_path = os.path.join(self.results_path,
                    #                      "transient_classifier_weights_{epoch:02d}-{val_accuracy:.4f}.h5")
                    file_path = os.path.join(self.results_path,
                                         "transient_classifier_weights_{epoch:02d}.h5")
            else:
                if self.cell_type_classifier_mode:
                    # file_path = os.path.join(self.results_path,
                    #                          "cell_type_classifier_full_model_{epoch:02d}-{val_accuracy:.4f}.h5")
                    file_path = os.path.join(self.results_path,
                                             "cell_type_classifier_full_model_{epoch:02d}.h5")
                else:
                    # file_path = os.path.join(self.results_path,
                    #                      "transient_classifier_full_model_{epoch:02d}-{val_accuracy:.4f}.h5")
                    file_path = os.path.join(self.results_path,
                                         "transient_classifier_full_model_{epoch:02d}.h5")
            # callbacks_list.append(ModelCheckpoint(filepath=file_path, monitor="val_accuracy", save_best_only=self.save_weigths_only,
            #                                       save_weights_only="True", mode="max"))
            # https://github.com/TextpertAi/alt-model-checkpoint
            # print(f"Before AltModelCheckpoint")
            self.callbacks_list.append(AltModelCheckpoint(file_path, model, save_weights_only=self.save_weigths_only))
            # print(f"After AltModelCheckpoint")
        # print("End prepare_model in cinac_model.py")

    def fit(self):
        if self.training_generator is None:
            print(f"prepare_model() method should be called before fit()")
            return

        # Train model on dataset
        start_time = time.time()

        print(f"self.parallel_model.fit_generator")
        if TF_VERSION[0] != "2":
            history = self.parallel_model.fit_generator(generator=self.training_generator,
                                                        validation_data=self.validation_generator,
                                                        epochs=self.n_epochs,
                                                        use_multiprocessing=True,
                                                        workers=self.workers,
                                                        callbacks=self.callbacks_list, verbose=self.verbose)
        else:
            history = self.parallel_model.fit(x=self.training_generator,
                                              validation_data=self.validation_generator,
                                              epochs=self.n_epochs,
                                              use_multiprocessing=True,
                                              workers=self.workers,
                                              callbacks=self.callbacks_list, verbose=self.verbose)

        # print(f"history.history.keys() {history.history.keys()}")
        stop_time = time.time()
        print(f"Time for fitting the model to the data with {self.n_epochs} epochs: "
              f"{np.round(stop_time - start_time, 3)} s")

        history_dict = history.history
        np.savez(os.path.join(self.results_path, "metrics_history.npz"), **history_dict)
        # TODO: save parameters used + metrics for each epochs
