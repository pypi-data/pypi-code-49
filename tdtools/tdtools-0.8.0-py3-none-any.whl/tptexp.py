#! /usr/bin/env python
"Generate TPT script to export Teradata table(s)"

__author__ = "Paresh Adhia"
__copyright__ = "Copyright 2019, Paresh Adhia"
__license__ = "GPL"

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

from typing import Callable, Tuple
from pathlib import Path
import re

from tdtypes.tpt import TPTJob, QB1, Instances, UtilSize, ExportOp, SelectorOp, FileWriterOp, ExportStep, YesNo, TPTVars
from tdtypes import Table as TDTable
from .util import getLogger

logger = getLogger(__name__)

class Table(TDTable):
	def src(self):
		return f'LOCK ROW ACCESS SELECT * FROM {self}'

def main():
	"script entry-point"
	args = user_args()

	job = build_job(args)

	if args.run:
		rc = job.run(args.jobvar, args.chkp, capture_counts=args.counts)
		if rc:
			return rc
		if args.counts:
			from yappt import pprint
			pprint(((c.step, c.rows_in, c.rows_out) for c in job.step_counts), ['Step', 'Ins', 'Sel'])
	else:
		print(str(job))

def user_args():
	"run-time options"
	import argparse
	import textwrap
	import functools
	import yappt
	from .util import AuthArg

	def src(pat: str) -> Callable[[Table], str]:
		"source is a file name or a patten-pair that derives filename from tablename"
		if not '=' in pat:
			return lambda t:pat

		try:
			pat, repl = pat.split('=')
			return functools.partial(re.compile(pat,re.IGNORECASE).sub, repl)
		except:
			raise argparse.ArgumentTypeError("Pattern shoud be of type <match>=<repl>")

	def yesno(v: str) -> bool:
		if v.lower() in ['yes', 'true', 'on']:
			return YesNo.YES
		if v.lower() in ['no', 'false', 'off']:
			return YesNo.NO
		raise argparse.ArgumentTypeError("Value must be yes/true/on or no/false/off")

	def table(v: str) -> Table:
		sch, name = v.split('.')
		return Table(sch, name)

	p = argparse.ArgumentParser(description=__doc__)

	p.add_argument('tbl', type=table, nargs='+', help='Table names')
	p.add_argument('dirpath', metavar='PATH', help='Output folder name')

	g = p.add_argument_group('Job options')
	g.add_argument('-j', '--job', metavar='NAME', help='TPT Jobname')
	g.add_argument('-z', '--chkp', metavar='INT', help='Checkpoint interval')
	g.add_argument('-v', '--jobvar', metavar='STR', help='TPT Job variable file')
	g.add_argument('--qb', type=QB1.parse, metavar='NAME=VALUE', nargs='*', help='QUERY_BAND information')
	g.add_argument('--run', action='store_true', help='Run the resulting TPT script (only on Linux)')
	g.add_argument('--counts', action='store_true', help='Capture and show counts after TPT job run')
	g.add_argument('--auth', type=AuthArg, metavar='AUTH', help='BTEQ style login information, example: dbc/dbc,dbc')

	g = p.add_argument_group('File options')
	g.add_argument('--tgt', metavar='PAT', type=src, help='File name or regex sub expression <match>=<repl>')
	g.add_argument('--dlm', metavar='CHAR/INT', nargs='?', default='', const='09', help='Field delimiter (--dlm with no value defaults to TAB)')
	g.add_argument('--binary', action='store_const', dest='dlm', const=None, help='Input data is in Teradata BINARY format')
	g.add_argument('--esc', metavar='CHAR', nargs='?', const='\\', help='Escape for Text delimiter (CHAR --esc with no value defaults to \\)')
	g.add_argument('--quoted', action='store_const', const='Yes', dest='quote', help="Quoted data")

	g = p.add_argument_group('Export options')
	g.add_argument('-d', '--db','--database', help='Default database name')
	g.add_argument('-p', '--pinst', metavar='INT', type=Instances, help='Number of producer instances')
	g.add_argument('-c', '--cinst', metavar='INT', type=Instances, help='Number of consumer instances')
	g.add_argument('--spool', metavar='YESNO', type=yesno, nargs='?', const=YesNo.YES, help='spool data for export (default True for LARGE and MEDIUM)')

	x = g.add_mutually_exclusive_group()
	x.add_argument('--large', dest='util_sz', action='store_const', const=UtilSize.LARGE, default=UtilSize.MEDIUM, help='Use UtilityDataSize=LARGE')
	x.add_argument('--medium', dest='util_sz', action='store_const', const=UtilSize.MEDIUM, help='Use UtilityDataSize=MEDIUM')
	x.add_argument('--small', dest='util_sz', action='store_const', const=UtilSize.SMALL, help='Use UtilityDataSize=SMALL')
	x.add_argument('--tiny', dest='util_sz', action='store_const', const=UtilSize.TINY, help='Use STREAM operator to load data')
	x.add_argument('--micro', dest='util_sz', action='store_const', const=UtilSize.MICRO, help='Use SELECTOR operator to load data')

	args = p.parse_args()

	return args

def build_job(args):
	"Return TPTJob instance built from command line parameters"
	def make_step(tb):
		if args.util_sz in [UtilSize.LARGE, UtilSize.MEDIUM, UtilSize.SMALL]:
			pop = ExportOp(tb, src=Table.src, qb=args.qb, inst=args.pinst, util_sz=args.util_sz, spool=args.spool)
		else:
			pop = SelectorOp(tb, src=Table.src, qb=args.qb)
		cop = FileWriterOp(args.tgt(tb), dirpath=args.dirpath, inst=args.cinst, dlm=args.dlm, esc=args.esc, quote=args.quote)

		return ExportStep(tb, pop, cop)

	def make_job(tblist):
		job = TPTJob(args.job or tblist[0].name if len(tblist) == 1 else 'TPTExport')
		job.vars['TargetWorkingDatabase'] = args.db
		if args.auth:
			job.varlist.append(args.auth.tptvars('Source'))
		job.add_steps(make_step(tb) for tb in tblist)
		job.refactor_attrs()

		return job

	if args.tgt is None:
		ext = 'dat' if args.dlm is None else 'csv' if args.dlm == ',' else 'txt'
		args.tgt = lambda t: f"{t.name.lower()}.{ext}"

	return make_job(args.tbl)

if __name__ == '__main__':
	main()
