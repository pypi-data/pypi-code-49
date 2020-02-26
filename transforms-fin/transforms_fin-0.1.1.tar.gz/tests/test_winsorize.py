from datacode import VariableCollection

import transforms_fin

import pandas as pd
from pandas.util.testing import assert_frame_equal

from tests.base import TransformTest


class TransformWinsorizeTest(TransformTest):
    expect_df_no_byvars = pd.DataFrame(
        data = [
            (5.8, 6.8, 'd'),
            (5.8, 6.8, 'd'),
            (5.8, 6.8, 'd'),
            (7.0, 8.0, 'd'),
            (9.0, 10.0, 'e'),
            (11.0, 12.0, 'e'),
            (12.2, 13.2, 'e'),
            (12.2, 13.2, 'e'),
            (12.2, 13.2, 'e'),
        ], columns = ['A', 'B', 'C']
    )

    expect_df_byvars = pd.DataFrame(
        data = [
            (2.8, 3.8, 'd'),
            (3.0, 4.0, 'd'),
            (5.0, 6.0, 'd'),
            (5.2, 6.2, 'd'),
            (11.4, 12.4, 'e'),
            (11.4, 12.4, 'e'),
            (13.0, 14.0, 'e'),
            (14.6, 15.6, 'e'),
            (14.6, 15.6, 'e'),
        ], columns = ['A', 'B', 'C']
    )


    def assert_variable_names_and_symbols(self, vc: VariableCollection):
        assert str(vc.a.winsor(0.3).symbol) == r'\text{A}'
        assert str(vc.b.winsor(0.3).symbol) == r'\text{B}'
        assert vc.a.winsor(0.3).name == 'A'
        assert vc.b.winsor(0.3).name == 'B'


class TestPortfolioTransform(TransformWinsorizeTest):

    def test_winsorize_no_byvars(self):
        vc, a, b, c = self.create_variable_collection()
        self.create_csv()
        all_cols = self.create_columns()
        load_variables = [
            vc.a.winsor(0.3),
            vc.b.winsor(0.3),
            c
        ]
        ds = self.create_source(df=None, columns=all_cols, load_variables=load_variables)
        assert_frame_equal(ds.df, self.expect_df_no_byvars)
        self.assert_variable_names_and_symbols(vc)

    def test_winsorize_byvars(self):
        vc, a, b, c = self.create_variable_collection()
        self.create_csv()
        all_cols = self.create_columns()
        load_variables = [
            vc.a.winsor(0.3, byvars=[vc.c.name]),
            vc.b.winsor(0.3, byvars=[vc.c.name]),
            c
        ]
        ds = self.create_source(df=None, columns=all_cols, load_variables=load_variables)
        assert_frame_equal(ds.df, self.expect_df_byvars)
        self.assert_variable_names_and_symbols(vc)
