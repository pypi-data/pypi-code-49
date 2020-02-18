import os
import logging
import argparse
import builtins
from ghcopy.utils import set_config, activate_virtual_environment, set_localization, get_logger

########################################################################################################################
#                                                 Configuration                                                        #
########################################################################################################################

parser = argparse.ArgumentParser(prog='ghcopy')
home = os.getenv("HOME")
parser.add_argument('-c', '--config', help='config file', default='~/.ghcopy/config.json')
parser.add_argument('-o', '--output', help='output directory', default='~/RemoteCopies')
parser.add_argument('-b', '--hub', help='repository type: github, bitbucket')
parser.add_argument('-u', '--user', help='user name')
parser.add_argument('-p', '--password', help='password')
parser.add_argument('-t', '--token', help='token')
parser.add_argument('-l', '--log_level', help='logging level: CRITICAL, ERROR, WARNING, INFO, DEBUG or NOTSET',
                    default='INFO')

cmd_args = parser.parse_args()
config_args = set_config(cmd_args.config.replace('~', home))
cmd_args.output = cmd_args.output.replace('~', home)

########################################################################################################################
#                                                  Localization                                                        #
########################################################################################################################

set_localization(**config_args)
translate = _ = builtins.__dict__.get('_', lambda x: x)


########################################################################################################################
#                                                    Logging                                                           #
########################################################################################################################

try:
    log_level, level_error = logging._nameToLevel[cmd_args.log_level], False
except KeyError:
    level_error = True
    log_level = logging._nameToLevel['INFO']
logger = get_logger('ghcopy', config_args.get("log_format", "%(levelname)-10s|%(asctime)s|"
                                                            "%(process)d|%(thread)d| %(name)s --- "
                                                            "%(message)s"),
                    config_args.get('log_file', '~/.report/report.log').replace('~', home), log_level)
if level_error:
    logger.warning('%s \'%s\', %s \'INFO\' %s' % (_('incorrect logging level'), cmd_args.log_level, _('used'),
                                                  _('by default')))
    cmd_args.log_level = 'INFO'


########################################################################################################################
#                                               Virtual environment                                                    #
########################################################################################################################

if config_args.get('environment') != "":
    activate_virtual_environment(**config_args)
    logger.info('%s \'%s\'' % (_('activated virtual environment'), config_args.get('environment')))
