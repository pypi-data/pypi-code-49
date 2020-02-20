from teradatasqlalchemy import (BYTEINT, SMALLINT, INTEGER, BIGINT, DECIMAL, FLOAT, NUMBER)
from teradatasqlalchemy import (TIMESTAMP, DATE, TIME)
from teradatasqlalchemy import (CHAR, VARCHAR, CLOB)
from teradatasqlalchemy import (BYTE, VARBYTE, BLOB)
from teradatasqlalchemy import (PERIOD_DATE, PERIOD_TIME, PERIOD_TIMESTAMP)
from teradatasqlalchemy import (INTERVAL_YEAR, INTERVAL_YEAR_TO_MONTH, INTERVAL_MONTH, INTERVAL_DAY,
                                      INTERVAL_DAY_TO_HOUR, INTERVAL_DAY_TO_MINUTE, INTERVAL_DAY_TO_SECOND,
                                      INTERVAL_HOUR, INTERVAL_HOUR_TO_MINUTE, INTERVAL_HOUR_TO_SECOND,
                                      INTERVAL_MINUTE, INTERVAL_MINUTE_TO_SECOND, INTERVAL_SECOND)
from teradataml.common.constants import TeradataTypes, PythonTypes

class _Dtypes:
    @staticmethod
    def _get_numeric_datatypes():
        """
        Returns the numeric data types used in Teradata Vantage
        **From : https://www.info.teradata.com/HTMLPubs/DB_TTU_16_00/
        index.html#page/General_Reference/B035-1091-160K/psa1472241434371.html

        PARAMETERS:
            None

        RAISES:
            None

        RETURNS:
            List of numeric data types used in Teradata Vantage
        """
        return [BYTEINT, SMALLINT, INTEGER, BIGINT, DECIMAL, FLOAT, NUMBER]

    @staticmethod
    def _get_timedate_datatypes():
        """
        Returns a list of TimeDate data types.

        PARAMETERS:
            None

        RAISES:
            None

        RETURNS:
            List of TimeDate data types used in Teradata Vantage
        """
        return [TIMESTAMP, DATE, TIME]

    @staticmethod
    def _get_character_datatypes():
        """
        Returns a list of Character data types.

        PARAMETERS:
            None

        RAISES:
            None

        RETURNS:
            List of Character data types used in Teradata Vantage
        """
        return [CHAR , VARCHAR, CLOB]

    @staticmethod
    def _get_byte_datatypes():
        """
        Returns a list of byte like data types.

        PARAMETERS:
            None

        RAISES:
            None

        RETURNS:
            List of Byte data types used in Teradata Vantage
        """
        return [BYTE , VARBYTE, BLOB]

    @staticmethod
    def _get_categorical_datatypes():
        """
        Returns a list of containing Character and TimeDate data types.

        PARAMETERS:
            None

        RAISES:
            None

        RETURNS:
            List of Character and TimeDate data types used in Teradata Vantage
        """
        return list.__add__(_Dtypes._get_character_datatypes(), _Dtypes._get_timedate_datatypes())

    @staticmethod
    def _get_all_datatypes():
        """
        Returns a list of Character, Numeric and TimeDate data types.

        PARAMETERS:
            None

        RAISES:
            None

        RETURNS:
            List of Character, Numeric and TimeDate data types used in Teradata Vantage
        """
        return list.__add__(_Dtypes._get_categorical_datatypes(), _Dtypes._get_numeric_datatypes())

    @staticmethod
    def _get_unsupported_data_types_for_aggregate_operations(operation, is_time_series_aggregate = False):
        """
        Returns the data types on which aggregate operations cannot
        be performed eg : min, max, avg

        PARAMETERS:
            operation : String. An aggregate operation to be performed
                        on the dataframe

        RAISES:
            None

        RETURNS:
            List of unsupported data types for aggregate operation in
            Teradata Vantage eg : min, max, avg
        """
        # TODO: investigate about unsupported data types of other
        # TODO: aggregate operations and return the same
        # TODO: by adding more else if's
        if operation in ['min', 'max']:
            return [BLOB, CLOB, PERIOD_DATE, PERIOD_TIME, PERIOD_TIMESTAMP]
        elif operation == 'mean':
            return [BLOB, BYTE, CHAR, CLOB, PERIOD_DATE, PERIOD_TIME, PERIOD_TIMESTAMP, TIME, TIMESTAMP, VARBYTE,
                    VARCHAR]
        elif operation in ['sum', 'percentile']:
            return [BLOB, BYTE, CHAR, CLOB, DATE, PERIOD_DATE, PERIOD_TIME, PERIOD_TIMESTAMP, TIME, TIMESTAMP, VARBYTE,
                    VARCHAR]
        elif operation in ['count', 'unique']:
            return []
        elif operation in ['std', 'var']:
            return [BLOB, BYTE, CHAR, CLOB, PERIOD_DATE, PERIOD_TIME, PERIOD_TIMESTAMP, TIME, TIMESTAMP, VARBYTE,
                    VARCHAR]
        elif operation == 'median' and not is_time_series_aggregate:
            return [BLOB, BYTE, CHAR, CLOB, DATE, PERIOD_DATE, PERIOD_TIME, PERIOD_TIMESTAMP, TIME, TIMESTAMP, VARCHAR]
        elif operation in ['bottom', 'bottom with ties', 'first', 'last', 'mad', 'median', 'mode', 'top', 
                           'top with ties']:
            return [BLOB, BYTE, CHAR, CLOB, DATE, INTERVAL_DAY, INTERVAL_DAY_TO_HOUR, INTERVAL_DAY_TO_MINUTE,
                    INTERVAL_DAY_TO_SECOND, INTERVAL_HOUR, INTERVAL_HOUR_TO_MINUTE, INTERVAL_HOUR_TO_SECOND,
                    INTERVAL_MINUTE, INTERVAL_MINUTE_TO_SECOND, INTERVAL_MONTH, INTERVAL_SECOND, INTERVAL_YEAR,
                    INTERVAL_YEAR_TO_MONTH, PERIOD_DATE, PERIOD_TIME, PERIOD_TIMESTAMP, TIMESTAMP, TIME, TIMESTAMP,
                    VARBYTE, VARCHAR]
        else:
            return []

    @staticmethod
    def _get_unsupported_data_types_for_describe_operations(operation):
        """
        Returns the data types on which the specified describe aggregate 'operation' cannot
        be performed. This function is used by the method DataFrame.describe().

        PARAMETERS:
            operation : String. An aggregate operation to be performed on the dataframe.
                        possible values are 'sum', 'min', 'max', 'mean','std', 'percentile',
                        'count', and 'unique'.

        RAISES:
            None

        RETURNS:
            List of unsupported data types for describe operation in
            Teradata Vantage eg : min, max, avg
        """
        if operation in ['sum', 'min', 'max', 'mean','std', 'percentile']:
            return [TIMESTAMP, TIME, DATE, PERIOD_TIME, PERIOD_DATE, PERIOD_TIMESTAMP, VARCHAR,
                    CLOB, BLOB, BYTE, VARBYTE, CHAR]
        elif operation in ['count']:
            return []
        elif operation in ['unique']:
            return [BYTEINT, SMALLINT, INTEGER, BIGINT, DECIMAL, FLOAT, NUMBER]
        elif operation in ['bottom', 'bottom with ties', 'first', 'last', 'median', 'mode', 'top', 'top with ties']:
            return [BLOB, BYTE, CHAR, CLOB, DATE, INTERVAL_DAY, INTERVAL_DAY_TO_HOUR, INTERVAL_DAY_TO_MINUTE,
                    INTERVAL_DAY_TO_SECOND, INTERVAL_HOUR, INTERVAL_HOUR_TO_MINUTE, INTERVAL_HOUR_TO_SECOND,
                    INTERVAL_MINUTE, INTERVAL_MINUTE_TO_SECOND, INTERVAL_MONTH, INTERVAL_SECOND, INTERVAL_YEAR,
                    INTERVAL_YEAR_TO_MONTH, PERIOD_DATE, PERIOD_TIME, PERIOD_TIMESTAMP, TIMESTAMP, TIME, TIMESTAMP,
                    VARBYTE, VARCHAR]
        else:
            return []

    @staticmethod
    def _teradata_type_to_python_type(td_type):
        """
        Translate the Teradata type from metaexpr to Python types.
        PARAMETERS:
            td_type - The Teradata type from metaexpr.

        RETURNS:
            The Python type for the given td_type.

        RAISES:

        EXAMPLES:
            # o is an instance of INTEGER
            pytype = _Dtypes._teradata_type_to_python_type(o)

        """

        # loggerlogger.debug("_help_col_to_python_type td_type = {0} ".format(td_type))
        if type(td_type) in TeradataTypes.TD_INTEGER_TYPES:
            return PythonTypes.PY_INT_TYPE
        elif type(td_type) in TeradataTypes.TD_FLOAT_TYPES:
            return PythonTypes.PY_FLOAT_TYPE
        elif type(td_type) in TeradataTypes.TD_DECIMAL_TYPES:
            return PythonTypes.PY_DECIMAL_TYPE
        elif type(td_type) in TeradataTypes.TD_BYTE_TYPES:
            return PythonTypes.PY_BYTES_TYPE
        elif type(td_type) in TeradataTypes.TD_DATETIME_TYPES:
            return PythonTypes.PY_DATETIME_TYPE
        elif type(td_type) in TeradataTypes.TD_TIME_TYPES:
            return PythonTypes.PY_TIME_TYPE
        elif type(td_type) in TeradataTypes.TD_DATE_TYPES:
            return PythonTypes.PY_DATE_TYPE

        return PythonTypes.PY_STRING_TYPE

    @staticmethod
    def _help_col_to_python_type(col_type, storage_format):
        """
        Translate the 1 or 2 character TD type codes from HELP COLUMN to Python types.
        PARAMETERS:
            col_type - The 1 or 2 character type code from HELP COLUMN command.
            storage_format - The storage format from HELP COLUMN command.

        RETURNS:
            The Python type for the given col_type.

        RAISES:

        EXAMPLES:
            pytype = _Dtypes._help_col_to_python_type('CV', None)
            pytype = _Dtypes._help_col_to_python_type('DT', 'CSV')

        """
        if col_type in TeradataTypes.TD_INTEGER_CODES:
            return PythonTypes.PY_INT_TYPE
        elif col_type in TeradataTypes.TD_FLOAT_CODES:
            return PythonTypes.PY_FLOAT_TYPE
        elif col_type in TeradataTypes.TD_DECIMAL_CODES:
            return PythonTypes.PY_DECIMAL_TYPE
        elif col_type in TeradataTypes.TD_BYTE_CODES:
            return PythonTypes.PY_BYTES_TYPE
        elif col_type in TeradataTypes.TD_DATETIME_CODES:
            return PythonTypes.PY_DATETIME_TYPE
        elif col_type in TeradataTypes.TD_TIME_CODES:
            return PythonTypes.PY_TIME_TYPE
        elif col_type in TeradataTypes.TD_DATE_CODES:
            return PythonTypes.PY_DATE_TYPE
        elif col_type == "DT":
            sfmt = storage_format.strip()
            if sfmt == "CSV":
                return PythonTypes.PY_STRING_TYPE
            elif sfmt == "AVRO":
                return PythonTypes.PY_BYTES_TYPE

        return PythonTypes.PY_STRING_TYPE

    @staticmethod
    def _help_col_to_td_type(col_type, udt_name, storage_format):
        """
        Translate the 2 character TD type codes from HELP COLUMN to Teradata types.
        PARAMETERS:
            col_type - The 2 character type code from HELP COLUMN command.
            udt_name - The UDT name from the HELP COLUMN command.
            storage_format - The storage format from HELP COLUMN command.

        RETURNS:
            The Teradata type for the given colType.

        RAISES:

        EXAMPLES:
            tdtype = _Dtypes._help_col_to_td_type('CV', None, None)

        """
        # logger.debug("helpColumnToTeradataTypeName colType = {0} udtName = {1} storageFormat {2}".format(colType, udtName, storageFormat))
        if col_type in DataTypeMapper.HELP_COL_TYPE_TO_TDTYPE.value:
            return DataTypeMapper.HELP_COL_TYPE_TO_TDTYPE.value[col_type]

        if col_type == "DT":
            return "DATASET STORAGE FORMAT {0}".format(storage_format.strip())

        if col_type in ["UD", "US", "UT", "A1", "AN"]:
            if udt_name:
                return udt_name

        return col_type