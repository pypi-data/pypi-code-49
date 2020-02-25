#!/usr/bin/env python3

# This script is a wrapper that provides SCP functionality via SSH connections
# through Session Manager (for SSM enabled instances).
#
# The script also automatically resolves IP addresses, private instance DNS names, and "name" tag
# values to the corresponding instance ID, if provided in place of instance ID in the command arguments
#
# Author: Chris Heath
# Email: SRE@vonage.com

import argparse
import botocore.exceptions
import boto3
import logging
import os
import re


streamHandler = logging.StreamHandler()
formatter = logging.Formatter(
    "[%(name)s] %(levelname)s: %(message)s"
)
streamHandler.setFormatter(formatter)
logger = logging.getLogger("ssm-ssh")
logger.addHandler(streamHandler)
logger.setLevel(logging.WARNING)
args = None


# Method uses ArgumentParser to retrieve command-line arguments and display help interface
def get_sys_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--region", metavar="REGION", help="Set / override AWS region")
    parser.add_argument("--profile", metavar="PROFILE", help="Configuration profile from ~/.aws/{credentials,config}")
    parser.add_argument("--params",  metavar="PARAMS", help='''String containing all extra SSH parameters. \n
                                    Example: ssm-ssh --params "-i user.pem -o StrictHostKeyChecking=no" user@host''')
    parser.add_argument('TARGET',
                        help='[user@]hostname -- hostname can be an instance-id, the \'name\' tag on a instance, a private instance DNS name, or IP')
    
    return parser.parse_args()


def format_filters(target):
    if re.match('^(10|127|169\.254|172\.1[6-9]|172\.2[0-9]|172\.3[0-1]|192\.168)\.', target):
        return [{'Name': 'private-ip-address', 'Values': [target]}]
    elif re.match('[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}', target):
        return [{'Name': 'ip-address', 'Values': [target]}]
    elif re.match('ip-[0-9]{1,3}-[0-9]{1,3}-[0-9]{1,3}-[0-9]{1,3}.ec2.internal', target):
        return [{'Name': 'private-dns-name', 'Values': [target]}]
    else:
        return [{'Name': 'tag:Name', 'Values': [target]}]
     

def get_instance(target):
    # Is it a valid Instance ID?
    if re.match('^i-[a-f0-9]+$', target):
        return target
    else:
        # Create boto3 client from session
        session = boto3.Session(profile_name=args.profile, region_name=args.region)
        ec2_client = session.client('ec2')
        
        instance_ids = []
        filters = format_filters(target)
        logger.debug(f"EC2 describe-instance filters: {filters}")
        paginator = ec2_client.get_paginator('describe_instances')
        response_iterator = paginator.paginate(Filters=filters)
        for reservations in response_iterator:
            for reservation in reservations['Reservations']:
                for instance in reservation['Instances']:
                    instance_id = instance['InstanceId']
                    if instance_id not in instance_ids:
                        instance_ids.append(instance_id)
                        
        if not instance_ids:
            return None

        if len(instance_ids) > 1:
            logger.warning("Found %d instances for '%s': %s", len(instance_ids), target, " ".join(instance_ids))
            logger.warning("Use INSTANCE_ID to connect to a specific one")
            quit(1)

        # Found only one instance - return it
        return instance_ids[0]
    

def start_session(instance):
    remote_command = f"\"{args.command}\" " if args.command else ""
    ssh_params      = f"{args.params} " if args.params else ""
    extra_args      = f"--profile {args.profile} " if args.profile else ""
    extra_args     += f"--region {args.region} " if args.region else ""
    conf            = os.path.join(os.path.expanduser('~'),'.ssm_ssh_conf')
    
    
    # Create an SSH config file that will enable SSH eonnections through Session Manager
    try:
        with open(conf, "w") as f:
            f.write(f'# SSH over Session Manager\n')
            f.write(f'host i-* mi-*\n')
            f.write(f'\tProxyCommand sh -c "aws {extra_args} ssm start-session --target %h --document-name AWS-StartSSHSession --parameters \'portNumber=%p\'"')
    except IOError:
        logger.error(f"File {cache_file} not accessible")


    command = f'ssh -F {conf} {ssh_params}{instance} {remote_command}'
    logger.debug("Running: %s", command)
    os.system(command)
        
        
def main():
    global args
    args = get_sys_args()

    try:
        user_host = args.TARGET.split('@')
        target = args.TARGET if len(user_host) < 2 else user_host[1]
        instance = get_instance(target)

        remote = instance if len(user_host) < 2 else f"{user_host[0]}@{instance}"
        start_session(remote)
        quit(0)

    except (botocore.exceptions.BotoCoreError,
            botocore.exceptions.ClientError) as e:
        logger.error(e)
        quit(1)

if __name__ == "__main__":
    main()