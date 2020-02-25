import sys
import boto3
import json
from botocore.client import ClientError


def init_client(service, region):
    return boto3.client(service, region_name = region)


def update_stack(cfn_client, stackName=None, templateURL=None, parameters=None):
    stack_response = cfn_client.update_stack(
        StackName = stackName,
        TemplateURL = templateURL,
        Parameters = parameters,
        Capabilities = [
            'CAPABILITY_NAMED_IAM',
        ]
    )


def create_stack(cfn_client, stackName=None, templateURL=None, parameters=None, cfn_timeout=15):
    stack_response = cfn_client.create_stack(
    StackName = stackName,
    TemplateURL = templateURL,
    Parameters = parameters,
    TimeoutInMinutes=cfn_timeout,
    Capabilities=[
        'CAPABILITY_NAMED_IAM'
    ],

    OnFailure='ROLLBACK',
    EnableTerminationProtection = True
    )


def write_output(cfn_client, stackName=None, outputPath=None):
    cloudformation_outputs = cfn_client.describe_stacks(StackName = stackName)['Stacks'][0]['Outputs']
    output_length = len(cloudformation_outputs)
    i=0
    json_output = {}
    while i<output_length:
        json_output[cloudformation_outputs[i]['OutputKey']]  = cloudformation_outputs[i]['OutputValue']
        i = i + 1
    with open(outputPath, 'w+') as outputsfile:
        json.dump(json_output, outputsfile, indent = 4)


def create_update_stack(cfn_client, cfn_timeout=15, stackName=None, templateURL=None, parameters=None, outputPath=None):
    try:
        cfn_client.describe_stacks(StackName = stackName)
        try:
            print("Updating stack: " + stackName)
            update_stack(cfn_client, stackName=stackName, templateURL=templateURL, parameters=parameters)
            stack_waiter = cfn_client.get_waiter('stack_update_complete')
            stack_waiter.wait(StackName = stackName)
            if outputPath:
                print("Config ouput written to: {}".format(outputPath))
                write_output(cfn_client, stackName=stackName, outputPath=outputPath)
            print("Successfully updated stack: " + stackName)
            return 0
        except ClientError as e:
            error_code = int(e.response['ResponseMetadata']['HTTPStatusCode'])
            if error_code == 400:
                print("Nothing to be updated on stack: " + stackName)
                return 0
            print("Error Occured.")
            sys.exit(error_code)
    except ClientError as e:
        error_code = int(e.response['ResponseMetadata']['HTTPStatusCode'])
        if error_code == 403:
            sys.exit("Private Cloudformation stack. Access denied!")
        elif error_code == 400:
            print("Stack does not exist! Creating stack: " + stackName)
            create_stack(cfn_client=cfn_client, stackName=stackName, templateURL=templateURL, parameters=parameters, cfn_timeout=cfn_timeout)
            stack_waiter = cfn_client.get_waiter('stack_create_complete')
            stack_waiter.wait(StackName = stackName)
            if outputPath:
                print("Config ouput written to: {}".format(outputPath))
                write_output(cfn_client, stackName=stackName, outputPath=outputPath)
            print("Created new stack: " + stackName)
            return 0
