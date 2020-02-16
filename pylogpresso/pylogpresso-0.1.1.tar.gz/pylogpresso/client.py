import os
import traceback
import sys
import threading
from enum import Enum

# logpresso modules
from .session import Session, LogpressoError
from .query import Query

class Cursor:
	def __init__(self, client, query_id: int, offset: int , limit: int, remove_on_close = True, fetch_unit = 10000):
		self.__client = client
		self.__query_id = query_id
		self.__offset = offset
		self.__limit = limit
		self.__remove_on_close = remove_on_close
		self.__p = offset
		self.__cached = None
		self.__current_cache_offset = None
		self.__next_cache_offset = offset
		self.__fetch_unit = fetch_unit
		self.__prefetch = None

	def __iter__(self):
		return self

	def __next__(self):
		if not self.__has_next():
			raise StopIteration

		item = self.__prefetch
		self.__prefetch = None
		return item

	def __has_next(self):
		if self.__prefetch != None:
			return True

		if (self.__p < self.__offset) or (self.__p > self.__offset + self.__limit):
			return False

		try:
			if self.__cached == None or self.__p >= self.__current_cache_offset + self.__fetch_unit:
				self.__cached = self.__client.get_result(self.__query_id, self.__next_cache_offset, self.__fetch_unit)
				self.__current_cache_offset = self.__next_cache_offset
				self.__next_cache_offset += self.__fetch_unit

			relative = self.__p - self.__current_cache_offset
			l = self.__cached.get('result')
			if relative >= len(l):
				return False

			self.__prefetch = l[relative]
			self.__p += 1
			return True

		except Exception as e:
			print('exception {}'.format(str(e)))
			return False

class LogpressoClient:
	def __init__(self):
		self.__session = None
		self.__queries = {}

	def connect(self, host, port, login_name: str, password: str, secure = False):
		self.__session = Session(host, port, secure)
		self.__session.login(login_name, password)
		self.__session.add_callback(self.on_trap)

	def close(self):
		if self.__session != None:
			self.__session.remove_callback(self.on_trap)
			self.__session.close()

	def query(self, query_string):
		query_id = self.create_query(query_string)
		self.start_query(query_id)
		q = self.__queries[query_id]
		q.wait()
		if q.status == 'Cancelled':
			raise LogpressoError('query cancelled')

		total = q.loaded_count
		return Cursor(self, query_id, 0, total)

	def create_query(self, query_string):
		params = {}
		params['query'] = query_string
		params['source'] = 'python-client'
		resp = self.rpc('org.araqne.logdb.msgbus.LogQueryPlugin.createQuery', params, 0)
		id = resp.params['id']
		self.__session.register_trap('logdb-query-' + str(id))

		q = Query()
		q.id = id
		q.query_string = query_string
		self.__queries[id] = q
		return id

	def start_query(self, query_id):
		params = {}
		params['id'] = query_id
		self.rpc('org.araqne.logdb.msgbus.LogQueryPlugin.startQuery', params, 0)

	def stop_query(self, query_id):
		params = {}
		params['id'] = query_id
		self.rpc('org.araqne.logdb.msgbus.LogQueryPlugin.stopQuery', params, 0)

	def remove_query(self, query_id):
		self.__session.unregister_trap('logdb-query-' + str(query_id))

		params = {}
		params['id'] = query_id
		self.rpc('org.araqne.logdb.msgbus.LogQueryPlugin.removeQuery', params, 0)

		self.__queries.pop(query_id, None)

	def get_queries(self):
		resp = self.rpc('org.araqne.logdb.msgbus.LogQueryPlugin.queries', {}, 0)
		queries = []
		for o in resp.params['queries']:
			q = self.__parse_query(o)
			queries.append(q)

		return queries

	def __parse_query(self, o):
		q = Query()
		q.id = o.get('id')
		q.query_string = o.get('query_string')
		q.source = o.get('source')
		q.login_name = o.get('login_name')
		q.remote_ip = o.get('remote_ip')
		q.background = o.get('background')
		q.elapsed = o.get('elapsed')

		stamp = o.get('stamp')
		q.update_count(o.get('rows'), stamp)

		end = o.get('is_end')
		eof = end
		if 'is_eof' in o:
			eof = o.get('is_eof')
		
		cancelled = False
		if 'is_cancelled' in o:
			cancelled = o.get('is_cancelled')

		if eof:
			if cancelled:
				q.update_status('Cancelled', stamp)
			else:
				q.update_status('Ended', stamp)
		elif end:
			q.update_status('Stopped', stamp)
		else:
			q.update_status('Running', stamp)

		return q

	def get_result(self, query_id, offset, limit):
		params = {}
		params['id'] = query_id
		params['offset'] = offset
		params['limit'] = limit
		# todo: params.put['binary_encode'] = true

		resp = self.rpc('org.araqne.logdb.msgbus.LogQueryPlugin.getResult', params, 0)
		if len(resp.params) == 0:
			raise LogpressoError('query-not-found')

		return resp.params

	def rpc(self, method, params, timeout):
		return self.__session.rpc(method, params, timeout)

	def on_trap(self, msg):
		method = msg.method

		if method.startswith('logdb-query-'):
			query_id = msg.params.get('id')
			q = self.__queries[query_id]
			self.__update_query_status(q, msg)
		else:
			print('unsupported trap: ' + str(msg))
		
	def __update_query_status(self, query, msg):
		msg_type = msg.params.get('type')
		stamp = 0
		if 'stamp' in msg.params:
			stamp = msg.params.get('stamp')

		if msg_type == 'eof':
			count = msg.params.get('total_count')
			query.update_count(count, stamp)

			cancel_reason = msg.params.get('cancel_reason')
			if cancel_reason != None and cancel_reason != 'PARTIAL_FETCH':
				query.cancel_reason = cancel_reason
				query.error_code = msg.params.get('error_code')
				query.error_detail = msg.params.get('error_detail')
				query.update_status('Cancelled', stamp)
			else:
				query.update_status('Ended', stamp)
		elif msg_type == 'status_change':
			count = msg.params.get('count')
			status = msg.params.get('status')
			query.update_count(count, stamp)
			query.update_status(status, stamp)

		query.stamp = stamp
