"TPT base type definitions"

__author__ = "Paresh Adhia"
__copyright__ = "Copyright 2016-2019, Paresh Adhia"

from typing import Union, List, Optional, Iterable, Tuple, Any, Dict
from collections import OrderedDict
from enum import Enum, auto
from pathlib import Path

AttrVal = Union[str, int, bool, List[str], List[int]]

class UtilSize(Enum):
	"TPT Utility data size"
	MICRO = auto()
	TINY = auto()
	SMALL = auto()
	MEDIUM = auto()
	LARGE = auto()

class YesNo(Enum):
	"Extended bool values"
	NO = auto()
	YES = auto()
	ALWAYS = auto()
	NEVER = auto()

class QB1:
	"A single QueryBand name-value pair"
	def __init__(self, name: str, val: str):
		self.name: str = name
		self.val: str = val

	def __str__(self):
		return f'{self.name}={self.val};'
	def __lt__(self, other):
		return isinstance(other, QB1) and (self.name, self.val) < (other.name, other.val)
	def __eq__(self, other):
		return isinstance(other, QB1) and (self.name, self.val) == (other.name, other.val)

	@staticmethod
	def parse(pair: str) -> 'QB1':
		"parse a string to QueryBand"
		if pair.count('=') != 1:
			raise ValueError('Invalid QueryBand value')
		name, val = pair.split('=')
		if val[-1] == ';':
			val = val[:-1]
		return QB1(name, val)

	@staticmethod
	def from_utsz(u: UtilSize) -> List['QB1']:
		"Return a list containing either 1 QB1 element if u is either SMALL or LARGE or an empty list"
		return [QB1('UtilityDataSize', u.name)] if u in [UtilSize.SMALL, UtilSize.LARGE] else []

class TPTVars(OrderedDict):
	"List of TPT variable/attribute and value"
	def __setitem__(self, k: str, v: Optional[AttrVal], **kargs) -> None:
		if v is None or v == []:
			if k in self:
				del self[k]
		else:
			OrderedDict.__setitem__(self, k,v, **kargs)

	def pairs(self) -> Iterable[Tuple[str, str]]:
		"list of tuple containing variable and its formatted value"
		def fmtval(val):
			"printable representation of value based on its type"
			if isinstance(val, bool): return "'Yes'" if val else "'No'"
			if isinstance(val, int):  return format(val)
			if isinstance(val, list): return "[{}]".format(', '.join(fmtval(v) for v in val))
			if isinstance(val, str):  return val if '@' in val or val.startswith("'") else "'{}'".format(val.replace("'","''"))
			return f"'{val}'"

		for k, v in self.items():
			yield (k, fmtval(v))

	def as_decl(self, indent='') -> str:
		"return as a string that SETs variable values"
		width = max([len(k) for k in self.keys()])
		return ('\n'+indent).join(f"SET {k:{width}} = {v};" for k,v in self.pairs())

	def as_attr(self, indent='') -> str:
		"return as a string of attributes"
		if not self:
			return ''
		return ' ATTR({})'.format((','+indent).join(f'{k}={v}' for k,v in self.pairs()))

	@staticmethod
	def from_auth(user: str, password: str = None, host: str = None, logmech: str = None, prefix: str = '') -> 'TPTVars':
		"Build TPTVars from authentication information"
		cvars = TPTVars()

		if host:
			cvars[f"{prefix}TdpId"] = host
		cvars[f"{prefix}UserName"] = user
		if password:
			cvars[f"{prefix}UserPassword"] = password
		if logmech:
			cvars[f"{prefix}LogonMech"] = logmech

		return cvars

class Instances(int):
	"Number of producer/consumer Instances"
	def __init__(self, val: Any):
		int.__init__(int(val))
		if self < 1:
			raise ValueError("Instnaces value can't be less than 1")

	def __str__(self):
		return ('['+int.__str__(self)+']') if self > 1 else ''

class TPTOp:
	"A TPT Operator"
	def __init__(self, name: str, inst: Optional[Instances] = None, sch: Optional[str] = None, dlm: bool = False):
		self.name: str = name
		self.inst: Instances = inst or Instances(1)
		self.sch: Optional[str] = sch
		self.dlm: bool = dlm
		self.attrs: TPTVars = TPTVars()

	def __str__(self):
		if self.sch:
			sch = f"({'DELIMITED ' if self.dlm else ''}'{self.sch}')"
		else:
			sch = ''
		return f"${self.name}{sch}{self.inst}" + self.attrs.as_attr("\n\t")

class S3:
	def __init__(self, name: str, bucket: str, pfx: Optional[str] = None, regn: Optional[str] = None, multi: bool = True):
		name = name if pfx is None else str(Path(pfx) / name)
		self.name = name[1:] if name[0] == '/' else name
		self.bucket: str = bucket
		self.regn: Optional[str] = regn
		self.multi = multi

	def __lt__(self, other):
		return isinstance(other, S3) and str(self) < str(other)

	def __str__(self) -> str:
		return ' '.join(f"{k}={v}" for k, v in [
			('S3Region', self.regn),
			('S3Bucket', self.bucket),
			('S3Object', self.name),
			('S3SinglePartFile', not self.multi)] if v)

def path_obj(dirpath: Optional[str], name: str) -> Union[S3, Path]:
	"If name is a valid S3 URN, return S3 object, Path otherwise"
	from urllib.parse import urlparse

	u = urlparse(dirpath or name)
	if u.scheme.lower() == 's3':
		return S3(str(Path(u.path) / name) if dirpath else u.path, u.netloc)

	return Path(dirpath) / name if dirpath else Path(name)

def file_attrs(dirpath: Optional[str], name: str) -> Dict[str, Any]:
	p = path_obj(dirpath, name)

	if isinstance(p, S3):
		return {'AccessModuleName': 'libs3axsmod.so', 'AccessModuleInitStr': p}

	if dirpath:
		return {'DirectoryPath': dirpath, 'FileName': name}

	return {'FileName': name}
