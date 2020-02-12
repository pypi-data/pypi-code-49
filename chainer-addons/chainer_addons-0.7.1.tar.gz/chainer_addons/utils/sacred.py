import logging
import os
import re
import sys

from sacred import Experiment, SETTINGS
from sacred.observers import MongoObserver
from sacred.utils import apply_backspaces_and_linefeeds

from pathlib import Path
from urllib.parse import quote_plus

def progress_bar_filter(text,
	escape=re.compile(r"\x1B\[([0-?]*[ -/]*[@-~])"),
	line_contents=re.compile(r".*(total|this epoch|Estimated time|\d+ iter, \d+ epoch / \d+ epochs).*\n")):
	_text = apply_backspaces_and_linefeeds(text)
	_text = escape.sub("", _text)
	_text = line_contents.sub("", _text)
	return _text


class MPIExperiment(Experiment):

	def __init__(self, opts, *args,
		host=None,
		comm=None,
		no_observer=False,
		output_filter=progress_bar_filter,
		**kwargs):

		if kwargs.get("base_dir") is None:
			base_dir = Path(sys.argv[0]).resolve().parent
			logging.info(f"Base experiment directory: {base_dir}")
			kwargs["base_dir"] = str(base_dir)

		super(MPIExperiment, self).__init__(*args, **kwargs)

		_main_process = comm is None or comm.rank == 0

		if no_observer or not _main_process:
			return

		self.logger = logging.getLogger()
		self.captured_out_filter = output_filter

		creds = MPIExperiment.get_creds()
		_mongo_observer = MongoObserver.create(
			url=MPIExperiment.auth_url(creds, host=host),
			db_name=creds["db_name"],
		)

		self.observers.append(_mongo_observer)

		self.add_config(**opts.__dict__)

	def __call__(self, *args, **kwargs):
		return self._create_run()(*args, **kwargs)

	@classmethod
	def get_creds(cls):
		return dict(
			user=quote_plus(os.environ["MONGODB_USER_NAME"]),
			password=quote_plus(os.environ["MONGODB_PASSWORD"]),
			db_name=quote_plus(os.environ["MONGODB_DB_NAME"]),
		)

	@classmethod
	def auth_url(cls, creds, host="localhost", port=27017):
		host = host or cls.get_host()
		logging.info(f"MongoDB host: {host}")

		url = "mongodb://{user}:{password}@{host}:{port}/{db_name}?authSource=admin".format(
			host=host, port=port, **creds)
		return url

	@classmethod
	def get_host(cls):
		return quote_plus(os.environ.get("MONGODB_HOST", "localhost"))

SETTINGS.DISCOVER_SOURCES = "dir"

__all__ = [
	"MPIExperiment",
	"progress_bar_filter"
]
