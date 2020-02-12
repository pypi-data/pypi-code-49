import asyncio
import json
import logging
import re
import socket
import struct
import sys

from . import _compat


logger = logging.getLogger(__name__)
mitm_logger = logging.getLogger(__name__ + '.mitm')


class NsqError(Exception):
	pass

class InvalidTopicName(Exception):
	pass

class ConnectionDropped(Exception):
	pass


class ReadTask:
	def __init__(self, reader, on_message, on_response, on_error):
		self.reader = reader
		self.on_error = on_error
		self.on_message = on_message
		self.on_response = on_response
		self.task = _compat.create_task(self.run_safe())

	async def run(self):
		re = self.reader.readexactly
		while True:
			sizeb = await re(4)
			size, = struct.unpack('>l', sizeb)

			ftb = await re(4)
			ft, = struct.unpack('>l', ftb)

			data = await re(size - 4)
			mitm_logger.debug('Read: %r', sizeb + ftb + data)

			if ft == 0:
				await self.on_response(data)
			elif ft == 1:
				self.on_error(NsqError(data.decode('utf-8')))
			elif ft == 2:
				await self.on_message(data)
			else: # pragma: no cover
				raise NotImplementedError()

	async def run_safe(self):
		# this should not be able to crash
		try:
			await self.run()
		except asyncio.CancelledError:
			pass
		except asyncio.IncompleteReadError:
			self.on_error(ConnectionDropped('Read task closed'))
		except Exception as exc:
			self.on_error(exc)

	async def cancel(self):
		self.task.cancel()
		await self.task
		del self.task


class Connection:
	def __init__(self, addr, identify_opts=None):
		self._addr = addr

		identify_opts = identify_opts or {}
		identify_opts['feature_negotiation'] = False
		identify_opts.setdefault('user_agent', 'lightbringer')
		hostname = socket.gethostname()
		identify_opts.setdefault('client_id', hostname)
		identify_opts.setdefault('hostname', hostname.split('.', 1)[0])
		self._identify_body = json.dumps(identify_opts).encode('utf-8')
		self._cmd_lock = asyncio.Lock()

	async def __aenter__(self):
		try:
			await self._setup()
		except Exception:
			await self.__aexit__(*sys.exc_info())
			raise
		return self

	async def __aexit__(self, *_):
		if hasattr(self, '_read_task'):
			t = self._read_task
			del self._read_task
			await t.cancel()

		if hasattr(self, '_writer'):
			w = self._writer
			del self._writer
			del self._reader
			w.close()
			# todo py3.7
			#await w.wait_closed()

	async def _setup(self):
		self._reader, self._writer = await asyncio.open_connection(*self._addr)

		self._read_task = ReadTask(
			self._reader,
			self.on_message,
			self._on_response,
			self._on_error,
		)

		self._writer.write(b'  V2')
		await self._ack_cmd('IDENTIFY', body=self._identify_body)

	async def _cmd(self, cmd, body=None):
		msg = cmd.encode('utf-8') + b'\n'
		if body:
			msg += struct.pack('>l', len(body)) + body
		mitm_logger.debug('Write: %r', msg)
		self._writer.write(msg)
		try:
			await self._writer.drain()
		except (OSError, ConnectionError):
			raise ConnectionDropped('Writer drain raised')

	async def _ack_cmd(self, *args, expected=b'OK', **kwargs):
		async with self._cmd_lock:
			self._response_fut = asyncio.get_event_loop().create_future()
			try:
				await self._cmd(*args, **kwargs)
				res = await self._response_fut
				if res != expected:
					raise NsqError(f'Unexpected response from the nsqd: expected {expected}, got {res}')
			finally:
				del self._response_fut

	async def on_message(self, msg): # pragma: no cover
		raise NotImplementedError()

	def on_error(self, exc): # pragma: no cover
		raise NotImplementedError()

	async def _on_response(self, data):
		if data == b'_heartbeat_':
			await self._cmd('NOP')
		else:
			self._response_fut.set_result(data)

	def _on_error(self, exc):
		if hasattr(self, '_response_fut') and not self._response_fut.done():
			self._response_fut.set_exception(exc)
			self._response_fut.exception()
		else:
			self.on_error(exc)


def validate_topic_name(name):
	if len(name) >= 65:
		raise InvalidTopicName()
	if not re.match(r'^[\.a-zA-Z0-9_-]+(#ephemeral)?$', name):
		raise InvalidTopicName()
