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

class RandomWalkSample:
    
    def __init__(self,
        vertices_data = None,
        edges_data = None,
        target_key = None,
        sample_rate = 0.15,
        flyback_rate = 0.15,
        seed = 1000,
        accumulate = None,
        vertices_data_sequence_column = None,
        edges_data_sequence_column = None,
        vertices_data_partition_column = None,
        edges_data_partition_column = None):
        """
        DESCRIPTION:
            The RandomWalkSample function takes an input graph (which is typically
            large) and outputs a sample graph.


        PARAMETERS:
            vertices_data:
                Required Argument.
                Specifies the teradataml DataFrame containing the vertex table.

            vertices_data_partition_column:
                Required Argument.
                Specifies Partition By columns for vertices_data.
                Values to this argument can be provided as list, if multiple
                columns are used for partition.
                Types: str OR list of Strings (str)

            edges_data:
                Required Argument.
                Specifies the teradataml DataFrame containing the edge table.

            edges_data_partition_column:
                Required Argument.
                Specifies Partition By columns for edges_data.
                Values to this argument can be provided as list, if multiple
                columns are used for partition.
                Types: str OR list of Strings (str)

            target_key:
                Required Argument.
                Specifies the names of the columns in the edges teradataml DataFrame that
                identify the target vertex of an edge.
                Types: str OR list of Strings (str)

            sample_rate:
                Optional Argument.
                Specifies the sampling rate. This value must be in the range (0, 1.0).
                Default Value: 0.15
                Types: float

            flyback_rate:
                Optional Argument.
                Specifies the chance, when visiting a vertex, of flying back to the starting
                vertex. This value must be in the range (0, 1.0).
                Default Value: 0.15
                Types: float

            seed:
                Optional Argument.
                Specifies the seed used to generate a series of random numbers
                for sample_rate, flyback_rate, and any random number used
                internally. Specifying this value guarantees that the function
                result is repeatable on the same cluster.
                Default Value: 1000
                Types: int

            accumulate:
                Optional Argument.
                Specifies the names of columns in the input vertex teradataml DataFrame
                to copy to the output vertex teradataml DataFrame.
                Types: str OR list of Strings (str)

            vertices_data_sequence_column:
                Optional Argument.
                Specifies the list of column(s) that uniquely identifies each row of
                the input argument "vertices_data". The argument is used to ensure
                deterministic results for functions which produce results that vary
                from run to run.
                Types: str OR list of Strings (str)

            edges_data_sequence_column:
                Optional Argument.
                Specifies the list of column(s) that uniquely identifies each row of
                the input argument "edges_data". The argument is used to ensure
                deterministic results for functions which produce results that vary
                from run to run.
                Types: str OR list of Strings (str)

        RETURNS:
            Instance of RandomWalkSample.
            Output teradataml DataFrames can be accessed using attribute
            references, such as RandomWalkSampleObj.<attribute_name>.
            Output teradataml DataFrame attribute names are:
                1. output_vertex_table
                2. output_edge_table
                3. output


        RAISES:
            TeradataMlException


        EXAMPLES:
            # Load example data.
            load_example_data("randomwalksample", ["citvertices_2", "citedges_2"])

            # Create teradataml DataFrame objects.
            # The RandomWalkSample function has two required input tables:
            #   • Vertices, which defines the set of vertices in the input graph.
            #   • Edges, which defines the set of edges in the input graph.
            citvertices_2 = DataFrame.from_table("citvertices_2")
            citedges_2 = DataFrame.from_table("citedges_2")

            # Example 1 - This function takes an input graph (which is typically
            # large) and outputs a sample graph that preserves graph properties.
            RandomWalkSample_out = RandomWalkSample(vertices_data = citvertices_2,
                                                    vertices_data_partition_column = ["id"],
                                                    edges_data = citedges_2,
                                                    edges_data_partition_column = ["from_id"],
                                                    target_key = ["to_id"],
                                                    sample_rate = 0.15,
                                                    flyback_rate = 0.15,
                                                    seed = 1000
                                                    )

            # Print the result DataFrame
            print(RandomWalkSample_out)
        
        """
        self.vertices_data  = vertices_data 
        self.edges_data  = edges_data 
        self.target_key  = target_key 
        self.sample_rate  = sample_rate 
        self.flyback_rate  = flyback_rate 
        self.seed  = seed 
        self.accumulate  = accumulate 
        self.vertices_data_sequence_column  = vertices_data_sequence_column 
        self.edges_data_sequence_column  = edges_data_sequence_column 
        self.vertices_data_partition_column  = vertices_data_partition_column 
        self.edges_data_partition_column  = edges_data_partition_column 
        
        # Create TeradataPyWrapperUtils instance which contains validation functions.
        self.__awu = AnalyticsWrapperUtils()
        self.__aed_utils = AedUtils()
        
        # Create argument information matrix to do parameter checking
        self.__arg_info_matrix = []
        self.__arg_info_matrix.append(["vertices_data", self.vertices_data, False, (DataFrame)])
        self.__arg_info_matrix.append(["vertices_data_partition_column", self.vertices_data_partition_column, False, (str,list)])
        self.__arg_info_matrix.append(["edges_data", self.edges_data, False, (DataFrame)])
        self.__arg_info_matrix.append(["edges_data_partition_column", self.edges_data_partition_column, False, (str,list)])
        self.__arg_info_matrix.append(["target_key", self.target_key, False, (str,list)])
        self.__arg_info_matrix.append(["sample_rate", self.sample_rate, True, (float)])
        self.__arg_info_matrix.append(["flyback_rate", self.flyback_rate, True, (float)])
        self.__arg_info_matrix.append(["seed", self.seed, True, (int)])
        self.__arg_info_matrix.append(["accumulate", self.accumulate, True, (str,list)])
        self.__arg_info_matrix.append(["vertices_data_sequence_column", self.vertices_data_sequence_column, True, (str,list)])
        self.__arg_info_matrix.append(["edges_data_sequence_column", self.edges_data_sequence_column, True, (str,list)])
        
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
        self.__awu._validate_input_table_datatype(self.vertices_data, "vertices_data", None)
        self.__awu._validate_input_table_datatype(self.edges_data, "edges_data", None)
        
        # Check whether the input columns passed to the argument are not empty.
        # Also check whether the input columns passed to the argument valid or not.
        self.__awu._validate_input_columns_not_empty(self.target_key, "target_key")
        self.__awu._validate_dataframe_has_argument_columns(self.target_key, "target_key", self.edges_data, "edges_data", False)
        
        self.__awu._validate_input_columns_not_empty(self.accumulate, "accumulate")
        self.__awu._validate_dataframe_has_argument_columns(self.accumulate, "accumulate", self.vertices_data, "vertices_data", False)
        
        self.__awu._validate_input_columns_not_empty(self.vertices_data_sequence_column, "vertices_data_sequence_column")
        self.__awu._validate_dataframe_has_argument_columns(self.vertices_data_sequence_column, "vertices_data_sequence_column", self.vertices_data, "vertices_data", False)
        
        self.__awu._validate_input_columns_not_empty(self.edges_data_sequence_column, "edges_data_sequence_column")
        self.__awu._validate_dataframe_has_argument_columns(self.edges_data_sequence_column, "edges_data_sequence_column", self.edges_data, "edges_data", False)
        
        self.__awu._validate_input_columns_not_empty(self.vertices_data_partition_column, "vertices_data_partition_column")
        self.__awu._validate_dataframe_has_argument_columns(self.vertices_data_partition_column, "vertices_data_partition_column", self.vertices_data, "vertices_data", False)
        
        self.__awu._validate_input_columns_not_empty(self.edges_data_partition_column, "edges_data_partition_column")
        self.__awu._validate_dataframe_has_argument_columns(self.edges_data_partition_column, "edges_data_partition_column", self.edges_data, "edges_data", False)
        
        
    def __form_tdml_query(self):
        """
        Function to generate the analytical function queries. The function defines 
        variables and list of arguments required to form the query.
        """
        # Generate temp table names for output table parameters if any.
        self.__output_vertex_table_temp_tablename = UtilFuncs._generate_temp_table_name(prefix = "td_randomwalksample0", use_default_database = True, gc_on_quit = True, quote=False, table_type = TeradataConstants.TERADATA_TABLE)
        self.__output_edge_table_temp_tablename = UtilFuncs._generate_temp_table_name(prefix = "td_randomwalksample1", use_default_database = True, gc_on_quit = True, quote=False, table_type = TeradataConstants.TERADATA_TABLE)
        
        # Output table arguments list
        self.__func_output_args_sql_names = ["VertexOutputTable", "EdgeOutputTable"]
        self.__func_output_args = [self.__output_vertex_table_temp_tablename, self.__output_edge_table_temp_tablename]
        
        # Generate lists for rest of the function arguments
        self.__func_other_arg_sql_names = []
        self.__func_other_args = []
        self.__func_other_arg_json_datatypes = []
        
        self.__func_other_arg_sql_names.append("TargetKey")
        self.__func_other_args.append(UtilFuncs._teradata_collapse_arglist(UtilFuncs._teradata_quote_arg(self.target_key,"\""),"'"))
        self.__func_other_arg_json_datatypes.append("COLUMNS")
        
        if self.accumulate is not None:
            self.__func_other_arg_sql_names.append("Accumulate")
            self.__func_other_args.append(UtilFuncs._teradata_collapse_arglist(UtilFuncs._teradata_quote_arg(self.accumulate,"\""),"'"))
            self.__func_other_arg_json_datatypes.append("COLUMNS")
        
        if self.sample_rate is not None and self.sample_rate != 0.15:
            self.__func_other_arg_sql_names.append("SampleRate")
            self.__func_other_args.append(UtilFuncs._teradata_collapse_arglist(self.sample_rate,"'"))
            self.__func_other_arg_json_datatypes.append("DOUBLE")
        
        if self.flyback_rate is not None and self.flyback_rate != 0.15:
            self.__func_other_arg_sql_names.append("FlybackRate")
            self.__func_other_args.append(UtilFuncs._teradata_collapse_arglist(self.flyback_rate,"'"))
            self.__func_other_arg_json_datatypes.append("DOUBLE")
        
        if self.seed is not None and self.seed != 1000:
            self.__func_other_arg_sql_names.append("Seed")
            self.__func_other_args.append(UtilFuncs._teradata_collapse_arglist(self.seed,"'"))
            self.__func_other_arg_json_datatypes.append("LONG")
        
        # Generate lists for rest of the function arguments
        sequence_input_by_list = []
        if self.vertices_data_sequence_column is not None:
            sequence_input_by_list.append("vertices:" + UtilFuncs._teradata_collapse_arglist(self.vertices_data_sequence_column,""))
        
        if self.edges_data_sequence_column is not None:
            sequence_input_by_list.append("edges:" + UtilFuncs._teradata_collapse_arglist(self.edges_data_sequence_column,""))
        
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
        
        # Process vertices_data
        vertices_data_partition_column = UtilFuncs._teradata_collapse_arglist(self.vertices_data_partition_column,"\"")
        self.__table_ref = self.__awu._teradata_on_clause_from_dataframe(self.vertices_data, False)
        self.__func_input_distribution.append("FACT")
        self.__func_input_arg_sql_names.append("vertices")
        self.__func_input_table_view_query.append(self.__table_ref["ref"])
        self.__func_input_dataframe_type.append(self.__table_ref["ref_type"])
        self.__func_input_partition_by_cols.append(vertices_data_partition_column)
        self.__func_input_order_by_cols.append("NA_character_")
        
        # Process edges_data
        edges_data_partition_column = UtilFuncs._teradata_collapse_arglist(self.edges_data_partition_column,"\"")
        self.__table_ref = self.__awu._teradata_on_clause_from_dataframe(self.edges_data, False)
        self.__func_input_distribution.append("FACT")
        self.__func_input_arg_sql_names.append("edges")
        self.__func_input_table_view_query.append(self.__table_ref["ref"])
        self.__func_input_dataframe_type.append(self.__table_ref["ref_type"])
        self.__func_input_partition_by_cols.append(edges_data_partition_column)
        self.__func_input_order_by_cols.append("NA_character_")
        
        function_name = "RandomWalkSample"
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
        self.output_vertex_table = self.__awu._create_data_set_object(df_input=UtilFuncs._extract_table_name(self.__output_vertex_table_temp_tablename), source_type="table", database_name=UtilFuncs._extract_db_name(self.__output_vertex_table_temp_tablename))
        self.output_edge_table = self.__awu._create_data_set_object(df_input=UtilFuncs._extract_table_name(self.__output_edge_table_temp_tablename), source_type="table", database_name=UtilFuncs._extract_db_name(self.__output_edge_table_temp_tablename))
        self.output = self.__awu._create_data_set_object(df_input=UtilFuncs._extract_table_name(sqlmr_stdout_temp_tablename), source_type="table", database_name=UtilFuncs._extract_db_name(sqlmr_stdout_temp_tablename))
        self._mlresults.append(self.output_vertex_table)
        self._mlresults.append(self.output_edge_table)
        self._mlresults.append(self.output)
        
    @classmethod
    def _from_model_manager(cls,
        output_vertex_table = None,
        output_edge_table = None,
        output = None,
        **kwargs):
        """
        Classmethod which will be used by Model Manager, to instantiate this wrapper class.
        """
        kwargs.pop("output_vertex_table", None)
        kwargs.pop("output_edge_table", None)
        kwargs.pop("output", None)
        
        # Let's create an object of this class.
        obj = cls(**kwargs)
        obj.output_vertex_table  = output_vertex_table 
        obj.output_edge_table  = output_edge_table 
        obj.output  = output 
        
        # Update output table data frames.
        obj._mlresults = []
        obj.output_vertex_table = obj.__awu._create_data_set_object(df_input=UtilFuncs._extract_table_name(obj.output_vertex_table), source_type="table", database_name=UtilFuncs._extract_db_name(obj.output_vertex_table))
        obj.output_edge_table = obj.__awu._create_data_set_object(df_input=UtilFuncs._extract_table_name(obj.output_edge_table), source_type="table", database_name=UtilFuncs._extract_db_name(obj.output_edge_table))
        obj.output = obj.__awu._create_data_set_object(df_input=UtilFuncs._extract_table_name(obj.output), source_type="table", database_name=UtilFuncs._extract_db_name(obj.output))
        obj._mlresults.append(obj.output_vertex_table)
        obj._mlresults.append(obj.output_edge_table)
        obj._mlresults.append(obj.output)
        return obj
        
    def __repr__(self):
        """
        Returns the string representation for a RandomWalkSample class instance.
        """
        repr_string="############ STDOUT Output ############"
        repr_string = "{}\n\n{}".format(repr_string,self.output)
        repr_string="{}\n\n\n############ output_vertex_table Output ############".format(repr_string)
        repr_string = "{}\n\n{}".format(repr_string,self.output_vertex_table)
        repr_string="{}\n\n\n############ output_edge_table Output ############".format(repr_string)
        repr_string = "{}\n\n{}".format(repr_string,self.output_edge_table)
        return repr_string
        
