from enum import Enum
import sys
import socket
import uuid
import json
import traceback
import threading

# logpresso modules
from .websocket import WebSocket

class MessageType(Enum):
	UNKNOWN = 0,
	REQUEST = 1,
	RESPONSE = 2,
	TRAP = 3

	def __str__(self):
		return self.name[0] + self.name.lower()[1:]

class Message:
	def __init__(self):
		self.__guid = str(uuid.uuid4())
		self.__type = MessageType.REQUEST
		self.__session = None
		self.__request_id = None
		self.__method = None
		self.__params = {}
		self.__source = '0'
		self.__target = '0'
		self.__error_code = None
		self.__error_msg = None

	def encode(self):
		header = {}
		header['guid'] = str(self.guid)
		header['type'] = str(self.type)
		header['method'] = self.method
		header['session'] = self.session
		header['source'] = self.source
		header['target'] = self.target
		return json.dumps([header, self.params])

	@property
	def guid(self):
		return self.__guid

	@guid.setter
	def guid(self, guid):
		self.__guid = guid

	@property
	def type(self):
		return self.__type

	@type.setter
	def type(self, type):
		self.__type = type

	@property
	def session(self):
		return self.__session

	@session.setter
	def session(self, session):
		self.__session = session

	@property
	def request_id(self):
		return self.__request_id

	@request_id.setter
	def request_id(self, request_id):
		self.__request_id = request_id
	
	@property
	def source(self):
		return self.__source

	@source.setter
	def source(self, source):
		self.__source = source

	@property
	def target(self):
		return self.__target

	@target.setter
	def target(self, target):
		self.__target = target

	@property
	def method(self):
		return self.__method

	@method.setter
	def method(self, method):
		self.__method = method

	@property
	def params(self):
		return self.__params

	@params.setter
	def params(self, params):
		self.__params = params

	@property
	def error_code(self):
		return self.__error_code

	@error_code.setter
	def error_code(self, error_code):
		self.__error_code = error_code

	@property
	def error_msg(self):
		return self.__error_msg

	@error_msg.setter
	def error_msg(self, error_msg):
		self.__error_msg = error_msg

	def __str__(self):
		return str(self.type) + ' ' + str(self.method) + ' ' + str(self.params)

class LogpressoError(Exception):

	def __init__(self, error_code, error_msg):
		self.__error_code = error_code
		self.__error_msg = error_msg

	@property
	def error_code(self):
		return self.__error_code

	@property
	def error_msg(self):
		return self.__error_msg

class WaitingCall:
	def __init__(self, guid):
		self.__guid = guid
		self.__done = threading.Event()

	@property
	def result(self):
		return self.__result

	def done(self, result: Message):
		self.__result = result
		self.__done.set()

	def wait(self):
		self.__done.wait()

class Session:
	def __init__(self, host: str, port: int, secure: bool):
		self.__calls = {}
		self.__callbacks = []
		scheme = 'wss://' if secure else 'ws://'
		self.__endpoint = scheme + host + ':' + str(port) + '/websocket'
		self.__websocket = WebSocket(self.__endpoint)
		self.__websocket.add_msg_callback(self.on_message)
		self.__websocket.add_error_callback(self.on_error)
		self.__websocket.add_close_callback(self.on_close)
		self.__websocket.connect()

	def close(self):
		self.__websocket.close()
		self.__websocket.remove_close_callback(self.on_close)
		self.__websocket.remove_error_callback(self.on_error)
		self.__websocket.remove_msg_callback(self.on_message)

	def add_callback(self, callback):
		self.__callbacks.append(callback)

	def remove_callback(self, callback):
		self.__callbacks.remove(callback)

	def login(self, login_name: str, password: str, timeout:int = 10):
		params = {}
		params['login_name'] = login_name
		params['password'] = password
		params['use_error_return'] = True

		resp = self.rpc('org.araqne.logdb.msgbus.ManagementPlugin.login', params, timeout)
		if 'error_code' in resp.params:
			raise RuntimeError(resp.error_code)

	def register_trap(self, callback_name):
		params = {}
		params['callback'] = callback_name
		self.rpc('org.araqne.msgbus.PushPlugin.subscribe', params, 0)

	def unregister_trap(self, callback_name):
		params = {}
		params['callback'] = callback_name
		self.rpc('org.araqne.msgbus.PushPlugin.unsubscribe', params, 0)

	def on_message(self, text: str):
		objs = json.loads(text)
		header = objs[0]
		params = objs[1]
		
		msg_type = header['type']

		msg = Message()
		msg.guid = header['guid']
		msg.method = header['method']
		msg.session = header['session']
		msg.source = header['source']
		msg.target = header['target']

		msg.request_id = header.get('requestId')
		msg.error_code = header.get('errorCode')
		msg.error_msg = header.get('errorMessage')

		msg.params = params

		if msg_type == 'Response':
			msg.type = MessageType.RESPONSE
			call = self.__calls[msg.request_id]
			if call != None:
				call.done(msg)

		elif msg_type == 'Trap':
			msg.type = MessageType.TRAP

			for callback in self.__callbacks:
				try:
					callback(msg)
				except:
					traceback.print_exc(file=sys.stdout)

	def on_error(self, error):
		pass

	def on_close(self, error = None):
		pass

	def rpc(self, method, params, timeout):
		req = Message()
		req.method = method
		req.params = params
		return self.__rpc(req, timeout)

	def __rpc(self, msg: Message, timeout: int):
		json = msg.encode()

		call = WaitingCall(msg.guid)
		self.__calls[msg.guid] = call
		self.__websocket.send(json)
		call.wait()

		result = call.result
		
		if result.error_code != None:
			raise LogpressoError(result.error_code, result.error_msg)

		return call.result
