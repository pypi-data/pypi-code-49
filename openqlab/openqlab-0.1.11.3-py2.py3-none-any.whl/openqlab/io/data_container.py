# from __future__ import annotations # with this one can use the class as return type inside the class itself
import contextlib
import io
import json
import warnings

import numpy as np
import pandas as pd


@contextlib.contextmanager
def _open_file_or_buff(path_or_buff, mode="r", **kwargs):
    file_handler = None
    try:
        try:
            file_handler = open(path_or_buff, mode=mode, newline="", **kwargs)
        except TypeError:
            file_handler = path_or_buff
        if path_or_buff is None:
            file_handler = io.StringIO()
        yield file_handler
    finally:
        try:
            file_handler.close()
        except AttributeError:
            pass


def header_wrapper(func):
    def wrapper(*args, **kwargs):
        header = {}
        first_arg = args[0]
        if isinstance(first_arg, DataContainer):
            header = first_arg.header
        elif isinstance(first_arg, list):
            for item in first_arg:
                if isinstance(item, DataContainer):
                    header = item.header
        for arg in args:
            header = _combine_header(header, arg)
        dataframe = func(*args, **kwargs)
        if isinstance(dataframe, (pd.DataFrame, pd.Series)):
            return DataContainer(dataframe, header=header)
        if isinstance(dataframe, type(None)):
            first_arg.header = header
            return None
        # raise TypeError("Not a DataFrame like object.")

    return wrapper


def wrapper_factory(func, base):
    if func in base.__dict__:

        @header_wrapper
        def wrapped_function(self, *args, **kwargs):
            return base.__dict__[func](self, *args, **kwargs)

        docstring = base.__dict__[func].__doc__
    elif func in base.__bases__[0].__dict__:

        @header_wrapper
        def wrapped_function(self, *args, **kwargs):
            return base.__bases__[0].__dict__[func](self, *args, **kwargs)

        docstring = base.__bases__[0].__dict__[func].__doc__
    else:
        raise LookupError(
            f"No function called '{func}' in original functions from {base}. It might be deprecated."
        )

    return wrapped_function, docstring


class MetaDataContainer(type):
    magic_methods = [
        "__add__",
        "__sub__",
        "__mul__",
        "__floordiv__",
        "__truediv__",
        "__mod__",
        "__pow__",
        "__and__",
        "__xor__",
        "__or__",
        "__iadd__",
        "__isub__",
        "__imul__",
        "__ifloordiv__",
        "__itruediv__",
        "__imod__",
        "__ipow__",
        "__iand__",
        "__ixor__",
        "__ior__",
    ]
    single_parameter_magic_methods = ["__neg__", "__abs__", "__invert__"]
    binary_operator = [
        "add",
        "sub",
        "mul",
        "div",
        "divide",
        "truediv",
        "floordiv",
        "mod",
        "pow",
        "dot",
        "radd",
        "rsub",
        "rmul",
        "rdiv",
        "rtruediv",
        "rfloordiv",
        "rmod",
        "rpow",
    ]
    combining = ["append", "join", "merge", "combine", "combine_first"]
    conversion = [
        "astype",
        "infer_objects",
        "copy",
        "isna",
        "notna",
        "isnull",
        "select_dtypes",
    ]
    indexing = ["isin", "where", "mask", "query"]
    function_application = ["apply", "applymap", "agg", "aggregate", "transform"]
    computations_single = [
        "abs",
        "clip",
        "corr",
        "cov",
        "cummax",
        "cummin",
        "cumprod",
        "cumsum",
        "describe",
        "diff",
        "kurt",
        "kurtosis",
        "mad",
        "max",
        "mean",
        "median",
        "min",
        "mode",
        "pct_change",
        "prod",
        "product",
        "quantile",
        "rank",
        "round",
        "sem",
        "skew",
        "sum",
        "std",
        "var",
        "nunique",
    ]
    computations = ["corrwith", "eval"]
    reindexing = [
        "add_prefix",
        "add_suffix",
        "at_time",
        "between_time",
        "drop",
        "drop_duplicates",
        "filter",
        "first",
        "last",
        "reindex",
        "reindex_like",
        "rename",
        "rename_axis",
        "reset_index",
        "sample",
        "set_axis",
        "set_index",
        "take",
        "truncate",
    ]
    missing_data = ["dropna", "fillna", "replace", "interpolate"]
    reshaping = [
        "pivot",
        "pivot_table",
        "reorder_levels",
        "sort_values",
        "sort_index",
        "nlargest",
        "nsmallest",
        "swaplevel",
        "stack",
        "unstack",
        "swapaxes",
        "melt",
        "squeeze",
        "transpose",
    ]
    time_series = [
        "asfreq",
        "asof",
        "shift",
        "slice_shift",
        "tshift",
        "to_period",
        "to_timestamp",
        "tz_convert",
        "tz_localize",
    ]
    normal_methods = (
        binary_operator
        + combining
        + conversion
        + indexing
        + function_application
        + computations
        + reindexing
        + missing_data
        + reshaping
        + time_series
    )
    functions = (
        normal_methods
        + magic_methods
        + single_parameter_magic_methods
        + computations_single
    )

    def __new__(mcs, name, bases, clsdict):
        base = bases[0]
        for function_ in MetaDataContainer.functions:
            try:
                clsdict[function_], docstring = wrapper_factory(function_, base)
            except LookupError as error:
                warnings.warn(f"{error}", Warning)
            else:
                if isinstance(docstring, str):
                    docstring = docstring.replace("DataFrame", "DataContainer")
                    docstring = docstring.replace("dataframe", "DataContainer")
                    docstring = docstring.replace("pd.DataContainer", "DataContainer")
                    docstring = docstring.replace("frame's", "DataContainer's")
                clsdict[function_].__doc__ = docstring
        return super().__new__(mcs, name, bases, clsdict)


class DataContainer(pd.DataFrame, metaclass=MetaDataContainer):
    """
    DataContainer inherits from pandas.DataFrame and works with header variable to store additional information
    besides plain data.
    """

    general_keys = ["xUnit", "yUnit", "Date"]
    header_keys = {
        "spectrum": ["RBW", "VBW", "Span", "CenterFrequency"] + general_keys,
        "osci": general_keys,
    }
    JSON_PREFIX = "-----DataContainerHeader\n"
    JSON_SUFFIX = "-----DataContainerData\n"

    def __init__(
        self, *args, header=None, header_type=None, type=None, **kwargs
    ):  # pylint: disable=redefined-builtin
        super().__init__(*args, **kwargs)

        if args:
            data = args[0]
        else:
            data = kwargs.get("data")

        if type:
            warnings.warn(
                f"Argument 'type' is deprecated. Use 'header_type' instead.",
                DeprecationWarning,
            )
            if not header_type:
                header_type = type
        self.header_type = header_type

        with warnings.catch_warnings():  # pandas otherwise gives userwarning
            warnings.simplefilter("ignore")

            self._header = {}
            if header:
                if isinstance(header, dict):
                    self.header = header
                else:
                    raise TypeError("argument 'header' must be a dict!")
            else:
                if isinstance(data, DataContainer):
                    self.header = data.header
                elif header_type:
                    try:
                        self._header_from_keys()
                    except KeyError:
                        raise TypeError(
                            f"'{header_type}' is not a valid header_type for {self.__class__}."
                        )
                else:
                    self.header = dict()

    def _ensure_type(self, obj):
        """Ensure that an object has same type as self.

        Used by type checkers.
        """
        assert isinstance(
            obj, (type(self), pd.DataFrame)
        ), f"{type(obj)} not a {pd.DataFrame}"
        return obj

    @property
    def header(self):
        return self._header

    @header.setter
    def header(self, header):
        if isinstance(header, dict):
            self._header = header
        else:
            raise TypeError("header variable must be a dict!")

    def __repr__(self):
        header_string = ""
        for key in self.header:
            header_string += "{0} : {1}\n".format(key, self.header[key])
        maxlen = 60
        length = maxlen  # if (maxlen < len(header_string)) else len(header_string)
        string = (
            "-" * length
            + "\n"
            + header_string
            + "-" * length
            + "\n"
            + super().__repr__()
        )

        return string

    def __getitem__(self, key):
        header = self.header
        output = super().__getitem__(key)
        if isinstance(output, pd.DataFrame):
            output = DataContainer(output, header=header)
        elif isinstance(output, pd.Series):
            pass
        return output

    def head(self, n=5):
        header = self.header
        return DataContainer(super().head(n), header=header)

    def tail(self, n=5):
        header = self.header
        return DataContainer(super().tail(n), header=header)

    def _header_from_keys(self):
        self.header = dict.fromkeys(DataContainer.header_keys[self.header_type])

    @staticmethod
    @header_wrapper
    def concat(*args, **kwargs):
        return pd.concat(*args, **kwargs)

    def update_header(self, other: dict):
        self.header = {**self.header, **other}
        empty_keys = self.emtpy_keys()
        if empty_keys:
            print(
                "Could not determine values for {0}".format(
                    "'" + ",".join(empty_keys) + "'"
                )
            )

    def emtpy_keys(self):
        empty = []
        for key in self.header:
            if self.header[key] is None:
                empty.append(key)
        return empty

    def to_csv(self, path_or_buf=None, mode="w", *args, **kwargs):
        with _open_file_or_buff(path_or_buf, mode=mode, **kwargs) as file:
            header = kwargs.get("header", True)
            if header:
                file.write(self._header_to_json())
            super().to_csv(path_or_buf=file, *args, **kwargs)
            if path_or_buf is None:
                return file.getvalue()

    @classmethod
    def from_csv(cls, *args, **kwargs):
        return cls.read_csv(*args, **kwargs)

    @classmethod
    def read_csv(cls, path_or_buf, *args, index_col=0, **kwargs) -> "DataContainer":
        with _open_file_or_buff(path_or_buf, mode="r") as file:
            header_dict = cls._json_to_header(file)
            return DataContainer(
                pd.read_csv(file, *args, index_col=index_col, **kwargs),
                header=header_dict,
            )

    def to_json(self, path_or_buf=None, mode="w", orient=None, **kwargs):
        with _open_file_or_buff(path_or_buf, mode=mode, **kwargs) as file:
            header = kwargs.get("header", True)
            if header:
                file.write(self._header_to_json())
            super().to_json(path_or_buf=file, orient=orient, **kwargs)
            if path_or_buf is None:
                return file.getvalue()

    @classmethod
    def from_json(cls, *args, **kwargs):
        return cls.read_json(*args, **kwargs)

    @classmethod
    def read_json(cls, path_or_buf, *args, orient=None, **kwargs):
        try:
            with _open_file_or_buff(path_or_buf, mode="r") as file:
                header_dict = cls._json_to_header(file)
                return DataContainer(
                    pd.read_json(file, *args, orient=orient, **kwargs),
                    header=header_dict,
                )
        except (FileNotFoundError, OSError):
            if (
                path_or_buf[0] == "{" and path_or_buf[-1] == "}"
            ) or path_or_buf.startswith(DataContainer.JSON_PREFIX):
                file = io.StringIO(path_or_buf)
                header_dict = cls._json_to_header(file)
                return DataContainer(
                    pd.read_json(file, *args, orient=orient, **kwargs),
                    header=header_dict,
                )

    def to_hdf(self, path_or_buf, key: str, **kwargs):
        df = pd.DataFrame(self)
        with pd.HDFStore(path_or_buf) as store:
            store.put(key, df)
            store.get_storer(key).attrs.metadata = self.header

    @staticmethod
    def read_hdf(path_or_buf, key: str):
        with pd.HDFStore(path_or_buf) as store:
            data = store.get(key)
            header = store.get_storer(key).attrs.metadata
            return DataContainer(data=data, header=header)

    @classmethod
    def from_hdf(cls, *args, **kwargs) -> "DataContainer":
        return cls.read_hdf(*args, **kwargs)

    @staticmethod
    def read_pickle(filepath_or_buf, *args, **kwargs):
        return pd.read_pickle(filepath_or_buf, *args, **kwargs)

    def __getstate__(self):
        return self.__dict__

    def __setstate__(self, d):
        self.__dict__ = d

    def _header_to_json(self):
        prefix = self.JSON_PREFIX
        suffix = self.JSON_SUFFIX
        try:
            header_string = prefix + json.dumps(self.header) + "\n" + suffix
        except TypeError as e:
            raise TypeError(e.__str__().join(". Remove it in order to save to file"))
        return header_string

    @classmethod
    def _json_to_header(cls, f):
        prefix = cls.JSON_PREFIX.strip()
        suffix = cls.JSON_SUFFIX.strip()
        first = f.readline().strip()
        header = f.readline().strip()
        last = f.readline().strip()

        if not (first == prefix and last == suffix):
            f.seek(0)
            header = None
        else:
            header = json.loads(header)
        return header

    def plot(self, *args, **kwargs):
        plotter = pd.DataFrame.plot(self)
        ax = plotter(*args, **kwargs)
        xUnit = self.header.get("xUnit")
        if xUnit:
            xlabel = "{0} ({1})".format(self.index.name, xUnit)
            if isinstance(ax, np.ndarray):
                ax[-1].set_xlabel(xlabel)
            else:
                ax.set_xlabel(xlabel)
        return ax


def _combine_header(header, other):
    if isinstance(other, list):
        itemlist = other[:]  # otherwise also other would be affectec by itemlist.pop()
        while itemlist:
            item = itemlist.pop()
            if isinstance(item, DataContainer):
                header = _combine_header(header, item.header)
            elif isinstance(item, dict):
                header = _combine_header(header, item)
            else:
                pass
    elif isinstance(other, DataContainer):
        header = _combine_header(header, other.header)
    elif isinstance(other, dict):
        d = dict()
        for key in header.keys() & other.keys():
            if header[key] == other[key]:
                d.update({key: header[key]})
        header = d
    return header
