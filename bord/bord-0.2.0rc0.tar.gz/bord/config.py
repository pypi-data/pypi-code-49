import os
import json
from typing import List, Optional
from dataclasses import dataclass
import logging

from screeninfo import get_monitors, Enumerator, Monitor

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class Config:
    interval: int
    urls: List[str]
    monitor: Monitor
    executable_path: Optional[str] = None


def _get_system_graphics_subsystem():
    system = os.uname()
    supported = {"Linux": Enumerator.Xinerama, "Darwin": Enumerator.OSX}
    try:
        return supported[system.sysname]
    except KeyError as e:
        raise Exception(
            f"Detecting monitors and resolution is not supported for {system.sysname}"
        ) from e


def init_config(config_path: str = None):
    if config_path is None:
        config_path = "./config.json"

    with open(config_path) as fp:
        cfg_json = json.load(fp)

    monitors = [monitor for monitor in get_monitors(_get_system_graphics_subsystem())]
    if len(monitors) > 1:
        logger.warning("Multiple monitors detected, using monitor[0]=", monitors[0])
    return Config(monitor=monitors[0], **cfg_json)
