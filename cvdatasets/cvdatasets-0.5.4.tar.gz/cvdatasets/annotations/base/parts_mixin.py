import abc
import logging
import numpy as np

from collections import OrderedDict
from collections import defaultdict
from cvdatasets.utils.decorators import only_with_info

class PartsMixin(abc.ABC):

	def __init__(self, *, parts=None, **kwargs):
		self.part_type = parts
		self.part_names = OrderedDict()
		self.part_name_list = []

		super(PartsMixin, self).__init__(**kwargs)

	@property
	@only_with_info
	def dataset_info(self):
		if self.part_type is not None:
			return self.info.PARTS[self.part_type]
		else:
			return super(PartsMixin, self).dataset_info

	def check_dataset_kwargs(self, subset, **kwargs):
		if self.dataset_info is None:
			return kwargs

		new_kwargs = {}

		if self.part_type is not None:
			new_kwargs["part_rescale_size"] = self.dataset_info.rescale_size

		new_kwargs.update(kwargs)

		return super(PartsMixin, self).check_dataset_kwargs(subset, **new_kwargs)

	@property
	def has_parts(self):
		return hasattr(self, "_part_locs") and self._part_locs is not None

	@property
	def has_part_names(self):
		return hasattr(self, "_part_names") and self._part_names is not None

	def load(self):
		super(PartsMixin, self).load()

		if self.has_parts:
			self._load_parts()

	def _load_parts(self):
		logging.debug("Loading part annotations")
		assert self.has_parts, "Part locations were not loaded!"
		# this part is quite slow... TODO: some runtime improvements?
		uuid_to_parts = defaultdict(list)
		for content in [i.split() for i in self._part_locs]:
			uuid = content[0]
			# assert uuid in self.uuids, \
			# 	"Could not find UUID \"\" from part annotations in image annotations!".format(uuid)
			uuid_to_parts[uuid].append([float(c) for c in content[1:]])

		uuid_to_parts = dict(uuid_to_parts)
		self.part_locs = np.stack([
			uuid_to_parts[uuid] for uuid in self.uuids]).astype(int)

		if self.has_part_names:
			self._load_part_names()

	def _load_part_names(self):
		self.part_names.clear()
		self.part_name_list.clear()

		for line in self._part_names:
			part_idx, _, name = line.partition(" ")
			self.part_names[int(part_idx)] = name
			self.part_name_list.append(name)

	def parts(self, uuid):
		if self.has_parts:
			return self.part_locs[self.uuid_to_idx[uuid]].copy()

		return None
