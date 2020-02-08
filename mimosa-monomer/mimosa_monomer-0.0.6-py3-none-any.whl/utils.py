"""Helper utility functions"""
import sys
from typing import Type, Any

import typer
from halo import Halo

from mimosa import db


def convert_string_to_bool(user_input: str) -> bool:
    if user_input.lower() == "false":
        return False
    elif user_input.lower() == "true":
        return True
    else:
        raise ValueError(f"Could not convert '{user_input} to boolean")


def convert_string_to_none(user_input: str) -> None:
    if user_input.lower() != "none":
        raise ValueError(
            f"Could not convert {user_input} to None. Expected 'None' or 'none'."
        )
    return None


def prompt_site_key() -> str:
    return typer.prompt("For which site key?", type=str)


def prompt(message: str, data_type=Type) -> Any:
    """More generic wrapper around typer.prompt"""
    return typer.prompt(message, type=data_type)


def check_site_key_exist(site_key: str):
    # Check if site key exists.
    spinner = Halo(text_color="blue")
    spinner.start(f"Checking if site key: {site_key} exists...")
    try:
        db.get_site_key(site_key)
        spinner.succeed()
    except (ValueError, db.NotFound) as err:
        spinner.fail()
        raise err
