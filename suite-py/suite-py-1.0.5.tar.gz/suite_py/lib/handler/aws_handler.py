# -*- encoding: utf-8 -*-
import sys
import time

import boto3
from halo import Halo

from suite_py.lib.logger import Logger

logger = Logger()

cloudformation = boto3.client("cloudformation", region_name="eu-west-1")
cloudfront = boto3.client("cloudfront", region_name="eu-west-1")


def update_stack(stack_name, version):
    params = update_template_params(stack_name, version)
    if params:
        logger.info(f"Effettuo update template cloudformation {stack_name}")
        cloudformation.update_stack(
            StackName=stack_name,
            TemplateBody=get_template_from_stack_name(stack_name),
            Parameters=params,
        )
    else:
        logger.error(f"Nessun parametro trovato sullo stack {stack_name}")
        sys.exit(-1)


def update_template_params(stack_name, version):
    new_parameter = []
    ReleaseVersionFound = False
    current_parameters = get_parameters_from_stack_name(stack_name)

    for param in current_parameters:
        if param["ParameterKey"] == "ReleaseVersion":
            new_parameter.append(
                {"ParameterKey": param["ParameterKey"], "ParameterValue": version}
            )
            ReleaseVersionFound = True
        else:
            new_parameter.append(
                {"ParameterKey": param["ParameterKey"], "UsePreviousValue": True}
            )

    if ReleaseVersionFound:
        return new_parameter
    return None


def get_parameters_from_stack_name(stack_name):
    return cloudformation.describe_stacks(StackName=stack_name)["Stacks"][0][
        "Parameters"
    ]


def get_template_from_stack_name(stack_name):
    return cloudformation.get_template(StackName=stack_name)["TemplateBody"]


def get_stacks_name(repo):
    stacks_name = []
    base_stacks_name = [
        f"ecs-task-{repo}-production",
        f"ecs-task-{repo}-vpc-production",
        f"ecs-job-{repo}-production",
        f"batch-job-{repo}-production",
    ]

    for stack_name in base_stacks_name:
        if stack_exists(stack_name):
            stacks_name.append(stack_name)

    return stacks_name


def stack_exists(stack_name):
    try:
        cloudformation.describe_stacks(StackName=stack_name)
        return True
    except Exception:
        return False


def get_stack_status(stack_name):
    return cloudformation.describe_stacks(StackName=stack_name)["Stacks"][0][
        "StackStatus"
    ]


def get_artifacts_from_s3(bucket_name, prefix):
    # pylint has issues with boto3...
    # pylint: disable=no-member
    with Halo(text="Loading releases...", spinner="dots", color="magenta"):
        s3 = boto3.resource("s3")
        bucket_artifacts = s3.Bucket(bucket_name)
        artifacts = []

        for bucket_object in bucket_artifacts.objects.filter(Prefix=prefix):
            artifacts.append(bucket_object.key.replace(prefix, ""))

    return artifacts


def is_cloudfront_distribution(repo):
    with Halo(text="Loading releases...", spinner="dots", color="magenta"):
        distributions = cloudfront.list_distributions()["DistributionList"]["Items"]
        for distribution in distributions:
            if (
                f"prima-prod-{repo}.s3.amazonaws.com"
                == distribution["Origins"]["Items"][0]["DomainName"]
            ):
                return True
    return False


def get_tag_from_s3_artifact(bucket_name, prefix, artifact):
    s3 = boto3.client("s3")

    return s3.get_object_tagging(Bucket=bucket_name, Key=f"{prefix}{artifact}")[
        "TagSet"
    ]


def stack_update_completed(stack_name):
    with Halo(text="Rollback in progress...", spinner="dots", color="magenta"):
        for _ in range(0, 60):
            stack_status = get_stack_status(stack_name)
            if stack_status == "UPDATE_COMPLETE":
                return True
            if "FAILED" in stack_status:
                break
            time.sleep(10)
    return False


def update_stacks(stacks_name, version):
    for stack_name in stacks_name:
        update_stack(stack_name, version)

    for stack_name in stacks_name:
        if not stack_update_completed(stack_name):
            logger.error(
                f"Errore durante l'update dello stack CloudFormation {stack_name}. Contattare i DevOps"
            )
            sys.exit(-1)
