#!/usr/bin/python
# ################################################################## 
# 
# Copyright 2018 Teradata. All rights reserved.
# TERADATA CONFIDENTIAL AND TRADE SECRET
# 
# Primary Owner: Pankaj Purandare (pankajvinod.purandare@teradata.com)
# Secondary Owner: Mounika Kotha (mounika.kotha@teradata.com)
# 
# Version: 1.2
# Function Version: 2.0
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

class HMMSupervised:
    
    def __init__(self,
        vertices = None,
        model_key = None,
        sequence_key = None,
        observed_key = None,
        state_key = None,
        skip_key = None,
        batch_size = None,
        vertices_sequence_column = None,
        vertices_partition_column = None,
        vertices_order_column=None):
        """
        DESCRIPTION:
            The HMMSupervised function runs on the SQL-GR framework. The function 
            can produce multiple HMM models simultaneously, where each model is 
            learned from a set of sequences and where each sequence represents a 
            vertex.
        
        
        PARAMETERS:
            vertices:
                Required Argument.
                Specifies the teradataml DataFrame containing the vertex data.

            vertices_partition_column:
                Required Argument.
                Specifies Partition By columns for vertices.
                Values to this argument can be provided as list, if multiple columns
                are used for partition.
                Types: str OR list of Strings (str)

            vertices_order_column:
                Required Argument.
                Specifies Order By columns for vertices.
                Values to this argument can be provided as list, if multiple columns
                are used for ordering.
                Types: str OR list of Strings (str)

            model_key:
                Optional Argument.
                Specifies the name of the column that contains the model attribute. When
                specifying this argument, its value must match a model_key in the
                vertices_partition_column.
                Types: str OR list of Strings (str)

            sequence_key:
                Required Argument.
                Specifies the name of the column that contains the sequence attribute. The
                sequence_key must be a sequence attribute in the
                vertices_partition_column. A sequence must contain more than two
                observation symbols.
                Types: str OR list of Strings (str)

            observed_key:
                Required Argument.
                Specifies the name of the column that contains the observed symbols. The
                function scans the input teradataml DataFrame to find all possible
                observed symbols.
                Note: Observed symbols are case-sensitive.
                Types: str OR list of Strings (str)

            state_key:
                Required Argument.
                Specifies the column containing state attributes. You can specify multiple
                states. The states are case-sensitive.
                Types: str OR list of Strings (str)

            skip_key:
                Optional Argument.
                Specifies the name of the column whose values determine whether the function
                skips the row. The function skips the row if the value is "true",
                "yes", "y", or "1". The function does not skip the row if the value
                is "false", "f", "no", "n", "0", or NULL.
                Types: str OR list of Strings (str)

            batch_size:
                Optional Argument.
                Specifies the number of models to process. The size must be positive. If the
                batch size is not specified, the function avoids out-of-memory errors
                by determining the appropriate size. If the batch size is specified
                and there is insufficient free memory, the function reduces the batch
                size. The batch size is determined dynamically, based on the memory
                conditions. For example, at time T1, the specified batch size 1000
                might be adjusted to 980, and at time T2, the batch size might be
                adjusted to 800.
                Types: int

            vertices_sequence_column:
                Optional Argument.
                Specifies the list of column(s) that uniquely identifies each row of
                the input argument "vertices". The argument is used to ensure
                deterministic results for functions which produce results that vary
                from run to run.
                Types: str OR list of Strings (str)

        RETURNS:
            Instance of HMMSupervised.
            Output teradataml DataFrames can be accessed using attribute
            references, such as HMMSupervisedObj.<attribute_name>.
            Output teradataml DataFrame attribute names are:
                1. output_initialstate_table
                2. output_statetransition_table
                3. output_emission_table
                4. output


        RAISES:
            TeradataMlException


        EXAMPLES:
            # Load example data.
            load_example_data("hmmsupervised", "customer_loyalty")

            #
            # "customer_loyalty" dataset contains events that are related to customer transaction.
            # Each event comprises of the time elapsed since the last transaction and
            # the amount spent compared  amount spent in the last transaction
            #
            # Time elapsed since the last transaction:
            #       small(S), medium(M) and large(L)
            # and the amount spent compared  amount spent in the last transaction:
            #       less(L), about same(S) and more(M).
            #
            # So there are 9 possible combinations, resulting in 9 events.
            # For example, the event SM implies a transaction, where the time elapsed
            # since the last transaction is small and the customer spent more than last time.
            #
            # Datset also contains 3 hidden states corresponding to 3 levels of loyalty:
            #       low(L), normal(N), high(H).

            # Create teradataml DataFrame objects.
            customer_loyalty = DataFrame.from_table("customer_loyalty")

            # Example 1 - Train a HMM Supervised model on the customer loyalty dataset
            HMMSupervised_out = HMMSupervised(vertices = customer_loyalty,
                                              vertices_partition_column = ["user_id", "seq_id"],
                                              vertices_order_column = ["user_id", "seq_id", "purchase_date"],
                                              model_key = "user_id",
                                              sequence_key = "seq_id",
                                              observed_key = "observation",
                                              state_key = "loyalty_level"
                                              )

            # Print the results.
            print(HMMSupervised_out.output_initialstate_table)
            print(HMMSupervised_out.output_statetransition_table)
            print(HMMSupervised_out.output_emission_table)
            print(HMMSupervised_out.output)

        
        """
        self.vertices  = vertices 
        self.model_key  = model_key 
        self.sequence_key  = sequence_key 
        self.observed_key  = observed_key 
        self.state_key  = state_key 
        self.skip_key  = skip_key 
        self.batch_size  = batch_size 
        self.vertices_sequence_column  = vertices_sequence_column 
        self.vertices_partition_column  = vertices_partition_column
        self.vertices_order_column = vertices_order_column
        
        # Create TeradataPyWrapperUtils instance which contains validation functions.
        self.__awu = AnalyticsWrapperUtils()
        self.__aed_utils = AedUtils()
        
        # Create argument information matrix to do parameter checking
        self.__arg_info_matrix = []
        self.__arg_info_matrix.append(["vertices", self.vertices, False, (DataFrame)])
        self.__arg_info_matrix.append(["vertices_partition_column", self.vertices_partition_column, False, (str,list)])
        self.__arg_info_matrix.append(["vertices_order_column", self.vertices_order_column, False, (str, list)])
        self.__arg_info_matrix.append(["model_key", self.model_key, True, (str)])
        self.__arg_info_matrix.append(["sequence_key", self.sequence_key, False, (str)])
        self.__arg_info_matrix.append(["observed_key", self.observed_key, False, (str)])
        self.__arg_info_matrix.append(["state_key", self.state_key, False, (str)])
        self.__arg_info_matrix.append(["skip_key", self.skip_key, True, (str)])
        self.__arg_info_matrix.append(["batch_size", self.batch_size, True, (int)])
        self.__arg_info_matrix.append(["vertices_sequence_column", self.vertices_sequence_column, True, (str,list)])
        
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
        self.__awu._validate_input_table_datatype(self.vertices, "vertices", None)
        
        # Check whether the input columns passed to the argument are not empty.
        # Also check whether the input columns passed to the argument valid or not.
        self.__awu._validate_input_columns_not_empty(self.state_key, "state_key")
        self.__awu._validate_dataframe_has_argument_columns(self.state_key, "state_key", self.vertices, "vertices", False)
        
        self.__awu._validate_input_columns_not_empty(self.observed_key, "observed_key")
        self.__awu._validate_dataframe_has_argument_columns(self.observed_key, "observed_key", self.vertices, "vertices", False)
        
        self.__awu._validate_input_columns_not_empty(self.sequence_key, "sequence_key")
        self.__awu._validate_dataframe_has_argument_columns(self.sequence_key, "sequence_key", self.vertices, "vertices", False)
        
        self.__awu._validate_input_columns_not_empty(self.skip_key, "skip_key")
        self.__awu._validate_dataframe_has_argument_columns(self.skip_key, "skip_key", self.vertices, "vertices", False)
        
        self.__awu._validate_input_columns_not_empty(self.model_key, "model_key")
        self.__awu._validate_dataframe_has_argument_columns(self.model_key, "model_key", self.vertices, "vertices", False)
        
        self.__awu._validate_input_columns_not_empty(self.vertices_sequence_column, "vertices_sequence_column")
        self.__awu._validate_dataframe_has_argument_columns(self.vertices_sequence_column, "vertices_sequence_column", self.vertices, "vertices", False)
        
        self.__awu._validate_input_columns_not_empty(self.vertices_partition_column, "vertices_partition_column")
        self.__awu._validate_dataframe_has_argument_columns(self.vertices_partition_column, "vertices_partition_column", self.vertices, "vertices", False)

        self.__awu._validate_input_columns_not_empty(self.vertices_order_column, "vertices_order_column")
        self.__awu._validate_dataframe_has_argument_columns(self.vertices_order_column, "vertices_order_column", self.vertices, "vertices", False)
        
    def __form_tdml_query(self):
        """
        Function to generate the analytical function queries. The function defines 
        variables and list of arguments required to form the query.
        """
        # Generate temp table names for output table parameters if any.
        self.__output_initialstate_table_temp_tablename = UtilFuncs._generate_temp_table_name(prefix = "td_hmmsupervised0", use_default_database = True, gc_on_quit = True, quote=False, table_type = TeradataConstants.TERADATA_TABLE)
        self.__output_statetransition_table_temp_tablename = UtilFuncs._generate_temp_table_name(prefix = "td_hmmsupervised1", use_default_database = True, gc_on_quit = True, quote=False, table_type = TeradataConstants.TERADATA_TABLE)
        self.__output_emission_table_temp_tablename = UtilFuncs._generate_temp_table_name(prefix = "td_hmmsupervised2", use_default_database = True, gc_on_quit = True, quote=False, table_type = TeradataConstants.TERADATA_TABLE)
        
        # Output table arguments list
        self.__func_output_args_sql_names = ["InitStateTable", "StateTransitionTable", "EmissionTable"]
        self.__func_output_args = [self.__output_initialstate_table_temp_tablename, self.__output_statetransition_table_temp_tablename, self.__output_emission_table_temp_tablename]
        
        # Generate lists for rest of the function arguments
        self.__func_other_arg_sql_names = []
        self.__func_other_args = []
        self.__func_other_arg_json_datatypes = []
        
        self.__func_other_arg_sql_names.append("StateColumn")
        self.__func_other_args.append(UtilFuncs._teradata_collapse_arglist(UtilFuncs._teradata_quote_arg(self.state_key,"\""),"'"))
        self.__func_other_arg_json_datatypes.append("COLUMNS")
        
        self.__func_other_arg_sql_names.append("ObservationColumn")
        self.__func_other_args.append(UtilFuncs._teradata_collapse_arglist(UtilFuncs._teradata_quote_arg(self.observed_key,"\""),"'"))
        self.__func_other_arg_json_datatypes.append("COLUMNS")
        
        self.__func_other_arg_sql_names.append("SeqColumn")
        self.__func_other_args.append(UtilFuncs._teradata_collapse_arglist(UtilFuncs._teradata_quote_arg(self.sequence_key,"\""),"'"))
        self.__func_other_arg_json_datatypes.append("COLUMNS")
        
        if self.skip_key is not None:
            self.__func_other_arg_sql_names.append("SkipColumn")
            self.__func_other_args.append(UtilFuncs._teradata_collapse_arglist(UtilFuncs._teradata_quote_arg(self.skip_key,"\""),"'"))
            self.__func_other_arg_json_datatypes.append("COLUMNS")
        
        if self.model_key is not None:
            self.__func_other_arg_sql_names.append("ModelColumn")
            self.__func_other_args.append(UtilFuncs._teradata_collapse_arglist(UtilFuncs._teradata_quote_arg(self.model_key,"\""),"'"))
            self.__func_other_arg_json_datatypes.append("COLUMNS")
        
        if self.batch_size is not None:
            self.__func_other_arg_sql_names.append("BatchSize")
            self.__func_other_args.append(UtilFuncs._teradata_collapse_arglist(self.batch_size,"'"))
            self.__func_other_arg_json_datatypes.append("INTEGER")
        
        # Generate lists for rest of the function arguments
        sequence_input_by_list = []
        if self.vertices_sequence_column is not None:
            sequence_input_by_list.append("vertices:" + UtilFuncs._teradata_collapse_arglist(self.vertices_sequence_column,""))
        
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
        
        # Process vertices
        self.vertices_partition_column = UtilFuncs._teradata_collapse_arglist(self.vertices_partition_column,"\"")
        self.__table_ref = self.__awu._teradata_on_clause_from_dataframe(self.vertices, False)
        self.__func_input_distribution.append("FACT")
        self.__func_input_arg_sql_names.append("vertices")
        self.__func_input_table_view_query.append(self.__table_ref["ref"])
        self.__func_input_dataframe_type.append(self.__table_ref["ref_type"])
        self.__func_input_partition_by_cols.append(self.vertices_partition_column)
        self.__func_input_order_by_cols.append(UtilFuncs._teradata_collapse_arglist(self.vertices_order_column,"\""))
        
        function_name = "HMMSupervised"
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
        sqlmr_stdout_temp_tablename = UtilFuncs._generate_temp_table_name(prefix = "td_sqlmr_out_", use_default_database = True, gc_on_quit = True, quote=False, table_type = TeradataConstants.TERADATA_TABLE)
        try:
            UtilFuncs._create_table(sqlmr_stdout_temp_tablename, self.sqlmr_query)
        except Exception as emsg:
            raise TeradataMlException(Messages.get_message(MessageCodes.TDMLDF_EXEC_SQL_FAILED, str(emsg)), MessageCodes.TDMLDF_EXEC_SQL_FAILED)
        
        # Update output table data frames.
        self._mlresults = []
        self.output_initialstate_table = self.__awu._create_data_set_object(df_input=UtilFuncs._extract_table_name(self.__output_initialstate_table_temp_tablename), source_type="table", database_name=UtilFuncs._extract_db_name(self.__output_initialstate_table_temp_tablename))
        self.output_statetransition_table = self.__awu._create_data_set_object(df_input=UtilFuncs._extract_table_name(self.__output_statetransition_table_temp_tablename), source_type="table", database_name=UtilFuncs._extract_db_name(self.__output_statetransition_table_temp_tablename))
        self.output_emission_table = self.__awu._create_data_set_object(df_input=UtilFuncs._extract_table_name(self.__output_emission_table_temp_tablename), source_type="table", database_name=UtilFuncs._extract_db_name(self.__output_emission_table_temp_tablename))
        self.output = self.__awu._create_data_set_object(df_input=UtilFuncs._extract_table_name(sqlmr_stdout_temp_tablename), source_type="table", database_name=UtilFuncs._extract_db_name(sqlmr_stdout_temp_tablename))
        self._mlresults.append(self.output_initialstate_table)
        self._mlresults.append(self.output_statetransition_table)
        self._mlresults.append(self.output_emission_table)
        self._mlresults.append(self.output)
        
    @classmethod
    def _from_model_manager(cls,
        output_initialstate_table = None,
        output_statetransition_table = None,
        output_emission_table = None,
        output = None,
        **kwargs):
        """
        Classmethod which will be used by Model Manager, to instantiate this wrapper class.
        """
        kwargs.pop("output_initialstate_table", None)
        kwargs.pop("output_statetransition_table", None)
        kwargs.pop("output_emission_table", None)
        kwargs.pop("output", None)
        
        # Let's create an object of this class.
        obj = cls(**kwargs)
        obj.output_initialstate_table  = output_initialstate_table 
        obj.output_statetransition_table  = output_statetransition_table 
        obj.output_emission_table  = output_emission_table 
        obj.output  = output 
        
        # Update output table data frames.
        obj._mlresults = []
        obj.output_initialstate_table = obj.__awu._create_data_set_object(df_input=UtilFuncs._extract_table_name(obj.output_initialstate_table), source_type="table", database_name=UtilFuncs._extract_db_name(obj.output_initialstate_table))
        obj.output_statetransition_table = obj.__awu._create_data_set_object(df_input=UtilFuncs._extract_table_name(obj.output_statetransition_table), source_type="table", database_name=UtilFuncs._extract_db_name(obj.output_statetransition_table))
        obj.output_emission_table = obj.__awu._create_data_set_object(df_input=UtilFuncs._extract_table_name(obj.output_emission_table), source_type="table", database_name=UtilFuncs._extract_db_name(obj.output_emission_table))
        obj.output = obj.__awu._create_data_set_object(df_input=UtilFuncs._extract_table_name(obj.output), source_type="table", database_name=UtilFuncs._extract_db_name(obj.output))
        obj._mlresults.append(obj.output_initialstate_table)
        obj._mlresults.append(obj.output_statetransition_table)
        obj._mlresults.append(obj.output_emission_table)
        obj._mlresults.append(obj.output)
        return obj
        
    def __repr__(self):
        """
        Returns the string representation for a HMMSupervised class instance.
        """
        repr_string="############ STDOUT Output ############"
        repr_string = "{}\n\n{}".format(repr_string,self.output)
        repr_string="{}\n\n\n############ output_initialstate_table Output ############".format(repr_string)
        repr_string = "{}\n\n{}".format(repr_string,self.output_initialstate_table)
        repr_string="{}\n\n\n############ output_statetransition_table Output ############".format(repr_string)
        repr_string = "{}\n\n{}".format(repr_string,self.output_statetransition_table)
        repr_string="{}\n\n\n############ output_emission_table Output ############".format(repr_string)
        repr_string = "{}\n\n{}".format(repr_string,self.output_emission_table)
        return repr_string
        
