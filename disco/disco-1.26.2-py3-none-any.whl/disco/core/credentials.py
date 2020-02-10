"""
Credentials related functionality (get current, set and load from env/config
"""
import os
import json

from typing import Tuple

from . import constants, exceptions


class Credentials:
    """Simple skeleton for credentials."""
    token = None
    username = None
    userid = None
    credentials: Tuple[str, str] = (None, None)

    @classmethod
    def has_credentials(cls):
        """Checks if the credentials object contains credentials"""
        return None not in list(cls.credentials)

    @classmethod
    def from_config(cls) -> Tuple[str, str]:
        """Gets credentials from environment variables or configuration file

        Returns:
            tuple [str, str]:
        """
        env_mail = os.environ.get(constants.ENV_VAR_EMAIL_NAME, None)
        env_pass = os.environ.get(constants.ENV_VAR_PASSWORD_NAME, None)

        if None not in (env_mail, env_pass):
            return env_mail, env_pass

        if constants.DISCO_CONFIG_PATH.exists():
            disco_config_content = json.loads(
                constants.DISCO_CONFIG_PATH.read_text())

            return (disco_config_content.get('email'),
                    disco_config_content.get('password'))

        raise exceptions.NoCredentials

    @classmethod
    def update(cls, email, password, save_to_config=False):
        """Set the DISCO credentials to be used when communicating
        with the server.
        Pass `save_to_config=True` to save the credentials to
        `~/.disco_py`, so next time you wouldn't have to set them.
        No need to login after running `set_credentials`,
        login will be done automatically on-demand.

        Args:
            email (str):
            password (str):
            save_to_config (bool):
        """

        if email is not None and password is not None and cls.credentials == (email, password):
            return

        cls.credentials = (email, password)
        cls.token = None
        cls.username = None
        cls.userid = None
        if save_to_config:
            json_content = json.dumps(
                {'email': email,
                 'password': password}
            )
            constants.DISCO_CONFIG_PATH.write_text(json_content)

    @classmethod
    def reset(cls):
        """Resets the credentials to none"""
        cls.credentials = (None, None)
        cls.token = None
        cls.username = None
        cls.userid = None
        try:
            os.remove(constants.DISCO_CONFIG_PATH)
        except OSError:
            pass


def get_credentials_from_config() -> Tuple[str, str]:
    """Legacy mapping to `Credentials.from_config` Gets credentials from
    environment variables or configuration file

    Returns:
        tuple [str, str]:
    """
    return Credentials.from_config()


def set_credentials(*args, **kwargs):
    """Legacy mapping to `Credentials.update`
    Set the DISCO credentials to be used when communicating with the server.
    Pass `save_to_config=True` to save the credentials to `~/.disco_py`, so
    next time you wouldn't have to set them.
    No need to login after running `set_credentials`, login will be done
    automatically on-demand.

    Args:
        *args:
        **kwargs:
    """
    return Credentials.update(*args, **kwargs)
