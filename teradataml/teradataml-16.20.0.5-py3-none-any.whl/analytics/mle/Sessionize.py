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

class Sessionize:
    
    def __init__(self,
        data = None,
        time_column = None,
        time_out = None,
        click_lag = None,
        emit_null = False,
        data_sequence_column = None,
        data_partition_column = None,
        data_order_column = None):
        """
        DESCRIPTION:
            The Sessionize function maps each click in a session to a unique
            session identifier. A session is defined as a sequence of clicks by
            one user that are separated by at most n seconds.

            The function is useful both for sessionization and for detecting web
            crawler (bot) activity. It is typically used to understand user browsing
            behavior on a web site.

            Note: This function is available only when teradataml is connected to
                  Vantage 1.1 or later versions.

        PARAMETERS:
            data:
                Required Argument.
                Specifies the input teradataml DataFrame.

            data_partition_column:
                Required Argument.
                Specifies Partition By columns for data.
                Values to this argument can be provided as a list, if multiple columns
                are used for partition.
                Types: str OR list of Strings (str)

            data_order_column:
                Required Argument.
                Specifies Order By columns for data.
                Values to this argument can be provided as a list, if multiple columns
                are used for ordering.
                Types: str OR list of Strings (str)

            time_column:
                Required Argument.
                Specifies the name of the input column that contains the click
                times.
                Note: The time_column must also be an data_order_column.
                Types: str

            time_out:
                Required Argument.
                Specifies the number of seconds at which the session times out.
                If time_out seconds elapse after a click, then the next click
                starts a new session.
                Types: float

            click_lag:
                Optional Argument.
                Specifies the minimum number of seconds between clicks for the
                session user to be considered human. If clicks are more frequent,
                indicating that the user is a "bot," the function ignores the
                session. The click_lag must be less than time_out.
                Types: float

            emit_null:
                Optional Argument.
                Specifies whether to output rows that have None values in their
                session id and rapid fire columns, even if their time_column
                has a None value.
                Default Value: False
                Types: bool

            data_sequence_column:
                Optional Argument.
                Specifies the list of column(s) that uniquely identifies each row of
                the input argument "data". The argument is used to ensure
                deterministic results for functions which produce results that vary
                from run to run.
                Types: str OR list of Strings (str)

        RETURNS:
            Instance of Sessionize.
            Output teradataml DataFrames can be accessed using attribute
            references, such as SessionizeObj.<attribute_name>.
            Output teradataml DataFrame attribute name is:
                result


        RAISES:
            TeradataMlException


        EXAMPLES:
            # Load the data to run the example.
            load_example_data("Sessionize","sessionize_table")

            # Create teradataml DataFram object.
            sessionize_table = DataFrame.from_table("sessionize_table")

            # Example 1 - This example maps each click in a session to a unique session identifer,
            # which uses input table web clickstream data recorded as user navigates through a web site
            # based on events — view, click, and so on which are recorded with a timestamp.
            sessionize_out = Sessionize(data = sessionize_table,
                                           data_partition_column = ["partition_id"],
                                           data_order_column = ["clicktime"],
                                           time_column = "clicktime",
                                           time_out = 60.0,
                                           click_lag = 0.2
                                           )

            # Print the result DataFrame
            print(sessionize_out.result)
        
        """
        self.data  = data 
        self.time_column  = time_column 
        self.time_out  = time_out 
        self.click_lag  = click_lag 
        self.emit_null  = emit_null 
        self.data_sequence_column  = data_sequence_column 
        self.data_partition_column  = data_partition_column 
        self.data_order_column  = data_order_column 
        
        # Create TeradataPyWrapperUtils instance which contains validation functions.
        self.__awu = AnalyticsWrapperUtils()
        self.__aed_utils = AedUtils()
        
        # Create argument information matrix to do parameter checking
        self.__arg_info_matrix = []
        self.__arg_info_matrix.append(["data", self.data, False, (DataFrame)])
        self.__arg_info_matrix.append(["data_partition_column", self.data_partition_column, False, (str,list)])
        self.__arg_info_matrix.append(["data_order_column", self.data_order_column, False, (str,list)])
        self.__arg_info_matrix.append(["time_column", self.time_column, False, (str)])
        self.__arg_info_matrix.append(["time_out", self.time_out, False, (float)])
        self.__arg_info_matrix.append(["click_lag", self.click_lag, True, (float)])
        self.__arg_info_matrix.append(["emit_null", self.emit_null, True, (bool)])
        self.__arg_info_matrix.append(["data_sequence_column", self.data_sequence_column, True, (str,list)])
        
        if inspect.stack()[1][3] != '_from_model_manager':
            # Perform the function validations
            self.__validate()
            # Generate the ML query
            self.__form_tdml_query()
            # Process output table schema
            self.__process_output_column_info()
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
        self.__awu._validate_input_columns_not_empty(self.time_column, "time_column")
        self.__awu._validate_dataframe_has_argument_columns(self.time_column, "time_column", self.data, "data", False)
        
        self.__awu._validate_input_columns_not_empty(self.data_sequence_column, "data_sequence_column")
        self.__awu._validate_dataframe_has_argument_columns(self.data_sequence_column, "data_sequence_column", self.data, "data", False)
        
        self.__awu._validate_input_columns_not_empty(self.data_partition_column, "data_partition_column")
        self.__awu._validate_dataframe_has_argument_columns(self.data_partition_column, "data_partition_column", self.data, "data", False)
        
        self.__awu._validate_input_columns_not_empty(self.data_order_column, "data_order_column")
        self.__awu._validate_dataframe_has_argument_columns(self.data_order_column, "data_order_column", self.data, "data", False)
        
        
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
        
        self.__func_other_arg_sql_names.append("TimeColumn")
        self.__func_other_args.append(UtilFuncs._teradata_collapse_arglist(UtilFuncs._teradata_quote_arg(self.time_column,"\""),"'"))
        self.__func_other_arg_json_datatypes.append("COLUMNS")
        
        self.__func_other_arg_sql_names.append("TimeOut")
        self.__func_other_args.append(UtilFuncs._teradata_collapse_arglist(self.time_out,"'"))
        self.__func_other_arg_json_datatypes.append("DOUBLE")
        
        if self.click_lag is not None:
            self.__func_other_arg_sql_names.append("ClickLag")
            self.__func_other_args.append(UtilFuncs._teradata_collapse_arglist(self.click_lag,"'"))
            self.__func_other_arg_json_datatypes.append("DOUBLE")
        
        if self.emit_null is not None and self.emit_null != False:
            self.__func_other_arg_sql_names.append("EmitNull")
            self.__func_other_args.append(UtilFuncs._teradata_collapse_arglist(self.emit_null,"'"))
            self.__func_other_arg_json_datatypes.append("BOOLEAN")
        
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
        self.data_partition_column = UtilFuncs._teradata_collapse_arglist(self.data_partition_column,"\"")
        self.__table_ref = self.__awu._teradata_on_clause_from_dataframe(self.data)
        self.__func_input_distribution.append("FACT")
        self.__func_input_arg_sql_names.append("input")
        self.__func_input_table_view_query.append(self.__table_ref["ref"])
        self.__func_input_dataframe_type.append(self.__table_ref["ref_type"])
        self.__func_input_partition_by_cols.append(self.data_partition_column)
        self.__func_input_order_by_cols.append(UtilFuncs._teradata_collapse_arglist(self.data_order_column,"\""))
        
        function_name = "Sessionize"
        # Create instance to generate SQLMR.
        self.__aqg_obj = AnalyticQueryGenerator(function_name 
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
        self.sqlmr_query = self.__aqg_obj._gen_sqlmr_select_stmt_sql()
        
        # Print SQL-MR query if requested to do so.
        if display.print_sqlmr_query:
            print(self.sqlmr_query)
        
    def __execute(self):
        """
        Function to generate AED nodes for output tables.
        This makes a call aed_ml_query() and then output table dataframes are created.
        """
        # Create a list of input node ids contributing to a query.
        self.__input_nodeids = []
        self.__input_nodeids.append(self.data._nodeid)
        
        # Generate STDOUT table name and add it to the output table list.
        sqlmr_stdout_temp_tablename = UtilFuncs._generate_temp_table_name(prefix = "td_sqlmr_out_", use_default_database = True, gc_on_quit = True, quote=False)
        self.__func_output_args.insert(0, sqlmr_stdout_temp_tablename)
        try:
            # Call aed_ml_query and generate AED nodes.
            node_id_list = self.__aed_utils._aed_ml_query(self.__input_nodeids, self.sqlmr_query, self.__func_output_args, "Sessionize", self.__aqg_obj._multi_query_input_nodes)
        except Exception as emsg:
            raise TeradataMlException(Messages.get_message(MessageCodes.AED_EXEC_FAILED, str(emsg)), MessageCodes.AED_EXEC_FAILED)
        
        
        # Update output table data frames.
        self._mlresults = []
        self.result = self.__awu._create_data_set_object(df_input=node_id_list[0], metaexpr=UtilFuncs._get_metaexpr_using_columns(node_id_list[0], self.__stdout_column_info))
        self._mlresults.append(self.result)
        
    def __process_output_column_info(self):
        """ 
        Function to process the output schema for all the ouptut tables.
        This function generates list of column names and column types
        for each generated output tables, which can be used to create metaexpr.
        """
        # Collecting STDOUT output column information.
        stdout_column_info_name = []
        stdout_column_info_type = []
        for column_name, column_type in self.__awu._retrieve_column_info(df_input=self.data, parameter=None, columns=None):
            stdout_column_info_name.append(column_name)
            stdout_column_info_type.append(column_type)
            
        stdout_column_info_name.append("sessionid")
        stdout_column_info_type.append(self.__awu._get_json_to_sqlalchemy_mapping("integer"))

        if self.click_lag:
            stdout_column_info_name.append("clicklag")
            stdout_column_info_type.append(self.__awu._get_json_to_sqlalchemy_mapping("boolean"))
        
        self.__stdout_column_info = zip(stdout_column_info_name, stdout_column_info_type)
        
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
        Returns the string representation for a Sessionize class instance.
        """
        repr_string="############ STDOUT Output ############"
        repr_string = "{}\n\n{}".format(repr_string,self.result)
        return repr_string
        
