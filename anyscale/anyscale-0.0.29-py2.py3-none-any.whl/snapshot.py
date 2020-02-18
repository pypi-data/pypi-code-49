import json
import logging
import requests
import os
import shutil
import subprocess
import time

import click
from git import Git
import ray.ray_constants
import yaml

from anyscale.project import get_project_id
from anyscale.common import (COMMIT_PATCH_BASENAME)
from anyscale.util import (confirm, send_json_request)


logging.basicConfig(format=ray.ray_constants.LOGGER_FORMAT)
logger = logging.getLogger(__file__)

# A temporary directory to download snapshots to.
TEMP_SNAPSHOT_DIRECTORY = '/tmp/anyscale-snapshot-{}'


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


def walk_files(roots, exclude_files=None):
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
    for root in roots:
        if root in exclude_files:
            continue
        if os.path.isdir(root):
            directories.append(root)
            contents = [os.path.join(root, file) for file in os.listdir(root)]
            subdirectories, subfiles = walk_files(
                contents, exclude_files=exclude_files)
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
    # files in the project directory that are not tracked by git and are not
    # explicitly specified by the user to be an output file in project.yaml.
    input_files = []
    commit_hash = None
    commit_patch_location = None
    if project_definition.git_repo() is not None:
        # Get and save the current git repo state.
        git = Git('.')
        try:
            commit_hash = git.rev_parse('HEAD')
        except Exception:
            pass

        # We succeeded in getting a git hash. Get the rest of the git state.
        if commit_hash is not None:
            # Find all files in the project that are not
            # already tracked by git.
            files = git.ls_files(
                project_dir, exclude_standard=True,
                others=True, directory=True)
            for untracked_file in files.split('\n'):
                # Save the pathname relative to the project so
                # that we can later recreate the directory structure
                # inside the project.
                untracked_file = os.path.relpath(
                    untracked_file, project_dir)
                input_files.append(untracked_file)
            commit_hash = git.rev_parse('HEAD')
            # Save the git diff, if any.
            diff = git.diff()
            if diff:
                filename = "{}.{}".format(COMMIT_PATCH_BASENAME, time.time())
                commit_patch_location = os.path.join("/tmp", filename)
                with open(commit_patch_location, 'w+') as f:
                    f.write(diff)
                    f.write('\n')
    else:
        for file in os.listdir(project_dir):
            input_files.append(file)

    # Confirm the files to save with the snapshot.
    if input_files or output_files or missing_output_files:
        print("Creating a new snapshot containing the files:")

        if input_files:
            print("Input files:")
            for file in input_files:
                print(" ", file)
        if output_files:
            print("Output files:")
            for file in output_files:
                print(" ", file)
        if missing_output_files:
            print("Missing output files:")
            for file in missing_output_files:
                print(" ", file)

    # Recursively get all input and output files.
    input_directories, input_files = walk_files(
        input_files, exclude_files=output_files)
    output_directories, output_files = walk_files(output_files)
    return {
            "commit_hash": commit_hash,
            "commit_patch_location": commit_patch_location,
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
    snapshot_to_s3 = resp["snapshot_to_s3"]
    mappings = resp["locations"]

    try:
        for source, target in mappings.items():
            copy_file(snapshot_to_s3, source, target, download=False)
    except (OSError, AssertionError) as e:
        # Tell the server to delete the snapshot.
        send_json_request("snapshot_delete", {
            "snapshot_uuids": [snapshot_uuid],
            }, post=True)
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
        send_json_request("snapshot_delete", {
            "snapshot_uuids": snapshot_uuids,
            }, post=True)
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


def download_snapshot(snapshot_info, target_directory=None, apply_patch=False):
    """Download a snapshot to a local target directory.

    This will recreate the original directory structure of the snapshot. Only
    input files (those found in the project directory during the snapshot
    creation) will be downloaded, not output files specified in the
    project.yaml. The git commit patch will also be downloaded, if any.

    Args:
        snapshot_info: Information about the snapshot as returned by
            snapshot_get.
        target_directory: Directory this snapshot gets downloaded to.
            If None, the snapshot will be downloaded to a temporary directory.
        apply_patch: If True, apply the git patch.

    Returns:
        tuple(str, str, str): The temporary local directory where the snapshot
        has been downloaded, the commit hash to check out if one was included
        in the snapshot, and the git patch to apply if one was included.
    """

    snapshot_to_s3 = snapshot_info["snapshot_to_s3"]
    commit_hash = snapshot_info["commit_hash"]
    commit_patch_source = snapshot_info["commit_patch_location"]
    input_directories = snapshot_info["input_directories"]
    input_files = snapshot_info["input_files"]

    if target_directory:
        snapshot_directory = target_directory
    else:
        snapshot_directory = TEMP_SNAPSHOT_DIRECTORY.format(time.time())

    for dir in input_directories:
        target = os.path.join(snapshot_directory, dir)
        if not os.path.exists(target):
            os.makedirs(target)

    for source, target in input_files.items():
        target = os.path.join(snapshot_directory, target)
        dirname = os.path.dirname(target)
        os.makedirs(dirname, exist_ok=True)
        copy_file(snapshot_to_s3, source, target, download=True)

    if commit_patch_source is not None:
        commit_patch = COMMIT_PATCH_BASENAME
        target = os.path.join(snapshot_directory, commit_patch)
        copy_file(snapshot_to_s3, commit_patch_source, target, download=True)
    else:
        commit_patch = None

    if apply_patch:
        if commit_hash:
            # Point the repo to the commit associated with the snapshot.
            subprocess.check_call(
                "git reset && git checkout . && git checkout {} && "
                "git clean -fxd".format(commit_hash),
                shell=True)

        # Apply the git diff to the session's project directory, if any.
        if commit_patch:
            # Remove the patch after applying.
            subprocess.check_call(
                "git apply {} && rm {}".format(commit_patch, commit_patch),
                shell=True)

    return snapshot_directory, commit_hash, commit_patch
