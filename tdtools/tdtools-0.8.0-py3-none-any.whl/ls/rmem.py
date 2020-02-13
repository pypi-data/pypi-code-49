#! /usr/bin/env python
"List Teradata Role Members"

__author__ = "Paresh Adhia"
__copyright__ = "Copyright 2016-2019, Paresh Adhia"
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

import tdtypes as td
from .util import Listing, dbc

class RMem(Listing):
	"Role Member Listing"

	def user_args(self):
		yield lambda p: p.add_argument("names", metavar='ROLE.MEM', type=td.DBObjPat, nargs='*',
										help="search for only specific role.member names (wild-cards allowed)")

	def cols(self):
		if self.args.verbose >= 2:
			yield ("NULLIF(WithAdmin,'N')" , "Adm")
		yield ("Grantee", "Mem")
		if self.args.verbose >= 1:
			yield ("RoleName", "Role")

	def build_sql(self):
		if self.args.names:
			where = "\nWHERE " + td.DBObjFinder(self.args.names, db='RoleName', tb='Grantee').sql_pred()
		else:
			where = ''

		return f"""\
SELECT {self.select()}
FROM {dbc.RoleMembersV}{where}
ORDER BY Grantee, RoleName"""

def main(args=None):
	"script entry-point"
	return RMem(__name__, __doc__, args).ls()

if __name__ == '__main__':
	import sys
	sys.exit(main())
