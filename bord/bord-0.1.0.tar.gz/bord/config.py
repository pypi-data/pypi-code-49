import json
from typing import List
from dataclasses import dataclass

from screeninfo import get_monitors, Enumerator, Monitor


@dataclass(frozen=True)
class Config:
    interval: int
    urls: List[str]
    monitor: Monitor


def init_config(config_path: str = None):
    if config_path is None:
        config_path = "./config.json"

    with open(config_path) as fp:
        cfg_json = json.load(fp)

    monitors = [monitor for monitor in get_monitors(Enumerator.Xinerama)]
    assert len(monitors) == 1, "Multiple monitors are not supported"
    return Config(monitor=monitors[0], **cfg_json)
