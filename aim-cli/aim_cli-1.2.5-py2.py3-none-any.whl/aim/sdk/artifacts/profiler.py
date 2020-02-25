from typing import Any
from abc import ABCMeta
import time

from aim.sdk.artifacts.serializable import Serializable
from aim.engine.stats import stats


class Profiler(Serializable, metaclass=ABCMeta):
    cat = ('profiler',)

    def __init__(self, name: str):
        self.name = name

        system_stats, gpu_stats, process_stats = stats()
        self.stats = {
            'time': time.time(),
            'stats': {
                'system': system_stats,
                'gpu': gpu_stats,
                'process': process_stats,
            }
        }

        super(Profiler, self).__init__(self.cat)

    def __str__(self):
        return self.name

    def serialize(self) -> dict:
        serialized = {
            self.LOG_FILE: {
                'name': self.name,
                'cat': self.cat,
                'content': self.stats,
                'mode': self.CONTENT_MODE_APPEND,
            },
        }

        return serialized
