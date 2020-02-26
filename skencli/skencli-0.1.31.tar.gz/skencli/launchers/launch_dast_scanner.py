import os
import docker 
import time
from .docker_util import docker_login, docker_pull_image, get_timestamp, save_stdout, save_stderr

def run_dast_scanner(params):
    client = docker_login(params['scan_info'])
    url = params['url']
    scanner = params['scanner']
    build_dir = params['build_dir']

    print('Launching scanner %s ' % params['scanner'])

    # context file
    if 'dastContext' in params['scan_info'] and params['scan_info']['dastContext'] is not None:
        with open(build_dir + 'sken.dast.context', 'w') as f:
            f.write(params['scan_info']['dastContext'])

    docker_image = 'owasp/zap2docker-stable:latest'
    print('Pulling latest image for %s ' % scanner)
    docker_pull_image(client, docker_image)
    scan_start = get_timestamp()
    
    py_file = ''
    if params['full_scan']:
        print('full scan started for ' + url) 
        py_file = 'zap-full-scan.py'
    else:
        print('baseline scan started for ' + url)
        py_file = 'zap-baseline.py'

    # check context file
    if os.path.exists(build_dir + 'sken.dast.context'):
        cs = py_file + ' -j -n /zap/wrk/sken.dast.context -t ' + url +' -J sken-dast-output.json'
    else:
        cs = py_file + ' -j -t ' + url +' -J sken-dast-output.json'

    container = client.containers.run(docker_image, cs, volumes={build_dir:{'bind':'/zap/wrk','mode':'rw'}}, detach=True, tty=False, stdout=True, stderr=True) 
    container.wait()
    print(container.logs().decode('UTF-8'))

    # write stdout and stderr output
    save_stdout(scanner, container.logs(stdout=True, stderr=False).decode('UTF-8'))
    save_stderr(scanner, container.logs(stdout=False, stderr=True).decode('UTF-8'))

    scan_end = get_timestamp()
    output_file = build_dir + 'sken-dast-output.json'
    
    if os.path.exists(build_dir + 'sken.dast.context'):
        os.remove(build_dir + 'sken.dast.context')

    return output_file, scan_start, scan_end

