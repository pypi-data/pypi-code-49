from datanator_query_python.util import mongo_util
from pymongo.collation import Collation, CollationStrength


class QueryKOC:

    def __init__(self, username=None, password=None, server=None, authSource='admin',
                 database='datanator', collection_str=None, readPreference='nearest'):

        self.mongo_manager = mongo_util.MongoUtil(MongoDB=server, username=username,
                                                  password=password, authSource=authSource, db=database,
                                                  readPreference=readPreference)
        self.client, self.db, self.collection = self.mongo_manager.con_db(collection_str)
        self.collation = Collation(locale='en', strength=CollationStrength.SECONDARY)

    def get_org_code_by_ncbi(self, _id):
        """Get Kegg organism code given NCBI Taxonomy ID.

        Args:
            _id (:obj:`int`): NCBI Taxonomy ID.

        Return:
            (:obj:`str`): Kegg organism code.
        """
        projection = {'_id': 0, 'kegg_organism_id': 1}
        query = {'ncbi_taxonomy_id': _id}
        result = self.collection.find_one(filter=query, projection=projection)
        if result is None:
            return 'No code found.'
        else:
            return result.get('kegg_organism_id')

    def get_ncbi_by_org_code(self, org_code):
        """Get kegg organism code by NCBI Taxonomy ID.
        
        Args:
            org_code (:obj:`int`): Kegg organism code.

        Return:
            (:obj:`int`): NCBI Taxonomy ID.
        """
        projection = {'_id': 0, 'ncbi_taxonomy_id': 1}
        query = {'kegg_organism_id': org_code}
        doc = self.collection.find_one(filter=query, projection=projection, collation=self.collation)
        if doc is None:
            return -1
        else:
            return doc['ncbi_taxonomy_id']