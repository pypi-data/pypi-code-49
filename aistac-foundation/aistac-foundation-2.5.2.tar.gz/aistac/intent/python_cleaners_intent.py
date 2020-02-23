import inspect
import re
import threading
from copy import deepcopy
from datetime import datetime

from aistac.intent.abstract_intent import AbstractIntentModel
from aistac.properties.abstract_properties import AbstractPropertyManager

__author__ = 'Darryl Oatridge'


class PythonCleanersIntentModel(AbstractIntentModel):
    """a pure python implementation of Cleaner Intent as a working example of the Intent Abstraction"""

    def __init__(self, property_manager: AbstractPropertyManager, default_save_intent: bool=None,
                 default_intent_level: bool=None, default_replace_intent: bool=None):
        """initialisation of the Intent class. The 'intent_param_exclude' is used to exclude commonly used method
         parameters from being included in the intent contract, this is particularly useful if passing a canonical, or
         non relevant parameters to an intent method pattern. Any named parameter in the intent_param_exclude list
         will not be included in the recorded intent contract for that method

        :param property_manager: the property manager class that references the intent contract.
        :param default_save_intent: (optional) The default action for saving intent in the property manager
        :param default_intent_level: (optional) the default level intent should be saved at
        :param default_replace_intent: (optional) the default replace existing intent behaviour
        """
        default_save_intent = default_save_intent if isinstance(default_save_intent, bool) else True
        default_replace_intent = default_replace_intent if isinstance(default_replace_intent, bool) else True
        default_intent_level = default_intent_level if isinstance(default_intent_level, (str, int, float)) else 0
        intent_param_exclude = ['data', 'inplace']
        intent_type_additions = []
        super().__init__(property_manager=property_manager, default_save_intent=default_save_intent,
                         intent_param_exclude=intent_param_exclude, default_intent_level=default_intent_level,
                         default_replace_intent=default_replace_intent, intent_type_additions=intent_type_additions)

    def run_intent_pipeline(self, canonical: dict, levels: [int, str, list]=None, inplace: bool=False, **kwargs):
        """ Collectively runs all parameterised intent taken from the property manager against the code base as
        defined by the intent_contract.

        It is expected that all intent methods have the 'canonical' as the first parameter of the method signature
        and will contain 'inplace' and 'save_intent' as parameters.

        :param canonical: this is the iterative value all intent are applied to and returned.
        :param levels: (optional) an single or list of levels to run, if list, run in order given
        :param inplace: (optional) change data in place or to return a deep copy. default False
        :param kwargs: additional kwargs to add to the parameterised intent, these will replace any that already exist
        :return Canonical with parameterised intent applied or None if inplace is True
        """
        inplace = inplace if isinstance(inplace, bool) else False

        # test if there is any intent to run
        if self._pm.has_intent() and not inplace:
            # create the copy and use this for all the operations
            if not inplace:
                with threading.Lock():
                    canonical = deepcopy(canonical)
            # get the list of levels to run
            if isinstance(levels, (int, str, list)):
                levels = self._pm.list_formatter(levels)
            else:
                levels = sorted(self._pm.get_intent().keys())
            for level in levels:
                for method, params in self._pm.get_intent(level=level).items():
                    if method in self.__dir__():
                        if isinstance(kwargs, dict):
                            params.update(kwargs)
                        canonical = eval(f"self.{method}(canonical, inplace=False, save_intent=False, **{params})")
        if not inplace:
            return canonical

    def auto_clean_header(self, data: dict, case: str=None, rename_map: dict=None, replace_spaces: str=None,
                          inplace: bool=False, save_intent: bool=None, intent_level: [int, str]=None):
        """ clean the headers of a pandas DataFrame replacing space with underscore

        :param data: the data to drop duplicates from
        :param rename_map: a from: to dictionary of headers to rename
        :param case: changes the headers to lower, upper, title. if none of these then no change
        :param replace_spaces: character to replace spaces with. Default is '_' (underscore)
        :param inplace: if the passed data should be used or a deep copy
        :param save_intent (optional) if the intent contract should be saved to the property manager
        :param intent_level: (optional) a level to place the intent
        :return: if inplace, returns a formatted cleaner contract for this method, else a deep copy data.
        """
        # intent persist options
        self._set_intend_signature(self._intent_builder(method=inspect.currentframe().f_code.co_name, params=locals()),
                                   intent_level=intent_level, save_intent=save_intent)
        # intent code
        replace_spaces = '_' if not isinstance(replace_spaces, str) else replace_spaces
        case = str.lower(case) if isinstance(case, str) and str.lower(case) in ['lower', 'upper', 'title'] else None
        if not inplace:
            with threading.Lock():
                data = deepcopy(data)

        for key in data.keys():
            # removes any hidden characters
            header = str(key)
            # remap any keys
            if isinstance(rename_map, dict) and header in rename_map.keys():
                header = rename_map[key]
            # convert case
            if case is not None:
                header = eval("str.{}(header)".format(case))
            # replaces spaces at the end just in case title is used
            header = str(header).replace(' ', replace_spaces)
            data[header] = data.pop(key)
        if not inplace:
            return data

    # drop column that only have 1 value in them
    def auto_remove_columns(self, data, null_min: float=None, predominant_max: float=None,
                            nulls_list: [bool, list]=None, inplace=False, save_intent: bool=None,
                            intent_level: [int, str]=None) -> dict:
        """ auto removes columns that are np.NaN, a single value or have a predominat value greater than.

        :param data: the data to auto remove
        :param null_min: the minimum number of null values default to 0.998 (99.8%) nulls
        :param predominant_max: the percentage max a single field predominates default is 0.998
        :param nulls_list: can be boolean or a list:
                    if boolean and True then null_list equals ['NaN', 'nan', 'null', '', 'None']
                    if list then this is considered potential null values.
        :param inplace: if to change the passed data or return a copy (see return)
        :param save_intent (optional) if the intent contract should be saved to the property manager
        :param intent_level: (optional) a level to place the intent
        :return: if inplace, returns a formatted cleaner contract for this method, else a deep copy data.
        """
        # intent persist options
        self._set_intend_signature(self._intent_builder(method=inspect.currentframe().f_code.co_name, params=locals()),
                                   intent_level=intent_level, save_intent=save_intent)
        # intent code
        null_min = 0.998 if not isinstance(null_min, (int, float)) else null_min
        predominant_max = 0.998 if not isinstance(predominant_max, (int, float)) else predominant_max
        if isinstance(nulls_list, bool) and nulls_list:
            nulls_list = ['NaN', 'nan', 'null', '', 'None']
        elif not isinstance(nulls_list, list):
            nulls_list = None
        if not inplace:
            with threading.Lock():
                data = deepcopy(data)

        to_remove = list()
        for c in data.keys():
            col = deepcopy(data.get(c))
            if nulls_list is not None:
                col[:] = [None if x in nulls_list else x for x in col]
            # remove all None using list comprehension
            col[:] = list(filter(None, col))
            if len(col) == 0 or round(len(col) / len(data.get(c)), 3) > null_min:
                to_remove.append(c)
            elif len(set(col)) == 1:
                to_remove.append(c)
            elif round(sorted([col.count(x) for x in set(col)], reverse=True)[0] / len(col), 3) >= predominant_max:
                to_remove.append(c)
        for c in to_remove:
            data.pop(c)
        if not inplace:
            return data

    def auto_drop_duplicates(self, data: dict, headers: [str, list]=None, drop: bool=False, dtype: [str, list]=None,
                             exclude: bool=False, regex: [str, list]=None, re_ignore_case: bool=True,
                             inplace: bool=False, save_intent: bool=None, intent_level: [int, str]=None) -> dict:
        """ drops duplicate columns

        :param data: the Canonical data to drop duplicates from
        :param headers: a list of headers to drop or filter on type
        :param drop: to drop or not drop the headers
        :param dtype: the column types to include or excluse. Default None else int, float, bool, object, 'number'
        :param exclude: to exclude or include the dtypes
        :param regex: a regiar expression to seach the headers
        :param re_ignore_case: true if the regex should ignore case. Default is False
        :param inplace: if the passed Canonical, should be used or a deep copy
        :param save_intent (optional) if the intent contract should be saved to the property manager
        :param intent_level: (optional) a level to place the intent
        :return: if inplace, returns a formatted cleaner contract for this method, else a deep copy Canonical,.
        """
        # intent persist options
        self._set_intend_signature(self._intent_builder(method=inspect.currentframe().f_code.co_name, params=locals()),
                                   intent_level=intent_level, save_intent=save_intent)
        # intent code
        if not inplace:
            with threading.Lock():
                data = deepcopy(data)

        dup_keys = set()
        keys = list(data.keys())
        for primary in data.keys():
            _ = keys.remove(primary)
            for secondary in keys:
                result = len([i for i, j in zip(data.get(primary), data.get(secondary)) if i == j])
                if result == len(data.get(primary)):
                    dup_keys.add(secondary)

        for dup in dup_keys:
            data.pop(dup)
        if not inplace:
            return data

    def to_remove(self, data: dict, headers: [str, list]=None, drop: bool=False, dtype: [str, list]=None,
                  exclude: bool=False, regex: [str, list]=None, re_ignore_case: bool=True,
                  inplace: bool=False, save_intent: bool=None, intent_level: [int, str]=None) -> dict:
        """ remove columns from the Canonical,

        :param data: the Canonical data to get the column headers from
        :param headers: a list of headers to drop or filter on type
        :param drop: to drop or not drop the headers
        :param dtype: the column types to include or excluse. Default None else int, float, bool, object, 'number'
        :param exclude: to exclude or include the dtypes
        :param regex: a regiar expression to seach the headers
        :param re_ignore_case: true if the regex should ignore case. Default is False
        :param inplace: if the passed Canonical, should be used or a deep copy
        :param save_intent (optional) if the intent contract should be saved to the property manager
        :param intent_level: (optional) a level to place the intent
        :return: if inplace, returns a formatted cleaner contract for this method, else a deep copy Canonical,.
        """
        # intent persist options
        self._set_intend_signature(self._intent_builder(method=inspect.currentframe().f_code.co_name, params=locals()),
                                   intent_level=intent_level, save_intent=save_intent)
        # intent code
        if not inplace:
            with threading.Lock():
                data = deepcopy(data)

        selection = self.filter_headers(data=data, headers=headers, drop=drop, dtype=dtype, exclude=exclude,
                                        regex=regex, re_ignore_case=re_ignore_case)
        for c in selection:
            data.pop(c)
        if not inplace:
            return data

    def to_select(self, data: dict, headers: [str, list]=None, drop: bool=False, dtype: [str, list]=None,
                  exclude: bool=False, regex: [str, list]=None, re_ignore_case: bool=True,
                  inplace: bool=False, save_intent: bool=None, intent_level: [int, str]=None) -> dict:
        """ remove columns from the Canonical,

        :param data: the Canonical data to get the column headers from
        :param headers: a list of headers to drop or filter on type
        :param drop: to drop or not drop the headers
        :param dtype: the column types to include or excluse. Default None else int, float, bool, object, 'number'
        :param exclude: to exclude or include the dtypes
        :param regex: a regiar expression to seach the headers
        :param re_ignore_case: true if the regex should ignore case. Default is False
        :param inplace: if the passed Canonical, should be used or a deep copy
        :param save_intent (optional) if the intent contract should be saved to the property manager
        :param intent_level: (optional) a level to place the intent
        :return: if inplace, returns a formatted cleaner contract for this method, else a deep copy Canonical,.
        """
        # intent persist options
        self._set_intend_signature(self._intent_builder(method=inspect.currentframe().f_code.co_name, params=locals()),
                                   intent_level=intent_level, save_intent=save_intent)
        # intent code
        if not inplace:
            with threading.Lock():
                data = deepcopy(data)

        data = self.filter_columns(data=data, headers=headers, drop=drop, dtype=dtype, exclude=exclude, regex=regex,
                                   re_ignore_case=re_ignore_case, inplace=True)
        if not inplace:
            return data

    def to_bool_type(self, data: dict, bool_map, headers: [str, list]=None, drop: bool=False, dtype: [str, list]=None,
                     exclude: bool=False, regex: [str, list]=None, re_ignore_case: bool=True,
                     inplace: bool=False, save_intent: bool=None, intent_level: [int, str]=None) -> dict:
        """ converts column to bool based on the map

        :param data: the Canonical data to get the column headers from
        :param bool_map: a mapping of what to make True and False
        :param headers: a list of headers to drop or filter on type
        :param drop: to drop or not drop the headers
        :param dtype: the column types to include or excluse. Default None else int, float, bool, object, 'number'
        :param exclude: to exclude or include the dtypes
        :param regex: a regiar expression to seach the headers
        :param re_ignore_case: true if the regex should ignore case. Default is False
        :param inplace: if the passed Canonical, should be used or a deep copy
        :param save_intent (optional) if the intent contract should be saved to the property manager
        :param intent_level: (optional) a level to place the intent
        :return: if inplace, returns a formatted cleaner contract for this method, else a deep copy Canonical,.
        """
        # intent persist options
        self._set_intend_signature(self._intent_builder(method=inspect.currentframe().f_code.co_name, params=locals()),
                                   intent_level=intent_level, save_intent=save_intent)
        # intent code
        if not inplace:
            with threading.Lock():
                data = deepcopy(data)

        selection = self.filter_headers(data=data, headers=headers, drop=drop, dtype=dtype, exclude=exclude,
                                        regex=regex, re_ignore_case=re_ignore_case)
        for c in selection:
            values = data.pop(c)
            data[c] = [bool(x) for x in values]
        if not inplace:
            return data

    def to_numeric_type(self, data: dict, headers: [str, list]=None, drop: bool=False, dtype: [str, list]=None,
                        exclude: bool=False, regex: [str, list]=None, re_ignore_case: bool=True, precision: int=None,
                        fillna: str=None, errors: str=None, inplace: bool=False, save_intent: bool=None,
                        intent_level: [int, str]=None) -> dict:
        """ converts columns to int type

        :param data: the Canonical data to get the column headers from
        :param headers: a list of headers to drop or filter on type
        :param drop: to drop or not drop the headers
        :param dtype: the column types to include or excluse. Default None else int, float, bool, object, 'number'
        :param exclude: to exclude or include the dtypes
        :param regex: a regiar expression to seach the headers
        :param re_ignore_case: true if the regex should ignore case. Default is False
        :param precision: how many decimal places to set the return values. if None then the number is unchanged
        :param fillna: { num_value, 'mean', 'mode', 'median' }. Default to np.nan
                    - If num_value, then replaces NaN with this number value. Must be a value not a string
                    - If 'mean', then replaces NaN with the mean of the column
                    - If 'mode', then replaces NaN with a mode of the column. random sample if more than 1
                    - If 'median', then replaces NaN with the median of the column
        :param errors : {'ignore', 'raise', 'coerce'}, default 'coerce'
                    - If 'raise', then invalid parsing will raise an exception
                    - If 'coerce', then invalid parsing will be set as NaN
                    - If 'ignore', then invalid parsing will return the input
        :param inplace: if the passed Canonical, should be used or a deep copy
        :param save_intent (optional) if the intent contract should be saved to the property manager
        :param intent_level: (optional) a level to place the intent
        :return: if inplace, returns a formatted cleaner contract for this method, else a deep copy Canonical,.
        """
        # intent persist options
        self._set_intend_signature(self._intent_builder(method=inspect.currentframe().f_code.co_name, params=locals()),
                                   intent_level=intent_level, save_intent=save_intent)
        # intent code
        precision = 3 if not isinstance(precision, int) else precision
        if not inplace:
            with threading.Lock():
                data = deepcopy(data)

        selection = self.filter_headers(data=data, headers=headers, drop=drop, dtype=dtype, exclude=exclude,
                                        regex=regex, re_ignore_case=re_ignore_case)
        for c in selection:
            values = data.pop(c)
            values = [round(float(x), precision) for x in values if isinstance(x, float)]
            values = [int(x) for x in values if isinstance(x, int)]
            data[c] = [float('nan') for x in values if not isinstance(x, (float, int))]
        if not inplace:
            return data

    def to_int_type(self, data: dict, headers: [str, list]=None, drop: bool=False, dtype: [str, list]=None,
                    exclude: bool=False, regex: [str, list]=None, re_ignore_case: bool=True, fillna: str=None,
                    errors: str=None, inplace: bool=False, save_intent: bool=None,
                    intent_level: [int, str]=None) -> dict:
        """ converts columns to int type

        :param data: the Canonical data to get the column headers from
        :param headers: a list of headers to drop or filter on type
        :param drop: to drop or not drop the headers
        :param dtype: the column types to include or excluse. Default None else int, float, bool, object, 'number'
        :param exclude: to exclude or include the dtypes
        :param regex: a regiar expression to seach the headers
        :param re_ignore_case: true if the regex should ignore case. Default is False
        :param fillna: { num_value, 'mean', 'mode', 'median' }. Default to 0
                    - If num_value, then replaces NaN with this number value
                    - If 'mean', then replaces NaN with the mean of the column
                    - If 'mode', then replaces NaN with a mode of the column. random sample if more than 1
                    - If 'median', then replaces NaN with the median of the column
        :param errors : {'ignore', 'raise', 'coerce'}, default 'coerce'
                    - If 'raise', then invalid parsing will raise an exception
                    - If 'coerce', then invalid parsing will be set as NaN
                    - If 'ignore', then invalid parsing will return the input
        :param inplace: if the passed Canonical, should be used or a deep copy
        :param save_intent (optional) if the intent contract should be saved to the property manager
        :param intent_level: (optional) a level to place the intent
        :return: if inplace, returns a formatted cleaner contract for this method, else a deep copy Canonical,.
        """
        # intent persist options
        self._set_intend_signature(self._intent_builder(method=inspect.currentframe().f_code.co_name, params=locals()),
                                   intent_level=intent_level, save_intent=save_intent)
        # intent code
        if not inplace:
            with threading.Lock():
                data = deepcopy(data)

        selection = self.filter_headers(data=data, headers=headers, drop=drop, dtype=dtype, exclude=exclude,
                                        regex=regex, re_ignore_case=re_ignore_case)
        for c in selection:
            values = data.pop(c)
            data[c] = [int(x) if isinstance(x, (float, int)) else int('nan') for x in values]
            if errors == 'raise':
                if int('nan') in data.get(c):
                    raise ValueError("Not all values can be converted to int")
        if not inplace:
            return data

    def to_float_type(self, data: dict, headers: [str, list]=None, drop: bool=False, dtype: [str, list]=None,
                      exclude: bool=False, regex: [str, list]=None, re_ignore_case: bool=True, precision: int=None,
                      fillna: str=None, errors: str=None, inplace: bool=False, save_intent: bool=None,
                      intent_level: [int, str]=None) -> dict:
        """ converts columns to float type

        :param data: the Canonical data to get the column headers from
        :param headers: a list of headers to drop or filter on type
        :param drop: to drop or not drop the headers
        :param dtype: the column types to include or excluse. Default None else int, float, bool, object, 'number'
        :param exclude: to exclude or include the dtypes
        :param regex: a regiar expression to seach the headers
        :param re_ignore_case: true if the regex should ignore case. Default is False
        :param precision: how many decimal places to set the return values. if None then the number is unchanged
        :param fillna: { num_value, 'mean', 'mode', 'median' }. Default to np.nan
                    - If num_value, then replaces NaN with this number value
                    - If 'mean', then replaces NaN with the mean of the column
                    - If 'mode', then replaces NaN with a mode of the column. random sample if more than 1
                    - If 'median', then replaces NaN with the median of the column
        :param errors : {'ignore', 'raise', 'coerce'}, default 'coerce' }. Default to 'coerce'
                    - If 'raise', then invalid parsing will raise an exception
                    - If 'coerce', then invalid parsing will be set as NaN
                    - If 'ignore', then invalid parsing will return the input
        :param inplace: if the passed Canonical, should be used or a deep copy
        :param save_intent (optional) if the intent contract should be saved to the property manager
        :param intent_level: (optional) a level to place the intent
        :return: if inplace, returns a formatted cleaner contract for this method, else a deep copy Canonical,.
        """
        # intent persist options
        self._set_intend_signature(self._intent_builder(method=inspect.currentframe().f_code.co_name, params=locals()),
                                   intent_level=intent_level, save_intent=save_intent)
        # intent code
        precision = 3 if not isinstance(precision, int) else precision
        if not inplace:
            with threading.Lock():
                data = deepcopy(data)

        selection = self.filter_headers(data=data, headers=headers, drop=drop, dtype=dtype, exclude=exclude,
                                        regex=regex, re_ignore_case=re_ignore_case)
        for c in selection:
            values = data.pop(c)
            data[c] = [round(float(x), precision) if isinstance(x, (float, int)) else float('nan') for x in values]
        if not inplace:
            return data

    def to_str_type(self, data: dict, headers: [str, list]=None, drop: bool=False, dtype: [str, list]=None,
                    exclude: bool=False, regex: [str, list]=None, re_ignore_case: bool=True, inplace: bool=False,
                    save_intent: bool=None, intent_level: [int, str]=None,
                    nulls_list: [bool, list]=None) -> dict:
        """ converts columns to object type

        :param data: the Canonical data to get the column headers from
        :param headers: a list of headers to drop or filter on type
        :param drop: to drop or not drop the headers
        :param dtype: the column types to include or excluse. Default None else int, float, bool, object, 'number'
        :param exclude: to exclude or include the dtypes
        :param regex: a regiar expression to seach the headers
        :param re_ignore_case: true if the regex should ignore case. Default is False
        :param nulls_list: can be boolean or a list:
                    if boolean and True then null_list equals ['NaN', 'nan', 'null', '', 'None']
                    if list then this is considered potential null values.
        :param inplace: if the passed Canonical, should be used or a deep copy
        :param save_intent (optional) if the intent contract should be saved to the property manager
        :param intent_level: (optional) a level to place the intent
        :return: if inplace, returns a formatted cleaner contract for this method, else a deep copy Canonical,.
       """
        # intent persist options
        self._set_intend_signature(self._intent_builder(method=inspect.currentframe().f_code.co_name, params=locals()),
                                   intent_level=intent_level, save_intent=save_intent)
        # intent code
        if not inplace:
            with threading.Lock():
                data = deepcopy(data)

        selection = self.filter_headers(data=data, headers=headers, drop=drop, dtype=dtype, exclude=exclude,
                                        regex=regex, re_ignore_case=re_ignore_case)
        for c in selection:
            values = data.pop(c)
            data[c] = [str(x) if x is not None else None for x in values]
        if not inplace:
            return data

    def to_date_type(self, data: dict, headers: [str, list]=None, drop: bool=False, dtype: [str, list]=None,
                     exclude: bool=False, regex: [str, list]=None, re_ignore_case: bool=None, as_num: bool=False,
                     day_first: bool=False, year_first: bool=False, inplace: bool=False,
                     save_intent: bool=None, intent_level: [int, str]=None) -> dict:
        """ converts columns to date types

        :param data: the Canonical data to get the column headers from
        :param headers: a list of headers to drop or filter on type
        :param drop: to drop or not drop the headers
        :param dtype: the column types to include or excluse. Default None else int, float, bool, object, 'number'
        :param exclude: to exclude or include the dtypes
        :param regex: a regiar expression to seach the headers
        :param re_ignore_case: true if the regex should ignore case. Default is False
        :param inplace: if the passed Canonical, should be used or a deep copy
        :param save_intent (optional) if the intent contract should be saved to the property manager
        :param intent_level: (optional) a level to place the intent
        :param as_num: if true returns number of days since 0001-01-01 00:00:00 with fraction being hours/mins/secs
        :param year_first: specifies if to parse with the year first
                If True parses dates with the year first, eg 10/11/12 is parsed as 2010-11-12.
                If both dayfirst and yearfirst are True, yearfirst is preceded (same as dateutil).
        :param day_first: specifies if to parse with the day first
                If True, parses dates with the day first, eg %d-%m-%Y.
                If False default to the a prefered preference, normally %m-%d-%Y (but not strict)
        :return: if inplace, returns a formatted cleaner contract for this method, else a deep copy Canonical,.
        """
        self._set_intend_signature(self._intent_builder(method=inspect.currentframe().f_code.co_name, params=locals()),
                                   intent_level=intent_level, save_intent=save_intent)
        if not inplace:
            with threading.Lock():
                data = deepcopy(data)

        selection = self.filter_headers(data=data, headers=headers, drop=drop, dtype=dtype, exclude=exclude,
                                        regex=regex, re_ignore_case=re_ignore_case)
        for c in selection:
            values = data.pop(c)
            data[c] = [datetime.strptime(x, '%m/%d/%Y') for x in values]
        if not inplace:
            return data

    @staticmethod
    def filter_headers(data: dict, headers: [str, list]=None, drop: bool=None, dtype: [str, list]=None,
                       exclude: bool=None, regex: [str, list]=None, re_ignore_case: bool=None) -> list:
        """ returns a list of headers based on the filter criteria

        :param data: the Canonical data to get the column headers from
        :param headers: a list of headers to drop or filter on type
        :param drop: to drop or not drop the headers
        :param dtype: the column types to include or excluse. Default None else int, float, bool, object, 'number'
        :param exclude: to exclude or include the dtypes. Default is False
        :param regex: a regiar expression to seach the headers
        :param re_ignore_case: true if the regex should ignore case. Default is False
        :return: a filtered list of headers

        :raise: TypeError if any of the types are not as expected
        """
        if drop is None or not isinstance(drop, bool):
            drop = False
        if exclude is None or not isinstance(exclude, bool):
            exclude = False
        if re_ignore_case is None or not isinstance(re_ignore_case, bool):
            re_ignore_case = False

        if not isinstance(data, dict):
            raise TypeError("The first function attribute must be a dictionary")
        _headers = AbstractPropertyManager.list_formatter(headers)
        dtype = AbstractPropertyManager.list_formatter(dtype)
        regex = AbstractPropertyManager.list_formatter(regex)
        _obj_cols = list(data.keys())
        _rtn_cols = set()
        unmodified = True

        if _headers is not None and _headers:
            _rtn_cols = set(_obj_cols).difference(_headers) if drop else set(_obj_cols).intersection(_headers)
            unmodified = False

        if regex is not None and regex:
            re_ignore_case = re.I if re_ignore_case else 0
            _regex_cols = list()
            for exp in regex:
                _regex_cols += [s for s in _obj_cols if re.search(exp, s, re_ignore_case)]
            _rtn_cols = _rtn_cols.union(set(_regex_cols))
            unmodified = False

        if unmodified:
            _rtn_cols = set(_obj_cols)

        if dtype is not None and dtype:
            type_header = []
            for col in _rtn_cols:
                if any((isinstance(x, tuple(dtype)) for x in col)):
                    type_header.append(col)
            _rtn_cols = set(_rtn_cols).difference(type_header) if exclude else set(_rtn_cols).intersection(type_header)

        return [c for c in _rtn_cols]

    def filter_columns(self, data: dict, headers=None, drop=False, dtype=None, exclude=False, regex=None,
                       re_ignore_case=None, inplace=False) -> dict:
        """ Returns a subset of columns based on the filter criteria

        :param data: the Canonical data to get the column headers from
        :param headers: a list of headers to drop or filter on type
        :param drop: to drop or not drop the headers
        :param dtype: the column types to include or excluse. Default None else int, float, bool, object, 'number'
        :param exclude: to exclude or include the dtypes
        :param regex: a regiar expression to seach the headers
        :param re_ignore_case: true if the regex should ignore case. Default is False
        :param inplace: if the passed pandas.DataFrame should be used or a deep copy
        :return:
        """
        if not inplace:
            with threading.Lock():
                data = deepcopy(data)
        obj_cols = self.filter_headers(data=data, headers=headers, drop=drop, dtype=dtype, exclude=exclude,
                                       regex=regex, re_ignore_case=re_ignore_case)
        for col in data.keys():
            if col not in obj_cols:
                data.pop(col)
        return data
