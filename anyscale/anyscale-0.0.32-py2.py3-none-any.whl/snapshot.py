import json
import logging
import requests
import os
import shutil
import subprocess
import time
import sys
import tempfile

import click
from subprocess import STDOUT
import ray.ray_constants
import yaml

from anyscale.project import get_project_id
from anyscale.util import (confirm, send_json_request)
from anyscale.conf import SNAPSHOT_REPO, SNAPSHOT_REPO_PASSWORD


logging.basicConfig(format=ray.ray_constants.LOGGER_FORMAT)
logger = logging.getLogger(__file__)

# A temporary directory to download snapshots to.
TEMP_SNAPSHOT_DIRECTORY = '/tmp/anyscale-snapshot-{}'


class SnapshotRunner:
    def __init__(self):
        self.snapshot_home = os.path.expanduser("~/.anyscale/snapshot")
        self.password = SNAPSHOT_REPO_PASSWORD
        self.snapshot_repo = SNAPSHOT_REPO

        # Get the right restic executable path depending on the OS.
        current_dir = os.path.dirname(os.path.realpath(__file__))
        if sys.platform.startswith("linux"):
            self.snapshot_executable = os.path.join(
                current_dir, "restic-linux")
        elif sys.platform.startswith("darwin"):
            self.snapshot_executable = os.path.join(
                current_dir, "restic-darwin")
        else:
            raise NotImplementedError(
                "Restic snapshot not supported on platform {}".format(
                    sys.platform))

    def setup(self):
        proc = subprocess.Popen([
            self.snapshot_executable, "init", "-r", self.snapshot_repo],
            env={'RESTIC_PASSWORD': self.password})

        proc.communicate()

    def upload(self, snapshot_uuid, project_dir, creds):
        new_env = os.environ.copy()
        new_env = {**new_env, **creds}
        new_env["RESTIC_PASSWORD"] = self.password
        print("Uploading snapshot: " + snapshot_uuid)
        proc = subprocess.Popen([
            self.snapshot_executable, "-r",
            self.snapshot_repo, "backup",
            "--tag", snapshot_uuid,
            "--tag", "project_dir="+project_dir,
            project_dir], env=new_env, stderr=STDOUT)
        proc.communicate()

    def download(self, name, target_directory, creds):
        new_env = os.environ.copy()
        new_env = {**new_env, **creds}
        new_env["RESTIC_PASSWORD"] = self.password

        restic_id, project_dir = self.get_restic_info(name, new_env)

        with tempfile.TemporaryDirectory() as snapshot_dir:
            proc = subprocess.Popen([
                self.snapshot_executable, "-r",
                self.snapshot_repo, "restore", "--tag",
                name, "latest", "--target", snapshot_dir],
                env=new_env, stderr=STDOUT)

            proc.communicate()

            # Convert absolute path used by restic to relative path
            # Strip the leading "/"
            relative_directory = project_dir[1:]
            shutil.move(
                os.path.join(snapshot_dir, relative_directory),
                target_directory)

    def delete(self, name, creds):
        new_env = os.environ.copy()
        new_env = {**new_env, **creds}
        new_env["RESTIC_PASSWORD"] = self.password

        # Getting restic snapshot ID from snapshot_uuid
        # Need this because we cannot delete snapshot with --tag
        restic_id, _ = self.get_restic_info(name, new_env)

        # Need this because if a deletion fails, restic repo will be locked.
        proc = subprocess.Popen([
            self.snapshot_executable, "-r", self.snapshot_repo,
            "unlock"],
            env=new_env, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        # Actual deletion
        proc = subprocess.Popen([
            self.snapshot_executable, "-r", self.snapshot_repo,
            "forget", restic_id, "--prune"],
            env=new_env, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        output, error = proc.communicate()
        if proc.returncode != 0:
            print(output, error)

    def describe(self, name, creds):
        new_env = os.environ.copy()
        new_env = {**new_env, **creds}
        new_env["RESTIC_PASSWORD"] = self.password

        restic_id, project_dir = self.get_restic_info(name, new_env)
        proc = subprocess.Popen([
            self.snapshot_executable, "-r", self.snapshot_repo,
            "ls", restic_id, "--recursive", project_dir, "--json"],
            env=new_env, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        output, error = proc.communicate()
        if proc.returncode != 0:
            print(output, error)

        snapshot_items = []
        for element in output.strip().split(b"\n"):
            snapshot_item = json.loads(element)
            path = snapshot_item.get("path")
            if path == project_dir:
                continue
            if path:
                snapshot_item["path"] = path[len(project_dir):]
                snapshot_items.append(snapshot_item)

        return snapshot_items

    def get_restic_info(self, tag, new_env):
        # Getting restic snapshot ID from snapshot_uuid
        # Need this because we cannot delete snapshot with --tag
        proc = subprocess.Popen([
            self.snapshot_executable, "-r", self.snapshot_repo,
            "snapshots", "--tag", tag],
            env=new_env, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        output, error = proc.communicate()
        if proc.returncode != 0:
            print(output, error)

        return parse_restic_snapshots_output(output)


snapshot_runner = SnapshotRunner()


def parse_restic_snapshots_output(output):
    """
    This function takes an ouput from the "restic snapshots" cmd
    and extract restic snapshot id and its project_dir
    """
    o = output.decode('UTF-8')
    assert len(o) >= 1, "No snapshots found"
    lines = o.split("\n")
    assert len(lines) >= 3, "Parsing restic output"
    snapshot = lines[2].split(" ")
    assert len(snapshot), "Parsing restic output"
    restic_id = snapshot[0]
    tags = snapshot[-3]
    project_dir = tags.split("project_dir=")
    assert len(project_dir) == 2, "Error parsing project_dir"
    return restic_id, project_dir[1]


def copy_file(to_s3, source, target, download):
    """Copy a file.

    The file source or target may be on S3.

    Args:
        to_s3 (bool): If this is True, then copy to/from S3, else the local
            disk. If this is True, then the file source or target will be a
            presigned URL to which GET or POST HTTP requests can be sent.
        source (str or S3 URL): Source file local pathname or S3 GET URL. If
            this is an S3 URL, target is assumed to be a local pathname.
        target (str or S3 URL): Target file local pathname or S3 URL with POST
            credentials. If this is an S3 URL, source is assumed to be a local
            pathname.
        download (bool): If this is True, then this will upload from source to
            target, else this will download.
    """
    try:
        if to_s3:
            if download:
                with open(target, 'wb') as f:
                    response = requests.get(source)
                    for block in response.iter_content(1024):
                        f.write(block)
            else:
                with open(source, 'rb') as f:
                    files = {'file': ('object', f)}
                    resp = requests.post(
                        target['url'], data=target['fields'], files=files)
                    assert resp.ok, resp.text
        else:
            shutil.copyfile(source, target)
    except (OSError, AssertionError) as e:
        logger.warn("Failed to copy file %s , aborting", source)
        raise e


def walk_files(roots, depth=0, exclude_files=None):
    """Helper function to get all snapshot files with a recursive walk.

    Args:
        roots: Top-level files to save. These may be directories.
        exclude_files: A list of files to skip during copy.

    Returns:
        (list, list): Tuple of (directories, files) seen when recursively
            walking the roots.
    """
    if exclude_files is None:
        exclude_files = []
    directories = []
    files = []
    if depth > 3:
        return directories, files
    for root in roots:
        if root in exclude_files:
            continue
        if os.path.isdir(root):
            directories.append(root)
            contents = [os.path.join(root, file) for file in os.listdir(root)]
            subdirectories, subfiles = walk_files(
                contents, depth + 1, exclude_files=exclude_files)
            directories += subdirectories
            files += subfiles
        else:
            files.append(root)

    return directories, files


def get_snapshot_files(project_definition):
    """Get all file metadata needed to create a snapshot.

    Args:
        project_definition: Project defininition.

    Returns:
        dict describing all file metadata needed for the snapshot.
    """
    project_dir = project_definition.root

    # Get the output files to save with the snapshot.
    output_files = []
    missing_output_files = []
    for output_file in project_definition.config.get('output_files', []):
        if os.path.exists(os.path.join(project_dir, output_file)):
            output_files.append(output_file)
        else:
            missing_output_files.append(output_file)

    # Get the input files to save with the snapshot. By default, this is all
    # files in the project directory and are not explicitly specified by the
    # user to be an output file in project.yaml.
    input_files = []
    for file in os.listdir(project_dir):
        input_files.append(file)

    # Recursively get all input and output files.
    input_directories, input_files = walk_files(
        input_files, exclude_files=output_files)
    output_directories, output_files = walk_files(output_files)
    return {
            "input_directories": input_directories,
            "input_files": input_files,
            "output_directories": output_directories,
            "output_files": output_files,
            "missing_output_files": missing_output_files,
            }


def create_snapshot(project_definition, yes, description=None, local=False):
    """Create a snapshot of a project.

    Args:
        project_definition: Project definition.
        yes: Don't ask for confirmation.
        description: An optional description of the snapshot.
        local: Whether the snapshot should be of a live session or
            the local project directory state.

    Raises:
        ValueError: If the current project directory does not match the project
            metadata entry in the database.
        Exception: If saving the snapshot files fails.
    """
    if not local:
        raise NotImplementedError(
            "Snapshots of a live session not currently supported.")

    # Find and validate the current project ID.
    project_dir = project_definition.root
    project_id = get_project_id(project_dir)

    files = get_snapshot_files(project_definition)
    with open(project_definition.cluster_yaml()) as f:
        cluster_config = yaml.safe_load(f)

    resp = send_json_request("snapshot_create", {
        "project_id": project_id,
        "project_config": json.dumps(project_definition.config),
        "cluster_config": json.dumps(cluster_config),
        "description": description if description else "",
        "files": files,
        }, post=True)

    snapshot_uuid = resp["uuid"]
    creds = resp["credentials"]

    try:
        snapshot_runner.upload(snapshot_uuid, project_dir, creds)
    except (OSError, AssertionError) as e:
        # Tell the server to delete the snapshot.
        delete_snapshot(project_dir, snapshot_uuid, True)
        raise e
    return snapshot_uuid


def delete_snapshot(project_dir, uuid, yes):
    """Delete the snapshot(s) with the given name.

    Delete the snapshot data from disk and the metadata from the database.

    Args:
        project_dir: Project root directory.
        uuid: The UUID of the snapshot to delete.
        yes: Don't ask for confirmation.

    Raises:
        ValueError: If the current project directory does not match the project
            metadata entry in the database.
    """
    # Find and validate the current project ID.
    project_id = get_project_id(project_dir)

    # Get the snapshots with the requested name.
    resp = send_json_request("snapshot_list", {
        "project_id": project_id,
        "snapshot_uuid": uuid,
        })
    snapshots = resp["snapshots"]
    if snapshots:
        snapshots_str = '\n'.join(snapshot["uuid"] for snapshot in snapshots)
        confirm("Delete snapshots?\n{}".format(snapshots_str), yes)
        snapshot_uuids = [snapshot["uuid"] for snapshot in snapshots]
        resp = send_json_request("snapshot_delete", {
            "snapshot_uuids": snapshot_uuids,
            }, post=True)

        assert "credentials" in resp

        snapshot_runner = SnapshotRunner()
        for name in snapshot_uuids:
            snapshot_runner.delete(name, resp["credentials"])

    else:
        logger.warn("No snapshots found with UUID %s", uuid)


def describe_snapshot(uuid):
    resp = send_json_request("snapshot_describe", {
        "snapshot_uuid": uuid,
    })
    return resp


def list_snapshots(project_dir):
    """List all snapshots associated with the given project.

    Args:
        project_dir: Project root directory.

    Returns:
        List of Snapshots for the current project.

    Raises:
        ValueError: If the current project directory does not match the project
            metadata entry in the database.
    """
    # Find and validate the current project ID.
    project_id = get_project_id(project_dir)
    resp = send_json_request("snapshot_list", {
        "project_id": project_id,
        })
    snapshots = resp["snapshots"]
    return [snapshot["uuid"] for snapshot in snapshots]


def get_snapshot_uuid(project_dir, snapshot_uuid):
    """Get a snapshot of the given project with the given name.

    Args:
        project_id: The ID of the project.
        snapshot_name: The name of the snapshot to get. If there are multiple
            snapshots with the same name, then the user will be prompted to
            choose a snapshot.
    """
    # Find and validate the current project ID.
    project_id = get_project_id(project_dir)
    resp = send_json_request("snapshot_list", {
        "project_id": project_id,
        "snapshot_uuid": snapshot_uuid,
        })
    snapshots = resp["snapshots"]
    if len(snapshots) == 0:
        raise ValueError(
            "No snapshots found with name {}".format(snapshot_uuid))
    snapshot_idx = 0
    if len(snapshots) > 1:
        print("More than one snapshot found with UUID {}. "
              "Which do you want to use?".format(snapshot_uuid))
        for i, snapshot in enumerate(snapshots):
            print("{}. {}".format(i + 1, snapshot["uuid"]))
        snapshot_idx = click.prompt(
            "Please enter a snapshot number from 1 to {}"
            .format(len(snapshots)), type=int)
        snapshot_idx -= 1
        if snapshot_idx < 0 or snapshot_idx > len(snapshots):
            raise ValueError(
                "Snapshot index {} is out of range"
                .format(snapshot_idx))
    return snapshots[snapshot_idx]["uuid"]


def download_snapshot(name, credentials, target_directory=None):
    """Download a snapshot to a local target directory.

    This will recreate the original directory structure of the snapshot. Only
    input files (those found in the project directory during the snapshot
    creation) will be downloaded, not output files specified in the
    project.yaml.

    Args:
        snapshot_info: Information about the snapshot as returned by
            snapshot_get.
        target_directory: Directory this snapshot gets downloaded to.
            If None, the snapshot will be downloaded to a temporary directory.

    Returns:
        tuple(str, str, str): The temporary local directory where the snapshot
        has been downloaded, the commit hash to check out if one was included
        in the snapshot.
    """
    if target_directory:
        snapshot_directory = target_directory
    else:
        snapshot_directory = TEMP_SNAPSHOT_DIRECTORY.format(time.time())

    snapshot_runner.download(name, target_directory, credentials)

    return snapshot_directory
