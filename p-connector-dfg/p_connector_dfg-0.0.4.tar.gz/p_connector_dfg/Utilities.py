'''
@author: majid
'''

import pandas as pd
import hashlib
from Crypto.Cipher import AES
import numpy as np
from pm4py.visualization.dfg import factory as dfg_vis_factory


class Utilities():
    '''
    classdocs
    '''
    
    def __init__(self, log):
        self.log = log
        self.resourceSet = set()
        self.activitySet = set()
        self.resourceList = list()
        self.activityList = list()
        
    
    def setResourceSetList(self, snMatrix):
        unique_resources = snMatrix['resource'].unique()
        self.resourceSet = set(unique_resources)
        self.resourceList = list(self.resourceSet)
        self.resourceList.sort() 
     
    def setActivitySetList(self, snMatrix):
        unique_activities = snMatrix['activity'].unique()
        self.activitySet = set(unique_activities)
        self.activityList = list(self.activitySet)
        self.activityList.sort() 
        
    def setResourceSetList_previous(self, snMatrix):
        unique_resources = snMatrix['resource'].unique()
        unique_next_resources = snMatrix['prev_resource'].unique()
        self.resourceSet = set(unique_resources) | set(unique_next_resources)
        self.resourceList = list(self.resourceSet)
        self.resourceList.sort()
    
    def setActivitySetList_previous(self, snMatrix):
        unique_activities = snMatrix['activity'].unique()
        unique_next_activities = snMatrix['prev_activity'].unique()
        self.activitySet = set(unique_activities) | set(unique_next_activities)
        self.activityList = list(self.activitySet)
        self.activityList.sort()
        
    
    def getResourceSet(self):
        return self.resourceSet
    
    def getActivitySet(self):
        return self.activitySet
    
    def getResourceList(self):
        return self.resourceList
    
    def getActivityList(self):
        return self.activityList
        
    
    
    def create_full_matrix_connector(self, **keyword_param):
        snFullList = []
        main_counter = 0
        for case_index, case in enumerate(self.log):
            sndict = {}
            sndict['prev_activity'] = ":Start:"
            sndict['prev_resource'] = ":Start:"
            for event_index, event in enumerate(case):
                
                try:
                    sndict['activity'] = event["concept:name"]
                except KeyError:
                    sndict['activity'] = ":None:"
                
                try:
                    sndict['resource'] = event["org:resource"]
                except KeyError:
                    sndict['resource'] = ":None:"
                
                if(keyword_param['relation_depth']):
                    sndict['relation_depth'] = "1"
                if(keyword_param['trace_length']):
                    sndict['trace_length'] = len(case)
                if(keyword_param['trace_id']):
                    sndict['trace0_id'] = case_index
                snFullList.append(sndict)
                
                sndict = {}
                sndict['prev_activity'] = snFullList[main_counter]['activity'] 
                sndict['prev_resource'] = snFullList[main_counter]['resource']   
                
                main_counter += 1
                
        
        full_df = pd.DataFrame(snFullList) 
        
        if(keyword_param['resource_encryption'] == True):
            for indexDF, rowDF in full_df.iterrows():
                print("-----------", rowDF)
                full_df.loc[indexDF,'resource'] = Utilities.AES_ECB_Encrypt(full_df.loc[indexDF,'resource'].encode('utf-8'),keyword_param['key'])
                if(full_df.loc[indexDF,'prev_resource'] != ":Start:"):
                    full_df.loc[indexDF,'prev_resource'] = Utilities.AES_ECB_Encrypt(full_df.loc[indexDF,'prev_resource'].encode('utf-8'),keyword_param['key'])
         
        Utilities.setResourceSetList_previous(self, full_df)   
        Utilities.setActivitySetList_previous(self, full_df)
        
        return full_df, self.resourceList, self.activityList
    
    
    def create_basic_matrix_connector_activity(self, **keyword_param):
        snBasicList = []
        main_counter = 0
        for case_index, case in enumerate(self.log):
            sndict = {}
            sndict['prev_activity'] = ":Start:"
            for event_index, event in enumerate(case):
                
                try:
                    sndict['activity'] = event["concept:name"]
                except KeyError:
                    sndict['activity'] = ":None:"
                
                if(keyword_param['relation_depth']):
                    sndict['relation_depth'] = "1"
                if(keyword_param['trace_length']):
                    sndict['trace_length'] = len(case)
                if(keyword_param['trace_id']):
                    sndict['trace_id'] = case_index
                snBasicList.append(sndict)
                
                sndict = {}
                sndict['prev_activity'] = snBasicList[main_counter]['activity']    
                
                main_counter += 1
                
        
        basic_df = pd.DataFrame(snBasicList) 
        
        Utilities.setActivitySetList_previous(self, basic_df)
        
        return basic_df, self.activityList
    

    def make_hash(self, value):
        m = hashlib.sha256()                      
        value = value.encode('utf-8')
        m.update(value)
        hexvalue = m.hexdigest()
        return hexvalue

    @staticmethod
    def AES_ECB_Encrypt(data,key):
        # key = 'M4J!DPASSWORD!!!'
        cipher = AES.new(key.encode('utf8'), AES.MODE_ECB)
        length = 16 - (len(data) % 16)
        data += bytes([length])*length
        msg = cipher.encrypt(data)
        result = msg.hex()
        return result
    
    @staticmethod
    def AES_ECB_Decrypt(enc_data,key):
        # key = 'M4J!DPASSWORD!!!'
        decipher = AES.new(key.encode('utf8'), AES.MODE_ECB)
        msg_dec = decipher.decrypt(bytes.fromhex(enc_data))
        msg_dec = msg_dec[:-msg_dec[-1]]
        return msg_dec.decode('utf-8')
    
    def resourceEncryption(self, snDF,key):
        for indexDF, rowDF in snDF.iterrows():
            print("-----------", rowDF)
            snDF.loc[indexDF,'resource'] = Utilities.AES_ECB_Encrypt(self, snDF.loc[indexDF,'resource'].encode('utf-8'),key)
            snDF.loc[indexDF,'next_resource'] = Utilities.AES_ECB_Encrypt(self, snDF.loc[indexDF,'next_resource'].encode('utf-8'),key)
        
        Utilities.setResourceSetList(self, snDF)   
        return snDF, self.resourceList
    
    def resourceEncryption_connector(self, snDF,key):
        for indexDF, rowDF in snDF.iterrows():
            print("-----------", rowDF)
            snDF.loc[indexDF,'resource'] = Utilities.AES_ECB_Encrypt(self, snDF.loc[indexDF,'resource'].encode('utf-8'),key)
            snDF.loc[indexDF,'prev_resource'] = Utilities.AES_ECB_Encrypt(self, snDF.loc[indexDF,'prev_resource'].encode('utf-8'),key)
        
        Utilities.setResourceSetList_previous(self, snDF)    
        return snDF, self.resourceList
    
    def resourceDecryption(self, resourceList,key):
        
        Decrypted_resourceList = list()
        for resource in resourceList:
            print("-----------", resource)
            Decrypted_resourceList.append(Utilities.AES_ECB_Decrypt(self, resource,key))
            
        return Decrypted_resourceList
            
    
    @staticmethod
    def makeDFG_connector(ConnectorBasicStructure, frequency_threshold, dfg_path, **keyword_param):
        
        unique_activities = ConnectorBasicStructure['activity'].unique()
        unique_next_activities = ConnectorBasicStructure['prev_activity'].unique()
        activitySet = set(unique_activities) | set(unique_next_activities)
        activityList = list(activitySet)
        activityList.sort()
        
        activityList.remove(':Start:')
        
        #edges
        groupedbyactivityPairs = ConnectorBasicStructure.groupby(['prev_activity', 'activity']).size().reset_index(name='counts')
        
        #just to return as matrix
        ActActMatrix = np.zeros([len(activityList), len(activityList)])
        for prev_activity, activity in zip(ConnectorBasicStructure['prev_activity'], ConnectorBasicStructure['activity']):
            if(prev_activity == ":Start:"):
                continue
            ActActMatrix[activityList.index(prev_activity)][activityList.index(activity)] += 1
        
        edges_dict = {}
        
        sumFrequency = groupedbyactivityPairs['counts'].sum() - groupedbyactivityPairs.loc[groupedbyactivityPairs['prev_activity'] == ":Start:", 'counts'][0]
        
        #edges_list = []
        for index, row in groupedbyactivityPairs.iterrows():
            if(row['prev_activity'] == ":Start:"):
                continue
            #edge_dict = {}  
            edge_list = [] 
            
            if(keyword_param['encryption']):
                edge_list.append(Utilities.AES_ECB_Encrypt(row['prev_activity'].encode('utf-8'))[0:5],keyword_param['key'])
                edge_list.append(Utilities.AES_ECB_Encrypt(row['activity'].encode('utf-8'))[0:5],keyword_param['key'])
            else:
                edge_list.append(row['prev_activity'])
                edge_list.append(row['activity'])
            edge_tuple = tuple(edge_list)
            if(row['counts']/sumFrequency >= frequency_threshold):
                edges_dict[edge_tuple] = row['counts']
            #edges_list.append(edge_dict)
            #edges_dict.append(edge_dict)
        

        
        #nodes
        activity_frequencyDF = ConnectorBasicStructure.groupby(['activity']).size().reset_index(name='counts')
        prev_activity_frequencyDF = ConnectorBasicStructure.groupby(['prev_activity']).size().reset_index(name='counts')
        prev_activity_frequencyDF = prev_activity_frequencyDF.rename(columns={'prev_activity':'activity'})
        final_activity_fequency = pd.concat([activity_frequencyDF, prev_activity_frequencyDF]).drop_duplicates(subset='activity', keep="first").reset_index(drop=True) 
        
        
        nodes = final_activity_fequency.set_index('activity').T.to_dict('records')
        nodes[0].pop(':Start:')
        #Making encrypted nodes
        nodes_new = {}
        for key, value in nodes[0].items():
            nodes_new[Utilities.AES_ECB_Encrypt(key.encode('utf-8'),keyword_param['key'])[0:5]] = value
        if(keyword_param['encryption']):
            gviz = dfg_vis_factory.apply(edges_dict, activities_count=nodes_new, parameters={"format": "svg"})
        else:
            gviz = dfg_vis_factory.apply(edges_dict, activities_count=nodes[0], parameters={"format": "svg"})
        
        if(keyword_param['visualization']):
            dfg_vis_factory.view(gviz)
            dfg_vis_factory.save(gviz, dfg_path)
        
        return ActActMatrix, activityList
        
