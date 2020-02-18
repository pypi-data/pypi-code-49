"Teradata column types"

__author__ = "Paresh Adhia"
__copyright__ = "Copyright 2016-2019, Paresh Adhia"

from typing import Iterator, List, Any, Optional, Mapping, Dict, Tuple
import xml.etree.ElementTree as ET
from cached_property import cached_property
from .util import Ident

class SQLRegister(str):
	"Built-in SQL Register/function"

class IdentityDef:
	"""Definition for IDENTITY columns"""
	def __init__(self, attr: Mapping[str, Any]):
		self.dflt = attr['valueGeneration'] == "ByDefault"
		self.by = attr['increment']
		self.start = attr['startValue']
		self.min = attr['minValue']
		self.max = attr['maxValue']
		self.cycle = attr['cycle'] == "true"

	def sqldef(self) -> str:
		"""Returns SQL DDL"""
		how = 'BY DEFAULT' if self.dflt else 'ALWAYS'
		cycle = ' CYCLE' if self.cycle else ''

		return f'GENERATED {how} AS IDENTITY (START WITH {self.start} INCREMENT BY {self.by} MINVALUE {self.min} MAXVALUE {self.max}{cycle}'

class Column:
	"Database Column"
	# When set to True, all attrubutes must match for two columns to be compared equally
	strict_compare = False

	def __init__(self,
			name: str,
			coltype: Optional[str] = None,
			nullable: bool = True,
			defval: Optional[Any] = None,
			fmtstr: Optional[str] = None,
			cprs: Optional[List] = None,
			idtype: Optional[IdentityDef] = None,
			sysgen: Optional[str] = None):

		self.name, self.coltype, self.nullable, self.defval, self.fmtstr, self.cprs, self.idtype, self.sysgen = \
			Ident(name), coltype, nullable, defval, fmtstr, cprs, idtype, sysgen

	def sqltype(self) -> str:
		"SQL type"
		return self.coltype

	def sqldef(self, fmtstr: str = "{:q} {} {}", incl_format: bool = False) -> str:
		"""Returns SQL DDL"""
		nm, tp, nl, ot = self.sqldef_parts(incl_format)
		if not nl:
			nl = '        '

		return fmtstr.format(nm, tp, nl+ot).rstrip()

	def sqldef_parts(self, incl_format: bool = False) -> List[str]:
		"""Return a 4 part sql definition to be formatted later"""

		def other():
			if self.idtype:
				yield self.idtype.sqldef()
			if incl_format and self.fmtstr:
				yield f"FORMAT '{self.fmtstr}'"
			if self.defval:
				yield f"DEFAULT {self.literal(self.defval)}"
			if self.cprs is not None:
				yield "COMPRESS" + (" ({})".format(','.join(self.literal(v) for v in self.cprs)) if self.cprs else "")
			if self.sysgen:
				yield "GENERATED ALWAYS AS ROW " + self.sysgen.upper()

		return (format(self.name, 'q'), self.sqltype(), '' if self.nullable else 'NOT NULL', ' '.join(other()))

	__repr__ = sqldef

	def __str__(self) -> str:
		return self.name

	def __eq__(self, other) -> bool:
		if isinstance(other, str):
			return self.name == other
		if isinstance(other, Column):
			if (self.name, self.coltype, self.nullable, self.idtype) == (other.name, other.coltype, other.nullable, other.idtype):
				return (self.cprs, self.defval, self.fmtstr) == (other.cprs, other.defval, other.fmtstr) if self.strict_compare else True

		return False

	@staticmethod
	def fromxml(cdef: ET.Element) -> 'Column':
		"factory method to create object from XML"
		name = cdef.attrib['name']

		attr = {'nullable': cdef.attrib['nullable'] == 'true'}

		def deftype(v):
			r = {'CurrentDate': 'CURRENT_DATE', 'CurrentTime': "CURRENT_TIME", 'CurrentTimestamp': "CURRENT_TIMESTAMP"}.get(v, None) or v.upper()
			return SQLRegister(r)

		defval = cdef.find('Default')
		if defval is not None:
			attr['defval'] = deftype(defval.attrib['type']) if 'type' in defval.attrib else defval.attrib['value']
		if 'format' in cdef.attrib:
			attr['fmtstr'] = cdef.attrib['format']
		if cdef.find('Compress') is not None:
			attr['cprs'] = [v.attrib['value'] for v in cdef.find('Compress')]
		if cdef.find('Identity') is not None:
			attr['idtype'] = IdentityDef(cdef.find('Identity').attrib)
		if cdef.attrib.get('systemGeneratedRowStart'):
			attr['sysgen'] = 'start'
		if cdef.attrib.get('systemGeneratedRowEnd'):
			attr['sysgen'] = 'end'

		t = cdef.find('DataType')[0]

		attr['coltype'] = t.tag.upper()

		def int_attr(attr: str) -> Optional[int]:
			"convert attribute to integer if present"
			return int(t.attrib[attr]) if attr in t.attrib else None

		# pylint: disable=locally-disabled, bad-whitespace, multiple-statements
		if   t.tag == 'Char':     return CharCol(name, int(t.attrib['length']), varchar=t.attrib['varying']=='true', charset=t.attrib['charset'], **attr)
		elif t.tag == 'Byte':     return ByteCol(name, int(t.attrib['length']), varying=t.attrib['varying']=='true', **attr)

		elif t.tag == 'Integer':  return IntegerCol(name, 4, **attr)
		elif t.tag == 'SmallInt': return IntegerCol(name, 2, **attr)
		elif t.tag == 'ByteInt':  return IntegerCol(name, 1, **attr)
		elif t.tag == 'BigInt':   return IntegerCol(name, 8, **attr)
		elif t.tag == 'Decimal':  return DecimalCol(name, int_attr('precision'), int_attr('scale'), **attr)
		elif t.tag == 'Number':   return NumberCol(name, int_attr('precision'), int_attr('scale'), **attr)
		elif t.tag == 'Float':    return FloatCol(name, **attr)

		elif t.tag == 'Date':     return DateCol(name, **attr)
		elif t.tag == 'Time':     return TimeCol(name, int(t.attrib['fractionalSecondsPrecision']), **attr)
		elif t.tag == 'TimeStamp':return TimestampCol(name, int(t.attrib['fractionalSecondsPrecision']), t.attrib.get("timezone", "false") == "true", **attr)
		elif t.tag == 'DerivedPeriod': return DerivedPeriod(name, t.attrib['startColumnName'], t.attrib['endColumnName'], **attr)
		elif t.tag.startswith('Interval'): return IntervalCol(name, t.tag[8:], int_attr('precision'), int_attr('fractionalSecondsPrecision'), **attr)

		elif t.tag == 'JSON':     return JSONCol(name, int_attr('size'), int_attr('inlinelength'), **attr)
		elif t.tag == 'XML':      return XMLCol(name, int_attr('size'), int_attr('inlinelength'), **attr)
		elif t.tag == 'UDT' and t.attrib['name'] == "SYSUDTLIB.XML": return XMLCol(name, None, None, **attr)

		return Column(name, **attr)

	@classmethod
	def literal(cls, v: Optional[str]) -> Optional[str]:
		"""Return literal value suitable for SQL script"""
		if v is None:
			return None
		if isinstance(v, SQLRegister):
			return str(v)
		return "'" + v.replace("'", "''") + "'"

	quote_val = literal

class CharCol(Column):
	"Database CHAR or VARCHAR column"
	def __init__(self, name: str, size: int, varchar: bool = False, cs: bool = False, charset: Optional[str] = None, **attr):
		super().__init__(name, **attr)
		self.size, self.varchar, self.cs, self.charset = size, varchar, cs, charset

	def sqltype(self) -> str:
		return '{}CHAR({})'.format('VAR' if self.varchar else '', self.size)

class ByteCol(Column):
	"Database BYTE or VARBYTE column"
	def __init__(self, name: str, size: int, varying: bool = False, **attr):
		super().__init__(name, **attr)
		self.size, self.varying = size, varying

	def sqltype(self) -> str:
		return '{}BYTE({})'.format('VAR' if self.varying else '', self.size)

	@classmethod
	def literal(cls, v: Optional[bytes]) -> Optional[str]:
		"""Return quoted value suitable for SQL script"""
		return "'" + ''.join(format(ord(b), '02x') for b in v) + "'xb" if v is not None else None


class NumericCol(Column):
	"Base class for all numeric Database columns"
	@classmethod
	def literal(cls, v):
		"""Return quoted value suitable for SQL script"""
		return v

class IntegerCol(NumericCol):
	"Dataase INT, BIGINT, SMALLINT, BYTEINT column"
	def __init__(self, name: str, size: int, **attr):
		super().__init__(name, **attr)
		self.size = size

	def sqltype(self) -> str:
		return {4: 'INTEGER', 2: 'SMALLINT', 1: 'BYTEINT', 8: 'BIGINT'}[self.size]

class DecimalCol(NumericCol):
	"Database DECIMAL or NUMERIC column"
	def __init__(self, name: str, precision: int, scale: int, **attr):
		super().__init__(name, **attr)
		self.precision, self.scale = precision, scale

	def sqltype(self) -> str:
		return f"{self.coltype}({self.precision},{self.scale})"

class FloatCol(NumericCol):
	"Database FLOAT column"
	def __init__(self, name: str, **attr):
		super().__init__(name, **attr)

class NumberCol(NumericCol):
	"Database DECIMAL or NUMERIC column"
	def __init__(self, name: str, precision: Optional[int], scale: Optional[int], **attr):
		super().__init__(name, **attr)
		self.precision, self.scale = precision, scale

	def sqltype(self) -> str:
		return self.coltype if self.precision is None else f'{self.coltype}({self.precision},{self.scale})'


class DateCol(Column):
	"Database DATE column"
	def __init__(self, name: str, **attr):
		super().__init__(name, **attr)

class TimeCol(Column):
	"Database TIME column"
	def __init__(self, name: str, frac: int, defval=None, **attr):
		if isinstance(defval, SQLRegister):
			defval = SQLRegister(f"{defval}({frac})")
		super().__init__(name, defval=defval, **attr)
		self.frac = frac

	def sqltype(self) -> str:
		return f'{self.coltype}({self.frac})'

class TimestampCol(Column):
	"Database TIMESTAMP column"
	def __init__(self, name: str, frac: int, with_tz: bool = False, defval=None, **attr):
		if isinstance(defval, SQLRegister):
			defval = SQLRegister(f"{defval}({frac})")
		super().__init__(name, defval=defval, **attr)
		self.frac, self.with_tz = frac, with_tz

	def sqltype(self) -> str:
		return f'TIMESTAMP({self.frac})' + (' WITH TIME ZONE' if self.with_tz else '')

class DerivedPeriod(Column):
	"Teradata Derived PERIOD column"
	def __init__(self, name: str, start: str, end: str, **attr):
		super().__init__(name, **attr)
		self.start, self.end = Ident(start), Ident(end)

	def sqltype(self) -> str:
		return f"PERIOD FOR {self.name} ({self.start}, {self.end})"

	def sqldef_parts(self, incl_format: bool = False) -> List[str]:
		"""Returns SQL DDL"""
		return (f"PERIOD FOR {self.name}", f"({self.start}, {self.end})", "", "")

class IntervalCol(Column):
	"Database INTERVAL column"
	def __init__(self, name: str, types: str, prec: Optional[int], secfrac: Optional[int], **attr):
		super().__init__(name, **attr)

		self.prec, self.secfrac = prec if prec is not None else 2, secfrac if secfrac is not None else 6
		if 'To' in types:
			self.type1, self.type2 = types.split('To')
		else:
			self.type1, self.type2 = types, None

	def sqltype(self) -> str:
		def tu(tp, l=None, ignore=None):
			digits = [] if l is None else [str(l)]
			s = tp.upper()
			if s == 'SECOND':
				digits.append(str(self.secfrac))
			prec = ','.join(digits)
			if prec and prec not in ignore:
				s += f"({prec})"
			return s

		s = 'INTERVAL ' + tu(self.type1, self.prec, ['2', '2,6'])
		if self.type2:
			s += " TO " + tu(self.type2, ignore=['6'])

		return s

class SemiStructCol(Column):
	"Semi-structured data types"
	def __init__(self, name: str, size: int, size_in: Optional[int], **attr):
		super().__init__(name, **attr)
		self.size, self.size_in = size, size_in

class JSONCol(SemiStructCol):
	"Database JSON column"
	def sqltype(self) -> str:
		col_t = self.coltype
		if self.size != 16776192:
			col_t += f'({self.size})'
		if self.size_in != 4096:
			col_t += f' INLINE LENGTH {self.size_in}'
		return col_t

class XMLCol(SemiStructCol):
	"Database XML column"
	def sqltype(self) -> str:
		col_t = self.coltype
		if self.size != 2097088000:
			col_t += f'({self.size})'
		if self.size_in != 4046:
			col_t += f' INLINE LENGTH {self.size_in}'
		return col_t

class ColMixin:
	"""A mixin that provides column dictionary and iterator"""
	@cached_property
	def col(self) -> Dict[str, Column]:
		"""return ordered dict of columns"""
		return dict((c.name, c) for c in self.columns) # python 3.6+ guarantees order

	def __iter__(self) -> Iterator[Column]:
		return iter(self.columns)
