'''
 Copyright (c) 2019, UChicago Argonne, LLC
 See LICENSE file.
'''
import logging
import logging.config
import os
from configparser import NoSectionError

__version__="1.3.0"

LOGGER_NAME="s33specimagesum"
METHOD_ENTER_STR = "Enter %s\n-------------------"
METHOD_EXIT_STR = "Exit %s\n---------------------"
LOGGER_DEFAULT = {
    'version' : 1,
    'handlers' : {'consoleHandler' : {'class' : 'logging.StreamHandler',
                               'level' : 'INFO',
                               'formatter' : 'consoleFormat',
                               'stream' : 'ext://sys.stdout'} ,
                  },
    'formatters' : {'consoleFormat' : {'format' : '%(asctime)-15s - %(name)s - %(funcName)s- %(levelname)s - %(message)s'},
                    },
    'loggers' : {'root' :{'level' : 'INFO',
                        'handlers' : ['consoleHandler',],
                      },
               LOGGER_NAME : {'level' : 'INFO',
                            'handlers' : ['consoleHandler',],
                            'qualname' : LOGGER_NAME
                            }
               },
   }

userDir = os.path.expanduser("~")
logConfigFile = os.path.join(userDir, LOGGER_NAME + 'Log.config')
if os.path.exists(logConfigFile):
    print ("logConfigFile " + logConfigFile )
    try:
        logging.config.fileConfig(logConfigFile, disable_existing_loggers=False)
        print("Success Openning logfile")
    except (NoSectionError,TypeError) as ex:
        print ("In Exception to load dictConfig package %s\n %s" % (LOGGER_NAME, ex))
        logging.config.dictConfig(LOGGER_DEFAULT)
    except KeyError as ex:
        print ("logfile %s was missing or had errant sections %s" %(logConfigFile, ex.args))

else:
    logging.config.dictConfig(LOGGER_DEFAULT)
