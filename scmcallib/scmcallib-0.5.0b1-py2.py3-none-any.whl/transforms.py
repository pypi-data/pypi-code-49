"""
Transforms are arbitary functions which perform some transformation on an input data set and return the result. In the optimisation
cycle, these transformations are applied to the raw model output before any metrics are calculated.
This allows for penalising for values outside a range or performing subsampling.

At a high-level the optimisation cycle is as follows:

#. Optimiser produces parameters
#. Model run
#. Output transformed
#. Metrics calculated
#. Repeat until convergence
"""

import ast
import numpy as np


def penalise(lower=None, upper=None, value=1e9):
    """
    Applies a penalty to values outside a range

    Parameters
    ----------
    lower: int
        Values lower than this are penalised
    upper: int
        Values more than `upper` are penalised
    value: float
        The value to set all the items outside the valid range

    """

    def _wrapper(df):
        mask = False

        if lower is not None:
            mask = mask | (df < lower)
        if upper is not None:
            mask = mask | (df > upper)
        df.values[mask] = value
        return df

    return _wrapper


def diff():
    """
    Take the first order derivative of the data

    Returns
    -------

    """
    def _wrapper(df):
        dt = df.columns[1] - df.columns[0]
        assert dt.days in [365, 366], "Assuming annual timesteps"

        # update units
        units = ["{} / yr".format(u) for u in df.index.get_level_values(level="unit")]
        df.index = df.index.set_levels(units, level="unit")

        df.values[0, 1:] = np.diff(df.values[0])
        df.values[0, 0] = np.nan
        return df
    return _wrapper

"""
Each transform is a function which can take arguments and keywords and returns a wrapped function which performs the
actual transformation
"""
transforms = {
    "penalise": penalise,
    "diff": diff
}


def _dump_ast(c):
    if isinstance(c, ast.Num):
        return c.n
    elif isinstance(c, ast.Str):
        return c.s
    elif isinstance(c, ast.Tuple) or isinstance(c, ast.List):
        return tuple([_dump_ast(i) for i in c.elts])
    elif isinstance(c, ast.UnaryOp) and isinstance(c.op, ast.USub):
        return -_dump_ast(c.operand)
    else:
        raise SyntaxError()


def _parse_transform(name):
    if "(" not in name:
        if ")" in name:
            raise SyntaxError()
        return name, [], {}

    # Use ast to parse the function call
    # Much simpler than using regex
    call = ast.parse(name)

    # Only parse simple functions (no modules) of form func(arg1, arg2, .., argn, kw1=val1, .., kwn=val2)
    # Only handles numbers and strings or list/tuples of them as args and kwargs as no other state will be available
    if len(call.body) != 1 and isinstance(call.body[0].value, ast.Call):
        raise ValueError("Cannot parse function call from transform: {}".format(name))

    call = call.body[0].value
    func_name = call.func.id

    args = [_dump_ast(i) for i in call.args]
    kwargs = {i.arg: _dump_ast(i.value) for i in call.keywords}

    return func_name, args, kwargs


def get_transform(name, *args, **kwargs):
    """
    Lookup a transform function

    The transform must be registered in ``transforms``

    Parameters
    ----------
    name: str
        Transform name.

        Can be in the form of a function call, such as ``func_name(arg1, arg2, kw1=val1)`` in which case the args and kwargs are
        parsed from call.
    args
        Transform args. Only used if a function name is passed to name, instead of a function call.
    kwargs
        Transform kwargs. Only used if a function name is passed to name, instead of a function call.
    Returns
    -------
    Function which takes a ``pd.DataFrame`` and returns a modified DataFrame
    """
    name, f_args, f_kwargs = _parse_transform(name)

    if len(f_args):
        if len(args):
            raise ValueError("Can't provide args in both function and as arguments")
        args = f_args

    if len(f_kwargs):
        if len(kwargs):
            raise ValueError("Can't provide kwargs in both function and as arguments")
        kwargs = f_kwargs

    if name not in transforms:
        raise ValueError("Unknown transform: {}".format(name))

    return transforms[name](*args, **kwargs)
