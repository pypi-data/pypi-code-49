from datanator_query_python.util import mongo_util
from pymongo.collation import Collation, CollationStrength


class QueryKO:

    def __init__(self, username=None, password=None, server=None, authSource='admin',
                 database='datanator', max_entries=float('inf'), verbose=True,
                 readPreference='nearest'):

        mongo_manager = mongo_util.MongoUtil(MongoDB=server, username=username,
                                             password=password, authSource=authSource, db=database,
                                             readPreference=readPreference)
        self.max_entries = max_entries
        self.verbose = verbose
        self.client, self.db, self.collection = mongo_manager.con_db(
            'kegg_orthology')
        self.collation = Collation(locale='en', strength=CollationStrength.SECONDARY)

    def get_ko_by_name(self, name):
        '''Get a gene's ko number by its gene name

        Args:
            name: (:obj:`str`): gene name
                
        Returns:
            result: (:obj:`str`): ko number of the gene
        '''
        query = {'gene_name': name}
        projection = {'gene_name': 1, 'kegg_orthology_id': 1}
        collation = {'locale': 'en', 'strength': 2}
        docs = self.collection.find_one(
            filter=query, projection=projection, collation=collation)
        if docs != None:
        	return docs['kegg_orthology_id']
        else:
        	return None

    def get_def_by_kegg_id(self, kegg_id):
        """Get kegg definition by kegg id
        
        Args:
            kegg_id (:obj:`str`): kegg orthology

        Returns:
            (:obj:`list` of :obj:`str`): list of kegg orthology definitions
        """
        query = {'kegg_orthology_id': kegg_id}
        projection = {'definition.name': 1, '_id': 0}
        doc = self.collection.find_one(filter=query, projection=projection)
        if doc is None:
            return [None]
        definitions = doc['definition']['name']
        return definitions

    def get_loci_by_id_org(self, kegg_id, org, gene_id):
        """Get ortholog locus id given kegg_id, organism code and gene_id.
        
        Args:
            kegg_id (:obj:`str`): Kegg ortholog id.
            org (:obj:`str`): Kegg organism code.
            gene_id (:obj:`str`): Gene id.

        Return:
            (:obj:`str`): locus id.
        """
        con_0 = {'kegg_orthology_id': kegg_id}
        con_1 = {'gene_ortholog.organism': org}
        con_2 = {'gene_ortholog.genetic_info.gene_id': gene_id}
        query = {'$and': [con_0, con_1, con_2]}
        projection = {'_id': 0, 'gene_ortholog.$': 1}
        doc = self.collection.find_one(filter=query, projection=projection, collation=self.collation)
        if doc is None:
            return {}
        else:
            obj = doc['gene_ortholog'][0]['genetic_info']
            return next((item['locus_id'] for item in obj if item["gene_id"] == gene_id), None)

    def get_meta_by_kegg_id(self, kegg_ids, projection={'_id': 0, 'gene_ortholog': 0}):
        """Get meta given kegg ids
        
        Args:
            kegg_ids (:obj:`list` of :obj:`str`): List of kegg ids.
            projection (:obj:`dict`): MongoDB result projection.

        Return:
            (:obj:`tuple` of :obj:`pymongo.Cursor` and :obj:`int`): pymongo Cursor obj and number of documents found.
        """
        projection['__order'] = 0
        query = {'kegg_orthology_id': {'$in': kegg_ids}}
        pipeline = [
             {'$match': {'kegg_orthology_id': {'$in': kegg_ids}}},
             {'$addFields': {"__order": {'$indexOfArray': [kegg_ids, "$kegg_orthology_id" ]}}},
             {'$sort': {"__order": 1}},
             {"$project": projection}
            ]
        docs = self.collection.aggregate(pipeline, collation=self.collation)
        count = self.collection.count_documents(query, collation=self.collation)
        return docs, count