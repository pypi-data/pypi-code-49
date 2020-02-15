"""This module is only  intended to be use with uvicorn "import path" mode."""

from escarpolette import create_app
from escarpolette.settings import Config


config = Config.current_config
if config is None:
    raise RuntimeError("The config was not initialised")
else:
    app = create_app(config)
