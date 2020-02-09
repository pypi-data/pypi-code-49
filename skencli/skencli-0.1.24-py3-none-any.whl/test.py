import os
import docker
import boto3
import base64
import subprocess


def main():
	#client = docker.from_env()
	
	username = 'AKIAZBFU5ISBJOKQ6TO5'
	password = 'i2F8bRh2PbN7GGSShlOSdQr4oK/k/AJ0brUTySQy'
	ecr_client = boto3.client(
		'ecr', 
		region_name='us-east-1',
		aws_access_key_id=username,
		aws_secret_access_key=password
		)

	token = ecr_client.get_authorization_token()
	ecr_username, ecr_password = base64.b64decode(token['authorizationData'][0]['authorizationToken']).decode().split(':')
	registry = token['authorizationData'][0]['proxyEndpoint']
	print(ecr_username)
	print(ecr_password)
	print(token)
	#login_result = client.login(username=ecr_username, password=ecr_password, registry=registry, reauth=True)
	command = ['docker', 'login', '-u', ecr_username, '-p', ecr_password, registry]
	p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
	#for line in p.stdout:
	#	print(line)
	p.wait()
	print('pulling')
	client = docker.from_env()
	print(client)
	client.images.pull('621002179714.dkr.ecr.us-east-1.amazonaws.com/nodejsscan:latest')
	exit(0)

	ecr_client = boto3.client('ecr', region_name='us-east-1')
	token = ecr_client.get_authorization_token()
	username, password = base64.b64decode(token['authorizationData'][0]['authorizationToken']).decode().split(':')
	registry = token['authorizationData'][0]['proxyEndpoint']
	
	username = 'AKIAZBFU5ISBJOKQ6TO5'
	password = 'i2F8bRh2PbN7GGSShlOSdQr4oK/k/AJ0brUTySQy'
	registry = 'https://621002179714.dkr.ecr.us-east-1.amazonaws.com'
	ecr_client = boto3.client(
		'ecr', 
		region_name='us-east-1',
		aws_access_key_id=username,
		aws_secret_access_key=password
		)

	token = ecr_client.get_authorization_token()
	ecr_username, ecr_password = base64.b64decode(token['authorizationData'][0]['authorizationToken']).decode().split(':')
	print(ecr_username)
	print(ecr_password)
	#login_result = client.login(ecr_username, ecr_password, registry=registry, reauth=True)
	#command = 'docker login -u %s -p %s %s' % (ecr_username, ecr_password, registry)
	command = ['docker', 'login', '-u', ecr_username, '-p', ecr_password, registry]
	p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
	#for line in p.stdout:
	#	print(line)
	p.wait()

	print('pulling')
	client.images.pull('621002179714.dkr.ecr.us-east-1.amazonaws.com/nodejsscan', tag='latest')
	exit(0)

	build_dir = 'E:/myprojects88/sken.ai/temp'
	container = client.containers.run('621002179714.dkr.ecr.us-east-1.amazonaws.com/nodejsscan:latest', volumes={
                                          build_dir: {'bind': '/scan', 'mode': 'rw'}}, detach=True, tty=False, stdout=False)
        
	container.wait()
	username = 'AKIAZBFU5ISBJOKQ6TO5'
	password = 'i2F8bRh2PbN7GGSShlOSdQr4oK/k/AJ0brUTySQy'
	registry = 'https://621002179714.dkr.ecr.us-east-1.amazonaws.com'
	session = boto3.Session(aws_access_key_id=username, aws_secret_access_key=password, region_name='us-east-1')
	ecr_client = session.client('ecr')
	token = ecr_client.get_authorization_token()

	ecr_username, ecr_password = base64.b64decode(token['authorizationData'][0]['authorizationToken']).decode().split(':')
	print(ecr_username)
	print(ecr_password)
	
	#login_result = client.login(username=ecr_username, password=ecr_password, registry=registry, reauth=True)
	#print(login_result)
	
	"""
	#command = 'docker login -u %s -p %s %s' % (ecr_username, ecr_password, registry)
	command = ['docker', 'login', '-u', ecr_username + '2', '-p', ecr_password, registry]
	p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
	#for line in iter(p.stdout.readline, b''):
	#	print(line)
	for line in p.stdout:
		print(line)
	p.wait()
	"""
	print('pulling image')
	client.images.pull('621002179714.dkr.ecr.us-east-1.amazonaws.com/nodejsscan', tag='latest')

if __name__ == "__main__":
    main()
