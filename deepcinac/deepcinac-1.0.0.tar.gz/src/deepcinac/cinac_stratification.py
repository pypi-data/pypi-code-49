import numpy as np
from deepcinac.utils.utils import get_continous_time_periods, find_all_onsets_and_peaks_on_fluorescence_signal

def neuronal_activity_encoding(raw_traces, smooth_traces, raster_dur):
    """
    Give for each frame of the cell what kind of activity is going on (real transient, fake etc...)
    Args:
        raw_traces: 1d float representing the raw fluorescence signal (should be normalized using z-score)
        smooth_traces: 1d float representing the smoothed fluorescence signal (should be normalized using z-score)
        raster_dur: 1d int (or bool), representing the frames during which a given cell is active
        (corresponding to the traces). It represents the "ground truth" used to know real transients.

    Returns:

    """
    n_frames = len(raw_traces)
    encoded_frames = np.zeros(n_frames, dtype="int16")
    decoding_frame_dict = dict()
    # zero will be the Neuropil
    decoding_frame_dict[0] = NeuropilEvent(frame_index=None)
    next_code = 1

    # first we add the real transient
    transient_periods = get_continous_time_periods(raster_dur)
    # print(f"sum ms.spike_struct.spike_nums_dur[cell] {np.sum(ms.spike_struct.spike_nums_dur[cell])}")
    # list of tuple, first frame and last frame (included) of each transient
    for transient_period in transient_periods:
        amplitude = np.max(raw_traces[transient_period[0]:transient_period[1] + 1])
        encoded_frames[transient_period[0]:transient_period[1] + 1] = next_code
        event = RealTransientEvent(frames_period=transient_period, amplitude=amplitude)
        decoding_frame_dict[next_code] = event
        next_code += 1

    # then we look for all transient and take the mean + 1 std of transient peak
    # and keep the one that are not real as fake one
    # for that first we need to compute peaks_nums, spike_nums and spike_nums_dur from all onsets
    raster_dur_all = find_all_onsets_and_peaks_on_fluorescence_signal(
        smooth_trace=smooth_traces, threshold_factor=1)
    all_transient_periods = get_continous_time_periods(raster_dur_all)
    for transient_period in all_transient_periods:
        # checking if it's part of a real transient
        sp_dur = raster_dur
        if np.sum(sp_dur[transient_period[0]:transient_period[1] + 1]) > 0:
            continue
        amplitude = np.max(raw_traces[transient_period[0]:transient_period[1] + 1])
        encoded_frames[transient_period[0]:transient_period[1] + 1] = next_code
        event = FakeTransientEvent(frames_period=transient_period, amplitude=amplitude)
        decoding_frame_dict[next_code] = event
        next_code += 1

    return encoded_frames, decoding_frame_dict


class MovieEvent:
    """
    Class that represent an event in a movie, for exemple a transient, neuropil etc...
    """

    def __init__(self):
        self.neuropil = False
        self.real_transient = False
        self.fake_transient = False
        self.movement = False
        # length in frames
        self.length_event = 1
        self.first_frame_event = None
        self.last_frame_event = None


class NeuropilEvent(MovieEvent):
    # it includes neuropil, but also decay of transient, everything that is not real or fake transient
    def __init__(self, frame_index):
        super().__init__()
        self.neuropil = True
        # frame_index could be None, in case we don't care about frame index
        self.first_frame_event = frame_index
        self.last_frame_event = frame_index


class RealTransientEvent(MovieEvent):

    def __init__(self, frames_period, amplitude):
        super().__init__()
        self.real_transient = True
        self.first_frame_event = frames_period[0]
        self.last_frame_event = frames_period[1]
        self.length_event = self.last_frame_event - self.first_frame_event + 1
        self.amplitude = amplitude


class FakeTransientEvent(MovieEvent):

    def __init__(self, frames_period, amplitude):
        super().__init__()
        self.fake_transient = True
        self.first_frame_event = frames_period[0]
        self.last_frame_event = frames_period[1]
        self.length_event = self.last_frame_event - self.first_frame_event + 1
        self.amplitude = amplitude


class MovementEvent(MovieEvent):

    def __init__(self, frames_period):
        super().__init__()
        self.movement = True
        self.first_frame_event = frames_period[0]
        self.last_frame_event = frames_period[1]
        self.length_event = self.last_frame_event - self.first_frame_event + 1


class StratificationCellTypeCamembert:

    def __init__(self, data_list, description,
                 n_max_transformations, debug_mode=False):
        self.data_list = data_list
        self.n_movie_patch = len(data_list)
        self.description = description
        self.debug_mode = debug_mode
        self.n_max_transformations = n_max_transformations
        if debug_mode:
            self.print_data_description()

    def augment_them_all(self):
        """
        Add to all movie patches in the camembert a given number of augmentation self.n_max_transformations
        :return:
        """
        for movie_patch_data in self.data_list:
            movie_patch_data.add_n_augmentation(self.n_max_transformations)

    def print_data_description(self):
        n_movie_patch = 0
        for movie_data in self.data_list:
            n_movie_patch += (1 + movie_data.n_augmentations_to_perform)

        # key is a string representing the cell type, and value an int representing the number of movie_patch of
        # this cell type
        cell_type_count_dict = dict()
        for movie_index, movie_data in enumerate(self.data_list):
            cell_type = movie_data.cinac_recording.cell_type
            cell_type_count_dict[cell_type] = cell_type_count_dict.get(cell_type, 0) + \
                                              (movie_data.n_augmentations_to_perform + 1)

        print("")
        print("-"*100)
        print("StratificationCellTypeCamembert")
        print(f"N movie patches: {n_movie_patch}")
        for cell_type, movie_patches_count in cell_type_count_dict.items():
            print(f"N movie patches for {cell_type}: {movie_patches_count}")
        print("-" * 100)
        print("")

class StratificationCamembert:

    def __init__(self, data_list, description,
                 n_max_transformations, debug_mode=False):
        self.data_list = data_list
        self.n_movie_patch = len(data_list)
        self.description = description
        self.debug_mode = debug_mode
        self.n_max_transformations = n_max_transformations

        ##### for fake and real transients
        self.n_transient_total = dict()
        self.n_transient_total["fake"] = 0
        self.n_transient_total["real"] = 0

        self.n_cropped_transient_total = dict()
        self.n_cropped_transient_total["fake"] = 0
        self.n_cropped_transient_total["real"] = 0

        self.n_full_transient_total = dict()
        self.n_full_transient_total["fake"] = 0
        self.n_full_transient_total["real"] = 0

        self.transient_movies = dict()
        self.transient_movies["fake"] = []
        self.transient_movies["real"] = []

        self.cropped_transient_movies = dict()
        self.cropped_transient_movies["fake"] = []
        self.cropped_transient_movies["real"] = []

        self.min_augmentation_for_transient = dict()
        self.min_augmentation_for_transient["fake"] = 2
        self.min_augmentation_for_transient["real"] = 2

        self.min_augmentation_for_cropped_transient = dict()
        self.min_augmentation_for_cropped_transient["fake"] = 0
        self.min_augmentation_for_cropped_transient["real"] = 0

        # count
        self.n_full_1_transient = dict()
        self.n_full_1_transient["fake"] = 0
        self.n_full_1_transient["real"] = 0

        self.n_full_2p_transient = dict()
        self.n_full_2p_transient["fake"] = 0
        self.n_full_2p_transient["real"] = 0

        # list of movie_data with full transient (1 rep)
        self.full_1_transient = dict()
        self.full_1_transient["fake"] = []
        self.full_1_transient["real"] = []

        self.full_2p_transient = dict()
        self.full_2p_transient["fake"] = []
        self.full_2p_transient["real"] = []

        # contains the indices of the movies (from data_list) in a sorted order (based on amplitude, from low to high)
        self.full_transient_sorted_amplitude = dict()
        self.full_transient_sorted_amplitude["fake"] = []
        self.full_transient_sorted_amplitude["real"] = []

        self.n_transient_dict = dict()
        self.n_transient_dict["fake"] = dict()
        self.n_transient_dict["real"] = dict()

        # perc of full with 1 transient
        self.full_1_transient_perc = dict()
        self.full_1_transient_perc["fake"] = 0
        self.full_1_transient_perc["real"] = 0

        # perc of full with 2 transients or more
        self.full_2p_transient_perc = dict()
        self.full_2p_transient_perc["fake"] = 0
        self.full_2p_transient_perc["real"] = 0

        # % among all transients
        self.full_transient_perc = dict()
        self.full_transient_perc["fake"] = 0
        self.full_transient_perc["real"] = 0

        self.cropped_transient_perc = dict()
        self.cropped_transient_perc["fake"] = 0
        self.cropped_transient_perc["real"] = 0

        self.n_cropped_transient_dict = dict()
        self.n_cropped_transient_dict["fake"] = dict()
        self.n_cropped_transient_dict["real"] = dict()

        self.total_transient_perc = dict()
        self.total_transient_perc["fake"] = 0
        self.total_transient_perc["real"] = 0

        self.transient_lengths = dict()
        self.transient_lengths["fake"] = []
        self.transient_lengths["real"] = []

        self.transient_amplitudes = dict()
        self.transient_amplitudes["fake"] = []
        self.transient_amplitudes["real"] = []

        # MoviePatchData list
        self.neuropil_movies = []

        self.n_only_neuropil = 0
        self.only_neuropil_perc = 0
        self.n_real_and_fake_transient = 0
        # disct with key ms.description and value the number of movies for this session
        self.n_movies_by_session = {}
        # key int representing age, and value the number of movie for this session
        self.n_movies_by_age = {}

        self.compute_slices()

    def compute_slices(self):
        """
        Compute the slices of the camembert
        :return:
        """
        # printing option
        # \x1b
        reset_color = '\033[30m'
        # red: 31, blue: 34
        perc_color = '\033[34m'
        self.n_movie_patch = 0
        for movie_data in self.data_list:
            self.n_movie_patch += (1 + movie_data.n_augmentations_to_perform)

        sorted_amplitudes = dict()
        amplitudes_movie_index = dict()

        for which_ones in ["real", "fake"]:
            # initializing variables
            self.transient_movies[which_ones] = []
            self.cropped_transient_movies[which_ones] = []
            self.full_1_transient[which_ones] = []
            self.full_2p_transient[which_ones] = []
            self.n_transient_dict[which_ones] = dict()
            self.n_cropped_transient_dict[which_ones] = dict()
            self.transient_lengths[which_ones] = []
            self.transient_amplitudes[which_ones] = []
            self.full_transient_sorted_amplitude[which_ones] = []
            sorted_amplitudes[which_ones] = []
            amplitudes_movie_index[which_ones] = []

        # MoviePatchData list
        self.neuropil_movies = []
        self.n_only_neuropil = 0
        self.only_neuropil_perc = 0
        self.n_real_and_fake_transient = 0
        # disct with key ms.description and value the number of movies for this session
        self.n_movies_by_session = {}
        # key int representing age, and value the number of movie for this session
        self.n_movies_by_age = {}

        if self.debug_mode:
            print(f"{'##' * 10}")
            print(f"{self.description}")
            print(f"{'##' * 10}")
        for movie_index, movie_data in enumerate(self.data_list):
            movie_info = movie_data.movie_info
            only_neuropil = True
            with_real_transient = False
            with_cropped_real_transient = False
            with_fake_transient = False
            n_movies = 1 + movie_data.n_augmentations_to_perform
            if "n_transient" in movie_info:
                with_real_transient = True
                only_neuropil = False
                n_transient = movie_info["n_transient"]
                if n_transient == 1:
                    self.full_1_transient["real"].append(movie_data)
                else:
                    self.full_2p_transient["real"].append(movie_data)
                self.transient_movies["real"].append(movie_data)
                self.n_transient_dict["real"][n_transient] = self.n_transient_dict["real"].get(n_transient,
                                                                                               0) + n_movies
                if "transients_amplitudes" in movie_info:
                    self.transient_amplitudes["real"].extend(movie_info["transients_amplitudes"])
                    sorted_amplitudes["real"].append(np.max(movie_info["transients_amplitudes"]))
                    amplitudes_movie_index["real"].append(movie_index)
                if "transients_lengths" in movie_info:
                    self.transient_lengths["real"].extend(movie_info["transients_lengths"])
            if ("n_cropped_transient" in movie_info) and (not with_real_transient):
                only_neuropil = False
                with_cropped_real_transient = True
                self.cropped_transient_movies["real"].append(movie_data)
                n_cropped_transient = movie_info["n_cropped_transient"]
                self.n_cropped_transient_dict["real"][n_cropped_transient] = \
                    self.n_cropped_transient_dict["real"].get(n_cropped_transient, 0) + n_movies
                if "transients_amplitudes" in movie_info:
                    sorted_amplitudes["real"].append(np.max(movie_info["transients_amplitudes"]))
                    amplitudes_movie_index["real"].append(movie_index)
            if ("n_fake_transient" in movie_info) and (not with_real_transient) and (not with_cropped_real_transient):
                only_neuropil = False
                with_fake_transient = True
                self.transient_movies["fake"].append(movie_data)
                n_fake_transient = movie_info["n_fake_transient"]
                if n_fake_transient == 1:
                    self.full_1_transient["fake"].append(movie_data)
                else:
                    self.full_2p_transient["fake"].append(movie_data)
                self.n_transient_dict["fake"][n_fake_transient] = \
                    self.n_transient_dict["fake"].get(n_fake_transient, 0) + n_movies

                if "fake_transients_amplitudes" in movie_info:
                    self.transient_amplitudes["fake"].extend(movie_info["fake_transients_amplitudes"])
                    sorted_amplitudes["fake"].append(np.max(movie_info["fake_transients_amplitudes"]))
                    amplitudes_movie_index["fake"].append(movie_index)
                if "fake_transients_lengths" in movie_info:
                    self.transient_lengths["fake"].extend(movie_info["fake_transients_lengths"])
            if ("n_cropped_fake_transient" in movie_info) and (not with_real_transient) and (not with_fake_transient) \
                    and (not with_cropped_real_transient):
                only_neuropil = False
                self.cropped_transient_movies["fake"].append(movie_data)
                n_cropped_fake_transient = movie_info["n_cropped_fake_transient"]
                self.n_cropped_transient_dict["fake"][n_cropped_fake_transient] = \
                    self.n_cropped_transient_dict["fake"].get(n_cropped_fake_transient, 0) + n_movies
                if "fake_transients_amplitudes" in movie_info:
                    sorted_amplitudes["fake"].append(np.max(movie_info["fake_transients_amplitudes"]))
                    amplitudes_movie_index["fake"].append(movie_index)

            if with_fake_transient and with_real_transient:
                self.n_real_and_fake_transient += n_movies

            if only_neuropil:
                self.n_only_neuropil += n_movies
                self.neuropil_movies.append(movie_data)
            # TODO: See to replace this by a field category that could be encoded in cinac
            self.n_movies_by_session[movie_data.session_id] = \
                self.n_movies_by_session.get(movie_data.session_id, 0) + n_movies
            # self.n_movies_by_age[movie_data.ms.age] = self.n_movies_by_age.get(movie_data.ms.age, 0) + n_movies

        # sorting movie_data by amplitude, from the smallest to the biggest
        for which_ones in ["real", "fake"]:
            index_array = np.argsort(sorted_amplitudes[which_ones])
            for index in index_array:
                self.full_transient_sorted_amplitude[which_ones].append(amplitudes_movie_index[which_ones][index])

        self.only_neuropil_perc = (self.n_only_neuropil / self.n_movie_patch) * 100

        if self.debug_mode:
            print(f"{'#' * 10}")
            print(f"{'#' * 10}")
            print(f"{'#' * 10}")
            print(f"len train data {self.n_movie_patch}")
            print("")
            print(f"n_real_and_fake_transient {self.n_real_and_fake_transient}")
            print("")
            print("")

        for which_ones in ["real", "fake"]:
            # calculating the max number of augmentations done
            movies = self.transient_movies[which_ones]
            movies.extend(self.cropped_transient_movies[which_ones])
            transformations_done = []
            for movie in movies:
                transformations_done.append(movie.n_augmentations_to_perform)
            transformations_done = np.array(transformations_done)
            if self.debug_mode and (len(transformations_done) > 0):
                print(f"{which_ones}: transformations, min {np.min(transformations_done)}, "
                      f"max {np.max(transformations_done)}, "
                      f"mean {str(np.round(np.mean(transformations_done), 2))}")
            if self.debug_mode:
                print(f"{which_ones}: n_transient_dict {self.n_transient_dict[which_ones]}")
            self.n_full_transient_total[which_ones] = 0
            self.n_full_1_transient[which_ones] = 0
            self.n_full_2p_transient[which_ones] = 0
            for rep, count in self.n_transient_dict[which_ones].items():
                self.n_full_transient_total[which_ones] += count
                if rep == 1:
                    self.n_full_1_transient[which_ones] += count
                else:
                    self.n_full_2p_transient[which_ones] += count
            if self.n_full_transient_total[which_ones] > 0:
                self.full_1_transient_perc[which_ones] = (self.n_full_1_transient[which_ones] /
                                                          self.n_full_transient_total[which_ones]) * 100
                self.full_2p_transient_perc[which_ones] = (self.n_full_2p_transient[which_ones] /
                                                           self.n_full_transient_total[which_ones]) * 100
                if self.debug_mode:
                    print(perc_color + f"1 full {which_ones} transient perc: "
                    f"{str(np.round(self.full_1_transient_perc[which_ones], 2))} %" + reset_color)
                    print(perc_color + f"2+ full {which_ones} transient perc: "
                    f"{str(np.round(self.full_2p_transient_perc[which_ones], 2))} %" + reset_color)
            if self.debug_mode:
                print(f"{which_ones}: n_cropped_transient_dict {self.n_cropped_transient_dict[which_ones]}")
            self.n_cropped_transient_total[which_ones] = 0
            for rep, count in self.n_cropped_transient_dict[which_ones].items():
                self.n_cropped_transient_total[which_ones] += count

            self.n_transient_total[which_ones] = self.n_cropped_transient_total[which_ones] + \
                                                 self.n_full_transient_total[which_ones]
            self.total_transient_perc[which_ones] = (self.n_transient_total[which_ones] / self.n_movie_patch) * 100

            if self.n_transient_total[which_ones] > 0:
                self.full_transient_perc[which_ones] = (self.n_full_transient_total[which_ones] /
                                                        self.n_transient_total[which_ones]) * 100
                self.cropped_transient_perc[which_ones] = (self.n_cropped_transient_total[which_ones] /
                                                           self.n_transient_total[which_ones]) * 100
                if self.debug_mode:
                    print(perc_color + f"Full {which_ones}: "
                    f"{str(np.round(self.full_transient_perc[which_ones], 2))} %" + reset_color)
                    print(perc_color + f"Cropped {which_ones}: "
                    f"{str(np.round(self.cropped_transient_perc[which_ones], 2))} %" + reset_color)
            if self.debug_mode and (len(self.transient_lengths[which_ones]) > 0):
                print(f"{which_ones}: transient_lengths n {len(self.transient_lengths[which_ones])} / "
                      f"min-max {np.min(self.transient_lengths[which_ones])} - "
                      f"{np.max(self.transient_lengths[which_ones])}")
                print(f"{which_ones}: mean transient_amplitudes {np.mean(self.transient_amplitudes[which_ones])}")
                print("")
                print("")

        if self.debug_mode:
            for which_ones in ["real", "fake"]:
                print(perc_color + f"Total movie with {which_ones} transients {self.n_transient_total[which_ones]}: "
                f"{str(np.round(self.total_transient_perc[which_ones], 2))} %" + reset_color)
            print(perc_color + f"n_only_neuropil {self.n_only_neuropil}: "
            f"{str(np.round(self.only_neuropil_perc, 2))} %" + reset_color)
            print("")
            print("")

        # if self.debug_mode:
            print(f"n_movies_by_session {self.n_movies_by_session}")
            for session, count in self.n_movies_by_session.items():
                print(perc_color + f"{session}: {str(np.round((count / self.n_movie_patch) * 100, 2))} %" + reset_color)
        #     print(f"n_movies_by_age {self.n_movies_by_age}")
        #     for age, count in self.n_movies_by_age.items():
        #         print(perc_color + f"p{age}: {str(np.round((count / self.n_movie_patch) * 100, 2))} %" + reset_color)

    def add_augmentation_to_all_patches(self, n_augmentation):
        """
        Add to all movie patches in the camember a given number of augmentation, except neuropil
        :param n_augmentation:
        :return:
        """
        for movie_patch_data in self.data_list:
            if "only_neuropil" not in movie_patch_data.movie_info:
                movie_patch_data.add_n_augmentation(n_augmentation)

    def set_weights(self):
        # first we compute the thresholds
        # print(f"len(self.transient_amplitudes['real']) {len(self.transient_amplitudes['real'])}")
        real_amplitudes = np.unique(self.transient_amplitudes["real"])
        # print(f"real_amplitudes {len(real_amplitudes)}")
        fake_amplitudes = np.unique(self.transient_amplitudes["fake"])
        real_lengths = np.unique(self.transient_lengths["real"])
        fake_lengths = np.unique(self.transient_lengths["fake"])

        if len(real_amplitudes) > 0:
            real_amplitudes_threshold = np.percentile(real_amplitudes, 10)
        else:
            real_amplitudes_threshold = None
        if len(fake_amplitudes) > 0:
            fake_amplitudes_threshold = np.percentile(fake_amplitudes, 90)
        else:
            fake_amplitudes_threshold = None
        if len(real_lengths) > 0:
            real_lengths_threshold = np.percentile(real_lengths, 90)
        else:
            real_lengths_threshold = None

        if len(fake_lengths) > 0:
            fake_lengths_threshold = np.percentile(fake_lengths, 90)
        else:
            fake_lengths_threshold = None

        for movie_data in self.data_list:
            movie_info = movie_data.movie_info
            if "n_transient" in movie_info:
                if movie_info["n_transient"] > 1:
                    movie_data.weight += 5
                if (real_lengths_threshold is not None) and ("transients_lengths" in movie_info):
                    lengths = np.array(movie_info["transients_lengths"])
                    if len(np.where(lengths > real_lengths_threshold)[0]) > 0:
                        # print(f"lengths {lengths}, real_lengths_threshold {real_lengths_threshold}")
                        # means at least a transient length is superior to the 90th percentile
                        movie_data.weight += 3
                if (real_amplitudes_threshold is not None) and ("transients_amplitudes" in movie_info):
                    amplitudes = np.array(movie_info["transients_amplitudes"])
                    if len(np.where(amplitudes < real_amplitudes_threshold)[0]) > 0:
                        # print(f"amplitudes {amplitudes}, real_amplitudes_threshold {real_amplitudes_threshold}")
                        # means at least a transient amplitude is inferior to the 10th percentile
                        movie_data.weight += 3
                continue
            if "n_cropped_transient" in movie_info:
                continue
            if "n_fake_transient" in movie_info:
                movie_data.weight += 50
                if (fake_lengths_threshold is not None) and ("fake_transients_lengths" in movie_info):
                    lengths = np.array(movie_info["fake_transients_lengths"])
                    if len(np.where(lengths > fake_lengths_threshold)[0]) > 0:
                        # print(f"lengths {lengths}, real_lengths_threshold {fake_lengths_threshold}")
                        # means at least a transient length is superior to the 90th percentile
                        movie_data.weight += 5
                if (fake_amplitudes_threshold is not None) and ("fake_transients_amplitudes" in movie_info):
                    amplitudes = np.array(movie_info["fake_transients_amplitudes"])
                    if len(np.where(amplitudes < fake_amplitudes_threshold)[0]) > 0:
                        # means at least a transient amplitude is superior to the 90th percentile
                        movie_data.weight += 10
                continue
            if "n_cropped_fake_transient" in movie_info:
                movie_data.weight += 5

    def balance_all(self, main_ratio_balance, first_round):
        # if a ratio is put to one, then the class is untouched, but then the sum of other ratio should be equal to
        # 1 or set to -1 as well
        # main_ratio_balance = (0.6, 0.25, 0.15)
        if self.debug_mode:
            print("")
            print(f"$$$$$$$$$$$$$$$$$$$$$$ camembert.balance_all {main_ratio_balance} $$$$$$$$$$$$$$$$$$$$$$")
            print("")

        tolerance = 0.5

        # dealing with the case of the ratio is 0
        if (main_ratio_balance[0] == 0) and first_round:
            # then we delete all real transients
            new_data_list = []
            for movie_data in self.data_list:
                movie_info = movie_data.movie_info
                if "n_transient" in movie_info:
                    continue
                if "n_cropped_transient" in movie_info:
                    continue
                new_data_list.append(movie_data)
            self.data_list = new_data_list
            # updating the stat
            self.compute_slices()

        if (main_ratio_balance[1] == 0) and first_round:
            # then we delete all fake transients
            new_data_list = []
            for movie_data in self.data_list:
                movie_info = movie_data.movie_info
                if "n_transient" in movie_info:
                    new_data_list.append(movie_data)
                    continue
                if "n_cropped_transient" in movie_info:
                    new_data_list.append(movie_data)
                    continue
                if "n_fake_transient" in movie_info:
                    continue
                if "n_cropped_fake_transient" in movie_info:
                    continue
                new_data_list.append(movie_data)
            self.data_list = new_data_list
            # updating the stat
            self.compute_slices()

        if (main_ratio_balance[0] > 0) and (main_ratio_balance[1] > 0):

            ratio_real_fake = main_ratio_balance[0] / main_ratio_balance[1]

            if (self.n_transient_total["real"] > 0) and (self.n_transient_total["fake"] > 0):
                if np.abs((self.n_transient_total["real"] / self.n_transient_total["fake"]) - ratio_real_fake) > \
                        tolerance:
                    if (self.n_transient_total["fake"] * ratio_real_fake) > self.n_transient_total["real"]:
                        # it means they are too many fakes, we need to add real transients or delete fake ones
                        if first_round:
                            # we delete fake, as we don't care about balance in fakes during first_round
                            # we want to change self.data_list
                            n_fake_to_delete = int(self.n_transient_total["fake"] -
                                                   (self.n_transient_total["real"] / ratio_real_fake))
                            delete_low_amplitudes_first = True
                            new_data_list = []
                            if delete_low_amplitudes_first:
                                # but keeping some still, thus keeping one and removing one
                                indices_to_remove = []
                                n_fake_removed = 0
                                sorted_index = 0
                                while n_fake_removed < n_fake_to_delete:
                                    if sorted_index >= len(self.full_transient_sorted_amplitude["fake"]):
                                        break
                                    index_data_list = self.full_transient_sorted_amplitude["fake"][sorted_index]
                                    movie_data = self.data_list[index_data_list]
                                    if movie_data.to_keep_absolutely:
                                        # print("while n_fake_removed < n_fake_to_delete: movie_data.to_keep_absolutely")
                                        sorted_index += 1
                                        continue
                                    indices_to_remove.append(index_data_list)
                                    n_fake_removed += (1 + movie_data.n_augmentations_to_perform)

                                for index_data_list, movie_data in enumerate(self.data_list):
                                    if index_data_list in indices_to_remove:
                                        continue
                                    new_data_list.append(movie_data)
                            else:
                                n_fake_removed = 0
                                for movie_data in self.data_list:
                                    if movie_data.to_keep_absolutely:
                                        print("removing fake: movie_data.to_keep_absolutely")
                                        new_data_list.append(movie_data)
                                        continue
                                    movie_info = movie_data.movie_info
                                    if "n_transient" in movie_info:
                                        new_data_list.append(movie_data)
                                        continue
                                    if "n_cropped_transient" in movie_info:
                                        new_data_list.append(movie_data)
                                        continue
                                    if "n_fake_transient" in movie_info:
                                        if n_fake_removed < n_fake_to_delete:
                                            n_fake_removed += (1 + movie_data.n_augmentations_to_perform)
                                            continue
                                    if "n_cropped_fake_transient" in movie_info:
                                        if n_fake_removed < n_fake_to_delete:
                                            n_fake_removed += (1 + movie_data.n_augmentations_to_perform)
                                            continue
                                    new_data_list.append(movie_data)
                            self.data_list = new_data_list
                        else:
                            # we add real transients
                            n_real_to_add = (self.n_transient_total["fake"] * ratio_real_fake) - \
                                            self.n_transient_total["real"]
                            # print(f"n_real_to_add {n_real_to_add}")
                            # we want to add the same numbers such that we keep the ratio among the real_transients
                            # n_unique_real_transients represents the number of original movie patches, without taking in
                            # consideration the transformations that will be made
                            n_unique_real_transients = len(self.transient_movies["real"])
                            n_unique_real_transients += len(self.cropped_transient_movies["real"])
                            n_augmentations_options = [n_unique_real_transients * x for x in
                                                       np.arange(0, (self.n_max_transformations -
                                                                     self.min_augmentation_for_transient["real"]) + 3)]
                            n_augmentations_options = np.array(n_augmentations_options)
                            idx = (np.abs(n_augmentations_options - n_real_to_add)).argmin()
                            # print(f"idx {idx}, len(n_augmentations_options): {len(n_augmentations_options)}")
                            # print(f"n_augmentations_options[idx] {n_augmentations_options[idx]}")
                            if idx > 0:
                                n_transients_at_max_before = 0
                                n_transients_at_max_after = 0
                                n_added = 0
                                for movie_patch_data in self.transient_movies["real"]:
                                    augm_before = movie_patch_data.n_augmentations_to_perform
                                    movie_patch_data.add_n_augmentation(n_augmentation=idx)
                                    augm_after = movie_patch_data.n_augmentations_to_perform
                                    if augm_before == augm_after:
                                        n_transients_at_max_before += 1
                                    elif (augm_before + idx) < augm_after:
                                        n_transients_at_max_after += 1
                                    n_added += (augm_after - augm_before)
                                for movie_patch_data in self.cropped_transient_movies["real"]:
                                    augm_before = movie_patch_data.n_augmentations_to_perform
                                    movie_patch_data.add_n_augmentation(n_augmentation=idx)
                                    augm_after = movie_patch_data.n_augmentations_to_perform
                                    if augm_before == augm_after:
                                        n_transients_at_max_before += 1
                                    elif (augm_before + idx) < augm_after:
                                        n_transients_at_max_after += 1
                                    n_added += (augm_after - augm_before)
                                # TODO: if the ratio is not good, it means we couldn't add more transformation, in that
                                # TODO: case we want to remove some fake frames ?
                                if self.debug_mode:
                                    print(f"n_real_to_add {n_real_to_add}, n_added {n_added}")
                                    # print(f"n_transients_at_max_before {n_transients_at_max_before}, "
                                    #       f"n_transients_at_max_after {n_transients_at_max_before}")

                    else:
                        # it means they are too many real, we need to add fake transients
                        n_fake_to_add = (self.n_transient_total["real"] / ratio_real_fake) - \
                                        self.n_transient_total["fake"]
                        # we want to add the same numbers such that we keep the ratio among the real_transients
                        # n_unique_fake_transients represents the number of original movie patches, without taking in
                        # consideration the transformations that will be made
                        n_unique_fake_transients = len(self.transient_movies["fake"])
                        n_unique_fake_transients += len(self.cropped_transient_movies["fake"])
                        n_augmentations_options = [n_unique_fake_transients * x for x in
                                                   np.arange(1, (self.n_max_transformations -
                                                                 self.min_augmentation_for_transient["fake"]) + 2)]
                        n_augmentations_options = np.array(n_augmentations_options)
                        idx = (np.abs(n_augmentations_options - n_fake_to_add)).argmin()
                        if idx > 0:
                            for movie_patch_data in self.transient_movies["fake"]:
                                movie_patch_data.add_n_augmentation(n_augmentation=idx)
                            for movie_patch_data in self.cropped_transient_movies["fake"]:
                                movie_patch_data.add_n_augmentation(n_augmentation=idx)

            # updating the stat
            self.compute_slices()

        if (main_ratio_balance[2] == 0) and first_round:
            # then we delete all neuropil patches
            new_data_list = []
            for movie_data in self.data_list:
                movie_info = movie_data.movie_info
                if ("only_neuropil" in movie_info) and (not movie_data.to_keep_absolutely):
                    continue
                new_data_list.append(movie_data)
            self.data_list = new_data_list
        elif (main_ratio_balance[2] > 0) and (self.n_only_neuropil > 0):
            if (self.n_transient_total["real"] > 0) or (self.n_transient_total["fake"] > 0):
                n_transient_total = self.n_transient_total["real"] + self.n_transient_total["fake"]
                ratio_transients_neuropils = (main_ratio_balance[0] + main_ratio_balance[1]) / main_ratio_balance[2]
                if np.abs((n_transient_total / self.n_only_neuropil) -
                          ratio_transients_neuropils) > tolerance:
                    if (self.n_only_neuropil * ratio_transients_neuropils) > n_transient_total:
                        # it means they are too many neuropil, we need to remove some
                        # TODO: See to remove neuropils with the lowest variation
                        n_neuropils_to_remove = int(self.n_only_neuropil -
                                                    (n_transient_total / ratio_transients_neuropils))
                        # print(f"!!!!!!!!!!!!!!!!!! n_neuropils_to_remove {n_neuropils_to_remove}")
                        # we want to change self.data_list
                        n_neuropils_removed = 0
                        new_data_list = []
                        for movie_data in self.data_list:
                            movie_info = movie_data.movie_info
                            if ("only_neuropil" in movie_info) and (n_neuropils_removed < n_neuropils_to_remove) and \
                                    (not movie_data.to_keep_absolutely):
                                n_neuropils_removed += 1 + movie_data.n_augmentations_to_perform
                            else:
                                new_data_list.append(movie_data)
                        self.data_list = new_data_list

                    else:
                        # it means they are too many transients, we need to add neuropil
                        if self.debug_mode:
                            print(f"=== adding neuropil")
                        neuropil_to_add = (n_transient_total / ratio_transients_neuropils) - self.n_only_neuropil
                        if self.debug_mode:
                            print(f"=== neuropil_to_add {neuropil_to_add}")
                            print(f"=== len(self.neuropil_movies) {len(self.neuropil_movies)}")
                        augmentation_added = 0
                        movie_index = 0
                        while augmentation_added < neuropil_to_add:
                            self.neuropil_movies[movie_index].add_n_augmentation(n_augmentation=1)
                            movie_index = (movie_index + 1) % len(self.neuropil_movies)
                            augmentation_added += 1

        if self.debug_mode:
            print("")
            print(f"***************** After balancing real transients, fake ones and neuropil *****************")
            print("")
        # updating the stat
        self.compute_slices()

    def balance_transients(self, which_ones, crop_non_crop_ratio_balance, non_crop_ratio_balance):
        # if a ratio is put to one, then the class is untouched, but then the sum of other ratio should be equal to
        # 1 or set to -1 as well
        if which_ones not in ["fake", "real"]:
            raise Exception(f"which_ones not in {['fake', 'real']}")

        if self.debug_mode:
            print("")
            print(f"$$$$$$$$$$$$$$$$$$$$$$ camembert.balance_transients {which_ones} $$$$$$$$$$$$$$$$$$$$$$")
            print("")

        if self.n_transient_total[which_ones] == 0:
            return

        tolerance = 0.5
        if self.min_augmentation_for_transient[which_ones] > 0:
            for movie_data in self.transient_movies[which_ones]:
                movie_data.add_n_augmentation(n_augmentation=self.min_augmentation_for_transient[which_ones])
        if self.min_augmentation_for_cropped_transient[which_ones] > 0:
            for movie_data in self.cropped_transient_movies[which_ones]:
                movie_data.add_n_augmentation(n_augmentation=self.min_augmentation_for_cropped_transient[which_ones])

        if self.debug_mode:
            print("")
            print(f"$$ After adding min augmentation $$")
            print("")
        # updating stat
        self.compute_slices()

        if non_crop_ratio_balance[0] == 0:
            # we want to delete all the full 1 transient
            new_data_list = []
            for movie_data in self.data_list:
                movie_info = movie_data.movie_info
                if movie_data.to_keep_absolutely:
                    print("non_crop_ratio_balance[0] == 0: movie_data.to_keep_absolutely")
                    new_data_list.append(movie_data)
                    continue
                if (which_ones == "fake") and ("n_fake_transient" in movie_info) \
                        and ("n_transient" not in movie_info) and ("n_cropped_transient" not in movie_info):
                    if movie_info["n_fake_transient"] == 1:
                        continue
                if (which_ones == "real") and ("n_transient" in movie_info):
                    if movie_info["n_transient"] == 1:
                        continue
                new_data_list.append(movie_data)
            self.data_list = new_data_list

            # updating stat
            self.compute_slices()
        if non_crop_ratio_balance[1] == 0:
            # we want to delete all the  2p full transient
            new_data_list = []
            for movie_data in self.data_list:
                movie_info = movie_data.movie_info
                if movie_data.to_keep_absolutely:
                    print("non_crop_ratio_balance[1] == 0: movie_data.to_keep_absolutely")
                    new_data_list.append(movie_data)
                    continue
                if (which_ones == "fake") and ("n_fake_transient" in movie_info) \
                        and ("n_transient" not in movie_info) and ("n_cropped_transient" not in movie_info):
                    if movie_info["n_fake_transient"] > 1:
                        continue
                if (which_ones == "real") and ("n_transient" in movie_info):
                    if movie_info["n_transient"] > 1:
                        continue
                new_data_list.append(movie_data)
            self.data_list = new_data_list

            # updating stat
            self.compute_slices()

        if (non_crop_ratio_balance[0] > 0) and (non_crop_ratio_balance[1] > 0):
            ratio = non_crop_ratio_balance[0] / non_crop_ratio_balance[1]
            if ((self.n_full_2p_transient[which_ones] > 0) and (self.n_full_1_transient[which_ones] > 0)) and \
                    (np.abs(
                        (self.n_full_1_transient[which_ones] / self.n_full_2p_transient[
                            which_ones]) - ratio) > tolerance):
                # we have a 5% tolerance
                if (self.n_full_2p_transient[which_ones] * ratio) > self.n_full_1_transient[which_ones]:
                    # to balance real, we augment them, to balance fake: we remove some
                    # TODO: take in consideration the initial balance and if possible augment fake to balance the session
                    if which_ones == "real":
                        # it means we don't have enough full 1 transient and need to augment self.n_full_1_transient
                        # first we need to determine the difference
                        full_1_to_add = (self.n_full_2p_transient[which_ones] * ratio) - self.n_full_1_transient[
                            which_ones]
                        if self.debug_mode:
                            print(f"n_full_2p_transient[which_ones] {self.n_full_2p_transient[which_ones]}, "
                                  f" ratio {ratio}, n_full_1_transient[which_ones] "
                                  f"{self.n_full_1_transient[which_ones]}")
                            print(f"diff {full_1_to_add}")
                        augmentation_added = 0
                        movie_index = 0
                        while augmentation_added < full_1_to_add:
                            self.full_1_transient[which_ones][movie_index].add_n_augmentation(n_augmentation=1)
                            movie_index = (movie_index + 1) % len(self.full_1_transient[which_ones])
                            augmentation_added += 1
                    else:
                        # we have too much full 2p transient, we want to remove some (for fakes ones)
                        # first we need to determine the difference
                        n_full_2p_to_remove = self.n_full_2p_transient[which_ones] - \
                                              (self.n_full_1_transient[which_ones] / ratio)
                        # we want to change self.data_list
                        n_full_2p_removed = 0
                        new_data_list = []
                        for movie_data in self.data_list:
                            movie_info = movie_data.movie_info
                            if movie_data.to_keep_absolutely:
                                print(" too much full 2p transient: movie_data.to_keep_absolutely")
                                new_data_list.append(movie_data)
                                continue
                            if "n_transient" in movie_info:
                                new_data_list.append(movie_data)
                                continue
                            if "n_cropped_transient" in movie_info:
                                new_data_list.append(movie_data)
                                continue
                            if "n_fake_transient" in movie_info:
                                n_fake_transient = movie_info["n_fake_transient"]
                                if n_fake_transient == 1:
                                    new_data_list.append(movie_data)
                                    continue
                                elif n_full_2p_removed < n_full_2p_to_remove:
                                    n_full_2p_removed += (1 + movie_data.n_augmentations_to_perform)
                                    continue
                            new_data_list.append(movie_data)
                        self.data_list = new_data_list
                else:
                    if which_ones == "real":
                        # it means we have too many full_1_transient, need to augment self.n_full_2p_transient
                        # first we want to respect the non_crop_ratio_balance
                        full_2p_to_add = (self.n_full_1_transient[which_ones] / ratio) - self.n_full_2p_transient[
                            which_ones]
                        augmentation_added = 0
                        movie_index = 0
                        missed_augm = 0
                        while augmentation_added < full_2p_to_add:
                            movie_patch = self.full_2p_transient[which_ones][movie_index]
                            movie_patch.add_n_augmentation(n_augmentation=1)
                            movie_index = (movie_index + 1) % len(self.full_2p_transient[which_ones])
                            augmentation_added += 1
                    else:
                        # we have too much full 1 transient, we want to remove some (for fakes ones)
                        # first we need to determine the difference
                        n_full_1_to_remove = self.n_full_1_transient[which_ones] - \
                                             (self.n_full_2p_transient[which_ones] * ratio)
                        # we want to change self.data_list
                        n_full_1_removed = 0
                        new_data_list = []
                        for movie_data in self.data_list:
                            movie_info = movie_data.movie_info
                            if "n_transient" in movie_info:
                                new_data_list.append(movie_data)
                                continue
                            if "n_cropped_transient" in movie_info:
                                new_data_list.append(movie_data)
                                continue
                            if "n_fake_transient" in movie_info:
                                n_fake_transient = movie_info["n_fake_transient"]
                                if n_fake_transient > 1:
                                    new_data_list.append(movie_data)
                                    continue
                                elif n_full_1_removed < n_full_1_to_remove:
                                    n_full_1_removed += (1 + movie_data.n_augmentations_to_perform)
                                    continue
                            new_data_list.append(movie_data)
                        self.data_list = new_data_list

        if self.debug_mode:
            print("")
            print(f"$$ After balancing non cropped {which_ones} transients $$")
            print("")
        # updating stat
        self.compute_slices()

        if self.n_cropped_transient_total[which_ones] == 0:
            return

        if crop_non_crop_ratio_balance[0] == 0:
            # we want to delete all the non cropped transients
            new_data_list = []
            for movie_data in self.data_list:
                movie_info = movie_data.movie_info
                if movie_data.to_keep_absolutely:
                    print("crop_non_crop_ratio_balance[0] == 0: movie_data.to_keep_absolutely")
                    new_data_list.append(movie_data)
                    continue
                if (which_ones == "fake") and ("n_fake_transient" in movie_info) \
                        and ("n_transient" not in movie_info) and ("n_cropped_transient" not in movie_info):
                    continue
                if (which_ones == "real") and ("n_transient" in movie_info):
                    continue
                new_data_list.append(movie_data)
            self.data_list = new_data_list

            # updating stat
            self.compute_slices()

        if crop_non_crop_ratio_balance[1] == 0:
            # we want to delete all the  cropped transients
            new_data_list = []
            for movie_data in self.data_list:
                movie_info = movie_data.movie_info
                if movie_data.to_keep_absolutely:
                    print("crop_non_crop_ratio_balance[1] == 0 == 0: movie_data.to_keep_absolutely")
                    new_data_list.append(movie_data)
                    continue
                if (which_ones == "fake") and ("n_cropped_fake_transient" in movie_info) \
                        and ("n_transient" not in movie_info) and ("n_cropped_transient" not in movie_info):
                    continue
                if (which_ones == "real") and ("n_cropped_transient" in movie_info) and \
                        ("n_transient" not in movie_info):
                    continue
                new_data_list.append(movie_data)
            self.data_list = new_data_list

            # updating stat
            self.compute_slices()

        if (crop_non_crop_ratio_balance[0] > 0) and (crop_non_crop_ratio_balance[1] > 0):
            # now we want to balance cropped and non cropped (full)
            ratio = crop_non_crop_ratio_balance[0] / crop_non_crop_ratio_balance[1]
            if np.abs((self.n_full_transient_total[which_ones] / self.n_cropped_transient_total[which_ones]) - ratio) > \
                    tolerance:
                if (self.n_cropped_transient_total[which_ones] * ratio) > self.n_full_transient_total[which_ones]:
                    if which_ones == "real":
                        # it means we have to many cropped one and we need to augment n_full_transient_total
                        # first we need to determine the difference
                        full_to_add = (self.n_cropped_transient_total[which_ones] * ratio) - \
                                      self.n_full_transient_total[which_ones]
                        # we compute how many full movie we have (self.n_full_transient_total[which_ones] contains the number
                        # of movies included all the transformation that will be perform) we want the number of unique original
                        # movies before transformations
                        n_full = len(self.full_1_transient[which_ones]) + len(self.full_2p_transient[which_ones])
                        # we want to add the same numbers such that we keep the ratio among the full_fake_transients
                        n_movie_patch_options = [n_full * x for x in
                                                 np.arange(0, (self.n_max_transformations -
                                                               self.min_augmentation_for_transient[which_ones]) + 3)]
                        n_movie_patch_options = np.array(n_movie_patch_options)
                        idx = (np.abs(n_movie_patch_options - full_to_add)).argmin()
                        # print(f"//// {which_ones}: self.n_cropped_transient_total[which_ones] "
                        #       f"{self.n_cropped_transient_total[which_ones]}, "
                        #       f" ratio {ratio}, self.n_full_transient_total[which_ones] "
                        #       f"{self.n_full_transient_total[which_ones]}")
                        # print(f"////  full_to_add {full_to_add}")
                        # print(f"////  n_movie_patch_options {n_movie_patch_options}")
                        # print(f"////  idx {idx}")
                        # print(f"////  n_movie_patch_options[idx] {n_movie_patch_options[idx]}")
                        if idx > 0:
                            for movie_patch_data in self.full_1_transient[which_ones]:
                                movie_patch_data.add_n_augmentation(n_augmentation=idx)
                            for movie_patch_data in self.full_2p_transient[which_ones]:
                                movie_patch_data.add_n_augmentation(n_augmentation=idx)
                    else:
                        # it means we have to many cropped one and we need to remove some
                        # first we need to determine the difference
                        n_cropped_to_remove = self.n_cropped_transient_total[which_ones] - \
                                              (self.n_full_transient_total[which_ones] / ratio)
                        # we want to change self.data_list
                        n_cropped_removed = 0
                        new_data_list = []
                        for movie_data in self.data_list:
                            if movie_data.to_keep_absolutely:
                                print("to many cropped one: movie_data.to_keep_absolutely")
                                new_data_list.append(movie_data)
                                continue
                            movie_info = movie_data.movie_info
                            if "n_transient" in movie_info:
                                new_data_list.append(movie_data)
                                continue
                            if "n_cropped_transient" in movie_info:
                                new_data_list.append(movie_data)
                                continue
                            if "n_fake_transient" in movie_info:
                                new_data_list.append(movie_data)
                                continue
                            if "n_cropped_fake_transient" in movie_info:
                                if n_cropped_removed < n_cropped_to_remove:
                                    n_cropped_removed += (1 + movie_data.n_augmentations_to_perform)
                                    continue
                            new_data_list.append(movie_data)
                        self.data_list = new_data_list
                else:
                    # for full transient, we don't want to remove some even for fake, otherwise it would unbalance
                    # the full1 and full2
                    # if means we have too many full transient, we need to augment n_cropped_transient_total
                    # first we want to respect the non_crop_ratio_balance
                    n_cropped_to_add = (self.n_full_transient_total[which_ones] / ratio) - \
                                       self.n_cropped_transient_total[which_ones]
                    augmentation_added = 0
                    movie_index = 0
                    print(f"++++++ n_cropped_to_add {n_cropped_to_add}")
                    print(f"n_full_transient_total {which_ones} {self.n_full_transient_total[which_ones]}, "
                          f"n_cropped_transient_total {which_ones}  {self.n_cropped_transient_total[which_ones]}")
                    while augmentation_added < n_cropped_to_add:
                        self.cropped_transient_movies[which_ones][movie_index].add_n_augmentation(n_augmentation=1)
                        movie_index = (movie_index + 1) % len(self.cropped_transient_movies[which_ones])
                        augmentation_added += 1

        if self.debug_mode:
            print("")
            print(f"$$ After balancing cropped and non cropped {which_ones} transients $$")
            print("")
        self.compute_slices()


class StratificationDataProcessor:

    def __init__(self, data_list, description, n_max_transformations, main_ratio_balance=(0.6, 0.25, 0.15),
                 crop_non_crop_ratio_balance=(0.9, 0.1), non_crop_ratio_balance=(0.6, 0.4),
                 debug_mode=False):
        self.data_list = data_list
        self.n_transformations_for_session = n_max_transformations // 3
        self.n_max_transformations = n_max_transformations - self.n_transformations_for_session

        # for each session, we make a camembert of the movie_patches of this session
        # and balance the patches in the session
        # then we will balance the session among themselves by adding the number of augmentation
        # for all the patches of a given session, thus keeping the balance in the data
        self.movie_patches_data_by_session = dict()
        for movie_data in self.data_list:
            if movie_data.session_id not in self.movie_patches_data_by_session:
                self.movie_patches_data_by_session[movie_data.session_id] = []
            self.movie_patches_data_by_session[movie_data.session_id].append(movie_data)

        # just to have the stat
        StratificationCamembert(data_list=self.data_list,
                                description=description,
                                n_max_transformations=self.n_max_transformations,
                                debug_mode=True)

        self.camembert_by_session = dict()
        for session, session_movie_data in self.movie_patches_data_by_session.items():
            self.camembert_by_session[session] = StratificationCamembert(data_list=session_movie_data,
                                                                         description=session,
                                                                         n_max_transformations=self.n_max_transformations,
                                                                         debug_mode=debug_mode)
        # #### First we want to balance each session in itself
        # a first step, would be to first balance the fake transients
        # then see how many transformations are needed to be added to real transients to get the right proportion
        # then look at neuropil and from neuropil decide if we want to delete some or do data augmentation in some of

        # for camembert in self.camembert_by_session.values():
        #     camembert.balance_all(main_ratio_balance=main_ratio_balance)

        # balancing the real transients, fake ones and neuropils among themselves
        for camembert in self.camembert_by_session.values():
            camembert.balance_all(main_ratio_balance=main_ratio_balance, first_round=True)

        # them
        for camembert in self.camembert_by_session.values():
            camembert.balance_transients(which_ones="fake", crop_non_crop_ratio_balance=crop_non_crop_ratio_balance,
                                         non_crop_ratio_balance=non_crop_ratio_balance)

        # balancing the real transients
        for camembert in self.camembert_by_session.values():
            camembert.balance_transients(which_ones="real", crop_non_crop_ratio_balance=crop_non_crop_ratio_balance,
                                         non_crop_ratio_balance=non_crop_ratio_balance)

        # balancing the real transients, fake ones and neuropils among themselves
        for camembert in self.camembert_by_session.values():
            camembert.balance_all(main_ratio_balance=main_ratio_balance, first_round=False)

        # ####  then balance session between themselves
        # taking the sessions with the most movies and using it as exemples
        balancing_sessions = False
        if balancing_sessions:
            max_movie_patch = 0
            for camembert in self.camembert_by_session.values():
                max_movie_patch = max(max_movie_patch, camembert.n_movie_patch)

            for camembert in self.camembert_by_session.values():
                if camembert.n_movie_patch == max_movie_patch:
                    continue
                # we need to find the multiplicator between 1 and (self.n_transformations_for_session +1)
                # that would give the closest count from the max
                n_movie_patch = camembert.n_movie_patch
                # list of potential movie patches in this session depending on the augmentation factor
                # from 1 (no transformation added) to (self.n_transformations_for_session + 1)
                n_movie_patch_options = [n_movie_patch * x for x in
                                         np.arange(1, (self.n_transformations_for_session + 2))]
                n_movie_patch_options = np.array(n_movie_patch_options)
                idx = (np.abs(n_movie_patch_options - max_movie_patch)).argmin()
                if idx > 0:
                    camembert.add_augmentation_to_all_patches(n_augmentation=idx)

        # updating the data list, in case some movie patches would have been deleted
        new_data_list = []
        for camembert in self.camembert_by_session.values():
            new_data_list.extend(camembert.data_list)
        self.data_list = new_data_list

        # just to have the stat
        if debug_mode:
            print(f"////////// AFTER balancing sessions //////////////")
        balanced_camembert = StratificationCamembert(data_list=self.data_list,
                                                     description=description + "_balanced",
                                                     n_max_transformations=self.n_max_transformations,
                                                     debug_mode=True)
        # setting the weight based on amplitudes and lengths of the transients
        # also adding weight to fake transients, and multiple real ones
        balanced_camembert.set_weights()

    def get_new_data_list(self):
        return self.data_list


class StratificationCellTypeDataProcessor:
    """
    Class used to stratified data for cell type
    So far we make it simple, the postulate being that the data has already been stratify by the user (given the same
    amount of pramidal and interneuron cells for exemple). So for now we just used it to do data augmentation on each
    movie patch and create a new dataset thus
    """
    def __init__(self, data_list, description, n_max_transformations, debug_mode=False):
        self.data_list = data_list
        # self.n_transformations_for_session = n_max_transformations // 3
        self.n_max_transformations = n_max_transformations


        # for each session, we make a camembert of the movie_patches of this session
        # and balance the patches in the session
        # then we will balance the session among themselves by adding the number of augmentation
        # for all the patches of a given session, thus keeping the balance in the data
        self.movie_patches_data_by_session = dict()
        for movie_data in self.data_list:
            if movie_data.session_id not in self.movie_patches_data_by_session:
                self.movie_patches_data_by_session[movie_data.session_id] = []
            self.movie_patches_data_by_session[movie_data.session_id].append(movie_data)

        # just to have the stat
        StratificationCellTypeCamembert(data_list=self.data_list,
                                        description=description,
                                        n_max_transformations=self.n_max_transformations,
                                        debug_mode=True)

        self.camembert_by_session = dict()
        for session, session_movie_data in self.movie_patches_data_by_session.items():
            self.camembert_by_session[session] = StratificationCellTypeCamembert(data_list=session_movie_data,
                                                                                 description=session,
                                                                                 n_max_transformations=self.n_max_transformations,
                                                                                 debug_mode=debug_mode)

        # balancing the real transients, fake ones and neuropils among themselves
        for camembert in self.camembert_by_session.values():
            camembert.augment_them_all()

        # updating the data list, in case some movie patches would have been deleted
        new_data_list = []
        for camembert in self.camembert_by_session.values():
            new_data_list.extend(camembert.data_list)
        self.data_list = new_data_list

        # just to have the stat
        print(f"////////// AFTER balancing sessions //////////////")
        balanced_camembert = StratificationCellTypeCamembert(data_list=self.data_list,
                                                             description=description + "_balanced",
                                                             n_max_transformations=self.n_max_transformations,
                                                             debug_mode=True)

    def get_new_data_list(self):
        return self.data_list