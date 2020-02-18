"""
brain_processor
===============

A module to prepare brains for registration
"""

import logging
import numpy as np

from tqdm import trange
from brainio import brainio
from imlib.image.scale import scale_and_convert_to_16_bits

from amap.tools import image

transpositions = {
    "horizontal": (1, 0, 2),
    "coronal": (1, 2, 0),
    "sagittal": (2, 1, 0),
}


class BrainProcessor(object):
    """
    A class to do some basic processing to the brains (3D image scans)
    including:
    - Changing the orientation
    - filtering using despeckle and pseudo flatfield
    """

    def __init__(
        self,
        atlas,
        target_brain_path,
        output_folder,
        x_pix_um,
        y_pix_um,
        z_pix_um,
        original_orientation="coronal",
        load_parallel=False,
        sort_input_file=False,
        load_atlas=True,
        n_free_cpus=2,
        scaling_rounding_decimals=5,
    ):
        """
        :param str target_brain_path: The path to the brain to be processed
            (image file, paths file or folder)
        :param str output_folder: The folder where to store the results
        :param float x_pix_um: The pixel spacing in the x dimension. It is
            used to scale the brain to the atlas.
        :param float y_pix_um: The pixel spacing in the x dimension. It is
            used to scale the brain to the atlas.
        :param float z_pix_um: The pixel spacing in the x dimension. It is
            used to scale the brain to the atlas.
        :param str original_orientation:
        :param bool load_parallel: Load planes in parallel using
            multiprocessing for faster data loading
        :param bool sort_input_file: If set to true and the input is a
            filepaths file, it will be naturally sorted
        """
        self.target_brain_path = target_brain_path

        self.atlas = atlas
        atlas_pixel_sizes = self.atlas.pix_sizes

        x_scaling = round(
            x_pix_um / atlas_pixel_sizes["x"], scaling_rounding_decimals
        )
        y_scaling = round(
            y_pix_um / atlas_pixel_sizes["y"], scaling_rounding_decimals
        )
        z_scaling = round(
            z_pix_um / atlas_pixel_sizes["z"], scaling_rounding_decimals
        )

        self.original_orientation = original_orientation

        logging.info("Loading raw image data")
        self.target_brain = brainio.load_any(
            self.target_brain_path,
            x_scaling,
            y_scaling,
            z_scaling,
            load_parallel=load_parallel,
            sort_input_file=sort_input_file,
            n_free_cpus=n_free_cpus,
        )
        self.swap_numpy_to_image_axis()
        self.output_folder = output_folder

        if load_atlas:
            self.atlas.load_all()

    def swap_numpy_to_image_axis(self):
        self.target_brain = np.swapaxes(self.target_brain, 0, 1)

    def flip(self, axes):
        """
        Flips the brain along the specified axes.

        :param tuple axes: a tuple of 3 booleans indicating which axes to
            flip or not
        """
        for axis_idx, flip_axis in enumerate(axes):
            if flip_axis:
                self.target_brain = np.flip(self.target_brain, axis_idx)

    def flip_atlas(self, axes):
        self.atlas.flip(axes)

    def swap_atlas_orientation_to_self(self):
        self.atlas.reorientate_to_sample(self.original_orientation)

    def filter(self):
        """
        Applies a set of filters to the brain to avoid overfitting details in
        the image during registration.
        """

        self.target_brain = BrainProcessor.filter_for_registration(
            self.target_brain
        )

    @staticmethod
    def filter_for_registration(brain):
        """
        A static method to filter a 3D image to allow registration
        (avoids overfitting details in the image) (algorithm from Alex Brown).
        The filter is composed of a despeckle filter using opening and a
        pseudo flatfield filter

        :return: The filtered brain
        :rtype: np.array
        """
        brain = brain.astype(np.float64, copy=False)
        # OPTIMISE: could multiprocess but not slow
        for i in trange(brain.shape[-1], desc="filtering", unit="plane"):
            # OPTIMISE: see if in place better
            brain[..., i] = filter_plane_for_registration(brain[..., i])
        brain = scale_and_convert_to_16_bits(brain)
        return brain

    def save(self, dest_path):
        """
        Save self.target_brain to dest_path as a nifty image.
        The scale (zooms of the output nifty image) is copied from the atlas
        brain.

        :param str dest_path: Where to save the image on the filesystem
        """
        atlas_pix_sizes = self.atlas.pix_sizes
        transformation_matrix = (
            self.atlas.make_atlas_scale_transformation_matrix()
        )
        brainio.to_nii(
            self.target_brain,
            dest_path,
            scale=(
                atlas_pix_sizes["x"] / 1000,
                atlas_pix_sizes["y"] / 1000,
                atlas_pix_sizes["z"] / 1000,
            ),
            affine_transform=transformation_matrix,
        )


def filter_plane_for_registration(img_plane):
    """
    Apply a set of filter to the plane (typically to avoid overfitting details
    in the image during registration)
    The filter is composed of a despeckle filter using opening and a pseudo
    flatfield filter

    :param np.array img_plane: A 2D array to filter
    :return: The filtered image
    :rtype: np.array
    """
    img_plane = image.despeckle_by_opening(img_plane)
    img_plane = image.pseudo_flatfield(img_plane)
    return img_plane
