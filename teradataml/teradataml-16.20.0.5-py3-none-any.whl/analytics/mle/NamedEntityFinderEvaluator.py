#!/usr/bin/python
# ################################################################## 
# 
# Copyright 2018 Teradata. All rights reserved.
# TERADATA CONFIDENTIAL AND TRADE SECRET
# 
# Primary Owner: Adithya Avvaru (adithya.avvaru@teradata.com)
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
from teradataml.analytics.mle.NamedEntityFinderTrainer import NamedEntityFinderTrainer

class NamedEntityFinderEvaluator:
    
    def __init__(self,
        newdata = None,
        text_column = None,
        model = None,
        newdata_sequence_column = None,
        newdata_order_column = None):
        """
        DESCRIPTION:
            The NamedEntityFinderEvaluator function includes two functions:
            • The NamedEntityFinderEvaluatorMap function operates as a row
              function.
            • The NamedEntityFinderEvaluatorReduce function operates as a
              partition function.
            Each function takes a set of evaluating data and creates the precision,
            recall, and F-measure values of a specified maximum entropy data model.
            Neither function supports regular-expression-based or dictionary-based
            models.


        PARAMETERS:
            newdata:
                Required Argument.
                Specifies the input teradataml DataFrame containing a text column
                which contains input text.

            newdata_order_column:
                Optional Argument.
                Specifies Order By columns for newdata.
                Values to this argument can be provided as a list, if multiple
                columns are used for ordering.
                Types: str OR list of Strings (str)

            text_column:
                Required Argument.
                Specifies the name of the input teradataml DataFrame column that
                contains the text to analyze.
                Types: str

            model:
                Required Argument.
                Specifies the name of the model file to evaluate.
                Types: str

            newdata_sequence_column:
                Optional Argument.
                Specifies the list of column(s) that uniquely identifies each row of
                the input argument "newdata". The argument is used to ensure
                deterministic results for functions which produce results that vary
                from run to run.
                Types: str OR list of Strings (str)

        RETURNS:
            Instance of NamedEntityFinderEvaluator.
            Output teradataml DataFrames can be accessed using attribute
            references, such as NamedEntityFinderEvaluatorObj.<attribute_name>.
            Output teradataml DataFrame attribute name is:
                result


        RAISES:
            TeradataMlException


        EXAMPLES:
            # Load example data.
            load_example_data("namedentityfinderevaluator", ["nermem_sports_train", "nermem_sports_test"])

            # Provided example tables are 'nermem_sports_train', 'nermem_sports_test'.
            # Table 'nermem_sports_train' contains column 'content' on which the analytical
            # function NamedEntityFinderTrainer is trained.
            # Table 'nermem_sports_test' contains column 'content' on which
            # NamedEntityFinderEvaluator is used to evaluate the content.

            # Create teradataml DataFrame objects.
            nermem_sports_train = DataFrame.from_table('nermem_sports_train')
            nermem_sports_test = DataFrame.from_table('nermem_sports_test')

            # Example 1 : Using NamedEntityFinderTrainer to train the NamedEntityFinder and
            #              get the precision, recall and F-score, on testing data using
            #              NamedEntityFinderEvaluator.
            trainer_out = NamedEntityFinderTrainer(data=nermem_sports_train,
                                                   entity_type="LOCATION",
                                                   text_column="content",
                                                   model='location.sports')

            # Here model is saved in 'location.sports' and is used in NamedEntityFinderEvaluator
            # to evaluate the named entities on test data.

            result = NamedEntityFinderEvaluator(newdata=nermem_sports_test, text_column='content',
                                                model='location.sports')

            # Print the results.
            print(result.result)
        
        """
        self.newdata  = newdata 
        self.text_column  = text_column 
        self.model  = model
        self.newdata_sequence_column  = newdata_sequence_column 
        self.newdata_order_column  = newdata_order_column 
        
        # Create TeradataPyWrapperUtils instance which contains validation functions.
        self.__awu = AnalyticsWrapperUtils()
        self.__aed_utils = AedUtils()
        
        # Create argument information matrix to do parameter checking
        self.__arg_info_matrix = []
        self.__arg_info_matrix.append(["newdata", self.newdata, False, (DataFrame)])
        self.__arg_info_matrix.append(["newdata_order_column", self.newdata_order_column, True, (str,list)])
        self.__arg_info_matrix.append(["text_column", self.text_column, False, (str)])
        self.__arg_info_matrix.append(["model", self.model, False, (str)])
        self.__arg_info_matrix.append(["newdata_sequence_column", self.newdata_sequence_column, True, (str,list)])
        
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
        self.__awu._validate_input_table_datatype(self.newdata, "newdata", None)
        
        # Check whether the input columns passed to the argument are not empty.
        # Also check whether the input columns passed to the argument valid or not.
        self.__awu._validate_input_columns_not_empty(self.text_column, "text_column")
        self.__awu._validate_dataframe_has_argument_columns(self.text_column, "text_column", self.newdata, "newdata", False)
        
        self.__awu._validate_input_columns_not_empty(self.newdata_sequence_column, "newdata_sequence_column")
        self.__awu._validate_dataframe_has_argument_columns(self.newdata_sequence_column, "newdata_sequence_column", self.newdata, "newdata", False)
        
        self.__awu._validate_input_columns_not_empty(self.newdata_order_column, "newdata_order_column")
        self.__awu._validate_dataframe_has_argument_columns(self.newdata_order_column, "newdata_order_column", self.newdata, "newdata", False)
        
        
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
        
        self.__func_other_arg_sql_names.append("TextColumn")
        self.__func_other_args.append(UtilFuncs._teradata_collapse_arglist(UtilFuncs._teradata_quote_arg(self.text_column,"\""),"'"))
        self.__func_other_arg_json_datatypes.append("COLUMNS")
        
        self.__func_other_arg_sql_names.append("Model")
        self.__func_other_args.append(UtilFuncs._teradata_collapse_arglist(self.model,"'"))
        self.__func_other_arg_json_datatypes.append("STRING")
        
        # Generate lists for rest of the function arguments
        sequence_input_by_list = []
        if self.newdata_sequence_column is not None:
            sequence_input_by_list.append("input:" + UtilFuncs._teradata_collapse_arglist(self.newdata_sequence_column,""))
        
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
        
        # Process newdata
        self.__table_ref = self.__awu._teradata_on_clause_from_dataframe(self.newdata, False)
        self.__func_input_distribution.append("FACT")
        self.__func_input_arg_sql_names.append("input")
        self.__func_input_table_view_query.append(self.__table_ref["ref"])
        self.__func_input_dataframe_type.append(self.__table_ref["ref_type"])
        self.__func_input_partition_by_cols.append("ANY")
        self.__func_input_order_by_cols.append(UtilFuncs._teradata_collapse_arglist(self.newdata_order_column,"\""))
        
        function_name = "NamedEntityFinderEvaluatorMap"
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
        
        # Declare empty lists to hold input table information.
        self.__func_input_arg_sql_names = []
        self.__func_input_table_view_query = []
        self.__func_input_dataframe_type = []
        self.__func_input_distribution = []
        self.__func_input_partition_by_cols = []
        self.__func_input_order_by_cols = []
        
        # Process data
        self.__table_ref = self.__awu._teradata_on_clause_from_dataframe(self.newdata, False)
        self.__func_input_distribution.append("FACT")
        self.__func_input_arg_sql_names.append("input")
        self.__func_input_table_view_query.append(aqg_obj._gen_sqlmr_invocation_sql())
        self.__func_input_dataframe_type.append("TABLE")
        self.__func_input_partition_by_cols.append("1")
        self.__func_input_order_by_cols.append("NA_character_")
        
        # Create instance for mapreduce SQLMR.
        aqg_obj = AnalyticQueryGenerator("NamedEntityFinderEvaluatorReduce"
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
        Returns the string representation for a NamedEntityFinderEvaluator class instance.
        """
        repr_string="############ STDOUT Output ############"
        repr_string = "{}\n\n{}".format(repr_string,self.result)
        return repr_string
        
