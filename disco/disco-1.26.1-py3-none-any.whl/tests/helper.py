#  Copyright (c) 2019 Samsung, Inc. and its affiliates.
#
#  This source code is licensed under the RESTRICTED license found in the
#  LICENSE file in the root directory of this source tree.

import glob
import inspect
import os
import sys
from zipfile import ZipFile
import decorator
import dill
import time
from disco import asset, Job
import requests
SCRIPT_PICKLE_RESULT = """
with open('run-result/result.pickle', 'wb') as f_result:
    dill.dump(result, f_result)   
"""

SCRIPT_HEADER_OPEN_ARGS = """
import sys, dill
from os import listdir
import os
os.environ['is_remote']='yes'
with open(sys.argv[1], "rb") as f_arg:
    arg = dill.load(f_arg)
"""

SCRIPT_HEADER_OPEN_PICKLED_MODULE = """
with open('customer-module.pickle', 'rb') as f_module:
    module = dill.load(f_module)
"""


def create_stand_alone_script(func):
    if not func:
        return None
    if not inspect.isfunction(func):
        return None
    source = inspect.getsourcefile(func)
    func_name = func.__name__
    with open(source, "r") as f:
        sourcecode = '#!/usr/bin/python3.6\n' if (
                sys.version_info >= (3, 0)) else '#!/usr/bin/python2.7\n'
        sourcecode += SCRIPT_HEADER_OPEN_ARGS
        sourcecode += f.read()
        sourcecode += str.format("result = {}(*arg)\n", func_name)
        sourcecode += SCRIPT_PICKLE_RESULT
    return sourcecode


def create_input_file(arg):
    return dill.dumps(arg, byref=False, recurse=True, protocol=0)


@decorator.decorator
def disco_job(func, name_of_job=None, *args, **kwargs):
    if os.environ.get("is_remote") == "yes":
        return func(*args, **kwargs)

    job_name = name_of_job if name_of_job else func.__name__ + str(time.time())
    script = create_stand_alone_script(func)
    input_file = create_input_file(args)

    # TODO: Enable a client to specify a cluster ID
    script_file_id = asset.upload_file(str(job_name) + '.py', script, show_progress_bar=False)
    input_file_id = asset.upload_file(str(job_name) + 'input.pickle', input_file, show_progress_bar=False)
    job = Job.create(script_file_id, [input_file_id], [], job_name)
    job.start()
    task_result = job.get_results(block=True)
    if task_result:
        for file_name, content in task_result[0].get_raw_result():
            if file_name == 'result.pickle':
                return dill.loads(content)
    else:
        print("no task result")
        return None


@disco_job
def add(x, y):
    return x + y
