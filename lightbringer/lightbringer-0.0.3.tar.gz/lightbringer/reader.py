import aiohttp
import asyncio
import contextlib
import datetime
import logging
import struct
import sys

from . import _compat
from .connection import Connection
from .connection import ConnectionDropped
from .connection import validate_topic_name


logger = logging.getLogger(__name__)

class ReaderConnection(Connection):
	def __init__(self,
		addr, *,
		topic,
		channel,
		queue,
		_on_unclean_exit,
		max_in_flight: int = 10,
		message_keepalive: int = 50, # should be bellow the nsqd --message-timeout (default 60)
		**kwargs,
	):
		super().__init__(addr, **kwargs)
		validate_topic_name(topic)
		self._topic = topic
		self._channel = channel
		self._queue = queue
		self._max_in_flight = max_in_flight
		self._message_keepalive = message_keepalive
		self._subscribed = False
		self._on_unclean_exit = _on_unclean_exit

	async def _setup(self):
		await super()._setup()
		self._inflight = {}
		await self._ack_cmd(f'SUB {self._topic} {self._channel}')
		await self._cmd(f'RDY {self._max_in_flight}')
		self._subscribed = True

	async def on_message(self, data):
		msg = Message(self, data)
		self._inflight[msg.mid] = msg
		await self._queue.put((msg, None))

	def on_error(self, exc):
		if not hasattr(self, '_exit_task'):
			self._exit_task = _compat.create_task(self._exit(exc))

	async def _exit(self, exc):
		if exc is not None and not isinstance(exc, asyncio.CancelledError):
			await self._on_unclean_exit(self, exc)

		if self._subscribed:
			self._subscribed = False
			try:
				await self._cmd('CLS') # not waiting for a CLOSE_WAIT that might never come
			except ConnectionDropped:
				pass

		if getattr(self, '_inflight', None):
			await asyncio.wait([msg.req() for msg in self._inflight.values()])
			del self._inflight

		await super().__aexit__(type(exc), exc, None)

	async def __aexit__(self, typ, val, tb):
		self.on_error(val)
		await self._exit_task


class DirectConnection(ReaderConnection):
	"""Manages a single direct connection to a nsqd"""

	def __init__(self, addr, *args, **kwargs):
		host, port = addr.rsplit(':', 1)
		super().__init__((host, int(port)), *args, **kwargs)


class Lookup:
	"""Manages the connections to all the producers returned by one lookup server"""

	def __init__(self, addr, topic, refresh_interval, conn_args):
		self._addr = addr
		self._topic = topic
		self._refresh_interval = refresh_interval
		self._conn_args = conn_args

	async def __aenter__(self):
		self._session = aiohttp.ClientSession()
		await self._session.__aenter__()

		self._connections = {}
		await self._refresh()
		coro = self._refresh_periodic()
		self._refresh_task = _compat.create_task(coro)

	async def __aexit__(self, *args):
		self._refresh_task.cancel()
		with contextlib.suppress(asyncio.CancelledError):
			await self._refresh_task
		del self._refresh_task

		await self._session.__aexit__(*args)
		del self._session

		await asyncio.gather(*(c.__aexit__(*args) for c in self._connections.values()))
		del self._connections

	async def _on_unclean_exit(self, conn, exc):
		if conn._addr in self._connections:
			del self._connections[conn._addr]
			if not self._connections:
				logger.warning(f'Dropped last connection to %s in lookup %s: {exc!r}', conn._addr, self._addr)

	async def _refresh(self):
		async with self._session.get(
			f'{self._addr}/lookup',
			params={'topic': self._topic},
		) as resp:
			if resp.status == 404:
				new = set()
			else:
				resp.raise_for_status()
				r = await resp.json()
				new = {(
					o.get('broadcast_address', o.get('address')),
					o['tcp_port'],
				) for o in r['producers']}

		old = set(self._connections.keys())

		async def remove(addr):
			conn = self._connections.pop(addr)
			await conn.__aexit__(None, None, None)
		async def add(addr):
			try:
				conn = ReaderConnection(addr, _on_unclean_exit=self._on_unclean_exit, **self._conn_args)
				await conn.__aenter__()
			except asyncio.CancelledError:
				raise
			except Exception as exc:
				logger.error(f'Error connecting to %s from lookup %s: {exc!r}', addr, self._addr)
			else:
				self._connections[addr] = conn

		await asyncio.gather(
			*(remove(addr) for addr in old if addr not in new),
			*(add(addr) for addr in new if addr not in old),
		)

	async def _refresh_periodic(self):
		while True:
			try:
				await self._refresh()
			except asyncio.CancelledError:
				raise
			except Exception as exc:
				logger.warning(f'Lookup call to %s failed: {exc!r}', self._addr)
			await asyncio.sleep(self._refresh_interval)


class Reader:
	def __init__(self, *,
		topic,
		channel,
		nsqd_tcp_addresses=None,
		lookupd_http_addresses=None,
		lookupd_refresh_interval=10, # seconds
		**kwargs,
	):
		self._topic = topic
		self._channel = channel
		self._nsqd_tcp_addresses = nsqd_tcp_addresses or []
		self._lookupd_http_addresses = lookupd_http_addresses or []
		self._lookupd_refresh_interval = lookupd_refresh_interval
		self._conn_args = kwargs

	async def _direct_conn_unclean_exit(self, conn, exc):
		await self._queue.put((None, exc))

	async def __aenter__(self):
		self._queue = asyncio.Queue()
		self._stack = await _compat.AsyncExitStack().__aenter__()

		conn_args = {
			'topic': self._topic,
			'channel': self._channel,
			'queue': self._queue,
			**self._conn_args
		}

		self._lookups = [
			Lookup(a, self._topic, self._lookupd_refresh_interval, conn_args)
			for a in self._lookupd_http_addresses
		]
		self._direct_connections = [
			DirectConnection(a, _on_unclean_exit=self._direct_conn_unclean_exit, **conn_args)
			for a in self._nsqd_tcp_addresses
		]
		await asyncio.gather(*(
			self._stack.enter_async_context(c)
			for c in self._lookups + self._direct_connections
		))
		return self

	async def __aexit__(self, *args):
		await self._stack.__aexit__(*args)
		del self._stack
		del self._queue

	async def __aiter__(self):
		while True:
			msg, exc = await self._queue.get()
			if exc is not None:
				raise exc
			yield msg


class SingleMessageReader:
	def __init__(self, **kwargs):
		self._reader = Reader(max_in_flight=0, **kwargs)

	async def __aenter__(self):
		self._queue = asyncio.Queue()
		await self._reader.__aenter__()

		self._ready = False

		coro = self._read()
		self._read_task = asyncio.get_event_loop().create_task(coro)

		return self

	async def __aexit__(self, *args):
		self._read_task.cancel()
		try: await self._read_task
		except asyncio.CancelledError: pass
		del self._read_task

		await self._reader.__aexit__(*args)
		self._reader = None

		del self._queue

	async def _read(self):
		async for msg in self._reader:
			if self._ready:
				self._ready = False
				await self._set_rdy(0)
				await self._queue.put(msg)
			else:
				# refuse all new messages that might come through while we are handling another
				# (race condition where two servers send messages at the same time)
				await msg.req()

	def _connections(self):
		yield from self._reader._direct_connections
		for lookup in self._reader._lookups:
			yield from lookup._connections.values()

	async def _set_rdy(self, n):
		await asyncio.wait([c._cmd(f'RDY {n}') for c in self._connections()])

	async def __aiter__(self):
		while True:
			# notify that we are ready again
			await self._set_rdy(1)
			self._ready = True
			msg = await self._queue.get()
			yield msg


class Message:
	def __init__(self, connection, data):
		self._connection = connection

		ts, = struct.unpack('>q', data[:8])
		self.ts = datetime.datetime.fromtimestamp(ts / 1000 / 1000 / 1000, tz=datetime.timezone.utc)
		self.attempts, = struct.unpack('>h', data[8:10])
		self.mid = data[10:26].decode('utf-8')
		self.body = data[26:]

		self._keepalive = _compat.create_task(self._keepalive_task())

	async def fin(self):
		try:
			await self._connection._cmd(f'FIN {self.mid}')
		finally:
			await self._drop()

	async def req(self, timeout=0, _inflight=True):
		try:
			await self._connection._cmd(f'REQ {self.mid} {timeout}')
		finally:
			await self._drop()

	async def _drop(self):
		del self._connection._inflight[self.mid]
		self._keepalive.cancel()
		try: await self._keepalive
		except asyncio.CancelledError: pass

	@property
	def nsqd_tcp_address(self):
		return '{}:{}'.format(*self._connection._addr)

	async def _keepalive_task(self):
		while True:
			await asyncio.sleep(self._connection._message_keepalive)
			await self._connection._cmd(f'TOUCH {self.mid}')

	def __repr__(self):
		return f'<lightbringer.Message mid:{self.mid}, ts:{self.ts.isoformat()}, attempts:{self.attempts} body:{self.body}>'
