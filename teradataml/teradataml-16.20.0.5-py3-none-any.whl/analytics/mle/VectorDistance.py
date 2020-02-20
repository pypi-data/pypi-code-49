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
# Function Version: 1.3
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

class VectorDistance:
    
    def __init__(self,
        target_data = None,
        ref_data = None,
        target_id = None,
        target_feature = None,
        target_value = None,
        ref_id = None,
        ref_feature = None,
        ref_value = None,
        reftable_size = "small",
        distance_measure = "cosine",
        ignore_mismatch = True,
        replace_invalid = "positiveinfinity",
        top_k = 2147483647,
        max_distance = None,
        target_data_sequence_column = None,
        ref_data_sequence_column = None,
        target_data_partition_column = None,
        target_data_order_column = None,
        ref_data_order_column = None):
        """
        DESCRIPTION:
            The VectorDistance function takes a teradataml DataFrame of target
            vectors and a teradataml DataFrame of reference vectors and returns a
            teradataml DataFrame that contains the distance between each
            target-reference pair.


        PARAMETERS:
            target_data:
                Required Argument.
                Specifies a teradataml DataFrame that contains target vectors.

            target_data_partition_column:
                Required Argument.
                Specifies Partition By columns for target_data.
                Values to this argument can be provided as list, if multiple columns
                are used for partition.
                Types: str OR list of Strings (str)

            target_data_order_column:
                Optional Argument.
                Specifies Order By columns for target_data.
                Values to this argument can be provided as a list, if multiple
                columns are used for ordering.
                Types: str OR list of Strings (str)

            ref_data:
                Required Argument.
                Specifies a teradataml DataFrame that contains reference vectors.

            ref_data_order_column:
                Optional Argument.
                Specifies Order By columns for ref_data.
                Values to this argument can be provided as a list, if multiple
                columns are used for ordering.
                Types: str OR list of Strings (str)

            target_id:
                Required Argument.
                Specifies the names of the columns that comprise the target vector
                identifier. You must partition the target input teradataml DataFrame
                by these columns and specify them with this argument.
                Types: str OR list of Strings (str)

            target_feature:
                Required Argument.
                Specifies the name of the column that contains the target vector
                feature name (for example, the axis of a 3-D vector).
                Note: An entry with a NULL value in a feature_column is dropped.
                Types: str

            target_value:
                Optional Argument.
                Specifies the name of the column that contains the value for the
                target vector feature. The default value is 1.
                Note: An entry with a NULL value in a value_column is dropped.
                Types: str

            ref_id:
                Optional Argument.
                Specifies the names of the columns that comprise the reference vector
                identifier. The default value is the target_id argument value.
                Types: str OR list of Strings (str)

            ref_feature:
                Optional Argument.
                Specifies the name of the column that contains the reference vector
                feature name. The default value is the target_feature argument value.
                Types: str

            ref_value:
                Optional Argument.
                Specifies the name of the column that contains the value for the
                reference vector feature. The default value is the target_value
                argument value.
                Note: An entry with a NULL value in a value_column is dropped.
                Types: str

            reftable_size:
                Optional Argument.
                Specifies the size of the reference table. Specify "LARGE" only if
                the reference teradataml DataFrame does not fit in memory.
                Default Value: "small"
                Permitted Values: small, large
                Types: str

            distance_measure:
                Optional Argument.
                Specifies the distance measures that the function uses.
                Default Value: "cosine"
                Permitted Values: COSINE, EUCLIDEAN, MANHATTAN, BINARY
                Types: str OR list of Strings (str)

            ignore_mismatch:
                Optional Argument.
                Specifies whether to drop mismatched dimensions. If distance_measure
                is "cosine", then this argument is "False". If you specify "True",
                then two vectors with no common features become two empty vectors
                when only their common features are considered, and the function
                cannot measure the distance between them.
                Default Value: True
                Types: bool

            replace_invalid:
                Optional Argument.
                Specifies the value to return when the function encounters an
                infinite value or empty vectors. For custom, you can supply any float
                value.
                Default Value: "positiveinfinity"
                Types: str

            top_k:
                Optional Argument.
                Specifies, for each target vector and for each measure, the maximum
                number of closest reference vectors to include in the output table.
                For k, you can supply any integer value.
                Default Value: 2147483647
                Types: int

            max_distance:
                Optional Argument.
                Specifies the maximum distance between a pair of target and reference
                vectors. If the distance exceeds the threshold, the pair does not
                appear in the output table. If the distance_measure argument
                specifies multiple measures, then the max_distance argument must
                specify a threshold for each measure. The ith threshold corresponds
                to the ith measure. Each threshold can be any float value. If you
                omit this argument, then the function returns all results.
                Types: float OR list of Floats (float)

            target_data_sequence_column:
                Optional Argument.
                Specifies the list of column(s) that uniquely identifies each row of
                the input argument "target_data". The argument is used to ensure
                deterministic results for functions which produce results that vary
                from run to run.
                Types: str OR list of Strings (str)

            ref_data_sequence_column:
                Optional Argument.
                Specifies the list of column(s) that uniquely identifies each row of
                the input argument "ref_data". The argument is used to ensure
                deterministic results for functions which produce results that vary
                from run to run.
                Types: str OR list of Strings (str)

        RETURNS:
            Instance of VectorDistance.
            Output teradataml DataFrames can be accessed using attribute
            references, such as VectorDistanceObj.<attribute_name>.
            Output teradataml DataFrame attribute name is:
                result


        RAISES:
            TeradataMlException


        EXAMPLES:
            # Load example data.
            load_example_data("vectordistance", ["target_mobile_data", "ref_mobile_data"])

            # Create teradataml DataFrame objects.
            target_mobile_data = DataFrame.from_table("target_mobile_data")
            ref_mobile_data = DataFrame.from_table("ref_mobile_data")

            # Example 1 - Using the default ("cosine") distance measure with no threshold.
            VectorDistance_out1 = VectorDistance(target_data = target_mobile_data,
                                                target_data_partition_column = ["userid"],
                                                ref_data = ref_mobile_data,
                                                target_id = ["userid"],
                                                target_feature = "feature",
                                                target_value = "value1"
                                                )
            # Print the output data
            print(VectorDistance_out1)

            # Example 2 - Using three distance measures with corresponding thresholds (max.distance).
            VectorDistance_out2 = VectorDistance(target_data = target_mobile_data,
                                                target_data_partition_column = ["userid"],
                                                ref_data = ref_mobile_data,
                                                target_id = ["userid"],
                                                target_feature = "feature",
                                                target_value = "value1",
                                                distance_measure = ["Cosine","Euclidean","Manhattan"],
                                                max_distance = [0.03,0.8,1.0]
                                                )
            # Print the output data
            print(VectorDistance_out2)
        
        """
        self.target_data  = target_data 
        self.ref_data  = ref_data 
        self.target_id  = target_id 
        self.target_feature  = target_feature 
        self.target_value  = target_value 
        self.ref_id  = ref_id 
        self.ref_feature  = ref_feature 
        self.ref_value  = ref_value 
        self.reftable_size  = reftable_size 
        self.distance_measure  = distance_measure 
        self.ignore_mismatch  = ignore_mismatch 
        self.replace_invalid  = replace_invalid 
        self.top_k  = top_k 
        self.max_distance  = max_distance 
        self.target_data_sequence_column  = target_data_sequence_column 
        self.ref_data_sequence_column  = ref_data_sequence_column 
        self.target_data_partition_column  = target_data_partition_column 
        self.target_data_order_column  = target_data_order_column 
        self.ref_data_order_column  = ref_data_order_column 
        
        # Create TeradataPyWrapperUtils instance which contains validation functions.
        self.__awu = AnalyticsWrapperUtils()
        self.__aed_utils = AedUtils()
        
        # Create argument information matrix to do parameter checking
        self.__arg_info_matrix = []
        self.__arg_info_matrix.append(["target_data", self.target_data, False, (DataFrame)])
        self.__arg_info_matrix.append(["target_data_partition_column", self.target_data_partition_column, False, (str,list)])
        self.__arg_info_matrix.append(["target_data_order_column", self.target_data_order_column, True, (str,list)])
        self.__arg_info_matrix.append(["ref_data", self.ref_data, False, (DataFrame)])
        self.__arg_info_matrix.append(["ref_data_order_column", self.ref_data_order_column, True, (str,list)])
        self.__arg_info_matrix.append(["target_id", self.target_id, False, (str,list)])
        self.__arg_info_matrix.append(["target_feature", self.target_feature, False, (str)])
        self.__arg_info_matrix.append(["target_value", self.target_value, True, (str)])
        self.__arg_info_matrix.append(["ref_id", self.ref_id, True, (str,list)])
        self.__arg_info_matrix.append(["ref_feature", self.ref_feature, True, (str)])
        self.__arg_info_matrix.append(["ref_value", self.ref_value, True, (str)])
        self.__arg_info_matrix.append(["reftable_size", self.reftable_size, True, (str)])
        self.__arg_info_matrix.append(["distance_measure", self.distance_measure, True, (str,list)])
        self.__arg_info_matrix.append(["ignore_mismatch", self.ignore_mismatch, True, (bool)])
        self.__arg_info_matrix.append(["replace_invalid", self.replace_invalid, True, (str)])
        self.__arg_info_matrix.append(["top_k", self.top_k, True, (int)])
        self.__arg_info_matrix.append(["max_distance", self.max_distance, True, (float,list)])
        self.__arg_info_matrix.append(["target_data_sequence_column", self.target_data_sequence_column, True, (str,list)])
        self.__arg_info_matrix.append(["ref_data_sequence_column", self.ref_data_sequence_column, True, (str,list)])
        
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
        self.__awu._validate_input_table_datatype(self.target_data, "target_data", None)
        self.__awu._validate_input_table_datatype(self.ref_data, "ref_data", None)
        
        # Check for permitted values
        reftable_size_permitted_values = ["SMALL", "LARGE"]
        self.__awu._validate_permitted_values(self.reftable_size, reftable_size_permitted_values, "reftable_size")
        
        distance_measure_permitted_values = ["COSINE", "EUCLIDEAN", "MANHATTAN", "BINARY"]
        self.__awu._validate_permitted_values(self.distance_measure, distance_measure_permitted_values, "distance_measure")
        
        # Check whether the input columns passed to the argument are not empty.
        # Also check whether the input columns passed to the argument valid or not.
        self.__awu._validate_input_columns_not_empty(self.target_id, "target_id")
        self.__awu._validate_dataframe_has_argument_columns(self.target_id, "target_id", self.target_data, "target_data", False)
        
        self.__awu._validate_input_columns_not_empty(self.target_feature, "target_feature")
        self.__awu._validate_dataframe_has_argument_columns(self.target_feature, "target_feature", self.target_data, "target_data", False)
        
        self.__awu._validate_input_columns_not_empty(self.target_value, "target_value")
        self.__awu._validate_dataframe_has_argument_columns(self.target_value, "target_value", self.target_data, "target_data", False)
        
        self.__awu._validate_input_columns_not_empty(self.ref_id, "ref_id")
        self.__awu._validate_dataframe_has_argument_columns(self.ref_id, "ref_id", self.ref_data, "ref_data", False)
        
        self.__awu._validate_input_columns_not_empty(self.ref_feature, "ref_feature")
        self.__awu._validate_dataframe_has_argument_columns(self.ref_feature, "ref_feature", self.ref_data, "ref_data", False)
        
        self.__awu._validate_input_columns_not_empty(self.ref_value, "ref_value")
        self.__awu._validate_dataframe_has_argument_columns(self.ref_value, "ref_value", self.ref_data, "ref_data", False)
        
        self.__awu._validate_input_columns_not_empty(self.target_data_sequence_column, "target_data_sequence_column")
        self.__awu._validate_dataframe_has_argument_columns(self.target_data_sequence_column, "target_data_sequence_column", self.target_data, "target_data", False)
        
        self.__awu._validate_input_columns_not_empty(self.ref_data_sequence_column, "ref_data_sequence_column")
        self.__awu._validate_dataframe_has_argument_columns(self.ref_data_sequence_column, "ref_data_sequence_column", self.ref_data, "ref_data", False)
        
        self.__awu._validate_input_columns_not_empty(self.target_data_partition_column, "target_data_partition_column")
        self.__awu._validate_dataframe_has_argument_columns(self.target_data_partition_column, "target_data_partition_column", self.target_data, "target_data", False)
        
        self.__awu._validate_input_columns_not_empty(self.target_data_order_column, "target_data_order_column")
        self.__awu._validate_dataframe_has_argument_columns(self.target_data_order_column, "target_data_order_column", self.target_data, "target_data", False)
        
        self.__awu._validate_input_columns_not_empty(self.ref_data_order_column, "ref_data_order_column")
        self.__awu._validate_dataframe_has_argument_columns(self.ref_data_order_column, "ref_data_order_column", self.ref_data, "ref_data", False)
        
        
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
        
        self.__func_other_arg_sql_names.append("TargetIdColumns")
        self.__func_other_args.append(UtilFuncs._teradata_collapse_arglist(UtilFuncs._teradata_quote_arg(self.target_id,"\""),"'"))
        self.__func_other_arg_json_datatypes.append("COLUMNS")
        
        self.__func_other_arg_sql_names.append("TargetFeatureColumn")
        self.__func_other_args.append(UtilFuncs._teradata_collapse_arglist(UtilFuncs._teradata_quote_arg(self.target_feature,"\""),"'"))
        self.__func_other_arg_json_datatypes.append("COLUMNS")
        
        if self.target_value is not None:
            self.__func_other_arg_sql_names.append("TargetValueColumn")
            self.__func_other_args.append(UtilFuncs._teradata_collapse_arglist(UtilFuncs._teradata_quote_arg(self.target_value,"\""),"'"))
            self.__func_other_arg_json_datatypes.append("COLUMNS")
        
        if self.ref_id is not None:
            self.__func_other_arg_sql_names.append("RefIdColumns")
            self.__func_other_args.append(UtilFuncs._teradata_collapse_arglist(UtilFuncs._teradata_quote_arg(self.ref_id,"\""),"'"))
            self.__func_other_arg_json_datatypes.append("COLUMNS")
        
        if self.ref_feature is not None:
            self.__func_other_arg_sql_names.append("RefFeatureColumn")
            self.__func_other_args.append(UtilFuncs._teradata_collapse_arglist(UtilFuncs._teradata_quote_arg(self.ref_feature,"\""),"'"))
            self.__func_other_arg_json_datatypes.append("COLUMNS")
        
        if self.ref_value is not None:
            self.__func_other_arg_sql_names.append("RefValueColumn")
            self.__func_other_args.append(UtilFuncs._teradata_collapse_arglist(UtilFuncs._teradata_quote_arg(self.ref_value,"\""),"'"))
            self.__func_other_arg_json_datatypes.append("COLUMNS")
        
        if self.replace_invalid is not None and self.replace_invalid != "positiveinfinity":
            self.__func_other_arg_sql_names.append("ReplaceInvalid")
            self.__func_other_args.append(UtilFuncs._teradata_collapse_arglist(self.replace_invalid,"'"))
            self.__func_other_arg_json_datatypes.append("STRING")
        
        if self.reftable_size is not None and self.reftable_size != "small":
            self.__func_other_arg_sql_names.append("RefTableSize")
            self.__func_other_args.append(UtilFuncs._teradata_collapse_arglist(self.reftable_size,"'"))
            self.__func_other_arg_json_datatypes.append("STRING")
        
        if self.distance_measure is not None and self.distance_measure != "cosine":
            self.__func_other_arg_sql_names.append("DistanceMeasure")
            self.__func_other_args.append(UtilFuncs._teradata_collapse_arglist(self.distance_measure,"'"))
            self.__func_other_arg_json_datatypes.append("STRING")
        
        if self.max_distance is not None:
            self.__func_other_arg_sql_names.append("MaxDistance")
            self.__func_other_args.append(UtilFuncs._teradata_collapse_arglist(self.max_distance,"'"))
            self.__func_other_arg_json_datatypes.append("DOUBLE")
        
        if self.ignore_mismatch is not None and self.ignore_mismatch != True:
            self.__func_other_arg_sql_names.append("IgnoreMismatch")
            self.__func_other_args.append(UtilFuncs._teradata_collapse_arglist(self.ignore_mismatch,"'"))
            self.__func_other_arg_json_datatypes.append("BOOLEAN")
        
        if self.top_k is not None and self.top_k != 2147483647:
            self.__func_other_arg_sql_names.append("TopK")
            self.__func_other_args.append(UtilFuncs._teradata_collapse_arglist(self.top_k,"'"))
            self.__func_other_arg_json_datatypes.append("INTEGER")
        
        # Generate lists for rest of the function arguments
        sequence_input_by_list = []
        if self.target_data_sequence_column is not None:
            sequence_input_by_list.append("target:" + UtilFuncs._teradata_collapse_arglist(self.target_data_sequence_column,""))
        
        if self.ref_data_sequence_column is not None:
            sequence_input_by_list.append("ref:" + UtilFuncs._teradata_collapse_arglist(self.ref_data_sequence_column,""))
        
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
        
        # Process target_data
        self.target_data_partition_column = UtilFuncs._teradata_collapse_arglist(self.target_data_partition_column,"\"")
        self.__table_ref = self.__awu._teradata_on_clause_from_dataframe(self.target_data, False)
        self.__func_input_distribution.append("FACT")
        self.__func_input_arg_sql_names.append("target")
        self.__func_input_table_view_query.append(self.__table_ref["ref"])
        self.__func_input_dataframe_type.append(self.__table_ref["ref_type"])
        self.__func_input_partition_by_cols.append(self.target_data_partition_column)
        self.__func_input_order_by_cols.append(UtilFuncs._teradata_collapse_arglist(self.target_data_order_column,"\""))
        
        # Process ref_data
        self.__table_ref = self.__awu._teradata_on_clause_from_dataframe(self.ref_data, False)
        self.__func_input_distribution.append("DIMENSION")
        self.__func_input_arg_sql_names.append("ref")
        self.__func_input_table_view_query.append(self.__table_ref["ref"])
        self.__func_input_dataframe_type.append(self.__table_ref["ref_type"])
        self.__func_input_partition_by_cols.append("NA_character_")
        self.__func_input_order_by_cols.append(UtilFuncs._teradata_collapse_arglist(self.ref_data_order_column,"\""))
        
        function_name = "VectorDistance"
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
        Returns the string representation for a VectorDistance class instance.
        """
        repr_string="############ STDOUT Output ############"
        repr_string = "{}\n\n{}".format(repr_string,self.result)
        return repr_string
        
