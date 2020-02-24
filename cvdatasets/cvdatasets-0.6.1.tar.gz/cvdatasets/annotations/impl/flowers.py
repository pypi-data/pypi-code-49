import numpy as np

from os.path import join

from cvdatasets.annotations.base import BaseAnnotations
from cvdatasets.annotations.base.bbox_mixin import BBoxMixin
from cvdatasets.annotations.base.parts_mixin import PartsMixin
from cvdatasets.utils import _MetaInfo



class FLOWERS_Annotations(BBoxMixin, PartsMixin, BaseAnnotations):
	name="FLOWERS"

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
			[info.bounding_boxes, "_bounding_boxes"],
			[info.parts_file, "_part_locs"],
			[info.part_names_file, "_part_names"],
		]
		return info

	def load(self, *args, **kwargs):
		super(FLOWERS_Annotations, self).load(*args, **kwargs)
		# set labels from [1..120] to [0..119]
		self.labels -= 1
