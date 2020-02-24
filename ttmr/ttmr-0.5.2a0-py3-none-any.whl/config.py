import os
from pathlib import Path
from types import SimpleNamespace

import pendulum
import tomlkit
from appdirs import AppDirs

DEFAULT_CONFIG = """
[ttmr]
project_dir=
timezone=US/Pacific
"""


def init_file(path):
    if not os.path.exists(path):
        with open(path, "w") as fh_:
            fh_.write("")


def assert_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)


def get_appdir():
    appdirs = AppDirs("ttmr", "mgemmill")
    user_data_dir = appdirs.user_data_dir
    assert_dir(user_data_dir)
    return user_data_dir


#  class Config(object):
#      def __str__(self):
#          output = []
#          for k, v in self.__dict__.items():
#              if not k.startswith("_"):
#                  output.append("{}={}".format(k, v))
#          return "\n".join(output)
#
#      def load_cli_args(self, args):
#          for key, val in args.items():
#              normalize_key = key.strip("-").replace("-", "_").lower()
#              setattr(self, "cli_" + normalize_key, val)


def get_config():
    cfg = SimpleNamespace()

    cfg.appdirs = appdirs = AppDirs("ttmr", "mgemmill")
    cfg.user_data_dir = app_dir = appdirs.user_data_dir

    assert_dir(app_dir)

    cfg.config_path = Path(app_dir, "ttmr.cfg").resolve()
    cfg.data = data = tomlkit.parse(cfg.config_path.read_text())
    cfg.db_path = Path(app_dir, data["ttmr"]["db"])
    cfg.timezone = timezone = data["ttmr"].get("timezone", "America/Vancouver")

    today = pendulum.today(timezone)
    hour, minute = [int(s) for s in data["ttmr"].get("start_time", "07:00").split(":")]

    cfg.day_start_time = pendulum.datetime(
        year=today.year, month=today.month, day=today.day, hour=hour, minute=minute
    )

    return cfg


#  def config():
#
#      c = Config()
#
#      c.appdir = appdir = get_appdir()
#      c.configfile = os.path.join(appdir, "ttmr.ini")
#
#      config_path = Path(appdir, 'ttmr.cfg').resolve()
#
#
#      c.sqlite = os.path.join(appdir, "ttmr.db3")
#
#      if not os.path.exists(c.configfile):
#          with open(c.configfile, "w") as fh_:
#              fh_.write(DEFAULT_CONFIG)
#
#      parser = SafeConfigParser()
#      parser.read(c.configfile)
#
#      c.project_dir = parser.get("ttmr", "project_dir")
#      c.timezone = parser.get("ttmr", "timezone")
#
#      c.dt = dt = DT(c.timezone)
#
#      if not os.path.exists(c.sqlite):
#          with Database(c.sqlite, dt) as db:
#              db.initialize()
#
#      c._dbfile = Path(appdir, 'ttmr.db')
#
#      c._cfg = tomlkit.parse(config_path.read_text())
#
#      return c
