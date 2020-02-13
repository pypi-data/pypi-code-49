"Module containing functions to obtain Teradata cursor"

__author__ = "Paresh Adhia"
__copyright__ = "Copyright 2016-2019 Paresh Adhia"

from typing import Optional
import xml.etree.ElementTree as ET
from .util import Ident

try:
	from tdconn_site import *
except ImportError:
	from .tdconn_default import *

conn = None # The first (and usually the only) connection object
csr = None  # The latest (and usually the only) cursor object

class Cursor:
	"Cursor wrapper class with some useful attributes"
	def __init__(self, base_csr, _conn):
		self.csr = base_csr
		self._conn = _conn

	@property
	def connection(self):
		"Connectionion object which created this cursor object"
		return self._conn

	@property
	def version(self) -> str:
		"return database version string"
		return self.connection.version

	def _builtin(self, fn):
		"built-in function"
		self.execute('select ' + fn)
		return self.fetchone()[0]

	@property
	def schema(self) -> str:
		"Current DATABASE"
		self.execute('select database')
		return self.fetchone()[0]

	@schema.setter
	def schema(self, new_schema: str) -> None:
		self.execute('database ' + new_schema)
		self.connection.commit()

	def fetchxml(self) -> str:
		"returns cleansed XML value from the first column of the result-set"
		import re

		val, more = '', True
		while more:
			val += ''.join(r[0] for r in self.fetchall())
			more = self.nextset()

		return re.sub('xmlns=".*?"', '', re.sub('encoding="UTF-16"', 'encoding="utf-8"', val, 1, flags=re.IGNORECASE), 1)

	def get_xmldef(self, kind: str, sch: str, name: str) -> ET.Element:
		"returns XML definition for a table or a view"

		obj_name = Ident.__format__(name, 'q')
		if sch:
			obj_name = Ident.__format__(sch, 'q') + "." + obj_name

		self.execute(f'SHOW IN XML {kind} {obj_name}')

		return ET.fromstring(self.fetchxml())[0]

	def __iter__(self):
		return self.csr.__iter__()

	def __enter__(self, *args, **kwargs):
		return self

	def __exit__(self, *args, **kwargs):
		return self.csr.__exit__(*args, **kwargs)

	def __getattr__(self, attr):
		if attr in ['current_user', 'current_date', 'current_role', 'current_time', 'current_timestamp', 'session', 'user']:
			return self._builtin(attr)
		return getattr(self.csr, attr)

class Connection:
	"Connection wrapper that provisions Cursor and commits before connection closes"
	def __init__(self, base_conn):
		self._conn = base_conn
		self._version: Optional[str] = None

	def cursor(self) -> Cursor:
		"returns an Cursor instance"
		return Cursor(self._conn.cursor(), self)

	@property
	def version(self) -> str:
		"Teradata database version"
		if self._version is None:
			with self.cursor() as csr:
				csr.execute("Select InfoData From DBC.DBCInfoV Where InfoKey = 'VERSION'")
				self._version = csr.fetchone()[0]

		return self._version

	def close(self) -> None:
		"commit and close the connection"
		self._conn.commit()
		self._conn.close()

	def __enter__(self, *args, **kwargs):
		return self

	def __exit__(self, *args, **kwargs):
		self.close()

	def __getattr__(self, attr):
		return getattr(self._conn, attr)

def connect(*args, **kargs) -> Connection:
	"return a datbase connection object"
	return Connection(dbconnect(*args, **kargs))

def cursor(*args, **kargs) -> Cursor:
	"return a new cursor object using the global connection object, and also save it as the global cursor object"
	global conn, csr

	if not conn:
		import atexit
		conn = connect(*args, **kargs)
		atexit.register(conn.close)

	csr = conn.cursor()

	return csr

def commit() -> None:
	"commit using the global connection object"
	conn.commit()
