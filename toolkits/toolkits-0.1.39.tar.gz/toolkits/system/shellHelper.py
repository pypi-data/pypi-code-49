# -*- coding: utf-8 -*-
import argparse
import os
import re
import sys
import traceback
import subprocess
import uuid
import arrow
import thread
from threading import Timer
import time
from log4python.Log4python import log
from multiprocessing import Process, current_process
from unipath import Path
from filesHelper import read_content

reload(sys)
logger = log("shellHelper")
sys.setdefaultencoding('utf8')


def change_the_path_split(file_path):
    path_split_str_win = "\\"
    path_split_str_linux = "/"
    if str(sys.platform).find("win") >= 0:
        path_final = str(file_path).replace(path_split_str_linux, path_split_str_win)
    else:
        path_final = str(file_path).replace(path_split_str_win, path_split_str_linux)
    return path_final


def include_path(target_root_directory, relative_path_list):
    for item in relative_path_list:
        item = change_the_path_split(item)
        path_parent = "%s/%s" % (target_root_directory, item)
        sys.path.append(path_parent)


def get_relative_directory_levels(script_file_path, relative_levels):
    path_cur = os.path.dirname(os.path.realpath(script_file_path))
    directory_target = "/.." * relative_levels
    target_root_path = "%s%s" % (path_cur, directory_target)
    return change_the_path_split(target_root_path)


def run_with_timeout(timeout, default, f, *args, **kwargs):
    if not timeout:
        return f(*args, **kwargs)
    timeout_timer = Timer(timeout, thread.interrupt_main)
    try:
        timeout_timer.start()
        result = f(*args, **kwargs)
        return result
    except KeyboardInterrupt:
        return default
    finally:
        timeout_timer.cancel()


def exec_cmd(cmd, work_path):
    exec_shell_with_pipe(cmd, work_path=work_path)


def worker(cmd, work_path):
    p = Process(target=exec_cmd, args=(cmd, work_path))
    p.start()
    os._exit(1)


def exec_external_cmd_background(cmd, work_path=""):
    p = Process(target=worker, args=(cmd, work_path))
    p.start()
    p.join()


def file_is_used(monitor_file):
    # fuser or lsof to check file's status
    cmd = "lsof %s" % monitor_file
    ret = exec_shell_with_pipe(cmd)
    if not ret:
        return True
    else:
        return False


def exec_shell_with_pipe(cmd, timeout=0, work_path=""):
    """exeShellWithPipe("grep 'processor' /proc/cpuinfo | sort -u | wc -l")

return-val
     output-lines-list  # line list ['output_01', 'output_02']

    :param work_path:
    :param timeout:
    :param cmd:  exec command
    """
    result = []
    none_num = 0
    if cmd == "" or cmd is None:
        return "No Cmd Input"
    if work_path == "":
        scan_process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    else:
        scan_process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=work_path)
    while True:
        if none_num > 3:
            break
        if timeout != 0:
            ret = run_with_timeout(timeout, None, scan_process.stdout.readline)
        else:
            ret = scan_process.stdout.readline()
        if ret == "" or ret is None:
            none_num += 1
        else:
            result.append(ret.strip())
            none_num = 0
    return result


def exec_shell(cmd, timeout=0, bufsize=0, executable=None,
               stdin=None, stdout=None, stderr=None,
               preexec_fn=None, close_fds=False, shell=False,
               cwd=None, env=None, universal_newlines=False,
               startupinfo=None, creationflags=0):
    """exec_shell("grep 'processor' /proc/cpuinfo | sort -u | wc -l")


return-code::

    ret = {
        "exit_code": return_code,  # 0 or -1
        "stdout": stdout_msg,  # line list ['output_01', 'output_02']
        "stderr": stderr_msg   # line list ['output_01', 'output_02']
    }
code-end

    :param preexec_fn:
    :type stdin: object
    :param executable:
    :param cwd:
    :param timeout:
    :param cmd:  exec command
    :return: return a dict to caller

    """
    if cmd == "" or cmd is None:
        return "No Cmd Input"

    fp_out = subprocess.PIPE
    fp_err = subprocess.PIPE
    stdout = "/tmp/stdout_%s" % str(uuid.uuid4()).replace("-", "").upper()
    stderr = "/tmp/stderr_%s" % str(uuid.uuid4()).replace("-", "").upper()
    if stdout:
        fp_out = open(stdout, "w+")
    if stderr:
        fp_err = open(stderr, "w+")

    scan_process = subprocess.Popen(cmd, shell=True, stdout=fp_out, stderr=fp_err, cwd=cwd, bufsize=bufsize,
                                    executable=executable, stdin=stdin,
                                    preexec_fn=preexec_fn, close_fds=close_fds,
                                    env=env, universal_newlines=universal_newlines,
                                    startupinfo=startupinfo, creationflags=creationflags)

    return_code = None
    while True:
        return_code = scan_process.poll()
        if return_code is None:
            time.sleep(1)
        else:
            break

    fp_out.close()
    fp_err.close()
    stdout_msg = read_content(stdout)
    stderr_msg = read_content(stderr)
    Path(stderr).remove()
    Path(stdout).remove()

    ret = {
        "exit_code": return_code,
        "stdout": stdout_msg,
        "stderr": stderr_msg
    }
    return ret


if __name__ == '__main__':
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument("logFile", type=str, help="specify the log file's path")
        args = parser.parse_args()
        print(args.logFile)
        exec_shell()
    except Exception, ex:
        logger.debug("Error: %s" % ex)
        logger.debug(traceback.format_exc())