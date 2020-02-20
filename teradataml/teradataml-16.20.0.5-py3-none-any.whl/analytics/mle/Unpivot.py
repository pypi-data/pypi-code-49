#!/usr/bin/python
# ################################################################## 
# 
# Copyright 2018 Teradata. All rights reserved.
# TERADATA CONFIDENTIAL AND TRADE SECRET
# 
# Primary Owner: Mounika Kotha (mounika.kotha@teradata.com)
# Secondary Owner: Pankaj Purandare (pankajvinod.purandare@teradata.com)
# 
# Version: 1.2
# Function Version: 1.5
# 
# ################################################################## 

import inspect
from teradataml.common.wrapper_utils import AnalyticsWrapperUtils
from teradataml.common.utils import UtilFuncs
from teradataml.context.context import *
from teradataml.dataframe.dataframe import DataFrame
from teradataml.common.aed_utils import AedUtils
from teradataml.analytics.analytic_query_generator import AnalyticQueryGenerator
from teradataml.common.exceptions import TeradataMlException
from teradataml.common.messages import Messages
from teradataml.common.messagecodes import MessageCodes
from teradataml.common.constants import TeradataConstants
from teradataml.dataframe.dataframe_utils import DataFrameUtils as df_utils
from teradataml.options.display import display

class Unpivot:
    
    def __init__(self,
        data = None,
        unpivot = None,
        input_types = False,
        attribute_column = "attribute",
        value_column = "value_col",
        accumulate = None,
        data_sequence_column = None,
        data_order_column = None):
        """
        DESCRIPTION:
            The Unpivot function pivots data that is stored in columns into rows.
            It is the reverse of the Pivot function.

        PARAMETERS:
            data:
                Required Argument.
                Specifies the teradataml DataFrame containing the data to be pivoted.

            data_order_column:
                Optional Argument.
                Specifies Order By columns for data.
                Values to this argument can be provided as a list, if multiple
                columns are used for ordering.
                Types: str OR list of Strings (str)

            unpivot:
                Required Argument.
                Specifies the names of the unpivot columns — the input columns to
                unpivot (convert to rows).
                Types: str OR list of Strings (str)

            input_types:
                Optional Argument.
                Specifies whether the unpivoted value column, in the output teradataml DataFrame,
                has the same data type as its corresponding unpivot column (if
                possible). For each unpivoted column, the function outputs the values
                in a single VARCHAR column. If you specify "true", the function
                outputs each unpivoted value column in a separate column. If the
                unpivot column has a 'real' data type, the unpivoted value column has
                the data type 'float'; if the unpivot column has an 'integer' data type,
                the unpivoted value column has the data type 'int'; if the unpivot
                column has any other data type, the unpivoted value column has the
                data type 'VARCHAR'.
                Default Value: False
                Types: bool

            attribute_column:
                Optional Argument.
                Specifies the name of the unpivoted attribute column in the output
                teradataml DataFrame.
                Default Value: "attribute"
                Types: str

            value_column:
                Optional Argument.
                Specifies the name of the unpivoted value column in the output
                teradataml DataFrame.
                Default Value: "value_col"
                Types: str

            accumulate:
                Required Argument.
                Specifies the names of input columns, other than unpivot columns,
                to copy to the output teradataml DataFrame. You must specify
                these columns in the same order that they appear in the input
                teradataml DataFrame. No accumulate_column can be an unpivot column.
                Types: str OR list of Strings (str)

            data_sequence_column:
                Optional Argument.
                Specifies the list of column(s) that uniquely identifies each row of
                the input argument "data". The argument is used to ensure
                deterministic results for functions which produce results that vary
                from run to run.
                Types: str OR list of Strings (str)

        RETURNS:
            Instance of Unpivot.
            Output teradataml DataFrames can be accessed using attribute
            references, such as UnpivotObj.<attribute_name>.
            Output teradataml DataFrame attribute name is:
                result


        RAISES:
            TeradataMlException


        EXAMPLES:
            # Load example data.
            load_example_data('Unpivot', "unpivot_input")


            # Create teradataml DataFrame objects.
            unpivot_input = DataFrame.from_table("unpivot_input")

            # Example 1 -
            unpivot_out1 = Unpivot(data=unpivot_input,
                                  unpivot = ["temp","pressure","dewpoint"],
                                  input_types = False,
                                  attribute_column = "attribute",
                                  value_column = "value_col",
                                  accumulate = ["sn","city","week"])
            # Print the result
            print(unpivot_out1.result)

            # Example 2 -
            unpivot_out2 = Unpivot(data=unpivot_input,
                                  unpivot = ["temp","pressure","dewpoint"],
                                  input_types = True,
                                  attribute_column = "climate_attributes",
                                  value_column = "attributevalue",
                                  accumulate = ["sn","city","week"])
            # Print the result
            print(unpivot_out2.result)

            # Example 3 -
            unpivot_out3 = Unpivot(data=unpivot_input,
                                  unpivot =  ["temp","pressure","dewpoint"],
                                  input_types = False,
                                  accumulate = ["sn","city","week"])
            # Print the result
            print(unpivot_out3.result)
        
        """
        self.data  = data 
        self.unpivot  = unpivot 
        self.input_types  = input_types 
        self.attribute_column  = attribute_column 
        self.value_column  = value_column 
        self.accumulate  = accumulate 
        self.data_sequence_column  = data_sequence_column 
        self.data_order_column  = data_order_column 
        
        # Create TeradataPyWrapperUtils instance which contains validation functions.
        self.__awu = AnalyticsWrapperUtils()
        self.__aed_utils = AedUtils()
        
        # Create argument information matrix to do parameter checking
        self.__arg_info_matrix = []
        self.__arg_info_matrix.append(["data", self.data, False, (DataFrame)])
        self.__arg_info_matrix.append(["data_order_column", self.data_order_column, True, (str,list)])
        self.__arg_info_matrix.append(["unpivot", self.unpivot, False, (str,list)])
        self.__arg_info_matrix.append(["input_types", self.input_types, True, (bool)])
        self.__arg_info_matrix.append(["attribute_column", self.attribute_column, True, (str)])
        self.__arg_info_matrix.append(["value_column", self.value_column, True, (str)])
        self.__arg_info_matrix.append(["accumulate", self.accumulate, False, (str,list)])
        self.__arg_info_matrix.append(["data_sequence_column", self.data_sequence_column, True, (str,list)])
        
        if inspect.stack()[1][3] != '_from_model_manager':
            # Perform the function validations
            self.__validate()
            # Generate the ML query
            self.__form_tdml_query()
            # Execute ML query
            self.__execute()
        
    def __validate(self):
        """
        Function to validate sqlmr function arguments, which verifies missing 
        arguments, input argument and table types. Also processes the 
        argument values.
        """
        
        # Make sure that a non-NULL value has been supplied for all mandatory arguments
        self.__awu._validate_missing_required_arguments(self.__arg_info_matrix)
        
        # Make sure that a non-NULL value has been supplied correct type of argument
        self.__awu._validate_argument_types(self.__arg_info_matrix)
        
        # Check to make sure input table types are strings or data frame objects or of valid type.
        self.__awu._validate_input_table_datatype(self.data, "data", None)
        
        # Check whether the input columns passed to the argument are not empty.
        # Also check whether the input columns passed to the argument valid or not.
        self.__awu._validate_input_columns_not_empty(self.unpivot, "unpivot")
        self.__awu._validate_dataframe_has_argument_columns(self.unpivot, "unpivot", self.data, "data", False)
        
        self.__awu._validate_input_columns_not_empty(self.accumulate, "accumulate")
        self.__awu._validate_dataframe_has_argument_columns(self.accumulate, "accumulate", self.data, "data", False)
        
        self.__awu._validate_input_columns_not_empty(self.data_sequence_column, "data_sequence_column")
        self.__awu._validate_dataframe_has_argument_columns(self.data_sequence_column, "data_sequence_column", self.data, "data", False)
        
        self.__awu._validate_input_columns_not_empty(self.data_order_column, "data_order_column")
        self.__awu._validate_dataframe_has_argument_columns(self.data_order_column, "data_order_column", self.data, "data", False)
        
        # Validate that value passed to the output column argument is not empty.
        self.__awu._validate_input_columns_not_empty(self.attribute_column, "attribute_column")
        self.__awu._validate_input_columns_not_empty(self.value_column, "value_column")
        
    def __form_tdml_query(self):
        """
        Function to generate the analytical function queries. The function defines 
        variables and list of arguments required to form the query.
        """
        
        # Output table arguments list
        self.__func_output_args_sql_names = []
        self.__func_output_args = []
        
        # Generate lists for rest of the function arguments
        self.__func_other_arg_sql_names = []
        self.__func_other_args = []
        self.__func_other_arg_json_datatypes = []
        
        self.__func_other_arg_sql_names.append("TargetColumns")
        self.__func_other_args.append(UtilFuncs._teradata_collapse_arglist(UtilFuncs._teradata_quote_arg(self.unpivot,"\""),"'"))
        self.__func_other_arg_json_datatypes.append("COLUMNS")
        
        self.__func_other_arg_sql_names.append("Accumulate")
        self.__func_other_args.append(UtilFuncs._teradata_collapse_arglist(UtilFuncs._teradata_quote_arg(self.accumulate,"\""),"'"))
        self.__func_other_arg_json_datatypes.append("COLUMNS")
        
        if self.input_types is not None and self.input_types != False:
            self.__func_other_arg_sql_names.append("InputTypes")
            self.__func_other_args.append(UtilFuncs._teradata_collapse_arglist(self.input_types,"'"))
            self.__func_other_arg_json_datatypes.append("BOOLEAN")
        
        if self.attribute_column is not None and self.attribute_column != "attribute":
            self.__func_other_arg_sql_names.append("AttributeColumn")
            self.__func_other_args.append(UtilFuncs._teradata_collapse_arglist(self.attribute_column,"'"))
            self.__func_other_arg_json_datatypes.append("STRING")
        
        if self.value_column is not None and self.value_column != "value_col":
            self.__func_other_arg_sql_names.append("ValueColumn")
            self.__func_other_args.append(UtilFuncs._teradata_collapse_arglist(self.value_column,"'"))
            self.__func_other_arg_json_datatypes.append("STRING")
        
        # Generate lists for rest of the function arguments
        sequence_input_by_list = []
        if self.data_sequence_column is not None:
            sequence_input_by_list.append("input:" + UtilFuncs._teradata_collapse_arglist(self.data_sequence_column,""))
        
        if len(sequence_input_by_list) > 0:
            self.__func_other_arg_sql_names.append("SequenceInputBy")
            self.__func_other_args.append(UtilFuncs._teradata_collapse_arglist(sequence_input_by_list,"'"))
            self.__func_other_arg_json_datatypes.append("STRING")
        
        
        # Declare empty lists to hold input table information.
        self.__func_input_arg_sql_names = []
        self.__func_input_table_view_query = []
        self.__func_input_dataframe_type = []
        self.__func_input_distribution = []
        self.__func_input_partition_by_cols = []
        self.__func_input_order_by_cols = []
        
        # Process data
        self.__table_ref = self.__awu._teradata_on_clause_from_dataframe(self.data, False)
        self.__func_input_distribution.append("FACT")
        self.__func_input_arg_sql_names.append("input")
        self.__func_input_table_view_query.append(self.__table_ref["ref"])
        self.__func_input_dataframe_type.append(self.__table_ref["ref_type"])
        self.__func_input_partition_by_cols.append("ANY")
        self.__func_input_order_by_cols.append(UtilFuncs._teradata_collapse_arglist(self.data_order_column,"\""))
        
        function_name = "Unpivoting"
        # Create instance to generate SQLMR.
        aqg_obj = AnalyticQueryGenerator(function_name 
                ,self.__func_input_arg_sql_names 
                ,self.__func_input_table_view_query 
                ,self.__func_input_dataframe_type 
                ,self.__func_input_distribution 
                ,self.__func_input_partition_by_cols 
                ,self.__func_input_order_by_cols 
                ,self.__func_other_arg_sql_names 
                ,self.__func_other_args 
                ,self.__func_other_arg_json_datatypes 
                ,self.__func_output_args_sql_names 
                ,self.__func_output_args 
                ,engine = "ENGINE_ML")
        # Invoke call to SQL-MR generation.
        self.sqlmr_query = aqg_obj._gen_sqlmr_select_stmt_sql()
        
        # Print SQL-MR query if requested to do so.
        if display.print_sqlmr_query:
            print(self.sqlmr_query)
        
    def __execute(self):
        """
        Function to execute SQL-MR queries. 
        Create DataFrames for the required SQL-MR outputs.
        """
        # Generate STDOUT table name and add it to the output table list.
        sqlmr_stdout_temp_tablename = UtilFuncs._generate_temp_table_name(prefix = "td_sqlmr_out_", use_default_database = True, gc_on_quit = True, quote=False)
        try:
            UtilFuncs._create_view(sqlmr_stdout_temp_tablename, self.sqlmr_query)
        except Exception as emsg:
            raise TeradataMlException(Messages.get_message(MessageCodes.TDMLDF_EXEC_SQL_FAILED, str(emsg)), MessageCodes.TDMLDF_EXEC_SQL_FAILED)
        
        # Update output table data frames.
        self._mlresults = []
        self.result = self.__awu._create_data_set_object(df_input=UtilFuncs._extract_table_name(sqlmr_stdout_temp_tablename), source_type="table", database_name=UtilFuncs._extract_db_name(sqlmr_stdout_temp_tablename))
        self._mlresults.append(self.result)
        
    @classmethod
    def _from_model_manager(cls,
        result = None,
        **kwargs):
        """
        Classmethod which will be used by Model Manager, to instantiate this wrapper class.
        """
        kwargs.pop("result", None)
        
        # Let's create an object of this class.
        obj = cls(**kwargs)
        obj.result  = result 
        
        # Update output table data frames.
        obj._mlresults = []
        obj.result = obj.__awu._create_data_set_object(df_input=UtilFuncs._extract_table_name(obj.result), source_type="table", database_name=UtilFuncs._extract_db_name(obj.result))
        obj._mlresults.append(obj.result)
        return obj
        
    def __repr__(self):
        """
        Returns the string representation for a Unpivot class instance.
        """
        repr_string="############ STDOUT Output ############"
        repr_string = "{}\n\n{}".format(repr_string,self.result)
        return repr_string
        
