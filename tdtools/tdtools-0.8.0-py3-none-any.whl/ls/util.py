"Common functions used by ls*.py utilities"

__author__ = "Paresh Adhia"
__copyright__ = "Copyright 2016-2020, Paresh Adhia"
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

from argparse import ArgumentParser
from typing import List, Iterable, Callable, Tuple, Optional

import yappt
import tdtypes as td
from .. import vsch
from .. import util

dbc = vsch.load_schema('dbc')

def args_size(p: ArgumentParser) -> None:
	"add size args"
	x = p.add_mutually_exclusive_group()
	x.add_argument("-h", "--human-readable", dest='sizefmt', action="store_const", const='.1h', default='.1h',
		help="print human readable sizes (e.g., 1K 234M 2G)")
	x.add_argument("--si", dest='sizefmt', action="store_const", const='.1s', help="like -h but use powers of 1000 instead of 1024")
	x.add_argument("-b", "--bytes", dest='sizefmt', action="store_const", const=',d', help="print size in number of bytes")

def args_misc(p: ArgumentParser) -> None:
	"add misc args"
	g = p.add_argument_group("Miscellaneous")
	x = g.add_mutually_exclusive_group()
	x.add_argument('-v', '-l', '--verbose', default=1, action='count', help='print verbose output. Use -vv for more details')
	x.add_argument('-1', action='store_const', const=0, dest='verbose', help='print only names')
	g.add_argument('--help', action='help', help='show this help message and exit')
	util.dbconn_args(g)

def args_sort(p: ArgumentParser) -> None:
	"add ordering results args"
	x = p.add_mutually_exclusive_group()
	x.add_argument('--sort', metavar='WORD', default='name', choices=['none', 'size', 'name', 'time'],
		help="sort by WORD instead of name: none (-U), size (-S), time (-t)")
	x.add_argument("-t", dest='sort', action='store_const', const='mtime', help="sort by time, newest first")
	x.add_argument("-U", dest='sort', action='store_const', const='none', help="do not sort; list entries in database order")
	x.add_argument("-S", dest='sort', action='store_const', const='size', help="sort by size, largest first")
	p.add_argument("-r", "--reverse", action="store_true", help="reverse order while sorting")

class Listing:
	"Information listing"
	def __init__(self, name: str, doc: str, args: Optional[List[str]] = None):
		self.logger = util.getLogger(name)
		p = ArgumentParser(description=doc, fromfile_prefix_chars='@', add_help=False)
		for fn in self.user_args():
			fn(p)
		args_misc(p)

		self.args = p.parse_args(args)

	def select(self) -> str:
		"columns for SELECT clause"
		return '\n\t, '.join(f'{expr} AS "{name}"' for (expr, name) in self.cols())

	def csr_to_ls(self, csr):
		sizefmt = getattr(self.args, 'sizefmt', '.1h')
		return ([yappt.PPCol.create((d[0], d[1]), title_encoded=True, sizefmt=sizefmt) for d in csr.description], csr)

	def ls(self) -> int:
		from ..util import cursor
		"script entry-point"
		sql = self.build_sql()
		self.logger.debug('SQL =>\n%s;', sql.replace('\t', '    '))

		with cursor(self.args) as csr:
			csr.execute(sql)
			if csr.rowcount == 0:
				return 3

			columns, data = self.csr_to_ls(csr)
			if len(columns) > 1:
				yappt.pprint(data, columns=columns, sep='  ')
			else:
				for c, in data:
					print(c)

		return 0

	def user_args(self) -> Iterable[Callable[[ArgumentParser], None]]:
		"returns a list of functions that will add arguments in to passed argparse Parser object"
		return []

	def build_sql(self) -> str:
		"build SQL based on run-time options"
		raise NotImplementedError()

	def cols(self) -> Iterable[Tuple[str, str]]:
		"columns that are to be part of the SELECT clause"
		return []
