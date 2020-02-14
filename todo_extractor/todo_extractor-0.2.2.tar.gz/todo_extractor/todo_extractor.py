"""Main functions for the todo-extractor script."""
import json
import re
import subprocess
import typing

TODO_REGEXP = "^.*TODO:.*"


def grep_cmd(search_string: str) -> typing.List[str]:
    """Returns the command to run the selected grep program including flags

    Prioritizes ripgrep (rg) and returns grep if rg is not installed.
    """
    cmd = ["grep", "-rn"]
    if not subprocess.run(
        "command -v rg", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
    ).returncode:
        cmd = ["rg", "-n"]
    cmd.append(search_string)
    return cmd


def search_folder(folder: str) -> typing.List[typing.Dict[str, str]]:
    """Search folder for TODO notes and return the commands"""

    r = subprocess.run(
        grep_cmd(TODO_REGEXP), cwd=folder, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding="utf-8"
    )
    return [
        m.groupdict()
        for m in re.finditer(r"^(?P<file>.*):(?P<line>\d*):.*TODO:\s*(?P<comment>.*)", r.stdout, re.M)
    ]


def serialize_result(search_result: list) -> str:
    """Serializes a list to JSON and return the string

    If the list cannot be serialized, an empty list will be returned.
    """
    try:
        return json.dumps(search_result, indent=2)
    except TypeError:
        # List contains non-serializable objects
        return "[]"


def search_todos(folder: str) -> str:
    """Searches in folder and returns JSON"""
    return serialize_result(search_folder(folder))
