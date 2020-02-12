import abc
import logging
import numpy as np

from collections import OrderedDict
from collections import defaultdict
from os.path import isdir
from os.path import isfile
from os.path import join

from cvdatasets.dataset import Dataset
from cvdatasets.utils import feature_file_name
from cvdatasets.utils import read_info_file
from cvdatasets.utils import pretty_print_dict
from cvdatasets.utils.decorators import only_with_info

class BaseAnnotations(abc.ABC):

	FEATURE_PHONY = dict(train=["train"], test=["test", "val"])

	@classmethod
	def new(cls, opts, **additional_kwargs):
		kwargs = dict(
			root_or_infofile=opts.data,
			parts=getattr(opts, "parts", None),
			load_strict=getattr(opts, "load_strict", False),
			feature_model=getattr(opts, "feature_model", False),
		)

		kwargs.update(additional_kwargs)

		return cls(**kwargs)


	def __init__(self, *, root_or_infofile, feature_model=None, load_strict=True, **kwargs):
		super(BaseAnnotations, self).__init__(**kwargs)
		self.feature_model = feature_model
		self.load_strict = load_strict

		if isdir(root_or_infofile):
			self.info = None
			self.root = root_or_infofile

		elif isfile(root_or_infofile):
			self.root = self.root_from_infofile(root_or_infofile)

		else:
			raise ValueError("Root folder or info file does not exist: \"{}\"".format(
				root_or_infofile
			))

		for fname, attr in self.meta.structure:
			self.read_content(fname, attr)

		self.load()


	@property
	@only_with_info
	def data_root(self):
		return join(self.info.BASE_DIR, self.info.DATA_DIR)

	@property
	@only_with_info
	def dataset_info(self):
		return self.info.DATASETS[self.__class__.name]

	def root_from_infofile(self, info_file):
		self.info = read_info_file(info_file)

		dataset_info = self.dataset_info
		annot_dir = join(self.data_root, dataset_info.folder, dataset_info.annotations)

		assert isdir(annot_dir), "Annotation folder does exist! \"{}\"".format(annot_dir)
		return annot_dir

	def new_dataset(self, subset=None, dataset_cls=Dataset, **kwargs):
		if subset is not None:
			uuids = getattr(self, "{}_uuids".format(subset))
		else:
			uuids = self.uuids

		kwargs = self.check_dataset_kwargs(subset, **kwargs)
		return dataset_cls(uuids=uuids, annotations=self, **kwargs)

	def check_dataset_kwargs(self, subset, **kwargs):
		dataset_info = self.dataset_info
		if dataset_info is None:
			return kwargs

		logging.debug("Dataset info: {}".format(pretty_print_dict(dataset_info)))

		# TODO: pass all scales
		new_kwargs = {}

		if "scales" in dataset_info:
			new_kwargs["ratio"] = dataset_info.scales[0]

		if "is_uniform" in dataset_info:
			new_kwargs["uniform_parts"] = dataset_info.is_uniform

		if None not in [subset, self.feature_model]:
			tried = []
			model_info = self.info.MODELS[self.feature_model]
			for subset_phony in BaseAnnotations.FEATURE_PHONY[subset]:
				features = feature_file_name(subset_phony, dataset_info, model_info)
				feature_path = join(self.root, "features", features)
				if isfile(feature_path): break
				tried.append(feature_path)
			else:
				raise ValueError(
					"Could not find any features in \"{}\" for {} subset. Tried features: {}".format(
					join(self.root, "features"), subset, tried))

			logging.info("Using features file from \"{}\"".format(feature_path))
			new_kwargs["features"] = feature_path
		new_kwargs.update(kwargs)

		logging.debug("Final kwargs: {}".format(pretty_print_dict(new_kwargs)))
		return new_kwargs

	@property
	@abc.abstractmethod
	def meta(self):
		pass

	def _path(self, file):
		return join(self.root, file)

	def _open(self, file):
		return open(self._path(file))

	def read_content(self, file, attr):
		content = None
		fpath = self._path(file)
		if isfile(fpath):
			with self._open(file) as f:
				content = [line.strip() for line in f if line.strip()]
		else:
			msg = "File \"{}\" was not found!".format(fpath)
			if self.load_strict:
				raise AssertionError(msg)
			else:
				logging.warning(msg)

		setattr(self, attr, content)


	def load(self):
		logging.debug("Loading uuids, labels and training-test split")
		self._load_uuids()
		self._load_labels()
		self._load_split()

	def _load_labels(self):
		self.labels = np.array([int(l) for l in self.labels], dtype=np.int32)

	def _load_uuids(self):
		assert self._images is not None, "Images were not loaded!"
		uuid_fnames = [i.split() for i in self._images]
		self.uuids, self.images = map(np.array, zip(*uuid_fnames))
		self.uuid_to_idx = {uuid: i for i, uuid in enumerate(self.uuids)}

	def _load_split(self):
		assert self._split is not None, "Train-test split was not loaded!"
		uuid_to_split = {uuid: int(split) for uuid, split in zip(self.uuids, self._split)}
		self.train_split = np.array([uuid_to_split[uuid] for uuid in self.uuids], dtype=bool)
		self.test_split = np.logical_not(self.train_split)

	def image_path(self, image):
		return join(self.root, self.meta.images_folder, image)

	def image(self, uuid):
		fname = self.images[self.uuid_to_idx[uuid]]
		return self.image_path(fname)

	def label(self, uuid):
		return self.labels[self.uuid_to_idx[uuid]].copy()

	def _uuids(self, split):
		return self.uuids[split]

	@property
	def train_uuids(self):
		return self._uuids(self.train_split)

	@property
	def test_uuids(self):
		return self._uuids(self.test_split)

from .bbox_mixin import BBoxMixin
from .parts_mixin import PartsMixin
