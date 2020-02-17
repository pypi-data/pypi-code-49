import asyncio
import uuid
from typing import Mapping, Optional

from aio_pika.patterns import RPC

from kode_rpc import request_trace_id
from kode_rpc.rabbitmq import RabbitMQ
from kode_rpc.util.rpc import JsonRPC


class RPCClient:
    def __init__(self, application_name: str):
        self._application_name = application_name
        self._broker: Optional[RabbitMQ] = None
        self._rpc: Optional[RPC] = None

    async def connect(self, *, rabbitmq_host: str, rabbitmq_user: str, rabbitmq_password: str):
        assert not self._broker, 'Client is already initialized'

        self._broker = RabbitMQ(
            host=rabbitmq_host,
            user=rabbitmq_user,
            password=rabbitmq_password,
        )

        await self._broker.connect()
        assert self._broker.connection, 'Broker connection is broken'

        channel = await self._broker.connection.channel()
        self._rpc = await JsonRPC.create(channel)

    async def disconnect(self):
        async def _closer():
            await self._rpc.close()
            await self._rpc.channel.close()
            await self._broker.disconnect()

        await asyncio.shield(_closer())

    def get_trace_id(self) -> str:
        try:
            return request_trace_id.get()
        except LookupError:
            return uuid.uuid4().hex

    async def _call(self, method: str, payload: Optional[Mapping] = None):
        assert self._rpc, 'Client is not initialized'
        # noinspection PyTypeChecker
        return await self._rpc.call(method_name=method, kwargs={
            **(payload or {}),
            'trace_id': self.get_trace_id(),
            'master': self._application_name
        })

    async def call(self, service_name: str, method: str, version: int = 1, payload: Optional[Mapping] = None):
        return await self._call(f'{service_name}_{method}_v{version}', payload)
