import yaml
import os
import urllib

from typing import List
from dataclasses import dataclass

@dataclass
class Source:
    type: str
    url: str

@dataclass
class Dataset:
    name: str
    type: str
    sources: List[Source]

@dataclass
class Group:
    name: str
