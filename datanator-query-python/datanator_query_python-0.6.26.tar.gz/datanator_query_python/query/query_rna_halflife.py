from datanator_query_python.util import mongo_util, file_util
from pymongo.collation import Collation, CollationStrength


class QueryRNA(mongo_util.MongoUtil):

    def __init__(self, server=None, username=None, password=None, verbose=False,
                 db=None, collection_str=None, authDB='admin', readPreference='nearest'):
        super().__init__(MongoDB=server, db=db, username=username,
                        password=password, authSource=authDB, readPreference=readPreference,
                        verbose=verbose)
        self.client, self.db, self.collection = self.con_db(collection_str)
        self.collation = Collation('en', strength=CollationStrength.SECONDARY)

    def get_doc_by_oln(self, oln, projection={'_id': 0}):
        """Get document by ordered locus name
        
        Args:
            oln (:obj:`str`): odered locus name.
            projection (:obj:`dict`): pymongo query projection.

        Return:
            (:obj:`tuple` of :obj:`Pymongo.Cursor` and :obj:`int`):
            Pymongo cursor object and number of documents returned
        """
        query = {'halflives.ordered_locus_name': oln}
        docs = self.collection.find(filter=query, projection=projection, collation=self.collation)
        count = self.collection.count_documents(query, collation=self.collation)
        return docs, count

    def get_doc_by_protein_name(self, protein_name, projection={'_id': 0},
                                _from=0, size=0):
        """Get document by protein name
        
        Args:
            protein_name (:obj:`str`): name of the protein
            projection (:obj:`dict`, optional): mongodb query result projection. Defaults to {'_id': 0}.
            _from (:obj:`int`): first page (0-indexed).
            size (:obj:`int`): number of items per page.

        Return:
            (:obj:`tuple` of :obj:`Pymongo.Cursor` and :obj:`int`):
            Pymongo cursor object and number of documents returned.
        """
        con_0 = {'function': protein_name}
        con_1 = {'protein_name': protein_name}
        con_2 = {'protein_synonyms': protein_name}
        query = {'$or': [con_0, con_1, con_2]}
        docs = self.collection.find(filter=query, projection=projection, collation=self.collation,
                                    skip=_from, limit=size)
        count = self.collection.count_documents(query, collation=self.collation)
        return docs, count