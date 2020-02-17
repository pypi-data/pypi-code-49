import tensorflow as tf

TF_VERSION = tf.__version__
print(f"TF_VERSION {TF_VERSION}")

# depending on the TF version installed
if TF_VERSION[0] == "2":
    import tensorflow.keras as keras
else:
    import keras

import numpy as np
from deepcinac.utils.utils import horizontal_flip, vertical_flip, v_h_flip, shift_movie, rotate_movie
from deepcinac.utils.utils import get_source_profile_param


class MoviePatchGenerator:
    """
    Used to generate movie patches, that will be produce for training data during each mini-batch.
    This is an abstract classes that need to have heritage.
    The function generate_movies_from_metadata will be used to produced those movie patches, the number
    vary depending on the class instantiated
    """

    def __init__(self, window_len, max_width, max_height, using_multi_class, cell_type_classifier_mode):
        self.window_len = window_len
        self.max_width = max_width
        self.max_height = max_height
        self.using_multi_class = using_multi_class
        self.cell_type_classifier_mode = cell_type_classifier_mode

    # self.n_inputs shouldn't be changed
    def get_nb_inputs(self):
        return self.n_inputs

    def generate_movies_from_metadata(self, movie_data_list, memory_dict, with_labels=True):
        pass


# TODO: See to add more MoviePatchGenerator versions

class MoviePatchGeneratorForCellType(MoviePatchGenerator):
    def __init__(self, window_len, max_width, max_height, pixels_around,
                 buffer, using_multi_class, cell_type_classifier_mode, with_all_pixels=False):
        super().__init__(window_len=window_len, max_width=max_width, max_height=max_height,
                         using_multi_class=using_multi_class, cell_type_classifier_mode=cell_type_classifier_mode)
        self.pixels_around = pixels_around
        self.buffer = buffer
        self.n_inputs = 1
        self.with_all_pixels = with_all_pixels
        if with_all_pixels:
            self.n_inputs += 1

    def generate_movies_from_metadata(self, movie_data_list, memory_dict=None, with_labels=True):
        """

        Args:
            movie_data_list: list of MoviePatchData instances
            memory_dict:
            with_labels:

        Returns:

        """
        # print(f"Start generate_movies_from_metadata() in cinac_movie_patch.py")
        source_profiles_dict = memory_dict
        if source_profiles_dict is None:
            source_profiles_dict = dict()
        batch_size = len(movie_data_list)
        if with_labels:
            if self.using_multi_class <= 1:
                if self.cell_type_classifier_mode:
                    labels = np.zeros((batch_size, 1), dtype="uint8")
                else:
                    labels = np.zeros((batch_size, self.window_len), dtype="uint8")
            else:
                if self.cell_type_classifier_mode:
                    labels = np.zeros((batch_size, self.using_multi_class), dtype="uint8")
                else:
                    labels = np.zeros((batch_size, self.window_len, self.using_multi_class), dtype="uint8")

        inputs_dict = dict()
        for input_index in np.arange(self.n_inputs):
            inputs_dict[f"input_{input_index}"] = np.zeros((batch_size, self.window_len, self.max_height,
                                                            self.max_width, 1))

        # Generate data
        for index_batch, movie_data in enumerate(movie_data_list):
            cinac_recording = movie_data.cinac_recording
            cell = movie_data.cell
            frame_index = movie_data.index_movie
            augmentation_fct = movie_data.data_augmentation_fct

            # now we generate the source profile of the cells for those frames and retrieve it if it has
            # already been generated
            # src_profile_key = cinac_recording.identifier + str(cell)
            # if src_profile_key in source_profiles_dict:
            #     mask_source_profiles, coords = source_profiles_dict[src_profile_key]
            # else:
            mask_source_profile, coords = \
                get_source_profile_param(cell=cell, movie_dimensions=cinac_recording.cinac_movie.get_dimensions(),
                                         coord_obj=cinac_recording.coord_obj, pixels_around=self.pixels_around,
                                         buffer=self.buffer,
                                         max_width=self.max_width, max_height=self.max_height,
                                         with_all_masks=False)
            # source_profiles_dict[src_profile_key] = [mask_source_profiles, coords]

            frames = np.arange(frame_index, frame_index + self.window_len)
            if with_labels:
                labels[index_batch] = movie_data.get_labels(using_multi_class=self.using_multi_class)
            # now adding the movie of those frames in this sliding_window
            # Takes around 0.65 sec on a macbook pro
            source_profile_frames = cinac_recording.get_source_profile_frames(frames_indices=frames, coords=coords)

            input_index = 0

            # then we compute the frame with just the mask of each cell (the main one (with input_0 index) and the ones
            # that overlaps)
            # mask_source_profiles_keys = np.array(list(mask_source_profiles.keys()))

            # mask_for_all_cells = np.zeros((source_profile_frames.shape[1], source_profile_frames.shape[2]),
            #                               dtype="int8")

            source_profile_frames_masked = np.copy(source_profile_frames)
            source_profile_frames_masked[:, mask_source_profile] = 0

            # doing augmentation if the function exists
            if augmentation_fct is not None:
                source_profile_frames_masked = augmentation_fct(source_profile_frames_masked)

            # then we fit it the frame use by the network, padding the surrounding by zero if necessary
            profile_fit_masked = np.zeros((len(frames), self.max_height, self.max_width))
            # we center the source profile
            y_coord = (profile_fit_masked.shape[1] - source_profile_frames.shape[1]) // 2
            x_coord = (profile_fit_masked.shape[2] - source_profile_frames.shape[2]) // 2
            profile_fit_masked[:, y_coord:source_profile_frames.shape[1] + y_coord,
            x_coord:source_profile_frames.shape[2] + x_coord] = \
                source_profile_frames_masked

            profile_fit_masked = profile_fit_masked.reshape((profile_fit_masked.shape[0],
                                                             profile_fit_masked.shape[1],
                                                             profile_fit_masked.shape[2], 1))

            inputs_dict[f"input_{input_index}"][index_batch] = profile_fit_masked


            input_index += 1

            if self.with_all_pixels:
                # doing augmentation if the function exists
                if augmentation_fct is not None:
                    # return new frames, doesn't change the original
                    source_profile_frames = augmentation_fct(source_profile_frames)
                # then we fit it the frame use by the network, padding the surrounding by zero if necessary
                profile_fit = np.zeros((len(frames), self.max_height, self.max_width))
                # we center the source profile
                y_coord = (profile_fit.shape[1] - source_profile_frames.shape[1]) // 2
                x_coord = (profile_fit.shape[2] - source_profile_frames.shape[2]) // 2
                profile_fit[:, y_coord:source_profile_frames.shape[1] + y_coord,
                x_coord:source_profile_frames.shape[2] + x_coord] = \
                    source_profile_frames

                profile_fit = profile_fit.reshape((profile_fit.shape[0], profile_fit.shape[1], profile_fit.shape[2], 1))
                data = inputs_dict[f"input_{input_index}"]
                data[index_batch] = profile_fit
                input_index += 1
        # print(f"End generate_movies_from_metadata() in cinac_movie_patch.py")

        if with_labels:
            return inputs_dict, labels
        else:
            return inputs_dict

    def __str__(self):
        bonus_str = ""
        if self.with_all_pixels:
            bonus_str = "+ one with all pixels"
        return f"{self.n_inputs} inputs. Main cell mask {bonus_str}"

class MoviePatchGeneratorMaskedVersions(MoviePatchGenerator):
    """
    Will generate one input being the masked cell (the one we focus on), the second input
    would be the whole patch without neuorpil and the main cell, the last inpu if with_neuropil_mask is True
    would be just the neuropil without the pixels in the cells
    """

    def __init__(self, window_len, max_width, max_height, pixels_around,
                 buffer, with_neuropil_mask, using_multi_class, cell_type_classifier_mode):
        super().__init__(window_len=window_len, max_width=max_width, max_height=max_height,
                         using_multi_class=using_multi_class, cell_type_classifier_mode=cell_type_classifier_mode)
        self.pixels_around = pixels_around
        self.buffer = buffer
        self.with_neuropil_mask = with_neuropil_mask
        self.n_inputs = 2
        if with_neuropil_mask:
            self.n_inputs += 1

    def generate_movies_from_metadata(self, movie_data_list, memory_dict=None, with_labels=True):
        """

        Args:
            movie_data_list: list of MoviePatchData instances
            memory_dict:
            with_labels:

        Returns:

        """
        # print(f"Start generate_movies_from_metadata() in cinac_movie_patch.py")
        source_profiles_dict = memory_dict
        if source_profiles_dict is None:
            source_profiles_dict = dict()
        batch_size = len(movie_data_list)
        if with_labels:
            if self.using_multi_class <= 1:
                if self.cell_type_classifier_mode:
                    labels = np.zeros((batch_size, 1), dtype="uint8")
                else:
                    labels = np.zeros((batch_size, self.window_len), dtype="uint8")
            else:
                if self.cell_type_classifier_mode:
                    labels = np.zeros((batch_size, 1, self.using_multi_class), dtype="uint8")
                else:
                    labels = np.zeros((batch_size, self.window_len, self.using_multi_class), dtype="uint8")

        # if there are no overlaping cells, we'll give empty frames as inputs (with pixels to zero)
        inputs_dict = dict()
        for input_index in np.arange(self.n_inputs):
            inputs_dict[f"input_{input_index}"] = np.zeros((batch_size, self.window_len, self.max_height,
                                                            self.max_width, 1))

        # Generate data
        for index_batch, movie_data in enumerate(movie_data_list):
            cinac_recording = movie_data.cinac_recording
            cell = movie_data.cell
            frame_index = movie_data.index_movie
            augmentation_fct = movie_data.data_augmentation_fct

            # now we generate the source profile of the cells for those frames and retrieve it if it has
            # already been generated
            # src_profile_key = cinac_recording.identifier + str(cell)
            # if src_profile_key in source_profiles_dict:
            #     mask_source_profiles, coords = source_profiles_dict[src_profile_key]
            # else:
            mask_source_profiles, coords = \
                get_source_profile_param(cell=cell, movie_dimensions=cinac_recording.cinac_movie.get_dimensions(),
                                         coord_obj=cinac_recording.coord_obj, pixels_around=self.pixels_around,
                                         buffer=self.buffer,
                                         max_width=self.max_width, max_height=self.max_height,
                                         with_all_masks=True)
            # source_profiles_dict[src_profile_key] = [mask_source_profiles, coords]

            frames = np.arange(frame_index, frame_index + self.window_len)
            if with_labels:
                labels[index_batch] = movie_data.get_labels(using_multi_class=self.using_multi_class)
            # now adding the movie of those frames in this sliding_window
            # Takes around 0.65 sec on a macbook pro
            source_profile_frames = cinac_recording.get_source_profile_frames(frames_indices=frames, coords=coords)

            input_index = 1

            use_the_whole_frame = False
            if use_the_whole_frame:
                # doing augmentation if the function exists
                if augmentation_fct is not None:
                    source_profile_frames = augmentation_fct(source_profile_frames)
                # then we fit it the frame use by the network, padding the surrounding by zero if necessary
                profile_fit = np.zeros((len(frames), self.max_height, self.max_width))
                # we center the source profile
                y_coord = (profile_fit.shape[1] - source_profile_frames.shape[1]) // 2
                x_coord = (profile_fit.shape[2] - source_profile_frames.shape[2]) // 2
                profile_fit[:, y_coord:source_profile_frames.shape[1] + y_coord,
                x_coord:source_profile_frames.shape[2] + x_coord] = \
                    source_profile_frames

                profile_fit = profile_fit.reshape((profile_fit.shape[0], profile_fit.shape[1], profile_fit.shape[2], 1))
                data = inputs_dict[f"input_{input_index}"]
                data[index_batch] = profile_fit
                input_index += 1

            # then we compute the frame with just the mask of each cell (the main one (with input_0 index) and the ones
            # that overlaps)
            mask_source_profiles_keys = np.array(list(mask_source_profiles.keys()))

            mask_for_all_cells = np.zeros((source_profile_frames.shape[1], source_profile_frames.shape[2]),
                                          dtype="int8")
            if self.with_neuropil_mask:
                neuropil_mask = np.zeros((source_profile_frames.shape[1], source_profile_frames.shape[2]),
                                         dtype="int8")
            for cell_index, mask_source_profile in mask_source_profiles.items():
                if cell_index == cell:
                    source_profile_frames_masked = np.copy(source_profile_frames)
                    source_profile_frames_masked[:, mask_source_profile] = 0
                    if self.with_neuropil_mask:
                        # print(f"source_profile_frames.shape {source_profile_frames.shape}, "
                        #       f"mask_source_profile.shape {mask_source_profile.shape}, "
                        #       f"neuropil_mask.shape {(1 - mask_source_profile).shape}")
                        neuropil_mask[1 - mask_source_profile] = 1

                    # doing augmentation if the function exists
                    if augmentation_fct is not None:
                        source_profile_frames_masked = augmentation_fct(source_profile_frames_masked)

                    # then we fit it the frame use by the network, padding the surrounding by zero if necessary
                    profile_fit_masked = np.zeros((len(frames), self.max_height, self.max_width))
                    # we center the source profile
                    y_coord = (profile_fit_masked.shape[1] - source_profile_frames.shape[1]) // 2
                    x_coord = (profile_fit_masked.shape[2] - source_profile_frames.shape[2]) // 2
                    profile_fit_masked[:, y_coord:source_profile_frames.shape[1] + y_coord,
                    x_coord:source_profile_frames.shape[2] + x_coord] = \
                        source_profile_frames_masked

                    profile_fit_masked = profile_fit_masked.reshape((profile_fit_masked.shape[0],
                                                                     profile_fit_masked.shape[1],
                                                                     profile_fit_masked.shape[2], 1))

                    inputs_dict["input_0"][index_batch] = profile_fit_masked
                    continue
                else:
                    # mask_source_profile worth zero for the pixels in the cell
                    mask_for_all_cells[1 - mask_source_profile] = 1
                    if self.with_neuropil_mask:
                        neuropil_mask[1 - mask_source_profile] = 1

            # now feeding it with the overlaping cells mask
            if len(mask_source_profiles) > 0:
                source_profile_frames_masked = np.copy(source_profile_frames)
                source_profile_frames_masked[:, 1 - mask_for_all_cells] = 0

                # doing augmentation if the function exists
                if augmentation_fct is not None:
                    source_profile_frames_masked = augmentation_fct(source_profile_frames_masked)

                # then we fit it the frame use by the network, padding the surrounding by zero if necessary
                profile_fit_masked = np.zeros((len(frames), self.max_height, self.max_width))
                # we center the source profile
                y_coord = (profile_fit_masked.shape[1] - source_profile_frames.shape[1]) // 2
                x_coord = (profile_fit_masked.shape[2] - source_profile_frames.shape[2]) // 2
                profile_fit_masked[:, y_coord:source_profile_frames.shape[1] + y_coord,
                x_coord:source_profile_frames.shape[2] + x_coord] = \
                    source_profile_frames_masked

                profile_fit_masked = profile_fit_masked.reshape((profile_fit_masked.shape[0],
                                                                 profile_fit_masked.shape[1],
                                                                 profile_fit_masked.shape[2], 1))

                inputs_dict["input_1"][index_batch] = profile_fit_masked
            else:
                # empty frame if there is not overlaping cell
                profile_fit_masked = np.zeros((len(frames), self.max_height, self.max_width))
                profile_fit_masked = profile_fit_masked.reshape((profile_fit_masked.shape[0],
                                                                 profile_fit_masked.shape[1],
                                                                 profile_fit_masked.shape[2], 1))

                inputs_dict["input_1"][index_batch] = profile_fit_masked

            # now feeding it with the neuropil mask
            if self.with_neuropil_mask:
                source_profile_frames_masked = np.copy(source_profile_frames)
                # "deleting" the cells
                source_profile_frames_masked[:, neuropil_mask] = 0

                # doing augmentation if the function exists
                if augmentation_fct is not None:
                    source_profile_frames_masked = augmentation_fct(source_profile_frames_masked)

                # then we fit it the frame use by the network, padding the surrounding by zero if necessary
                profile_fit_masked = np.zeros((len(frames), self.max_height, self.max_width))
                # we center the source profile
                y_coord = (profile_fit_masked.shape[1] - source_profile_frames.shape[1]) // 2
                x_coord = (profile_fit_masked.shape[2] - source_profile_frames.shape[2]) // 2
                profile_fit_masked[:, y_coord:source_profile_frames.shape[1] + y_coord,
                x_coord:source_profile_frames.shape[2] + x_coord] = \
                    source_profile_frames_masked

                profile_fit_masked = profile_fit_masked.reshape((profile_fit_masked.shape[0],
                                                                 profile_fit_masked.shape[1],
                                                                 profile_fit_masked.shape[2], 1))

                inputs_dict["input_2"][index_batch] = profile_fit_masked

        # print(f"End generate_movies_from_metadata() in cinac_movie_patch.py")

        if with_labels:
            return inputs_dict, labels
        else:
            return inputs_dict

    def __str__(self):
        bonus_str = ""
        if self.with_neuropil_mask:
            bonus_str = " + one with neuropil mask"
        return f"{self.n_inputs} inputs. Main cell mask + one with all overlaping cells mask{bonus_str}"


class MoviePatchData:

    def __init__(self, cinac_recording, cell, index_movie, max_n_transformations,
                 encoded_frames, decoding_frame_dict, window_len, cell_type_classifier_mode=False,
                 session_id=None, with_info=False, to_keep_absolutely=False,
                 ground_truth=None):
        """

        Args:
            cinac_recording:
            cell:
            index_movie:
            max_n_transformations:
            encoded_frames: could be None if with_info is False
            decoding_frame_dict:could be None if with_info is False
            window_len:
            cell_type_classifier_mode: boolean, indicate if we should classify cell type or cell activity
            session_id: a string representing the id of the session. If None, it will be given a default.
            Session_id is used to stratify movie_patch according to their session, so sessions are balanced between
            themselves. Useful for training data, not to predict
            with_info: to know how many transients in this frame
            to_keep_absolutely:
            ground_truth: if cell activity classifier represents a 1d array, same length as window_len,
            give for each frame of the given cell, if it is active (1) or non active (0). If we use it as a cell type
            classifier then the value is encoded as 0 or 1 for a single class or more integers values for a multi-class
            classifier
        """
        # max_n_transformationsmax number of transformations to a movie patch
        # if the number of available function to transform is lower, the lower one would be kept
        self.manual_max_transformation = max_n_transformations
        self.cinac_recording = cinac_recording
        self.recording_identifier = cinac_recording.identifier
        self.cell = cell
        # session id, allows to stratify data according to the session of the recording
        self.session_id = session_id if session_id is not None else "jon_doe"
        # index of the first frame of the movie over the whole movie
        self.index_movie = index_movie
        self.last_index_movie = index_movie + window_len - 1
        self.window_len = window_len
        self.ground_truth = ground_truth
        self.cell_type_classifier_mode = cell_type_classifier_mode
        if self.ground_truth is not None and (not self.cell_type_classifier_mode):
            if len(self.ground_truth) != self.window_len:
                raise Exception("Ground_truth and window_len should be the same length. "
                                 "Here {len(self.ground_truth)} != {len(self.window_len)}")
        # weight to apply, use by the model to produce the loss function result
        self.weight = 1
        # means it's an import movie patch and that it should not be deleted during stratification
        # also it would have a minimum number of transformation
        self.to_keep_absolutely = to_keep_absolutely
        # number of transformation to perform on this movie, information to use if with_info == True
        # otherwise it means the object will be transform with the self.data_augmentation_fct
        if self.to_keep_absolutely:
            self.n_augmentations_to_perform = 3
        else:
            self.n_augmentations_to_perform = 0

        # used if a movie_data has been copied
        self.data_augmentation_fct = None

        # set of functions used for data augmentation, one will be selected when copying a movie
        self.data_augmentation_fct_list = list()
        # functions based on rotations and flips
        rot_fct = []
        # adding fct to the set
        flips = [horizontal_flip, vertical_flip, v_h_flip]
        for flip in flips:
            rot_fct.append(flip)
        # 180° angle is the same as same as v_h_flip
        # 10 angles
        rotation_angles = np.array([20, 50, 90, 120, 160, 200, 230, 270, 310, 240])
        np.random.shuffle(rotation_angles)
        for angle in rotation_angles:
            rot_fct.append(lambda movie: rotate_movie(movie, angle))
        # 24 shifting transformations combinaison
        x_shift_y_shift_couples = []
        for x_shift in np.arange(-2, 3):
            for y_shift in np.arange(-2, 3):
                if (x_shift == 0) and (y_shift == 0):
                    continue
                x_shift_y_shift_couples.append((x_shift, y_shift))
        shifts_fct = []
        # keeping 11 shifts, from random
        n_shifts = 11
        shift_indices = np.arange(len(x_shift_y_shift_couples))
        if n_shifts < len(shift_indices):
            np.random.shuffle(shift_indices)
            shift_indices = shift_indices[:n_shifts]
        for index in shift_indices:
            x_shift = x_shift_y_shift_couples[index][0]
            y_shift = x_shift_y_shift_couples[index][1]
            shifts_fct.append(lambda movie: shift_movie(movie, x_shift=x_shift, y_shift=x_shift))

        for i in np.arange(max(len(rot_fct), len(shifts_fct))):
            if i < len(rot_fct):
                self.data_augmentation_fct_list.append(rot_fct[i])
            if i < len(shifts_fct):
                self.data_augmentation_fct_list.append(shifts_fct[i])

        self.n_available_augmentation_fct = min(self.manual_max_transformation, len(self.data_augmentation_fct_list))

        # movie_info dict containing the different informations about the movie such as the number of transients etc...
        """
        Keys so far for self.movie_info (with value type) -> comments :

        n_transient (int)
        transients_lengths (list of int)
        transients_amplitudes (list of float)
        n_cropped_transient (int) -> max value should be 2
        cropped_transients_lengths (list of int)
        n_fake_transient (int)
        n_cropped_fake_transient (int) > max value should be 2
        fake_transients_lengths (list of int)
        fake_transients_amplitudes (list of float)
        """
        self.movie_info = None
        self.encoded_frames = encoded_frames
        self.decoding_frame_dict = decoding_frame_dict
        if with_info:
            self.movie_info = dict()
            # then we want to know how many transients in this frame etc...
            # each code represent a specific event
            unique_codes = np.unique(encoded_frames[index_movie:index_movie + window_len])
            # print(f"unique_codes {unique_codes},  len {len(unique_codes)}")
            is_only_neuropil = True
            for code in unique_codes:
                event = decoding_frame_dict[code]
                if not event.neuropil:
                    is_only_neuropil = False

                if event.real_transient or event.fake_transient:

                    # we need to determine if it's a cropped one or full one
                    if (event.first_frame_event < index_movie) or (event.last_frame_event > self.last_index_movie):
                        # it's cropped
                        if event.real_transient:
                            key_str = "n_cropped_transient"
                            if "cropped_transients_lengths" not in self.movie_info:
                                self.movie_info["cropped_transients_lengths"] = []
                            self.movie_info["cropped_transients_lengths"].append(event.length_event)
                            if "transients_amplitudes" not in self.movie_info:
                                self.movie_info["transients_amplitudes"] = []
                            self.movie_info["transients_amplitudes"].append(event.amplitude)
                        else:
                            key_str = "n_cropped_fake_transient"
                            if "fake_transients_amplitudes" not in self.movie_info:
                                self.movie_info["fake_transients_amplitudes"] = []
                            self.movie_info["fake_transients_amplitudes"].append(event.amplitude)
                        self.movie_info[key_str] = self.movie_info.get(key_str, 0) + 1
                        continue

                    # means it's a full transient
                    if event.real_transient:
                        key_str = "n_transient"
                        if "transients_lengths" not in self.movie_info:
                            self.movie_info["transients_lengths"] = []
                        self.movie_info["transients_lengths"].append(event.length_event)
                        if "transients_amplitudes" not in self.movie_info:
                            self.movie_info["transients_amplitudes"] = []
                        self.movie_info["transients_amplitudes"].append(event.amplitude)
                    else:
                        key_str = "n_fake_transient"
                        if "fake_transients_lengths" not in self.movie_info:
                            self.movie_info["fake_transients_lengths"] = []
                        self.movie_info["fake_transients_lengths"].append(event.length_event)
                        if "fake_transients_amplitudes" not in self.movie_info:
                            self.movie_info["fake_transients_amplitudes"] = []
                        self.movie_info["fake_transients_amplitudes"].append(event.amplitude)
                    self.movie_info[key_str] = self.movie_info.get(key_str, 0) + 1
            if is_only_neuropil:
                self.movie_info["only_neuropil"] = True

    def get_labels(self, using_multi_class):
        """
        Return the labels for this data, could be if the cell is active for any given frame or the cell
        type depending on the classifier mode
        Args:
            using_multi_class:

        Returns:

        """
        frames = np.arange(self.index_movie, self.last_index_movie + 1)
        if using_multi_class <= 1:
            return self.ground_truth
        else:
            if self.cell_type_classifier_mode:
                labels = np.zeros(using_multi_class, dtype="uint8")
                labels[self.ground_truth] = 1
                return labels

            if using_multi_class == 3:
                unique_codes = np.unique(self.encoded_frames[frames])
                labels = np.zeros((self.window_len, using_multi_class), dtype="uint8")
                # class 0: real transient
                # class 1: fake transient
                # class 2 is "unclassifierd" or "noise" that includes decay and neuropil
                for code in unique_codes:
                    movie_event = self.decoding_frame_dict[code]
                    if movie_event.real_transient:
                        labels[self.encoded_frames[frames] == code, 0] = 1
                    elif movie_event.fake_transient:
                        labels[self.encoded_frames[frames] == code, 1] = 1
                    else:
                        labels[self.encoded_frames[frames] == code, 2] = 1
                return labels
            else:
                raise Exception(f"using_multi_class {using_multi_class} not implemented yet")

    def __eq__(self, other):
        if self.recording_identifier != other.recording_identifier:
            return False
        if self.cell != other.cell:
            return False
        if self.index_movie != self.index_movie:
            return False
        return True

    def copy(self):
        movie_copy = MoviePatchData(cinac_recording=self.cinac_recording, cell=self.cell,
                                    index_movie=self.index_movie, session_id=self.session_id,
                                    max_n_transformations=self.manual_max_transformation,
                                    encoded_frames=self.encoded_frames, decoding_frame_dict=self.decoding_frame_dict,
                                    window_len=self.window_len, ground_truth=self.ground_truth,
                                    cell_type_classifier_mode=self.cell_type_classifier_mode,
                                    to_keep_absolutely=self.to_keep_absolutely)
        movie_copy.data_augmentation_fct = self.data_augmentation_fct
        return movie_copy

    def add_n_augmentation(self, n_augmentation):
        self.n_augmentations_to_perform = min(self.n_augmentations_to_perform + n_augmentation,
                                              self.n_available_augmentation_fct)

    def pick_a_transformation_fct(self):
        if len(self.data_augmentation_fct_list) > 0:
            fct = self.data_augmentation_fct_list[0]
            self.data_augmentation_fct_list = self.data_augmentation_fct_list[1:]
            return fct
        return None

    def is_only_neuropil(self):
        """

        :return: True if there is only neuropil (no transients), False otherwise
        """
        if self.movie_info is None:
            return False

        if "n_transient" in self.movie_info:
            return False
        if "n_cropped_transient" in self.movie_info:
            return False
        if "n_fake_transient" in self.movie_info:
            return False
        if "n_cropped_fake_transient" in self.movie_info:
            return False

        return True

# TODO: use tf.data instead of keras.utils.Sequence in the future
class DataGenerator(keras.utils.Sequence):
    """
    Based on an exemple found in https://stanford.edu/~shervine/blog/keras-how-to-generate-data-on-the-fly
    Feed to keras to generate data
    """

    # 'Generates data for Keras'
    def __init__(self, data_list, movie_patch_generator,
                 batch_size, window_len, with_augmentation,
                 pixels_around, buffer, max_width, max_height,
                 is_shuffle=True):
        """

        :param data_list: a list containing the information to get the data. Each element
        is an instance of MoviePatchData
        :param batch_size:
        :param window_len:
        :param with_augmentation:
        :param is_shuffle:
        :param max_width:
        :param max_height:
        :param cell_type_classifier_mode: indicate the labeling is regarding what is the cell type and not is the cell
        active
        """
        # 'Initialization'
        self.max_width = max_width
        self.max_height = max_height
        self.pixels_around = pixels_around
        self.buffer = buffer
        self.window_len = window_len
        self.input_shape = (self.window_len, self.max_height, self.max_width, 1)
        self.batch_size = batch_size
        self.data_list = data_list
        self.with_augmentation = with_augmentation
        self.movie_patch_generator = movie_patch_generator
        # to improve performance, keep in memory the mask_profile of a cell and the coords of the frame surrounding the
        # the cell, the key is a string ms.description + cell
        # not used anymore
        # self.source_profiles_dict = dict()

        if self.with_augmentation:
            # augment the dict now, adding to the key a str representing the transformation and same for
            # in the value
            self.prepare_augmentation()

        # useful for the shuffling
        self.n_samples = len(self.data_list)
        # self.n_channels = n_channels
        # self.n_classes = n_classes
        self.is_shuffle = is_shuffle
        self.indexes = None
        self.on_epoch_end()

    def prepare_augmentation(self):
        n_samples = len(self.data_list)
        print(f"n_samples before data augmentation: {n_samples}")
        new_data = []

        for index_data in np.arange(n_samples):
            movie_data = self.data_list[index_data]
            # we will do as many transformation as indicated in movie_data.n_augmentations_to_perform
            if movie_data.n_augmentations_to_perform == 0:
                continue
            for t in np.arange(movie_data.n_augmentations_to_perform):
                if t >= movie_data.n_available_augmentation_fct:
                    break
                new_movie = movie_data.copy()
                new_movie.data_augmentation_fct = movie_data.pick_a_transformation_fct()
                new_data.append(new_movie)

        self.data_list.extend(new_data)

        print(f"n_samples after data augmentation: {len(self.data_list)}")

    def __len__(self):
        # 'Denotes the number of batches per epoch'
        return int(np.floor(self.n_samples / self.batch_size))

    def __getitem__(self, index):
        # 'Generate one batch of data'
        # Generate indexes of the batch
        indexes = self.indexes[index * self.batch_size:(index + 1) * self.batch_size]
        # print(f"len(indexes) {len(indexes)}")
        # Find list of IDs
        data_list_tmp = [self.data_list[k] for k in indexes]

        # Generate data
        data, labels, sample_weights = self.__data_generation(data_list_tmp)

        return data, labels, sample_weights

    def on_epoch_end(self):
        # 'Updates indexes after each epoch'
        self.indexes = np.arange(self.n_samples)
        # TODO: each mini-batch should have the same proportion of data (neuropil, transients, fake transients)
        # TODO: create a function that shuffle the index with respect of this information
        if self.is_shuffle:
            np.random.shuffle(self.indexes)
        # self.data_keys = list(self.data_dict.keys())
        # if self.is_shuffle:
        #     shuffle(self.data_keys)

    def __data_generation(self, data_list_tmp):
        # len(data_list_tmp) == self.batch_size
        # 'Generates data containing batch_size samples' # data : (self.batch_size, *dim, n_channels)
        # Initialization

        # data, data_masked, labels = generate_movies_from_metadata(movie_data_list=data_list_tmp,
        #                                                           window_len=self.window_len,
        #                                                           max_width=self.max_width,
        #                                                           max_height=self.max_height,
        #                                                           pixels_around=self.pixels_around,
        #                                                           buffer=self.buffer,
        #                                                           source_profiles_dict=self.source_profiles_dict)
        data_dict, labels = self.movie_patch_generator.generate_movies_from_metadata(movie_data_list=data_list_tmp,
                                                                                     memory_dict=None)
        # print(f"__data_generation data.shape {data.shape}")
        # put more weight to the active frames
        # TODO: reshape labels such as shape is (batch_size, window_len, 1) and then use "temporal" mode in compile
        # TODO: otherwise, use the weight in the movie_data in data_list_tmp to apply the corresponding weight
        # sample_weights = np.ones(labels.shape)
        # sample_weights[labels == 1] = 5
        sample_weights = np.ones(labels.shape[0])

        for index_batch, movie_data in enumerate(data_list_tmp):
            sample_weights[index_batch] = movie_data.weight

        return data_dict, labels, sample_weights
