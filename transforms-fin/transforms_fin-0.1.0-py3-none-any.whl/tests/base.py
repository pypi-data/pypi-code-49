import os
import shutil
import unittest
from typing import Tuple, Optional, List

import pandas as pd
from datacode import Variable, VariableCollection, Column, Index, StringType, ColumnIndex, DataSource

VC_NAME = 'my_collection'
GENERATED_PATH = os.path.join('tests', 'generated_files')


class TransformTest(unittest.TestCase):
    csv_path = os.path.join(GENERATED_PATH, 'data.csv')

    test_df = pd.DataFrame(
        [
            (1, 2, 'd'),
            (3, 4, 'd'),
            (5, 6, 'd'),
            (7, 8, 'd'),
            (9, 10, 'e'),
            (11, 12, 'e'),
            (13, 14, 'e'),
            (15, 16, 'e'),
            (17, 18, 'e'),
        ],
        columns=['a', 'b', 'c']
    )

    def setup_method(self, *args, **kwargs):
        os.makedirs(GENERATED_PATH)

    def teardown_method(self, *args, **kwargs):
        shutil.rmtree(GENERATED_PATH)

    def create_variables(self) -> Tuple[Variable, Variable, Variable]:
        a = Variable('a', 'A', dtype='int')
        b = Variable('b', 'B', dtype='int')
        c = Variable('c', 'C', dtype='str')
        return a, b, c

    def create_variable_collection(self, with_index: bool = False,
                                   **kwargs) -> Tuple[VariableCollection, Variable, Variable, Variable]:
        config_dict = dict(
            name=VC_NAME
        )
        config_dict.update(**kwargs)
        if with_index:
            (a, b, c), c_ind = self.create_variables_and_c_colindex()
        else:
            a, b, c = self.create_variables()
        vc = VariableCollection(a, b, c, **config_dict)
        return vc, a, b, c

    def create_csv(self, df: Optional[pd.DataFrame] = None, **to_csv_kwargs):
        if df is None:
            df = self.test_df
        df.to_csv(self.csv_path, index=False, **to_csv_kwargs)

    def create_source(self, **kwargs) -> DataSource:
        config_dict = dict(
            df=self.test_df,
            location=self.csv_path,
        )
        config_dict.update(kwargs)
        return DataSource(**config_dict)

    def create_columns(self) -> List[Column]:
        a, b, c = self.create_variables()
        ac = Column(a, 'a')
        bc = Column(b, 'b')
        cc = Column(c, 'c')
        return [
            ac,
            bc,
            cc
        ]

    def create_c_index(self) -> Index:
        c_index = Index('c', dtype=StringType(categorical=True))
        return c_index

    def create_variables_and_c_colindex(self) -> Tuple[List[Variable], ColumnIndex]:
        a, b, c = self.create_variables()
        c_index = self.create_c_index()

        c_col_index = ColumnIndex(c_index, [c])

        return [a, b, c], c_col_index

    def create_indexed_columns(self) -> List[Column]:
        (a, b, c), c_col_index = self.create_variables_and_c_colindex()
        ac = Column(a, 'a', indices=[c_col_index])
        bc = Column(b, 'b', indices=[c_col_index])
        cc = Column(c, 'c')
        return [
            ac,
            bc,
            cc
        ]