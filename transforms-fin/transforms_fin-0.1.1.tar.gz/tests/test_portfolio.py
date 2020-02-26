from datacode import VariableCollection

import transforms_fin

import pandas as pd
from pandas.util.testing import assert_frame_equal

from tests.base import TransformTest


class TransformPortfolioTest(TransformTest):
    expect_df_no_byvars = pd.DataFrame(
        [
            (1, 1, 'd'),
            (1, 1, 'd'),
            (1, 1, 'd'),
            (2, 2, 'd'),
            (2, 2, 'e'),
            (2, 2, 'e'),
            (3, 3, 'e'),
            (3, 3, 'e'),
            (3, 3, 'e'),
        ], columns=['A Portfolio', 'B Portfolio', 'C']
    )
    expect_df_with_c_index = pd.DataFrame(
        [
            ('d', 1, 1),
            ('d', 1, 1),
            ('d', 2, 2),
            ('d', 3, 3),
            ('e', 1, 1),
            ('e', 1, 1),
            ('e', 2, 2),
            ('e', 3, 3),
            ('e', 3, 3),
        ], columns=['C', 'A Portfolio', 'B Portfolio']
    ).set_index('C')
    expect_df_manual_c_byvars = pd.DataFrame(
        [
            (1, 1, 'd'),
            (1, 1, 'd'),
            (2, 2, 'd'),
            (3, 3, 'd'),
            (1, 1, 'e'),
            (1, 1, 'e'),
            (2, 2, 'e'),
            (3, 3, 'e'),
            (3, 3, 'e'),
        ], columns=['A Portfolio', 'B Portfolio', 'C']
    )

    def assert_variable_names_and_symbols(self, vc: VariableCollection):
        assert str(vc.a.port().symbol) == r'\text{Port}(\text{A})'
        assert str(vc.b.port().symbol) == r'\text{Port}(\text{B})'
        assert vc.a.port().name == 'A Portfolio'
        assert vc.b.port().name == 'B Portfolio'


class TestPortfolioTransform(TransformPortfolioTest):

    def test_portfolio_no_byvars(self):
        vc, a, b, c = self.create_variable_collection()
        self.create_csv()
        all_cols = self.create_columns()
        load_variables = [
            vc.a.port(ngroups=3),
            vc.b.port(ngroups=3),
            c
        ]
        ds = self.create_source(df=None, columns=all_cols, load_variables=load_variables)
        assert_frame_equal(ds.df, self.expect_df_no_byvars)
        self.assert_variable_names_and_symbols(vc)

    def test_portfolio_auto_byvars(self):
        vc, a, b, c = self.create_variable_collection(with_index=True)
        self.create_csv()
        all_cols = self.create_indexed_columns()
        load_variables = [
            vc.a.port(ngroups=3),
            vc.b.port(ngroups=3),
            c
        ]
        ds = self.create_source(df=None, columns=all_cols, load_variables=load_variables)
        assert_frame_equal(ds.df, self.expect_df_with_c_index)
        self.assert_variable_names_and_symbols(vc)

    def test_portfolio_manual_byvars(self):
        vc, a, b, c = self.create_variable_collection()
        self.create_csv()
        all_cols = self.create_columns()
        load_variables = [
            vc.a.port(ngroups=3, byvars=vc.c.name),
            vc.b.port(ngroups=3, byvars=vc.c.name),
            c
        ]
        ds = self.create_source(df=None, columns=all_cols, load_variables=load_variables)
        assert_frame_equal(ds.df, self.expect_df_manual_c_byvars)
        self.assert_variable_names_and_symbols(vc)
