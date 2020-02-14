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


import unittest
import six
import os
import glob
import tempfile
import logging

import numpy as np

from ..algorithm import Algorithm
from ..data_loaders import DataLoaderList
from ..data_loaders import DataLoader
from ..dataformat import DataFormat
from ..data import CachedDataSink
from ..data import CachedDataSource
from ..inputs import Input
from ..inputs import InputGroup
from ..inputs import InputList
from ..outputs import Output
from ..outputs import OutputList
from ..outputs import SynchronizationListener

from .mocks import MockDataSink
from .mocks import MockLoggingHandler

from . import prefix


# ----------------------------------------------------------


class TestLegacyAPI_Loading(unittest.TestCase):
    def test_load_unknown_algorithm(self):
        algorithm = Algorithm(prefix, "legacy/unknown/1")
        self.assertFalse(algorithm.valid)
        self.assertTrue(algorithm.errors[0].find("file not found") != -1)

    def test_raises_syntax_error(self):
        algorithm = Algorithm(prefix, "legacy/syntax_error/1")
        self.assertTrue(algorithm.valid, algorithm.errors)

        with self.assertRaises(SyntaxError):
            algorithm.runner()

    def test_raises_runtime_error(self):
        algorithm = Algorithm(prefix, "legacy/syntax_error/1")
        self.assertTrue(algorithm.valid, algorithm.errors)

        with self.assertRaises(RuntimeError):
            algorithm.runner(exc=RuntimeError)

    def test_missing_class_raises(self):
        algorithm = Algorithm(prefix, "legacy/no_class/1")
        self.assertTrue(algorithm.valid, algorithm.errors)

        with self.assertRaises(AttributeError):
            algorithm.runner()

    def test_duplicate_key_error(self):
        algorithm = Algorithm(prefix, "legacy/duplicate_key_error/1")
        self.assertFalse(algorithm.valid)
        self.assertNotEqual(
            algorithm.errors[0].find("Algorithm declaration file invalid"), -1
        )

    def test_load_valid_algorithm(self):
        algorithm = Algorithm(prefix, "legacy/valid_algorithm/1")
        self.assertEqual(algorithm.name, "legacy/valid_algorithm/1")
        self.assertTrue(algorithm.valid, algorithm.errors)

        self.assertFalse(algorithm.errors)
        self.assertFalse(algorithm.results)  # it is not an analyzer
        self.assertFalse(algorithm.parameters)  # does not contain parameters
        self.assertTrue(algorithm.input_map)
        self.assertTrue(algorithm.output_map)
        self.assertEqual(algorithm.schema_version, 1)
        self.assertEqual(algorithm.api_version, 1)
        self.assertEqual(algorithm.type, Algorithm.LEGACY)

        runnable = algorithm.runner()
        self.assertTrue(runnable.ready)  # no setup
        self.assertTrue(runnable.prepared)

    def test_load_valid_analyser(self):
        algorithm = Algorithm(prefix, "legacy/valid_analysis/1")
        self.assertEqual(algorithm.name, "legacy/valid_analysis/1")
        self.assertTrue(algorithm.valid, algorithm.errors)

        self.assertFalse(algorithm.errors)
        self.assertFalse(algorithm.output_map)  # it is an analyzer
        self.assertFalse(algorithm.parameters)  # does not contain parameters
        self.assertTrue(algorithm.input_map)
        self.assertTrue(algorithm.results)
        self.assertEqual(algorithm.schema_version, 1)
        self.assertEqual(algorithm.api_version, 1)
        self.assertEqual(algorithm.type, Algorithm.LEGACY)

        self.assertEqual(len(algorithm.results), 2)

        self.assertTrue("c" in algorithm.results)
        self.assertEqual(
            algorithm.results["c"], dict(type="plot/scatter/1", display=False)
        )

        self.assertTrue("v" in algorithm.results)
        self.assertEqual(algorithm.results["v"], dict(type="float32", display=True))

        runnable = algorithm.runner()
        self.assertTrue(runnable.ready)  # no setup
        self.assertTrue(runnable.prepared)

    def test_hash(self):
        algorithm = Algorithm(prefix, "legacy/valid_analysis/1")
        self.assertTrue(algorithm.valid, algorithm.errors)
        self.assertEqual(len(algorithm.hash()), 64)

        v2 = Algorithm(prefix, "legacy/valid_analysis/2")  # only doc changes
        self.assertTrue(algorithm.valid, algorithm.errors)
        self.assertEqual(algorithm.hash(), v2.hash())

    def test_no_description(self):
        algorithm = Algorithm(prefix, "legacy/no_doc/1")
        self.assertTrue(algorithm.valid, algorithm.errors)
        self.assertTrue(algorithm.description is None)
        self.assertTrue(algorithm.documentation is None)

        description = "This is my descriptor"
        algorithm.description = description

        self.assertTrue(isinstance(algorithm.description, six.string_types))
        self.assertEqual(algorithm.description, description)

    def test_description(self):
        algorithm = Algorithm(prefix, "legacy/valid_analysis/2")  # only doc changes
        self.assertTrue(algorithm.valid, algorithm.errors)
        self.assertTrue(isinstance(algorithm.description, six.string_types))
        self.assertTrue(len(algorithm.description) > 0)
        self.assertTrue(algorithm.documentation is None)

    def test_analyzer_format(self):
        algorithm_name = "legacy/valid_analysis/1"
        algorithm = Algorithm(prefix, algorithm_name)
        self.assertTrue(algorithm.valid, algorithm.errors)

        dataformat = algorithm.result_dataformat()
        self.assertTrue(dataformat.valid)

        self.assertEqual(dataformat.name, "analysis:" + algorithm_name)


# ----------------------------------------------------------


class TestSequentialAPI_Loading(unittest.TestCase):
    def test_load_valid_algorithm(self):
        algorithm = Algorithm(prefix, "sequential/valid_algorithm/1")
        self.assertEqual(algorithm.name, "sequential/valid_algorithm/1")
        self.assertTrue(algorithm.valid, algorithm.errors)

        self.assertFalse(algorithm.errors)
        self.assertFalse(algorithm.results)  # it is not an analyzer
        self.assertFalse(algorithm.parameters)  # does not contain parameters
        self.assertTrue(algorithm.input_map)
        self.assertTrue(algorithm.output_map)
        self.assertEqual(algorithm.schema_version, 2)
        self.assertEqual(algorithm.api_version, 2)
        self.assertEqual(algorithm.type, Algorithm.SEQUENTIAL)

        runnable = algorithm.runner()
        self.assertFalse(runnable.ready)
        self.assertFalse(runnable.prepared)

    def test_load_valid_analyser(self):
        algorithm = Algorithm(prefix, "sequential/valid_analysis/1")
        self.assertEqual(algorithm.name, "sequential/valid_analysis/1")
        self.assertTrue(algorithm.valid, algorithm.errors)

        self.assertFalse(algorithm.errors)
        self.assertFalse(algorithm.output_map)  # it is an analyzer
        self.assertFalse(algorithm.parameters)  # does not contain parameters
        self.assertTrue(algorithm.input_map)
        self.assertTrue(algorithm.results)
        self.assertEqual(algorithm.schema_version, 2)
        self.assertEqual(algorithm.api_version, 2)
        self.assertEqual(algorithm.type, Algorithm.SEQUENTIAL)

        self.assertEqual(len(algorithm.results), 2)

        self.assertTrue("c" in algorithm.results)
        self.assertEqual(
            algorithm.results["c"], dict(type="plot/scatter/1", display=False)
        )

        self.assertTrue("v" in algorithm.results)
        self.assertEqual(algorithm.results["v"], dict(type="float32", display=True))

        runnable = algorithm.runner()
        self.assertFalse(runnable.ready)
        self.assertFalse(runnable.prepared)

    def test_load_valid_loop_evaluator(self):
        algorithm = Algorithm(prefix, "sequential/loop_evaluator/1")
        self.assertEqual(algorithm.name, "sequential/loop_evaluator/1")
        self.assertTrue(algorithm.valid, algorithm.errors)

        self.assertFalse(algorithm.errors)
        self.assertFalse(algorithm.results)  # it is not an analyzer
        self.assertTrue(algorithm.parameters)  # does not contain parameters
        self.assertTrue(algorithm.input_map)
        self.assertTrue(algorithm.output_map)
        self.assertEqual(algorithm.schema_version, 3)
        self.assertEqual(algorithm.api_version, 2)
        self.assertEqual(algorithm.type, Algorithm.SEQUENTIAL_LOOP_EVALUATOR)

        runnable = algorithm.runner()
        self.assertFalse(runnable.ready)
        self.assertTrue(runnable.prepared)

    def test_load_valid_loop_processor(self):
        algorithm = Algorithm(prefix, "sequential/loop_processor/1")
        self.assertEqual(algorithm.name, "sequential/loop_processor/1")
        self.assertTrue(algorithm.valid, algorithm.errors)

        self.assertFalse(algorithm.errors)
        self.assertFalse(algorithm.results)  # it is not an analyzer
        self.assertFalse(algorithm.parameters)  # does not contain parameters
        self.assertTrue(algorithm.input_map)
        self.assertTrue(algorithm.output_map)
        self.assertEqual(algorithm.schema_version, 3)
        self.assertEqual(algorithm.api_version, 2)
        self.assertEqual(algorithm.type, Algorithm.SEQUENTIAL_LOOP_PROCESSOR)

        runnable = algorithm.runner()
        self.assertTrue(runnable.ready)
        self.assertTrue(runnable.prepared)


# ----------------------------------------------------------


class TestAutonomousAPI_Loading(unittest.TestCase):
    def test_load_valid_algorithm(self):
        algorithm = Algorithm(prefix, "autonomous/valid_algorithm/1")
        self.assertEqual(algorithm.name, "autonomous/valid_algorithm/1")
        self.assertTrue(algorithm.valid, algorithm.errors)

        self.assertFalse(algorithm.errors)
        self.assertFalse(algorithm.results)  # it is not an analyzer
        self.assertFalse(algorithm.parameters)  # does not contain parameters
        self.assertTrue(algorithm.input_map)
        self.assertTrue(algorithm.output_map)
        self.assertEqual(algorithm.schema_version, 2)
        self.assertEqual(algorithm.api_version, 2)
        self.assertEqual(algorithm.type, Algorithm.AUTONOMOUS)

        runnable = algorithm.runner()
        self.assertFalse(runnable.ready)
        self.assertFalse(runnable.prepared)

    def test_load_valid_analyser(self):
        algorithm = Algorithm(prefix, "autonomous/valid_analysis/1")
        self.assertEqual(algorithm.name, "autonomous/valid_analysis/1")
        self.assertTrue(algorithm.valid, algorithm.errors)

        self.assertFalse(algorithm.errors)
        self.assertFalse(algorithm.output_map)  # it is an analyzer
        self.assertFalse(algorithm.parameters)  # does not contain parameters
        self.assertTrue(algorithm.input_map)
        self.assertTrue(algorithm.results)
        self.assertEqual(algorithm.schema_version, 2)
        self.assertEqual(algorithm.api_version, 2)
        self.assertEqual(algorithm.type, Algorithm.AUTONOMOUS)

        self.assertEqual(len(algorithm.results), 2)

        self.assertTrue("c" in algorithm.results)
        self.assertEqual(
            algorithm.results["c"], dict(type="plot/scatter/1", display=False)
        )

        self.assertTrue("v" in algorithm.results)
        self.assertEqual(algorithm.results["v"], dict(type="float32", display=True))

        runnable = algorithm.runner()
        self.assertFalse(runnable.ready)
        self.assertFalse(runnable.prepared)

    def test_load_valid_loop_evaluator(self):
        algorithm = Algorithm(prefix, "autonomous/loop_evaluator/1")
        self.assertEqual(algorithm.name, "autonomous/loop_evaluator/1")
        self.assertTrue(algorithm.valid, algorithm.errors)

        self.assertFalse(algorithm.errors)
        self.assertFalse(algorithm.results)  # it is not an analyzer
        self.assertTrue(algorithm.parameters)
        self.assertTrue(algorithm.input_map)
        self.assertTrue(algorithm.output_map)
        self.assertEqual(algorithm.schema_version, 3)
        self.assertEqual(algorithm.api_version, 2)
        self.assertEqual(algorithm.type, Algorithm.AUTONOMOUS_LOOP_EVALUATOR)

        runnable = algorithm.runner()
        self.assertFalse(runnable.ready)
        self.assertTrue(
            runnable.prepared
        )  # loop/1 has no prepare method so is prepared

    def test_load_valid_loop_processor(self):
        algorithm = Algorithm(prefix, "autonomous/loop_processor/1")
        self.assertEqual(algorithm.name, "autonomous/loop_processor/1")
        self.assertTrue(algorithm.valid, algorithm.errors)

        self.assertFalse(algorithm.errors)
        self.assertFalse(algorithm.results)  # it is not an analyzer
        self.assertFalse(algorithm.parameters)  # does not contain parameters
        self.assertTrue(algorithm.input_map)
        self.assertTrue(algorithm.output_map)
        self.assertEqual(algorithm.schema_version, 3)
        self.assertEqual(algorithm.api_version, 2)
        self.assertEqual(algorithm.type, Algorithm.AUTONOMOUS_LOOP_PROCESSOR)

        runnable = algorithm.runner()
        self.assertTrue(runnable.ready)
        self.assertTrue(runnable.prepared)


# ----------------------------------------------------------


class TestLegacyAPI_Setup(unittest.TestCase):
    def __init__(self, methodName="runTest"):
        super(TestLegacyAPI_Setup, self).__init__(methodName)
        self.username = "legacy"

    def test_setup_crashing_algorithm(self):
        algorithm = Algorithm(prefix, self.username + "/setup_crash/1")
        self.assertTrue(algorithm.valid, algorithm.errors)

        runnable = algorithm.runner()
        self.assertFalse(runnable.ready)

        with self.assertRaises(NameError):
            runnable.setup({})

    def test_setup_failing_algorithm(self):
        algorithm = Algorithm(prefix, self.username + "/setup_fail/1")
        self.assertTrue(algorithm.valid, algorithm.errors)

        runnable = algorithm.runner()
        self.assertFalse(runnable.ready)
        self.assertFalse(runnable.setup({}))
        self.assertFalse(runnable.ready)

    def test_setup_nonparametrized_algorithm(self):
        algorithm = Algorithm(prefix, self.username + "/no_setup/1")
        self.assertTrue(algorithm.valid, algorithm.errors)

        runnable = algorithm.runner()
        self.assertTrue(runnable.ready)
        self.assertTrue(runnable.setup({}))
        self.assertTrue(runnable.ready)

    def test_setup_parametrized_algorithm_default_values(self):
        algorithm = Algorithm(prefix, self.username + "/parametrized/1")
        self.assertTrue(algorithm.valid, algorithm.errors)

        runnable = algorithm.runner()
        self.assertFalse(runnable.ready)
        self.assertTrue(runnable.setup({}))
        self.assertTrue(runnable.ready)

        self.assertEqual(runnable.int8_value, 5)
        self.assertEqual(runnable.int8_range, 6)
        self.assertEqual(runnable.int16_value, 500)
        self.assertEqual(runnable.int16_range, 300)
        self.assertEqual(runnable.int32_value, 500000)
        self.assertEqual(runnable.int32_range, 500000)
        self.assertEqual(runnable.int64_value, 5000000000)
        self.assertEqual(runnable.int64_range, 5000000000)
        self.assertEqual(runnable.uint8_value, 5)
        self.assertEqual(runnable.uint8_range, 6)
        self.assertEqual(runnable.uint16_value, 500)
        self.assertEqual(runnable.uint16_range, 500)
        self.assertEqual(runnable.uint32_value, 500000)
        self.assertEqual(runnable.uint32_range, 500000)
        self.assertEqual(runnable.uint64_value, 5000000000)
        self.assertEqual(runnable.uint64_range, 5000000000)
        self.assertEqual(runnable.float32_value, 0.0)
        self.assertEqual(runnable.float32_range, 0.0)
        self.assertEqual(runnable.float64_value, 0.0)
        self.assertEqual(runnable.float64_range, 0.0)
        self.assertEqual(runnable.bool_value, True)
        self.assertEqual(runnable.string_value, "choice1")

    def test_setup_parametrized_algorithm_customized_values(self):
        algorithm = Algorithm(prefix, self.username + "/parametrized/1")
        self.assertTrue(algorithm.valid, algorithm.errors)

        runnable = algorithm.runner()
        self.assertFalse(runnable.ready)

        self.assertTrue(
            runnable.setup(
                dict(
                    int8_value=10,
                    int8_range=10,
                    float32_value=5.0,
                    float32_range=5.0,
                    bool_value=False,
                    string_value="choice2",
                )
            )
        )
        self.assertTrue(runnable.ready)

        self.assertEqual(runnable.int8_value, 10)
        self.assertEqual(runnable.int8_range, 10)
        self.assertEqual(runnable.int16_value, 500)
        self.assertEqual(runnable.int16_range, 300)
        self.assertEqual(runnable.int32_value, 500000)
        self.assertEqual(runnable.int32_range, 500000)
        self.assertEqual(runnable.int64_value, 5000000000)
        self.assertEqual(runnable.int64_range, 5000000000)
        self.assertEqual(runnable.uint8_value, 5)
        self.assertEqual(runnable.uint8_range, 6)
        self.assertEqual(runnable.uint16_value, 500)
        self.assertEqual(runnable.uint16_range, 500)
        self.assertEqual(runnable.uint32_value, 500000)
        self.assertEqual(runnable.uint32_range, 500000)
        self.assertEqual(runnable.uint64_value, 5000000000)
        self.assertEqual(runnable.uint64_range, 5000000000)
        self.assertEqual(runnable.float32_value, 5.0)
        self.assertEqual(runnable.float32_range, 5.0)
        self.assertEqual(runnable.float64_value, 0.0)
        self.assertEqual(runnable.float64_range, 0.0)
        self.assertEqual(runnable.bool_value, False)
        self.assertEqual(runnable.string_value, "choice2")

    def test_setup_parametrized_algorithm_out_of_range_value(self):
        algorithm = Algorithm(prefix, self.username + "/parametrized/1")
        self.assertTrue(algorithm.valid, algorithm.errors)

        runnable = algorithm.runner()
        self.assertFalse(runnable.ready)

        with self.assertRaises(ValueError):
            self.assertTrue(runnable.setup(dict(int8_range=100)))

    def test_setup_parametrized_algorithm_invalid_choice_value(self):
        algorithm = Algorithm(prefix, self.username + "/parametrized/1")
        self.assertTrue(algorithm.valid, algorithm.errors)

        runnable = algorithm.runner()
        self.assertFalse(runnable.ready)

        with self.assertRaises(ValueError):
            self.assertTrue(runnable.setup(dict(string_value="unknown")))


# ----------------------------------------------------------


class TestSequentialAPI_Setup(TestLegacyAPI_Setup):
    def __init__(self, methodName="runTest"):
        super(TestSequentialAPI_Setup, self).__init__(methodName)
        self.username = "sequential"


# ----------------------------------------------------------


class TestAutonomousAPI_Setup(TestLegacyAPI_Setup):
    def __init__(self, methodName="runTest"):
        super(TestAutonomousAPI_Setup, self).__init__(methodName)
        self.username = "sequential"


# ----------------------------------------------------------


class TestLegacyAPI_Prepare(unittest.TestCase):
    def test_always_prepared(self):
        algorithm = Algorithm(prefix, "legacy/valid_algorithm/1")
        self.assertTrue(algorithm.valid, algorithm.errors)

        runnable = algorithm.runner()
        self.assertTrue(runnable.prepared)
        self.assertTrue(runnable.prepare(DataLoaderList()))
        self.assertTrue(runnable.prepared)

    def test_prepare_warning(self):
        log_handler = MockLoggingHandler(level="DEBUG")
        logging.getLogger().addHandler(log_handler)
        log_messages = log_handler.messages

        algorithm = Algorithm(prefix, "legacy/prepare/1")
        self.assertTrue(algorithm.valid, algorithm.errors)

        runnable = algorithm.runner()
        self.assertTrue(runnable.prepared)
        self.assertTrue(runnable.prepare(DataLoaderList()))
        self.assertTrue(runnable.prepared)

        info_len = len(log_messages["warning"])
        self.assertEqual(info_len, 1)
        self.assertEqual(
            log_messages["warning"][info_len - 1],
            "Prepare is a reserved function name starting with API V2",
        )


# ----------------------------------------------------------


class TestSequentialAPI_Prepare(unittest.TestCase):
    def __init__(self, methodName="runTest"):
        super(TestSequentialAPI_Prepare, self).__init__(methodName)
        self.username = "sequential"

    def test_prepare_crashing_algorithm(self):
        algorithm = Algorithm(prefix, self.username + "/prepare_crash/1")
        self.assertTrue(algorithm.valid, algorithm.errors)

        runnable = algorithm.runner()
        self.assertTrue(runnable.ready)

        self.assertFalse(runnable.prepared)

        with self.assertRaises(NameError):
            runnable.prepare(DataLoaderList())

    def test_prepare_failing_algorithm(self):
        algorithm = Algorithm(prefix, self.username + "/prepare_fail/1")
        self.assertTrue(algorithm.valid, algorithm.errors)

        runnable = algorithm.runner()
        self.assertTrue(runnable.ready)

        self.assertFalse(runnable.prepared)
        self.assertFalse(runnable.prepare(DataLoaderList()))
        self.assertFalse(runnable.prepared)

    def test_no_preparation_algorithm(self):
        algorithm = Algorithm(prefix, self.username + "/no_prepare/1")
        self.assertTrue(algorithm.valid, algorithm.errors)

        runnable = algorithm.runner()
        self.assertTrue(runnable.ready)

        self.assertTrue(runnable.prepared)
        self.assertTrue(runnable.prepare(DataLoaderList()))
        self.assertTrue(runnable.prepared)


# ----------------------------------------------------------


class TestAutonomousAPI_Prepare(TestSequentialAPI_Prepare):
    def __init__(self, methodName="runTest"):
        super(TestAutonomousAPI_Prepare, self).__init__(methodName)
        self.username = "autonomous"


# ----------------------------------------------------------


class TestExecutionBase(unittest.TestCase):
    def setUp(self):
        self.filenames = {}

    def tearDown(self):
        for f in self.filenames.values():
            basename, ext = os.path.splitext(f)
            filenames = [f]
            filenames += glob.glob(basename + "*")
            for filename in filenames:
                if os.path.exists(filename):
                    os.unlink(filename)

    def writeData(self, input_name, indices, start_value):
        testfile = tempfile.NamedTemporaryFile(
            prefix=__name__ + input_name, suffix=".data"
        )
        testfile.close()  # preserve only the name
        self.filenames[input_name] = testfile.name

        dataformat = DataFormat(prefix, "user/single_integer/1")
        self.assertTrue(dataformat.valid)

        data_sink = CachedDataSink()
        self.assertTrue(
            data_sink.setup(
                self.filenames[input_name], dataformat, indices[0][0], indices[-1][1]
            )
        )

        for i in indices:
            data = dataformat.type()
            data.value = np.int32(start_value + i[0])
            data_sink.write(data, i[0], i[1])

        (nb_bytes, duration) = data_sink.statistics()
        self.assertTrue(nb_bytes > 0)
        self.assertTrue(duration > 0)

        data_sink.close()
        del data_sink


# ----------------------------------------------------------


class TestLegacyAPI_Process(TestExecutionBase):
    def create_io(self, infos):
        dataformat = DataFormat(prefix, "user/single_integer/1")

        synchronization_listener = SynchronizationListener()

        # Inputs
        inputs = InputList()

        for group_name, group_inputs in infos.items():
            if len(inputs) == 0:
                group = InputGroup(group_name, synchronization_listener, True)
            else:
                group = InputGroup(group_name, None, False)

            inputs.add(group)

            for input_name in group_inputs:
                data_source = CachedDataSource()
                data_source.setup(self.filenames[input_name], prefix)
                group.add(Input(input_name, dataformat, data_source))

        # Outputs
        outputs = OutputList()

        data_sink = MockDataSink(dataformat)
        outputs.add(Output("out", data_sink, synchronization_listener))

        return (inputs, outputs, data_sink)

    def test_process_crashing_algorithm(self):
        algorithm = Algorithm(prefix, "legacy/process_crash/1")
        self.assertTrue(algorithm.valid, algorithm.errors)

        runnable = algorithm.runner()
        self.assertTrue(runnable.ready)

        with self.assertRaises(NameError):
            runnable.process(inputs=InputList(), outputs=OutputList())

    def test_one_group_of_one_input(self):
        self.writeData("in", [(0, 0), (1, 1), (2, 2), (3, 3)], 1000)

        (inputs, outputs, data_sink) = self.create_io({"group1": ["in"]})

        algorithm = Algorithm(prefix, "legacy/echo/1")
        runner = algorithm.runner()

        group = inputs.main_group

        while group.hasMoreData():
            group.restricted_access = False
            group.next()
            group.restricted_access = True
            self.assertTrue(runner.process(inputs=inputs, outputs=outputs))

        self.assertEqual(len(data_sink.written), 4)

        for i in range(0, 4):
            self.assertEqual(data_sink.written[i].start, i)
            self.assertEqual(data_sink.written[i].end, i)
            self.assertEqual(data_sink.written[i].data.value, 1000 + i)

    def test_one_group_of_two_inputs_1(self):
        self.writeData("in1", [(0, 0), (1, 1), (2, 2), (3, 3)], 1000)
        self.writeData("in2", [(0, 1), (2, 3)], 2000)

        (inputs, outputs, data_sink) = self.create_io({"group1": ["in1", "in2"]})

        algorithm = Algorithm(prefix, "legacy/add/1")
        runner = algorithm.runner()

        self.assertTrue(runner.setup({"sync": "in1"}))

        group = inputs.main_group

        while group.hasMoreData():
            group.restricted_access = False
            group.next()
            group.restricted_access = True
            self.assertTrue(runner.process(inputs=inputs, outputs=outputs))

        self.assertEqual(len(data_sink.written), 4)

        data_unit = data_sink.written[0]
        self.assertEqual(data_unit.start, 0)
        self.assertEqual(data_unit.end, 0)
        self.assertEqual(data_unit.data.value, 3000)

        data_unit = data_sink.written[1]
        self.assertEqual(data_unit.start, 1)
        self.assertEqual(data_unit.end, 1)
        self.assertEqual(data_unit.data.value, 3001)

        data_unit = data_sink.written[2]
        self.assertEqual(data_unit.start, 2)
        self.assertEqual(data_unit.end, 2)
        self.assertEqual(data_unit.data.value, 3004)

        data_unit = data_sink.written[3]
        self.assertEqual(data_unit.start, 3)
        self.assertEqual(data_unit.end, 3)
        self.assertEqual(data_unit.data.value, 3005)

    def test_one_group_of_two_inputs_2(self):
        self.writeData("in1", [(0, 0), (1, 1), (2, 2), (3, 3)], 1000)
        self.writeData("in2", [(0, 1), (2, 3)], 2000)

        (inputs, outputs, data_sink) = self.create_io({"group1": ["in1", "in2"]})

        algorithm = Algorithm(prefix, "legacy/add/1")
        runner = algorithm.runner()

        self.assertTrue(runner.setup({"sync": "in2"}))

        group = inputs.main_group

        while group.hasMoreData():
            group.restricted_access = False
            group.next()
            group.restricted_access = True
            self.assertTrue(runner.process(inputs=inputs, outputs=outputs))

        self.assertEqual(len(data_sink.written), 2)

        data_unit = data_sink.written[0]
        self.assertEqual(data_unit.start, 0)
        self.assertEqual(data_unit.end, 1)
        self.assertEqual(data_unit.data.value, 3001)

        data_unit = data_sink.written[1]
        self.assertEqual(data_unit.start, 2)
        self.assertEqual(data_unit.end, 3)
        self.assertEqual(data_unit.data.value, 3005)

    def test_two_groups_of_one_input(self):
        self.writeData("in1", [(0, 0), (1, 1), (2, 2), (3, 3)], 1000)
        self.writeData("in2", [(0, 3)], 2000)

        (inputs, outputs, data_sink) = self.create_io(
            {"group1": ["in1"], "group2": ["in2"]}
        )

        algorithm = Algorithm(prefix, "legacy/add2/1")
        runner = algorithm.runner()

        group = inputs.main_group

        while group.hasMoreData():
            group.restricted_access = False
            group.next()
            group.restricted_access = True
            self.assertTrue(runner.process(inputs=inputs, outputs=outputs))

        self.assertEqual(len(data_sink.written), 4)

        data_unit = data_sink.written[0]
        self.assertEqual(data_unit.start, 0)
        self.assertEqual(data_unit.end, 0)
        self.assertEqual(data_unit.data.value, 3000)

        data_unit = data_sink.written[1]
        self.assertEqual(data_unit.start, 1)
        self.assertEqual(data_unit.end, 1)
        self.assertEqual(data_unit.data.value, 3001)

        data_unit = data_sink.written[2]
        self.assertEqual(data_unit.start, 2)
        self.assertEqual(data_unit.end, 2)
        self.assertEqual(data_unit.data.value, 3002)

        data_unit = data_sink.written[3]
        self.assertEqual(data_unit.start, 3)
        self.assertEqual(data_unit.end, 3)
        self.assertEqual(data_unit.data.value, 3003)


# ----------------------------------------------------------


class TestSequentialAPI_Process(TestExecutionBase):
    def create_io(self, infos):
        dataformat = DataFormat(prefix, "user/single_integer/1")

        synchronization_listener = SynchronizationListener()

        # Data loaders & inputs
        inputs = None
        data_loaders = DataLoaderList()

        for group_name, group_inputs in infos.items():
            if inputs is None:
                inputs = InputGroup(group_name, synchronization_listener, True)

                for input_name in group_inputs:
                    data_source = CachedDataSource()
                    data_source.setup(self.filenames[input_name], prefix)
                    inputs.add(Input(input_name, dataformat, data_source))

            else:
                data_loader = DataLoader(group_name)
                data_loaders.add(data_loader)

                for input_name in group_inputs:
                    cached_file = CachedDataSource()
                    cached_file.setup(self.filenames[input_name], prefix)
                    data_loader.add(input_name, cached_file)

        # Outputs
        outputs = OutputList()

        data_sink = MockDataSink(dataformat)
        outputs.add(Output("out", data_sink, synchronization_listener))

        return (data_loaders, inputs, outputs, data_sink)

    def test_process_crashing_algorithm(self):
        algorithm = Algorithm(prefix, "sequential/process_crash/1")
        self.assertTrue(algorithm.valid, algorithm.errors)

        runnable = algorithm.runner()
        self.assertTrue(runnable.ready)

        with self.assertRaises(NameError):
            runnable.process(
                inputs=InputList(), data_loaders=DataLoaderList(), outputs=OutputList()
            )

    def test_one_group_of_one_input(self):
        self.writeData("in", [(0, 0), (1, 1), (2, 2), (3, 3)], 1000)

        (data_loaders, inputs, outputs, data_sink) = self.create_io({"group1": ["in"]})

        algorithm = Algorithm(prefix, "sequential/echo/1")
        runner = algorithm.runner()

        self.assertTrue(runner.prepare(data_loaders=data_loaders))

        while inputs.hasMoreData():
            inputs.restricted_access = False
            inputs.next()
            inputs.restricted_access = True
            self.assertTrue(
                runner.process(
                    inputs=inputs, data_loaders=data_loaders, outputs=outputs
                )
            )

        self.assertEqual(len(data_sink.written), 4)

        for i in range(0, 4):
            self.assertEqual(data_sink.written[i].start, i)
            self.assertEqual(data_sink.written[i].end, i)
            self.assertEqual(data_sink.written[i].data.value, 1000 + i)

    def test_one_group_of_two_inputs_1(self):
        self.writeData("in1", [(0, 0), (1, 1), (2, 2), (3, 3)], 1000)
        self.writeData("in2", [(0, 1), (2, 3)], 2000)

        (data_loaders, inputs, outputs, data_sink) = self.create_io(
            {"group1": ["in1", "in2"]}
        )

        algorithm = Algorithm(prefix, "sequential/add/1")
        runner = algorithm.runner()

        self.assertTrue(runner.setup({"sync": "in1"}))

        self.assertTrue(runner.prepare(data_loaders=data_loaders))

        while inputs.hasMoreData():
            inputs.restricted_access = False
            inputs.next()
            inputs.restricted_access = True
            self.assertTrue(
                runner.process(
                    inputs=inputs, data_loaders=data_loaders, outputs=outputs
                )
            )

        self.assertEqual(len(data_sink.written), 4)

        data_unit = data_sink.written[0]
        self.assertEqual(data_unit.start, 0)
        self.assertEqual(data_unit.end, 0)
        self.assertEqual(data_unit.data.value, 3000)

        data_unit = data_sink.written[1]
        self.assertEqual(data_unit.start, 1)
        self.assertEqual(data_unit.end, 1)
        self.assertEqual(data_unit.data.value, 3001)

        data_unit = data_sink.written[2]
        self.assertEqual(data_unit.start, 2)
        self.assertEqual(data_unit.end, 2)
        self.assertEqual(data_unit.data.value, 3004)

        data_unit = data_sink.written[3]
        self.assertEqual(data_unit.start, 3)
        self.assertEqual(data_unit.end, 3)
        self.assertEqual(data_unit.data.value, 3005)

    def test_one_group_of_two_inputs_2(self):
        self.writeData("in1", [(0, 0), (1, 1), (2, 2), (3, 3)], 1000)
        self.writeData("in2", [(0, 1), (2, 3)], 2000)

        (data_loaders, inputs, outputs, data_sink) = self.create_io(
            {"group1": ["in1", "in2"]}
        )

        algorithm = Algorithm(prefix, "sequential/add/1")
        runner = algorithm.runner()

        self.assertTrue(runner.setup({"sync": "in2"}))

        self.assertTrue(runner.prepare(data_loaders=data_loaders))

        while inputs.hasMoreData():
            inputs.restricted_access = False
            inputs.next()
            inputs.restricted_access = True
            self.assertTrue(
                runner.process(
                    inputs=inputs, data_loaders=data_loaders, outputs=outputs
                )
            )

        self.assertEqual(len(data_sink.written), 2)

        data_unit = data_sink.written[0]
        self.assertEqual(data_unit.start, 0)
        self.assertEqual(data_unit.end, 1)
        self.assertEqual(data_unit.data.value, 3001)

        data_unit = data_sink.written[1]
        self.assertEqual(data_unit.start, 2)
        self.assertEqual(data_unit.end, 3)
        self.assertEqual(data_unit.data.value, 3005)

    def test_two_groups_of_one_input(self):
        self.writeData("in1", [(0, 0), (1, 1), (2, 2), (3, 3)], 1000)
        self.writeData("in2", [(0, 3)], 2000)

        (data_loaders, inputs, outputs, data_sink) = self.create_io(
            {"group1": ["in1"], "group2": ["in2"]}
        )

        algorithm = Algorithm(prefix, "sequential/add2/1")
        runner = algorithm.runner()

        self.assertTrue(runner.prepare(data_loaders=data_loaders))

        while inputs.hasMoreData():
            inputs.restricted_access = False
            inputs.next()
            inputs.restricted_access = True
            self.assertTrue(
                runner.process(
                    inputs=inputs, data_loaders=data_loaders, outputs=outputs
                )
            )

        self.assertEqual(len(data_sink.written), 4)

        data_unit = data_sink.written[0]
        self.assertEqual(data_unit.start, 0)
        self.assertEqual(data_unit.end, 0)
        self.assertEqual(data_unit.data.value, 3000)

        data_unit = data_sink.written[1]
        self.assertEqual(data_unit.start, 1)
        self.assertEqual(data_unit.end, 1)
        self.assertEqual(data_unit.data.value, 3001)

        data_unit = data_sink.written[2]
        self.assertEqual(data_unit.start, 2)
        self.assertEqual(data_unit.end, 2)
        self.assertEqual(data_unit.data.value, 3002)

        data_unit = data_sink.written[3]
        self.assertEqual(data_unit.start, 3)
        self.assertEqual(data_unit.end, 3)
        self.assertEqual(data_unit.data.value, 3003)

    def test_two_groups_of_related_inputs(self):
        self.writeData("value", [(0, 0), (1, 1), (2, 2), (3, 3)], 0)  # 0, 1, 2, 3
        self.writeData("offset_index", [(0, 0), (1, 2), (3, 3)], 0)  # 0, 1, 3
        self.writeData(
            "offset", [(0, 0), (1, 5), (6, 10), (11, 11)], 2000
        )  # 2000, 2001, 2006, 2011

        (data_loaders, inputs, outputs, data_sink) = self.create_io(
            {"group1": ["value", "offset_index"], "group2": ["offset"]}
        )

        algorithm = Algorithm(prefix, "sequential/add3/1")
        runner = algorithm.runner()

        self.assertTrue(runner.prepare(data_loaders=data_loaders))

        while inputs.hasMoreData():
            inputs.restricted_access = False
            inputs.next()
            inputs.restricted_access = True
            self.assertTrue(
                runner.process(
                    inputs=inputs, data_loaders=data_loaders, outputs=outputs
                )
            )

        self.assertEqual(len(data_sink.written), 4)

        data_unit = data_sink.written[0]
        self.assertEqual(data_unit.start, 0)
        self.assertEqual(data_unit.end, 0)
        self.assertEqual(data_unit.data.value, 2000)

        data_unit = data_sink.written[1]
        self.assertEqual(data_unit.start, 1)
        self.assertEqual(data_unit.end, 1)
        self.assertEqual(data_unit.data.value, 2002)

        data_unit = data_sink.written[2]
        self.assertEqual(data_unit.start, 2)
        self.assertEqual(data_unit.end, 2)
        self.assertEqual(data_unit.data.value, 2003)

        data_unit = data_sink.written[3]
        self.assertEqual(data_unit.start, 3)
        self.assertEqual(data_unit.end, 3)
        self.assertEqual(data_unit.data.value, 2014)


# ----------------------------------------------------------


class TestAutonomousAPI_Process(TestExecutionBase):
    def create_io(self, infos):
        dataformat = DataFormat(prefix, "user/single_integer/1")

        # Data loaders
        data_loaders = DataLoaderList()

        for group_name, group_inputs in infos.items():
            data_loader = DataLoader(group_name)
            data_loaders.add(data_loader)

            for input_name in group_inputs:
                cached_file = CachedDataSource()
                cached_file.setup(self.filenames[input_name], prefix)
                data_loader.add(input_name, cached_file)

        # Outputs
        outputs = OutputList()

        data_sink = MockDataSink(dataformat)
        outputs.add(Output("out", data_sink))

        return (data_loaders, outputs, data_sink)

    def test_process_crashing_algorithm(self):
        algorithm = Algorithm(prefix, "autonomous/process_crash/1")
        self.assertTrue(algorithm.valid, algorithm.errors)

        runnable = algorithm.runner()
        self.assertTrue(runnable.ready)

        with self.assertRaises(NameError):
            runnable.process(data_loaders=DataLoaderList(), outputs=OutputList())

    def test_one_group_of_one_input(self):
        self.writeData("in", [(0, 0), (1, 1), (2, 2), (3, 3)], 1000)

        (data_loaders, outputs, data_sink) = self.create_io({"group1": ["in"]})

        algorithm = Algorithm(prefix, "autonomous/echo/1")
        runner = algorithm.runner()

        self.assertTrue(runner.prepare(data_loaders=data_loaders.secondaries()))
        self.assertTrue(runner.process(data_loaders=data_loaders, outputs=outputs))

        self.assertEqual(len(data_sink.written), 4)

        for i in range(0, 4):
            self.assertEqual(data_sink.written[i].start, i)
            self.assertEqual(data_sink.written[i].end, i)
            self.assertEqual(data_sink.written[i].data.value, 1000 + i)

    def test_one_group_of_two_inputs_1(self):
        self.writeData("in1", [(0, 0), (1, 1), (2, 2), (3, 3)], 1000)
        self.writeData("in2", [(0, 1), (2, 3)], 2000)

        (data_loaders, outputs, data_sink) = self.create_io({"group1": ["in1", "in2"]})

        algorithm = Algorithm(prefix, "autonomous/add/1")
        runner = algorithm.runner()

        self.assertTrue(runner.setup({"sync": "in1"}))

        self.assertTrue(runner.prepare(data_loaders=data_loaders.secondaries()))
        self.assertTrue(runner.process(data_loaders=data_loaders, outputs=outputs))

        self.assertEqual(len(data_sink.written), 4)

        data_unit = data_sink.written[0]
        self.assertEqual(data_unit.start, 0)
        self.assertEqual(data_unit.end, 0)
        self.assertEqual(data_unit.data.value, 3000)

        data_unit = data_sink.written[1]
        self.assertEqual(data_unit.start, 1)
        self.assertEqual(data_unit.end, 1)
        self.assertEqual(data_unit.data.value, 3001)

        data_unit = data_sink.written[2]
        self.assertEqual(data_unit.start, 2)
        self.assertEqual(data_unit.end, 2)
        self.assertEqual(data_unit.data.value, 3004)

        data_unit = data_sink.written[3]
        self.assertEqual(data_unit.start, 3)
        self.assertEqual(data_unit.end, 3)
        self.assertEqual(data_unit.data.value, 3005)

    def test_one_group_of_two_inputs_2(self):
        self.writeData("in1", [(0, 0), (1, 1), (2, 2), (3, 3)], 1000)
        self.writeData("in2", [(0, 1), (2, 3)], 2000)

        (data_loaders, outputs, data_sink) = self.create_io({"group1": ["in1", "in2"]})

        algorithm = Algorithm(prefix, "autonomous/add/1")
        runner = algorithm.runner()

        self.assertTrue(runner.setup({"sync": "in2"}))

        self.assertTrue(runner.prepare(data_loaders=data_loaders.secondaries()))
        self.assertTrue(runner.process(data_loaders=data_loaders, outputs=outputs))

        self.assertEqual(len(data_sink.written), 2)

        data_unit = data_sink.written[0]
        self.assertEqual(data_unit.start, 0)
        self.assertEqual(data_unit.end, 1)
        self.assertEqual(data_unit.data.value, 3001)

        data_unit = data_sink.written[1]
        self.assertEqual(data_unit.start, 2)
        self.assertEqual(data_unit.end, 3)
        self.assertEqual(data_unit.data.value, 3005)

    def test_two_groups_of_one_input(self):
        self.writeData("in1", [(0, 0), (1, 1), (2, 2), (3, 3)], 1000)
        self.writeData("in2", [(0, 3)], 2000)

        (data_loaders, outputs, data_sink) = self.create_io(
            {"group1": ["in1"], "group2": ["in2"]}
        )

        algorithm = Algorithm(prefix, "autonomous/add2/1")
        runner = algorithm.runner()

        self.assertTrue(runner.prepare(data_loaders=data_loaders.secondaries()))
        self.assertTrue(runner.process(data_loaders=data_loaders, outputs=outputs))

        self.assertEqual(len(data_sink.written), 4)

        data_unit = data_sink.written[0]
        self.assertEqual(data_unit.start, 0)
        self.assertEqual(data_unit.end, 0)
        self.assertEqual(data_unit.data.value, 3000)

        data_unit = data_sink.written[1]
        self.assertEqual(data_unit.start, 1)
        self.assertEqual(data_unit.end, 1)
        self.assertEqual(data_unit.data.value, 3001)

        data_unit = data_sink.written[2]
        self.assertEqual(data_unit.start, 2)
        self.assertEqual(data_unit.end, 2)
        self.assertEqual(data_unit.data.value, 3002)

        data_unit = data_sink.written[3]
        self.assertEqual(data_unit.start, 3)
        self.assertEqual(data_unit.end, 3)
        self.assertEqual(data_unit.data.value, 3003)

    def test_two_groups_of_related_inputs(self):
        self.writeData("value", [(0, 0), (1, 1), (2, 2), (3, 3)], 0)  # 0, 1, 2, 3
        self.writeData("offset_index", [(0, 0), (1, 2), (3, 3)], 0)  # 0, 1, 3
        self.writeData(
            "offset", [(0, 0), (1, 5), (6, 10), (11, 11)], 2000
        )  # 2000, 2001, 2006, 2011

        (data_loaders, outputs, data_sink) = self.create_io(
            {"group1": ["value", "offset_index"], "group2": ["offset"]}
        )

        algorithm = Algorithm(prefix, "autonomous/add3/1")
        runner = algorithm.runner()

        self.assertTrue(runner.prepare(data_loaders=data_loaders.secondaries()))
        self.assertTrue(runner.process(data_loaders=data_loaders, outputs=outputs))

        self.assertEqual(len(data_sink.written), 4)

        data_unit = data_sink.written[0]
        self.assertEqual(data_unit.start, 0)
        self.assertEqual(data_unit.end, 0)
        self.assertEqual(data_unit.data.value, 2000)

        data_unit = data_sink.written[1]
        self.assertEqual(data_unit.start, 1)
        self.assertEqual(data_unit.end, 1)
        self.assertEqual(data_unit.data.value, 2002)

        data_unit = data_sink.written[2]
        self.assertEqual(data_unit.start, 2)
        self.assertEqual(data_unit.end, 2)
        self.assertEqual(data_unit.data.value, 2003)

        data_unit = data_sink.written[3]
        self.assertEqual(data_unit.start, 3)
        self.assertEqual(data_unit.end, 3)
        self.assertEqual(data_unit.data.value, 2014)
