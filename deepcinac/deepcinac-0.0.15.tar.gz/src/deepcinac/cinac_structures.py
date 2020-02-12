# import tensorflow as tf

# TF_VERSION = tf.__version__
# print(f"TF_VERSION {TF_VERSION}")
#
# # depending on the TF version installed
# if TF_VERSION[0] == "2":
#     from tensorflow.keras.models import model_from_json
# else:
#     from keras.models import model_from_json

import numpy as np
from deepcinac.utils.utils import smooth_convolve, create_one_npy_file_by_frame, load_movie


from deepcinac.utils.cells_map_utils import CellsCoord, create_cells_coord_from_suite_2p
import PIL
import os
from abc import ABC, abstractmethod
from ScanImageTiffReader import ScanImageTiffReader
from shapely.geometry import MultiPoint, LineString


class CinacMovie(ABC):
    def __init__(self):
        self.dimensions = None
        self.n_frames = 0

    @abstractmethod
    def get_frames_section(self, frames, minx, maxx, miny, maxy):
        pass

    def get_dimensions(self):
        """
        Get x and y dimensions of the movie
        Returns: a 1d array of integers

        """
        return self.dimensions

    def get_n_frames(self):
        """
        The number of frames in the movie
        Returns: integer

        """
        return self.n_frames

    @abstractmethod
    def get_full_movie(self, normalized):
        """
        Full movie, if available a 3d array n_frames x len_y x len_x
        Args:
            normalized: bool, if True return normalized movie, False original movie if available

        Returns:

        """
        pass


class CinacDataMovie(CinacMovie):
    """
    Take the movie as a 2d array directly
    """

    def __init__(self, movie, already_normalized=False):
        super().__init__()

        self.movie = None
        if already_normalized:
            self.movie_normalized = movie
        else:
            self.movie = movie
            self.movie_normalized = movie - np.mean(movie)
            self.movie_normalized = self.movie_normalized / np.std(movie)
        self.n_frames = len(self.movie_normalized)
        self.dimensions = self.movie_normalized.shape[1:]

    def get_frames_section(self, frames, minx, maxx, miny, maxy):
        return self.movie_normalized[frames, miny:maxy + 1, minx:maxx + 1]

    def get_full_movie(self, normalized):
        """
        Full movie, if available a 3d array n_frames x len_y x len_x
        Args:
            normalized: bool, if True return normalized movie, False original movie if available

        Returns:

        """
        if normalized or (self.movie is None):
            return self.movie_normalized
        return self.movie


class CinacTiffMovie(CinacMovie):
    def __init__(self, tiff_file_name=None, tiff_movie=None):
        super().__init__()
        if tiff_movie is None:
            if tiff_file_name is None:
                raise Exception("tiff_file_name and tiff_movie can't both be set to None.")
            self.tiff_movie_normalized = load_movie(file_name=tiff_file_name,
                                                    with_normalization=True, verbose=True)
            # TODO: change code, tiff_movie is not used
        else:
            self.tiff_movie = tiff_movie
            self.tiff_movie_normalized = tiff_movie - np.mean(tiff_movie)
            self.tiff_movie_normalized = self.tiff_movie_normalized / np.std(tiff_movie)

        self.n_frames = len(self.tiff_movie_normalized)
        self.dimensions = self.tiff_movie_normalized.shape[1:]

    def get_frames_section(self, frames, minx, maxx, miny, maxy):
        return self.tiff_movie_normalized[frames, miny:maxy + 1, minx:maxx + 1]

    def get_full_movie(self, normalized):
        """
        Full movie, if available a 3d array n_frames x len_y x len_x
        Args:
            normalized: bool, if True return normalized movie, False original movie if available

        Returns:

        """
        if normalized or (self.tiff_movie is None):
            return self.tiff_movie_normalized
        return self.tiff_movie


class CinacFileReaderMovie(CinacMovie):
    def __init__(self, cinac_file_reader, segment):
        """

        Args:
            cinac_file_reader: CinacFileReader instance
            segment: tuple of 3 int, cell, first_frame and last_frame to identify the segment
        """
        super().__init__()
        self.cinac_file_reader = cinac_file_reader
        self.segment = segment

        self.n_frames = segment[2] - segment[1] + 1
        self.dimensions = self.cinac_file_reader.get_segment_ci_movie_frames(segment=self.segment,
                                                                             frames=np.array([0])).shape[1:]

    def get_frames_section(self, frames, minx, maxx, miny, maxy):
        frames_section = self.cinac_file_reader.get_segment_ci_movie_frames(segment=self.segment, frames=frames)
        # print(f"CinacFileReaderMovie frames_section.shape {frames_section.shape}")
        coords = [minx, maxx, miny, maxy]
        # print(f"CinacFileReaderMovie coords {coords}")
        frames_section = frames_section[:, miny:maxy + 1, minx:maxx + 1]
        # print(f"CinacFileReaderMovie frames_section.shape bis {frames_section.shape}")
        return frames_section

    def get_full_movie(self, normalized):
        """
        Full movie, if available a 3d array n_frames x len_y x len_x
        Args:
            normalized: bool, if True return normalized movie, False original movie if available

        Returns:

        """
        print("### CinacFileReaderMovie get_full_movie()")
        # not keeping the full movie in memory so that the garbage collector could free the memory
        # if the movie is not used anymore elsewhere, but means the file will be read everytime the function
        # get_full_movie() will be called
        ci_movie = self.cinac_file_reader.get_segment_ci_movie(segment=self.segment)
        if normalized:
            return (ci_movie - np.mean(ci_movie)) / np.std(ci_movie)
        return ci_movie

class CinacSplitedTiffMovie(CinacMovie):
    """
    Used if tiff movie has been splitted as as many tiff files as frames in the movie
    """

    def __init__(self, identifier, tiffs_dirname, already_normalized=False, tiff_file_name=None, tiff_movie=None):
        """

        Args:
            identifier: string
            tiffs_dirname: dirname of where to save the tiffs created
            tiff_file_name: string, if not None, will create a tiff by frame from this tiff movie if not already done.
            Will be saved in tiffs_dirname. If tiff_movie is not None, the tiff movie will be chosen.
            tiff_movie: numpy 3d array f not None, will create a tiff by frame from this tiff movie if not already done.
            Will be saved in tiffs_dirname.
            already_normalized: indicate if the movie if already normalized (valid if tiff_file_name or tiff_movie
            is not None. Otherwise, normalization will be done if a mean and std files are found in the tiffs directory
        """
        super().__init__()
        self.tiffs_dirname = tiffs_dirname
        self.identifier = identifier

        self.tiff_movie = tiff_movie
        self.movie_normalized = None

        # first if tiff_file_name or tiff_movie are not None, it means we should try to create the SplittedTiffVersion
        # if they doen't exist yet
        if tiff_file_name is not None or tiff_movie is not None:
            movies_to_split = dict()
            if tiff_movie is not None:
                movies_to_split[identifier] = tiff_movie
            else:
                movies_to_split[identifier] = tiff_file_name
            # won't do anything if the tiffs already have been created
            # used to be: create_one_tiff_file_by_frame
            create_one_npy_file_by_frame(movies_to_split=movies_to_split,
                                          results_path=tiffs_dirname,
                                          without_mean_std_files=already_normalized,
                                          verbose=2)

        self.tiff_movie_mean = None
        self.tiff_movie_std = None

        file_names = []

        # look for filenames in the fisrst directory, if we don't break, it will go through all directories
        for (dirpath, dirnames, local_filenames) in os.walk(os.path.join(self.tiffs_dirname, self.identifier)):
            file_names.extend(local_filenames)
            break

        # we loop in the directory filenames in order to set the mean and std of the movie and count how many frames
        # are in the movie (according they have all be saved correctly)
        # if mean and std are not present, it means the movie is already normalized
        self.n_frames = 0
        for file_name in file_names:
            if file_name.endswith("mean.npy"):
                mean_value = np.load(os.path.join(self.tiffs_dirname, self.identifier, file_name))
                self.tiff_movie_mean = mean_value
            elif file_name.endswith("std.npy"):
                std_value = np.load(os.path.join(self.tiffs_dirname, self.identifier, "std.npy"))
                self.tiff_movie_std = std_value
            # elif file_name.endswith("tiff") or file_name.endswith("tif"):
            elif file_name.endswith("npy"):
                self.n_frames += 1
                if self.dimensions is None:
                    im = np.load(os.path.join(self.tiffs_dirname, self.identifier, file_name))
                    # im = PIL.Image.open(os.path.join(self.tiffs_dirname, self.identifier, file_name))
                    # im = np.array(im)
                    self.dimensions = im.shape

    def get_frames_section(self, frames_indices, minx, maxx, miny, maxy):
        """
        get section of given frames from the calcium imaging movie
        Args:
            frames_indices: numpy array of integers, representing the frame's indices to select
            minx: integer, min x coordinate
            maxx: integer, max x coordinate
            miny: integer, min y coordinate
            maxy: integer, max y coordinate

        Returns:

        """

        frames_section = np.zeros((len(frames_indices), maxy - miny + 1, maxx - minx + 1))
        for frame_index, frame in enumerate(frames_indices):
            im = np.load(os.path.join(self.tiffs_dirname, self.identifier, f"{frame}.npy"))
            # try:
            #     im = ScanImageTiffReader(os.path.join(self.tiffs_dirname,
            #                                           self.identifier, f"{frame}.tiff")).data()
            # except Exception as e:
            #     im = PIL.Image.open(os.path.join(self.tiffs_dirname,
            #                                      self.identifier, f"{frame}.tiff"))
            #     im = np.array(im)
            frames_section[frame_index] = im[miny:maxy + 1, minx:maxx + 1]
        # normalizing using the mean and std from the whole movie
        if self.tiff_movie_mean is not None:
            frames_section = (frames_section - self.tiff_movie_mean) / self.tiff_movie_std
        # if None, then we suppose the movie is already normalized
        return frames_section

    def get_full_movie(self, normalized):
        """
        Full movie, if available a 3d array n_frames x len_y x len_x
        Args:
            normalized: bool, if True return normalized movie, False original movie if available

        Returns:

        """
        print("#### get_full_movie() in CinacSplitedTiffMovie")
        if self.tiff_movie is None:
            tiff_movie = np.zeros((self.n_frames, self.dimensions[0], self.dimensions[1]), dtype="uint16")
            for frame_index in np.arange(self.n_frames):
                try:
                    im = ScanImageTiffReader(os.path.join(self.tiffs_dirname,
                                                          self.identifier, f"{frame_index}.tiff")).data()
                except Exception as e:
                    im = PIL.Image.open(os.path.join(self.tiffs_dirname,
                                                     self.identifier, f"{frame_index}.tiff"))
                    im = np.array(im)
                tiff_movie[frame_index] = im

            self.tiff_movie = tiff_movie

        if normalized:
            if self.movie_normalized is None:
                if self.tiff_movie_mean is None:
                    self.movie_normalized = self.tiff_movie
                else:
                    self.movie_normalized = self.tiff_movie - self.tiff_movie_mean
                    self.movie_normalized = self.movie_normalized / self.tiff_movie_std
            return self.tiff_movie_normalized
        return self.tiff_movie


def get_cinac_movie_from_cinac_file_reader(cinac_file_reader):
    """

    Args:
        cinac_file_reader: CinacFileReader instance

    Returns:

    """
    ci_movie_file_name = cinac_file_reader.get_ci_movie_file_name()
    if ci_movie_file_name is None or (not os.path.exists(ci_movie_file_name)):
        raise Exception(f"ci_movie_file_name in cinac_file should be valid: {ci_movie_file_name}")

    ci_movie = load_movie(file_name=ci_movie_file_name, both_instances=False,
                          with_normalization=False, verbose=True)
    cinac_movie = CinacDataMovie(movie=ci_movie, already_normalized=False)
    return cinac_movie


def create_cinac_recording_from_cinac_file_segment(identifier, cinac_file_reader, segment):
    """

    Args:
        identifier: cinac_recording identifier
        cinac_file_reader: CinacFileReaderInstance
        cinac_movie: CinacMovie instance
        segment: tuple of 3 int (cell, first_frame, last_frame

    Returns:

    """
    # cinac_file_reader = CinacFileReader(file_name=cinac_file_name)
    # segments_list = cinac_file_reader.get_all_segments()
    cinac_movie = CinacFileReaderMovie(cinac_file_reader=cinac_file_reader,
                                       segment=segment)
    cinac_recording = CinacRecording(identifier)
    cinac_recording.set_movie(cinac_movie)
    # smooth_traces is already saved in z_score normalized format
    cinac_recording.smooth_traces = cinac_file_reader.get_segment_smooth_traces(segment=segment)
    cinac_recording.smooth_traces_z_score = cinac_recording.smooth_traces
    # ci_movie = cinac_movie.get_full_movie(normalized=True)
    coords_data = cinac_file_reader.get_segment_cells_contour(segment)
    coords_data = [np.vstack((coord_data[0], coord_data[1])) for coord_data in coords_data]
    # coord_obj = CellsCoord(coords=coords_data, pixel_masks=None, nb_lines=ci_movie.shape[1],
    #                        nb_col=ci_movie.shape[2],
    #                        from_matlab=False, invert_xy_coord=False)
    # cinac_recording.coord_obj = coord_obj
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

    cinac_recording.cell_type = cinac_file_reader.get_segment_cell_type(segment=segment)
    return cinac_recording

class CinacRecording:
    # TODO: add fields that will contains the ground truth

    def __init__(self, identifier):
        self.cinac_movie = None
        self.identifier = identifier
        self.coord_obj = None
        # string defining the cell type of the recording, if known means it is unknown
        self.cell_type = None
        self.raw_traces = None
        self.raw_traces_z_score = None
        self.smooth_traces = None
        self.smooth_traces_z_score = None

    def _build_traces(self):
        self.raw_traces = self.coord_obj.build_raw_traces_from_movie(movie=
                                                                     self.cinac_movie.get_full_movie(normalized=False))
        self.smooth_traces = np.copy(self.raw_traces)
        windows = ['hanning', 'hamming', 'bartlett', 'blackman']
        i_w = 1
        window_length = 7  # 11
        for i in np.arange(self.smooth_traces.shape[0]):
            smooth_signal = smooth_convolve(x=self.smooth_traces[i], window_len=window_length,
                                            window=windows[i_w])
            beg = (window_length - 1) // 2
            self.smooth_traces[i] = smooth_signal[beg:-beg]
        self.smooth_traces_z_score = np.zeros(self.smooth_traces.shape)
        self.raw_traces_z_score = np.zeros(self.raw_traces.shape)
        for i in np.arange(len(self.raw_traces)):
            # -2 so smooth smooth_traces will be displayed under the raw smooth_traces
            self.smooth_traces_z_score[i, :] = ((self.smooth_traces[i, :] - np.mean(self.smooth_traces[i, :])) / np.std(
                self.smooth_traces[i, :])) - 2
            self.raw_traces_z_score[i, :] = (self.raw_traces[i, :] - np.mean(self.raw_traces[i, :])) \
                                            / np.std(self.raw_traces[i, :])

    def get_raw_traces(self, normalized):
        """

        Args:
            normalized: if True, get the raw_traces normalized

        Returns:

        """
        if self.raw_traces is None:
            self._build_traces()

        if normalized:
            return self.raw_traces_z_score
        else:
            return self.raw_traces

    def get_smooth_traces(self, normalized):
        """

        Args:
            normalized: if True, get the raw_traces normalized

        Returns:

        """
        if self.smooth_traces is None:
            self._build_traces()

        if normalized:
            return self.smooth_traces_z_score
        else:
            return self.smooth_traces

    def set_movie(self, cinac_movie):
        """
        Set the instance of CinacMovie, that will be used to get the frames given to the network
        Args:
            cinac_movie:

        Returns:

        """
        self.cinac_movie = cinac_movie

    def set_rois_from_suite_2p(self, is_cell_file_name, stat_file_name):
        """

        Args:
            is_cell_file_name: path and file_name of the file iscell.npy produce by suite2p segmentation process
            stat_file_name: path and file_name of the file stat.npy produce by suite2p segmentation process

        Returns:

        """
        if self.cinac_movie is None:
            raise Exception(f"cinac_movie should be set using the method set_movie() before setting the Rois")
        pass

        self.coord_obj = create_cells_coord_from_suite_2p(is_cell_file_name=is_cell_file_name,
                                                          stat_file_name=stat_file_name,
                                                          movie_dimensions=self.cinac_movie.get_dimensions())

    def set_rois_2d_array(self, coord, from_matlab):
        """

        Args:
            coord: numpy array of 2d, first dimension of length 2 (x and y) and 2nd dimension of length the number of
            cells. Could also be a list of lists or tuples of 2 integers
            from_matlab: Indicate if the data has been computed by matlab, then 1 will be removed to the coordinates
            so it starts at zero.

        Returns:

        """
        if self.cinac_movie is None:
            raise Exception(f"cinac_movie should be set using the method set_movie() before setting the Rois")
        dimensions = self.cinac_movie.get_dimensions()
        self.coord_obj = CellsCoord(coords=coord, nb_lines=dimensions[0], nb_col=dimensions[1], from_matlab=from_matlab)

    def set_rois_from_nwb(self, nwb_data, name_module, name_segmentation, name_seg_plane):
        """

        Args:
            nwb_data: nwb object instance
            name_module: Name of the module to find segmentation. Will be used this way: nwb_data.modules[name_module]
                Ex: name_module = 'ophys'
            name_segmentation: Name of the segmentation in which find the plane segmentation.
                Used this way:get_plane_segmentation(name_segmentation)
                Ex: name_segmentation = 'segmentation_suite2p'
            name_seg_plane: Name of the segmentation plane in which to find the ROIs data
            Used this way: mod[name_segmentation]get_plane_segmentation(name_seq_plane)
                Ex: name_segmentation = 'my_plane_seg'

        Returns:

        """
        if self.cinac_movie is None:
            raise Exception(f"cinac_movie should be set using the method set_movie() before setting the Rois")
        mod = nwb_data.modules[name_module]
        plane_seg = mod[name_segmentation].get_plane_segmentation(name_seg_plane)

        if 'pixel_mask' not in plane_seg:
            raise Exception("'pixel_mask' has to exist in plane_segmentation in order to create ROIs")

        self.set_rois_using_pixel_mask(pixel_masks=plane_seg['pixel_mask'])

    def set_rois_using_pixel_mask(self, pixel_masks):
        """

        Args:
            pixel_masks: list of list of 2 integers representing for each cell all the pixels that belongs to the cell

        Returns:

        """
        if self.cinac_movie is None:
            raise Exception(f"cinac_movie should be set using the method set_movie() before setting the Rois")

        # TODO: use pixel_mask instead of using the coord of the contour of the cell
        #  means changing the way coord_cell works
        coord_list = []
        for cell in np.arange(len(pixel_masks)):
            pixels_coord = pixel_masks[cell]
            list_points_coord = [(pix[0], pix[1]) for pix in pixels_coord]
            convex_hull = MultiPoint(list_points_coord).convex_hull
            if isinstance(convex_hull, LineString):
                coord_shapely = MultiPoint(list_points_coord).convex_hull.coords
            else:
                coord_shapely = MultiPoint(list_points_coord).convex_hull.exterior.coords
            coord_list.append(np.array(coord_shapely).transpose())

        dimensions = self.cinac_movie.get_dimensions()
        self.coord_obj = CellsCoord(coords=coord_list, nb_lines=dimensions[0], nb_col=dimensions[1],
                                    from_matlab=False)

    def get_n_frames(self):
        """
        Return the number of frames in the movie
        Returns:

        """
        return self.cinac_movie.get_n_frames()

    def get_n_cells(self):
        return self.coord_obj.n_cells

    def get_source_profile_frames(self, frames_indices, coords):
        """
        Return frames section based on the indices of the frames and the coordinates of the corners of the section
        Args:
            frames_indices: array of integers
            coords: tuple of 4 integers: (minx, maxx, miny, maxy)

        Returns: A numpy array of dimensions len(frames_indices) * (maxy - miny + 1) * (maxx - minx + 1)

        """

        frames_section = self.cinac_movie.get_frames_section(frames_indices, *coords)

        return frames_section










