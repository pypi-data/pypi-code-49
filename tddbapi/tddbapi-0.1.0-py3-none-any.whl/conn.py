"DB API connect method"

from teradatasql import TeradataConnection, TeradataCursor
from .excp import fix_excp
from .data import fix_data

class TDDBApiConnection(TeradataConnection):
	"Customize class with overriden connection parmeters and cursor method"
	def __init__(self, *args, **kwargs):
		kwargs["fake_result_sets"] = "true"
		super().__init__(*args, **kwargs)

	def cursor(self):
		"Return overriden cursor object"
		return TDDBApiCursor(self)

	close = fix_excp(TeradataConnection.close)

	__enter__ = TeradataConnection.__enter__
	__exit__ = TeradataConnection.__exit__

@fix_excp
def connect(*args, **kwargs):
	"Return connection object with overriden methods"
	return TDDBApiConnection(*args, **kwargs)

@fix_data
class TDDBApiCursor(TeradataCursor):
	"Cursor object that modifies data and exception types"
	nextset = fix_excp(TeradataCursor.nextset)
	close = fix_excp(TeradataCursor.close)
	executemany = fix_excp(TeradataCursor.executemany)

	__iter__ = TeradataCursor.__iter__
	__next__ = fix_excp(TeradataCursor.__next__)
	__enter__ = TeradataCursor.__enter__
	__exit__ = TeradataCursor.__exit__
