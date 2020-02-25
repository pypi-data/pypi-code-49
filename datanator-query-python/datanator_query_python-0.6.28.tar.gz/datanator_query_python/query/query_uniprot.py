import pandas
import requests
from pymongo.errors import OperationFailure
import io
from datanator_query_python.util import mongo_util
from datanator_query_python.query import query_kegg_organism_code
from pymongo.collation import Collation, CollationStrength


class QueryUniprot:

    def __init__(self, username=None, password=None, server=None, authSource='admin',
                 database='datanator', collection_str=None, readPreference='nearest'):

        self.mongo_manager = mongo_util.MongoUtil(MongoDB=server, username=username,
                                                  password=password, authSource=authSource, db=database,
                                                  readPreference=readPreference)
        self.koc_manager = query_kegg_organism_code.QueryKOC(username=username, password=password,
        server=server, authSource=authSource, collection_str='kegg_organism_code', readPreference=readPreference)
        self.client, self.db, self.collection = self.mongo_manager.con_db(collection_str)
        self.collation = Collation(locale='en', strength=CollationStrength.SECONDARY)

    def get_doc_by_locus(self, locus, projection={'_id':0}):
        """Get preferred gene name by locus name
        
        Args:
            locus (:obj:`str`): Gene locus name
            projection (:obj:`dict`, optional): MongoDB query projection. Defaults to {'_id':0}.

        Return:
            (:obj:`tuple` of :obj:`Iter` and `int`): pymongo cursor object and number of documents.
        """
        con_0 = {'gene_name': locus}
        con_1 = {'gene_name_alt': locus}
        con_2 = {'gene_name_orf': locus}
        con_3 = {'gene_name_oln': locus}
        query = {'$or': [con_0, con_1, con_2, con_3]}
        docs = self.collection.find(filter=query, projection=projection, collation=self.collation)
        count = self.collection.count_documents(query, collation=self.collation)
        return docs, count

    def get_gene_protein_name_by_oln(self, oln, species=None, projection={'_id': 0}):
        """Get documents by ordered locus name
        
        Args:
            oln (:obj:`str`): Ordered locus name.
            species (:obj:`list`): NCBI taxonomy id. Defaults to None.
            projection (:obj:`dict`, optional): Pymongo projection. Defaults to {'_id': 0}.

        Return:
            (:obj:`tuple` of :obj:`str`): gene_name and protein_name
        """
        if species is None:
            query = {'gene_name_oln': oln}
        else:
            query = {'$and': [{'gene_name_oln': oln}, {'ncbi_taxonomy_id': {'$in': species}}]}
        doc = self.collection.find_one(filter=query, projection=projection, collation=self.collation)
        if doc is None:
            return None, None
        else:
            return doc['gene_name'], doc['protein_name']

    def get_protein_name_by_gn(self, gene_name, species=None, projection={'_id': 0}):
        """Get documents by gene name.
        
        Args:
            gene_name (:obj:`str`): gene name.
            species (:obj:`list`): NCBI taxonomy id. Defaults to None.
            projection (:obj:`dict`, optional): Pymongo projection. Defaults to {'_id': 0}.

        Return:
            (:obj:`tuple` of :obj:`str`): gene_name and protein_name
        """
        con_0 = {'gene_name': gene_name}
        con_1 = {'gene_name_alt': gene_name}
        con_2 = {'gene_name_orf': gene_name}
        con_3 = {'gene_name_oln': gene_name}
        name_search = {'$or': [con_0, con_1, con_2, con_3]}
        if species is None:
            query = {'gene_name': gene_name}
        else:
            query = {'$and': [name_search, {'ncbi_taxonomy_id': {'$in': species}}]}
        doc = self.collection.find_one(filter=query, projection=projection, collation=self.collation)
        if doc is None:
            return None
        else:
            return doc['protein_name']

    def get_gene_protein_name_by_embl(self, embl, species=None, projection={'_id': 0}):
        """Get documents by EMBL or RefSeq.
        
        Args:
            embl (:obj:`list`): EMBL information.
            species (:obj:`list`): NCBI taxonomy id. Defaults to None.
            projection (:obj:`dict`, optional): Pymongo projection. Defaults to {'_id': 0}.

        Return:
            (:obj:`tuple` of :obj:`str`): gene_name and protein_name
        """
        con_0 = {'sequence_refseq': {'$in': embl}}
        con_1 = {'sequence_embl': {'$in': embl}}
        if species is None:
            query = {'$and': [con_0, con_1]}
        else:
            query = {'$and': [con_0, con_1, {'ncbi_taxonomy_id': {'$in': species}}]}
        doc = self.collection.find_one(filter=query, projection=projection, collation=self.collation)
        if doc is None:
            return None, None
        else:
            return doc['gene_name'], doc['protein_name']
        
    def get_names_by_gene_name(self, gene_name):
        """Get standard gene name by gene name.
        
        Args:
            gene_name (:obj:`list` of :obj:`str`): list of gene names belonging to one protein.

        Return:
            (:obj:`tuple` of :obj:`str`): standard gene_name, protein_name
        """
        query = {'gene_name': {'$in': gene_name}}
        projection = {'uniprot_id': 1, 'gene_name': 1, 'protein_name': 1}
        doc = self.collection.find_one(filter=query, projection=projection, collation=self.collation)
        if doc is None:
            return None, None
        else:
            return doc['gene_name'], doc['protein_name']

    def get_id_by_org_gene(self, org_gene):
        """Convert kegg org_gene into uniprot id.
        
        Args:
            org_gene (:obj:`str`): Kegg org_gene format, e.g. aly:ARALYDRAFT_486312.

        Return:
            (:obj:`str`): Uniprot ID.
        """
        _list = org_gene.split(':')
        org = _list[0]
        gene_name = _list[1]
        con_0 = {'gene_name': gene_name}
        con_1 = {'gene_name_alt': gene_name}
        con_2 = {'gene_name_orf': gene_name}
        con_3 = {'gene_name_oln': gene_name}
        name_search = {'$or': [con_0, con_1, con_2, con_3]}
        ncbi_id = self.koc_manager.get_ncbi_by_org_code(org)
        query = {'$and': [name_search, {'ncbi_taxonomy_id': ncbi_id}]}
        projection = {'_id': 0, 'uniprot_id': 1}
        docs = self.collection.find(filter=query, projection=projection, collation=self.collation)
        count = self.collection.count_documents(query, collation=self.collation)
        return docs, count

    def get_info_by_entrez_id(self, entrez_id):
        """Get protein info by gene entrez information
        
        Args:
            entrez_id (:obj:`str`): Gene entrez id.

        Return:
            (:obj:`str`): Uniprot ID.
        """
        query = {'entrez_id': entrez_id}
        projection = {'_id': 0, 'uniprot_id': 1}
        doc = self.collection.find_one(filter=query, projection=projection, collation=self.collation)
        if doc is None:
            return None
        else:
            return doc['uniprot_id']
        
    def get_similar_proteins(self, uniprot_id, identity=90):
        """This section provides links to proteins that are similar to the protein sequence(s) 
        described in this entry at different levels of sequence identity thresholds (100%, 90% and 50%)
        based on their membership in UniProt Reference Clusters (UniRef).
        (Queries MongoDB first, if not in MongoDB, query uniprot.org, insert results into the 
        corresponding document).

        Args:
            uniprot_id (:obj:`str`): Uniprot ID of the protein
            identity (:obj:`float`, optional): Identity score. Defaults to 90 (%). Can only be 100, 90, or 50. 

        Return:
            (:obj:`list` of :obj:`str`): List of similar proteins' uniprot IDs.
        """
        def query_update_return(uniprot_id, identity, key):
            """search on uniprot.org and insert results into mongo.
            """
            _list = self.get_similar_proteins_from_uniprot(uniprot_id, identity=identity)
            try:
                self.collection.update_one({'uniprot_id': uniprot_id},
                                            {'$set': {'similar_proteins.{}'.format(key): _list}}, collation=self.collation, upsert=False)
            except OperationFailure:
                return _list
            return _list

        projection = {'uniprot_id': 1, 'similar_proteins': 1}
        doc = self.collection.find_one({'uniprot_id': uniprot_id}, projection=projection,
                                        collation=self.collation)
        if doc is None:
            return self.get_similar_proteins_from_uniprot(uniprot_id, identity=identity)
        key = 'identity_' + str(identity)
        similar_proteins = doc.get('similar_proteins')
        if similar_proteins is not None:            
            proteins = similar_proteins.get(key)
            if proteins is not None: # in mongo
                return proteins
            else: # search on uniprot.org and insert results into mongo
                return query_update_return(uniprot_id, identity, key)
        else:
            return query_update_return(uniprot_id, identity, key)

    def get_similar_proteins_from_uniprot(self, uniprot_id, identity=90, limit=10):
        """This section provides links to proteins that are similar to the protein sequence(s) 
        described in this entry at different levels of sequence identity thresholds (100%, 90% and 50%)
        based on their membership in UniProt Reference Clusters (UniRef).

        Args:
            uniprot_id (:obj:`str`): Uniprot ID of the protein
            identity (:obj:`float`, optional): Identity score. Defaults to 90 (%). Can only be 100, 90, or 50.
            limit (:obj:`int`, optional): Max number of results. Defaults to 10.

        Return:
            (:obj:`list` of :obj:`str`): List of similar proteins' uniprot IDs.
        """
        if identity not in [100, 90, 50]:
            return []
        fields = '&columns=id'
        percent = identity / 100
        url = 'https://www.uniprot.org/uniprot/?query=cluster:(uniprot:{}*%20identity:{})%20not%20id:{}'.format(uniprot_id, percent, uniprot_id)
        url += '&sort=score'
        url += fields
        url += '&format=tab'
        url += '&compress=no'
        url += '&limit={}'.format(limit)
        try:
            response = requests.get(url, stream=False)
            response.raise_for_status()
        except requests.exceptions.ConnectionError:
            pass         

        try:
            data = pandas.read_csv(io.BytesIO(response.content), delimiter='\t', encoding='utf-8', low_memory=False)
        except pandas.errors.EmptyDataError:
            return []
        except UnboundLocalError:
            return []
        data.columns = ['uniprot_id']
        return data['uniprot_id'].tolist()        