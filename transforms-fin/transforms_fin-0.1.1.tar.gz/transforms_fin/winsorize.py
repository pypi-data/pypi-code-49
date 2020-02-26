import datacode as dc
from pd_utils import winsorize
from sympy import Symbol


def winsorize_name_func(name: str, *args, **kwargs) -> str:
    return name


def winsorize_symbol_func(sym: Symbol, *args, **kwargs) -> Symbol:
    return sym


def winsorize_data_func(col: dc.Column, variable: dc.Variable, source: dc.DataSource, *args, **kwargs) -> dc.DataSource:
    # TODO: add tests

    source.df = winsorize(
        source.df,
        *args,
        subset=variable.name,
        **kwargs
    )

    return source


winsorize_transform = dc.Transform(
    'winsor',
    name_func=winsorize_name_func,
    data_func=winsorize_data_func,
    symbol_func=winsorize_symbol_func,
    data_func_target='source'
)