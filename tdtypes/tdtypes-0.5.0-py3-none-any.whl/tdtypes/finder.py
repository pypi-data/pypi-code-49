"Teradata Database Object search and instantion"

try:
	from tdfinder_site import DBObjPat, DBObjFinder
except ModuleNotFoundError:
	from .tdfinder_default import DBObjPat, DBObjFinder
