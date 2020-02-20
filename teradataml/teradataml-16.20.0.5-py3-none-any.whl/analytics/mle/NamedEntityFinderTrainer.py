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
# Function Version: 1.7
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

class NamedEntityFinderTrainer:
    
    def __init__(self,
        data = None,
        text_column = None,
        entity_type = None,
        model = None,
        iter_num = 100,
        cutoff = 5,
        data_sequence_column = None):
        """
        DESCRIPTION:
            The NamedEntityFinderTrainer function takes training data and outputs
            a Max Entropy data model. The function is based on OpenNLP, and
            follows its annotation. For more information on OpenNLP, see
            https://opennlp.apache.org/docs/1.8.4/manual/opennlp.html.

            The trainer supports only the English language.

        PARAMETERS:
            data:
                Required Argument.
                Specifies the input teradataml DataFrame containing text column
                to train.

            text_column:
                Required Argument.
                Specifies the name of the input teradataml DataFrame column that
                contains the text to analyze.
                Types: str

            entity_type:
                Required Argument.
                Specifies the entity type to be trained (for example, PERSON). The
                input training documents must contain the same tag.
                Types: str

            model:
                Required Argument.
                Specifies the name of the data model file to be generated.
                Types: str

            iter_num:
                Optional Argument.
                Specifies the iterator number for training (an openNLP training
                parameter).
                Default Value: 100
                Types: int

            cutoff:
                Optional Argument.
                Specifies the cutoff number for training (an openNLP training
                parameter).
                Default Value: 5
                Types: int

            data_sequence_column:
                Optional Argument.
                Specifies the list of column(s) that uniquely identifies each row of
                the input argument "data". The argument is used to ensure
                deterministic results for functions which produce results that vary
                from run to run.
                Types: str OR list of Strings (str)

        RETURNS:
            Instance of NamedEntityFinderTrainer.
            Output teradataml DataFrames can be accessed using attribute
            references, such as NamedEntityFinderTrainerObj.<attribute_name>.
            Output teradataml DataFrame attribute name is:
                result


        RAISES:
            TeradataMlException


        EXAMPLES:
            # Load example data.
            load_example_data('namedentityfindertrainer', 'nermem_sports_train')

            # Provided example table is 'nermem_sports_train'. It contains two columns - 'id' and
            # 'content'. 'content' column contains the training text data.

            # Create teradataml DataFrame objects.
            nermem_sports_train = DataFrame.from_table('nermem_sports_train')

            # Example 1: Train a NamedEntityFinder model on entity type: "LOCATION".
            #            The trained model is stored in a binary file: "location.sports"
            NamedEntityFinderTrainer_out = NamedEntityFinderTrainer(data=nermem_sports_train,
                                                                    text_column='content',
                                                                    entity_type='LOCATION',
                                                                    model='location.sports',
                                                                    cutoff=5,
                                                                    data_sequence_column='id')
            # Print the results
            print(NamedEntityFinderTrainer_out.result)
        
        """
        self.data  = data 
        self.text_column  = text_column 
        self.entity_type  = entity_type 
        self.model  = model 
        self.iter_num  = iter_num 
        self.cutoff  = cutoff 
        self.data_sequence_column  = data_sequence_column 
        
        # Create TeradataPyWrapperUtils instance which contains validation functions.
        self.__awu = AnalyticsWrapperUtils()
        self.__aed_utils = AedUtils()
        
        # Create argument information matrix to do parameter checking
        self.__arg_info_matrix = []
        self.__arg_info_matrix.append(["data", self.data, False, (DataFrame)])
        self.__arg_info_matrix.append(["text_column", self.text_column, False, (str)])
        self.__arg_info_matrix.append(["entity_type", self.entity_type, False, (str)])
        self.__arg_info_matrix.append(["model", self.model, False, (str)])
        self.__arg_info_matrix.append(["iter_num", self.iter_num, True, (int)])
        self.__arg_info_matrix.append(["cutoff", self.cutoff, True, (int)])
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
        self.__awu._validate_input_columns_not_empty(self.text_column, "text_column")
        self.__awu._validate_dataframe_has_argument_columns(self.text_column, "text_column", self.data, "data", False)
        
        self.__awu._validate_input_columns_not_empty(self.data_sequence_column, "data_sequence_column")
        self.__awu._validate_dataframe_has_argument_columns(self.data_sequence_column, "data_sequence_column", self.data, "data", False)
        
        
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
        
        self.__func_other_arg_sql_names.append("EntityType")
        self.__func_other_args.append(UtilFuncs._teradata_collapse_arglist(self.entity_type,"'"))
        self.__func_other_arg_json_datatypes.append("STRING")
        
        self.__func_other_arg_sql_names.append("Model")
        self.__func_other_args.append(UtilFuncs._teradata_collapse_arglist(self.model,"'"))
        self.__func_other_arg_json_datatypes.append("STRING")
        
        if self.iter_num is not None and self.iter_num != 100:
            self.__func_other_arg_sql_names.append("IterNum")
            self.__func_other_args.append(UtilFuncs._teradata_collapse_arglist(self.iter_num,"'"))
            self.__func_other_arg_json_datatypes.append("INTEGER")
        
        if self.cutoff is not None and self.cutoff != 5:
            self.__func_other_arg_sql_names.append("Cutoff")
            self.__func_other_args.append(UtilFuncs._teradata_collapse_arglist(self.cutoff,"'"))
            self.__func_other_arg_json_datatypes.append("INTEGER")
        
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
        self.__func_input_partition_by_cols.append("1")
        self.__func_input_order_by_cols.append("NA_character_")
        
        function_name = "NamedEntityFinderTrainer"
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
            UtilFuncs._create_table(sqlmr_stdout_temp_tablename, self.sqlmr_query)
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
        Returns the string representation for a NamedEntityFinderTrainer class instance.
        """
        repr_string="############ STDOUT Output ############"
        repr_string = "{}\n\n{}".format(repr_string,self.result)
        return repr_string
        
