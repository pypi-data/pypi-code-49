import configparser
import logging
logger = logging.getLogger(__name__)
import socket
import os
import sys
from pathlib import Path

# Used to check file types
from magic import from_file

#####
# Load or create config from config.ini

# Load any stored values from our last run to use as defaults, create entries if the are not there.
class Config(object):

    parser = None

    #----------------------------------------------------------------------
    def __init__(self):
        self.home = str(Path.home())
        self.configpath = os.path.join(self.home, ".config")
        self.configDir = os.path.join(self.configpath,"eurekaroom",)

        self.parser = configparser.ConfigParser()
        self.parser['general'] = {
            'port': '5000', 
            'mediapath': 'media/',
            'nodename': socket.gethostname(),
            'configpath': self.configDir
            }
        
        ####TODO: validate or create the config.ini file, here
        try:
            os.mkdir(path=self.configpath)
            logger.debug('Created dir at {}'.format(self.configpath))
        except Exception as err:
            logger.debug('Error making dir with exception {}'.format(err))
        finally:
            logger.info('Config path: {}'.format(self.configpath))

        try:
            os.mkdir(path= self.configDir)
            logger.debug('Created dir at {}'.format(self.configDir))
        except Exception as err:
            logger.debug('Error making dir with exception {}'.format(err))
        finally:
            logger.info('Config path: {}'.format(self.configDir))
        
        self.configfile = os.path.join(self.configDir,"config.ini")
        try:
            self.parser.read(self.configfile)
            logger.debug('Configuration read in')
        except Exception as err:
            logger.debug('Error loading {}'.format(self.configfile))
        
    #----------------------------------------------------------------------
    def checkMedia(self, args):
        
        media = ['video', 'image', 'audio']
        for m in media:
            if not self.parser.has_section(m):
                self.parser.add_section(m)
                logger.info("An empty '{}' section has been added.  Use -aw to auto-populate it.".format(m))

                # If this is an empty config, and the media has not yet been added, but -a flag is set,
                # automatically scan the specified media folder and add the files to the temporary config    
           
        logger.debug("Automatically adding the media files from {}".format(args.mediapath))

        for dirpath, dirnames, files in os.walk(args.mediapath):
            logger.debug('Found directory: {}'.format(dirpath))
            for file_name in files:
                     
                # strip out any non media files as we go 
                type = from_file(dirpath + '/' + file_name, mime=True)
                type = str(type)[0:type.find('/')]
                
                if type.startswith(tuple(['video', 'image', 'audio'])):  
                    logger.debug("Adding {} to config {}/{}".format(type, dirpath, file_name))  
                    self.parser.set(type, file_name, "{}/{}".format(dirpath, file_name))      

    #----------------------------------------------------------------------
    def storeConfig(self, args):
        """
        This Function will store configuration changes from the arguments back to the ini file.
        """

        self.parser['general']['port'] = "{}".format(args.port)
        self.parser['general']['mediapath'] = "{}".format(args.mediapath)
        self.parser['general']['nodename'] = "{}".format(args.nodename)
        with open(self.configfile, 'w') as configfile:
            self.parser.write(configfile)
        sys.exit()

#######################################################################

######
## Load or create config from config.ini
try:
    config = Config()
    logger.info("Loaded config file '{}' ".format(config.configfile))
except Exception as err:
    logger.warning(" '{}' could NOT load {}".format(config.configfile, err))
#
#####

