#!/usr/bin/python
# ################################################################## 
# 
# Copyright 2018 Teradata. All rights reserved.
# TERADATA CONFIDENTIAL AND TRADE SECRET
# 
# Primary Owner: N Bhavana (bhavana.n@teradata.com)
# Secondary Owner: Pankaj Purandare (pankajvinod.purandare@teradata.com)
# 
# Version: 1.2
# Function Version: 2.1
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

class KNN:
    
    def __init__(self,
        train = None,
        test = None,
        k = None,
        response_column = None,
        id_column = None,
        distance_features = None,
        voting_weight = 0.0,
        customized_distance = None,
        force_mapreduce = False,
        parblock_size = None,
        partition_key = None,
        accumulate = None,
        output_prob = False,
        train_sequence_column = None,
        test_sequence_column = None):
        """
        DESCRIPTION:
            The KNN function uses training data objects to map test data objects 
            to categories. The function is optimized for both small and large 
            training sets. The function supports user-defined distance metrics 
            and distance-weighted voting.
        
        
        PARAMETERS:
            train:
                Required Argument.
                Specifies the name of the teradataml DataFrame that contains the 
                training data. Each row represents a classified data object.
            
            test:
                Required Argument.
                Specifies the name of the teradataml DataFrame that contains the test 
                data to be classified by the KNN algorithm. Each row represents a
                test data object.

            k:
                Required Argument.
                Specifies the number of nearest neighbors to use for classifying the
                test data.
                Types: int

            response_column:
                Required Argument.
                Specifies the name of the training teradataml DataFrame column that
                contains the class label or classification of the classified data
                objects.
                Types: str

            id_column:
                Required Argument.
                Specifies the name of the testing teradataml DataFrame column that
                uniquely identifies a data object.
                Types: str

            distance_features:
                Required Argument.
                Specifies the names of the training teradataml DataFrame columns that
                the function uses to compute the distance between a test object and
                the training objects. The test teradataml DataFrame must also have
                these columns.
                Types: str OR list of Strings (str)

            voting_weight:
                Optional Argument.
                Specifies the voting weight of the distance between a test object and
                the training objects. The voting_weight must be a nonnegative
                integer. The function calculates distance-weighted voting, w, with this
                equation: w = 1/POWER(distance, voting_weight) Where distance is the distance
                between the test object and the training object.
                Default Value: 0.0
                Types: float

            customized_distance:
                Optional Argument.
                This argument is currently not supported.

            force_mapreduce:
                Optional Argument.
                Specifies whether to partition the training data. which causes the
                KNN function to load all training data into memory and use only
                the row function. If you specify True, the KNN function
                partitions the training data and uses the map-and reduce function.
                Default Value: False
                Types: bool

            parblock_size:
                Optional Argument.
                Specifies the partition block size to use with force_mapreduce
                (True). The recommended value depends on training data size and
                number of vworkers.
                For example, if your training data size is 10 billion and you have 10 vworkers,
                the recommended, partition_block_size is 1/n billion, where n is an integer that
                corresponds to your vworker nodes memory. Omitting this argument or
                specifying an inappropriate partition_block_size can degrade
                performance.
                Types: int

            partition_key:
                Optional Argument.
                Specifies the name of the training teradataml DataFrame column that
                partition data in parallel model. The default value is the first
                column of distance_features.
                Note: “partition_key” argument support is only available when teradataml
                      is connected to Vantage 1.0 Maintenance Update 2 version or later.
                Types: str

            accumulate:
                Optional Argument.
                Specifies the names of test teradataml DataFrame columns to copy to
                the output teradataml DataFrame.
                Note: “accumulate” argument support is only available when teradataml
                      is connected to Vantage 1.1 or later.
                Types: str OR list of Strings (str)

            output_prob:
                Optional Argument.
                Specifies whether to display output probability for the predicted
                category.
                Note: “output_prob” argument support is only available when teradataml
                      is connected to Vantage 1.1 or later.
                Default Value: False
                Types: bool

            train_sequence_column:
                Optional Argument.
                Specifies the list of column(s) that uniquely identifies each row of
                the input argument "train". The argument is used to ensure
                deterministic results for functions which produce results that vary
                from run to run.
                Types: str OR list of Strings (str)

            test_sequence_column:
                Optional Argument.
                Specifies the list of column(s) that uniquely identifies each row of
                the input argument "test". The argument is used to ensure
                deterministic results for functions which produce results that vary
                from run to run.
                Types: str OR list of Strings (str)

        RETURNS:
            Instance of KNN.
            Output teradataml DataFrames can be accessed using attribute
            references, such as KNNObj.<attribute_name>.
            Output teradataml DataFrame attribute name is:
                1. output_table
                2. output


        RAISES:
            TeradataMlException

        EXAMPLES:

            # Load the data to run the example
            load_example_data("knn", ["computers_train1_clustered","computers_test1"])

            # Create teradataml DataFrame objects.
            # The "computers_train1_clustered" and "computers_test1" remote tables
            # contains five attributes of personal computers price, speed, hard disk
            # size, RAM, and screen size.
            computers_train1_clustered = DataFrame.from_table("computers_train1_clustered")
            computers_test1 = DataFrame.from_table("computers_test1")

            # Example 1 - Map the test computer data to their respective categories
            knn_out = KNN(train = computers_train1_clustered,
                         test = computers_test1,
                         k = 50,
                         response_column = "computer_category",
                         id_column = "id",
                         distance_features = ["price","speed","hd","ram","screen"],
                         voting_weight = 1.0
                         )
            # Print the result DataFrame
            print(knn_out)
        """
        self.train  = train 
        self.test  = test 
        self.k  = k 
        self.response_column  = response_column 
        self.id_column  = id_column 
        self.distance_features  = distance_features 
        self.voting_weight  = voting_weight 
        self.customized_distance  = customized_distance 
        self.force_mapreduce  = force_mapreduce 
        self.parblock_size  = parblock_size 
        self.partition_key  = partition_key 
        self.accumulate  = accumulate 
        self.output_prob  = output_prob 
        self.train_sequence_column  = train_sequence_column 
        self.test_sequence_column  = test_sequence_column 
        
        # Create TeradataPyWrapperUtils instance which contains validation functions.
        self.__awu = AnalyticsWrapperUtils()
        self.__aed_utils = AedUtils()
        
        # Create argument information matrix to do parameter checking
        self.__arg_info_matrix = []
        self.__arg_info_matrix.append(["train", self.train, False, (DataFrame)])
        self.__arg_info_matrix.append(["test", self.test, False, (DataFrame)])
        self.__arg_info_matrix.append(["k", self.k, False, (int)])
        self.__arg_info_matrix.append(["response_column", self.response_column, False, (str)])
        self.__arg_info_matrix.append(["id_column", self.id_column, False, (str)])
        self.__arg_info_matrix.append(["distance_features", self.distance_features, False, (str,list)])
        self.__arg_info_matrix.append(["voting_weight", self.voting_weight, True, (float)])
        self.__arg_info_matrix.append(["customized_distance", self.customized_distance, True, (str,list)])
        self.__arg_info_matrix.append(["force_mapreduce", self.force_mapreduce, True, (bool)])
        self.__arg_info_matrix.append(["parblock_size", self.parblock_size, True, (int)])
        self.__arg_info_matrix.append(["partition_key", self.partition_key, True, (str)])
        self.__arg_info_matrix.append(["accumulate", self.accumulate, True, (str,list)])
        self.__arg_info_matrix.append(["output_prob", self.output_prob, True, (bool)])
        self.__arg_info_matrix.append(["train_sequence_column", self.train_sequence_column, True, (str,list)])
        self.__arg_info_matrix.append(["test_sequence_column", self.test_sequence_column, True, (str,list)])
        
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
        # Check whether customized_distance argument is present.
        # If present throw error
        # This check is valid till support is provided in R and Python.
        if self.customized_distance:
            raise TeradataMlException(
                Messages.get_message(MessageCodes.UNSUPPORTED_ARGUMENT, "customized_distance", "customized_distance"),
                MessageCodes.UNSUPPORTED_ARGUMENT)

        # Make sure that a non-NULL value has been supplied for all mandatory arguments
        self.__awu._validate_missing_required_arguments(self.__arg_info_matrix)
        
        # Make sure that a non-NULL value has been supplied correct type of argument
        self.__awu._validate_argument_types(self.__arg_info_matrix)
        
        # Check to make sure input table types are strings or data frame objects or of valid type.
        self.__awu._validate_input_table_datatype(self.train, "train", None)
        self.__awu._validate_input_table_datatype(self.test, "test", None)
        
        # Check whether the input columns passed to the argument are not empty.
        # Also check whether the input columns passed to the argument valid or not.
        self.__awu._validate_input_columns_not_empty(self.response_column, "response_column")
        self.__awu._validate_dataframe_has_argument_columns(self.response_column, "response_column", self.train, "train", False)
        
        self.__awu._validate_input_columns_not_empty(self.id_column, "id_column")
        self.__awu._validate_dataframe_has_argument_columns(self.id_column, "id_column", self.test, "test", False)
        
        self.__awu._validate_input_columns_not_empty(self.distance_features, "distance_features")
        self.__awu._validate_dataframe_has_argument_columns(self.distance_features, "distance_features", self.train, "train", False)
        
        self.__awu._validate_input_columns_not_empty(self.partition_key, "partition_key")
        self.__awu._validate_dataframe_has_argument_columns(self.partition_key, "partition_key", self.train, "train", False)
        
        self.__awu._validate_input_columns_not_empty(self.accumulate, "accumulate")
        self.__awu._validate_dataframe_has_argument_columns(self.accumulate, "accumulate", self.test, "test", False)
        
        self.__awu._validate_input_columns_not_empty(self.train_sequence_column, "train_sequence_column")
        self.__awu._validate_dataframe_has_argument_columns(self.train_sequence_column, "train_sequence_column", self.train, "train", False)
        
        self.__awu._validate_input_columns_not_empty(self.test_sequence_column, "test_sequence_column")
        self.__awu._validate_dataframe_has_argument_columns(self.test_sequence_column, "test_sequence_column", self.test, "test", False)
        
        
    def __form_tdml_query(self):
        """
        Function to generate the analytical function queries. The function defines 
        variables and list of arguments required to form the query.
        """
        # Generate temp table names for output table parameters if any.
        self.__output_table_temp_tablename = UtilFuncs._generate_temp_table_name(prefix = "td_knn0", use_default_database = True, gc_on_quit = True, quote=False, table_type = TeradataConstants.TERADATA_TABLE)
        
        # Output table arguments list
        self.__func_output_args_sql_names = ["OutputTable"]
        self.__func_output_args = [self.__output_table_temp_tablename]
        
        # Generate lists for rest of the function arguments
        self.__func_other_arg_sql_names = []
        self.__func_other_args = []
        self.__func_other_arg_json_datatypes = []
        
        self.__func_other_arg_sql_names.append("ResponseColumn")
        self.__func_other_args.append(UtilFuncs._teradata_collapse_arglist(UtilFuncs._teradata_quote_arg(self.response_column,"\""),"'"))
        self.__func_other_arg_json_datatypes.append("COLUMN_NAMES")
        
        self.__func_other_arg_sql_names.append("IdColumn")
        self.__func_other_args.append(UtilFuncs._teradata_collapse_arglist(UtilFuncs._teradata_quote_arg(self.id_column,"\""),"'"))
        self.__func_other_arg_json_datatypes.append("COLUMN_NAMES")
        
        self.__func_other_arg_sql_names.append("DistanceFeatures")
        self.__func_other_args.append(UtilFuncs._teradata_collapse_arglist(UtilFuncs._teradata_quote_arg(self.distance_features,"\""),"'"))
        self.__func_other_arg_json_datatypes.append("COLUMN_NAMES")
        
        if self.partition_key is not None:
            self.__func_other_arg_sql_names.append("PartitionColumn")
            self.__func_other_args.append(UtilFuncs._teradata_collapse_arglist(UtilFuncs._teradata_quote_arg(self.partition_key,"\""),"'"))
            self.__func_other_arg_json_datatypes.append("COLUMN_NAMES")
        
        if self.accumulate is not None:
            self.__func_other_arg_sql_names.append("Accumulate")
            self.__func_other_args.append(UtilFuncs._teradata_collapse_arglist(UtilFuncs._teradata_quote_arg(self.accumulate,"\""),"'"))
            self.__func_other_arg_json_datatypes.append("COLUMN_NAMES")
        
        self.__func_other_arg_sql_names.append("K")
        self.__func_other_args.append(UtilFuncs._teradata_collapse_arglist(self.k,"'"))
        self.__func_other_arg_json_datatypes.append("INTEGER")
        
        if self.parblock_size is not None:
            self.__func_other_arg_sql_names.append("PartitionBlockSize")
            self.__func_other_args.append(UtilFuncs._teradata_collapse_arglist(self.parblock_size,"'"))
            self.__func_other_arg_json_datatypes.append("INTEGER")
        
        if self.force_mapreduce is not None and self.force_mapreduce != False:
            self.__func_other_arg_sql_names.append("ForceMapreduce")
            self.__func_other_args.append(UtilFuncs._teradata_collapse_arglist(self.force_mapreduce,"'"))
            self.__func_other_arg_json_datatypes.append("BOOLEAN")
        
        if self.customized_distance is not None:
            self.__func_other_arg_sql_names.append("CustomizedDistance")
            self.__func_other_args.append(UtilFuncs._teradata_collapse_arglist(self.customized_distance,"'"))
            self.__func_other_arg_json_datatypes.append("STRING")
        
        if self.voting_weight is not None and self.voting_weight != 0:
            self.__func_other_arg_sql_names.append("VotingWeight")
            self.__func_other_args.append(UtilFuncs._teradata_collapse_arglist(self.voting_weight,"'"))
            self.__func_other_arg_json_datatypes.append("DOUBLE")
        
        if self.output_prob is not None and self.output_prob != False:
            self.__func_other_arg_sql_names.append("OutputProb")
            self.__func_other_args.append(UtilFuncs._teradata_collapse_arglist(self.output_prob,"'"))
            self.__func_other_arg_json_datatypes.append("BOOLEAN")
        
        # Generate lists for rest of the function arguments
        sequence_input_by_list = []
        if self.train_sequence_column is not None:
            sequence_input_by_list.append("TrainingTable:" + UtilFuncs._teradata_collapse_arglist(self.train_sequence_column,""))
        
        if self.test_sequence_column is not None:
            sequence_input_by_list.append("TestTable:" + UtilFuncs._teradata_collapse_arglist(self.test_sequence_column,""))
        
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
        
        # Process train
        self.__table_ref = self.__awu._teradata_on_clause_from_dataframe(self.train, False)
        self.__func_input_distribution.append("NONE")
        self.__func_input_arg_sql_names.append("TrainingTable")
        self.__func_input_table_view_query.append(self.__table_ref["ref"])
        self.__func_input_dataframe_type.append(self.__table_ref["ref_type"])
        self.__func_input_partition_by_cols.append("NA_character_")
        self.__func_input_order_by_cols.append("NA_character_")
        
        # Process test
        self.__table_ref = self.__awu._teradata_on_clause_from_dataframe(self.test, False)
        self.__func_input_distribution.append("NONE")
        self.__func_input_arg_sql_names.append("TestTable")
        self.__func_input_table_view_query.append(self.__table_ref["ref"])
        self.__func_input_dataframe_type.append(self.__table_ref["ref_type"])
        self.__func_input_partition_by_cols.append("NA_character_")
        self.__func_input_order_by_cols.append("NA_character_")
        
        function_name = "KNN"
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
        self.output_table = self.__awu._create_data_set_object(df_input=UtilFuncs._extract_table_name(self.__output_table_temp_tablename), source_type="table", database_name=UtilFuncs._extract_db_name(self.__output_table_temp_tablename))
        self.output = self.__awu._create_data_set_object(df_input=UtilFuncs._extract_table_name(sqlmr_stdout_temp_tablename), source_type="table", database_name=UtilFuncs._extract_db_name(sqlmr_stdout_temp_tablename))
        self._mlresults.append(self.output_table)
        self._mlresults.append(self.output)
        
    @classmethod
    def _from_model_manager(cls,
        output_table = None,
        output = None,
        **kwargs):
        """
        Classmethod which will be used by Model Manager, to instantiate this wrapper class.
        """
        kwargs.pop("output_table", None)
        kwargs.pop("output", None)
        
        # Let's create an object of this class.
        obj = cls(**kwargs)
        obj.output_table  = output_table 
        obj.output  = output 
        
        # Update output table data frames.
        obj._mlresults = []
        obj.output_table = obj.__awu._create_data_set_object(df_input=UtilFuncs._extract_table_name(obj.output_table), source_type="table", database_name=UtilFuncs._extract_db_name(obj.output_table))
        obj.output = obj.__awu._create_data_set_object(df_input=UtilFuncs._extract_table_name(obj.output), source_type="table", database_name=UtilFuncs._extract_db_name(obj.output))
        obj._mlresults.append(obj.output_table)
        obj._mlresults.append(obj.output)
        return obj
        
    def __repr__(self):
        """
        Returns the string representation for a KNN class instance.
        """
        repr_string="############ STDOUT Output ############"
        repr_string = "{}\n\n{}".format(repr_string,self.output)
        repr_string="{}\n\n\n############ output_table Output ############".format(repr_string)
        repr_string = "{}\n\n{}".format(repr_string,self.output_table)
        return repr_string
        
