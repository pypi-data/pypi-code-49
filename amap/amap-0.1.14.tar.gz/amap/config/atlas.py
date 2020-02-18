import os

import numpy as np
import nibabel as nb
from brainio import brainio

from imlib.general.config import get_config_obj

transpositions = {
    "horizontal": (1, 0, 2),
    "coronal": (2, 0, 1),
    "sagittal": (2, 1, 0),
}


class AtlasError(Exception):
    pass


class Atlas(object):
    """
    A class to handle all the atlas data (including the
    """

    def __init__(self, config_path, dest_folder=""):
        config_obj = get_config_obj(config_path)
        self.atlas_conf = config_obj["atlas"]

        self.dest_folder = dest_folder

        self._pix_sizes = None  # cached to avoid reloading atlas
        self._data = None
        self._brain_data = None
        self._hemispheres_data = None

        self.original_orientation = self.atlas_conf["orientation"]
        if self.original_orientation != "horizontal":
            raise NotImplementedError(
                "Unknown orientation {}. Only horizontal supported so far".format(
                    self.original_orientation
                )
            )

    @property
    def pix_sizes(self):
        """
        Get the dictionary of x, y, z from the after loading it
        or if the atlas size is default, use the values from the config file

        :return: The dictionary of x, y, z pixel sizes
        """
        if self._pix_sizes is None:
            pixel_sizes = self.get_data().header.get_zooms()
            if pixel_sizes != (0, 0, 0):
                self._pix_sizes = {
                    axis: round(size * 1000, 3)  # convert to um
                    for axis, size in zip(("x", "y", "z"), pixel_sizes)
                }
            else:
                self._pix_sizes = self.get_pixel_sizes_from_config()
        return self._pix_sizes

    def get_path(self):
        """
        Get the path to the reference atlas

        :return: The atlas path
        :rtype: str
        """
        return self.get_atlas_element_path("atlas_name")

    def get_brain_path(self):
        return self.get_atlas_element_path("brain_name")

    def get_hemispheres_path(self):
        return self.get_atlas_element_path("hemispheres_name")

    def get_structures_path(self):
        return self.get_atlas_element_path("structures_name")

    def get_left_hemisphere_value(self):
        return int(self.atlas_conf["left_hemisphere_value"])

    def get_right_hemisphere_value(self):
        return int(self.atlas_conf["right_hemisphere_value"])

    def get_data(self):
        """
        Load the atlas and return it

        :return: The atlas (nifty image)
        """
        atlas_path = self.get_path()
        if self._data is None:
            self._data = brainio.load_nii(atlas_path)
        return self._data

    def load_all(self):
        if self._data is None:
            self._data = brainio.load_nii(self.get_path())
        if self._brain_data is None:
            self._brain_data = brainio.load_nii(self.get_brain_path())
        if self._hemispheres_data is None:
            self._hemispheres_data = brainio.load_nii(
                self.get_hemispheres_path()
            )

    def save_all(self):
        brainio.to_nii(self._data, self.get_dest_path("atlas_name"))
        brainio.to_nii(self._brain_data, self.get_dest_path("brain_name"))
        brainio.to_nii(
            self._hemispheres_data, self.get_dest_path("hemispheres_name")
        )

    # FIXME: should be just changing the header
    def _flip(self, nii_img, axis_idx):
        return nb.Nifti1Image(
            np.flip(nii_img.get_data(), axis_idx),
            nii_img.affine,
            nii_img.header,
        )

    def _flip_all(self, axis_idx):
        self._data = self._flip(self._data, axis_idx)
        self._brain_data = self._flip(self._brain_data, axis_idx)
        self._hemispheres_data = self._flip(self._hemispheres_data, axis_idx)

    def flip(self, axes):
        for axis_idx, flip_axis in enumerate(axes):
            if flip_axis:
                self._flip_all(axis_idx)

    def _transpose(self, nii_img, transposition):
        # FIXME: should be just changing the header
        data = np.transpose(nii_img.get_data(), transposition)
        data = np.swapaxes(data, 0, 1)
        return nb.Nifti1Image(data, nii_img.affine, nii_img.header)

    def _transpose_all(self, transposition):
        self._data = self._transpose(self._data, transposition)
        self._brain_data = self._transpose(self._brain_data, transposition)
        self._hemispheres_data = self._transpose(
            self._hemispheres_data, transposition
        )

    def reorientate_to_sample(self, sample_orientation):
        self._transpose_all(transpositions[sample_orientation])

    def get_dest_path(self, atlas_element_name):
        if not self.dest_folder:
            raise AtlasError(
                "Could not get destination path. "
                "Missing destination folder information"
            )
        return os.path.join(
            self.dest_folder, self.atlas_conf[atlas_element_name]
        )

    def make_atlas_scale_transformation_matrix(self):
        scale = self.pix_sizes
        transformation_matrix = np.eye(4)
        for i, axis in enumerate(("x", "y", "z")):
            transformation_matrix[i, i] = scale[axis] / 1000
        return transformation_matrix

    def get_pixel_sizes_from_config(self):
        """
        Get the dictionary of atlas pixel sizes from the config file.
        The dictionary is structured like this:
        {'x': x_pixel_size_in_um,
         'y': y_pixel_size_in_um,
         'z': z_pixel_size_in_um
        }

        :return: the pixel size dictionary
        :rtype: dict
        """
        return self.atlas_conf["pixel_size"]

    def get_atlas_element_path(self, config_entry_name):
        """
        Get the path to an 'element' of the atlas (i.e. the average brain,
        the atlas, or the hemispheres atlas)

        :param str config_entry_name: The name of the item to retrieve
        :return: The path to that atlas element on the filesystem
        :rtype: str
        """
        atlas_folder_name = os.path.expanduser(self.atlas_conf["base_folder"])
        atlas_element_filename = self.atlas_conf[config_entry_name]
        return os.path.abspath(
            os.path.normpath(
                os.path.join(atlas_folder_name, atlas_element_filename)
            )
        )
