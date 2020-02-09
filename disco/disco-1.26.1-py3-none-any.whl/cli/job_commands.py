import errno
import glob
import os
import time
from pathlib import Path
import click

from disco import Job, upload_file, input_files_from_bucket, Cluster
from disco.core.constants import JobStatus
from disco.core.exceptions import DiscoException, TimeOutError, GraphQLRequestException, \
    BucketPathsException, BucketPathsErrorTypes, RequestException
from disco.models import JobDetails

from .command_utils import info_message, list_to_table, \
    error_message, success_message, verify_logged_in, exception_message, ExpandedPath
from .context_state import pass_state
from .common_options import common_options

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


@click.group('job', context_settings=CONTEXT_SETTINGS)
def job_commands():
    """Manage jobs."""


@job_commands.command('create', context_settings=CONTEXT_SETTINGS, short_help="Create a new job.")
@click.option('-s', '--script', help='Local path to the script file to run.',
              type=ExpandedPath(exists=True))
@click.option('-i', '--input', 'inputs',
              help='Local comma-separated path to the input file(s) for the script, (wildcards allowed).')
@click.option('-b', '--bucket', 'raw_bucket_paths',
              help="Comma-separated paths for a bucket in your cluster"
                   " to scan for the input files for the script."
                   " Only file and directory paths are allowed. Wildcards are not supported.")
@click.option('-c', '--constants', help='Local path to the constants file that will be sent to each task.')
@click.option('-n', '--name', help='Job name.', prompt="Please enter job name")
@click.option('-r', '--run', help='Create and run the job.', is_flag=True)
@click.option('-w', '--wait', help='Wait for the job to finish.', is_flag=True)
@click.option('-cit', '--instance-type',
              help="Cluster instance type, options are: -s (small - default), -m (meduim), -l (large).",
              type=click.Choice(['s', 'm', 'l']), default='s')
@click.option('-cid', '--cluster-id', help="Cluster id to run the job on. "
                                           "You can use the ‘cluster list’ command to view your clusters. "
                                           "In case no cluster-id specified, Dis.co runs the job "
                                           "on the default Dis.co cluster.")
@click.option('-rep', '--repository-id', help='ID of the repository in which the script file resides.')
@click.option('-f', '--file-path', 'script_file_path_in_repo', help='Path in the Git repository to the script file.')
@click.option('-did', '--docker-image-id', help='The id of the docker image to run the job in')  # pylint: disable=all
@click.option('-to', '--timeout', help='Timeout on the wait for a job to finish (seconds, default: 1 hour)',
              default=(60 * 60))
@click.option('--debug-mode', hidden=True, is_flag=True)
@click.option('--dont-generate-req-file', hidden=True, is_flag=True)
@common_options
@pass_state
def create_job(state, script, inputs, raw_bucket_paths, constants, name, run, wait, instance_type, cluster_id,
               # pylint: disable=redefined-builtin
               repository_id, script_file_path_in_repo, docker_image_id, timeout, debug_mode, dont_generate_req_file):
    """
    Create a new job that can be launched immediately, or later.

    $ disco job create —n <job’s name> -s <script file path> -i <input file path> --run
    """
    if not verify_logged_in():
        return

    if script is None and repository_id is None:
        error_message("Please specify the script file using either `--script` "
                      "or `--repository-id` with `--file-path`")
        return
    if repository_id is not None and script_file_path_in_repo is None:
        error_message("Please specify the script file path using `--file-path`")
        return

    script_path = Path(script) if script is not None else Path(script_file_path_in_repo)
    if (script_path.suffix not in ['.sh', '.py']):
        error_message("Cannot use script file. Currently only Python and bash scripts are supported")
        return

    input_file_ids = []
    cluster = None

    if cluster_id:
        cluster = Cluster.fetch_and_validate_by_id(cluster_id)
        if not cluster:
            error_message(f'Cluster {cluster_id} is invalid or missing.')
            return

    if raw_bucket_paths:
        bucket_input_file_ids, is_error = _get_bucket_input_file_ids(raw_bucket_paths, cluster)
        if is_error:
            return
        input_file_ids += bucket_input_file_ids

    try:
        input_paths = get_file_list(inputs) if inputs else []
        const_paths = get_file_list(constants) if constants else []
    except FileNotFoundError as ex:
        error_message(str(ex))
        return

    try:
        show_progress_bar = not state.quite_mode
        const_file_ids, local_input_file_ids = upload_job_files(input_paths, const_paths, cluster, show_progress_bar)
        input_file_ids += local_input_file_ids

        script_file_id = None if script is None else upload_job_script_file(script, cluster, show_progress_bar)
        created_job = Job.create(script_file_id=script_file_id, input_file_ids=input_file_ids,
                                 constants_file_ids=const_file_ids, job_name=name, cluster_instance_type=instance_type,
                                 cluster_id=cluster_id, script_repo_id=repository_id,
                                 script_file_path_in_repo=script_file_path_in_repo, auto_start=run,
                                 upload_requirements_file=not dont_generate_req_file, docker_image_id=docker_image_id)

    except GraphQLRequestException as ex:
        messages = list(map(lambda error: error['message'], ex.errors))
        if any(msg.find('Unable to find artifacts repository') >= 0 or
               msg.find('doesn\'t own the repository provided') >= 0 for msg in messages):
            error_message('Invalid repository id (try `repository list` command)')
            return
        if any(msg.find('Unable to find docker image') >= 0 or
               msg.find(f'The docker image provided (id: {docker_image_id}) doesn\'t belong') >= 0 for msg in messages):
            error_message('Invalid docker image id (try `docker list` command)')
            return
        if any(msg.find('Insufficient balance') >= 0 for msg in messages):
            info_message(' Job created')
            error_message('You have reached your compute limit. '
                          'In order to continue running new jobs request more compute time.')
            return
    except DiscoException as ex:
        if debug_mode:
            print(ex)
        exception_message(ex)
        return

    job_status = None
    if run:
        info_message(f' Job {created_job.job_id} started')
    if wait and not run:
        info_message('Warning: waiting for a job that hadn\'t started')
    if wait:
        info_message(' Waiting for job to finish')
        try:
            job_status = created_job.wait_for_finish(timeout=timeout)
        except TimeOutError:
            error_message(f"Timed out while waiting for job {created_job.job_id}. "
                          f"Your job may still be running. "
                          f"Use 'disco job view' to check the job's status")
            return
    display_job(created_job.job_id, job_status)


@job_commands.command('start', context_settings=CONTEXT_SETTINGS, short_help="Start an existing job.")
@click.argument('job_id', metavar='<JOB_ID>')
def start_job(job_id):
    """
    Start an existing job.

    $ disco job start <job_id>

    You may use ‘job list’ command to get the job id.
    """
    if not verify_logged_in():
        return
    try:
        job = Job(job_id)
        job.start()
        success_message(f"Job {job_id} started")
    except GraphQLRequestException as ex:
        messages = list(map(lambda error: error['message'], ex.errors))
        if any(msg.find('Insufficient balance') >= 0 for msg in messages):
            error_message('You have reached your compute limit. '
                          'In order to continue running new jobs request more compute time.')
    except DiscoException as ex:
        error_message("Error occurred while starting job")
        exception_message(ex)


@job_commands.command('list', context_settings=CONTEXT_SETTINGS, short_help="List all jobs and their status.")
def list_jobs():
    """
    List all jobs and their status.

    $ disco job list

    Status Decription: \n

    Deleted\t The job failed\n\r
    Done\t The job is done\n
    Failed\t The job failed\n
    Listed\t The job is queued\n
    Stopped\t The job has stopped\n
    Unknown\t The job has no status\n
    Working\t The job is working\n
    """

    if not verify_logged_in():
        return
    try:
        job_list = Job.list_jobs()
        display_job_list(job_list)
    except DiscoException as ex:
        exception_message(ex)


@job_commands.command('stop', context_settings=CONTEXT_SETTINGS, short_help="Stop a running job.")
@click.argument('job_id', metavar='<JOB_ID>')
def stop_job(job_id):
    """
    Stop a running job.

    $ disco job stop <job_id>

    You may use ‘job list’ command to get the job id.
    """

    if not verify_logged_in():
        return
    try:
        job = Job(job_id)
        job.stop()
        success_message(f"Stopping job {job_id}")
    except DiscoException as ex:
        exception_message(ex)


@job_commands.command('archive', context_settings=CONTEXT_SETTINGS, short_help="Archive a specific job.")
@click.argument('job_id', metavar='<JOB_ID>')
def archive_job(job_id):
    """
    Archive a specific job.

    $ disco job archive <job_id>

    You may use ‘job list’ command to get the job id.
    """

    if not verify_logged_in():
        return

    try:
        job = Job(job_id)
        job.archive()
        success_message(f"Job {job_id} was archived")
    except DiscoException as ex:
        error_message("Failed to archive job")
        exception_message(ex)


@job_commands.command('view', context_settings=CONTEXT_SETTINGS, short_help="View specific job's details.")
@click.argument('job_id', metavar='<JOB_ID>')
def view_job(job_id):
    """
    View specific job's details.

    $ disco job view <job_id>

    You may use ‘job list’ command to get the job id.
    """

    if not verify_logged_in():
        return
    try:
        job = Job(job_id)
        details = job.get_details()
        display_job_details(details)
    except DiscoException as ex:
        error_message("Error occurred while getting job details")
        exception_message(ex)


@job_commands.command('download-results', context_settings=CONTEXT_SETTINGS, short_help="Download results of a job.")
@click.argument('job_id', metavar='<JOB_ID>')
@click.option('-d', '--destination', prompt="Path for result files",
              help="The destination path to download the result files to.")
def download_results(job_id, destination):
    """
    Download results of a job.

    $ disco job download-results <job_id> -d <results files path>

    You may use ‘job list’ command to get the job id.
    """

    if not verify_logged_in():
        return
    dest_dir = Path(destination)
    if not dest_dir.exists():
        error_message(f"{destination} doesn't exist")
        return
    if not dest_dir.is_dir():
        error_message("Destination must be a folder")
        return

    try:
        task_results = Job(job_id).get_results(block=True)
        for task_result in task_results:
            task_dir = os.path.join(destination, f"{int(time.time() * 1000)}-{task_result.task_id}")
            safe_make_dirs(task_dir)
            task_result.write_files(task_dir)
            success_message("Results downloaded successfully")
    except DiscoException as ex:
        error_message(f"Error occurred while getting job {job_id} results")
        exception_message(ex)


def display_job_list(job_list):
    """Receives a list of jobs and prints them as a table"""
    tabulated_array = []
    for job in job_list:
        tabulated_array.append([job.id, job.name, job.status])
    displayable_table = list_to_table(tabulated_array, ["ID", "Name", "Status"])
    info_message(displayable_table)


def display_job(job, job_status=None):
    """Displays the job id on the screen"""
    if job_status is None:
        info_message(f"Created job with id {job}")
    elif job_status == JobStatus.failed:
        error_message(f"Job {job} failed")
    elif job_status == JobStatus.done:
        success_message(f"Job {job} finished successfully")
    else:
        info_message(f"Created job with id {job}")


def display_job_details(job: JobDetails):
    """Receives a job details and prints it to the screen"""
    info_message(f"Name: {job.name}")
    info_message(f"Status: {job.status}")
    info_message('Task summary')
    info_message('------------')
    info_message(f"Waiting: {job.tasks_summary.queued}")
    info_message(f"queued: {job.tasks_summary.queued}")
    info_message(f"running: {job.tasks_summary.running}")
    info_message(f"failed: {job.tasks_summary.failed}")
    info_message(f"success: {job.tasks_summary.success}")


def get_file_list(file_list_string):
    """
    Args:
        file_list_string:

    Returns:
        list
    """
    file_paths = []
    split_file_list = file_list_string.split(',')
    for file_path in split_file_list:
        full_file_path = os.path.expanduser(file_path)
        if full_file_path.find('*') >= 0:
            files = glob.glob(full_file_path)
            files.sort(key=os.path.getmtime)
            file_paths += [Path(file) for file in files]
            continue
        path = Path(full_file_path)
        if not path.exists():
            raise FileNotFoundError(f"{full_file_path} doesn't exist")
        if path.is_dir():
            expanded_file = list(Path(full_file_path).glob('**/*'))
            if len(expanded_file) == 0:
                raise FileNotFoundError(f"Folder {full_file_path} is empty")
            file_paths += expanded_file
        else:
            file_paths.append(path)
    return file_paths


def upload_job_script_file(script, cluster, show_progress_bar):
    """
    Args:
        script: path to script file.
        cluster (ClusterDetails):
        show_progress_bar (bool):

    Returns:
        DB Id for script file.
    """
    script_file_id = upload_file(Path(script).name, Path(script), cluster, show_progress_bar)
    info_message(" Script file uploaded")
    return script_file_id


def upload_job_files(input_paths, const_paths, cluster, show_progress_bar=True):
    """
    Args:
        input_paths: list of paths to input file
        const_paths: list of paths to constant files
        cluster (ClusterDetails):
        show_progress_bar (bool):

    Returns:
        DB Ids for constant files and input files

    """
    input_file_ids = []
    for input_file in input_paths:
        input_file_id = upload_file(input_file.name, input_file, cluster, show_progress_bar)
        input_file_ids.append(input_file_id)
        info_message(f" Uploaded input file {input_file}")
    const_file_ids = []
    for const_file in const_paths:
        const_file_id = upload_file(const_file.name, const_file, cluster, show_progress_bar)
        const_file_ids.append(const_file_id)
        info_message(f" Uploaded constants file {const_file}")
    return const_file_ids, input_file_ids


def _get_bucket_input_file_ids(raw_bucket_paths, cluster):
    """
    Args:
        raw_bucket_paths (str):
        cluster (ClusterDetails):

    Returns:
        (list, bool): list of file ids and a flag if we got an error
    """

    is_error = True
    empty_result = ([], is_error)

    if not cluster:
        error_message("Please specify the cluster ID which contains your bucket, using `--cluster-id`")
        return empty_result

    if not cluster.supports_register_files_from_bucket:
        error_message("Uploading files from a bucket only is only supported for AWS, GCP and Azure clusters.")
        return empty_result

    bucket_paths = raw_bucket_paths.split(',')
    try:
        bucket_input_file_ids = input_files_from_bucket(bucket_paths, cluster.id)
    except RequestException as error:
        error_message(str(error))
        return empty_result
    except BucketPathsException as error:
        invalid_bucket_paths = sorted([bucket_path for bucket_path, error_type in error.bucket_paths_errors.items()
                                       if error_type == BucketPathsErrorTypes.InvalidPath])

        empty_bucket_paths = sorted([bucket_path for bucket_path, error_type in error.bucket_paths_errors.items()
                                     if error_type == BucketPathsErrorTypes.NoFilesInPath])

        if len(invalid_bucket_paths) > 0:
            error_message('Invalid or missing buckets paths specified:')
            for bucket_path in invalid_bucket_paths:
                error_message(bucket_path)

        if len(empty_bucket_paths) > 0:
            error_message('No input files found in the following buckets paths:')
            for bucket_path in empty_bucket_paths:
                error_message(bucket_path)

        return empty_result

    if len(bucket_input_file_ids) == 0:
        error_message('No input files found in the specified buckets paths')
        return empty_result

    info_message(f'Found {len(bucket_input_file_ids)} input files in your bucket')

    return bucket_input_file_ids, False


def safe_make_dirs(dir_path):
    """

    Args:
        dir_path: directory to create

    Returns:

    """
    try:
        os.makedirs(dir_path)
    except OSError as ex:
        if ex.errno != errno.EEXIST:
            raise
