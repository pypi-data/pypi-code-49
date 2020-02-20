# -*- coding: utf-8 -*-
"""
Unpublished work.
Copyright (c) 2018 by Teradata Corporation. All rights reserved.
TERADATA CORPORATION CONFIDENTIAL AND TRADE SECRET

Primary Owner: rameshchandra.d@teradata.com
Secondary Owner:
    
teradataml garbage collector module 
----------
The garbage collector functionlity helps to collect & cleanup the temporary 
output tables generated while executing Teradata Vantage analytical functions.

"""
from os.path import expanduser
import teradataml.common as tdmlutil
import teradataml.context as tdmlctx
from teradataml.common.sqlbundle import SQLBundle
from teradataml.common.constants import SQLConstants
from teradataml.common.exceptions import TeradataMlException
from teradataml.common import pylogger
from teradataml.common.messages import Messages
from teradataml.common.messagecodes import MessageCodes
from teradataml.common.constants import TeradataConstants
from teradatasql import OperationalError
import psutil
import getpass
import os

logger = pylogger.getLogger()

class GarbageCollector():

    """
    The class has functionality to add temporary tables/views to garbage collection, 
    so that they can be dropped when connection is disconnected/lost.
    Writes to a output file where the database name & table/view names are persisted.
    """
    __garbage_persistent_file_name = getpass.getuser() + "_garbagecollect.info"
    __garbagecollector_folder_name = ".teradataml"
    __contentseperator = ","
    __version = "ver1.0"

    @staticmethod
    def __make_temp_file_name():
        """
        Builds the temp directory where the garbage collector file will be persisted.
        
        PARAMETERS:
            None.
    
        RETURNS:
            Garbage collector temporary file name.
    
        RAISES:
            None.
    
        EXAMPLES:
            GarbageCollector.__build_temp_directory()
        """
        tempdir = expanduser("~")
        tempdir = os.path.join(tempdir, GarbageCollector.__garbagecollector_folder_name)
        os.makedirs(tempdir, exist_ok=True)
        tempfile = os.path.join(os.path.sep, tempdir, GarbageCollector.__garbage_persistent_file_name)
        return tempfile
    
    @staticmethod
    def _add_to_garbagecollector(tableorviewname, tabletype = TeradataConstants.TERADATA_TABLE):
        """
        Add databasename & temporary table/view name to the garbage collector.
        
        PARAMETERS:
            tableorviewname:
                Required Argument.
                Name of the temporary table/view name along with database name
                that needs to be garbage collected.

            tabletype:
                Optional Argument.
                Specifies the type of object to be added to Garbage Collector.
                Default Values: TeradataConstants.TERADATA_TABLE
    
        RETURNS:
            True/False
    
        RAISES:
            None.
    
        EXAMPLES:
            GarbageCollector._add_to_garbagecollector(tableorviewname = "temp"."temp_table1")
        """
        if tableorviewname and tabletype:
            try:
                tempfilename = GarbageCollector.__make_temp_file_name()
                writecontent = str(GarbageCollector.__version) + "," + str(os.getpid())
                if tabletype is TeradataConstants.TERADATA_TABLE:
                    writecontent+="," + str(TeradataConstants.TERADATA_TABLE.value)
                else:
                    writecontent+="," + str(TeradataConstants.TERADATA_VIEW.value)
                writecontent+="," + tableorviewname + "\n"
                with open(tempfilename, 'a+') as fgc:
                    fgc.write(writecontent)
            except TeradataMlException:
                raise
            except Exception as err:
                logger.error(Messages.get_message(MessageCodes.TDMLDF_CREATE_GARBAGE_COLLECTOR) + str(err))
                raise TeradataMlException(Messages.get_message(MessageCodes.TDMLDF_CREATE_GARBAGE_COLLECTOR), MessageCodes.TDMLDF_CREATE_GARBAGE_COLLECTOR) from err
            finally:
                if fgc is not None:
                    fgc.close()         
        return True
    
    @staticmethod
    def _deleterow(table_view_to_delete):
        """
        Deletes an entry of table or viewname from persisted file.
        
        PARAMETERS:
            table_view_to_delete - Name of the table/view to be deleted
    
        RETURNS:
            None
    
        RAISES:
            None.
    
        EXAMPLES:
            GarbageCollector._deleterow(table_view_to_delete = 'temp.temp_table1')
        """
        try:
            tempfilename = GarbageCollector.__make_temp_file_name()
            if not os.path.isfile(tempfilename):
                return True
            with open(tempfilename, 'r+') as fgc:
                output = fgc.readlines()
                fgc.seek(0)
                for dbtablename in output:
                    if table_view_to_delete != dbtablename.strip():
                        fgc.write(dbtablename)
                fgc.truncate()
        except Exception as e:
            raise
        finally:
            if fgc and fgc is not None:
                fgc.close()

    @staticmethod
    def _delete_table_view_entry(table_view_to_delete):
        """
        Deletes an entry of table or viewname from persisted file.

        PARAMETERS:
            table_view_to_delete - Name of the table/view to be deleted

        RETURNS:
            None

        RAISES:
            None.

        EXAMPLES:
            GarbageCollector._delete_table_view_entry(table_view_to_delete = 'temp.temp_table1')
        """
        try:
            tempfilename = GarbageCollector.__make_temp_file_name()
            if not os.path.isfile(tempfilename):
                return True
            with open(tempfilename, 'r+') as fgc:
                output = fgc.readlines()
                fgc.seek(0)
                for dbtablename in output:
                    if not (table_view_to_delete in dbtablename.strip() and str(os.getpid()) in dbtablename.strip()):
                        fgc.write(dbtablename)
                fgc.truncate()
        except Exception as e:
            raise
        finally:
            if fgc and fgc is not None:
                fgc.close()

    @staticmethod
    def _cleanup_garbage_collector():
        """
        Drops the tables/views that are garbage collected.
        
        PARAMETERS:
            None
    
        RETURNS:
            True/False
    
        RAISES:
            None.
    
        EXAMPLES:
            GarbageCollector._cleanup_garbage_collector()
        """
        try:
            td_connection = tdmlctx.context.get_connection()
            tempfilename = GarbageCollector.__make_temp_file_name()
            if not os.path.isfile(tempfilename):
                return True
            with open(tempfilename, 'r+') as fgc:
                content = fgc.readlines()
            sqlbundle = SQLBundle()
            for contentrecord in content:
                contentrecord = contentrecord.strip()
                if (td_connection is not None) and (len(contentrecord) > 0):
                    try:
                        recordparts = contentrecord.split(GarbageCollector.__contentseperator)
                        version = recordparts[0]
                        contentpid = recordparts[1]
                        # Check and garbage collect even currrent running process at exit.
                        # Check if contentpid is not of current process as well as any
                        # currently running process in the system
                        proceed_to_cleanup = False
                        if (int(contentpid) != int(os.getpid())):
                            if not psutil.pid_exists(int(contentpid)):
                                proceed_to_cleanup = True
                        else:
                            proceed_to_cleanup = True
                        if (proceed_to_cleanup == True):
                            tabletype = recordparts[2]
                            databaseobject = recordparts[3]
                            try:
                                # Drop the table or view based on database object type retreived from the collector file.
                                if (TeradataConstants.TERADATA_TABLE.value == int(tabletype.strip())):
                                    tdmlutil.utils.UtilFuncs._drop_table(databaseobject.strip(), check_table_exist = False)
                                else:
                                    tdmlutil.utils.UtilFuncs._drop_view(databaseobject.strip(), check_view_exist = False)
                                # Remove the entry for a table/view from GC, after it has been dropped.
                                GarbageCollector._deleterow(contentrecord)
                            except OperationalError as operr:
                                # Remove the entry for a table/view even after drop has failed,
                                # if that object does not exist.
                                if "[Teradata Database] [Error 3807] Object" in str(operr):
                                    GarbageCollector._deleterow(contentrecord)
                                pass
                    except Exception as err:
                        pass
                        #logger.error(Messages.get_message(MessageCodes.TDMLDF_DELETE_GARBAGE_COLLECTOR) + str(err))
        except Exception as e:
            logger.error(Messages.get_message(MessageCodes.TDMLDF_DELETE_GARBAGE_COLLECTOR) + str(e))
        return True