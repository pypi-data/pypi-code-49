from imblearn.over_sampling import SMOTE
from scipy.spatial.distance import pdist, squareform
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from .util import plot_corr_matrix, distcorr
from .util import pickle_object

class FeatureSelection:
    def __init__(self, df, target='type', dataset_name='all'):
        self.X, self.y = df.loc[:, df.columns != target], df[target]
        self.attrs = self.X.columns
        self.all_attrs = {}
        self.dataset_name = dataset_name
        self.attrs = self.X.columns
    
    def upsample(self, ratio=1):
        sm = SMOTE(random_state=12, ratio = ratio)
        x_res, y_res = sm.fit_sample(self.X, self.y)
        self.X = pd.DataFrame(x_res, columns=self.X.columns)
        self.y = pd.DataFrame(y_res, columns=['type'])

    def low_variance_attr(self, thresh=0.8):
        ''' Select attributes with low variance'''
        desc = self.X.describe().T
        self.low_var_attr = desc[desc['std'] < thresh].index

    def pairwise_corr(self, plot=True):
        '''Pairwise distance corr of attributes'''
        self.X = self.X.drop(self.low_var_attr, axis=1)
        self.attrs = self.X.columns
        self.corr = []
        for a1 in self.attrs:
            t = []
            for a2 in self.attrs:
                t.append(distcorr(self.X[a1], self.X[a2]))
            self.corr.append(t)
        if plot:
            plot_corr_matrix(self.corr)
        

    def type_corr(self, plot=True):
        self.corr_type = []
        for a1 in self.attrs:
            t = []
            t.append(distcorr(self.X[a1], self.y['type']))
            self.corr_type.append(t)
        if plot:
            plot_corr_matrix(self.corr_type)

    def get_final_attrs(self, thresh=0.85, plot=True):
        '''Filter attributes with low corr and high corr with target'''
        for i, a in enumerate(self.attrs):
            self.all_attrs[i] = {'name': a, 'imp': True}

        for i1, c1 in enumerate(self.corr):
            for i2, c2 in enumerate(c1):
                at = sorted((i1, i2))
                if c2 > thresh and i1 != i2:
                    if self.corr_type[i1][0] > self.corr_type[i2][0]:
                        self.all_attrs[i2]['imp'] = False

        self.final_attrs = [self.all_attrs[i]['name'] for i in self.all_attrs if self.all_attrs[i]['imp'] == True]

    def select_attrs(self):
        self.low_variance_attr()
        self.pairwise_corr()
        self.type_corr()
        self.get_final_attrs()
        

    def save_attrs(self, path, version):
        p = f'{path}/attrs_{self.dataset_name}_v{version}.pkl'
        pickle_object(self.final_attrs, p)
        print(f'Saved in {p}')