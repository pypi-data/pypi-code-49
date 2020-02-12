import numpy as np
import simplejson as json

from os.path import isfile
from os.path import join
from sklearn.model_selection import StratifiedShuffleSplit

from cvdatasets.annotations.base import BaseAnnotations
from cvdatasets.utils import _MetaInfo

class TIGERS_Annotations(BaseAnnotations):
	name="tigers"

	@property
	def meta(self):
		info = _MetaInfo(
			images_folder="images",
			images_file=join("atrw_anno_reid_train", "reid_list_train.csv"),
			parts_file=join("atrw_anno_reid_train", "reid_keypoints_train.json"),
		)

		info.structure = [
			[info.images_file, "_images"],
			[info.parts_file, "_part_locs"],
		]
		return info


	def _load_uuids(self):
		self.uuids, self.cls_ids = [], []
		self.uuid_to_idx, self.images = {}, []

		for i, line in enumerate(self._images):
			cls_id, imname = line.split(",")
			self.uuids.append(imname)
			self.uuid_to_idx[imname] = i

			self.images.append(imname)
			self.cls_ids.append(int(cls_id))

		self.uuids, self.images, self.cls_ids = map(np.array, [self.uuids, self.images, self.cls_ids])

	def _load_labels(self):
		self.classes, self.labels = np.unique(self.cls_ids, return_inverse=True)

	def _load_split(self, seed=4211):

		splitter = StratifiedShuffleSplit(n_splits=1, test_size=0.3, random_state=seed)

		(train_IDs, test_IDs), = splitter.split(X=self.uuids, y=self.labels)

		self.train_split = np.zeros_like(self.uuids, dtype=bool)

		self.train_split[train_IDs] = 1
		self.test_split = np.logical_not(self.train_split)

	def _load_parts(self):
		keypoints = []
		for image in self.images:
			kpts = self._part_locs[image]
			kpts = np.array(kpts).reshape(-1, 3)
			kpt_idxs = np.arange(len(kpts))
			kpts = np.hstack([kpt_idxs.reshape(-1, 1), kpts])

			keypoints.append(kpts)

		self.part_locs = np.array(keypoints)
		self.part_locs = np.minimum(self.part_locs, 0)
		n_parts = self.part_locs.shape[1]
		self._part_names = [f"{i} part #{i}" for i in range(n_parts)]
		self._load_part_names()

	def read_content(self, file, attr):
		if not file.endswith(".json"):
			return super(TIGERS_Annotations, self).read_content(file, attr)

		with self._open(file) as f:
			content = json.load(f)

		setattr(self, attr, content)
