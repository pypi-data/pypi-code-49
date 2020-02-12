import numpy as np

from os.path import join

from cvdatasets.annotations.base import BaseAnnotations
from cvdatasets.annotations.base.bbox_mixin import BBoxMixin
from cvdatasets.annotations.base.parts_mixin import PartsMixin
from cvdatasets.utils import _MetaInfo



class CUB_Annotations(BBoxMixin, PartsMixin, BaseAnnotations):
	name="CUB200"

	@property
	def meta(self):
		info = _MetaInfo(
			images_folder="images",
			images_file="images.txt",
			labels_file="labels.txt",
			split_file="tr_ID.txt",
			bounding_boxes="bounding_boxes.txt",
			bounding_box_dtype=np.dtype([(v, np.int32) for v in "xywh"]),
			parts_file=join("parts", "part_locs.txt"),
			part_names_file=join("parts", "parts.txt"),

		)

		info.structure = [
			[info.images_file, "_images"],
			[info.labels_file, "labels"],
			[info.split_file, "_split"],
			[info.parts_file, "_part_locs"],
			[info.part_names_file, "_part_names"],
			[info.bounding_boxes, "_bounding_boxes"],
		]
		return info

	def load(self):
		super(CUB_Annotations, self).load()
		# set labels from [1..200] to [0..199]
		self.labels -= 1

		if self.has_parts:
			# set part idxs from 1-idxs to 0-idxs
			self.part_locs[..., 0] -= 1
