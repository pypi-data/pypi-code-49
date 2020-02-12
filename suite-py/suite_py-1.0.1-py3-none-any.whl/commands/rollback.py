# -*- encoding: utf-8 -*-
from distutils.version import StrictVersion
import re
import sys

from halo import Halo

from suite_py.lib.handler.github_handler import GithubHandler
from suite_py.lib.handler.slack_handler import SlackHandler
from suite_py.lib.handler import prompt_utils
from suite_py.lib.handler import aws_handler as aws
from suite_py.lib.handler import drone_handler as drone
from suite_py.lib.logger import Logger


github = GithubHandler()
logger = Logger()
slack = SlackHandler()


def entrypoint(project):
    bucket_name = "prima-artifacts-encrypted"
    repo = github.get_repo(project)

    if project == "prima":
        stacks_name = ["ecs-task-web-vpc-production", "ecs-task-consumer-vpc-production",
                       "ecs-task-cron-vpc-production", "batch-job-php-production"]
        prefix = "prima/"

        artifacts = aws.get_artifacts_from_s3(
            bucket_name, prefix)
        versions, prima_version_mapping = get_versions_from_artifacts(
            project, bucket_name, artifacts)

        version = ask_version(repo, versions)
        rollback_stacks(args.project, stacks_name,
                        prima_version_mapping[version])

    elif aws.is_cloudfront_distribution(project):
        with Halo(text='Loading releases...', spinner='dots', color='magenta'):
            versions = drone.get_tag_from_builds(project)
        version = ask_version(repo, versions)
        build = drone.get_build_from_tag(project, version)
        drone.launch_build(project, build)
        logger.info("Build rilanciata, controlla lo stato su drone")
        post_rollback_complete_on_slack(args.project, version)

    else:
        stacks_name = aws.get_stacks_name(project)
        prefix = "microservices/{}/".format(project)

        if len(stacks_name) > 0:
            artifacts = aws.get_artifacts_from_s3(
                bucket_name, prefix)
            versions, _ = get_versions_from_artifacts(
                project, bucket_name, artifacts)

            if len(versions) > 0:
                version = ask_version(repo, versions)
                rollback_stacks(args.project, stacks_name, version)
            else:
                logger.error(
                    "Nessuna release trovata. Impossibile procedere con il rollback.")
                sys.exit(-1)

        else:
            logger.error(
                "Nessuno stack trovato. Impossibile procedere con il rollback.")


def ask_version(repo, choiches):
    version = prompt_utils.ask_choices("Seleziona release: ", choiches)
    release = github.get_release_if_exists(repo, version)
    logger.info(
        "\nDescrizione della release selezionata:\n{}\n".format(release.body))
    if not prompt_utils.ask_confirm("Vuoi continuare con il rollback?"):
        sys.exit(-1)
    return version


def get_versions_from_artifacts(project, bucket_name, artifacts):
    with Halo(text='Loading releases...', spinner='dots', color='magenta'):

        versions = []
        prima_version_mapping = {}

        for artifact in artifacts:

            if project == "prima":

                tags_object = aws.get_tag_from_s3_artifact(
                    bucket_name, "prima/", artifact)

                for tag_object in tags_object:
                    if tag_object["Key"] == "ReleaseVersion":
                        versions.append(tag_object["Value"])
                        prima_version_mapping[tag_object["Value"]] = artifact.replace(
                            ".tar.gz", "")

            else:
                if re.match("[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}-production.tar.gz", artifact):
                    versions.append(artifact.replace("-production.tar.gz", ""))

        versions.sort(key=StrictVersion, reverse=True)
    return versions, prima_version_mapping


def rollback_stacks(project, stacks_name, version):
    aws.update_stacks(stacks_name, version)
    post_rollback_complete_on_slack(project, version)
    logger.info(
        "Rollback completato con successo. Versione in produzione: {}".format(version))


def post_rollback_complete_on_slack(project, version):
    try:
        slack.post("#deploy", "ho effettuato il rollback di {}. Versione in produzione: {}".format(
            project, version))
    except:
        logger.warning("Non sono riuscito a inviare il messaggo su Slack")
