"Teradata Database Object types"

__author__ = "Paresh Adhia"
__copyright__ = "Copyright 2016-2020, Paresh Adhia"

from typing import List, Optional, Callable, Mapping, Union
import xml.etree.ElementTree as ET
from textwrap import dedent

from cached_property import cached_property

from .util import getLogger, Ident
from .column import Column, ColMixin
from .index import Index

logger = getLogger(__name__)

XMLDefGetter = Callable[[str, str, str], ET.Element] # function that returns object definition as XML Doc

class XMLDefMixin:
	@cached_property
	def _xmldef(self) -> ET.Element:
		"""get XML definition for an object, either using registered function or default cursor"""
		if self.get_xmldef is None:
			raise RuntimeError('No get_xmldef() function has been registered')

		return self.get_xmldef(self._show_type, self.sch, self.name)

class DBObj:
	"A Database object that has schema and a name"
	_xml_type = None

	def __init__(self, sch: str, name: str, objtype: Optional[str] = None):
		self.sch, self.name, self.objtype = Ident(sch), Ident(name), objtype
		self.get_xmldef: Optional[XMLDefGetter] = None

	def __str__(self):
		return format(self.sch, 'q') + '.' + format(self.name, 'q')

	def __format__(self, spec):
		return format(str(self), spec)

	def __repr__(self):
		if self.__class__ is DBObj:
			return f"DBObj({repr(self.sch)}, {repr(self.name)}, {repr(self.objtype)})"
		return f"{self.__class__.__name__}({repr(self.sch)}, {repr(self.name)})"

	# pylint: disable=locally-disabled, bad-whitespace, multiple-statements
	def __eq__(self, other): return isinstance(other, DBObj) and (self.sch, self.name) == (other.sch, other.name)
	def __lt__(self, other): return isinstance(other, DBObj) and (self.sch, self.name) < (other.sch, other.name)
	def __le__(self, other): return self.__eq__(other) or self.__lt__(other)
	def __ge__(self, other): return not self.__lt__(other)
	def __ne__(self, other): return not self.__eq__(other)
	def __gt__(self, other): return not self.__le__(other)

	def __hash__(self):
		return (self.sch.lower() + self.name.lower()).__hash__()

	@staticmethod
	def create(sch: str, name: str, objtype: Optional[str], get_xmldef: Optional[XMLDefGetter] = None) -> 'DBObj':
		"instantiate object based on type"
		if objtype is None:
			return DBObj(sch, name)

		objtype = objtype.rstrip() # Hack: teradatasql python driver returns "wide strings"

		if objtype == 'V':
			return View(sch, name, get_xmldef)
		if objtype == 'v': # hack for Volatile table
			return VolatileTable(sch, name, 'T', get_xmldef)
		if objtype == 't': # hack for GTT
			return GTTable(sch, name, 'T', get_xmldef)
		if objtype == 'O':
			return NoPITable(sch, name, get_xmldef)
		if objtype == 'T':
			return Table(sch, name, objtype, get_xmldef)

		return DBObj(sch, name, objtype)

class Table(ColMixin, XMLDefMixin, DBObj):
	"Teradata table. Except for schema and name, all attributes are lazily evaluated"
	_xml_type = 'Table'
	_show_type = 'TABLE'

	def __init__(self, sch, name, objtype='T', get_xmldef: Optional[XMLDefGetter] = None):
		super().__init__(sch, name, objtype=objtype)
		self.get_xmldef: Optional[XMLDefGetter] = get_xmldef

	@cached_property
	def columns(self) -> List[Column]:
		"""ordered list of table columns"""
		return [Column.fromxml(c) for c in self._xmldef.find('./ColumnList')]

	@cached_property
	def indexes(self) -> List[Index]:
		"list of indexes"
		from .index import Index
		return [Index.fromxml(i, self.col) for i in self._xmldef.find('./Indexes') if i.tag != 'NoPrimaryIndex']

	@property
	def pi_cols(self) -> List[Column]:
		"list of Primary Index columns"
		from .index import PrimaryIndex
		return next((ix.columns for ix in self.indexes if isinstance(ix, PrimaryIndex)), [])

	@property
	def pk_cols(self) -> List[Column]:
		"list of primary key columns"
		try:
			return next(ix for ix in self.indexes if ix.is_pk).columns
		except StopIteration:
			return []

	@cached_property
	def is_multiset(self) -> bool:
		"returns True if table is MULTISET"
		return self._xmldef.attrib['kind'] == 'Multiset'

	@cached_property
	def has_fallback(self) -> bool:
		"returns True if table has FALLBACK"
		return self._xmldef.attrib['fallback'] == 'true'

	@cached_property
	def is_sysver(self) -> bool:
		"returns True if table is system versioned TEMPORAL"
		return self._xmldef.attrib.get("systemVersioned", "false") == "true"

	@cached_property
	def pt_cols(self) -> List[Column]:
		"list of columns that participate in table partitioning"
		import re
		from .index import PPI
		from .index import RowPartition

		return [c for i in self.indexes if isinstance(i, PPI)
				for pt in i.parts if isinstance(pt, RowPartition)
				for c in self.columns if re.search(r'\b'+c.name+r'\b', pt.expr)]

	def cstr_defs(self) -> List[str]:
		"""retuns a list of SQL constraints"""
		return []

	def sqldef(self, col_format: bool = False) -> str:
		"""Returns SQL DDL"""
		from .column import DerivedPeriod

		colps = [c.sqldef_parts(incl_format=col_format) for c in self.columns]
		def part_len(n):
			return max(len(p[n]) for p in colps)

		colfmt = f"{{:<{part_len(0)}}}  {{:<{part_len(1)}}} {{:<{part_len(2)}}} {{}}"

		def post_opts():
			"returns a generator to table post-def options"
			from .index import PrimaryIndex

			if not any(True for ix in self.indexes if isinstance(ix, PrimaryIndex)):
				yield "NO PRIMARY INDEX"
			yield from (i.sqldef() for i in self.indexes)
			yield from self.cstr_defs()
			if self.is_sysver:
				yield "WITH SYSTEM VERSIONING"

		return dedent("""\
			CREATE {} {}TABLE {}
			( {}
			) {};""").format(
				'MULTISET' if self.is_multiset else 'SET',
				{GTTable: 'GLOBAL TEMPORARY ', VolatileTable: 'VOLATILE '}.get(type(self), ''),
				str(self),
				'\n, '.join(colfmt.format(*p) for p in colps),
				"\n  ".join(post_opts())
			)

class NoPITable(Table):
	"NOPI Table"
	def __init__(self, sch: str, name: str, *args, **kwargs):
		super().__init__(sch, name, 'O', *args, **kwargs)

	@cached_property
	def pi_cols(self) -> List[Column]:
		return []

class TemporaryTable(Table):
	"""Temporary Table"""
	@cached_property
	def preserve_on_commit(self) -> bool:
		"""Returns True if on commit behavior is to perserve rows"""
		return self._xmldef.find('./TableConstraint/TablePreserveMode').attrib['onCommit'] == 'Preserve'

	def cstr_defs(self) -> List[str]:
		return super().cstr_defs() + ['ON COMMIT {} ROWS'.format('PRESERVE' if self.preserve_on_commit else 'DELETE')]

class VolatileTable(TemporaryTable):
	"""Volatile Table"""
	_xml_type = 'VolatileTable'

class GTTable(TemporaryTable):
	"""Global Temporary Table"""
	_xml_type = 'GlobalTemporaryTable'

class View(ColMixin, XMLDefMixin, DBObj):
	"Database View"
	_xml_type = 'View'
	_show_type = 'VIEW'

	def __init__(self, sch: str, name: str, get_xmldef: Optional[XMLDefGetter] = None):
		super().__init__(sch, name, 'V')
		self.get_xmldef: Optional[XMLDefGetter] = get_xmldef

	@cached_property
	def columns(self) -> List[Column]:
		"""ordered dictionary of table columns"""
		return [Column.fromxml(c) for c in self._xmldef.find('./ColumnList')]

	@cached_property
	def refs(self) -> List[Union[Table, 'View']]:
		"list of objects referred by this view"
		if not self._xmldef.find('./RefList'):
			logger.info("XML definition for '%s' did not contain referenced objects list", str(self))
			return []

		def xml2ob(x):
			"convert reference in xml to Table/View"
			sch, name, tv = x.attrib['dbName'], x.attrib['name'], x.attrib['type']
			return View(sch, name, get_xmldef=self.get_xmldef) if tv == 'View' else Table(sch, name, tv, get_xmldef=self.get_xmldef)

		return [xml2ob(r) for r in self._xmldef.find('./RefList')]

	def sqldef(self) -> str:
		"Return SQL definition"
		return self._xmldef.find('SQLText').text
