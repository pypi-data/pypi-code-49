"TPT Step types"

__author__ = "Paresh Adhia"
__copyright__ = "Copyright 2016-2019, Paresh Adhia"

from typing import List, Callable, Optional, Union
from textwrap import dedent

from ..util import indent2
from ..table import Table

from .util import TPTVars, QB1
from .cop import ConsumerOp
from .pop import ProducerOp
from .sop import DDLOp, StandAloneOp

class TPTStep:
	"TPT Job step definition"
	def __init__(self, name: str, cop: Union[StandAloneOp, ConsumerOp], pop: Optional[ProducerOp] = None):
		self.name: str = name
		self.cop: Union[StandAloneOp, ConsumerOp] = cop
		self.pop: Optional[ProducerOp] = pop
		self.vars: TPTVars = TPTVars()

	def apply(self):
		"generate APPLY clause"
		raise NotImplementedError

	def to_string(self, suffix: int = None):
		"Convert step to string, optionally add suffix to step name (to it keep unique)"
		sfx = '_'+format(suffix) if suffix else ''

		return dedent(f"""\
			STEP {self.name}{sfx} (
				{indent2(self.apply(), 4)}
			);""")

	__str__ = to_string

class DDLStep(TPTStep):
	"A TPT Step that runs SQLs"
	def __init__(self,
			name: str,
			tblist: List[Table],
			ddl: Callable[[Table], str],
			qb: Optional[List[QB1]] = None,
			errors: Optional[List[str]] = None):
		super().__init__(name, cop=DDLOp(errors, qb))
		self.tblist = tblist
		self.ddl = ddl

	def apply(self) -> str:
		def genddl(t):
			"strinify and escape the generated value"
			return "'" + self.ddl(t).replace("'","''") + "'"

		ddls = ',\n\t'.join([genddl(t) for t in self.tblist])
		return f"APPLY {ddls} TO OPERATOR ({self.cop});"

class LoadStep(TPTStep):
	"TPT Job Load step"
	def __init__(self, tbl: Table, pop: ProducerOp, cop: ConsumerOp):
		super().__init__(tbl.name, cop=cop, pop=pop)
		self.tbl = tbl

	def apply(self) -> str:
		return dedent(f"""\
			APPLY
			$INSERT '{self.tbl}' TO OPERATOR (
				{indent2(self.cop, 4)}
			)
			SELECT * FROM OPERATOR (
				{indent2(self.pop, 4)}
			);""")

class ExportStep(TPTStep):
	"TPT Job Load step"
	def __init__(self, tbl: Table, pop: ProducerOp, cop: ConsumerOp):
		super().__init__(tbl.name, cop=cop, pop=pop)
		self.tbl = tbl

	def apply(self) -> str:
		return dedent(f"""\
			APPLY
			TO OPERATOR (
				{indent2(self.cop, 4)}
			)
			SELECT * FROM OPERATOR (
				{indent2(self.pop, 4)}
			);""")
