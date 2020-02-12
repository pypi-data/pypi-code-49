import subprocess
import os
import sys
import traceback
import glob
from os.path import join
from multiprocessing import Pool, Value
import multiprocessing
import time
from termcolor import cprint
from threading import Thread
from queue import Queue, Empty

from msbase.logging import logger

def timed(func):
    def function_wrapper(*args, **kwargs):
        now = time.time()
        ret = func(*args, **kwargs)
        logger.info("%s(%s, %s) spent %.2fs" %
                     (func.__qualname__, args, kwargs, time.time() - now))
        return ret
    return function_wrapper

ON_POSIX = 'posix' in sys.builtin_module_names

def enqueue_output(out, queue):
    for line in iter(out.readline, b''):
        queue.put(line)
    out.close()

def call_std(args, cwd=None, env={}, output=True, timeout_s=None):
    if output:
        p = subprocess.Popen(args, stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE, bufsize=1,
                             close_fds=ON_POSIX, cwd=cwd, env=dict(os.environ, **env))
        start_time = time.time()
        stdout = ""
        q_stdout = Queue()
        t_stdout = Thread(target=enqueue_output, args=(p.stdout, q_stdout))
        t_stdout.daemon = True
        t_stdout.start()
        stderr = ""
        q_stderr = Queue()
        t_stderr = Thread(target=enqueue_output, args=(p.stderr, q_stderr))
        t_stderr.daemon = True
        t_stderr.start()
        while True:
            return_code = p.poll()
            if return_code is not None:
                break
            try:
                stdout_line = str(q_stdout.get_nowait(), "utf-8")
            except Empty:
                stdout_line = ''
            try:
                stderr_line = str(q_stderr.get_nowait(), "utf-8")
            except Empty:
                stderr_line = ''
            if stdout_line:
                stdout += stdout_line
                logger.info(stdout_line.rstrip())
            if stderr_line:
                stderr += stderr_line
                logger.warning(stderr_line.rstrip())
            if timeout_s is not None and time.time() - start_time > timeout_s:
                p.kill()
                return (-1, "", "TIMEOUT!")
        while True:
            try:
                stdout_line = str(q_stdout.get(timeout=.1), "utf-8")
            except Empty:
                break
            stdout += stdout_line
            logger.info(stdout_line.rstrip())
            if timeout_s is not None and time.time() - start_time > timeout_s:
                p.kill()
                return (-1, "", "TIMEOUT!")
        while True:
            try:
                stderr_line = str(q_stderr.get(timeout=.1), "utf-8")
            except Empty:
                break
            stderr += stderr_line
            logger.warning(stderr_line.rstrip())
            if timeout_s is not None and time.time() - start_time > timeout_s:
                p.kill()
                return (-1, "", "TIMEOUT!")
        return (return_code, stdout, stderr)
    else:
        proc = subprocess.Popen(args, cwd=cwd, stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE, env=dict(os.environ, **env))
        code = proc.wait(timeout=timeout_s)
        return (code, proc.stdout, proc.stderr)

class CallStdException(Exception):
    def __init__(self, code, stdout, stderr):
        super().__init__("%s\n%s\n%s" % (code, stdout, stderr))
        self.code = code
        self.stdout = stdout
        self.stderr = stderr

@timed
def try_call_std(args, cwd=None, env={}, print_cmd=True, output=True, noexception=False, timeout_s=None):
    '''An asynchronously logged process executor
    that returns essential information all you need
    '''
    if print_cmd:
        cprint("+ " + " ".join(args), "blue")
    code, stdout, stderr = call_std(args, cwd, env, output, timeout_s=timeout_s)
    if not noexception and code != 0:
        raise Exception(CallStdException(code, stdout, stderr))
    else:
        return stdout, stderr, code

def multiprocess(task, inputs, n: int, verbose=True, return_dict=True, throws=False, debug_mode=False):
    '''How to use this effectively:
    1. Use debug_mode=True to switch to tracked for-loop
    '''
    if debug_mode:
        results = []
        for arg in inputs:
            start_time = time.time()
            logger.info("Working on %s" % arg)
            results.append(task(arg))
            logger.info("Time spent: %.2f" % (time.time() - start_time))
        return results
    counter = Value('i', 0)
    total = float(len(inputs))
    start_time = time.time()

    global run
    def run(input):
        with counter.get_lock():
            if verbose:
                logger.info("%fs - progress: %f" % (time.time() - start_time, counter.value / total))
            counter.value += 1
        try:
            return (True, task(input))
        except Exception as e:
            return (False, "%s\n%s" % (e, traceback.format_exc()))

    with Pool(n) as p:
        results = p.map(run, inputs)
        if verbose:
            logger.info("total spent time: %f" % (time.time() - start_time))
        if throws:
            ret = []
            for ok, r in results:
                if not ok:
                    raise Exception(str(r))
                ret.append(r)
            return ret
        if return_dict:
            return dict(zip(inputs, results))
        else:
            return results

