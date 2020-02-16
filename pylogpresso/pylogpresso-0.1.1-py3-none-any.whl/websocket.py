from enum import Enum
import os
import sys
import socket
import base64
import hashlib
import threading
import traceback

class WebSocketFrameType(Enum):
	CONTINUATION = 0
	TEXT = 1
	BINARY = 2
	CLOSE = 8
	PING = 9
	PONG = 10

class WebSocketFrame:

	def __init__(self, text):
		self.__fin = True
		self.__mask = True
		self.__frame_type = WebSocketFrameType.TEXT
		self.__mask_key = os.urandom(4)
		self.__payload = text.encode('utf-8')

	def encode(self):
		size = len(self.__payload)
		mask_len = 4 if self.__mask else 0
		header_len = 0

		buf = None
		if size <= 125:
			header_len = 2
			frame_size = header_len + mask_len + size
			buf = bytearray(frame_size)
			buf[0] = self.__frame_type
			if self.__fin:
				buf[0] |= 0x80

			buf[1] = (size | 0x80) if self.__mask else size

			pass
		elif size <= 65535:
			header_len = 4
			frame_size = header_len + mask_len + size

			buf = bytearray(frame_size)
			buf[0] = self.__frame_type.value
			if self.__fin:
				buf[0] |= 0x80

			buf[1] = (126 | 0x80) if self.__mask else 126
			buf[2] = (size >> 8) & 0xff
			buf[3] = size & 0xff
			pass
		else:
			header_len = 10
			frame_size = header_len + mask_len + size
			buf = bytearray(frame_size)
			buf[0] = self.__frame_type
			if self.__fin:
				buf[0] |= 0x80

			buf[1] = (127 | 0x80) if self.__mask else 127
			buf[2] = buf[3] = buf[4] = buf[5] = 0
			buf[6] = (size >> 24) & 0xff
			buf[7] = (size >> 16) & 0xff
			buf[8] = (size >> 8) & 0xff
			buf[9] = size & 0xff
			pass

		if self.__mask:
			buf[header_len:header_len + mask_len] = self.__mask_key
			base = header_len + mask_len

			for i in range(size):
				buf[base + i] = self.__payload[i] ^ (self.__mask_key[i % 4])
		
		else:
			buf[header_len:] = self.__payload

		return buf

class WebSocket:
	def __init__(self, url):
		self.__closed = None
		self.__closing = None
		self.__msg_callbacks = []
		self.__error_callbacks = []
		self.__close_callbacks = []
		self.__url = url
		if not url.startswith('ws://') and not url.startswith('wss://'):
			raise ValueError('url should starts with ws:// or wss:// scheme')
		
		(self.__host, self.__port) = self.__get_addr(url)
	
	def __get_addr(self, url):
		b = url.find('://') + len('://')
		e = url.find('/', b)
		e = len(url) if e < 0 else e
		addr = url[b:e]
		t = addr.split(':')
		host = t[0]
		port = 80 if url.startswith('ws://') else 443
		if len(t) == 2:
			port = int(t[1])

		return (host, port)

	def add_msg_callback(self, callback):
		self.__msg_callbacks.append(callback)

	def remove_msg_callback(self, callback):
		self.__msg_callbacks.remove(callback)

	def add_error_callback(self, callback):
		self.__error_callbacks.append(callback)

	def remove_error_callback(self, callback):
		self.__error_callbacks.remove(callback)

	def add_close_callback(self, callback):
		self.__close_callbacks.append(callback)

	def remove_close_callback(self, callback):
		self.__close_callbacks.remove(callback)

	def send(self, text):
		frame = WebSocketFrame(text)
		self.__sock.send(frame.encode())
		pass

	def connect(self):
		self.__sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.__sock.connect((self.__host, self.__port))
		self.__sock.settimeout(1)

		websocket_key = self.__new_websocket_key()
		handshake = self.__new_handshake_request(self.__host, websocket_key)
		self.__sock.send(handshake.encode())

		resp = ''
		while True:
			try:
				buf = self.__sock.recv(8192)
				if len(buf) == 0:
					break

				resp += buf.decode('utf-8')
				if resp.find('\r\n\r\n') > 0:
					break
			except socket.timeout:
				pass

		if not resp.startswith('HTTP/1.1 101 '):
			raise RuntimeError('websocket not supported')

		headers = {}
		for line in resp.split('\r\n'):
			p = line.find(':')
			if p < 0:
				continue

			key = line[0:p].strip().lower()
			val = line[p + 1:].strip()
			headers[key] = val

		upgrade = headers['upgrade']
		connection = headers['connection']
		accept = headers['sec-websocket-accept']

		if upgrade.lower() != 'websocket':
			raise RuntimeError('Unexpected Upgrade header: ' + upgrade)

		if connection.lower() != 'upgrade':
			raise RuntimeError('Unexpected Connection header: ' + connection)

		calculated = self.__calculate_accept_key(websocket_key)
		if calculated != accept:
			raise RuntimeError('Unexpected Sec-WebSocket-Accept header: ' + accept)

		self.__closing = False
		self.__thread = threading.Thread(target=self.__receiver, daemon=True)
		self.__thread.start()

	def close(self):
		self.__closing = True
		self.__closed.wait()
		pass

	def __receiver(self):
		error = None
		while not self.__closing:
			try:
				self.__recv()
			except socket.timeout:
				pass
			except Exception as e:
				error = e
				traceback.print_exc(file=sys.stdout)
				pass

		self.__sock.close()

		for callback in self.__close_callbacks:
			try:
				callback(error)
			except:
				pass

		self.__closed.set()

		print('receiver terminated')

	def __recv(self):
		header = self.__ensure_read(2)
		fin = (header[0] & 0x80) == 0x80
		opcode = header[0] & 0x0f
		mask = (header[1] & 0x80) == 0x80

		size = header[1] & 0x7f

		payload_size = 0
		if size < 126:
			payload_size = size
		elif size == 126:
			size_buf = self.__ensure_read(2)
			payload_size = (size_buf[0] & 0xff) << 8 | (size_buf[1] & 0xff)
		elif size == 127:
			size_buf = self.__ensure_read(8)
			payload_size = (size_buf[0] & 0xff) << 56 | (size_buf[1] & 0xff) << 48 | (size_buf[2] & 0xff) << 40 | (size_buf[3] & 0xff) << 32 \
				| (size_buf[4] & 0xff) << 24 | (size_buf[5] & 0xff) << 16 | (size_buf[6] & 0xff) << 8 | (size_buf[7] & 0xff)

		payload = self.__ensure_read(payload_size)
		text = payload.decode('utf-8')

		if not text.endswith(']'):
			print('payload size {}, text <{}>'.format(payload_size, text))
			sys.exit(-1)

		for callback in self.__msg_callbacks:
			callback(text)

	def __ensure_read(self, size):
		buf = bytearray(size)
		view = memoryview(buf)
		while size:
			n = self.__sock.recv_into(view, size)
			view = view[n:]
			size -= n

		return buf

	def __calculate_accept_key(self, websocket_key):
		key = websocket_key + '258EAFA5-E914-47DA-95CA-C5AB0DC85B11'
		h = hashlib.sha1()
		h.update(key.encode('utf-8'))
		return base64.b64encode(h.digest()).decode('utf-8')

	def __new_websocket_key(self):
		return base64.b64encode(os.urandom(16)).decode('utf-8')

	def __new_handshake_request(self, host, websocket_key):
		return 'GET /websocket HTTP/1.1\r\n' \
			'Host: ' + host + '\r\n' \
			'Upgrade: websocket\r\n' \
			'Connection: Upgrade\r\n' \
			'Sec-WebSocket-Key: ' + websocket_key + '\r\n' \
			'Sec-WebSocket-Version: 13\r\n' \
			'Content-Length: 0\r\n\r\n'
