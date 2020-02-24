import numpy as np
import simplejson as json

from os.path import join

from cvdatasets.annotations.base import BaseAnnotations
from cvdatasets.annotations.base.bbox_mixin import BBoxMixin
from cvdatasets.annotations.base.parts_mixin import PartsMixin
from cvdatasets.utils import _MetaInfo


class HED_Annotations(BBoxMixin, PartsMixin, BaseAnnotations):

	name="HED"

	@property
	def meta(self):
		info = _MetaInfo(
			images_folder="images",

			images_file="images.txt",
			labels_file="labels.txt",
			split_file="tr_ID.txt",
			# fake bounding boxes: the whole image
			bounding_box_dtype=np.dtype([(v, np.int32) for v in "xywh"]),

			parts_file=join("parts", "part_locs.txt"),
			part_names_file=join("parts", "parts.txt"),
		)

		info.structure = [
			[info.images_file, "_images"],
			[info.labels_file, "labels"],
			[info.split_file, "_split"],
		]
		return info

	def _load_bounding_boxes(self):
		self.bounding_boxes = np.zeros(len(self.uuids),
			dtype=self.meta.bounding_box_dtype)

		for i in range(len(self.uuids)):
			self.bounding_boxes[i]["w"] = 224
			self.bounding_boxes[i]["h"] = 224
