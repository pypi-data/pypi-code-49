import os
import logging
import numpy as np

from amap.register.brain_processor import BrainProcessor


def save_downsampled_image(
    image,
    name,
    output_folder,
    atlas,
    x_pixel_um=0.02,
    y_pixel_um=0.02,
    z_pixel_um=0.05,
    orientation="coronal",
    n_free_cpus=2,
    sort_input_file=False,
    load_parallel=True,
):
    """

    :param image: Image to be downsampled.
    :param str name: Name of the image (for the filename and logging)
    :param output_folder: Where the image is to be saved
    :param atlas: atlas config
    :param x_pixel_um: pixel spacing in the first dimension
    :param y_pixel_um: pixel spacing in the second dimension
    :param z_pixel_um: pixel spacing in the second dimension
    :param orientation: anatomical orientation of the image
    :param n_free_cpus: how many cpus to leave free when loading data
    :param sort_input_file: Should the data be naturally sorted
    (e.g. file paths)
    :param load_parallel: If possible, load the data in parallel
    """

    logging.info(f"Downsampling image: {name}")
    logging.info("Loading data")
    brain = BrainProcessor(
        atlas,
        image,
        output_folder,
        x_pixel_um,
        y_pixel_um,
        z_pixel_um,
        original_orientation=orientation,
        load_parallel=load_parallel,
        sort_input_file=sort_input_file,
        load_atlas=False,
        n_free_cpus=n_free_cpus,
    )

    downsampled_brain_path = os.path.join(
        output_folder, f"downsampled_{name}.nii"
    )

    brain.target_brain = brain.target_brain.astype(np.uint16, copy=False)
    logging.info("Saving downsampled image")
    brain.save(downsampled_brain_path)
    del brain
