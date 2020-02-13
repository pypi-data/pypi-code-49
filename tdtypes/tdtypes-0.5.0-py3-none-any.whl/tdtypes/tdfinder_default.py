"Teradata Find framework to help object instantiation"

__author__ = "Paresh Adhia"
__copyright__ = "Copyright 2016-2020, Paresh Adhia"

from typing import Optional, List, Union, TypeVar, Callable, Iterable
import xml.etree.ElementTree as ET
from textwrap import dedent

from .tvm import DBObj, XMLDefGetter
from .util import getLogger

logger = getLogger(__name__)

class DBObjPat:
	"[!][<DB-PAT>.]<TB-PAT>; supported wild-card characters: [%%,*,?]; e.g. DB1.TB%%, DB?.TB1*, !db2.tb2%%, tb2?last"
	def __init__(self, pat: str):
		self.pat = pat
		if pat.startswith('!'):
			self.incl = False
			pat = pat[1:]
		else:
			self.incl = True
		self.sch, self.name = pat.split('.') if '.' in pat else (None, pat)

	def sqlrepr(self, db: str = 'DatabaseName', tb: str = 'TableName', match_ovr:Optional[bool] = None) -> str:
		"build SQL search condition using search predicates formed by schema and name"
		incl = self.incl if match_ovr is None else match_ovr

		cond = []
		if self.sch is None and incl:
			cond.append(self.search_predicate(db, None, defval='DATABASE'))
		elif self.sch != '%':
			cond.append(self.search_predicate(db, self.sch, match=incl))
		if self.name != "%":
			cond.append(self.search_predicate(tb, self.name, match=incl))

		if not cond:
			return self.search_predicate(db, "%", match=incl)
		if len(cond) == 1:
			return cond[0]

		return " AND ".join(cond) if incl else "(" + " OR ".join(cond) + ")"

	search_cond = sqlrepr # legacy compatibility name
	__str__ = sqlrepr

	def __repr__(self):
		return "'" + self.pat + "'"

	@staticmethod
	def search_predicate(col: str, val: Optional[str], defval: Optional[str] = None, match:bool = True) -> Optional[str]:
		"build SQL search predicate based on if value contains any wild-card characters"
		eq, like = ('=', 'LIKE') if match else ('<>', 'NOT LIKE')

		if val is None:
			return col + f' {eq} ' + defval if defval is not None else None
		if '%' in val or '?' in val or '*' in val:
			esc = " ESCAPE '+'" if '_' in val else ''
			val = val.replace('_', '+_').replace('?', '_').replace('*', '%')
			return col + f" {like} '{val}'{esc}"
		return col + f" {eq} '{val}'"

	@staticmethod
	def findall(patterns, objtypes='', flatten=True, warn_notfound=True, csr=None) -> Union[List[DBObj], List[List[DBObj]]]:
		"factory method that returns list of objects matching list of wild-cards"
		from . import sqlcsr
		return DBObjFinder(patterns, objtypes).findall(csr or sqlcsr.csr, flatten=flatten, warn_notfound=warn_notfound)

class DBObjFinder:
	"Class to find all DBObj that match a list of DBOBjPat"
	def __init__(self, patterns: Iterable[Union[DBObjPat,str]], objtypes: str = '', db: str = 'DatabaseName', tb: str = 'TableName'):
		self.patterns = [DBObjPat(p) if isinstance(p, str) else p for p in patterns]
		self.objtypes, self.db, self.tb = objtypes, db, tb

	@property
	def caseexpr(self) -> str:
		"returns SQL CASE expression that evaluates to the index of the matched pattern"
		from itertools import chain, tee

		patterns = enumerate(self.patterns) # number each pattern
		i1, i2 = tee(patterns)
		# sequence non-matches before matches
		patterns = chain(filter(lambda x: not x[1].incl, i1), filter(lambda x: x[1].incl, i2))

		# default match is any if all are exclude-types, otherwise, default is non-match
		default_match = 'NULL' if any(p for p in self.patterns if p.incl) else '-1'

		def when(pos: int, pat: DBObjPat) -> str:
			return f'WHEN {pat.sqlrepr(self.db, self.tb, match_ovr=True)} THEN ' + (str(pos) if pat.incl else 'NULL')

		return dedent("""\
			CASE
				{}
				ELSE {}
			END""").format('\n\t'.join(when(e, p) for e, p in patterns), default_match)

	def sql_pred(self) -> str:
		"return SQL predicate that checks for any (non-)matching patterns"
		if len(self.patterns) == 1:
			return self.patterns[0].search_cond(db=self.db, tb=self.tb)

		return self.caseexpr + " IS NOT NULL"

	def match_col(self, indent: str = "\t") -> str:
		"returns indented SQL CASE expression that evaluates to the index of the matched pattern"
		return self.caseexpr.replace('\n', '\n'+indent)

	def make_sql(self) -> str:
		"Build SQL to find objects matching patterns"

		obj_pred = ' AND TableKind IN ({})'.format(', '.join("'{}'".format(t) for t in self.objtypes)) if self.objtypes else ''

		return dedent("""\
			SELECT DatabaseName
				, TableName
				, CASE WHEN CommitOpt <> 'N' THEN 't' ELSE TableKind END AS TableKind
				, {} AS MATCHED_PAT
			FROM dbc.TablesV T
			WHERE MATCHED_PAT IS NOT NULL{}""").format(self.caseexpr.replace('\n', '\n\t'), obj_pred)

	def names2objs(self, names, flatten=True, warn_notfound=True, get_xmldef: Optional[XMLDefGetter] = None) -> Union[List[DBObj], List[List[DBObj]]]:
		"group names by pattern index that they belong to"
		matches = [[] for p in self.patterns]
		for db, tb, tp, m in names:
			matches[m].append(DBObj.create(db, tb, tp, get_xmldef))

		if warn_notfound:
			all_notfound = ', '.join(repr(p) for p, m in zip(self.patterns, matches) if p.incl and not m)
			if all_notfound:
				logger.warning('No matching objects found for: %s', all_notfound)

		return [o for m in matches for o in m] if flatten else matches

	def findall(self, csr, flatten=True, warn_notfound=True) -> Union[List[DBObj], List[List[DBObj]]]:
		"returns list of matching objects"
		sql = self.make_sql() + '\nORDER BY MATCHED_PAT, 1, 2'
		logger.debug('Search patterns: {}, SQL:{}\n'.format(', '.join(str(p) for p in self.patterns), sql))
		csr.execute(sql)

		return self.names2objs([r[:4] for r in csr.fetchall()], flatten=flatten, warn_notfound=warn_notfound, get_xmldef=csr.get_xmldef)
