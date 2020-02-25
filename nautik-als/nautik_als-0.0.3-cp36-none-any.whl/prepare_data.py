""" Functions to prepare data before and after ALS calculation """
import pandas as pd
import numpy as np
import scipy
import scipy.sparse


def create_index(df, column):
        unique_ids = np.unique(df[column])
        index = np.arange(len(unique_ids))
        return dict(zip(unique_ids, index))

def get_previous_trained_matrix(self, previous_matrix, path=''):
    """
    Load the previous trained factor matrix
    previous matrix: parquet [string: identifier, 
                              double: n factors]
    """
    previous_matrix = pd.read_parquet(path)
    previous_matrix['previous_index']
    
    
    
def prepare_user_item_matrix(self, user_item_matrix=None,
                             warmstart=False,
                             previous_user_matrix=None,
                             previous_item_matrix=None):
    """
    Take the dataframe of interactions for users and item
    and prepares it for training.
    
    user_item_matrix: pandas DataFrame [string: user, string: item, double: score]
    """
    
    
    df_columns = list(user_item_matrix.columns.values)

    # create index mapping
    self.user_index_dict = self.create_index(user_item_matrix, column=df_columns[0])
    self.item_index_dict = self.create_index(user_item_matrix, column=df_columns[1])
    
    user_data = \
        user_item_matrix[[df_columns[0]]] \
        .applymap(lambda x: self.user_index_dict[x])[df_columns[0]].values
        
    item_data = \
        user_item_matrix[[df_columns[0]]] \
        .applymap(lambda x: self.item_index_dict[x])[df_columns[0]].values
        
    user_item_data = user_item_matrix[df_columns[2]]
    
    user_item = scipy.sparse.csr_matrix((user_item_data, user_data, item_data))
    
    return user_item


    
    

def perform_warmstart(self, user_factors=None, item_factors=None):
    """ Allows to set the initial factor matrices, 
    so a 'warm-start' is possible
    
    The item and user indices of the initial matrices 
    have to match the indices of the current ones
    
    """
    self.user_factors = user_factors
    self.item_factors = item_factors
