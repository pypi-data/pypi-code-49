import tensorflow as tf

TF_VERSION = tf.__version__
print(f"TF_VERSION {TF_VERSION}")

# depending on the TF version installed
if TF_VERSION[0] == "2":
    from tensorflow.keras.models import model_from_json
else:
    from keras.models import model_from_json

import numpy as np
import time
from deepcinac.utils.utils import horizontal_flip, vertical_flip, v_h_flip
from deepcinac.cinac_movie_patch import MoviePatchGeneratorMaskedVersions, MoviePatchGeneratorForCellType, \
    MoviePatchData
# from deepcinac.utils.cells_map_utils import CellsCoord, create_cells_coord_from_suite_2p
# import PIL
import os
# from abc import ABC, abstractmethod
# from ScanImageTiffReader import ScanImageTiffReader
# from PIL import ImageSequence
import scipy.io as sio
# from shapely.geometry import MultiPoint, LineString
from datetime import datetime
import scipy.signal
import deepcinac.cinac_model

class CinacPredictor:

    def __init__(self, verbose=0):
        self.recordings = []
        self.verbose = verbose

    def add_recording(self, cinac_recording, model_files_dict=None, removed_cells_mapping=None):
        """
        Add a recording as a set of a calcium imaging movie, ROIs, and a list of cell to predict
        Args:
            cinac_recording: an instance of CinacRecording
            model_files_dict: dictionary. Key is a tuple of three string representing the file_name of the json file,
              the filename of the weights file and network_identifier and an identifier for the model
             and weights used (will be added to the name of files containing the predictions
             in addition of recording identifier.)
             the value of the dict being a list or array of integers that represents
             the indices of the cell to be predicted by the given model and set of weights.
             If None, means all cells activity will be predicted. Cells not including, will have their prediction
             set to 0 for all the frames
            removed_cells_mapping: integers array of length the original numbers of cells
            (such as defined in CinacRecording)
            and as value either of positive int representing the new index of the cell or -1 if the cell has been
            removed

        Returns:

        """
        self.recordings.append((cinac_recording, model_files_dict, removed_cells_mapping))

    @staticmethod
    def get_new_cell_indices_if_cells_removed(cell_indices_array, removed_cells_mapping):
        """
        Take an array of int, and return another one with new index in case some cells would have been removed
        and some cells ROIs are not matching anymore
        Args:
            cell_indices_array: np.array of integers, containing the cells indices to remap
            removed_cells_mapping: integers array of length the original numbers of cells
            (such as defined in CinacRecording)
            and as value either of positive int representing the new index of the cell or -1 if the cell has been
            removed

        Returns: new_cell_indices_array an np.array that contains integers representing the new indices of cells that
        have not been removed
        original_cell_indices_mapping, np.array, for each new cell index, contains the corresponding original index

        """

        if removed_cells_mapping is None:
            return np.copy(cell_indices_array), np.copy(cell_indices_array)

        new_cell_indices_array = removed_cells_mapping[cell_indices_array]
        # removing cell indices of cell that has been removed
        copy_new_cell_indices_array = np.copy(new_cell_indices_array)
        new_cell_indices_array = new_cell_indices_array[new_cell_indices_array >= 0]
        original_cell_indices_mapping = np.copy(cell_indices_array[copy_new_cell_indices_array >= 0])

        return new_cell_indices_array, original_cell_indices_mapping

    def predict(self, results_path, overlap_value=0.5, output_file_formats="npy", cell_type_classifier_mode=False,
                n_segments_to_use_for_prediction=2, cell_type_pred_fct=np.mean, create_dir_for_results=True,
                **kwargs):
        """
        Will predict the neural activity state of the cell for each frame of the calcium imaging movies.
        Recordings have to be added previously though the add_recording method.
        Args:
            results_path: if None, predictions are not saved in a file
            overlap_value:
            cell_type_classifier_mode: means we want to classify each cell to know its type. So far return a prediction
            value between 0 and 1, 1 meaning 100% a pyramidal cell, 0 100% sure not (should be interneuron then)
            output_file_formats: a string or list of string, representing the format in which saving the 2d array
            representing the prediction for each movie. The choices are: "mat" or "npy". If "mat", matlab format, then
            the predictions named will be "predictions"
            n_segments_to_use_for_prediction: used when cell_type_classifier_mode is at True. Indicate how many segment
            of window_len should be used to predict the cell_type. For example if the value is 2 and window_len is 200,
            then we take the mean of the prediction over 2 segments of 200 frames. Those segments are selected based
            on their activity (the more a cell is active (amplitudes) the best chance the segment is to be selected)
            cell_type_pred_fct: fct to use to average the predictons if it is done in more than one segment
            create_dir_for_results: if True, create a dir with timestamps to store the results. The directory is created
            in results_path. Else predictions are stored directly in results_path
            **kwargs:


        Returns: a dict with key being the id of the cinac recording and value a numpy array of n_cells

        """

        use_data_augmentation = False
        if "use_data_augmentation" in kwargs:
            use_data_augmentation = kwargs["use_data_augmentation"]

        # output_file_formats = "npy"
        if "output_file_formats" in kwargs:
            output_file_formats = kwargs["output_file_formats"]

        # dictionary that will contains the predictions results. Keys are the CinacRecording identifiers
        predictions_dict = dict()
        for recording in self.recordings:
            cinac_recording, model_files_dict, removed_cells_mapping = recording
            n_cells = cinac_recording.get_n_cells()
            n_frames = cinac_recording.get_n_frames()

            for file_names, cells_to_predict in model_files_dict.items():
                json_model_file_name, weights_file_name, network_identifier = file_names
                # ms.tiffs_for_transient_classifier_path = tiffs_for_transient_classifier_path

                if cells_to_predict is None:
                    cells_to_load = np.arange(n_cells)
                else:
                    cells_to_load = np.array(cells_to_predict)
                    # if cell_type_classifier_mode:
                    #     n_cells = len(cells_to_load)

                original_cells_to_load = np.copy(cells_to_load)
                cells_to_load, \
                original_cell_indices_mapping = self.get_new_cell_indices_if_cells_removed(cells_to_load,
                                                                                           removed_cells_mapping)
                total_n_cells = len(cells_to_load)
                # print(f'total_n_cells {total_n_cells}')

                if total_n_cells == 0:
                    print(f"No cells loaded for {cinac_recording.identifier}")
                    continue

                # print(f"transients_prediction_from_movie n_frames {n_frames}")
                # we keep the original number of cells, so if a different segmentation was used another prediction,
                # we can still compare it using the indices we know
                if cell_type_classifier_mode:
                    # will be initiated later when the number of classes will be known
                    predictions_by_cell = None #np.zeros(n_cells)
                else:
                    predictions_by_cell = np.zeros((n_cells, n_frames))

                # loading model
                # Model reconstruction from JSON file
                with open(json_model_file_name, 'r') as f:
                    model = model_from_json(f.read(), custom_objects={"deepcinac.cinac_model": deepcinac.cinac_model})

                # Load weights into the new model
                model.load_weights(weights_file_name)

                start_time = time.time()
                predictions_threshold = 0.5
                # in case we want to use tqdm
                # for cell_index in tqdm(range(len(cells_to_load)),
                #                              desc=f"{cinac_recording.identifier} - {network_identifier}"):
                #     cell = cells_to_load[cell_index]
                for cell_index in range(len(cells_to_load)):
                    cell = cells_to_load[cell_index]
                    original_cell = original_cell_indices_mapping[cell_index]
                    if cell_type_classifier_mode:
                        predictions = predict_cell_type_from_model(cinac_recording=cinac_recording,
                                                                   cell=cell, model=model, overlap_value=overlap_value,
                                                                   use_data_augmentation=use_data_augmentation,
                                                                   n_frames=n_frames,
                                                                   n_segments_to_use_for_prediction=
                                                                   n_segments_to_use_for_prediction,
                                                                   verbose=self.verbose)
                        # print(f"predictions in predict() {len(predictions)} {len(predictions[0])} {predictions}")
                        if len(predictions) > 1:
                            if len(predictions[0]) == 1:
                                if predictions_by_cell is None:
                                    predictions_by_cell = np.zeros(n_cells)
                                predictions = cell_type_pred_fct(predictions)
                            else:
                                if predictions_by_cell is None:
                                    predictions_by_cell = np.zeros((n_cells, len(predictions[0])))
                                predictions = cell_type_pred_fct(predictions, axis=0)
                        else:
                            if predictions_by_cell is None:
                                predictions_by_cell = np.zeros(n_cells)
                            predictions = predictions[0]
                        predictions_by_cell[original_cell] = predictions
                    else:
                        predictions = predict_transient_from_model(cinac_recording=cinac_recording,
                                                                   cell=cell, model=model, overlap_value=overlap_value,
                                                                   use_data_augmentation=use_data_augmentation,
                                                                   n_frames=n_frames)
                        if len(predictions.shape) == 1:
                            predictions_by_cell[original_cell] = predictions
                        elif (len(predictions.shape) == 2) and (predictions.shape[1] == 1):
                            predictions_by_cell[original_cell] = predictions[:, 0]
                        elif (len(predictions.shape) == 2) and (predictions.shape[1] == 3):
                            # real transient, fake ones, other (neuropil, decay etc...)
                            # keeping predictions about real transient when superior
                            # to other prediction on the same frame
                            max_pred_by_frame = np.max(predictions, axis=1)
                            real_transient_frames = (predictions[:, 0] == max_pred_by_frame)
                            predictions_by_cell[original_cell, real_transient_frames] = 1
                        elif predictions.shape[1] == 2:
                            # real transient, fake ones
                            # keeping predictions about real transient superior to the threshold
                            # and superior to other prediction on the same frame
                            max_pred_by_frame = np.max(predictions, axis=1)
                            real_transient_frames = np.logical_and((predictions[:, 0] >= predictions_threshold),
                                                                   (predictions[:, 0] == max_pred_by_frame))
                            predictions_by_cell[original_cell, real_transient_frames] = 1

            stop_time = time.time()
            if self.verbose > 0:
                print(f"Time to predict {total_n_cells} cells: "
                      f"{np.round(stop_time - start_time, 3)} s")
            if isinstance(output_file_formats, str):
                output_file_formats = [output_file_formats]

            # TODO: use all network_identifier if more than one
            if network_identifier is None:
                network_identifier = ""
            else:
                network_identifier = "_" + network_identifier
            if results_path is not None:
                if create_dir_for_results:
                    time_str = datetime.now().strftime("%Y_%m_%d.%H-%M-%S")
                    new_dir_results = os.path.join(results_path, f"{time_str}/")
                    os.mkdir(new_dir_results)
                else:
                    new_dir_results = results_path

                file_name = f"{cinac_recording.identifier}_predictions{network_identifier}"
                for output_file_format in output_file_formats:
                    if "mat" in output_file_format:
                        sio.savemat(os.path.join(new_dir_results, file_name + ".mat"),
                                    {'predictions': predictions_by_cell, "cells": original_cells_to_load})
                    elif "npy" in output_file_format:
                        np.save(os.path.join(new_dir_results, file_name + ".npz"),
                                {'predictions': predictions_by_cell, "cells": original_cells_to_load},
                                allow_pickle=True)
            predictions_dict[cinac_recording.identifier] = predictions_by_cell

        return predictions_dict

def predict_cell_type_from_model(cinac_recording, cell, model,
                                 n_frames, n_segments_to_use_for_prediction=2,
                                 overlap_value=0, pixels_around=0,
                                 use_data_augmentation=False, buffer=None, verbose=0):
    # if n_frames is None, then the movie need to have been loaded
    # start_time = time.time()
    # multi_inputs = (model.layers[0].output_shape == model.layers[1].output_shape)
    # print(f"model.layers[0].output_shape {model.layers[0].output_shape}")
    window_len = model.layers[0].output_shape[0][1]
    max_height = model.layers[0].output_shape[0][2]
    max_width = model.layers[0].output_shape[0][3]

    # Determining how many classes were used
    if len(model.layers[-1].output_shape) == 2:
        using_multi_class = 1
    else:
        using_multi_class = model.layers[-1].output_shape[2]
        # print(f"predict_transient_from_model using_multi_class {using_multi_class}")

    if use_data_augmentation:
        augmentation_functions = [horizontal_flip, vertical_flip, v_h_flip]
    else:
        augmentation_functions = None

    movie_patches, data_frame_indices = load_data_for_cell_type_prediction(cinac_recording=cinac_recording,
                                                                           cell=cell,
                                                                           sliding_window_len=window_len,
                                                                           overlap_value=overlap_value,
                                                                           augmentation_functions=augmentation_functions,
                                                                           n_frames=n_frames,
                                                                           n_windows_len_to_keep_by_cell=
                                                                           n_segments_to_use_for_prediction)


    movie_patch_generator = \
        MoviePatchGeneratorForCellType(window_len=window_len, max_width=max_width, max_height=max_height,
                                       pixels_around=pixels_around, buffer=buffer, with_all_pixels=False,
                                       using_multi_class=using_multi_class, cell_type_classifier_mode=True)

    data_dict = movie_patch_generator.generate_movies_from_metadata(movie_data_list=movie_patches,
                                                                    with_labels=False)

    # stop_time = time.time()
    # print(f"Time to get the data: "
    #       f"{np.round(stop_time - start_time, 3)} s")
    start_time = time.time()

    predictions = model.predict(data_dict)

    stop_time = time.time()
    if verbose > 0:
        print(f"Time to get predictions for cell {cell}: "
              f"{np.round(stop_time - start_time, 3)} s")

    return predictions

def load_data_for_prediction(cinac_recording, cell, sliding_window_len, overlap_value,
                             augmentation_functions, n_frames):
    """
    Create data that will be used to predict neural activity. The data will be representing by instances of
    MoviePatchData that will contains information concerning this movie segment for a given
    cell to give to the neuronal network.
    Args:
        cinac_recording: instance of CinacRecording, contains the movie frames and the ROIs
        cell: integer, the cell index
        sliding_window_len: integer, length in frames of the window used by the neuronal network. Predictions will be
        made for each frame of this segment
        overlap_value: float value between 0 and 1, representing by how much 2 movie segments will overlap.
        0.5 is equivalent to a 50% overlap. It allows the network to avoid edge effect in order to get a full temporal
        vision of all transient. A good default value is 0.5
        augmentation_functions: list of function that takes an image (np array) as input and return a copy of the image
        transformed.
        n_frames: number of frames in the movie

    Returns: a list of MoviePatchData instance and an integer representing the index of the first frame of the patch

    """
    # n_frames is None, the movie need to have been loaded
    # we suppose that the movie is already loaded and normalized
    movie_patches = []
    data_frame_indices = []
    frames_step = int(np.ceil(sliding_window_len * (1 - overlap_value)))
    # number of indices to remove so index + sliding_window_len won't be superior to number of frames
    n_step_to_remove = 0 if (overlap_value == 0) else int(1 / (1 - overlap_value))
    frame_indices_for_movies = np.arange(0, n_frames, frames_step)
    if n_step_to_remove > 0:
        frame_indices_for_movies = frame_indices_for_movies[:-n_step_to_remove + 1]
    # in case the n_frames wouldn't be divisible by frames_step
    if frame_indices_for_movies[-1] + frames_step > n_frames:
        frame_indices_for_movies[-1] = n_frames - sliding_window_len

    for i, index_movie in enumerate(frame_indices_for_movies):
        break_it = False
        first_frame = index_movie
        if (index_movie + sliding_window_len) == n_frames:
            break_it = True
        elif (index_movie + sliding_window_len) > n_frames:
            # in case the number of frames is not divisible by sliding_window_len
            first_frame = n_frames - sliding_window_len
            break_it = True
        movie_data = MoviePatchData(cinac_recording=cinac_recording, cell=cell, index_movie=first_frame,
                                    window_len=sliding_window_len,
                                    max_n_transformations=3,
                                    with_info=False, encoded_frames=None,
                                    decoding_frame_dict=None)

        movie_patches.append(movie_data)
        data_frame_indices.append(first_frame)
        if augmentation_functions is not None:
            for augmentation_fct in augmentation_functions:
                new_movie = movie_data.copy()
                new_movie.data_augmentation_fct = augmentation_fct
                movie_patches.append(new_movie)
                data_frame_indices.append(first_frame)

        if break_it:
            break

    return movie_patches, data_frame_indices

def load_data_for_cell_type_prediction(cinac_recording, cell, sliding_window_len, overlap_value,
                                       augmentation_functions, n_frames, n_windows_len_to_keep_by_cell=2):
    """
    Create data that will be used to predict cell type. The data will be representing by instances of
    MoviePatchData that will contains information concerning this movie segment for a given
    cell to give to the neuronal network.
    Args:
        cinac_recording: instance of CinacRecording, contains the movie frames and the ROIs
        cell: integer, the cell index
        sliding_window_len: integer, length in frames of the window used by the neuronal network. Predictions will be
        made for each frame of this segment
        overlap_value: float value between 0 and 1, representing by how much 2 movie segments will overlap.
        0.5 is equivalent to a 50% overlap. It allows the network to avoid edge effect in order to get a full temporal
        vision of all transient. A good default value is 0.5
        augmentation_functions: list of function that takes an image (np array) as input and return a copy of the image
        transformed.
        n_frames: number of frames in the movie
        n_windows_len_to_keep_by_cell: how many segment of window_len frames should be used to predict cell_type,
        so the length of the returned list will be the same as n_windows_len_to_keep_by_cell
    Returns: a list of MoviePatchData instance and an integer representing the index of the first frame of the patch

    """
    # n_frames is None, the movie need to have been loaded
    # we suppose that the movie is already loaded and normalized
    movie_patches = []
    data_frame_indices = []
    frames_step = int(np.ceil(sliding_window_len * (1 - overlap_value)))
    # number of indices to remove so index + sliding_window_len won't be superior to number of frames
    n_step_to_remove = 0 if (overlap_value == 0) else int(1 / (1 - overlap_value))
    frame_indices_for_movies = np.arange(0, n_frames, frames_step)
    if n_step_to_remove > 0:
        frame_indices_for_movies = frame_indices_for_movies[:-n_step_to_remove + 1]
    # in case the n_frames wouldn't be divisible by frames_step
    if frame_indices_for_movies[-1] + frames_step > n_frames:
        frame_indices_for_movies[-1] = n_frames - sliding_window_len

    # list of  int representing the first_frame possible candidate
    # for moviepatch to add for predicting. We want to keep for each cell only the most active
    # one
    first_frames_to_filter = []
    n_windows_len_to_keep_by_cell = max(0, n_windows_len_to_keep_by_cell)

    for i, index_movie in enumerate(frame_indices_for_movies):
        break_it = False
        first_frame = index_movie
        if (index_movie + sliding_window_len) == n_frames:
            break_it = True
        elif (index_movie + sliding_window_len) > n_frames:
            # in case the number of frames is not divisible by sliding_window_len
            first_frame = n_frames - sliding_window_len
            break_it = True
        first_frames_to_filter.append(first_frame)

        if break_it:
            break

    # we want to select at least a first_frame to create a moviePatch
    # the idea is to sort the first_frame and the segment that goes with (adding self.window_len)
    # according to the activity of the cell, we're looking for the segment with the highest amplitude peaks
    first_frames_selected = []
    # will contain a score representing the avg amplitude of the highest peaks
    avg_peaks_amplitudes = []
    smooth_traces = cinac_recording.get_smooth_traces(normalized=True)
    if len(smooth_traces.shape) == 1:
        pass
    else:
        smooth_traces = smooth_traces[cell]

    peaks, properties = scipy.signal.find_peaks(x=smooth_traces, distance=2)
    peak_nums = np.zeros(n_frames, dtype="int8")
    peak_nums[peaks] = 1
    for first_frame in first_frames_to_filter:
        peaks = np.where(peak_nums[first_frame:first_frame + sliding_window_len])[0] + first_frame
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

    for first_frame in first_frames_selected:
        movie_data = MoviePatchData(cinac_recording=cinac_recording, cell=cell, index_movie=first_frame,
                                    window_len=sliding_window_len,
                                    max_n_transformations=3,
                                    with_info=False, encoded_frames=None,
                                    cell_type_classifier_mode=True,
                                    decoding_frame_dict=None)

        movie_patches.append(movie_data)
        data_frame_indices.append(first_frame)
        if augmentation_functions is not None:
            for augmentation_fct in augmentation_functions:
                new_movie = movie_data.copy()
                new_movie.data_augmentation_fct = augmentation_fct
                movie_patches.append(new_movie)
                data_frame_indices.append(first_frame)

    return movie_patches, data_frame_indices

def predict_transient_from_model(cinac_recording, cell, model,
                                 n_frames, overlap_value=0.8, pixels_around=0,
                                 use_data_augmentation=False, buffer=None):
    # if n_frames is None, then the movie need to have been loaded
    # start_time = time.time()
    # multi_inputs = (model.layers[0].output_shape == model.layers[1].output_shape)
    window_len = model.layers[0].output_shape[1]
    max_height = model.layers[0].output_shape[2]
    max_width = model.layers[0].output_shape[3]

    # Determining how many classes were used
    if len(model.layers[-1].output_shape) == 2:
        using_multi_class = 1
    else:
        using_multi_class = model.layers[-1].output_shape[2]
        # print(f"predict_transient_from_model using_multi_class {using_multi_class}")

    if use_data_augmentation:
        augmentation_functions = [horizontal_flip, vertical_flip, v_h_flip]
    else:
        augmentation_functions = None
    # start_time_bis = time.time()
    movie_patches, data_frame_indices = load_data_for_prediction(cinac_recording=cinac_recording,
                                                                 cell=cell,
                                                                 sliding_window_len=window_len,
                                                                 overlap_value=overlap_value,
                                                                 augmentation_functions=augmentation_functions,
                                                                 n_frames=n_frames)
    # stop_time_bis = time.time()
    # print(f"Time to get load_data_for_prediction: "
    #       f"{np.round(stop_time_bis - start_time_bis, 3)} s")

    movie_patch_generator = \
        MoviePatchGeneratorMaskedVersions(window_len=window_len, max_width=max_width, max_height=max_height,
                                          pixels_around=pixels_around, buffer=buffer, with_neuropil_mask=True,
                                          using_multi_class=using_multi_class)

    data_dict = movie_patch_generator.generate_movies_from_metadata(movie_data_list=movie_patches,
                                                                    with_labels=False)

    # stop_time = time.time()
    # print(f"Time to get the data: "
    #       f"{np.round(stop_time - start_time, 3)} s")
    start_time = time.time()

    predictions = model.predict(data_dict)

    stop_time = time.time()
    print(f"Time to get predictions for cell {cell}: "
          f"{np.round(stop_time - start_time, 3)} s")

    # now we want to take the prediction with the maximal value for a given frame
    # the rational being that often if a transient arrive right at the end or the beginning
    # it won't be recognized as True
    if (overlap_value > 0) or (augmentation_functions is not None):
        frames_predictions = dict()
        # print(f"predictions.shape {predictions.shape}, data_frame_indices.shape {data_frame_indices.shape}")
        for i, data_frame_index in enumerate(data_frame_indices):
            frames_index = np.arange(data_frame_index, data_frame_index + window_len)
            predictions_for_frames = predictions[i]
            for j, frame_index in enumerate(frames_index):
                if frame_index not in frames_predictions:
                    frames_predictions[frame_index] = dict()
                if len(predictions_for_frames.shape) == 1:
                    if 0 not in frames_predictions[frame_index]:
                        frames_predictions[frame_index][0] = []
                    frames_predictions[frame_index][0].append(predictions_for_frames[j])
                else:
                    # then it's muti_class labels
                    for index in np.arange(len(predictions_for_frames[j])):
                        if index not in frames_predictions[frame_index]:
                            frames_predictions[frame_index][index] = []
                        frames_predictions[frame_index][index].append(predictions_for_frames[j, index])

        predictions = np.zeros((n_frames, using_multi_class))
        for frame_index, class_dict in frames_predictions.items():
            for class_index, prediction_values in class_dict.items():
                # max value
                predictions[frame_index, class_index] = np.max(prediction_values)
    else:
        # to flatten all but last dimensions
        predictions = np.ndarray.flatten(predictions)

        # now we remove the extra prediction in case the number of frames was not divisible by the window length
        if (n_frames % window_len) != 0:
            print("(n_frames % window_len) != 0")
            real_predictions = np.zeros((n_frames, using_multi_class))
            modulo = n_frames % window_len
            real_predictions[:len(predictions) - window_len] = predictions[
                                                               :len(predictions) - window_len]
            real_predictions[len(predictions) - window_len:] = predictions[-modulo:]
            predictions = real_predictions

    if len(predictions) != n_frames:
        raise Exception(f"predictions len {len(predictions)} is different from the number of frames {n_frames}")

    return predictions