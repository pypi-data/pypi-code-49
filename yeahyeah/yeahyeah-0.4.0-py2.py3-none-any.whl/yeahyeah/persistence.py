"""Saving and loading things. Raising useful exceptions

"""
import json
from typing import Dict

from yeahyeah.exceptions import YeahYeahException


class SettingsFile:
    """Base class for a context file that can be loaded and saved"""

    def __init__(self, path):
        """
        Parameters
        ----------
        path: Pathlike
            full path to file
        """

        self.path = path

    def save(self, data):
        """Save given data to file

        Raises
        ------
        YeahYeahPersistenceException
            If saving does not work

        """
        raise NotImplemented()

    def load(self):
        """
        Raises
        ------
        FileNotFoundError
            If rel_path does not exist
        YeahYeahPersistenceException
            If loading does not work

        """
        raise NotImplemented()


class JSONSettingsFile(SettingsFile):
    """A JSON-encoded file

    """

    def load(self):
        """
        Raises
        ------
        FileNotFoundError
            If rel_path does not exist
        YeahYeahPersistenceException
            If loading does not work

        Returns
        -------
        dict:
            The loaded json

        """
        with open(self.path, "r") as f:
            try:
                return json.loads(f.read())
            except json.decoder.JSONDecodeError as e:
                raise YeahYeahPersistenceException(
                    f"Error trying to decode contents of {self.path}: {e}"
                )

    def save(self, dict_in: Dict):
        """

        Parameters
        ----------
        dict_in:
            The data to save

        Raises
        ------
        YeahYeahPersistenceException
            If saving does not work

        Returns
        -------
        dict:
            The data to save in json format

        """
        with open(self.path, "w") as f:
            try:
                f.write(json.dumps(dict_in))
            except TypeError as e:
                raise YeahYeahPersistenceException(
                    f"Error trying to save dict {dict_in} to {self.path}: {e}"
                )

    def exists(self):
        return self.path.exists()


class YeahYeahPersistenceException(YeahYeahException):
    pass
