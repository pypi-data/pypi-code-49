from .clientservice import AnalyticToolClient
from .connection import ServerConnection
from .. import config
from ..interfaces import ClientMode


def run():
    client = AnalyticToolClient(
        ServerConnection(**config.__dict__), ClientMode[config.mode]
    )
    client.start()
