import threading

class Query:
	def __init__(self):
		self.__id = 0
		self.__query_string = None
		self.__source = None
		self.__login_name = None
		self.__remote_ip = None
		self.__status = None
		self.__loaded_count = 0
		self.__background = False
		self.__stamp = 0
		self.__start_time = None
		self.__finish_time = None
		self.__error_code = None
		self.__error_detail = None
		self.__cancel_reason = None
		self.__elapsed = None
		self.__commands = []
		self.__done = threading.Event()

	def wait(self):
		self.__done.wait()

	def update_count(self, loaded_count, stamp):
		if self.__stamp == None or stamp > self.__stamp:
			self.__loaded_count = loaded_count

	def update_status(self, status, stamp):
		if stamp != 0 and self.__stamp >= stamp:
			return

		self.__status = status
		if status == 'Ended' or status == 'Cancelled':
			self.__done.set()

	@property
	def id(self):
		return self.__id

	@id.setter
	def id(self, id):
		self.__id = id

	@property
	def query_string(self):
		return self.__query_string
	
	@query_string.setter
	def query_string(self, query_string):
		self.__query_string = query_string

	@property
	def source(self):
		return self.__source

	@source.setter
	def source(self, source):
		self.__source = source
	
	@property
	def login_name(self):
		return self.__login_name

	@login_name.setter
	def login_name(self, login_name):
		self.__login_name = login_name

	@property
	def remote_ip(self):
		return self.__remote_ip

	@remote_ip.setter
	def remote_ip(self, remote_ip):
		self.__remote_ip = remote_ip

	@property
	def status(self):
		return self.__status

	@property
	def loaded_count(self):
		return self.__loaded_count
	
	@property
	def background(self):
		return self.__background

	@background.setter
	def background(self, background):
		self.__background = background

	@property
	def stamp(self):
		return self.__stamp

	@stamp.setter
	def stamp(self, stamp):
		self.__stamp = stamp

	@property
	def start_time(self):
		return self.__start_time

	@start_time.setter
	def start_time(self, start_time):
		self.__start_time = start_time

	@property
	def finish_time(self):
		return self.__finish_time

	@finish_time.setter
	def finish_time(self, finish_time):
		self.__finish_time = finish_time

	@property
	def error_code(self):
		return self.__error_code

	@error_code.setter
	def error_code(self, error_code):
		self.__error_code = error_code

	@property
	def error_detail(self):
		return self.__error_detail

	@error_detail.setter
	def error_detail(self, error_detail):
		self.__error_detail = error_detail

	@property
	def cancel_reason(self):
		return self.__cancel_reason

	@cancel_reason.setter
	def cancel_reason(self, cancel_reason):
		self.__cancel_reason = cancel_reason

	@property
	def elapsed(self):
		return self.__elapsed

	@elapsed.setter
	def elapsed(self, elapsed):
		self.__elapsed = elapsed

	def __str__(self):
		return 'id={}, query={}, status={}, loaded={}, login={}, remote={}, source={}'.format(
			self.id, self.query_string, self.status, self.loaded_count, self.login_name, self.remote_ip, self.source)
