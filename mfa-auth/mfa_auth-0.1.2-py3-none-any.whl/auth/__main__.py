import os
from configparser import ConfigParser

import boto3
from botocore.exceptions import ClientError as BotoClientError


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def mfa_auth():
    """

    :return:
    """
    auth_profile = input(f"{bcolors.OKBLUE}Aws Profile(default: default): {bcolors.ENDC}")
    if not auth_profile:
        auth_profile = "default"
    username = input(f"{bcolors.OKBLUE}Enter Aws Username(xxx@yyy.com): {bcolors.ENDC}")
    while True:
        new_profile_name = input(f"{bcolors.OKBLUE}Enter MFA Profile Name(if need): {bcolors.ENDC}")
        if not new_profile_name:
            new_profile_name = 'default'
        if auth_profile == new_profile_name:
            new_profile_name = 'mfa-default'
        if auth_profile and new_profile_name and auth_profile != new_profile_name:
            print(f"{bcolors.WARNING}MFA Profile Name is {new_profile_name}{bcolors.ENDC}")
            break

    # The calls to AWS STS GetSessionToken must be signed with the access key ID and secret
    # access key of an IAM user. The credentials can be in environment variables or in
    # a configuration file and will be discovered automatically
    # by the STSConnection() function. For more information, see the Python SDK
    # documentation: http://boto.readthedocs.org/en/latest/boto_config_tut.html
    session = boto3.session.Session(profile_name=auth_profile)
    sts_client = session.client('sts')
    account_id = sts_client.get_caller_identity().get('Account')

    yes_or_no = input(f'{bcolors.OKBLUE}Is AWS account_id ({account_id}) right?(yes/no): {bcolors.ENDC}')
    try:
        if yes_or_no == 'yes':
            yes_or_no = True
        elif yes_or_no == 'no':
            return False
        else:
            raise ValueError("Invalid Input Data")
    except ValueError as e:
        print(f"{bcolors.FAIL}{e}{bcolors.ENDC}")
        return False

    temp_credentials = {}
    while True:
        # Prompt for MFA time-based one-time password (TOTP)
        mfa_TOTP = input(f"{bcolors.OKBLUE}Enter the MFA code: {bcolors.ENDC}")
        try:
            temp_credentials = sts_client.get_session_token(
                DurationSeconds=129600,
                SerialNumber=f"arn:aws:iam::{account_id}:mfa/{username}",
                TokenCode=mfa_TOTP
            )['Credentials']
        except BotoClientError as e:
            print(f"{bcolors.FAIL}{e.response['Error']['Message']}{bcolors.ENDC}")
            continue
        break

    home_path = os.path.expanduser("~")
    credentials = ConfigParser()
    credentials.read(f'{home_path}/.aws/credentials')

    profile_name = new_profile_name
    credentials[profile_name] = {
        'aws_access_key_id': temp_credentials['AccessKeyId'],
        'aws_secret_access_key': temp_credentials['SecretAccessKey'],
        'aws_session_token': temp_credentials['SessionToken'],
    }

    with open(f'{home_path}/.aws/credentials', 'w') as credential_file:
        credentials.write(credential_file)

    print(f"{bcolors.OKGREEN}Success!!(profile_name: {new_profile_name}){bcolors.ENDC}")
    return temp_credentials


if __name__ == '__main__':
    result = mfa_auth()

