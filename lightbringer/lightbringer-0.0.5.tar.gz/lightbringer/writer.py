from .connection import Connection
from .connection import validate_topic_name


class WriterConnection(Connection):
	async def _setup(self):
		self._pub_error = None
		await super()._setup()

	async def __aexit__(self, typ, val, tb):
		await super().__aexit__(typ, val, tb)
		if val is None and self._pub_error is not None:
			raise self._pub_error

	def on_error(self, exc):
		self._pub_error = exc

	async def _pub_cmd(self, *args, **kwargs):
		if self._pub_error is not None:
			raise self._pub_error
		return await self._ack_cmd(*args, **kwargs)


class Writer:
	def __init__(self, addr, *, topic, **kwargs):
		host, port = addr.rsplit(':', 1)
		self._server = host, int(port)
		self._conn_args = kwargs

		validate_topic_name(topic)
		self._topic = topic

	async def __aenter__(self):
		self._conn = WriterConnection(self._server, **self._conn_args)
		await self._conn.__aenter__()
		return self

	async def __aexit__(self, *args):
		await self._conn.__aexit__(*args)
		del self._conn

	async def pub(self, body):
		return await self._conn._pub_cmd(f'PUB {self._topic}', body=body)

	async def dpub(self, delay, body):
		return await self._conn._pub_cmd(f'DPUB {self._topic} {delay}', body=body)
