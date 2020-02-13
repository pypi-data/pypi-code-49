from datanator_query_python.util import mongo_util, chem_util, file_util
from pymongo.collation import Collation, CollationStrength
from . import query_nosql, query_taxon_tree, query_sabio_compound
import json
import re
from pymongo import ASCENDING, DESCENDING


class QuerySabioOld(query_nosql.DataQuery):
    '''Queries specific to sabio_rk collection
    '''

    def __init__(self, cache_dirname=None, MongoDB=None, replicaSet=None, db='datanator',
                 collection_str='sabio_rk_old', verbose=False, max_entries=float('inf'), username=None,
                 password=None, authSource='admin', readPreference='nearest'):
        self.max_entries = max_entries
        super().__init__(cache_dirname=cache_dirname, MongoDB=MongoDB,
                        replicaSet=replicaSet, db=db,
                        verbose=verbose, max_entries=max_entries, username=username,
                        password=password, authSource=authSource, readPreference=readPreference)
        self.chem_manager = chem_util.ChemUtil()
        self.file_manager = file_util.FileUtil()
        self.client, self.db_obj, self.collection = self.con_db(collection_str)
        self.collection_str = collection_str
        self.taxon_manager = query_taxon_tree.QueryTaxonTree(username=username, password=password,
        authSource=authSource, readPreference=readPreference, MongoDB=MongoDB)
        self.compound_manager = query_sabio_compound.QuerySabioCompound(server=MongoDB, database=db,
                                                                        username=username, password=password, 
                                                                        readPreference=readPreference, authSource=authSource)
        self.collation = Collation(locale='en', strength=CollationStrength.SECONDARY)

    def get_kinlaw_by_environment(self, taxon=None, taxon_wildtype=None, ph_range=None, temp_range=None,
                          name_space=None, param_type=None, projection={'_id': 0}):
        """get kinlaw info based on experimental conditions
        
        Args:
            taxon (:obj:`list`, optional): list of ncbi taxon id
            taxon_wildtype (:obj:`list` of :obj:`bool`, optional): True indicates wildtype and False indicates mutant
            ph_range (:obj:`list`, optional): range of pH
            temp_range (:obj:`list`, optional): range of temperature
            name_space (:obj:`dict`, optional): cross_reference key/value pair, i.e. {'ec-code': '3.4.21.62'}
            param_type (:obj:`list`, optional): possible values for parameters.type
            projection (:obj:`dict`, optional): mongodb query result projection

        Returns:
            (:obj:`tuple`) consisting of 
            docs (:obj:`list` of :obj:`dict`): list of docs;
            count (:obj:`int`): number of documents found 
        """
        all_constraints = []
        taxon_wildtype = [int(x) for x in taxon_wildtype]
        if taxon:
            all_constraints.append({'taxon_id': {'$in': taxon}})
        if taxon_wildtype:
            all_constraints.append({'taxon_wildtype': {'$in': taxon_wildtype}})
        if ph_range:
            all_constraints.append({'ph': {'$gte': ph_range[0], '$lte': ph_range[1]}})
        if temp_range:
            all_constraints.append({'temperature': {'$gte': temp_range[0], '$lte': temp_range[1]}})
        if name_space:
            key = list(name_space.keys())[0]
            val = list(name_space.values())[0]
            all_constraints.append({"resource": {'$elemMatch': {'namespace': key, 'id': val}}})
        if param_type:
            all_constraints.append({'parameter': {'$elemMatch': {'type': {'$in': param_type}}}})

        query = {'$and': all_constraints}
        docs = self.collection.find(filter=query, projection=projection)
        count = self.collection.count_documents(query)
        return docs, count

    def get_reaction_doc(self, kinlaw_id, projection={'_id': 0}):
        '''Find a document on reaction with the kinlaw_id
        Args:
            kinlaw_id (:obj:`list` of :obj:`int`) list of kinlaw_id to search for
            projection (:obj:`dict`): mongodb query result projection

        Returns:
            (:obj:`tuple`) consisting of 
            docs (:obj:`list` of :obj:`dict`): list of docs;
            count (:obj:`int`): number of documents found
        '''
        query = {'kinlaw_id': {'$in': kinlaw_id}}
        docs = self.collection.find(filter=query, projection=projection)
        count = self.collection.count_documents(query)
        return docs, count

    def get_kinlawid_by_rxn(self, substrates, products, dof=0):
        ''' Find the kinlaw_id defined in sabio_rk using 
            rxn participants' inchikey

            Args:
                substrates (:obj:`list`): list of substrates' inchikey
                products (:obj:`list`): list of products' inchikey
                dof (:obj:`int`, optional): degree of freedom allowed (number of parts of
                                  inchikey to truncate); the default is 0 

            Return:
                rxns: list of kinlaw_ids that satisfy the condition
                [id0, id1, id2,...,  ]
        '''
        result = []
        substrate = 'reaction_participant.substrate_aggregate'
        product = 'reaction_participant.product_aggregate'
        projection = {'kinlaw_id': 1, '_id': 0}
        if dof == 0:
            substrates = substrates
            products = products
        elif dof == 1:
            substrates = [re.compile('^' + x[:-2]) for x in substrates]
            products = [re.compile('^' + x[:-2]) for x in products]
        else:
            substrates = [re.compile('^' + x[:14]) for x in substrates]
            products = [re.compile('^' + x[:14]) for x in products]

        constraint_0 = {substrate: {'$all': substrates}}
        constraint_1 = {product: {'$all': products}}
        query = {'$and': [constraint_0, constraint_1]}
        docs = self.collection.find(filter=query, projection=projection)
        for doc in docs:
            result.append(doc['kinlaw_id'])
        return result

    def get_kinlaw_by_rxn(self, substrates, products, dof=0,
                          projection={'kinlaw_id': 1, '_id': 0},
                          bound='loose'):
        ''' Find the kinlaw_id defined in sabio_rk using 
            rxn participants' inchikey

            Args:
                substrates (:obj:`list`): list of substrates' inchikey
                products (:obj:`list`): list of products' inchikey
                dof (:obj:`int`, optional): degree of freedom allowed (number of parts of
                                  inchikey to truncate); the default is 0
                projection (:obj:`dict`): pymongo query projection 
                bound (:obj:`str`): limit substrates/products to include only input values

            Return:
                (:obj:`list` of :obj:`dict`): list of kinlaws that satisfy the condition
        '''
        substrate = 'reaction_participant.substrate_aggregate'
        product = 'reaction_participant.product_aggregate'
        if dof == 0:
            substrates = substrates
            products = products
        elif dof == 1:
            substrates = [re.compile('^' + x[:-2]) for x in substrates]
            products = [re.compile('^' + x[:-2]) for x in products]
        else:
            substrates = [re.compile('^' + x[:14]) for x in substrates]
            products = [re.compile('^' + x[:14]) for x in products]

        if bound == 'loose':
            constraint_0 = {substrate: {'$all': substrates}}
            constraint_1 = {product: {'$all': products}}
        else:
            constraint_0 = {substrate: substrates}
            constraint_1 = {product: products}            
        query = {'$and': [constraint_0, constraint_1]}
        docs = self.collection.find(filter=query, projection=projection)
        count = self.collection.count_documents(query)
        return count, docs

    def get_kinlaw_by_entryid(self, entry_id):
        """Find reactions by sabio entry id
        
        Args:
            entry_id (:obj:`int`): entry_id

            Return:
                (:obj:`dict`): {'kinlaw_id': [], 'substrates': [], 'products': []}
        """
        result = {}
        kinlaw_id = []
        substrates = []
        products = []
        constraint_0 = {'namespace': 'sabiork.reaction', 'id': str(entry_id)}
        query = {'resource': {'$elemMatch': constraint_0}}
        projection = {'_id': 0, 'kinlaw_id': 1, 'reaction_participant.substrate_aggregate': 1,
                     'reaction_participant.product_aggregate': 1}
        docs = self.collection.find(filter=query, projection=projection)
        for doc in docs:
            kinlaw_id.append(doc['kinlaw_id'])
            substrates.append(doc['reaction_participant'][3]['substrate_aggregate'])
            products.append(doc['reaction_participant'][4]['product_aggregate'])

        result['kinlaw_id'] = kinlaw_id
        result['substrates'] = substrates
        result['products'] = products
        return result


    def get_info_by_entryid(self, entry_id, target_organism=None, size=10, last_id=0):
        """Find reactions by sabio entry id, return all information
        
        Args:
            entry_id (:obj:`int`): entry_id
            target_organism (:obj:`str`): the organism in which the reaction occurs
            size (:obj:`int`): pagination page size
            last_id (:obj:`int`) the largest kinlaw id from previous page

        Return:
            (:obj:`list` of :obj:`dict`): list of documents of entry id
        """
        constraint_0 = {'namespace': 'sabiork.reaction', 'id': str(entry_id)}
        query = {'resource': {'$elemMatch': constraint_0}}
        projection = {'_id': 0}
        sort = [('kinlaw_id', ASCENDING)]
        taxon_name = None
        distance = -1
        result = []
        docs = self.collection.find(filter=query, projection=projection, sort=sort, limit=size)
        if target_organism is not None:  # need distance information
            for i, doc in enumerate(docs):
                if i == 0:
                    taxon_name = doc['taxon_name']
                    _, dist = self.taxon_manager.get_common_ancestor(taxon_name, target_organism)
                    distance = dist[0]
                    doc['taxon_distance'] = distance
                    result.append(doc)
                else:
                    doc['taxon_distance'] = distance
                    result.append(doc)
        else:
            for doc in docs:
                result.append(doc)
        return result

    def get_kinlaw_by_rxn_name(self, substrates, products,
                                projection={'kinlaw_id': 1},
                                bound='loose'):
        ''' Find the kinlaw_id defined in sabio_rk using 
            rxn participants' names

            Args:
                substrates (:obj:`list`): list of substrates' names
                products (:obj:`list`): list of products' names
                projection (:obj:`dict`): pymongo query projection 
                bound (:obj:`str`): limit substrates/products to include only input values

            Return:
                (:obj:`list` of :obj:`dict`): list of kinlaws that satisfy the condition
        '''
        sub_id_field = 'reaction_participant.substrate.sabio_compound_id'
        pro_id_field = 'reaction_participant.product.sabio_compound_id'
        bounded_s = {'reaction_participant.substrate': {'$size': len(substrates)}}
        bounded_p = {'reaction_participant.product': {'$size': len(products)}}

        substrate_ids = self.compound_manager.get_id_by_name(substrates)
        product_ids = self.compound_manager.get_id_by_name(products)

        s_constraint = {sub_id_field: {'$all': substrate_ids}}
        p_constraint = {pro_id_field: {'$all': product_ids}}

        if bound == 'loose':
            query = {'$and': [s_constraint, p_constraint]}
        else:
            query = {'$and': [s_constraint, p_constraint, bounded_s, bounded_p]}
        docs = self.collection.find(filter=query, projection=projection)
        count = self.collection.count_documents(query)
        return count, docs

    def get_unique_entries(self):
        """Get number of unique curated entries.

        Return:
            (:obj:`int`): Number of unique entries.
        """
        return len(self.collection.distinct('kinlaw_id'))

    def get_unique_organisms(self):
        """Get number of unique organisms.

        Return:
            (:obj:`int`): Number of unique organisms.
        """
        return len(self.collection.distinct('taxon_id'))

    def get_rxn_with_prm(self, kinlaw_ids, _from=0, size=10):
        """Given a list of kinlaw ids, return documents where
        kinlaw has at least one Km or kcat.
        
        Args:
            kinlaw_ids (:obj:`list` of :obj:`int`): List of kinlaw IDs.
            _from (:obj:`int`): record offset. Defaults to 0.
            size (:obj:`int`): number of records to be returned. Defaults to 10.

        Return:
            (:obj:`tuple` of :obj:`list` of :obj:`dict` and :obj:`list` of :obj:`int`): list of rxn documents, and ids that have parameter
        """
        result = []
        have = []
        con_0 = {'parameter.observed_name': {'$in': ['Km', 'kcat']}}
        con_1 = {'kinlaw_id': {'$in': kinlaw_ids}}
        query = {'$and': [con_0, con_1]}
        projection = {'_id': 0}
        cursor = self.collection.find(filter=query, projection=projection, collation=self.collation,
                                      skip=_from, limit=size)
        if cursor is None:
            return result, have
        for r in cursor:
            result.append(r)
            have.append(r['kinlaw_id'])
        return result, have