import logging
import asyncio

from pipeline import settings


LOG = logging.getLogger(__name__)


class Producer():
    ''' Base class for producers. '''
    def __init__(self):
        self.hosts = settings.PRODUCER_HOSTS
        self.target = settings.PRODUCER_TARGET
        self.database = settings.PRODUCER_DATABASE
        self.username = settings.PRODUCER_USERNAME
        self.password = settings.PRODUCER_PASSWORD

        self.producer = None
        self.connected = False
        self.loop = asyncio.get_event_loop()

    async def _setup(self) -> None:
        LOG.debug('Setting up producer.')

    async def connect(self) -> None:
        ''' Connect to producer destination '''
        raise NotImplementedError("No driver specified")

    async def disconnect(self) -> None:
        ''' Disconnect from producer destination '''
        raise NotImplementedError("No driver specified")

    async def produce_data(self, data: dict, target: str = None) -> None:
        '''
        Override this method to produce data to specific producer destination,
        which we randomly call target.
        '''
        if not target:
            target = settings.PRODUCER_TARGET
