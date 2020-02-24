from .execution import Execution
from .client import Client
from .const import DEFAULT_HOST


def get_execution_environment(apikey, host=DEFAULT_HOST):
    """
    Returns an Execution object that enables interaction with an instances Execution Environment.
    This includes functionality to create and delete stream/table resources and transformations.

    :param apikey:
    API key associated with StreamSQL instance
    :param host:
    Host of the StreamSQL instance. Defaults to streamsql.io
    :return:
    A new Execution object associated with the StreamSQL instance
    """
    return Execution(apikey, host)


def get_client_environment(apikey, host=DEFAULT_HOST):
    """
    Returns a Client object that enables interaction with an instances Client Environment.
    This includes functionality to ingest and fetch data.

    :param apikey:
    API key associated with StreamSQL instance
    :param host:
    Host of the StreamSQL instance. Defaults to streamsql.io
    :return:
    A new Client object associated with the StreamSQL instance
    """
    return Client(apikey, host)
