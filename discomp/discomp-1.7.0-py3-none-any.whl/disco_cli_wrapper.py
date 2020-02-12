# /**
#  * Copyright (c) Samsung, Inc. and its affiliates.
#  *
#  * This source code is licensed under the RESTRICTED license found in the
#  * LICENSE file in the root directory of this source tree.
#  */
import os
from time import sleep

from . import utils


def disco_login():
    user = os.environ.get('DISCO_LOGIN_USER')
    password = os.environ.get('DISCO_LOGIN_PASSWORD')
    if (user is None or password is None):
        print('Please use your credentials to login to dis.co')
        return False

    login_success_output = 'Signed in successfully'
    # 'Login' to cli 
    output = utils.send_command(['disco', 'login', '-u', user, '-p', password], False)
    if login_success_output in output:
        return True
    else:
        print('%s' % output)
        return False


def disco_cli(cmd_args, print_output=True, input=''):
    if disco_login():
        output = utils.send_command(cmd_args, print_output, input)
        return output
    else:
        return "Not logged in"


def add_job_request(job_name, temp_dir=".", wait=False):
    machine_size = os.environ.get('DISCO_MACHINE_SIZE')
    cluster_id = os.environ.get('DISCO_CLUSTER_ID')
    docker_image_id = os.environ.get('DOCKER_IMAGE_ID')
    script_name = temp_dir + "/" + utils.get_script_file_name(job_name)
    input_files = temp_dir + "/" + utils.get_input_file_name_prefix() + "*"  # "input-data*"
    cmd = ['disco', 'job', 'create', '-n', job_name, '-s', script_name, '-i',
           input_files, '-c', f"{utils.get_module_file_name()},requirements.txt"]
    cmd += ['--clusterInstanceType', str(machine_size)] if machine_size else []
    cmd += ['--clusterId', str(cluster_id)] if cluster_id else []
    cmd += ['--docker-image-id', docker_image_id] if docker_image_id else []
    cmd += ['--dont-generate-req-file']
    cmd += ['--run', '--wait'] if wait else []
    input = 'Yes' if wait else ''
    output = disco_cli(cmd, True, input)
    return output


def add_job_parse_reply(output):
    lines = list(filter(lambda line: 'Created job with id' in line, output.splitlines()))
    if len(lines) == 0:
        return False
    job_id = lines[0][20:]
    if 'Failed' in output:
        return False
    return job_id


def add_wait_for_job_done_parse_reply(output):
    lines = list(filter(lambda line: 'successfully' in line, output.splitlines()))
    if len(lines) == 0:
        return False
    job_id = lines[0][4:28]
    if 'Failed' in output:
        return False
    return job_id


def start_job_request(job_id):
    output = disco_cli(['disco', 'job', 'start', job_id])
    return output


def start_job_parse_reply(output):
    return output and 'started' in output


def wait_for_finish_and_download(job_id):
    output = ''
    while 'Done' not in output and 'Failed' not in output:
        cmd = ['disco', 'job', 'view', job_id]
        output = disco_cli(cmd, False)
        sleep(5)
    return get_job_status(job_id)


def get_job_status(job_id):
    is_downloaded = False
    cmd = ['disco', 'job', 'view', job_id]
    output = disco_cli(cmd, False)
    # Job is done
    if output and 'Done' in output:
        if 'success: 0' not in output:  # At least one of the tasks has succeeded
            # Download the results
            if not os.path.exists(job_id):
                os.mkdir(job_id)
            cmd = ['disco', 'job', 'download-results', job_id, '-d', job_id]
            disco_cli(cmd, True, 'Yes')  # 'Yes' will overwrite existing directory result (with the same job name)
            is_downloaded = True
        else:  # All tasks failed
            cmd = ['disco', 'job', 'view', job_id]
            disco_cli(cmd)
            is_downloaded = False

    return is_downloaded
