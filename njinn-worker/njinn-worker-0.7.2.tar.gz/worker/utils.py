import os
import sys

def is_windows():
    return sys.platform.startswith("win")

def get_config_path():
    working_dir = os.path.dirname(os.path.realpath(__file__))
    config_path = os.getenv("NJINN_WORKER_CONFIG")
    config_file = "worker.ini"
    if not config_path:
        if sys.platform in ("linux2", "linux"):
            config_path = f"/etc/njinn/{config_file}"
        else:
            config_path = os.path.join(working_dir, config_file)
    return config_path