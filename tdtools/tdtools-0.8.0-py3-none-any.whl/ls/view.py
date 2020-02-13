#! /usr/bin/env python
"List Teradata views"

__author__ = "Paresh Adhia"
__copyright__ = "Copyright 2020, Paresh Adhia"
__license__ = "GPL"

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import sys
from textwrap import dedent

from tdtypes import DBObjPat, DBObjFinder, View
from .util import Listing, dbc
from ..util import indent2

class TVM(Listing):
	"TVM listing"

	def user_args(self):
		yield lambda p: p.add_argument("names", metavar='PATTERN', nargs='*', type=DBObjPat, help=DBObjPat.__doc__)
		yield args_filter
		yield args_display
		yield args_order

	def cols(self):
		def tscol(ts):
			return ts if self.args.verbose >= 3 else f"CAST({ts} AS DATE)"

		if self.args.verbose >= 2:
			yield ("CreatorName", "Creator")

		if self.args.verbose >= 1:
			yield (tscol("CreateTimestamp"), "Created")
			yield (tscol("LastAlterTimestamp"), "Altered")

		yield (None, "View")

	def build_sql(self):
		def preds():
			if self.args.names:
				yield indent2(DBObjFinder(self.args.names, db='DatabaseName', tb='TableName').sql_pred(), 2)
			else:
				yield 'DatabaseName = Database'

			if self.args.ctime:
				yield f"CAST(CreateTimestamp AS DATE) {self.args.ctime}"
			if self.args.mtime:
				yield f"CAST(LastAlterTimestamp AS DATE) {self.args.mtime}"
			if self.args.user:
				yield f"CreatorName = '{self.args.user}'"

		where = '\n\tAND '.join(preds())

		select = "\n\t, ".join(list(f"{expr} AS {col}" for expr, col in self.cols() if expr is not None) + ["DatabaseName", "TableName"])

		sql = dedent(f"""\
			SELECT {indent2(select,3)}
			FROM {dbc.TablesV}
			WHERE TableKind = 'V'
				AND {where}""")

		order = []
		if self.args.sort:
			if self.args.sort == 'name':
				if self.args.showdb:
					order.append('DatabaseName')
				order.append('TableName')
			else:
				order.append({'time': "CreateTimestamp", 'mtime': 'LastAlterTimestamp'}[self.args.sort])

		if order:
			def collate(c):
				"generate correct SQL ORDER BY clause"
				desc = c in ["CreateTimestamp", "LastAlterTimestamp"]
				if self.args.reverse:
					desc = not desc
				return 'DESC' if desc else 'ASC'

			sql += "\nORDER BY " + ', '.join(f"{c} {collate(c)}" for c in order)

		return sql

	def csr_to_ls(self, csr):
		import yappt

		def row_iter():
			for r in csr:
				*cols, sch, name = r
				yield (cols + [sch + '.' + name]) if self.args.showdb else (cols + [name])

		def tree_iter():
			for r in csr.fetchall():
				*cols, sch, name = r
				vw = View(sch, name, get_xmldef=csr.get_xmldef)
				try:
					for pfx, node in yappt.treeiter(vw, getch=lambda v: v.refs if isinstance(v, View) else []):
						yield cols + [str(pfx) + (str(node) if self.args.showdb else node.name)]
						cols = len(cols) * [None]
				except Exception as err:
					self.logger.error("Couldn't get referenced objects for %s: %s", vw, err)

		cols = [yappt.PPCol.create((d[0], d[1]), title_encoded=True) for d in csr.description[:-2]]
		cols.append(yappt.PPCol("View", ctype=str))

		return (cols, tree_iter() if self.args.tree else row_iter())

def args_filter(p):
	"options to filter listing"
	import os.path

	def rel_time(val: str) -> str:
		"relative time like in find linux command"
		import datetime as dt
		val = int(val.lstrip())
		return "{} '{}'".format('>=' if val < 0 else '<', (dt.date.today() - dt.timedelta(days=abs(val))).isoformat())

	cmd = os.path.split(sys.argv[0])[1]
	kind = {'lstb':'TO', 'lsvw':'V', 'lspr':'PE', 'lsji':'I', 'lsmc':'M', 'lsfn':'ABCFRSL'}.get(cmd)

	# pylint: disable=locally-disabled, bad-whitespace
	g = p.add_argument_group("Filters")
	g.add_argument("-I", "--hide",    type=lambda v: DBObjPat('!'+v), dest='names', action='append', default=[], metavar='PATTERN',  help="exclude tables that match PATTERN")
	g.add_argument(      "--mtime",   metavar='+N,-N,N', type=rel_time,    help="modify time n*24 hours ago")
	g.add_argument(      "--ctime",   metavar='+N,-N,N', type=rel_time,    help="create time n*24 hours ago")
	g.add_argument(      "--user",                                         help="only display tables created by this user")

def args_display(p):
	"options to format the display"
	g = p.add_argument_group("Display")
	g.add_argument("-D", dest="showdb", action="store_false", help="show just the object name without database prefix")
	g.add_argument("-T", "--tree", action="store_true", help="show hierarchy of objects referenced by views")

def args_order(p):
	"options to order the listing"
	g = p.add_argument_group("Ordering")
	x = g.add_mutually_exclusive_group()
	x.add_argument('--sort', metavar='WORD', default='name', choices=['none', 'name', 'time'],
		help="sort by WORD instead of name: none (-U), time (-t)")
	x.add_argument("-t", dest='sort', action='store_const', const='mtime', help="sort by time, newest first")
	x.add_argument("-U", dest='sort', action='store_const', const='none', help="do not sort; list entries in database order")
	g.add_argument("-r", "--reverse", action="store_true", help="reverse order while sorting")

def main(args=None):
	"script entry-point"
	return TVM(__name__, __doc__, args).ls()

if __name__ == '__main__':
	sys.exit(main())
