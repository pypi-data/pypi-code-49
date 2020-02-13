#! /usr/bin/env python
"View Reference Table maintenance"

from typing import List, Tuple, Optional
from textwrap import dedent
import tdtypes as td
from tdtools.util import getLogger

DFLT_REFTB = "SysDBA.ViewRefs"

logger = getLogger(__name__)

def main(args: Optional[List[str]] = None) -> None:
	"script entry-point"
	import argparse
	from . import util

	parser = argparse.ArgumentParser(description=__doc__)
	parser.add_argument('views', type=td.DBObjPat, nargs='*', metavar='%DB%.%VW%', help="Optional list of views (wildcard allowed) to refresh (default all)")
	parser.add_argument("-I", "--hide", type=lambda v: td.DBObjPat('!'+v), dest='views', action='append', metavar='%DB%.%VW%', help="exclude tables that match PATTERN")
	parser.add_argument('-t', '--reftb', metavar='TBL', default=DFLT_REFTB, help=f'table for storing view reference data (default: {DFLT_REFTB})')
	parser.add_argument('--ddl', action='store_true', help='Show DDL for creating a new table to store static references')
	parser.add_argument('--look-back', type=int, metavar='INT', help='Number of days to limit scan to look for non-existent views')
	util.dbconn_args(parser)

	args = parser.parse_args(args)

	if args.ddl:
		print(get_ddl(args.reftb) + ';')
	else:
		with util.cursor(args) as csr:
			try:
				added, removed, invalid = refresh(csr, args.views, reftb=args.reftb, lookback=args.look_back)
				print(f"Views: {added:,d} added, {removed:,d} removed, {invalid:,d} were invalid")
			except td.sqlcsr.DatabaseError as err:
				raise SystemExit(str(err))

def get_ddl(reftb: str) -> None:
	"print DDL for storing static view reference info needed for reverse lookup"
	return dedent(f"""\
		CREATE TABLE {reftb}
		( ViewDB    varchar(128) character set unicode not null
		, ViewName  varchar(128) character set unicode not null
		, ViewUpdTS Timestamp(0) not null
		, RefDB     varchar(128) character set unicode
		, RefName   varchar(128) character set unicode
		) PRIMARY INDEX(ViewDB,ViewName)""")

def refresh(
		csr: td.sqlcsr.Cursor,
		names: List[td.DBObjPat] = None,
		reftb: str = DFLT_REFTB,
		lookback: Optional[int] = None
	) -> Tuple[int, int, int]:
	"refresh static reftb with views that were altered since last they were evaluated"

	ref_pred = []
	if names:
		ref_pred.append(td.DBObjFinder(names, db='ViewDB', tb='ViewName').sql_pred().replace('\n', '\n\t\t'))

	dbc_pred = []
	if names:
		dbc_pred.append(td.DBObjFinder(names).sql_pred().replace('\n', '\n\t\t'))
	if lookback:
		dbc_pred.append(f"LastAlterTimestamp > CURRENT_TIMESTAMP - INTERVAL '{lookback}' DAY")

	def tbl_expr(tbl: str, pred: List[str], indent: int = 0) -> str:
		if not pred:
			return tbl

		return dedent("""\
			(
				SELECT *
				FROM {}
				WHERE {}
			)""").format(tbl, "\n\t\tAND ".join(pred)).replace('\n', '\n' + '\t' * indent)

	def runsql(sql, parms=None):
		if parms is None:
			csr.execute(sql)
		else:
			csr.executemany(sql, parms)
		rowc = csr.rowcount
		logger.debug("%d rows affected\n> %s\n", rowc, sql.replace('\t', '    ').replace('\n', '\n> '))
		return rowc

	# remove views which no longer exists or whose references no longer exist or were altered
	removed = runsql(dedent(f"""\
		DELETE
		FROM {reftb}
		WHERE (ViewDB, ViewName) IN (
				SELECT DISTINCT ViewDB, ViewName
				FROM {tbl_expr(reftb, ref_pred, 3)} R
				LEFT JOIN dbc.TablesV T ON T.DatabaseName = R.RefDB and T.TableName = R.RefName
				LEFT JOIN dbc.TablesV V ON V.DatabaseName = R.ViewDB and V.TableName = R.ViewName AND V.TableKind = 'V'
				WHERE (
						T.DatabaseName IS NULL AND R.RefDB IS NOT NULL OR
						V.DatabaseName IS NULL OR
						V.LastAlterTimestamp > R.ViewUpdTS
					)
			)"""))

	# find new views for inclusion
	reeval = runsql(dedent(f"""\
		SELECT DatabaseName
			, TableName
			, LastAlterTimestamp
		FROM {tbl_expr('dbc.TablesV', dbc_pred, 1)} V
		WHERE TableKind = 'V'
			AND NOT EXISTS (
					SELECT 1
					FROM {reftb} R
					WHERE V.DatabaseName = R.ViewDB
						AND V.TableName = R.ViewName
				)"""))

	def vdeps(db, vw) -> List[Tuple[str, str]]:
		try:
			return [(r.sch, r.name) for r in td.View(db, vw, csr.get_xmldef).refs] or [(None, None)]
		except td.sqlcsr.DatabaseError:
			logger.info("Unable to obtain referenced objects for '%s.%s'", db, vw)
			return []

	deps = [(db, vw, ts, vdeps(db, vw)) for db, vw, ts in csr.fetchall()]
	refs = [(db, vw, ts, rdb, rob) for db, vw, ts, rl in deps for rdb, rob in rl]
	if refs:
		runsql(f"INSERT INTO {reftb} (ViewDB,ViewName,ViewUpdTS,RefDB,RefName) VALUES(?,?,?,?,?)", refs)
	invalid = sum(1 for v in deps if not v[3]) # Views that had error

	return (reeval - invalid, removed, invalid)

if __name__ == '__main__':
	main()
