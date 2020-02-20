# -*- coding: utf-8 -*-
"""
Unpublished work.
Copyright (c) 2018 by Teradata Corporation. All rights reserved.
TERADATA CORPORATION CONFIDENTIAL AND TRADE SECRET

Primary Owner: rameshchandra.d@teradata.com
Secondary Owner:

teradataml context
----------
A teradataml context functions provide interface to Teradata Vantage. Provides functionality to get and set a global context which
can be used by other analytical functions to get the Teradata Vantage connection.

"""
from sqlalchemy import create_engine
from teradataml.common.exceptions import TeradataMlException
from teradataml.common.messages import Messages
from teradataml.common.messagecodes import MessageCodes
from teradataml.common.sqlbundle import SQLBundle
from teradataml.common.constants import SQLConstants
from teradataml.common.garbagecollector import GarbageCollector
from teradataml.context.aed_context import AEDContext
from teradataml.common.constants import TeradataConstants
from teradataml.common.utils import UtilFuncs
from teradataml.options.configure import configure
from teradataml.utils.validators import _Validators
from sqlalchemy.engine.base import Engine
import os
import warnings
import atexit

# Store an global Teradata Vantage Connection.
# Right now user can only provide an single Vantage connection at any point of time.
td_connection = None
td_sqlalchemy_engine = None
temporary_database_name = None
user_specified_connection = False

function_alias_mappings = {}

# Current directory is context folder.
teradataml_folder = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
config_folder = os.path.join(teradataml_folder, "config")

def _get_current_databasename():
    """
    Returns the database name associated with the current context.

    PARAMETERS:
        None.

    RETURNS:
        Database name associated with the current context

    RAISES:
        TeradataMlException - If Vantage connection can't be established using the engine.

    EXAMPLES:
        _get_current_databasename()
    """
    if get_connection() is not None:
        try:
            sqlbundle = SQLBundle()
            select_user_query = sqlbundle._get_sql_query(SQLConstants.SQL_SELECT_DATABASE)
            result = get_connection().execute(select_user_query)
            for row in result:
                return row[0]
        except TeradataMlException:
            raise
        except Exception as err:
            raise TeradataMlException(Messages.get_message(MessageCodes.TDMLDF_EXEC_SQL_FAILED, select_user_query),
                                      MessageCodes.TDMLDF_EXEC_SQL_FAILED) from err
    else:
        return None

def _get_database_username():
    """
    Function to get the database user name.

    PARAMETERS:
        None.

    RETURNS:
        Database user name.

    RAISES:
        TeradataMlException - If "select user" query fails.

    EXAMPLES:
        _get_database_username()
    """
    if get_connection() is not None:
        try:
            sqlbundle = SQLBundle()
            select_query = sqlbundle._get_sql_query(SQLConstants.SQL_SELECT_USER)
            result = get_connection().execute(select_query)
            for row in result:
                return row[0]
        except TeradataMlException:
            raise
        except Exception as err:
            raise TeradataMlException(Messages.get_message(MessageCodes.TDMLDF_EXEC_SQL_FAILED, select_query),
                                      MessageCodes.TDMLDF_EXEC_SQL_FAILED) from err
    else:
        return None

def __cleanup_garbage_collection():
    """initiate the garbage collection."""
    GarbageCollector._cleanup_garbage_collector()

def create_context(host = None, username = None, password = None,  tdsqlengine = None,
                   temp_database_name = None, logmech = None, logdata = None):
    """
    DESCRIPTION:
        Creates a connection to the Teradata Vantage using the teradatasql + teradatasqlalchemy DBAPI and dialect combination.
        Users can pass all required parameters (host, username, password) for establishing a connection to Vantage,
        or pass a sqlalchemy engine to the tdsqlengine parameter to override the default DBAPI and dialect combination.

    PARAMETERS:
        host:
            Optional Argument.
            Specifies the fully qualified domain name or IP address of the Teradata System.
            Types: str
        
        username:
            Optional Argument.
            Specifies the username for logging onto the Teradata Vantage.
            Types: str
        
        password:
            Optional Argument.
            Specifies the password required for the username.
            Types: str
            Note:
                Encrypted passwords can also be passed to this argument, using Stored Password Protection feature. 
                Examples section below demonstrates passing encrypted password to 'create_context'.
                More details on Stored Password Protection and how to generate key and encrypted password file 
                can be found at https://pypi.org/project/teradatasql/#StoredPasswordProtection
            
        tdsqlengine:
            Optional Argument.
            Specifies Teradata Vantage sqlalchemy engine object that should be used to establish a Teradata Vantage connection.
            Types: str
            
        temp_database_name:
            Optional Argument.
            Specifies the temporary database name where temporary tables, views will be created.
            Types: str
            
        logmech:
            Optional Argument.
            Specifies the type of logon mechanism to establish a connection to Teradata Vantage. 
            Permitted Values: 'TD2', 'TDNEGO', 'LDAP', 'KRB5' & 'JWT'.
                TD2: 
                    The Teradata 2 (TD2) mechanism provides authentication using a 
                    Vantage username and password. This is the default logon mechanism
                    using which the connection is established to Vantage.
                TDNEGO:
                    A security mechanism that automatically determines the actual 
                    mechanism required, based on policy, without user's involvement.
                    The actual mechanism is determined by the TDGSS server configuration
                    and by the security policy's mechanism restrictions.
                LDAP:
                    A directory-based user logon to Vantage with a directory username
                    and password and is authenticated by the directory.
                KRB5 (Kerberos):
                    A directory-based user logon to Vantage with a domain username
                    and password and is authenticated by Kerberos (KRB5 mechanism).
                JWT: 
                    The JSON Web Token (JWT) authentication mechanism enables single 
                    sign-on (SSO) to the Vantage after the user successfully authenticates
                    to Teradata UDA User Service.
            Types: str

            Note:
                teradataml expects the client environments are already setup with appropriate
                security mechanisms and are in working conditions.
                For more information please refer Teradata Vantage™ - Advanced SQL Engine
                Security Administration at https://www.info.teradata.com/
        
        logdata:
            Optional Argument.
            Specifies parameters to the LOGMECH command beyond those needed by the logon mechanism, such as 
            user ID, password and tokens (in case of JWT) to successfully authenticate the user.
            Types: str
            Note:
                Password passed as part of logdata can also be in encrypted format using Stored Password 
                Protection. Example section below demonstrates passing encrypted password to logdata parameter.
                More details on Stored Password Protection and how to generate key and encrypted password file 
                can be found at https://pypi.org/project/teradatasql/#StoredPasswordProtection

    RETURNS:
        A Teradata sqlalchemy engine object.

    RAISES:
        TeradataMlException

    EXAMPLES:
        >>> from teradataml.context.context import *

        >>> # Example 1: Create context using hostname, username and password
        >>> td_context = create_context(host = 'tdhost', username='tduser', password = 'tdpassword')

        >>> # Example 2: Create context using already created sqlalchemy engine
        >>> from sqlalchemy import create_engine
        >>> sqlalchemy_engine  = create_engine('teradatasql://'+ tduser +':' + tdpassword + '@'+tdhost)
        >>> td_context = create_context(tdsqlengine = sqlalchemy_engine)

        >>> # Example 3: Creating context for Vantage with default logmech 'TD2'
        >>> td_context = create_context(host = 'tdhost', username='tduser', password = 'tdpassword', logmech='TD2')

        >>> # Example 4: Creating context for Vantage with logmech as 'TDNEGO'
        >>> td_context = create_context(host = 'tdhost', username='tduser', password = 'tdpassword', logmech='TDNEGO')

        >>> # Example 5: Creating context for Vantage with logmech as 'LDAP'
        >>> td_context = create_context(host = 'tdhost', username='tduser', password = 'tdpassword', logmech='LDAP')

        >>> # Example 6: Creating context for Vantage with logmech as 'KRB5'
        >>> td_context = create_context(host = 'tdhost', username='tduser', password = 'tdpassword', logmech='KRB5')

        >>> # Example 7: Creating context for Vantage with logmech as 'JWT'
        >>> td_context = create_context(host = 'tdhost', logmech='JWT', logdata='token=eyJpc...h8dA')

        Note: User must use logdata parameter when using 'JWT' as logging mechanism.

        >>> # Example 8: Create context using encrypted password and key passed to 'password' parameter.
        >>> # The password should be specified in the format mentioned below:
        >>> # ENCRYPTED_PASSWORD(file:<PasswordEncryptionKeyFileName>, file:<EncryptedPasswordFileName>)
        >>> # The PasswordEncryptionKeyFileName specifies the name of a file that contains the password encryption key
        >>> # and associated information.
        >>> # The EncryptedPasswordFileName specifies the name of a file that contains the encrypted password and
        >>> # associated information.
        >>> # Each filename must be preceded by the 'file:' prefix. The PasswordEncryptionKeyFileName must be separated
        >>> # from the EncryptedPasswordFileName by a single comma.
        >>> td_context = create_context(host = 'tdhost', username='tduser',
                                        password = "ENCRYPTED_PASSWORD(file:PassKey.properties, file:EncPass.properties)")

        >>> # Example 9: Create context using encrypted password and key passed to 'logdata' parameter.
        >>> from sqlalchemy import create_engine
        >>> sqlalchemy_engine = create_engine("teradatasql://@tdhost/?LOGMECH=LDAP&"
                                              "LOGDATA=tduser@@ENCRYPTED_PASSWORD(file:PassKey.properties,file:EncPass.properties)")
        >>> td_context = create_context(tdsqlengine = sqlalchemy_engine)

    """
    global td_connection
    global td_sqlalchemy_engine
    global temporary_database_name
    global user_specified_connection
    logmech_valid_values = ['TD2','TDNEGO','LDAP','KRB5','JWT']
    logmech_value = ""
    logdata_value = ""
    awu_matrix = []
    awu_matrix.append(["host", host, True , (str), True])
    awu_matrix.append(["username", username, True , (str), True])
    awu_matrix.append(["password", password, True , (str), True])
    awu_matrix.append(["tdsqlengine", tdsqlengine, True , (Engine)])
    awu_matrix.append(["logmech", logmech, True , (str), True, logmech_valid_values])
    awu_matrix.append(["logdata", logdata, True , (str)])
    
    awu = _Validators()
    awu._validate_function_arguments(awu_matrix)

    # Check if teradata sqlalchemy engine is provided by the user    
    if tdsqlengine:
        try:
            if td_connection is not None:
                warnings.warn(Messages.get_message(MessageCodes.OVERWRITE_CONTEXT))
                remove_context()
            td_connection = tdsqlengine.connect()
            td_sqlalchemy_engine = tdsqlengine
            user_specified_connection = True
        except TeradataMlException:
            raise
        except Exception as err:
            raise TeradataMlException(Messages.get_message(MessageCodes.CONNECTION_FAILURE), MessageCodes.CONNECTION_FAILURE) from err
    # Check if host and username and password are provided
    elif host and username and password:
        try:
            if td_connection is not None:
                warnings.warn(Messages.get_message(MessageCodes.OVERWRITE_CONTEXT))
                remove_context()
            if logmech is not None:
                logmech_value = '/?LOGMECH=' + logmech.upper()
                if logdata is not None:
                    logdata_value = '&LOGDATA=' + logdata
            else:
                if logdata is not None:
                    logdata_value = '/?LOGDATA=' + logdata
            td_sqlalchemy_engine  = create_engine('teradatasql://'+ username +':' + password + '@'+ host + logmech_value + logdata_value)
            td_connection = td_sqlalchemy_engine.connect()
            user_specified_connection= False
        except TeradataMlException:
            raise
        except Exception as err:
            raise TeradataMlException(Messages.get_message(MessageCodes.CONNECTION_FAILURE), MessageCodes.CONNECTION_FAILURE) from err
    # Check if host & logmech are only provided
    elif host and logmech.upper() == 'JWT':
        try:
            if td_connection is not None:
                warnings.warn(Messages.get_message(MessageCodes.OVERWRITE_CONTEXT))
                remove_context()
            logmech_value = '/?LOGMECH=' + logmech.upper()
            if logdata is not None:
                logdata_value = '&LOGDATA=' + logdata
            td_sqlalchemy_engine  = create_engine('teradatasql://'+ host + logmech_value + logdata_value)
            td_connection = td_sqlalchemy_engine.connect()
            user_specified_connection= False
        except TeradataMlException:
            raise
        except Exception as err:
            raise TeradataMlException(Messages.get_message(MessageCodes.CONNECTION_FAILURE), MessageCodes.CONNECTION_FAILURE) from err

    # Load function aliases from config.
    _load_function_aliases()

    # Assign the tempdatabase name to global
    if temp_database_name is None:
        temporary_database_name = _get_current_databasename()
    else:
        temporary_database_name = temp_database_name

    # Connection is established initiate the garbage collection
    atexit.register(__cleanup_garbage_collection)
    __cleanup_garbage_collection()
    # Initialise Dag
    __initalise_dag()
    # Return the connection by default
    return td_sqlalchemy_engine

def get_context():
    """
    DESCRIPTION:
        Returns the Teradata Vantage connection associated with the current context.

    PARAMETERS:
        None

    RETURNS:
        A Teradata sqlalchemy engine object.

    RAISES:
        None.

    EXAMPLES:
        td_sqlalchemy_engine = get_context()
        
    """
    global td_sqlalchemy_engine
    return td_sqlalchemy_engine

def get_connection():
    """
    DESCRIPTION:
        Returns the Teradata Vantage connection associated with the current context.

    PARAMETERS:
        None

    RETURNS:
        A Teradata dbapi connection object.

    RAISES:
        None.

    EXAMPLES:
        tdconnection = get_connection()
        
    """
    global td_connection
    return td_connection

def set_context(tdsqlengine, temp_database_name = None):
    """
    DESCRIPTION:
        Specifies a Teradata Vantage sqlalchemy engine as current context.

    PARAMETERS:
        tdsqlengine:
            Required Argument.
            Specifies Teradata Vantage sqlalchemy engine object that should be used to establish a Teradata Vantage connection.
            Types: str
            
        temp_database_name:
            Optional Argument.
            Specifies the temporary database name where temporary tables, views will be created.
            Types: str

    RETURNS:
        A Teradata Vantage connection object.

    RAISES:
        TeradataMlException

    EXAMPLES:
        set_context(tdsqlengine = td_sqlalchemy_engine)
        
    """
    global td_connection
    global td_sqlalchemy_engine
    global temporary_database_name
    if td_connection is not None:
        warnings.warn(Messages.get_message(MessageCodes.OVERWRITE_CONTEXT))
        remove_context()

    if tdsqlengine:
        try:
            td_connection = tdsqlengine.connect()
            td_sqlalchemy_engine = tdsqlengine
            # Assign the tempdatabase name to global
            if temp_database_name is None:
                temporary_database_name = _get_current_databasename()
            else:
                temporary_database_name = temp_database_name

            user_specified_connection = True
        except TeradataMlException:
            raise
        except Exception as err:
            raise TeradataMlException(Messages.get_message(MessageCodes.CONNECTION_FAILURE), MessageCodes.CONNECTION_FAILURE) from err
    else:
        return None

    # Load function aliases from config.
    _load_function_aliases()

    # Initialise Dag
    __initalise_dag()

    return td_connection

def remove_context():
    """
    DESCRIPTION:
        Removes the current context associated with the Teradata Vantage connection.

    PARAMETERS:
        None.

    RETURNS:
        None.

    RAISES:
        None.

    EXAMPLES:
        remove_context()
        
    """
    global td_connection
    global td_sqlalchemy_engine
    global user_specified_connection

    # Intiate the garbage collection
    __cleanup_garbage_collection()

    if user_specified_connection is not True:
        try:
            # Close the connection if not user specified connection.
            td_connection.close()
        except TeradataMlException:
            raise
        except Exception as err:
            raise TeradataMlException(Messages.get_message(MessageCodes.DISCONNECT_FAILURE), MessageCodes.DISCONNECT_FAILURE) from err
    td_connection = None
    td_sqlalchemy_engine = None
    # Closing Dag
    __close_dag()
    return True

def _get_context_temp_databasename():
    """
    Returns the temporary database name associated with the current context.

    PARAMETERS:
        None.

    RETURNS:
        Database name associated with the current context

    RAISES:
        None.

    EXAMPLES:
        _get_context_temp_databasename()
    """
    global temporary_database_name
    return temporary_database_name

def __initalise_dag():
    """
        Intialises the Dag

        PARAMETERS:
            None.

        RETURNS:
            None

        RAISES:
            None.

        EXAMPLES:
            __initalise_dag()
    """
    aed_context = AEDContext()
    # Closing the Dag if previous instance is still exists.
    __close_dag()
    # TODO: Need to add logLevel and log_file functionlaity once AED is implemented these functionalities
    aed_context._init_dag(_get_database_username(),_get_context_temp_databasename(),
                           log_level=4,log_file="")

def __close_dag():
    """
    Closes the Dag

    PARAMETERS:
        None.

    RETURNS:
        None

    RAISES:
        None.

    EXAMPLES:
        __close_dag()
    """
    try:
        AEDContext()._close_dag()
    # Ignore if any exception occurs.
    except TeradataMlException:
        pass


def _load_function_aliases():
    """
    Function to load function aliases for analytical functions
    based on the vantage version from configuration file.

    PARAMETERS:
        None

    RETURNS:
        None

    RAISES:
        TeradataMLException

    EXAMPLES:
        _load_function_aliases()
    """

    global function_alias_mappings
    function_alias_mappings = {}

    supported_engines = TeradataConstants.SUPPORTED_ENGINES.value
    vantage_versions = TeradataConstants.SUPPORTED_VANTAGE_VERSIONS.value

    __set_vantage_version()

    for vv in vantage_versions.keys():
        function_alias_mappings_by_engine = {}
        for engine in supported_engines.keys():
            alias_config_file = os.path.join(config_folder,
                                             "{}_{}".format(supported_engines[engine]["file"], vantage_versions[vv]))
            engine_name = supported_engines[engine]['name']
            UtilFuncs._check_alias_config_file_exists(vv, alias_config_file)
            function_alias_mappings_by_engine[engine_name] = \
                UtilFuncs._get_function_mappings_from_config_file(alias_config_file)
            function_alias_mappings[vv] = function_alias_mappings_by_engine

def __set_vantage_version():
    """
    Function to retrieve underlying vantage version and set the configuration option vantage_version.

    PARAMETERS:
        None

    RETURNS:
        None

    RAISES:
        TeradataMLException

    EXAMPLES:
        __set_vantage_version()
    """

    if td_sqlalchemy_engine.dialect.has_table(td_sqlalchemy_engine, "versionInfo", schema="pm"):

        # BTEQ -- Enter your SQL request or BTEQ command:
        # select * from pm.versionInfo;
        #
        # select * from pm.versionInfo;
        #
        # *** Query completed. 2 rows found. 2 columns returned.
        # *** Total elapsed time was 1 second.
        #
        # InfoKey                        InfoData
        # ------------------------------ --------------------------------------------
        # BUILD_VERSION                  08.10.00.00-e84ce5f7
        # RELEASE                        Vantage 1.1 GA

        try:
            vantage_ver_qry = "select InfoData from pm.versionInfo where InfoKey = 'RELEASE' (NOT CASESPECIFIC)"
            res = get_context().execute(vantage_ver_qry).scalar()
            if "vantage1.1" in res.lower().replace(" ", ""):
                configure.vantage_version = "vantage1.1"
        except:
            # Raise warning here.
            warnings.warn(Messages.get_message(
                MessageCodes.UNABLE_TO_GET_VANTAGE_VERSION).format("vantage_version", configure.vantage_version))
    else:
        # If "pm.versionInfo" does not exist, then vantage version is 1.0
        configure.vantage_version = "vantage1.0"

def _get_function_mappings():
    """
    Function to return function aliases for analytical functions.

    PARAMETERS:
        None

    RETURNS:
        Dict of function aliases of the format
        {'mle' : {'func_name': "alias_name", ...},
        'sqle' : {'func_name': "alias_name", ...}
        ......
        }

    RAISES:
        None

    EXAMPLES:
        get_function_aliases()
    """
    global function_alias_mappings
    return function_alias_mappings
