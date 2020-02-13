'''
@author: majid
'''

from p_connector_dfg.Utilities import Utilities
from pm4py.objects.log.importer.xes import factory as xes_importer_factory
import pandas as pd
import numpy as np
from random import randint
from p_connector_dfg.PMA import PMA

class privacyPreserving(object):
    '''
    Applying privacy preserving technique and/or see the results
    '''

    def __init__(self, log):
        '''
        Constructor
        '''
        self.log = xes_importer_factory.apply(log)

    def fake_id_generator(self, n):
        id_list = []
        digit_number = len(str(n))
        firstId = self.random_with_N_digits(digit_number)
        for rows in range(n):
            fake_id_int = firstId + rows
            fake_id_str = f"{fake_id_int:0{digit_number}d}"
            id_list.append(fake_id_str)
        return id_list

    def random_with_N_digits(self, n):
        range_start = 10 ** (n - 1)
        range_end = (10 ** n) - 1
        return randint(range_start, range_end)

    def apply_privacyPreserving(self, key, pma_path, pma_method, pma_desired_analyses,  event_log, **keyword_param):
        
        utils = Utilities(self.log)
        connectorBasic_DF, activityList = utils.create_basic_matrix_connector_activity(relation_depth = keyword_param['relation_depth'], trace_length = keyword_param['trace_length'], trace_id = keyword_param['trace_id'])

        #adding fake id
        connectorBasic_DF_connector = connectorBasic_DF.copy()
        row_number = connectorBasic_DF_connector.shape[0]
        fake_ids = self.fake_id_generator(row_number)
        connectorBasic_DF_connector['new_id'] = np.array(fake_ids)

        #adding previous id
        prev_id = []
        digit_number = len(str(row_number))
        first_prev_id = f"{0:0{digit_number}d}"
        for index, item in enumerate(connectorBasic_DF_connector['prev_activity']):
            if (item == ":Start:"):
                prev_id.append(first_prev_id)
                previous_id = connectorBasic_DF_connector['new_id'][index]
            else:
                prev_id.append(previous_id)
                previous_id = connectorBasic_DF_connector['new_id'][index]
        connectorBasic_DF_connector['prev_id'] = np.array(prev_id)


        #Adding connector column
        connector = []
        for indexDF, rowDF in connectorBasic_DF_connector.iterrows():
            print("-----------", rowDF)
            connector_value = Utilities.AES_ECB_Encrypt((rowDF['prev_id'] +'::'+ rowDF['new_id']).encode('utf-8'),key)
            connector.append(connector_value)
        connectorBasic_DF_connector['connector'] = np.array(connector)

        # connectorBasic_DF.to_csv(connector_dataStructure_path, sep=',', encoding='utf-8')
        # connectorBasic_DF_connector.to_csv(connector_dataStructure_path, sep=',', encoding='utf-8')

        #del new_id and prev_id
        del connectorBasic_DF_connector['new_id']
        del connectorBasic_DF_connector['prev_id']

        #shuffle the order
        connectorBasic_DF_connector = connectorBasic_DF_connector.sample(frac=1).reset_index(drop=True)


        #create xml from the abstract
        pma = PMA()
        pma.set_values(origin=event_log, method=pma_method, desired_analyses=pma_desired_analyses, data=connectorBasic_DF_connector)
        pma.create_xml(pma_path)

    
        # if(show_final_result):
        #     read_external_connector_ds = False
        #     connector_dataStructure_path = ".\intermediate_results\ConnectorStructure_Activity.csv"
        #     activity_activity_matrix_path = ".\intermediate_results\ActActMatrix.csv"
        #     export_ActActMatrix = True
        #     visualizeResult = True
        #     encryptedResult = False
        #     frequencyThreshold = 0.0
        #
        #     self.result_maker(read_external_connector_ds, export_ActActMatrix, visualizeResult, encryptedResult, frequencyThreshold,
        #                                             connector_dataStructure_path = connector_dataStructure_path, activity_activity_matrix_path =activity_activity_matrix_path,
        #                                             connector_ds = connectorBasic_DF)

    
    def result_maker(self, read_external_connector_ds, export_ActActMatrix, visualizeResult, encryptedResult, frequencyThreshold, **keyword_param):
        
        if(read_external_connector_ds):
            connector_dataStructure = keyword_param['connector_dataStructure_path']
            snBasic_DF = pd.read_csv(connector_dataStructure)
            snBasic_DF = snBasic_DF.iloc[:,1:]
        else:
            snBasic_DF = keyword_param['connector_ds']

        ActActMatrix, activityList = Utilities.makeDFG_connector(snBasic_DF, frequencyThreshold, encryption=encryptedResult, visualization=visualizeResult, key=keyword_param['key'])

        ActActMatrix_pd = pd.DataFrame(ActActMatrix, index=activityList, columns=activityList)

        if(export_ActActMatrix):
            ActActMatrix_pd.to_csv(keyword_param['activity_activity_matrix_path'], sep=',', encoding='utf-8')

    def result_maker_pma(self, filepath, encryptedResult, visualizeResult, export_ActActMatrix, frequencyThreshold, dfg_path, **keyword_param):
        pma = PMA()
        xml_data = pma.read_xml(filepath)

        data = pd.DataFrame(xml_data['data'])

        ActActMatrix, activityList = Utilities.makeDFG_connector(data, frequencyThreshold, dfg_path,
                                                                 encryption=encryptedResult,
                                                                 visualization=visualizeResult,key=keyword_param['key'])

        ActActMatrix_pd = pd.DataFrame(ActActMatrix, index=activityList, columns=activityList)

        if (export_ActActMatrix):
            ActActMatrix_pd.to_csv(keyword_param['activity_activity_matrix_path'], sep=',', encoding='utf-8')
            
            
            
            