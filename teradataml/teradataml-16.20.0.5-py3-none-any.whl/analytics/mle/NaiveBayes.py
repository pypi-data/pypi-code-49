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
# Function Version: 1.9
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

class NaiveBayes:
    
    def __init__(self,
        formula = None,
        data = None,
        data_sequence_column = None,
        data_order_column = None):
        """
        DESCRIPTION:
            The NaiveBayesMap and NaiveBayesReduce functions generate a model from
            training data. A virtual data frame of training data is input to
            the NaiveBayesMap function, whose output is the input to
            NaiveBayesReduce function, which outputs the model.


        PARAMETERS:
            formula:
                Required Argument.
                A string consisting of "formula". Specifies the model to be fitted. Only
                basic formula of the "col1 ~ col2 + col3 +..." form is supported and
                all variables must be from the same virtual data frame object. The
                response should be column of type real, numeric, integer or boolean.
                Types: str

            data:
                Required Argument.
                This is teradataml DataFrame defining the input training data.

            data_order_column:
                Optional Argument.
                Specifies Order By columns for data.
                Values to this argument can be provided as a list, if multiple
                columns are used for ordering.
                Types: str OR list of Strings (str)

            data_sequence_column:
                Optional Argument.
                Specifies the list of column(s) that uniquely identifies each row of
                the input argument "data". The argument is used to ensure
                deterministic results for functions which produce results that vary
                from run to run.
                Types: str OR list of Strings (str)

        RETURNS:
            Instance of NaiveBayes.
            Output teradataml DataFrames can be accessed using attribute
            references, such as NaiveBayesObj.<attribute_name>.
            Output teradataml DataFrame attribute name is:
                result


        RAISES:
            TeradataMlException


        EXAMPLES:
            # Load the data to run the example
            load_example_data("NaiveBayes","nb_iris_input_train")

            # Create teradataml DataFrame object.
            nb_iris_input_train = DataFrame.from_table("nb_iris_input_train")

            # Run the train function
            naivebayes_train = NaiveBayes(formula="species ~ petal_length + sepal_width + petal_width + sepal_length",
                                          data=nb_iris_input_train)

            # Print the result DataFrame
            print(naivebayes_train.result)
        
        """
        self.formula  = formula 
        self.data  = data 
        self.data_sequence_column  = data_sequence_column 
        self.data_order_column  = data_order_column 
        
        # Create TeradataPyWrapperUtils instance which contains validation functions.
        self.__awu = AnalyticsWrapperUtils()
        self.__aed_utils = AedUtils()
        
        # Create argument information matrix to do parameter checking
        self.__arg_info_matrix = []
        self.__arg_info_matrix.append(["formula", self.formula, False, "formula"])
        self.__arg_info_matrix.append(["data", self.data, False, (DataFrame)])
        self.__arg_info_matrix.append(["data_order_column", self.data_order_column, True, (str,list)])
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
        self.__awu._validate_input_columns_not_empty(self.data_sequence_column, "data_sequence_column")
        self.__awu._validate_dataframe_has_argument_columns(self.data_sequence_column, "data_sequence_column", self.data, "data", False)
        
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
        
        # Generate lists for rest of the function arguments
        sequence_input_by_list = []
        if self.data_sequence_column is not None:
            sequence_input_by_list.append("input:" + UtilFuncs._teradata_collapse_arglist(self.data_sequence_column,""))
        
        if len(sequence_input_by_list) > 0:
            self.__func_other_arg_sql_names.append("SequenceInputBy")
            self.__func_other_args.append(UtilFuncs._teradata_collapse_arglist(sequence_input_by_list,"'"))
            self.__func_other_arg_json_datatypes.append("STRING")
        
        # Let's process formula argument
        formula_object = self.__awu._validate_formula_notation(self.formula, self.data, "formula")
        # response variable
        response = formula_object._get_dependent_vars()
        self.__func_other_arg_sql_names.append("ResponseColumn")
        self.__func_other_args.append(UtilFuncs._teradata_collapse_arglist(UtilFuncs._teradata_quote_arg(response,"\""),"'"))
        self.__func_other_arg_json_datatypes.append("COLUMN_NAMES")
        
        # numerical input columns
        numerical_inputs = self.__awu._get_columns_by_type(formula_object,self.data, "numerical")
        if len(numerical_inputs) > 0:
            self.__func_other_arg_sql_names.append("NumericInputs")
            self.__func_other_args.append(UtilFuncs._teradata_collapse_arglist(UtilFuncs._teradata_quote_arg(numerical_inputs,"\""),"'"))
            self.__func_other_arg_json_datatypes.append("COLUMN_NAMES")
        
        # categorical input columns
        categorical_inputs = self.__awu._get_columns_by_type(formula_object,self.data, "categorical")
        if len(categorical_inputs) > 0:
            self.__func_other_arg_sql_names.append("CategoricalInputs")
            self.__func_other_args.append(UtilFuncs._teradata_collapse_arglist(UtilFuncs._teradata_quote_arg(categorical_inputs,"\""),"'"))
            self.__func_other_arg_json_datatypes.append("COLUMN_NAMES")
        
        
        # Declare empty lists to hold input table information.
        self.__func_input_arg_sql_names = []
        self.__func_input_table_view_query = []
        self.__func_input_dataframe_type = []
        self.__func_input_distribution = []
        self.__func_input_partition_by_cols = []
        self.__func_input_order_by_cols = []
        
        # Process data
        self.__table_ref = self.__awu._teradata_on_clause_from_dataframe(self.data)
        self.__func_input_distribution.append("FACT")
        self.__func_input_arg_sql_names.append("input")
        self.__func_input_table_view_query.append(self.__table_ref["ref"])
        self.__func_input_dataframe_type.append(self.__table_ref["ref_type"])
        self.__func_input_partition_by_cols.append("ANY")
        self.__func_input_order_by_cols.append(UtilFuncs._teradata_collapse_arglist(self.data_order_column,"\""))
        
        function_name = "NaiveBayesMap"
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
        
        # Declare empty lists to hold input table information.
        self.__func_input_arg_sql_names = []
        self.__func_input_table_view_query = []
        self.__func_input_dataframe_type = []
        self.__func_input_distribution = []
        self.__func_input_partition_by_cols = []
        self.__func_input_order_by_cols = []
        
        # Process data
        self.__table_ref = self.__awu._teradata_on_clause_from_dataframe(self.data)
        self.__func_input_distribution.append("FACT")
        self.__func_input_arg_sql_names.append("input")
        self.__func_input_table_view_query.append(self.__aqg_obj._gen_sqlmr_invocation_sql())
        self.__func_input_dataframe_type.append("TABLE")
        self.__func_input_partition_by_cols.append("class_nb")
        self.__func_input_order_by_cols.append("NA_character_")
        
        # Create instance for mapreduce SQLMR.
        self.__aqg_obj = AnalyticQueryGenerator("NaiveBayesReduce" 
                ,self.__func_input_arg_sql_names 
                ,self.__func_input_table_view_query 
                ,self.__func_input_dataframe_type 
                ,self.__func_input_distribution 
                ,self.__func_input_partition_by_cols 
                ,self.__func_input_order_by_cols 
                ,[] 
                ,[] 
                ,[] 
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
            node_id_list = self.__aed_utils._aed_ml_query(self.__input_nodeids, self.sqlmr_query, self.__func_output_args, "NaiveBayes", self.__aqg_obj._multi_query_input_nodes)
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
        stdout_column_info_name.append("class_nb")
        stdout_column_info_type.append(self.__awu._get_json_to_sqlalchemy_mapping("varchar"))
        
        stdout_column_info_name.append("variable_nb")
        stdout_column_info_type.append(self.__awu._get_json_to_sqlalchemy_mapping("varchar"))
        
        stdout_column_info_name.append("type_nb")
        stdout_column_info_type.append(self.__awu._get_json_to_sqlalchemy_mapping("varchar"))
        
        stdout_column_info_name.append("category")
        stdout_column_info_type.append(self.__awu._get_json_to_sqlalchemy_mapping("varchar"))
        
        stdout_column_info_name.append("cnt")
        stdout_column_info_type.append(self.__awu._get_json_to_sqlalchemy_mapping("bigint"))
        
        stdout_column_info_name.append("sum_nb")
        stdout_column_info_type.append(self.__awu._get_json_to_sqlalchemy_mapping("double precision"))
        
        stdout_column_info_name.append("sum_sq")
        stdout_column_info_type.append(self.__awu._get_json_to_sqlalchemy_mapping("double precision"))
        
        stdout_column_info_name.append("total_cnt")
        stdout_column_info_type.append(self.__awu._get_json_to_sqlalchemy_mapping("bigint"))
        
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
        Returns the string representation for a NaiveBayes class instance.
        """
        repr_string="############ STDOUT Output ############"
        repr_string = "{}\n\n{}".format(repr_string,self.result)
        return repr_string
        
