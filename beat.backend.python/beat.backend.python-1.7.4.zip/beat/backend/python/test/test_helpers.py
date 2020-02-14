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


# Tests for experiment execution

import os
import logging
logger = logging.getLogger(__name__)

import unittest
import zmq
import tempfile
import shutil

from ..database import Database
from ..data_loaders import DataLoader
from ..hash import hashDataset
from ..hash import toPath
from ..algorithm import Algorithm
from ..helpers import create_inputs_from_configuration
from ..helpers import AccessMode
from ..execution import MessageHandler

from . import prefix


#----------------------------------------------------------


DB_VIEW_HASH = hashDataset('integers_db/1', 'double', 'double')
DB_INDEX_PATH = toPath(DB_VIEW_HASH, suffix='.db')

CONFIGURATION_DB_LEGACY = {
    'queue': 'queue',
    'algorithm': 'legacy/echo/1',
    'nb_slots': 1,
    'channel': 'integers',
    'parameters': {
    },
    'environment': {
        'name': 'Python 2.7',
        'version': '1.2.0'
    },
    'inputs': {
        'in': {
            'database': 'integers_db/1',
            'protocol': 'double',
            'set': 'double',
            'output': 'a',
            'endpoint': 'in',
            'channel': 'integers',
            'path': DB_INDEX_PATH,
            'hash': DB_VIEW_HASH,
        },
    },
    'outputs': {
        'out': {
            'endpoint': 'out',
            'channel': 'integers',
            'path': '20/61/b6/2df3c3bedd5366f4a625c5d87ffbf5a26007c46c456e9abf21b46c6681',
            'hash': '2061b62df3c3bedd5366f4a625c5d87ffbf5a26007c46c456e9abf21b46c6681',
        }
    }
}

CONFIGURATION_DB_SEQUENTIAL = {
    'queue': 'queue',
    'algorithm': 'sequential/echo/1',
    'nb_slots': 1,
    'channel': 'integers',
    'parameters': {
    },
    'environment': {
        'name': 'Python 2.7',
        'version': '1.2.0'
    },
    'inputs': {
        'in': {
            'database': 'integers_db/1',
            'protocol': 'double',
            'set': 'double',
            'output': 'a',
            'endpoint': 'in',
            'channel': 'integers',
            'path': DB_INDEX_PATH,
            'hash': DB_VIEW_HASH,
        },
    },
    'outputs': {
        'out': {
            'endpoint': 'out',
            'channel': 'integers',
            'path': '20/61/b6/2df3c3bedd5366f4a625c5d87ffbf5a26007c46c456e9abf21b46c6681',
            'hash': '2061b62df3c3bedd5366f4a625c5d87ffbf5a26007c46c456e9abf21b46c6681',
        }
    }
}

CONFIGURATION_DB_AUTONOMOUS = {
    'queue': 'queue',
    'algorithm': 'autonomous/echo/1',
    'nb_slots': 1,
    'channel': 'integers',
    'parameters': {
    },
    'environment': {
        'name': 'Python 2.7',
        'version': '1.2.0'
    },
    'inputs': {
        'in': {
            'database': 'integers_db/1',
            'protocol': 'double',
            'set': 'double',
            'output': 'a',
            'endpoint': 'in',
            'channel': 'integers',
            'path': DB_INDEX_PATH,
            'hash': DB_VIEW_HASH,
        },
    },
    'outputs': {
        'out': {
            'endpoint': 'out',
            'channel': 'integers',
            'path': '20/61/b6/2df3c3bedd5366f4a625c5d87ffbf5a26007c46c456e9abf21b46c6681',
            'hash': '2061b62df3c3bedd5366f4a625c5d87ffbf5a26007c46c456e9abf21b46c6681',
        }
    }
}


#----------------------------------------------------------


class TestCreateInputsFromConfiguration_RemoteDatabase(unittest.TestCase):

    def setUp(self, remote=True):
        self.remote = remote

        self.cache_root = tempfile.mkdtemp(prefix=__name__)

        database = Database(prefix, 'integers_db/1')
        view = database.view('double', 'double')

        view.index(os.path.join(self.cache_root, DB_INDEX_PATH))

        self.databases = {}
        self.databases['integers_db/1'] = database

        if remote:
            view.setup(os.path.join(self.cache_root, DB_INDEX_PATH))

            data_sources = {
                'in': view.data_sources['a'],
            }

            self.message_handler = MessageHandler('127.0.0.1', data_sources=data_sources)
            self.message_handler.start()

            self.zmq_context = zmq.Context()
            self.socket = self.zmq_context.socket(zmq.PAIR)
            self.socket.connect(self.message_handler.address)
        else:
            self.message_handler = None
            self.socket = None


    def tearDown(self):
        if self.message_handler is not None:
            self.message_handler.kill()
            self.message_handler.join()
            self.message_handler.destroy()
            self.message_handler = None

        if self.socket is not None:
            self.socket.setsockopt(zmq.LINGER, 0)
            self.socket.close()
            self.zmq_context.destroy()
            self.socket = None
            self.zmq_context = None

        shutil.rmtree(self.cache_root)


    def test_legacy_algorithm(self):
        algorithm = Algorithm(prefix, CONFIGURATION_DB_LEGACY['algorithm'])
        runner = algorithm.runner()

        if self.remote:
            db_access = db_access=AccessMode.REMOTE
        else:
            db_access = db_access=AccessMode.LOCAL

        (input_list, data_loader_list) = \
                create_inputs_from_configuration(CONFIGURATION_DB_LEGACY, algorithm,
                                                 prefix, self.cache_root,
                                                 cache_access=AccessMode.NONE,
                                                 db_access=db_access,
                                                 unpack=True,
                                                 databases=self.databases,
                                                 socket=self.socket,
                                                 no_synchronisation_listeners=False
        )

        self.assertEqual(len(input_list), 1)
        self.assertEqual(len(data_loader_list), 0)


    def test_sequential_algorithm(self):
        algorithm = Algorithm(prefix, CONFIGURATION_DB_SEQUENTIAL['algorithm'])
        runner = algorithm.runner()

        if self.remote:
            db_access = db_access=AccessMode.REMOTE
        else:
            db_access = db_access=AccessMode.LOCAL

        (input_list, data_loader_list) = \
                create_inputs_from_configuration(CONFIGURATION_DB_SEQUENTIAL, algorithm,
                                                 prefix, self.cache_root,
                                                 cache_access=AccessMode.NONE,
                                                 db_access=db_access,
                                                 unpack=True,
                                                 databases=self.databases,
                                                 socket=self.socket,
                                                 no_synchronisation_listeners=False
        )

        self.assertEqual(len(input_list), 1)
        self.assertEqual(len(data_loader_list), 0)


    def test_autonomous_algorithm(self):
        algorithm = Algorithm(prefix, CONFIGURATION_DB_AUTONOMOUS['algorithm'])
        runner = algorithm.runner()

        if self.remote:
            db_access = db_access=AccessMode.REMOTE
        else:
            db_access = db_access=AccessMode.LOCAL

        (input_list, data_loader_list) = \
                create_inputs_from_configuration(CONFIGURATION_DB_AUTONOMOUS, algorithm,
                                                 prefix, self.cache_root,
                                                 cache_access=AccessMode.NONE,
                                                 db_access=db_access,
                                                 unpack=True,
                                                 databases=self.databases,
                                                 socket=self.socket,
                                                 no_synchronisation_listeners=False
        )

        self.assertEqual(len(input_list), 0)
        self.assertEqual(len(data_loader_list), 1)


#----------------------------------------------------------


class TestCreateInputsFromConfiguration_LocalDatabase(TestCreateInputsFromConfiguration_RemoteDatabase):

    def setUp(self):
        super(TestCreateInputsFromConfiguration_LocalDatabase, self).setUp(remote=False)
