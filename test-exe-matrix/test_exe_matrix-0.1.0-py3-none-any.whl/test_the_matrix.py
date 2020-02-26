"""test output
"""
import os
import tempfile
import subprocess
import threading
import time


ENCODING = "utf-8"
TIMEOUT = 1  # second


class Utils:
    @staticmethod
    def decode_out(filename):
        with open(filename, "r", encoding=ENCODING) as open_file_desc:
            return open_file_desc.read()


class ExeThread(threading.Thread):
    def __init__(self, exe, args):
        self.exe = exe
        self.args = args

        self.process = None
        self.retcode = None
        self.stdout = None
        self.stderr = None

        super().__init__()

    def run(self):
        command = [self.exe] + self.args

        temp_dir_manager = temp_dir_manager_gen()
        artifacts = next(temp_dir_manager)

        self.process = subprocess.Popen(
            command, stdout=artifacts["stdoutbuf"], stderr=artifacts["stderrbuf"],
        )

        self.process.wait()

        for open_file in ("stdoutbuf", "stderrbuf"):
            artifacts[open_file].close()

        self.retcode = self.process.returncode
        self.stdout = Utils.decode_out(artifacts["stdoutname"])
        self.stderr = Utils.decode_out(artifacts["stderrname"])

        try:
            next(temp_dir_manager)
        except StopIteration:
            # this is ugly but expected
            pass


def temp_dir_manager_gen():
    """
    Creates/cleanup a tempdir and 2 tempfiles to store process output

    implementation detail: this is a generator generating only one value, so we
    have automatic cleaning up after us.
    """
    with tempfile.TemporaryDirectory(prefix="test_exe_matrix-") as tmpdirname:
        stdout_fname = os.path.join(tmpdirname, "stdout")
        stderr_fname = os.path.join(tmpdirname, "stderr")
        with open(stdout_fname, "wb") as stdout_buf, open(
            stderr_fname, "wb"
        ) as stderr_buf:

            yield {
                "stdoutname": stdout_fname,
                "stderrname": stderr_fname,
                "stdoutbuf": stdout_buf,
                "stderrbuf": stderr_buf,
            }


def test_one_situation(exetest):
    starttime = time.time()
    exethread = ExeThread(exetest["exe"], exetest.get("args", []))

    exethread.start()
    timeout = exetest["timeout"]

    while True:

        if exethread.retcode is not None:
            break

        time.sleep(0.1)
        now = time.time()
        duration = now - starttime
        try:
            assert duration < timeout, "Exe took too long"
        except AssertionError:
            exethread.process.kill()
            if exetest.get("expect_too_long", False):
                return
            raise

    assert not exetest.get("expect_too_long", False), "Execution should have timed out"

    if "partstdout" in exetest:
        expected_partstdout = exetest["partstdout"]
        assert (
            expected_partstdout in exethread.stdout
        ), f"Did not find substring '{expected_partstdout}' in '{exethread.stdout}'"

    if "partstderr" in exetest:
        assert exetest["partstderr"] in exethread.stderr

    if "stdout" in exetest:
        assert exetest["stdout"] == exethread.stdout

    if "stderr" in exetest:
        assert exetest["stderr"] == exethread.stderr

    if "retcode" in exetest:
        expected_retcode = exetest["retcode"]
        assert expected_retcode == exethread.retcode, (
            f"expected retcode is {expected_retcode}, but process ended with"
            f"code {exethread.retcode}"
        )
