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
import glob
import logging
import nose.tools
import subprocess as sp  # nosec

from shutil import rmtree

from ..experiment import Experiment
from ..execution import LocalExecutor
from ..execution import SubprocessExecutor
from ..hash import hashFileContents
from ..hash import hashDataset
from ..hash import toPath
from ..data import CachedDataSource

from . import prefix, tmp_prefix
from .utils import slow


logger = logging.getLogger(__name__)


# ----------------------------------------------------------
# Helpers


def create_conda_environment(additional_packages=[]):
    environment_name = "subprocess_environment"
    environment_prefix = os.path.join(tmp_prefix, environment_name)
    packages = ["python=3"] + additional_packages
    sp.run(
        [
            "conda",
            "create",
            "-y",
            "-c",
            "defaults",
            "-c",
            "http://www.idiap.ch/software/bob/conda/",
            "--prefix",
            environment_prefix,
        ]
        + packages,
        check=True,
        stdout=sp.PIPE,
        stderr=sp.PIPE,
    )
    return environment_prefix


def clear_conda_environment(environment_prefix):
    rmtree(environment_prefix)


# ----------------------------------------------------------


class BaseExecutionMixIn(object):
    def check_output(self, prefix, path):
        """Checks if a given output exists, together with its indexes and checksums
        """

        finalpath = os.path.join(prefix, path)
        datafiles = glob.glob(finalpath + "*.data")
        datachksums = glob.glob(finalpath + "*.data.checksum")
        indexfiles = glob.glob(finalpath + "*.index")
        indexchksums = glob.glob(finalpath + "*.index.checksum")

        nose.tools.assert_true(datafiles)
        nose.tools.eq_(len(datafiles), len(indexfiles))
        for k in datafiles + indexfiles:
            checksum_file = k + ".checksum"
            nose.tools.assert_true(checksum_file in datachksums + indexchksums)
            stored_checksum = None
            with open(checksum_file, "rt") as f:
                stored_checksum = f.read().strip()
            current_checksum = hashFileContents(k)
            nose.tools.eq_(current_checksum, stored_checksum)

    def load_result(self, executor):
        """Loads the result of an experiment, in a single go"""

        f = CachedDataSource()
        nose.tools.assert_true(
            f.setup(
                os.path.join(executor.cache, executor.data["result"]["path"] + ".data"),
                executor.prefix,
            )
        )

        data, start, end = f[0]
        nose.tools.eq_(start, 0)
        nose.tools.assert_true(end >= start)
        f.close()
        return data

    def execute(self, label, expected_result, **kwargs):
        """Executes the full experiment, block after block, returning results. If an
        error occurs, returns information about the err'd block. Otherwise, returns
        ``None``.

        This bit of code mimics the scheduler, but does everything on the local
        machine. It borrows some code from the package ``beat.cmdline``.
        """

        executor_parameters = kwargs.pop("executor_parameters", {})

        dataformat_cache = {}
        database_cache = {}
        algorithm_cache = {}

        experiment = Experiment(
            prefix, label, dataformat_cache, database_cache, algorithm_cache
        )

        nose.tools.assert_true(
            experiment.valid, "\n  * %s" % "\n  * ".join(experiment.errors)
        )

        for block_name, infos in experiment.datasets.items():
            view = infos["database"].view(infos["protocol"], infos["set"])
            filename = toPath(
                hashDataset(infos["database"].name, infos["protocol"], infos["set"]),
                suffix=".db",
            )
            view.index(os.path.join(tmp_prefix, filename))

        scheduled = experiment.setup()

        # can we execute it?
        results = []
        for key, value in scheduled.items():
            configuration = {**value["configuration"], **kwargs}

            executor = self.create_executor(
                prefix,
                configuration,
                tmp_prefix,
                dataformat_cache,
                database_cache,
                algorithm_cache,
                **executor_parameters
            )
            nose.tools.assert_true(
                executor.valid, "\n  * %s" % "\n  * ".join(executor.errors)
            )

            with executor:
                result = executor.process(timeout_in_minutes=3)
                nose.tools.assert_true(result)
                nose.tools.assert_true("status" in result)
                nose.tools.assert_true("stdout" in result)
                nose.tools.assert_true("stderr" in result)
                nose.tools.assert_true("timed_out" in result)
                nose.tools.assert_true("system_error" in result)
                nose.tools.assert_true("user_error" in result)
                if result["status"] != 0:
                    logger.warn("status: %i", result["status"])
                    logger.warn("(eventual) system errors: %s", result["system_error"])
                    logger.warn("(eventual) user errors: %s", result["user_error"])
                    logger.warn("stdout: %s", result["stdout"])
                    logger.warn("stderr: %s", result["stderr"])
                    return result
                if result["system_error"]:
                    logger.warn("system errors: %s", result["system_error"])
                    return result
                nose.tools.eq_(result["status"], 0)

                if "statistics" in result:
                    nose.tools.assert_true(isinstance(result["statistics"], dict))

            if executor.analysis:
                self.check_output(tmp_prefix, executor.data["result"]["path"])
                results.append(self.load_result(executor))
            else:
                for name, details in executor.data["outputs"].items():
                    self.check_output(tmp_prefix, details["path"])

        # compares all results
        nose.tools.assert_true(results)

        for k, result in enumerate(results):
            expected = result.__class__()
            expected.from_dict(expected_result[k], casting="unsafe")  # defaults=False

            nose.tools.assert_true(
                result.isclose(expected),
                "%r is not close enough to %r" % (result.as_dict(), expected.as_dict()),
            )

    @slow
    def test_integers_addition_1(self):
        nose.tools.assert_is_none(
            self.execute(
                "user/user/integers_addition/1/integers_addition",
                [{"sum": 495, "nb": 9}],
            )
        )

    @slow
    def test_integers_addition_2(self):
        nose.tools.assert_is_none(
            self.execute(
                "user/user/integers_addition/2/integers_addition",
                [{"sum": 4995, "nb": 9}],
            )
        )

    @slow
    def test_single_1_single(self):
        nose.tools.assert_is_none(
            self.execute("user/user/single/1/single", [{"out_data": 42}])
        )

    @slow
    def test_single_1_add(self):
        nose.tools.assert_is_none(
            self.execute("user/user/single/1/single_add", [{"out_data": 43}])
        )

    @slow
    def test_single_1_add2(self):
        nose.tools.assert_is_none(
            self.execute("user/user/single/1/single_add2", [{"out_data": 44}])
        )

    @slow
    def test_single_1_error(self):
        result = self.execute("errors/user/single/1/single_error", [None])
        nose.tools.assert_true(result)
        nose.tools.eq_(result["status"], 1)
        nose.tools.assert_true(result["user_error"])
        nose.tools.assert_true("NameError" in result["user_error"])
        nose.tools.eq_(result["system_error"], "")

    @slow
    def test_single_1_crash(self):
        result = self.execute("errors/user/single/1/single_crash", [None])
        nose.tools.assert_true(result)
        nose.tools.eq_(result["status"], 1)
        nose.tools.assert_true(result["user_error"])
        nose.tools.assert_true("NameError" in result["user_error"])
        nose.tools.eq_(result["system_error"], "")

    @slow
    def test_single_1_db_crash(self):
        result = self.execute("errors/user/single/1/single_db_crash", [None])
        nose.tools.assert_true(result)
        nose.tools.assert_not_equal(result["status"], 0)
        nose.tools.assert_true(result["user_error"])
        nose.tools.assert_true("a = b" in result["user_error"])
        nose.tools.eq_(result["system_error"], "")

    @slow
    def test_single_1_large(self):
        nose.tools.assert_is_none(
            self.execute("user/user/single/1/single_large", [{"out_data": 2.0}])
        )

    @slow
    def test_double_1(self):
        nose.tools.assert_is_none(
            self.execute("user/user/double/1/double", [{"out_data": 42}])
        )

    @slow
    def test_triangle_1(self):
        nose.tools.assert_is_none(
            self.execute("user/user/triangle/1/triangle", [{"out_data": 42}])
        )

    @slow
    def test_too_many_nexts(self):
        result = self.execute("errors/user/triangle/1/too_many_nexts", [None])
        nose.tools.assert_true(result)
        nose.tools.assert_not_equal(result["status"], 0)
        nose.tools.assert_true(result["user_error"])
        nose.tools.assert_true("no more data" in result["user_error"])

    @slow
    def test_double_triangle_1(self):
        nose.tools.assert_is_none(
            self.execute(
                "user/user/double_triangle/1/double_triangle", [{"out_data": 42}]
            )
        )

    @slow
    def test_inputs_mix_1(self):
        nose.tools.assert_is_none(
            self.execute("user/user/inputs_mix/1/test", [{"sum": 495, "nb": 9}])
        )

    @slow
    def test_inputs_mix_2(self):
        nose.tools.assert_is_none(
            self.execute("user/user/inputs_mix/2/test", [{"sum": 495, "nb": 9}])
        )

    @slow
    def test_inputs_mix_3(self):
        nose.tools.assert_is_none(
            self.execute("user/user/inputs_mix/3/test", [{"sum": 945, "nb": 9}])
        )

    @slow
    def test_inputs_mix_3b(self):
        nose.tools.assert_is_none(
            self.execute("user/user/inputs_mix/3/test2", [{"sum": 954, "nb": 9}])
        )

    @slow
    def test_inputs_mix_4(self):
        nose.tools.assert_is_none(
            self.execute("user/user/inputs_mix/4/test", [{"sum": 990, "nb": 9}])
        )

    @slow
    def test_inputs_mix_4b(self):
        nose.tools.assert_is_none(
            self.execute("user/user/inputs_mix/4/test2", [{"sum": 1008, "nb": 9}])
        )

    @slow
    def test_integers_labelled_1(self):
        nose.tools.assert_is_none(
            self.execute(
                "user/user/integers_labelled/1/test",
                [{"nb_data_units": 3, "indices": "0 - 4\n5 - 9\n10 - 14\n"}],
            )
        )

    @slow
    def test_preprocessing_1(self):
        nose.tools.assert_is_none(
            self.execute(
                "user/user/preprocessing/1/different_frequencies",
                [{"sum": 363, "nb": 8}],
            )
        )

    @slow
    def test_single_1_prepare_success(self):
        nose.tools.assert_is_none(
            self.execute("user/user/single/1/prepare_success", [{"out_data": 42}])
        )

    @slow
    def test_loop_1(self):
        nose.tools.assert_is_none(
            self.execute(
                "user/user/loop/1/loop", [{"sum": 135, "nb": 9}, {"sum": 9, "nb": 9}]
            )
        )

    @slow
    def test_two_loops_1(self):
        nose.tools.assert_is_none(
            self.execute(
                "user/user/two_loops/1/two_loops",
                [{"sum": 621, "nb": 9}, {"sum": 108, "nb": 9}],
            )
        )

    # For benchmark purposes
    # @slow
    # def test_double_1_large(self):
    #     import time
    #     start = time.time()
    #     assert self.execute('user/user/double/1/large', [{'out_data': 49489830}]) is None
    #     print(time.time() - start)

    # For benchmark purposes
    # @slow
    # def test_double_1_large2(self):
    #     import time
    #     start = time.time()
    #     assert self.execute('user/user/double/1/large2', [{'out_data': 21513820}]) is None
    #     print(time.time() - start)


# ----------------------------------------------------------


class TestLocalExecution(BaseExecutionMixIn):
    def create_executor(
        self,
        prefix,
        configuration,
        tmp_prefix,
        dataformat_cache,
        database_cache,
        algorithm_cache,
        **kwargs
    ):
        return LocalExecutor(
            prefix,
            configuration,
            tmp_prefix,
            dataformat_cache,
            database_cache,
            algorithm_cache,
        )

    @slow
    def test_single_1_prepare_error(self):
        with nose.tools.assert_raises(RuntimeError) as context:
            self.execute("errors/user/single/1/prepare_error", [None])
            nose.tools.assert_true("Algorithm prepare failed" in context.exception)

    @slow
    def test_single_1_setup_error(self):
        with nose.tools.assert_raises(RuntimeError) as context:
            self.execute("errors/user/single/1/setup_error", [None])
            nose.tools.assert_true("Algorithm setup failed" in context.exception)


# ----------------------------------------------------------


class TestSubprocessExecution(BaseExecutionMixIn):
    def create_executor(
        self,
        prefix,
        configuration,
        tmp_prefix,
        dataformat_cache,
        database_cache,
        algorithm_cache,
        python_path=None,
    ):
        return SubprocessExecutor(
            prefix=prefix,
            data=configuration,
            cache=tmp_prefix,
            dataformat_cache=dataformat_cache,
            database_cache=database_cache,
            algorithm_cache=algorithm_cache,
            python_path=python_path,
        )

    @slow
    def test_single_1_prepare_error(self):
        result = self.execute("errors/user/single/1/prepare_error", [None])

        nose.tools.eq_(result["status"], 1)
        nose.tools.eq_(
            result["user_error"], "'Could not prepare algorithm (returned False)'"
        )

    @slow
    def test_single_1_setup_error(self):
        result = self.execute("errors/user/single/1/setup_error", [None])

        nose.tools.eq_(result["status"], 1)
        nose.tools.eq_(
            result["user_error"], "'Could not setup algorithm (returned False)'"
        )

    @slow
    def test_different_environment(self):
        environment_prefix = create_conda_environment(["beat.backend.python"])
        result = self.execute(
            "user/user/loop/1/loop",
            [{"sum": 135, "nb": 9}, {"sum": 9, "nb": 9}],
            executor_parameters={
                "python_path": os.path.join(environment_prefix, "bin", "python")
            },
        )
        clear_conda_environment(environment_prefix)

        nose.tools.assert_is_none(result)

    @slow
    def test_wrong_different_environment(self):
        environment_prefix = create_conda_environment()
        with nose.tools.assert_raises(RuntimeError):
            self.execute(
                "user/user/loop/1/loop",
                [{"sum": 135, "nb": 9}, {"sum": 9, "nb": 9}],
                executor_parameters={
                    "python_path": os.path.join(environment_prefix, "bin", "python")
                },
            )
        clear_conda_environment(environment_prefix)
