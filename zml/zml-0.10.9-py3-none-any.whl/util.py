import os
import time
from pprint import pprint
from zml.exceptions import FileNotLoadedException, DocumentNotDefinedException
import subprocess
import shlex
import socket


def load_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
            return content
    except Exception:
        raise FileNotLoadedException


def find_file_in_dirs(filename, directories):
    for d in directories:
        abs_path = os.path.join(d, filename)
        if os.path.exists(abs_path):
            return abs_path
    raise DocumentNotDefinedException


def minimise(code):
    # return code.replace('\n', '')
    return code.strip()


def deb(obj):
    pprint(obj.asDict())


def set_base_path(base_path):
    os.chdir(base_path)


def start_ipfs_daemon(user_data_dir=None):
    if not user_data_dir:
        raise Exception('No user data dir defined.')
    daemon_is_running = False
    while True:
        # rc, std_out, std_err = run_command('ipfs daemon --enable-namesys-pubsub --enable-pubsub-experiment')
        rc, std_out, std_err = run_command('ipfs daemon')
        token_out = 'Daemon is ready'
        token_err = 'ipfs daemon is running'
        token_not_inited = 'no IPFS repo found'
        if std_out and any(token in token_out for token in std_out.decode('utf-8')):
            daemon_is_running = True
        if std_err and any(token in token_err for token in std_err.decode()):
            daemon_is_running = True
        if std_err and any(token in token_not_inited for token in std_err.decode()):
            os.chdir(user_data_dir)
            rc, std_out, std_err = run_command('ipfs init')
        if daemon_is_running:
            # check if daemon is listening on port 5001
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex(('127.0.0.1', 5001))
            if result == 0:
                break
        time.sleep(1)


def run_command(command):
    process = subprocess.Popen(shlex.split(command), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    try:
        std_out, std_err = process.communicate(timeout=1)
    except subprocess.TimeoutExpired:
        std_out, std_err = None, None
    return process.returncode, std_out, std_err
