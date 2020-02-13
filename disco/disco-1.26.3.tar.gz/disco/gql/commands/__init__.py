"""
Tool for retriving GQL commands from files.
Autoloads the queries present in the dir as dictionary
"""
import os
from pathlib import Path


def _load_commands():
    _here = os.path.abspath(os.path.dirname(__file__))
    return {p.name[:-4]: p.read_text() for p in Path(_here).glob("*.gql")}


REGISTERED_COMMANDS = _load_commands()
