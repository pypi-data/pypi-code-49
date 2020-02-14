#!/usr/bin/env python
# vim: set fileencoding=utf-8 :

###################################################################################
#                                                                                 #
# Copyright (c) 2019 Idiap Research Institute, http://www.idiap.ch/               #
# Contact: beat.support@idiap.ch                                                  #
#                                                                                 #
# Redistribution and use in source and binary forms, with or without              #
# modification, are permitted provided that the following conditions are met:     #
#                                                                                 #
# 1. Redistributions of source code must retain the above copyright notice, this  #
# list of conditions and the following disclaimer.                                #
#                                                                                 #
# 2. Redistributions in binary form must reproduce the above copyright notice,    #
# this list of conditions and the following disclaimer in the documentation       #
# and/or other materials provided with the distribution.                          #
#                                                                                 #
# 3. Neither the name of the copyright holder nor the names of its contributors   #
# may be used to endorse or promote products derived from this software without   #
# specific prior written permission.                                              #
#                                                                                 #
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND #
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED   #
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE          #
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE    #
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL      #
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR      #
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER      #
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,   #
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE   #
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.            #
#                                                                                 #
###################################################################################


"""Executes some database views. (%(version)s)

usage:
  %(prog)s [--debug] <addr> <dir> <cache> [<conf_name>]
  %(prog)s (--help)
  %(prog)s (--version)


arguments:
  <addr>        Listen for incoming request on this address ('host:port')
  <dir>         Directory containing all configuration required to run the views
  <cache>       Path to the cache
  <conf_name>   Name of the configuration to load


options:
  -h, --help         Shows this help message and exit
  -V, --version      Shows program's version number and exit
  -d, --debug        Runs executor in debugging mode

"""

import logging

import os
import sys
import docopt
import simplejson
import pwd
import stat
import json

import zmq

from beat.backend.python.execution import DBExecutor
from beat.backend.python.execution import MessageHandler
from beat.backend.python.exceptions import UserError


#----------------------------------------------------------


def process_traceback(tb, prefix):
    import traceback

    databases_prefix = os.path.join(prefix, 'databases') + os.sep

    for first_line, line in enumerate(tb):
        if line[0].startswith(databases_prefix):
            break

    s = ''.join(traceback.format_list(tb[first_line:]))
    s = s.replace(databases_prefix, 'databases' + os.sep).strip()

    return s


#----------------------------------------------------------


def main(arguments=None):

    # Parse the command-line arguments
    if arguments is None:
        arguments = sys.argv[1:]

    package = __name__.rsplit('.', 2)[0]
    version = package + ' v' + \
              __import__('pkg_resources').require(package)[0].version

    prog = os.path.basename(sys.argv[0])

    args = docopt.docopt(
        __doc__ % dict(prog=prog, version=version),
        argv=arguments,
        version=version
    )


    # Setup the logging system
    formatter = logging.Formatter(fmt="[%(asctime)s - databases_provider.py - " \
                                      "%(name)s] %(levelname)s: %(message)s",
                                  datefmt="%d/%b/%Y %H:%M:%S")

    handler = logging.StreamHandler()
    handler.setFormatter(formatter)

    root_logger = logging.getLogger('beat.backend.python')
    root_logger.addHandler(handler)

    if args['--debug']:
        root_logger.setLevel(logging.DEBUG)
    else:
        root_logger.setLevel(logging.INFO)

    logger = logging.getLogger(__name__)


    # Create the message handler
    message_handler = MessageHandler(args['<addr>'])


    # If necessary, change to another user (with less privileges, but has access
    # to the databases)
    with open(os.path.join(args['<dir>'], 'configuration.json'), 'r') as f:
        cfg = simplejson.load(f)

    if 'datasets_uid' in cfg:
        # First create the user (if it doesn't exists)
        try:
            user = pwd.getpwuid(cfg['datasets_uid'])
        except:
            import subprocess
            retcode = subprocess.call(['adduser', '--uid', str(cfg['datasets_uid']),
                                       '--no-create-home', '--disabled-password',
                                       '--disabled-login', '--gecos', '""', '-q',
                                       'beat-nobody'])
            if retcode != 0:
                message_handler.send_error('Failed to create an user with the UID %s' % args['uid'], 'sys')
                return 1

        # Change the current user
        try:
            os.setgid(cfg['datasets_uid'])
            os.setuid(cfg['datasets_uid'])
        except:
            import traceback
            message_handler.send_error(traceback.format_exc(), 'sys')
            message_handler.destroy()
            return 1


    try:

        # Check the dir
        if not os.path.exists(args['<dir>']):
            raise IOError("Running directory `%s' not found" % args['<dir>'])

        # Sets up the execution
        dataformat_cache = {}
        database_cache = {}

        try:
            configuration_path = os.path.join(args['<dir>'], 'configuration.json')
            if not os.path.exists(configuration_path):
                raise RuntimeError("Configuration file '%s' not found" %
                                   configuration_path)

            with open(configuration_path) as f:
                configuration_data = json.load(f)

            configuration_name = args.get('<conf_name>', None)
            if configuration_name is not None:
                configuration_data = configuration_data.get(configuration_name,
                                                            None)
                if configuration_data is None:
                    raise RuntimeError("Configuration section '%s' not found" %
                                       configuration_name)

            dbexecutor = DBExecutor(message_handler,
                                    os.path.join(args['<dir>'], 'prefix'),
                                    args['<cache>'],
                                    configuration_data,
                                    dataformat_cache,
                                    database_cache)
        except (MemoryError):
            raise
        except Exception as e:
            import traceback
            exc_type, exc_value, exc_traceback = sys.exc_info()
            tb = traceback.extract_tb(exc_traceback)
            s = process_traceback(tb, os.path.join(args['<dir>'], 'prefix'))
            raise UserError("%s%s: %s" % (s, type(e).__name__, e))

        # Execute the code
        try:
            dbexecutor.process()
            dbexecutor.wait()
        except (MemoryError):
            raise
        except Exception as e:
            import traceback
            exc_type, exc_value, exc_traceback = sys.exc_info()
            tb = traceback.extract_tb(exc_traceback)
            s = process_traceback(tb, os.path.join(args['<dir>'], 'prefix'))
            raise UserError("%s%s: %s" % (s, type(e).__name__, e))

    except UserError as e:
        message_handler.send_error(str(e), 'usr')
        message_handler.destroy()
        return 1

    except MemoryError as e:
        # Say something meaningful to the user
        msg = "The user process for this block ran out of memory. We " \
              "suggest you optimise your code to reduce memory usage or, " \
              "if this is not an option, choose an appropriate processing " \
              "queue with enough memory."
        message_handler.send_error(msg, 'usr')
        message_handler.destroy()
        return 1

    except Exception as e:
        import traceback
        message_handler.send_error(traceback.format_exc(), 'sys')
        message_handler.destroy()
        return 1

    message_handler.destroy()

    return 0



if __name__ == '__main__':
    sys.exit(main())
