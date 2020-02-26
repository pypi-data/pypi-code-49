import docker
import boto3
import base64
import subprocess
from datetime import datetime
import time
import sys
import os
import shutil

sken_output_foler = ''

def docker_login(scan_info):
    print('Login to docker')
    session = boto3.Session(
        aws_access_key_id=scan_info['awsAccessKeyId'], 
        aws_secret_access_key=scan_info['awsSecretAccessKey'], 
        region_name=scan_info['awsRegion'])

    ecr_client = session.client('ecr')
    token = ecr_client.get_authorization_token()
    ecr_username, ecr_password = base64.b64decode(token['authorizationData'][0]['authorizationToken']).decode().split(':')
    registry = token['authorizationData'][0]['proxyEndpoint']
    
    command = ['docker', 'login', '-u', ecr_username, '--password-stdin', registry]
    if sys.version_info < (3, 0):
        command = ['docker login -u ' + ecr_username + ' --password-stdin ' + registry]

    p = subprocess.Popen(command, stdout=subprocess.PIPE, stdin=subprocess.PIPE, shell=True)
    p.communicate(input=ecr_password.encode('utf-8'))
    p.wait()
    client = docker.from_env()
    print('Login to docker succeeded.')

    return client

def docker_pull_image(docker_client, image):
    command = ['docker', 'image', 'pull', image]
    if sys.version_info < (3, 0):
        command = ['docker image pull ' + image]
        
    p = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
    for line in iter(p.stdout.readline, b''):
        line = line.rstrip().decode('utf8')
        print(line)
    p.stdout.close()
    p.wait()
    
    #docker_client.images.pull(image)

def get_timestamp():
    now = datetime.now()
    try:
        return round(now.timestamp())
    except Exception as e:
        return int(round(time.mktime(now.timetuple())))

def get_formated_timestamp():
    now = get_timestamp()
    return datetime.strftime(datetime.utcfromtimestamp(now),'%Y%m%d%H%M%S')

def create_skenoutput_folder(dir):
    global sken_output_foler
    sken_output_foler = dir

    if not os.path.exists(dir):
        os.makedirs(dir)
        os.chmod(dir, 0o777)

def delete_skenoutput_folder():
    shutil.rmtree(sken_output_foler)

def save_stdout(scanner, content):
    with open(sken_output_foler + os.path.sep + scanner + '-stdout.txt', 'w') as f:
        f.write(content)

def save_stderr(scanner, content):
    with open(sken_output_foler + os.path.sep + scanner + '-stderr.txt', 'w') as f:
        f.write(content)