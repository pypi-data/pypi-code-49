import abc
import logging
import numpy as np

class BBoxMixin(abc.ABC):

	@property
	def has_bounding_boxes(self):
		return hasattr(self, "_bounding_boxes") and self._bounding_boxes is not None

	def load(self):
		super(BBoxMixin, self).load()

		if self.has_bounding_boxes:
			self._load_bounding_boxes()

	def _load_bounding_boxes(self):
		logging.debug("Loading bounding box annotations")
		assert self._bounding_boxes is not None, "Bouding boxes were not loaded!"

		uuid_to_bbox = {}
		for content in [i.split() for i in self._bounding_boxes]:
			uuid, bbox = content[0], content[1:]
			uuid_to_bbox[uuid] = [float(i) for i in bbox]

		self.bounding_boxes = np.array(
			[tuple(uuid_to_bbox[uuid]) for uuid in self.uuids],
			dtype=self.meta.bounding_box_dtype)

	def bounding_box(self, uuid):
		if self.has_bounding_boxes:
			return self.bounding_boxes[self.uuid_to_idx[uuid]].copy()

		return np.array((0,0, 1,1), dtype=self.meta.bounding_box_dtype)
