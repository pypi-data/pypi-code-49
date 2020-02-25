# -*- coding: utf-8 -*-

import os
import re
import nwae.utils.BaseConfig as baseconfig
import nwae.utils.Log as lg
from inspect import currentframe, getframeinfo
import nwae.utils.Log as nwaelog


#
# We put all our common file paths here
#
class Config(baseconfig.BaseConfig):

    #######################################################################
    # Main Stuff
    #######################################################################
    PARAM_TOPDIR = 'topdir'
    DEFVAL_TOPDIR = '~/git/nwae/nwae.broadcaster'

    PARAM_LOG_LEVEL = 'loglevel'
    DEFVAL_LOGLEVEL = lg.Log.LOG_LEVEL_INFO

    PARAM_DEBUG = 'debug'
    DEFVAL_DEBUG = False

    #######################################################################
    # Server Stuff
    #######################################################################
    PARAM_PORT_AGGREGATOR = 'port_aggregator'
    DEFVAL_PORT_AGGREGATOR = 7002

    PARAM_PORT_BROADCASTER = 'port_broadcaster'
    DEFVAL_PORT_BROADCASTER = 7003

    PARAM_DIR_SERVER = 'dir_server'
    DEFVAL_DIR_SERVER = DEFVAL_TOPDIR + '/app.data/server'

    PARAM_FILEPATH_SERVER_LOGS = 'filepath_server_logs'
    DEFVAL_FILEPATH_SERVER_LOGS = DEFVAL_DIR_SERVER + '/server.' + str(DEFVAL_PORT_BROADCASTER) +'.log'

    PARAM_DIR_SERVER_CACHE = 'dir_server_cache'
    DEFVAL_DIR_SERVER_CACHE = DEFVAL_TOPDIR + '/app.data/server.cache'

    def __init__(
            self,
            config_file
    ):
        super().__init__(
            config_file = config_file
        )
        self.reload_config()
        return

    def reload_config(
            self
    ):
        # Call base class first
        lg.Log.debug(
            str(self.__class__) + ' ' + str(getframeinfo(currentframe()).lineno) \
            + ': Calling base class reload config for "' + str(self.config_file) + '"..'
        )
        super(Config,self).reload_config()

        #
        # Top directory MUST EXIST.
        # This is the only variable that we should change, the top directory
        #
        topdir = self.get_config(param=Config.PARAM_TOPDIR)
        if not os.path.isdir(topdir):
            errmsg = str(self.__class__) + ' ' + str(getframeinfo(currentframe()).lineno) \
                     + ': Fatal error initializing config, "' + str(topdir) + '" is not a directory!'
            lg.Log.critical(errmsg)
            raise Exception(errmsg)

        try:
            self.reset_default_config()

            self.__reconfigure_paths_requiring_topdir()

            #
            # This is the part we convert our values to desired types
            #
            self.convert_value_to_float_type(
                param = Config.PARAM_LOG_LEVEL,
                default_val = Config.DEFVAL_LOGLEVEL
            )
            lg.Log.LOGLEVEL = self.param_value[Config.PARAM_LOG_LEVEL]
            lg.Log.LOGFILE = self.param_value[Config.PARAM_FILEPATH_SERVER_LOGS]
            lg.Log.important(
                str(self.__class__) + ' ' + str(getframeinfo(currentframe()).lineno)
                + ': Set log level to "' + str(lg.Log.LOGLEVEL) + '" and log file "'
                + str(lg.Log.LOGFILE) + '".'
            )
            # Also do for nwae logs
            nwaelog.Log.LOGLEVEL = lg.Log.LOGLEVEL
            nwaelog.Log.LOGFILE = lg.Log.LOGFILE

            #
            # Here lies the important question, should we standardize all config
            # to only string type, or convert them?
            #
            self.convert_value_to_boolean_type(
                param = Config.PARAM_DEBUG
            )
            lg.Log.DEBUG_PRINT_ALL_TO_SCREEN = self.param_value[Config.PARAM_DEBUG]
            nwaelog.Log.DEBUG_PRINT_ALL_TO_SCREEN = lg.Log.DEBUG_PRINT_ALL_TO_SCREEN

            read_easy_config = str(self.param_value)
            read_easy_config = re.sub(pattern=', ', repl='\n\t', string=read_easy_config)
            read_easy_config = re.sub(pattern='{', repl='{\n\t', string=read_easy_config)
            read_easy_config = re.sub(pattern='}', repl='\n}', string=read_easy_config)

            lg.Log.important(
                str(self.__class__) + ' ' + str(getframeinfo(currentframe()).lineno) \
                + ' BROADCAST SERVER CONFIG "' + str(self.config_file) + '" reloaded as follows:\n\r'
                + str(read_easy_config)
            )
        except Exception as ex:
            errmsg = str(self.__class__) + ' ' + str(getframeinfo(currentframe()).lineno)\
                     + ': Error initializing config file "' + str(self.config_file)\
                     + '". Exception message ' + str(ex)
            lg.Log.critical(errmsg)
            raise Exception(errmsg)

        return

    #
    # For those params not found in config file, we give default values
    #
    def reset_default_config(
            self
    ):
        param_values_to_set = {
            #######################################################################
            # Main Stuff
            #######################################################################
            Config.PARAM_TOPDIR: Config.DEFVAL_TOPDIR,
            Config.PARAM_LOG_LEVEL: Config.DEFVAL_LOGLEVEL,
            Config.PARAM_DEBUG: Config.DEFVAL_DEBUG,
            #######################################################################
            # Server Stuff
            #######################################################################
            Config.PARAM_PORT_AGGREGATOR: Config.DEFVAL_PORT_AGGREGATOR,
            Config.PARAM_PORT_BROADCASTER: Config.DEFVAL_PORT_BROADCASTER,
            Config.PARAM_DIR_SERVER: Config.DEFVAL_DIR_SERVER,
            Config.PARAM_FILEPATH_SERVER_LOGS: Config.DEFVAL_FILEPATH_SERVER_LOGS,
        }

        for param in param_values_to_set.keys():
            default_value = param_values_to_set[param]
            self.set_default_value_if_not_exist(
                param = param,
                default_value = default_value
            )
        return

    def __reconfigure_paths_requiring_topdir(self):
        topdir = self.get_config(param=Config.PARAM_TOPDIR)

        self.param_value[Config.PARAM_DIR_SERVER] = topdir + '/app.data/server'
        self.param_value[Config.PARAM_FILEPATH_SERVER_LOGS] =\
            self.param_value[Config.PARAM_DIR_SERVER]\
            + '/server.' + str(self.param_value[Config.PARAM_PORT_BROADCASTER]) +'.log'

        self.param_value[Config.PARAM_DIR_SERVER_CACHE] =\
            topdir + '/app.data/server.cache'


if __name__ == '__main__':
    import time

    config = Config.get_cmdline_params_and_init_config_singleton(
        Derived_Class = Config,
        default_config_file = '/usr/local/git/nwae/nwae.broadcaster/app.data/config/broadcaster.cf'
    )
    print(config.param_value)
    #
    # Singleton should already exist
    #
    print('*************** Test Singleton exists')
    Config.get_cmdline_params_and_init_config_singleton(
        Derived_Class = Config,
        default_config_file='/usr/local/git/nwae/nwae.broadcaster/app.data/config/broadcaster.cf'
    )
    time.sleep(3)

    print('*************** Test config file reload..')
    config = Config(
        config_file = '/usr/local/git/nwae/nwae.broadcaster/app.data/config/broadcaster.cf'
    )
    while True:
        time.sleep(3)
        if config.is_file_last_updated_time_is_newer():
            print('********************* FILE TIME UPDATED...')
            config.reload_config()
            print(config.get_config(param='topdir'))
            print(config.param_value)