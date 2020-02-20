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
# Function Version: 1.6
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
from teradataml.analytics.mle.SentimentExtractor import SentimentExtractor

class SentimentEvaluator:
    
    def __init__(self,
        object = None,
        obs_column = None,
        sentiment_column = None,
        object_sequence_column = None,
        object_order_column = None):
        """
        DESCRIPTION:
            The SentimentEvaluator function uses test data to evaluate the
            precision and recall of the predictions output by the function
            SentimentExtractor. The precision and recall are affected by the
            model that SentimentExtractor uses; therefore, if you change the
            model, you must rerun SentimentEvaluator on the new predictions.


        PARAMETERS:
            object:
                Required Argument.
                Specifies the input teradataml DataFrame containing a text
                column with the input text.

            object_order_column:
                Optional Argument.
                Specifies Order By columns for object.
                Values to this argument can be provided as list, if multiple columns
                are used for ordering.
                Types: str OR list of Strings (str)

            obs_column:
                Required Argument.
                Specifies the name of the input column with the observed sentiment
                (POS, NEG or NEU).
                Types: str

            sentiment_column:
                Required Argument.
                Specifies the name of the input column with the predicted sentiment
                (POS, NEG or NEU).
                Types: str

            object_sequence_column:
                Optional Argument.
                Specifies the list of column(s) that uniquely identifies each row of
                the input argument "object". The argument is used to ensure
                deterministic results for functions which produce results that vary
                from run to run.
                Types: str OR list of Strings (str)

        RETURNS:
            Instance of SentimentEvaluator.
            Output teradataml DataFrames can be accessed using attribute
            references, such as SentimentEvaluatorObj.<attribute_name>.
            Output teradataml DataFrame attribute name is:
                result


        RAISES:
            TeradataMlException


        EXAMPLES:
            # Load example data.
            load_example_data("sentimenttrainer", "sentiment_train")
            load_example_data("sentimentextractor", ["sentiment_extract_input", "sentiment_word"])

            # Create teradataml DataFrame objects.
            sentiment_train = DataFrame.from_table("sentiment_train")
            sentiment_extract_input = DataFrame.from_table("sentiment_extract_input")
            sentiment_word = DataFrame.from_table("sentiment_word")

            # Example 1 -This example uses the dictionary model file 'default_sentiment_lexicon.txt'.
            SentimentExtractorOut1 = SentimentExtractor(object = "dictionary",
                                                        newdata = sentiment_extract_input,
                                                        text_column = "review",
                                                        accumulate = ["category"]
                                                        )

            SentimentEvaluatorOut1 = SentimentEvaluator(object=SentimentExtractorOut1.result,
                                                        obs_column='category',
                                                        sentiment_column='out_polarity'
                                                       )

            # Print the results.
            print(SentimentEvaluatorOut1)

            # Example 2 - This example uses the classification model file
            #             'default_sentiment_classification_model.bin'.
            SentimentExtractorOut2 = SentimentExtractor(object = "classification:default_sentiment_classification_model.bin",
                                                        newdata = sentiment_extract_input,
                                                        text_column = "review",
                                                        accumulate = ["category"]
                                                        )

            SentimentEvaluatorOut2 = SentimentEvaluator(object=SentimentExtractorOut2.result,
                                                        obs_column='category',
                                                        sentiment_column='out_polarity'
                                                       )

            # Print the results.
            print(SentimentEvaluatorOut2)

            # Example 3 - This example uses classification model file output by
            #             the SentimentTrainer function.
            SentimentTrainerOut = SentimentTrainer(data = sentiment_train,
                                                   text_column = "review",
                                                   sentiment_column = "category",
                                                   model_file = "sentimentmodel1.bin"
                                                   )

            # Use the sentiment extractor function to extract sentiment of each input document.
            SentimentExtractorOut3 = SentimentExtractor(object = "classification:sentimentmodel1.bin",
                                                        newdata = sentiment_extract_input,
                                                        text_column = "review",
                                                        accumulate = ["category"]
                                                        )

            SentimentEvaluatorOut3 = SentimentEvaluator(object=SentimentExtractorOut3.result,
                                                        obs_column="category",
                                                        sentiment_column="out_polarity"
                                                       )

            # Print the results.
            print(SentimentEvaluatorOut3)

            # Example 4 - This example uses a dictionary table ('sentiment_word')
            #             instead of model file.
            SentimentExtractorOut4 = SentimentExtractor(newdata = sentiment_extract_input,
                                                        dict_data = sentiment_word,
                                                        text_column = "review",
                                                        accumulate = ["category"]
                                                        )

            SentimentEvaluatorOut4 = SentimentEvaluator(object=SentimentExtractorOut4.result,
                                                        obs_column="category",
                                                        sentiment_column="out_polarity"
                                                       )

            # Print the results.
            print(SentimentEvaluatorOut4)
            
        
        """
        self.object  = object 
        self.obs_column  = obs_column 
        self.sentiment_column  = sentiment_column 
        self.object_sequence_column  = object_sequence_column 
        self.object_order_column  = object_order_column 
        
        # Create TeradataPyWrapperUtils instance which contains validation functions.
        self.__awu = AnalyticsWrapperUtils()
        self.__aed_utils = AedUtils()
        
        # Create argument information matrix to do parameter checking
        self.__arg_info_matrix = []
        self.__arg_info_matrix.append(["object", self.object, False, (DataFrame)])
        self.__arg_info_matrix.append(["object_order_column", self.object_order_column, True, (str,list)])
        self.__arg_info_matrix.append(["obs_column", self.obs_column, False, (str)])
        self.__arg_info_matrix.append(["sentiment_column", self.sentiment_column, False, (str)])
        self.__arg_info_matrix.append(["object_sequence_column", self.object_sequence_column, True, (str,list)])
        
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
        if isinstance(self.object, SentimentExtractor):
            self.object = self.object._mlresults[0]
        
        # Make sure that a non-NULL value has been supplied for all mandatory arguments
        self.__awu._validate_missing_required_arguments(self.__arg_info_matrix)
        
        # Make sure that a non-NULL value has been supplied correct type of argument
        self.__awu._validate_argument_types(self.__arg_info_matrix)
        
        # Check to make sure input table types are strings or data frame objects or of valid type.
        self.__awu._validate_input_table_datatype(self.object, "object", SentimentExtractor)
        
        # Check whether the input columns passed to the argument are not empty.
        # Also check whether the input columns passed to the argument valid or not.
        self.__awu._validate_input_columns_not_empty(self.obs_column, "obs_column")
        self.__awu._validate_dataframe_has_argument_columns(self.obs_column, "obs_column", self.object, "object", False)
        
        self.__awu._validate_input_columns_not_empty(self.sentiment_column, "sentiment_column")
        self.__awu._validate_dataframe_has_argument_columns(self.sentiment_column, "sentiment_column", self.object, "object", False)
        
        self.__awu._validate_input_columns_not_empty(self.object_sequence_column, "object_sequence_column")
        self.__awu._validate_dataframe_has_argument_columns(self.object_sequence_column, "object_sequence_column", self.object, "object", False)
        
        self.__awu._validate_input_columns_not_empty(self.object_order_column, "object_order_column")
        self.__awu._validate_dataframe_has_argument_columns(self.object_order_column, "object_order_column", self.object, "object", False)
        
        
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
        
        self.__func_other_arg_sql_names.append("ObservationColumn")
        self.__func_other_args.append(UtilFuncs._teradata_collapse_arglist(UtilFuncs._teradata_quote_arg(self.obs_column,"\""),"'"))
        self.__func_other_arg_json_datatypes.append("COLUMNS")
        
        self.__func_other_arg_sql_names.append("SentimentColumn")
        self.__func_other_args.append(UtilFuncs._teradata_collapse_arglist(UtilFuncs._teradata_quote_arg(self.sentiment_column,"\""),"'"))
        self.__func_other_arg_json_datatypes.append("COLUMNS")
        
        # Generate lists for rest of the function arguments
        sequence_input_by_list = []
        if self.object_sequence_column is not None:
            sequence_input_by_list.append("input:" + UtilFuncs._teradata_collapse_arglist(self.object_sequence_column,""))
        
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
        
        # Process object
        self.__table_ref = self.__awu._teradata_on_clause_from_dataframe(self.object, False)
        self.__func_input_distribution.append("FACT")
        self.__func_input_arg_sql_names.append("input")
        self.__func_input_table_view_query.append(self.__table_ref["ref"])
        self.__func_input_dataframe_type.append(self.__table_ref["ref_type"])
        self.__func_input_partition_by_cols.append("1")
        self.__func_input_order_by_cols.append(UtilFuncs._teradata_collapse_arglist(self.object_order_column,"\""))
        
        function_name = "SentimentEvaluator"
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
        Returns the string representation for a SentimentEvaluator class instance.
        """
        repr_string="############ STDOUT Output ############"
        repr_string = "{}\n\n{}".format(repr_string,self.result)
        return repr_string
        
