import functools
import logging
import sys
from os import getcwd, path
from pathlib import Path
from pprint import pformat
from subprocess import check_output

import click
import requests
import yaml
from git import Repo

from .model_validator import validate_model
from .util import generate_request_timestamp, sign_payload

_logger = logging.getLogger(__name__)


def confirmation_prompt(question):
    reply = input(question + " (y or n): ")
    if reply[0] == "y":
        return True
    if reply[0] == "n":
        return False
    else:
        return confirmation_prompt("Please enter ")


@functools.lru_cache()
def fetch_remote_git_yaml(remote_url, git_ref, file_path):
    cmd = "git archive --remote={} {} {} | tar -xO".format(remote_url, git_ref, file_path)
    file_str = check_output(cmd, shell=True).decode()
    return yaml.load(file_str)


def fetch_git_yaml(relpath, git_ref):
    if git_ref:
        repo = Repo(".", search_parent_directories=True)
        reldir = path.relpath(getcwd(), repo.working_dir)
        git_path = path.join(reldir, relpath)
        _logger.info("\tUsing {} at ref {}, will fetch latest".format(git_path, git_ref))
        for fetch_info in repo.remotes["origin"].fetch():
            _logger.info("\tUpdated %s to %s" % (fetch_info.ref, fetch_info.commit))
        model_str = repo.git.show("{}:{}".format(git_ref, git_path))
        return yaml.load(model_str)
    else:
        with open(relpath, "r") as f:
            _logger.info("Using {} from current working directory".format(relpath))
            return yaml.load(f)


def confirm_git_branch(work_dir, nomitall):
    if work_dir:
        if nomitall == "nomitall-prod":
            question = "You are about to push your working directory to production!\
            Are you absolutely sure you want to do this?"

            if not confirmation_prompt(question):
                _logger.info("You have chosen wisely")
                sys.exit()
            if not confirmation_prompt("Absolutely sure?"):
                _logger.info("You have chosen wisely")
                sys.exit()
        branch = None
    else:
        if nomitall == "nomitall-prod":
            branch = "origin/master"
        elif nomitall == "nomitall-stage":
            branch = "origin/staging"
    return branch


def fetch_include(fpath, git_ref, model_fp, remote=None):
    if remote:
        return fetch_remote_git_yaml(remote, git_ref, fpath)
    else:
        final_path = Path(path.abspath(model_fp)).parent / Path(fpath)
        return fetch_git_yaml(final_path.resolve(), git_ref)


def include_includes(parameters, git_ref, model_fp, remote=None):
    parsed_params = []
    for parameter in parameters:
        if "parameters" in parameter:
            parameter["parameters"] = include_includes(
                parameter["parameters"], git_ref, model_fp
            )
            parsed_params.append(parameter)
        elif "include" in parameter:
            for include in parameter["include"]:
                _logger.info(
                    "\tIncluding file {} from {}@{}".format(include, remote, git_ref)
                )
                include_doc = fetch_include(include, git_ref, model_fp, remote)
                include_doc = include_includes(include_doc, git_ref, model_fp, remote)
                parsed_params.extend(include_doc)
        elif "include_git" in parameter:
            for include in parameter["include_git"]:
                new_remote, new_ref, fpath = include.split(" ")
                _logger.info(
                    "\tIncluding file {} from {}@{}".format(fpath, new_remote, new_ref)
                )
                include_doc = fetch_include(fpath, new_ref, model_fp, new_remote)
                include_doc = include_includes(include_doc, new_ref, model_fp, new_remote)
                parsed_params.extend(include_doc)
        else:
            parsed_params.append(parameter)
    return parsed_params


@click.command()
@click.option(
    "-wd",
    "--use_work_dir",
    "--using-work-dir",
    "work_dir",
    is_flag=True,
    help="Use model files from current working directory instead of git",
)
@click.option(
    "-ns",
    "--nomitall-secret",
    required=True,
    help="Secret key to authenticate with nomitall",
)
@click.option(
    "-n",
    "--nomitall",
    default="nomitall-stage",
    help="Specify the nomitall to update [nomitall-prod,nomitall-stage,custom_url]",
)
@click.option(
    "-dr",
    "--dry_run",
    "--dry-run",
    is_flag=True,
    help="Do not update nomitall, just output parsed model json",
)
@click.option(
    "-f",
    "--file",
    "model_fn",
    default="model.yaml",
    help="Model YAML file to build + deploy",
)
def model_update(
    work_dir=None, nomitall_secret=None, nomitall=None, dry_run=None, model_fn=None
):
    """Update staging or prod nomitall model definitions. Defaults to using files from git master/staging branch for prod/staging"""
    relpath = model_fn
    branch = confirm_git_branch(work_dir, nomitall)
    doc = fetch_git_yaml(relpath, branch)
    model_type = doc.get("type")
    doc.pop("docker", None)
    if not model_type:
        _logger.error("Model does not have a type, this is required")
        sys.exit(1)
    # add legacy model verison if it doesn't exit
    if model_type == "engine":
        for action, action_dict in doc["actions"].items():
            _logger.info("Parsing {}".format(action))
            action_dict["parameters"] = include_includes(
                action_dict["parameters"], branch, model_fn
            )
        try:
            image, tag = doc["location"]["image"].split(":")
        except ValueError:
            image = doc["location"]["image"]
        if nomitall == "nomitall-prod":
            tag = "prod"
        elif nomitall == "nomitall-stage":
            tag = "stage"
        else:
            tag = "stage"
        doc["location"]["image"] = ":".join([image, tag])
    else:
        doc["parameters"] = include_includes(doc["parameters"], branch, model_fn)

    if dry_run:
        _logger.info("PARSED MODEL :")
        _logger.info(pformat(doc))
        sys.exit()

    if not validate_model(doc):
        sys.exit(1)

    if nomitall == "nomitall-prod":
        nomitall_url = "https://api.nomnomdata.com/api/1"
    elif nomitall == "nomitall-stage":
        nomitall_url = "https://staging.api.nomnomdata.com/api/1"
    else:
        nomitall_url = nomitall

    update_engine(nomitall_url, doc, model_type, nomitall_secret)


def update_engine(nomitall_url, model, model_type, nomitall_secret):
    _logger.info("Pushing model to nomitall @ : {}".format(nomitall_url))
    ts = generate_request_timestamp()
    if model_type == "engine":
        nomitall_uri = "{base}/engine/deploy?ts={ts}".format(base=nomitall_url, ts=ts)
    elif model_type == "shared_object_type":
        nomitall_uri = "{base}/shared_object_type/update?ts={ts}".format(
            base=nomitall_url, ts=ts
        )
    elif model_type == "connection":
        nomitall_uri = "{base}/connection_type/update?ts={ts}".format(
            base=nomitall_url, ts=ts
        )
    sig = sign_payload(nomitall_uri, ts, nomitall_secret, payload=model)
    resp = requests.request(
        "POST",
        nomitall_uri,
        verify=False,
        json=model,
        headers={"X-NomNom-Signature": sig},
    )
    if resp.status_code == 500:
        _logger.error(f"Internal server error{resp.text}")
        return
    reply_data = resp.json()
    if reply_data.get("error"):
        raise Exception(str(reply_data))
    if reply_data.get("status"):
        if reply_data["status"] == "success":
            _logger.info("Model updated successfully")
    if resp.status_code == 401:
        _logger.error("Check secret key is valid")
    resp.raise_for_status()
    return resp
