import os
import docker
from .docker_util import docker_login, docker_pull_image, get_timestamp, save_stdout, save_stderr

def run_sca_scanner(params):
    client = docker_login(params['scan_info'])
    scanner = params['scanner']
    build_dir = params['build_dir']

    print('Launching scanner %s ' % params['scanner'])

    output_file = build_dir + 'dependency-check-report.json'

    docker_image = '621002179714.dkr.ecr.us-east-1.amazonaws.com/dependency-check:latest'
    print('Pulling latest image for %s ' % scanner)
    docker_pull_image(client, docker_image)
    print('Scanning started')
    scan_start = get_timestamp()
    container = client.containers.run(
        docker_image, 
        volumes={
            build_dir: {'bind': '/scan', 'mode': 'rw'}
        }, 
        detach=True, tty=False, stdout=True, stderr=True)
    container.wait()

    # write stdout and stderr output
    save_stdout(scanner, container.logs(stdout=True, stderr=False).decode('UTF-8'))
    save_stderr(scanner, container.logs(stdout=False, stderr=True).decode('UTF-8'))

    scan_end = get_timestamp()
    print('Scanning completed. Output file: ' + output_file)
    
    return output_file, scan_start, scan_end
