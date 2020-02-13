"Teradata Index and Partition types"

__author__ = "Paresh Adhia"
__copyright__ = "Copyright 2016-2020, Paresh Adhia"

from typing import Mapping, List, Optional, Union, Sequence
from collections import OrderedDict
import xml.etree.ElementTree as ET

from cached_property import cached_property
from .util import Ident
from .column import Column, ColMixin

class ColGroup(list):
	"A Column group of column partition"
	def __init__(self, copy: Optional[List[Column]] = None, compressed: bool = False, row: bool = False):
		super().__init__()
		if copy:
			self.extend(copy)
		self.compressed: bool = compressed
		self.row: bool = row

	def sqldef(self) -> str:
		"""SQL DDL"""
		ddl = 'ROW ' if self.row else ''
		ddl += ','.join(c.name for c in self)
		if len(self) > 1:
			ddl += '(' + ddl + ')'
		if not self.compressed:
			ddl += ' NO AUTO COMPRESS'
		return ddl

	def __repr__(self):
		return 'ColGroup({}, Compressed={}, Row={})'.format([c.name for c in self], self.compressed, self.row)

	@staticmethod
	def fromxml(xml: ET.Element, cdefs: Mapping[str, Column]) -> 'ColGroup':
		"factory method to create object from XML"
		cg = ColGroup(compressed=xml.get('autoCompress', "false") == "true", row=xml.get('storage', "column") == "Row")
		cg.extend(cdefs[Ident(xcol.attrib['name'])] for xcol in xml.find('./ColumnList'))

		return cg

class Partition:
	"Base class for ROW or COLUMN partition"
	def __init__(self, level: int, extra: int = 0):
		self.level: int = level
		self.extra: int = extra

	def sqldef(self) -> str:
		"""Return SQL definition"""
		pass

	@staticmethod
	def fromxml(xml: ET.Element, cdefs: Mapping[str, Column]) -> Union['RowPartition', 'ColPartition']:
		"factory method to create object from XML"
		level = int(xml.attrib['level'])
		extra = xml.get('extraPartitions', None)
		extra = int(extra) if extra else 0

		if xml.tag == 'RowPartitioning':
			return RowPartition(level, xml.attrib['expression'], extra=extra)

		if xml.tag == 'ColumnPartitioning':
			return ColPartition(level, [ColGroup.fromxml(cg, cdefs) for cg in xml], extra=extra)

class RowPartition(Partition):
	"Row Partition"
	def __init__(self, level: int, expr: str, extra: int = 0):
		super().__init__(level, extra)
		self.expr: str = expr.replace('\r', '\n')

	def sqldef(self) -> str:
		return self.expr

	def __repr__(self) -> str:
		return f'RowPartition("{self.expr}", level={self.level}, extra={self.extra})'

class ColPartition(Partition):
	"Column Partition"
	def __init__(self, level: int, col_groups: List[ColGroup], extra: int = 0):
		super().__init__(level, extra)
		self.col_groups = col_groups

	def sqldef(self):
		ddl = "COLUMN"
		groups = [g for g in self.col_groups if len(g) > 1 or not g.compressed or g.row]
		if groups:
			if len(groups) == 1 and groups[0].row:
				ddl += ' ALL BUT '
			ddl += "(" + ', '.join(g.sqldef() for g in groups) + ')'
		if self.extra:
			ddl += f" ADD {self.extra}"

		return ddl

	def __repr__(self) -> str:
		return f'ColPartition({self.col_groups}, level={self.level}, extra={self.extra})'

class Index(ColMixin):
	"""Database INDEX"""
	def __init__(self, xml: ET.Element, columns: Sequence[Column]):
		from collections import OrderedDict

		self._xml: ET.Element = xml
		self.name: Optional[str] = xml.get('name')
		self.columns: Sequence[Column] = columns
		self.is_uniq = xml.attrib.get('unique', 'false') == 'true'
		self.is_pk = xml.get('implicitIndexFor', 'None') == "PrimaryKeyConstraint"
		self.allness = xml.get('allOption', "false") == 'true'

	def sqldef(self) -> str:
		"""Return SQL definition of the index"""
		if self.is_pk:
			ddl = 'PRIMARY KEY'
		else:
			ddl = '{}{}INDEX'.format('UNIQUE ' if self.is_uniq else '', 'PRIMARY ' if isinstance(self, PrimaryIndex) else '')
		if self.name: ddl += ' '+self.name
		if self.allness: ddl += ' ALL'
		ddl += ' ({})'.format(','.join(c.name for c in self.columns))

		if self._ix_attr:
			ddl += '\n' + self._ix_attr

		return ddl

	def __repr__(self) -> str:
		return "Index('"+self.sqldef()+"')"

	@property
	def _ix_attr(self) -> str:
		return ''

	@staticmethod
	def fromxml(xml: ET.Element, cdefs: Mapping[str, Column]) -> 'Index':
		"factory method to create object from XML"
		columns = [cdefs[Ident(xc.attrib['name'])] for xc in xml.find('./ColumnList')]

		o_xml = xml.find('./OrderBy')
		if o_xml is not None:
			o_col = cdefs[Ident(o_xml.attrib['column'])]
			o_byval = o_xml.attrib['type'] == 'Values'
			return VOSI(xml, columns, o_col, o_byval)

		if xml.tag == 'PrimaryIndex':
			pt_xml = xml.find('PartitioningList')
			if pt_xml is None:
				return PrimaryIndex(xml, columns)
			else:
				return PPI(xml, columns, parts=[Partition.fromxml(pt, cdefs) for pt in pt_xml])

		return Index(xml, columns)

class VOSI(Index):
	"Value Ordered Secondary Index"
	def __init__(self, xml: ET.Element, columns: Sequence[Column], order_col: Column, byval: bool):
		super().__init__(xml, columns)
		self.order_col: Column = order_col
		self.order_byval: bool = byval

	@property
	def _ix_attr(self) -> str:
		ddl = 'ORDER BY ' + ('VALUES' if self.order_byval else 'HASH')
		if self.order_col:
			ddl += f'({self.order_col.name})'
		return ddl

class PrimaryIndex(Index):
	"Primary Index"

class PPI(PrimaryIndex):
	"Partitioned Primary Index"
	def __init__(self, xml: ET.Element, columns: Sequence[Column], parts: List[Partition]):
		super().__init__(xml, columns)
		self.parts = parts

	@property
	def _ix_attr(self) -> str:
		return "PARTITION BY ({})".format('\n, '.join(p.sqldef() for p in self.parts))
