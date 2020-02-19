import aiohttp
import asyncio
import datetime
import functools
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
		message_keepalive: int = 30, # should be bellow the nsqd --message-timeout (default 60)
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

	async def rdy(self, n):
		return await self._cmd(f'RDY {n}')

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
			async def cleanup(msg):
				try:
					await msg.req()
				except (OSError, ConnectionError, ConnectionDropped):
					pass
			await asyncio.gather(*(cleanup(msg) for msg in self._inflight.values()))
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


class LookupsManager:
	def __init__(self, addrs, topic, refresh_interval, conn_args):
		self._addrs = addrs
		self._topic = topic
		self._refresh_interval = refresh_interval
		self._conn_args = conn_args

	async def __aenter__(self):
		if not self._addrs:
			return

		self._session = aiohttp.ClientSession()
		await self._session.__aenter__()

		self._connections = {}
		await self._refresh()
		coro = self._refresh_periodic()
		self._refresh_task = _compat.create_task(coro)

	async def __aexit__(self, *args):
		if not self._addrs:
			return

		self._refresh_task.cancel()
		try: await self._refresh_task
		except asyncio.CancelledError: pass
		del self._refresh_task

		await self._session.__aexit__(*args)
		del self._session

		await asyncio.gather(*(c.__aexit__(*args) for c in self._connections.values()))
		del self._connections

	async def rdy(self, n):
		if not self._addrs:
			return
		self._conn_args['max_in_flight'] = n
		await asyncio.wait([c.rdy(n) for c in self._connections.values()])

	async def _on_unclean_exit(self, conn, exc):
		if conn._addr in self._connections:
			del self._connections[conn._addr]
			if not self._connections:
				logger.warning(f'Dropped last connection to %s in %r: {exc!r}', conn._addr, self)

	async def _fetch_lookup(self, addr):
		async with self._session.get(f'{addr}/lookup', params={'topic': self._topic}) as resp:
			if resp.status == 404:
				return set()

			resp.raise_for_status()
			r = await resp.json()

		return {(
			o.get('broadcast_address', o.get('address')),
			o['tcp_port'],
		) for o in r['producers']}

	async def _refresh(self):
		news = await asyncio.gather(*(self._fetch_lookup(a) for a in self._addrs))
		new = functools.reduce(lambda a, b: a | b, news, set())
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
				logger.error(f'Error connecting to %s in %r: {exc!r}', addr, self)
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
				logger.error(f'Failed refreshing %r: {exc!r}', self)
			await asyncio.sleep(self._refresh_interval)

	def __repr__(self):
		addrs = ', '.join(self._addrs)
		return f'<lightbringer.reader.LookupsManager {addrs}>'


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

		self._managers = [
			LookupsManager(
				self._lookupd_http_addresses,
				self._topic,
				self._lookupd_refresh_interval,
				conn_args,
			),
			*(
				DirectConnection(a, _on_unclean_exit=self._direct_conn_unclean_exit, **conn_args)
				for a in self._nsqd_tcp_addresses
			),
		]
		await asyncio.gather(*(self._stack.enter_async_context(c) for c in self._managers))
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

	async def _set_rdy(self, n):
		await asyncio.wait([m.rdy(n) for m in self._reader._managers])

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
		self._connection_addr = connection._addr

		ts, = struct.unpack('>q', data[:8])
		self.ts = datetime.datetime.fromtimestamp(ts / 1000 / 1000 / 1000, tz=datetime.timezone.utc)
		self.attempts, = struct.unpack('>h', data[8:10])
		self.mid = data[10:26].decode('utf-8')
		self.body = data[26:]

		self._keepalive = _compat.create_task(self._keepalive_task())

	async def fin(self):
		conn, ka = self._drop()
		await conn._cmd(f'FIN {self.mid}')
		try: await ka
		except asyncio.CancelledError: pass

	async def req(self, timeout=0, _inflight=True):
		conn, ka = self._drop() # needs to be sync, to avoid race conditions
		await conn._cmd(f'REQ {self.mid} {timeout}')
		try: await ka
		except asyncio.CancelledError: pass

	def _drop(self):
		# do this first, to avoid race conditions
		conn, self._connection = self._connection, None
		if conn is None:
			raise ConnectionDropped()

		del conn._inflight[self.mid]

		ka = self._keepalive
		del self._keepalive
		ka.cancel()

		return conn, ka

	@property
	def nsqd_tcp_address(self):
		return '{}:{}'.format(*self._connection_addr)

	async def _keepalive_task(self):
		while True:
			await asyncio.sleep(self._connection._message_keepalive)
			await self._connection._cmd(f'TOUCH {self.mid}')

	def __repr__(self):
		return f'<lightbringer.Message mid:{self.mid}, ts:{self.ts.isoformat()}, attempts:{self.attempts} body:{self.body}>'
