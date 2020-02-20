from slate_utils.docs.base import BaseDocClass
from slate_utils.docs.utils import pkv_to_dict
from lxml import html

class QueryDocs(BaseDocClass):

    def fetch(self, id):
        return Query(next(self.db.select("""select * from [query] where [id] = ?""", (id,))))


class Query:
    def __init__(self, src):
        self.src = src

    @property
    def config(self):
        """Return dictionary of query.config data."""
        return pkv_to_dict(self.src.config)

    def serialize(self):
        serialized = self.src.copy()
        serialized['config'] = self.config
        return serialized
