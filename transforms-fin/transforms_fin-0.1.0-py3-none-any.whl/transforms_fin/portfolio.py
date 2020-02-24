from typing import List

import datacode as dc
from pd_utils import portfolio
from sympy import Symbol


def portfolio_name_func(name: str, **kwargs) -> str:
    return name + ' Portfolio'


def portfolio_symbol_func(sym: Symbol, **kwargs) -> Symbol:
    sym_str = str(sym)
    new_sym_str = r'\text{Port}(' + sym_str + ')'
    sym = Symbol(new_sym_str)
    return sym


def portfolio_data_func(col: dc.Column, variable: dc.Variable, source: dc.DataSource, **kwargs) -> dc.DataSource:
    if 'portvar' in kwargs:
        raise ValueError('cannot pass portvar as variable will be transformed into portvar')

    if 'byvars' not in kwargs and source.index_vars:
        by_vars: List[dc.Variable] = []
        other_indices = [col_idx for col_idx in col.indices if col_idx]
        if len(other_indices) > 0:
            # Got other indices
            for col_idx in other_indices:
                by_vars.extend(col_idx.variables)
        by_var_names = [var.name for var in by_vars]
        if by_var_names:
            kwargs['byvars'] = by_var_names

    # TODO: remove portfolio column reordering once pd_utils.portfolio retains order
    orig_columns = [col for col in source.df.columns]

    # TODO: remore portfolio index handling once pd_utils.portfolio supports using index
    if source.index_vars:
        orig_index_names = source.df.index.names
        source.df.reset_index(inplace=True)
        orig_columns = [col for col in source.df.columns]

    source.df = portfolio(
        source.df,
        variable.name,
        **kwargs
    )

    source.df.drop([variable.name], axis=1, inplace=True)
    source.df.rename(columns={'portfolio': variable.name}, inplace=True)
    source.df = source.df[orig_columns]

    if source.index_vars:
        source.df.set_index(orig_index_names, inplace=True)
    return source


portfolio_transform = dc.Transform(
    'port',
    name_func=portfolio_name_func,
    data_func=portfolio_data_func,
    symbol_func=portfolio_symbol_func,
    data_func_target='source'
)