"TPT Producer operators"

__author__ = "Paresh Adhia"
__copyright__ = "Copyright 2016-2019, Paresh Adhia"

from typing import List, Optional, Callable
from .util import TPTOp, QB1, UtilSize, file_attrs, YesNo
from ..table import Table

class ProducerOp(TPTOp):
	"TPT Producer operator"

class FileReaderOp(ProducerOp):
	"Data Connector Producer operator"
	TmplPfx = 'FileReader'

	def __init__(self,
			tbl: Table,
			src: Callable[[Table], str] = lambda t: getattr(t, 'src'),
			dirpath: Optional[str] = None,
			dlm: Optional[str] = None,  # None => binary
			esc: Optional[str] = None,
			quote: Optional[str] = None,
			fit: bool = False,
			empty: bool = False,
			skip1: bool = False,
			**kwargs):
		super().__init__('FILE_READER', sch=tbl, dlm=(dlm is not None), **kwargs)

		if dlm is None:
			self.attrs['Format'] = 'Binary'
			self.attrs['IndicatorMode'] = True
		else:
			self.attrs['Format'] = 'Delimited'
			self.attrs['EscapeTextDelimiter'] = esc
			if empty:
				self.attrs['AcceptMissingColumns'] = empty
				self.attrs['NullColumns'] = empty

		if fit:
			self.attrs['TruncateColumnData'] = True

		if dlm:
			try:
				self.attrs['TextDelimiterHEX'] = format(int(dlm), '02X')
			except ValueError:
				self.attrs['TextDelimiter'] = dlm

		if quote is not None:
			self.attrs['QuotedData'] = quote

		self.attrs.update(file_attrs(dirpath, src(tbl)))

		if skip1:
			self.attrs['SkipRows'] = 1

class SQLProducerOp(ProducerOp):
	"Generic SQL producer operator"
	def __init__(self, op: str, tbl: Table, src: Callable[[Table], str] = lambda t: getattr(t, 'src'), **kwargs):
		super().__init__(op, **kwargs)
		self.attrs['SelectStmt'] = src(tbl)

class ExportOp(SQLProducerOp):
	"EXPORT operator"
	TmplPfx = 'Export'

	def __init__(self, tbl: Table, qb: Optional[List[QB1]] = None, util_sz: Optional[UtilSize] = None, spool: Optional[YesNo] = None, **kwargs):
		super().__init__('EXPORT', tbl, **kwargs)

		self.attrs['QueryBandSessInfo'] = ([] if qb is None else qb) + QB1.from_utsz(util_sz)
		self.attrs['SpoolMode'] = {YesNo.NO: 'noSpool', YesNo.YES: 'Spool', YesNo.NEVER: 'noSpoolOnly'}.get(spool, None)

class SelectorOp(SQLProducerOp):
	"SELECTOR operator"
	TmplPfx = 'Selector'

	def __init__(self, tbl: Table, qb: Optional[List[QB1]] = None, **kwargs):
		super().__init__('SELECTOR', tbl, **kwargs)
		self.attrs['QueryBandSessInfo'] = [] if qb is None else qb

class OdbcOp(SQLProducerOp):
	"ODBC operator"
	TmplPfx = 'ODBC'

	def __init__(self, tbl: Table, conn: str, **kwargs):
		super().__init__('ODBC', tbl, **kwargs)
		self.attrs['ConnectString'] = conn
		self.attrs['TruncateData'] = True
