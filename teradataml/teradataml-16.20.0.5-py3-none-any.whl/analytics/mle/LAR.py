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

class LAR:
    
    def __init__(self,
        formula = None,
        data = None,
        type = "LASSO",
        max_steps  = None,
        normalize = True,
        intercept = True,
        data_sequence_column = None):
        """
        DESCRIPTION:
            The LAR (Least Angle Regression) function creates a model that the function LARPredict uses to
            make predictions for the response variables.


        PARAMETERS:
            formula:
                Required Argument.
                A string consisting of "formula". Specifies the model to be fitted.
                Only basic formula of the "col1 ~ col2 + col3 +..." form are
                supported and all variables must be from the same teradataml
                DataFrame object. The response should be column of type float, int or
                bool.
                Types: str

            data:
                Required Argument.
                Specifies the name of the input teradataml DataFrame.

            type:
                Optional Argument.
                Specifies the method to use for linear regression.
                Default Value: "LASSO"
                Permitted Values: LAR, LASSO
                Types: str

            max_steps :
                Optional Argument.
                Specifies the maximum number of steps the function executes. The
                default value is 8 * min(number_of_predictors, sample_size -
                intercept).
                For example, if the number of predictors is 11, the sample size
                (number of rows in the input teradataml DataFrame) is 1532, and the intercept
                is 1, then the default value is 8 * min(11, 1532 - 1) = 88.
                Types: int

            normalize:
                Optional Argument.
                Specifies whether each predictor is standardized to have unit L2
                norm.
                Default Value: True
                Types: bool

            intercept:
                Optional Argument.
                Specifies whether an intercept is included in the model (and not
                penalized).
                Default Value: True
                Types: bool

            data_sequence_column:
                Optional Argument.
                Specifies the list of column(s) that uniquely identifies each row of
                the input argument "data". The argument is used to ensure
                deterministic results for functions which produce results that vary
                from run to run.
                Types: str OR list of Strings (str)

        RETURNS:
            Instance of LAR.
            Output teradataml DataFrames can be accessed using attribute
            references, such as LARObj.<attribute_name>.
            Output teradataml DataFrame attribute name is:
                1. output_table
                2. output


        RAISES:
            TeradataMlException


        EXAMPLES:
            # Load example data
            load_example_data("lar", "diabetes")

            # Create teradataml DataFrame objects.
            diabetes = DataFrame.from_table("diabetes")

            # Example - Build a LAR model with response variable 'y' and ten baseline predictors
            LAR_out = LAR(formula = "y ~ hdl + glu + ldl + map1 + sex + tch + age + ltg + bmi + tc",
                          data = diabetes,
                          type = "lar",
                          max_steps  = 20,
                          normalize = True,
                          intercept = True
                          )

            # Print the results
            print(LAR_out)
        
        """
        self.formula  = formula 
        self.data  = data 
        self.type  = type 
        self.max_steps   = max_steps  
        self.normalize  = normalize 
        self.intercept  = intercept 
        self.data_sequence_column  = data_sequence_column 
        
        # Create TeradataPyWrapperUtils instance which contains validation functions.
        self.__awu = AnalyticsWrapperUtils()
        self.__aed_utils = AedUtils()
        
        # Create argument information matrix to do parameter checking
        self.__arg_info_matrix = []
        self.__arg_info_matrix.append(["formula", self.formula, False, "formula"])
        self.__arg_info_matrix.append(["data", self.data, False, (DataFrame)])
        self.__arg_info_matrix.append(["type", self.type, True, (str)])
        self.__arg_info_matrix.append(["max_steps ", self.max_steps , True, (int)])
        self.__arg_info_matrix.append(["normalize", self.normalize, True, (bool)])
        self.__arg_info_matrix.append(["intercept", self.intercept, True, (bool)])
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
        
        # Check for permitted values
        type_permitted_values = ["LAR", "LASSO"]
        self.__awu._validate_permitted_values(self.type, type_permitted_values, "type")
        
        # Check whether the input columns passed to the argument are not empty.
        # Also check whether the input columns passed to the argument valid or not.
        self.__awu._validate_input_columns_not_empty(self.data_sequence_column, "data_sequence_column")
        self.__awu._validate_dataframe_has_argument_columns(self.data_sequence_column, "data_sequence_column", self.data, "data", False)
        
        
    def __form_tdml_query(self):
        """
        Function to generate the analytical function queries. The function defines 
        variables and list of arguments required to form the query.
        """
        # Generate temp table names for output table parameters if any.
        self.__output_table_temp_tablename = UtilFuncs._generate_temp_table_name(prefix = "td_lar0", use_default_database = True, gc_on_quit = True, quote=False, table_type = TeradataConstants.TERADATA_TABLE)
        
        # Output table arguments list
        self.__func_output_args_sql_names = ["OutputTable"]
        self.__func_output_args = [self.__output_table_temp_tablename]
        
        # Generate lists for rest of the function arguments
        self.__func_other_arg_sql_names = []
        self.__func_other_args = []
        self.__func_other_arg_json_datatypes = []
        
        if self.type is not None and self.type != "LASSO":
            self.__func_other_arg_sql_names.append("FitMethod")
            self.__func_other_args.append(UtilFuncs._teradata_collapse_arglist(self.type,"'"))
            self.__func_other_arg_json_datatypes.append("STRING")
        
        if self.max_steps  is not None:
            self.__func_other_arg_sql_names.append("MaxIterNum")
            self.__func_other_args.append(UtilFuncs._teradata_collapse_arglist(self.max_steps ,"'"))
            self.__func_other_arg_json_datatypes.append("INTEGER")
        
        if self.intercept is not None and self.intercept != True:
            self.__func_other_arg_sql_names.append("Intercept")
            self.__func_other_args.append(UtilFuncs._teradata_collapse_arglist(self.intercept,"'"))
            self.__func_other_arg_json_datatypes.append("BOOLEAN")
        
        if self.normalize is not None and self.normalize != True:
            self.__func_other_arg_sql_names.append("L2Normalization")
            self.__func_other_args.append(UtilFuncs._teradata_collapse_arglist(self.normalize,"'"))
            self.__func_other_arg_json_datatypes.append("BOOLEAN")
        
        # Generate lists for rest of the function arguments
        sequence_input_by_list = []
        if self.data_sequence_column is not None:
            sequence_input_by_list.append("InputTable:" + UtilFuncs._teradata_collapse_arglist(self.data_sequence_column,""))
        
        if len(sequence_input_by_list) > 0:
            self.__func_other_arg_sql_names.append("SequenceInputBy")
            self.__func_other_args.append(UtilFuncs._teradata_collapse_arglist(sequence_input_by_list,"'"))
            self.__func_other_arg_json_datatypes.append("STRING")
        
        # Let's process formula argument
        formula_object = self.__awu._validate_formula_notation(self.formula, self.data, "formula")
        # numerical input columns
        numerical_inputs = self.__awu._get_columns_by_type(formula_object,self.data, "numerical")
        if len(numerical_inputs) > 0:
            self.__func_other_arg_sql_names.append("TargetColumns")
            self.__func_other_args.append(UtilFuncs._teradata_collapse_arglist(UtilFuncs._teradata_quote_arg(numerical_inputs,"\""),"'"))
            self.__func_other_arg_json_datatypes.append("COLUMN_NAMES")
        
        
        # Declare empty lists to hold input table information.
        self.__func_input_arg_sql_names = []
        self.__func_input_table_view_query = []
        self.__func_input_dataframe_type = []
        self.__func_input_distribution = []
        self.__func_input_partition_by_cols = []
        self.__func_input_order_by_cols = []
        
        # Process data
        self.__table_ref = self.__awu._teradata_on_clause_from_dataframe(self.data, False)
        self.__func_input_distribution.append("NONE")
        self.__func_input_arg_sql_names.append("InputTable")
        self.__func_input_table_view_query.append(self.__table_ref["ref"])
        self.__func_input_dataframe_type.append(self.__table_ref["ref_type"])
        self.__func_input_partition_by_cols.append("NA_character_")
        self.__func_input_order_by_cols.append("NA_character_")
        
        function_name = "LAR"
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
        Returns the string representation for a LAR class instance.
        """
        repr_string="############ STDOUT Output ############"
        repr_string = "{}\n\n{}".format(repr_string,self.output)
        repr_string="{}\n\n\n############ output_table Output ############".format(repr_string)
        repr_string = "{}\n\n{}".format(repr_string,self.output_table)
        return repr_string
        
