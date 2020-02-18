import logging
from brainio import brainio
from skimage.segmentation import find_boundaries
from imlib.image.scale import scale_and_convert_to_16_bits
from imlib.image import nii

from amap.tools.source_files import source_custom_config


def main(registered_atlas, boundaries_out_path, atlas_config=None):
    atlas_info = GetAtlas(registered_atlas, atlas_config=atlas_config)
    boundaries(
        atlas_info.atlas,
        boundaries_out_path,
        atlas_scale=atlas_info.atlas_scale,
        transformation_matrix=atlas_info.transformation_matrix,
    )


class GetAtlas:
    def __init__(self, registered_atlas, atlas_config=None):

        self._atlas_path = registered_atlas
        self._atlas_config = atlas_config

        self.atlas = None
        self.atlas_scale = None
        self.transformation_matrix = None

        self.get_atlas_config()
        self.get_atlas()

    def get_atlas_config(self):
        if self._atlas_config is None:
            self._atlas_config = source_custom_config()

    def get_atlas(self):
        atlas = brainio.load_nii(self._atlas_path, as_array=False)
        self.atlas_scale = atlas.header.get_zooms()
        self.atlas = atlas.get_data()
        self.get_transformation_matrix()

    def get_transformation_matrix(self):
        self.transformation_matrix = nii.get_transformation_matrix(
            self._atlas_config
        )


def boundaries(
    atlas,
    boundaries_out_path,
    atlas_labels=False,
    atlas_scale=None,
    transformation_matrix=None,
):
    """
    Generate the boundary image, which is the border between each segmentation
    region. Useful for overlaying on the raw image to assess the registration
    and segmentation

    :param atlas: The registered atlas
    :param boundaries_out_path: Path to save the boundary image
    :param atlas_labels: If True, keep the numerical values of the atlas for
    the labels
    :param atlas_scale: Image scaling so that the resulting nifti can be
    processed using other tools.
    :param transformation_matrix: Transformation matrix so that the resulting
    nifti can be processed using other tools.
    """
    boundaries_image = find_boundaries(atlas, mode="inner")
    if atlas_labels:
        boundaries_image = boundaries_image * atlas
    boundaries_image = scale_and_convert_to_16_bits(boundaries_image)
    logging.debug("Saving segmentation boundary image")
    brainio.to_nii(
        boundaries_image,
        boundaries_out_path,
        scale=atlas_scale,
        affine_transform=transformation_matrix,
    )
