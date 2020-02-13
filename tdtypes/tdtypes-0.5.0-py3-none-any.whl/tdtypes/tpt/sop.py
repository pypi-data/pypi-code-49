"TPT stand-alone operators"

__author__ = "Paresh Adhia"
__copyright__ = "Copyright 2016-2019, Paresh Adhia"

from typing import Optional, List
from .util import TPTOp, QB1

class StandAloneOp(TPTOp):
	"Stand alone TPT operator"

class DDLOp(StandAloneOp):
	"DDL operator"
	TmplPfx = 'DDL'

	def __init__(self, errors: Optional[List[str]] = None, qb: Optional[List[QB1]] = None):
		super().__init__('DDL')
		self.attrs['ErrorList'] = errors if errors else []
		self.attrs['QueryBandSessInfo'] = qb
