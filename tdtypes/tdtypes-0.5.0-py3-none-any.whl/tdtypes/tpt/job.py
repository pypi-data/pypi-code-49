"TPT Job type"

__author__ = "Paresh Adhia"
__copyright__ = "Copyright 2016-2019, Paresh Adhia"

JOBID_PATTERN = '^Job id is (.*),'

from typing import List, Dict, Optional, Tuple, Union, Sequence, Iterable
from pathlib import Path
from itertools import chain, groupby

from ..util import getLogger, indent, indent2
from .util import TPTVars, AttrVal, TPTOp
from .step import TPTStep

logger = getLogger(__name__)

class UnexpectedError(RuntimeError):
	pass

class StepCounts:
	"inserted and exported row counts"
	def __init__(self, step: str, rows_in: int = 0, rows_out: int = 0):
		self.step, self.rows_in, self.rows_out = step, rows_in, rows_out

	def __repr__(self):
		return f'StepCount({self.step}, rows_in={self.rows_in}, rows_out={self.rows_out})'

class TPTJob:
	"TPT Job"
	def __init__(self, name: str):
		self.name: str = name
		self.steps: List[TPTStep] = []
		self.varlist: List[TPTVars] = [TPTVars()]
		self.vars: TPTVars = self.varlist[0]
		self.jobid: str = None
		self.step_counts: List[StepCounts] = None

	def add_step(self, step: TPTStep) -> None:
		self.steps.append(step)

	def add_steps(self, steps: Iterable[TPTStep]) -> None:
		self.steps.extend(steps)

	def run(self,
			jobvar: Optional[Union[str,Path]] = None,
			chkpt: Optional[str] = None,
			capture_counts: bool = False) -> int:
		"execute this TPT job"
		import tempfile
		import os
		from subprocess import run, PIPE

		with tempfile.NamedTemporaryFile(delete=False) as tmp:
			tmp.write(str(self).encode())
			script_file = tmp.name

		cmd = ['tbuild', '-f', script_file]
		if jobvar:
			cmd.extend(['-v', str(jobvar)])
		if chkpt:
			cmd.extend(['-z', chkpt])
		cmd.append(self.name)

		logger.info('Invoking command: %s', cmd)
		retval = run(cmd, stdout=(PIPE if capture_counts else None))
		if retval.returncode:
			logger.error("tbuild command failed with error code: %d. Manually remove '%s'", retval.returncode, script_file)
			return retval.returncode
		os.unlink(script_file)

		if capture_counts:
			try:
				self.jobid, self.step_counts = get_counts(retval.stdout.decode())
			except UnexpectedError as err:
				logger.error(err)
				return 1

		return 0

	def refactor_attrs(self):
		"refactor most frquently used attributes from at operator level to job level"
		from collections import defaultdict

		def mfv(key: str, attrs: Sequence[TPTVars]) -> AttrVal:
			"return the most frequent value used by all attributes for the key"
			if any(a for a in attrs if key not in a): # all must have some value
				return None

			vals = [(v, len(list(l))) for (v, l) in groupby(sorted(attr[key] for attr in attrs))]
			if len(vals) == 1 or vals[0][1] > vals[1][1]:
				return vals[0][0]

			return None

		def refactor_op_attrs(comm: TPTVars, pfx: str, attrs: Sequence[TPTVars]) -> None:
			"refactor most frequently used attribute values to common attribute"
			freq_vals = [(k, mfv(k, attrs)) for k in attrs[0]]
			freq_vals = [(k, v) for k, v in freq_vals if v is not None]

			if not freq_vals:
				return None

			for k, v in freq_vals:
				comm[pfx+k] = v
				for a in attrs:
					del a[k]

		ops = defaultdict(list)
		for s in self.steps:
			ops[s.cop.__class__].append(s.cop.attrs)
			if s.pop:
				ops[s.pop.__class__].append(s.pop.attrs)

		jvars = TPTVars()
		for cls, attrs in ops.items():
			refactor_op_attrs(jvars, cls.TmplPfx, attrs)

		if jvars:
			self.varlist.append(jvars)

	def __str__(self) -> str:
		for s in self.steps:
			self.vars.update(s.vars)

		names: Dict[str, int] = {}
		def step2str(step: TPTStep) -> str:
			"convert TPTStep to string"
			try:
				names[step.name] += 1
			except KeyError:
				names[step.name] = 0
			return step.to_string(names[step.name])

		body = '\n\n'.join(chain((v.as_decl() for v in self.varlist if v), (step2str(s) for s in self.steps)))

		return f"DEFINE JOB {self.name}\n(\n{indent(body)}\n);".replace('\t', '    ')

def get_counts(job_output: str) -> Tuple[str, List[StepCounts]]:
	from subprocess import run, PIPE
	from collections import OrderedDict

	def find_jobid(output: str) -> Optional[str]:
		import re
		for l in output.splitlines():
			m = re.match(JOBID_PATTERN, l)
			if m:
				return m.group(1)

	jobid = find_jobid(job_output)
	if jobid is None:
		print(job_output)
		raise UnexpectedError('Unable to determine jobid from the output')

	retval = run(['tlogview', '-j', jobid, '-f', 'TWB_EVENTS'], stdout=PIPE)
	if retval.returncode:
		raise UnexpectedError(f'tlogview command to retrieve TPT job output failed with RC={retval.returncode}')

	counts: OrderedDict[str, StepCounts] = OrderedDict()

	for l in retval.stdout.decode().rstrip().splitlines():
		_, _, _, op, step, _, _, _, rows, _ = l.split(',', 9)
		if step not in counts:
			counts[step] = StepCounts(step)
		if op.endswith('RowsInserted'):
			counts[step].rows_in += int(rows)
		if op.endswith('RowsExported'):
			counts[step].rows_out += int(rows)

	return (jobid, counts.values())
