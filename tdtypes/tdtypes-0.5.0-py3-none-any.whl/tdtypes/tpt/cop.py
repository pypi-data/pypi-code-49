"TPT Consumer operators"

__author__ = "Paresh Adhia"
__copyright__ = "Copyright 2016-2019, Paresh Adhia"

from typing import List, Optional
from .util import TPTOp, UtilSize, QB1, file_attrs
from ..table import DBObj

class ConsumerOp(TPTOp):
	"TPT Consumer operator"

class FMLoadOp(ConsumerOp):
	"Generic TPT Load/Update operator"
	def __init__(self,
			tbl: DBObj,
			util_sz: UtilSize = UtilSize.MEDIUM,
			temp_db: Optional[str] = None,
			errlim: Optional[int] = None,
			qb: Optional[List[QB1]] = None,
			update: bool = False,
			**kwargs):
		super().__init__('UPDATE' if update else 'LOAD', **kwargs)

		if errlim is not None: self.attrs['ErrorLimit'] = errlim

		self.attrs['TargetTable'] = tbl
		self.attrs['QueryBandSessInfo'] = ([] if qb is None else qb)  + QB1.from_utsz(util_sz)

		if temp_db:
			temp_pfx = f'{temp_db}.{tbl.name}_'
			self.attrs['LogTable']    = temp_pfx + 'RL'
			self.attrs['ErrorTable1'] = temp_pfx + 'ET'
			self.attrs['ErrorTable2'] = temp_pfx + 'UV'
			if update:
				self.attrs['WorkTable'] = temp_pfx + 'WT'

class LoadOp(FMLoadOp):
	"TPT Load operator"
	TmplPfx = 'Load'

	def __init__(self, *args, **kwargs):
		super().__init__(*args, update=False, **kwargs)

class UpdateOp(FMLoadOp):
	"TPT Update operator"
	TmplPfx = 'Update'

	def __init__(self, *args, **kwargs):
		super().__init__(*args, update=True, **kwargs)

class StreamOp(ConsumerOp):
	"TPT Stream operator"
	TmplPfx = 'Stream'

	def __init__(self,
			tbl: DBObj,
			temp_db: Optional[str] = None,
			mac_db: Optional[str] = None,
			pack: int = None,
			sess: int = 1,
			errlim: int = 1,
			qb: Optional[List[QB1]] = None,
			**kwargs):
		super().__init__('STREAM', **kwargs)

		self.attrs['MacroDatabase'] = mac_db
		self.attrs['ErrorLimit'] = errlim
		self.attrs['QueryBandSessInfo'] = qb

		self.attrs['MaxSessions'] = sess
		self.attrs['Pack'] = pack

		if temp_db:
			self.attrs['LogTable'] = f'{temp_db}.{tbl.name}_RL'
			self.attrs['ErrorTable'] = f'{temp_db}.{tbl.name}_ET'

class InserterOp(ConsumerOp):
	"TPT SQL INSERTER Operator"
	TmplPfx = 'Inserter'

	def __init__(self, sess: Optional[int] = None, qb: Optional[List[QB1]] = None, **kwargs):
		super().__init__('INSERTER', **kwargs)
		self.attrs['MaxSessions'] = sess
		self.attrs['QueryBandSessInfo'] = qb

class FileWriterOp(ConsumerOp):
	"Data Connector Consumer operator"
	TmplPfx = 'FileWriter'

	def __init__(self,
			name: str,
			dirpath: Optional[str] = None,
			dlm: Optional[str] = None,
			esc: Optional[str] = None,
			quote: Optional[str] = None,
			**kwargs):
		super().__init__('FILE_WRITER', dlm=(dlm is not None), **kwargs)

		if dlm is None:
			self.attrs['Format'] = 'Binary'
			self.attrs['IndicatorMode'] = True
		else:
			self.attrs['Format'] = 'Delimited'
			self.attrs['EscapeTextDelimiter'] = esc

		if dlm:
			try:
				self.attrs['TextDelimiterHEX'] = format(int(dlm), '02X')
			except ValueError:
				self.attrs['TextDelimiter'] = dlm

		self.attrs['QuotedData'] = quote

		self.attrs.update(file_attrs(dirpath, name))
