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
# Function Version: 3.7
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

class TextTokenizer:
    
    def __init__(self,
        data = None,
        dict_data = None,
        text_column = None,
        language = "en",
        model = None,
        output_delimiter = "/",
        output_byword = False,
        user_dictionary = None,
        accumulate = None,
        data_sequence_column = None,
        dict_data_sequence_column = None,
        data_order_column = None,
        dict_data_order_column = None):
        """
        DESCRIPTION:
            The TextTokenizer function extracts English, Chinese, or Japanese
            tokens from text. Examples of tokens are words, punctuation marks,
            and numbers. Tokenization is the first step of many types of
            text analysis.


        PARAMETERS:
            data:
                Required Argument.
                teradataml DataFrame that contains the text to be scanned.

            data_order_column:
                Optional Argument.
                Specifies Order By columns for data.
                Values to this argument can be provided as a list, if multiple
                columns are used for ordering.
                Types: str OR list of Strings (str)

            dict_data:
                Optional Argument.
                teradataml DataFrame that contains the dictionary for
                segementing words.

            dict_data_order_column:
                Optional Argument.
                Specifies Order By columns for dict_data.
                Values to this argument can be provided as a list, if multiple
                columns are used for ordering.
                Types: str OR list of Strings (str)

            text_column:
                Required Argument.
                Specifies name of the column in the argument data, that contains
                the text to tokenize.
                Types: str

            language:
                Optional Argument.
                Specifies the language of the text in text_column.
                Default Value: "en"
                Permitted Values: en, zh_CN, zh_TW, jp
                Types: str

            model:
                Optional Argument.
                Specifies the name of model file that the function uses for
                tokenizing. The model must be a conditional random-fields model and
                model_file must already be installed on the database. If you omit
                this argument, or if model_file is not installed on the database,
                then the function uses white spaces to separate English words and an
                embedded dictionary to tokenize Chinese text.
                Note: If you specify the argument "language" with value "jp", the
                      function ignores this argument.
                Types: str

            output_delimiter:
                Optional Argument.
                Specifies the delimiter for separating tokens in the output.
                Default Value: "/"
                Types: str

            output_byword:
                Optional Argument.
                Specifies whether to output one token in each row (output one
                line of text in each row).
                Default Value: False
                Types: bool

            user_dictionary:
                Optional Argument.
                Specifies the name of the user dictionary to use to correct
                results specified by the model. If you specify both this
                argument and a dictionary teradataml DataFrame (dict_data), then
                the function uses the union of user_dictionary and dict_data as
                its dictionary. That describes the format of user_dictionary_file
                and dict.
                Note: If the function finds more than one matched term,
                      it selects the longest term for the first match.
                Types: str

            accumulate:
                Optional Argument.
                Specifies the name of the column in the argument data, to copy
                to the output table.
                Types: str OR list of Strings (str)

            data_sequence_column:
                Optional Argument.
                Specifies the list of column(s) that uniquely identifies each
                row of the input argument "data". The argument is used to ensure
                deterministic results for functions which produce results that
                vary from run to run.
                Types: str OR list of Strings (str)

            dict_data_sequence_column:
                Optional Argument.
                Specifies the list of column(s) that uniquely identifies each
                row of the input argument "dict_data". The argument is used to
                ensure deterministic results for functions which produce results
                that vary from run to run.
                Types: str OR list of Strings (str)

        RETURNS:
            Instance of TextTokenizer.
            Output teradataml DataFrames can be accessed using attribute
            references, such as TextTokenizerObj.<attribute_name>.
            Output teradataml DataFrame attribute name is:
                result


        RAISES:
            TeradataMlException


        EXAMPLES:
            # Load the data to run the example.
            load_example_data("TextTokenizer","complaints")

            # Create teradataml DataFrame
            complaints = DataFrame.from_table("complaints")

            # Example 1 -
            text_tokenizer_out = TextTokenizer(data=complaints,
                                               text_column='text_data',
                                               language='en',
                                               output_delimiter=' ',
                                               output_byword =True,
                                               accumulate='doc_id')
            # Print the result DataFrame
            print(text_tokenizer_out.result)

        """
        self.data  = data 
        self.dict_data  = dict_data 
        self.text_column  = text_column 
        self.language  = language 
        self.model  = model 
        self.output_delimiter  = output_delimiter 
        self.output_byword  = output_byword
        self.user_dictionary  = user_dictionary 
        self.accumulate  = accumulate 
        self.data_sequence_column  = data_sequence_column 
        self.dict_data_sequence_column  = dict_data_sequence_column 
        self.data_order_column  = data_order_column 
        self.dict_data_order_column  = dict_data_order_column 
        
        # Create TeradataPyWrapperUtils instance which contains validation functions.
        self.__awu = AnalyticsWrapperUtils()
        self.__aed_utils = AedUtils()
        
        # Create argument information matrix to do parameter checking
        self.__arg_info_matrix = []
        self.__arg_info_matrix.append(["data", self.data, False, (DataFrame)])
        self.__arg_info_matrix.append(["data_order_column", self.data_order_column, True, (str,list)])
        self.__arg_info_matrix.append(["dict_data", self.dict_data, True, (DataFrame)])
        self.__arg_info_matrix.append(["dict_data_order_column", self.dict_data_order_column, True, (str,list)])
        self.__arg_info_matrix.append(["text_column", self.text_column, False, (str)])
        self.__arg_info_matrix.append(["language", self.language, True, (str)])
        self.__arg_info_matrix.append(["model", self.model, True, (str)])
        self.__arg_info_matrix.append(["output_delimiter", self.output_delimiter, True, (str)])
        self.__arg_info_matrix.append(["output_byword", self.output_byword, True, (bool)])
        self.__arg_info_matrix.append(["user_dictionary", self.user_dictionary, True, (str)])
        self.__arg_info_matrix.append(["accumulate", self.accumulate, True, (str,list)])
        self.__arg_info_matrix.append(["data_sequence_column", self.data_sequence_column, True, (str,list)])
        self.__arg_info_matrix.append(["dict_data_sequence_column", self.dict_data_sequence_column, True, (str,list)])
        
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
        self.__awu._validate_input_table_datatype(self.dict_data, "dict_data", None)
        
        # Check for permitted values
        language_permitted_values = ["EN", "ZH_CN", "ZH_TW", "JP"]
        self.__awu._validate_permitted_values(self.language, language_permitted_values, "language")
        
        # Check whether the input columns passed to the argument are not empty.
        # Also check whether the input columns passed to the argument valid or not.
        self.__awu._validate_input_columns_not_empty(self.text_column, "text_column")
        self.__awu._validate_dataframe_has_argument_columns(self.text_column, "text_column", self.data, "data", False)
        
        self.__awu._validate_input_columns_not_empty(self.accumulate, "accumulate")
        self.__awu._validate_dataframe_has_argument_columns(self.accumulate, "accumulate", self.data, "data", False)
        
        self.__awu._validate_input_columns_not_empty(self.data_sequence_column, "data_sequence_column")
        self.__awu._validate_dataframe_has_argument_columns(self.data_sequence_column, "data_sequence_column", self.data, "data", False)
        
        self.__awu._validate_input_columns_not_empty(self.dict_data_sequence_column, "dict_data_sequence_column")
        self.__awu._validate_dataframe_has_argument_columns(self.dict_data_sequence_column, "dict_data_sequence_column", self.dict_data, "dict_data", False)
        
        self.__awu._validate_input_columns_not_empty(self.data_order_column, "data_order_column")
        self.__awu._validate_dataframe_has_argument_columns(self.data_order_column, "data_order_column", self.data, "data", False)
        
        self.__awu._validate_input_columns_not_empty(self.dict_data_order_column, "dict_data_order_column")
        self.__awu._validate_dataframe_has_argument_columns(self.dict_data_order_column, "dict_data_order_column", self.dict_data, "dict_data", False)
        
        
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
        
        if self.accumulate is not None:
            self.__func_other_arg_sql_names.append("Accumulate")
            self.__func_other_args.append(UtilFuncs._teradata_collapse_arglist(UtilFuncs._teradata_quote_arg(self.accumulate,"\""),"'"))
            self.__func_other_arg_json_datatypes.append("COLUMNS")
        
        if self.language is not None and self.language != "en":
            self.__func_other_arg_sql_names.append("InputLanguage")
            self.__func_other_args.append(UtilFuncs._teradata_collapse_arglist(self.language,"'"))
            self.__func_other_arg_json_datatypes.append("STRING")
        
        if self.output_delimiter is not None and self.output_delimiter != "/":
            self.__func_other_arg_sql_names.append("OutputDelimiter")
            self.__func_other_args.append(UtilFuncs._teradata_collapse_arglist(self.output_delimiter,"'"))
            self.__func_other_arg_json_datatypes.append("STRING")
        
        if self.output_byword is not None and self.output_byword != False:
            self.__func_other_arg_sql_names.append("OutputByWord")
            self.__func_other_args.append(UtilFuncs._teradata_collapse_arglist(self.output_byword,"'"))
            self.__func_other_arg_json_datatypes.append("BOOLEAN")
        
        if self.user_dictionary is not None:
            self.__func_other_arg_sql_names.append("userDictionaryFile")
            self.__func_other_args.append(UtilFuncs._teradata_collapse_arglist(self.user_dictionary,"'"))
            self.__func_other_arg_json_datatypes.append("STRING")
        
        if self.model is not None:
            self.__func_other_arg_sql_names.append("ModelFile")
            self.__func_other_args.append(UtilFuncs._teradata_collapse_arglist(self.model,"'"))
            self.__func_other_arg_json_datatypes.append("STRING")
        
        # Generate lists for rest of the function arguments
        sequence_input_by_list = []
        if self.data_sequence_column is not None:
            sequence_input_by_list.append("input:" + UtilFuncs._teradata_collapse_arglist(self.data_sequence_column,""))
        
        if self.dict_data_sequence_column is not None:
            sequence_input_by_list.append("dict:" + UtilFuncs._teradata_collapse_arglist(self.dict_data_sequence_column,""))
        
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
        
        # Process dict_data
        if self.dict_data is not None:
            self.__table_ref = self.__awu._teradata_on_clause_from_dataframe(self.dict_data, False)
            self.__func_input_distribution.append("DIMENSION")
            self.__func_input_arg_sql_names.append("dict")
            self.__func_input_table_view_query.append(self.__table_ref["ref"])
            self.__func_input_dataframe_type.append(self.__table_ref["ref_type"])
            self.__func_input_partition_by_cols.append("NA_character_")
            self.__func_input_order_by_cols.append(UtilFuncs._teradata_collapse_arglist(self.dict_data_order_column,"\""))
        
        function_name = "TextTokenizer"
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
        Returns the string representation for a TextTokenizer class instance.
        """
        repr_string="############ STDOUT Output ############"
        repr_string = "{}\n\n{}".format(repr_string,self.result)
        return repr_string
        
