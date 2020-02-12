import os
import logging
import platform

from chainer_addons.training import OptimizerType
from chainer_addons.models import PrepareType
from chainer_addons.links import PoolingType

from cvargparse import GPUParser, Arg, ArgFactory
from cvdatasets.utils import read_info_file

DEFAULT_INFO_FILE=os.environ.get("DATA", "/home/korsch/Data/info.yml")

info_file = read_info_file(DEFAULT_INFO_FILE)

def default_factory(extra_list=[]):
	return ArgFactory(extra_list + [

			Arg("data", default=DEFAULT_INFO_FILE),

			Arg("dataset", choices=info_file.DATASETS.keys()),
			Arg("parts", choices=info_file.PARTS.keys()),
			Arg("--model_type", "-mt",
				default="resnet", choices=info_file.MODELS.keys(),
				help="type of the model"),

			Arg("--input_size", type=int, nargs="+", default=0,
				help="overrides default input size of the model, if greater than 0"),

			PrepareType.as_arg("prepare_type",
				help_text="type of image preprocessing"),

			PoolingType.as_arg("pooling",
				help_text="type of pre-classification pooling"),

			Arg("--load", type=str, help="ignore weights and load already fine-tuned model"),
			Arg("--headless", action="store_true", help="ignores classifier layer during loading"),

			Arg("--n_jobs", "-j", type=int, default=0,
				help="number of loading processes. If 0, then images are loaded in the same process"),

			Arg("--warm_up", type=int, help="warm up epochs"),

			OptimizerType.as_arg("optimizer", "opt",
				help_text="type of the optimizer"),

			Arg("--cosine_schedule", type=int,
				default=-1,
				help="enable cosine annealing LR schedule. This parameter sets the number of schedule stages"),

			Arg("--l1_loss", action="store_true",
				help="(only with \"--only_head\" option!) use L1 Hinge Loss instead of Softmax Cross-Entropy"),

			Arg("--from_scratch", action="store_true",
				help="Do not load any weights. Train the model from scratch"),

			Arg("--label_shift", type=int, default=1,
				help="label shift"),

			Arg("--swap_channels", action="store_true",
				help="preprocessing option: swap channels from RGB to BGR"),

			Arg("--label_smoothing", type=float, default=0,
				help="Factor for label smoothing"),

			Arg("--no_center_crop_on_val", action="store_true",
				help="do not center crop imaages in the validation step!"),

			Arg("--only_head", action="store_true", help="fine-tune only last layer"),
			Arg("--no_progress", action="store_true", help="dont show progress bar"),
			Arg("--augment", action="store_true", help="do data augmentation (random croping and random hor. flipping)"),
			Arg("--force_load", action="store_true", help="force loading from caffe model"),
			Arg("--only_eval", action="store_true", help="evaluate the model only. do not train!"),
			Arg("--init_eval", action="store_true", help="evaluate the model before training"),
			Arg("--no_snapshot", action="store_true", help="do not save trained model"),

			Arg("--output", "-o", type=str, default=".out", help="output folder"),

		])\
		.seed()\
		.batch_size()\
		.epochs()\
		.debug()\
		.learning_rate(lr=1e-2, lrs=10, lrt=1e-5, lrd=1e-1)\
		.weight_decay(default=5e-4)


class FineTuneParser(GPUParser):
	def init_logger(self, simple=False, logfile=None):
		if not self.has_logging: return
		fmt = '{levelname:s} - [{asctime:s}] {filename:s}:{lineno:d} [{funcName:s}]: {message:s}'

		handler0 = logging.StreamHandler()
		handler0.addFilter(HostnameFilter())
		handler0.setFormatter(logging.Formatter("<{hostname:^10s}>: " + fmt, style="{"))

		filename = logfile if logfile is not None else f"{platform.node()}.log"
		handler1 = logging.FileHandler(filename=filename, mode="w")
		handler1.setFormatter(logging.Formatter(fmt, style="{"))

		logger = logging.getLogger()
		logger.addHandler(handler0)
		logger.addHandler(handler1)
		logger.setLevel(getattr(logging, self.args.loglevel.upper(), logging.DEBUG))

class HostnameFilter(logging.Filter):

	def filter(self, record):
		record.hostname = platform.node()
		return True
