from typing import Any

from .base import Client


async def init_client(cls: Client, **kwargs: Any) -> Client:
    '''
    Creates an instance and runs setup instructions of supplied client class.
    '''
    client = cls(**kwargs)
    await client._setup()
    return client


