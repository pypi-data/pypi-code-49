"""Path/Module utils."""
import os

from importlib import import_module


def file_exists(filepath: str):
    """Validate the existence of a filepath."""
    return os.path.exists(filepath)


def module_exists(filepath: str):
    """Find and validate existence of python module"""
    if not filepath:
        return False

    pkg, mdl = _parse_import(filepath)

    try:
        exists = getattr(import_module(pkg), mdl)
    except AttributeError:
        exists = None
    except ModuleNotFoundError:
        exists = None

    return bool(exists)


def _parse_import(filepath):
    """Parse input source module to execute."""
    pkg = ".".join(filepath.split(".")[:-1])
    mdl = filepath.split(".")[-1]

    return pkg, mdl
