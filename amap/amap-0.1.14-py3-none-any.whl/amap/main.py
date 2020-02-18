import logging
import numpy as np

from pathlib import Path
from imlib.general.system import get_num_processes, delete_temp

from amap.register.brain_processor import BrainProcessor
from amap.register.brain_registration import BrainRegistration
from amap.register.volume import calculate_volumes
from amap.config.atlas import Atlas
from amap.vis.boundaries import main as calc_boundaries
from amap.register.registration_params import RegistrationParams
from amap.register.tools import save_downsampled_image
from amap.utils.paths import Paths
from amap.utils.run import Run

flips = {
    "horizontal": (True, True, False),
    "coronal": (True, True, False),
    "sagittal": (False, True, False),
}


def check_downsampled(registration_output_folder, name):
    return Path(registration_output_folder, f"downsampled_{name}.nii").exists()


def main(
    registration_config,
    target_brain_path,
    registration_output_folder,
    x_pixel_um=0.02,
    y_pixel_um=0.02,
    z_pixel_um=0.05,
    orientation="coronal",
    flip_x=False,
    flip_y=False,
    flip_z=False,
    affine_n_steps=6,
    affine_use_n_steps=5,
    freeform_n_steps=6,
    freeform_use_n_steps=4,
    bending_energy_weight=0.95,
    grid_spacing_x=-10,
    smoothing_sigma_reference=-1.0,
    smoothing_sigma_floating=-1.0,
    histogram_n_bins_floating=128,
    histogram_n_bins_reference=128,
    n_free_cpus=2,
    sort_input_file=False,
    save_downsampled=True,
    additional_images_downsample=None,
    boundaries=True,
    debug=False,
):
    """
        The main function that will perform the library calls and
    register the atlas to the brain given on the CLI

    :param registration_config:
    :param target_brain_path:
    :param registration_output_folder:
    :param filtered_brain_path:
    :param x_pixel_um:
    :param y_pixel_um:
    :param z_pixel_um:
    :param orientation:
    :param flip_x:
    :param flip_y:
    :param flip_z:
    :param n_free_cpus:
    :param sort_input_file:
    :param save_downsampled:
    :param additional_images_downsample: dict of
    {image_name: image_to_be_downsampled}
    :return:
    """
    n_processes = get_num_processes(min_free_cpu_cores=n_free_cpus)
    load_parallel = n_processes > 1
    paths = Paths(registration_output_folder)
    atlas = Atlas(registration_config, dest_folder=registration_output_folder)
    run = Run(paths, atlas, boundaries=boundaries, debug=debug)

    if run.preprocess:
        logging.info("Preprocessing data for registration")
        logging.info("Loading data")

        brain = BrainProcessor(
            atlas,
            target_brain_path,
            registration_output_folder,
            x_pixel_um,
            y_pixel_um,
            z_pixel_um,
            original_orientation=orientation,
            load_parallel=load_parallel,
            sort_input_file=sort_input_file,
            n_free_cpus=n_free_cpus,
        )

        # reorients the atlas to the orientation of the sample
        brain.swap_atlas_orientation_to_self()

        # reorients atlas to the nifti (origin is the most ventral, posterior,
        # left voxel) coordinate framework

        flip = flips[orientation]
        brain.flip_atlas(flip)

        # flips if the input data doesnt match the nifti standard
        brain.flip_atlas((flip_x, flip_y, flip_z))

        brain.atlas.save_all()
        if save_downsampled:
            brain.target_brain = brain.target_brain.astype(
                np.uint16, copy=False
            )
            logging.info("Saving downsampled image")
            brain.save(paths.downsampled_brain_path)

        brain.filter()
        logging.info("Saving filtered image")
        brain.save(paths.tmp__downsampled_filtered)

        del brain

    if additional_images_downsample:
        for name, image in additional_images_downsample.items():
            if not check_downsampled(registration_output_folder, name):
                save_downsampled_image(
                    image,
                    name,
                    registration_output_folder,
                    atlas,
                    x_pixel_um=x_pixel_um,
                    y_pixel_um=y_pixel_um,
                    z_pixel_um=z_pixel_um,
                    orientation=orientation,
                    n_free_cpus=n_free_cpus,
                    sort_input_file=sort_input_file,
                    load_parallel=load_parallel,
                )
            else:
                logging.info(f"Image: {name} already downsampled, skipping.")

    if run.register:
        logging.info("Registering")

    if any(
        [
            run.affine,
            run.freeform,
            run.segment,
            run.hemispheres,
            run.inverse_transform,
        ]
    ):
        registration_params = RegistrationParams(
            registration_config,
            affine_n_steps=affine_n_steps,
            affine_use_n_steps=affine_use_n_steps,
            freeform_n_steps=freeform_n_steps,
            freeform_use_n_steps=freeform_use_n_steps,
            bending_energy_weight=bending_energy_weight,
            grid_spacing_x=grid_spacing_x,
            smoothing_sigma_reference=smoothing_sigma_reference,
            smoothing_sigma_floating=smoothing_sigma_floating,
            histogram_n_bins_floating=histogram_n_bins_floating,
            histogram_n_bins_reference=histogram_n_bins_reference,
        )
        brain_reg = BrainRegistration(
            registration_config,
            paths,
            registration_params,
            n_processes=n_processes,
        )

    if run.affine:
        logging.info("Starting affine registration")
        brain_reg.register_affine()

    if run.freeform:
        logging.info("Starting freeform registration")
        brain_reg.register_freeform()

    if run.segment:
        logging.info("Starting segmentation")
        brain_reg.segment()

    if run.hemispheres:
        logging.info("Segmenting hemispheres")
        brain_reg.register_hemispheres()

    if run.inverse_transform:
        logging.info("Generating inverse (sample to atlas) transforms")
        brain_reg.generate_inverse_transforms()

    if run.volumes:
        logging.info("Calculating volumes of each brain area")
        calculate_volumes(
            paths.registered_atlas_path,
            paths.hemispheres_atlas_path,
            atlas.get_structures_path(),
            registration_config,
            paths.volume_csv_path,
            left_hemisphere_value=atlas.get_left_hemisphere_value(),
            right_hemisphere_value=atlas.get_right_hemisphere_value(),
        )

    if run.boundaries:
        logging.info("Generating boundary image")
        calc_boundaries(
            paths.registered_atlas_path,
            paths.boundaries_file_path,
            atlas_config=registration_config,
        )

    if run.delete_temp:
        logging.info("Removing registration temp files")
        delete_temp(paths.registration_output_folder, paths)

    logging.info(
        f"amap completed. Results can be found here: "
        f"{registration_output_folder}"
    )
