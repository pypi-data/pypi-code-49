import os
import docker
from .docker_util import docker_login, docker_pull_image, get_timestamp, save_stdout, save_stderr

def run_sast_scanner(params):
    client = docker_login(params['scan_info'])
    scanner = params['scanner']
    build_dir = params['build_dir']
    print('Launching scanner %s ' % scanner)

    output_file = build_dir + 'sken-'+scanner+'-output.json'

    docker_image = ''
    if scanner == 'brakeman':
        docker_image = '621002179714.dkr.ecr.us-east-1.amazonaws.com/brakeman:latest'
    elif scanner == 'nodejsscan': 
        docker_image = '621002179714.dkr.ecr.us-east-1.amazonaws.com/nodejsscan:latest'
    elif scanner == 'eslintsec': 
        docker_image = '621002179714.dkr.ecr.us-east-1.amazonaws.com/eslintsec:latest'
    elif scanner == 'tslintsec': 
        docker_image = '621002179714.dkr.ecr.us-east-1.amazonaws.com/tslintsec:latest'
    elif scanner == 'banditpy2':
        docker_image = '621002179714.dkr.ecr.us-east-1.amazonaws.com/bandit-python2:latest'
    elif scanner == 'banditpy3':
        docker_image = '621002179714.dkr.ecr.us-east-1.amazonaws.com/bandit-python3:latest'
        output_file = build_dir + 'sken-bandit3-output.json'
    elif scanner == 'findsecbugs':
        docker_image = '621002179714.dkr.ecr.us-east-1.amazonaws.com/findsecbugs:latest'
        output_file = build_dir + 'sken-secbugs-output.xml'
    elif scanner == 'gosec':
        docker_image = '621002179714.dkr.ecr.us-east-1.amazonaws.com/gosec:latest'
    elif scanner == 'phpcs':
        docker_image = '621002179714.dkr.ecr.us-east-1.amazonaws.com/phpcs:latest'
    elif scanner == 'gitleaks':
        docker_image = '621002179714.dkr.ecr.us-east-1.amazonaws.com/gitleaks:latest'

    print('Pulling latest image for %s ' % scanner)
    docker_pull_image(client, docker_image)
    print('Scanning started')
    scan_start = get_timestamp()
    container = client.containers.run(docker_image, volumes={build_dir: {
                                          'bind': '/scan', 'mode': 'rw'}}, detach=True, tty=False, stdout=True, stderr=True)
    container.wait()

    # write stdout and stderr output
    save_stdout(scanner, container.logs(stdout=True, stderr=False).decode('UTF-8'))
    save_stderr(scanner, container.logs(stdout=False, stderr=True).decode('UTF-8'))

    scan_end = get_timestamp()
    if os.path.exists(output_file):
        print('Scanning completed. Output file: ' + output_file)
    else:
        print('Scanning completed')
    
    return output_file, scan_start, scan_end
