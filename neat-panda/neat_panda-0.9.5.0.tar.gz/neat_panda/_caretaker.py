# -*- coding: utf-8 -*-

import re
from dataclasses import dataclass
from collections import Counter
from typing import Union, List, Dict, Optional

import pandas as pd
import pandas_flavor as pf


@pf.register_dataframe_method
def clean_column_names(
    object_: Union[List[Union[str, int]], pd.Index, pd.DataFrame],
    case_type: str = "snake",
    basic_cleaning: bool = True,
    convert_duplicates: bool = True,
    custom_transformation: Optional[Dict[str, str]] = None,
    custom_expressions: Optional[List[str]] = None,
):
    """Clean messy column names. Inspired by the functions make_clean_names and clean_names from
    the R package janitor.

    Alters the columns of the original DataFrame. Use copy [e.g. df.clean_column_names().copy()] if this behavior is not desired.

    Parameters
    ----------
    object_: Union[List[Union[str, int]], pd.Index, pd.DataFrame]\n
        Messy strings in a list, pandas index or a pandas dataframe with messy columnames
    case_type: str\n
        Which case type to use, the alternatives are: snake (s) [case_type], camel (c) [caseType], pascal (p) [CaseType]. Not case sensitive.
        Equals 'snake' by default.
    basic_cleaning: bool\n
        Performs basic cleaning of the strings if supplied. Performs three actions:
            1. Replaces multiple spaces with one space\n
            2. Replaces all non-alphanumeric characters in a string (except underscore) with underscore\n
            3. Removes leading and lagging underscores
        By default True.\n
    convert_duplicates : bool, optional\n
        If True, unique columnnames are created. E.g. if there are two columns, country and Country (and the case type is 'snake'),
        this option set the columnnames to country1 and country2. By default True.\n
    custom_transformation : Dict[Any, Any], optional\n
        If you want to replace one specific character with another specific character.
        E.g if you want exclamationpoints to be replaced with dollarsigns, pass the following:
        /{'!':'$'/}. Use with caution if the custom_expressions parameter is used since the custom_expressions parameter
        is evaluated after the custom_transformation parameter.
        Cannot be used together with basic_cleaning, i.e. to use custom transformations basic_cleaning must be set to False.\n
        By default None
    custom_expressions : List[str], optional\n
        In this parameter any string method or regex can be passed. They must be passed as a string
        with column as object. E.g if you want, as in the example with in the custom_transformation parameter, wants
        to exclamation point to be replaced with dollarsign, pass the following:
         ["column.replace('!', '$')"]
        or you want capitalize the columns:
         ["column.capitalize()"]
        or you want to replace multiple spaces with one space:
         [r're.sub(r"\s+", " ", column).strip()'] # noqa: W605
        or if you want to do all of the above:
        ['column.replace("!", "$")',
         'column.capitalize()',
         r're.sub(r"\s+", " ", column).strip()' # noqa: W605
        ]
        By default None
    Returns
    -------
    List[str] or a pandas DataFrame\n
        A list of cleaned columnames or a dataframe with cleaned columnames

    Raises
    ------
    TypeError\n
        Raises TypeError if the passed object_ is not a list, pandas index or a pandas dataframe
    KeyError\n
        Raises KeyError if both basic_cleaning and custom_transformations is used.
    """
    return CleanColumnNames(
        object_,
        case_type,
        basic_cleaning,
        convert_duplicates,
        custom_transformation,
        custom_expressions,
    ).clean_column_names()


@dataclass
class CleanColumnNames:
    """Clean messy column names. Inspired by the functions make_clean_names and clean_names from
    the R package janitor.

    snake_case: Code is based on code from [StackOverflow](https://stackoverflow.com/questions/1175208/elegant-python-function-to-convert-camelcase-to-snake-case)

    camelCase: Code is based on code from [StackOverflow](https://stackoverflow.com/questions/19053707/converting-snake-case-to-lower-camel-case-lowercamelcase)

    Parameters
    ----------
    object_: Union[List[Union[str, int]], pd.Index, pd.DataFrame]\n
        Messy strings in a list, pandas index or a pandas dataframe with messy columnames
    case_type: str\n
        Which case type to use, the alternatives are: snake (s) [case_type], camel (c) [caseType], pascal (p) [CaseType]. Not case sensitive.
        Equals 'snake' by default.
    basic_cleaning: bool\n
        Performs basic cleaning of the strings if supplied. Performs three actions:
            1. Replaces multiple spaces with one space\n
            2. Replaces all non-alphanumeric characters in a string (except underscore) with underscore\n
            3. Removes leading and lagging underscores
        By default True.\n
    convert_duplicates : bool, optional\n
        If True, unique columnnames are created. E.g. if there are two columns, country and Country (and the case type is 'snake'),
        this option set the columnnames to country1 and country2. By default True.\n
    custom_transformation : Dict[Any, Any], optional\n
        If you want to replace one specific character with another specific character.
        E.g if you want exclamationpoints to be replaced with dollarsigns, pass the following:
        /{'!':'$'/}. Use with caution if the custom_expressions parameter is used since the custom_expressions parameter
        is evaluated after the custom_transformation parameter.
        Cannot be used together with basic_cleaning, i.e. to use custom transformations basic_cleaning must be set to False.\n
        By default None
    custom_expressions : List[str], optional\n
        In this parameter any string method or regex can be passed. They must be passed as a string
        with column as object. E.g if you want, as in the example with in the custom_transformation parameter, wants
        to exclamation point to be replaced with dollarsign, pass the following:
         ["column.replace('!', '$')"]
        or you want capitalize the columns:
         ["column.capitalize()"]
        or you want to replace multiple spaces with one space:
         [r're.sub(r"\s+", " ", column).strip()'] # noqa: W605
        or if you want to do all of the above:
        ['column.replace("!", "$")',
         'column.capitalize()',
         r're.sub(r"\s+", " ", column).strip()' # noqa: W605
        ]
        By default None
    Returns
    -------
    List[str] or a pandas DataFrame\n
        A list of cleaned columnames or a dataframe with cleaned columnames

    Raises
    ------
    TypeError\n
        Raises TypeError if the passed object_ is not a list, pandas index or a pandas dataframe
    KeyError\n
        Raises KeyError if both basic_cleaning and custom_transformations is used.

    Example
    -------
    ```python
    # Pandas
    import pandas as pd
    import neat_panda

    df = pd.DataFrame(
    data={
        "CountryName": ["Sweden", "Sweden", "Denmark"],
        "Continent": ["Europe", "Europe", "Not known"],
        "yearNo": [2018, 2019, 2018],
        "ACTUAL": [1, 2, 3],
        }
    )
    print(df.columns.to_list()) # ['CountryName', 'Continent', 'yearNo', 'ACTUAL']
    df = df.clean_column_names()
    print(df.columns.to_list()) # ['CountryName', 'Continent', 'yearNo', 'ACTUAL']


    # Cleaning of list
    from neat_panda import clean_column_names
    # snake_case
    a = ["CountryName", "subRegion"]
    b = clean_column_names(columns=a) # ["country_name", "sub_region"]
    # camelCase
    c = clean_column_names(columns=b, case_type="camel") # ["countryName", "subRegion"]
    # PascalCase
    d = clean_column_names(columns=b, case_type="pascal") # ["CountryName", "SubRegion"]
    ```
    """

    object_: Union[List[Union[str, int]], pd.Index, pd.DataFrame]
    case_type: str = "snake"
    basic_cleaning: bool = True
    convert_duplicates: bool = True
    custom_transformation: Optional[Dict[str, str]] = None
    custom_expressions: Optional[List[str]] = None

    SNAKE = [
        r're.sub(r"(.)([A-Z][a-z]+)", r"\1\2", column)',
        r're.sub(r"([a-z0-9])([A-Z])", r"\1_\2", column).lower().replace("__", "_")',
    ]
    CAMEL = SNAKE + [r're.sub(r"_([a-zA-Z0-9])", lambda x: x.group(1).upper(), column)']
    PASCAL = CAMEL + [r"column[0].upper() + column[1:]"]

    def clean_column_names(self) -> Union[List[str], pd.DataFrame]:
        """Clean messy column names. Inspired by the functions make_clean_names and clean_names from
        the R package janitor.

        Returns
        -------
        List[str] or a pandas DataFrame\n
            A list of cleaned columnames or a dataframe with cleaned columnames

        Raises
        ------
        TypeError\n
            Raises TypeError if the passed object_ is not a list, pandas index or a pandas dataframe
        """
        if self.basic_cleaning and self.custom_transformation:
            raise KeyError(
                "Both basic_cleaning and custom_transformation is set. This is not aloud. Choose one!"
            )
        if isinstance(self.object_, (list, pd.Index)):
            columns = self._clean_column_names_list()
            return columns
        elif isinstance(self.object_, pd.DataFrame):
            df = self._clean_column_names_dataframe()
            return df
        else:
            raise TypeError(
                f"The passed object_ is a {type(self.object_)}. It must be a list, pandas index or a pandas dataframe!"
            )

    def _clean_column_names_list(self) -> List[str]:
        """Cleans messy columnames. Written to be a utility function.

        Returns
        -------
        List[str]\n
            Cleaned columnnames
        """
        columns = self.object_
        if self.basic_cleaning:
            columns = self._basic_cleaning(columns=columns)
        columns = self._clean_column_names(columns)
        return columns

    def _basic_cleaning(self, columns) -> List[str]:
        for reg in self._basic_cleaning_expression():
            columns = [
                eval(reg, {}, {"column": column, "re": re}) for column in columns
            ]
        return columns

    def _clean_column_names_dataframe(self) -> pd.DataFrame:
        """Cleans messy columnames of a dataframe. Written to be a utility function. It is recommended
        to use the clean_columnames function instead.

        Does not alter the original DataFrame.

        Returns
        -------
        pd.DataFrame\n
            A dataframe with cleaned columnames

        Raises
        ------
        TypeError\n
            If the df object is not a pandas dataframe TypeError is raised
        """
        if not isinstance(self.object_, pd.DataFrame):
            raise TypeError(
                f"The passed df is a {type(self.object_)}. It must be a pandas dataframe!"
            )
        self.object_.columns = self._clean_column_names_list()
        return self.object_

    def _clean_column_names(self, columns) -> List[str]:
        """Base function for clean_columnames. Can be used for very specific needs.
        ----------
        columns : Union[List[Union[str, int]], pd.Index]\n
            Messy columnnames

        Returns
        -------
        List[str]\n
            Clean columnnames

        Raises
        ------
        TypeError\n
            If passed column object is not a list or a pandas index TypeError is raised
        """
        if not isinstance(columns, (list, pd.Index)):
            raise TypeError(
                f"The passed columns is a {type(columns)}. It must be a list or a pandas index!"
            )
        if type(columns) == pd.Index:
            columns = columns.to_list()  # type: ignore
        columns = [str(column) for column in columns]
        if self.custom_transformation:
            for i, j in self.custom_transformation.items():
                columns = [k.replace(i, j) for k in columns]
        if self.custom_expressions:
            columns = self._expressions_eval(
                columns=columns, expressions=self.custom_expressions
            )
        if self.case_type:
            # columns = self._case_chooser(columns=columns)
            _expressions = self._expressions_case_setter()
            columns = self._expressions_eval(columns=columns, expressions=_expressions)
        if self.convert_duplicates:
            columns = self._convert_duplicates(columns=columns)
        return columns

    def _expressions_case_setter(self):
        if self.case_type.lower() not in ["camel", "pascal", "snake", "c", "p", "s"]:
            raise KeyError()
        if self.case_type[0].lower() == "s":
            return self.SNAKE
        elif self.case_type[0].lower() == "c":
            return self.CAMEL
        else:
            return self.PASCAL

    def _expressions_eval(self, columns, expressions):
        for reg in expressions:
            columns = [
                eval(reg, {}, {"column": column, "re": re}) for column in columns
            ]
        return columns

    @staticmethod
    def _convert_duplicates(columns: List[str]) -> List[str]:
        """Adds progressive numbers to a list of duplicate strings. Ignores non-duplicates.

        Function is based on code from [StackOverflow](https://stackoverflow.com/questions/30650474/python-rename-duplicates-in-list-with-progressive-numbers-without-sorting-list/30651843#30651843)

        Parameters
        ----------
        columns : List[str]\n
            A list of strings

        Returns
        -------
        List[str]\n
            A list of strings with progressive numbers added to duplicates.

        Example
        -------
        ```python
        a = ["country_name", "sub_region", "country_name"]\n
        b = _convert_duplicates(columns=a)\n
        print(b)
        ["country_name1", "sub_region", "country_name2"]
        ```


        """
        d: Dict[str, List] = {
            a: list(range(1, b + 1)) if b > 1 else []
            for a, b in Counter(columns).items()
        }
        columns = [i + str(d[i].pop(0)) if len(d[i]) else i for i in columns]
        return columns

    @staticmethod
    def _basic_cleaning_expression() -> List[str]:
        """
        Regex that replace multiple spaces with one space i based on the user Nasir's answer at
        [StackOverflow](https://stackoverflow.com/questions/1546226/simple-way-to-remove-multiple-spaces-in-a-string)

        Regex that replace all non-alphanumeric characters in a string (except underscore) with underscore
        is based on the user psun's answer at [StackOverflow](https://stackoverflow.com/questions/12985456/replace-all-non-alphanumeric-characters-in-a-string/12985459)
        """
        return [
            r"str(column)",  # ensure string type
            r're.sub(r"\s+", " ", column).strip()',  # replace multiple spaces with one space
            r're.sub(r"\W+", "_", column).strip()',  # replace all non-alphanumeric characters in a string (except underscore) with underscore
            r'column.rstrip("_").lstrip("_")',  # remove leading and lagging underscores
        ]


if __name__ == "__main__":
    pass
