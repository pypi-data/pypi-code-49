import logging
import sys
from base64 import b64decode

import boto3
import click
import docker
import requests
from compose.progress_stream import stream_output

_logger = logging.getLogger(__name__)

engine_config = {
    "repo_arn": "arn:aws:ecr:us-east-1:445607516549:repository",
    "repo_uri": "445607516549.dkr.ecr.us-east-1.amazonaws.com",
}


def repo_login(repo, profile):
    # Login to the necessary docker repository so we can pull images if we have access.
    # Once the host is logged in it should stay logged in for about 24 hours
    region = repo["repo_uri"].split(".")[3]
    registryId = repo["repo_uri"].split(".")[0]
    if profile:
        session = boto3.Session(profile_name=profile)
        ecr = session.client("ecr", region_name=region)
    else:
        ecr = boto3.client("ecr", region_name=region)
    result = ecr.get_authorization_token(registryIds=[registryId])["authorizationData"][0]

    auth_token = b64decode(result["authorizationToken"]).decode()
    username, password = auth_token.split(":")

    return {
        "username": username,
        "password": password,
        "registry": result["proxyEndpoint"],
    }


def image_tag(str):
    image, tag = str.split(":")
    return image, tag


@click.command()
@click.option(
    "-t",
    "--tag",
    required=True,
    help="Override destination tag, defaults to being the same as the tag of the image being pushed",
)
@click.option("-p", "--profile", help="AWS Profile to use")
@click.option(
    "-i",
    "--image",
    "image_tag",
    type=image_tag,
    help="Full image name/tag of local image to deploy.  Example nomnom/test/waittask:stage",
)
def deploy(tag=None, profile=None, image_tag=None):
    "Deploy engine images to the aws repo"
    tag = tag or image_tag[1]
    client = docker.from_env()
    try:
        client.ping()
    except (requests.ConnectionError, docker.errors.APIError) as e:
        raise Exception(
            "There was a problem connecting to the docker agent, ensure it is running and in a good state"
        ) from e
    repo_credentials = repo_login(engine_config, profile)
    _logger.info("Logging in to Amazon ECS")
    client.login(
        username=repo_credentials["username"],
        password=repo_credentials["password"],
        registry=repo_credentials["registry"],
        reauth=True,
    )
    image_name, image_tag = image_tag
    target_image_name = "/".join([engine_config["repo_uri"], image_name])
    _logger.info("Fetching image {}:{}".format(image_name, image_tag))
    image = client.images.get(image_name + ":" + image_tag)
    _logger.info("Tagging image into repository {}".format(target_image_name))
    image.tag(repository=target_image_name, tag=tag)
    _logger.info("Pushing to repo with tag {}".format(tag))
    result = client.images.push(target_image_name, tag=tag, stream=True)
    list(stream_output(result, sys.stdout))
