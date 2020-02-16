import sys
import traceback
from .client import LogpressoClient

class Console:

	def __init__(self):
		self.__client = None

	def run(self):
		print('pylogpresso console')
		print('type "help" for more information')

		while True:
			line = input('logpresso> ')
			tokens = line.split(' ')

			cmd = tokens[0]
			if cmd == 'help':
				self.__help()
			elif cmd == 'connect':
				self.__connect(line)
			elif cmd == 'queries':
				self.__queries()
			elif cmd == 'query':
				self.__query(line)
			elif cmd == 'create_query':
				self.__create_query(line)
			elif cmd == 'start_query':
				self.__start_query(line)
			elif cmd == 'stop_query':
				self.__stop_query(line)
			elif cmd == 'remove_query':
				self.__remove_query(line)
			elif cmd == 'fetch':
				self.__fetch(line)
			else:
				print('invalid command: ' + cmd)

	def __help(self):
		print('connect <host:port> <login_name> <password>')
		print('\tconnect to specified logpresso instance')
		print('queries')
		print('\tprint all queries initiated by this session')
		print('query <query_string>')
		print('\tcreate, start and fetch query result at once')
		print('create_query <query_string>')
		print('\tcreate query with specified query string, and return allocated query id')
		print('start_query <query_id>')
		print('\tstart specified query')
		print('stop_query <query_id>')
		print('\tstop specified query')
		print('remove_query <query_id>')
		print('\tstop and remove specifeid query')
		print('fetch <query_id> <offset> <limit>')
		print('\tfetch result set of specified region. you can fetch partial result before query is finished')

	def __connect(self, line):
		try:
			tokens = line.split(' ')
			if len(tokens) < 4:
				print('Usage: connect <host:port> <loginname> [<password>]')
				return

			if self.__client != None:
				print('already connected')
				return

			addr = tokens[1].split(':')
			host = addr[0]
			port = 8888
			if len(addr) > 1:
				port = int(addr[1])

			login_name = tokens[2]
			password = tokens[3]

			self.__client = LogpressoClient()
			self.__client.connect(host, port, login_name, password)
			print('connected')
		except:
			traceback.print_exc(file=sys.stdout)

	def __queries(self):
		if self.__client == None:
			print('connect first please')
			return

		try:
			queries = self.__client.get_queries()
			for query in queries:
				print(str(query))
		except:
			traceback.print_exc(file=sys.stdout)

	def __create_query(self, line):
		if self.__client == None:
			print('connect first please')
			return

		try:
			line = line.strip()
			p = line.find(' ')
			query_string = line[p:].strip()
			query_id = self.__client.create_query(query_string)
			print('query id: ' + str(query_id))
		except:
			traceback.print_exc(file=sys.stdout)

	def __start_query(self, line):
		if self.__client == None:
			print('connect first please')
			return

		try:
			line = line.strip()
			query_id = int(line.split(' ')[1])
			self.__client.start_query(query_id)
			print('started query ' + str(query_id))
		except:
			traceback.print_exc(file=sys.stdout)

	def __stop_query(self, line):
		if self.__client == None:
			print('connect first please')
			return

		try:
			line = line.strip()
			query_id = int(line.split(' ')[1])
			self.__client.stop_query(query_id)
			print('stopped query ' + str(query_id))
		except:
			traceback.print_exc(file=sys.stdout)

	def __remove_query(self, line):
		if self.__client == None:
			print('connect first please')
			return

		try:
			line = line.strip()
			query_id = int(line.split(' ')[1])
			self.__client.remove_query(query_id)
			print('removed query ' + str(query_id))
		except:
			traceback.print_exc(file=sys.stdout)

	def __fetch(self, line):
		if self.__client == None:
			print('connect first please')
			return

		line = line.strip()
		tokens = line.split(' ')
		if len(tokens) < 4:
			print('Usage: fetch <query_id> <offset> <limit>')
			return

		try:
			query_id = int(tokens[1])
			offset = int(tokens[2])
			limit = int(tokens[3])

			page = self.__client.get_result(query_id, offset, limit)
			rows = page.get('result')
			for row in rows:
				print(row)
		except:
			traceback.print_exc(file=sys.stdout)
	
	def __query(self, line):
		if self.__client == None:
			print('connect first please')
			return

		line = line.strip()
		query_string = line[line.find(' '):].strip()

		try:
			print('querying [{}]...'.format(query_string))

			count = 0
			cursor = self.__client.query(query_string)
			for record in cursor:
				print(record)
				count += 1

			print('total {} rows'.format(count))
		except:
			traceback.print_exc(file=sys.stdout)

Console().run()
