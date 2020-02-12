from datanator_query_python.util import mongo_util, file_util
from pymongo.collation import Collation, CollationStrength
import json


class QuerySabioCompound:

    def __init__(self, username=None, password=None, server=None, authSource='admin',
                 database='datanator', max_entries=float('inf'), verbose=True, collection_str='sabio_compound',
                 readPreference='nearest'):

        self.mongo_manager = mongo_util.MongoUtil(MongoDB=server, username=username,
                                             password=password, authSource=authSource, db=database,
                                             readPreference=readPreference)
        self.file_manager = file_util.FileUtil()
        self.max_entries = max_entries
        self.verbose = verbose
        self.client, self.db, self.collection = self.mongo_manager.con_db(collection_str)
        self.collation = Collation(locale='en', strength=CollationStrength.SECONDARY)
        self.collection_str = collection_str

    def get_id_by_name(self, names):
        """Get sabio compound id given compound name
        
        Args:
            name (:obj:`list` of :obj:`str`): names of the compound

        Return:
            (:obj:`list` of :obj:`int`): sabio compound ids
        """
        result = []
        name_field = 'name'
        synonym_field = 'synonyms'
        pos_0 = {name_field: {'$in': names}}
        pos_1 = {synonym_field: {'$in': names}}
        query = {'$or': [pos_0, pos_1]}
        projection = {'_id': 1}
        docs = self.collection.find(filter=query, projection=projection, collation=self.collation)
        for doc in docs:
            print(doc)
            result.append(doc['_id'])
        return result