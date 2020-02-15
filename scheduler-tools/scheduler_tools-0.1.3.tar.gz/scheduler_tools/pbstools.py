import subprocess
import os
import re

# QSUB to SLURM Mappings
# queue_name    -> partition
# walltime      -> time
SBATCH_TEMPLATE = """#!/bin/bash

#SBATCH --partition={partition}
#SBATCH --time={walltime}
#SBATCH --output={out_err_format}.out
#SBATCH --error={out_err_format}.err
{conditional_array_string}
{conditional_deps_string}

srun {task_name} {conditional_verbose}
"""


def submit_jobs(files, json_obj, tmp_file_name="tmp.script"):

    # Cast files to a list
    if not isinstance(files, list):
        files = [files]

    # Determine array structure
    task_path_sep = files[0].split("/")
    shell_script_name = task_path_sep[-1]

    # Only manipulate the task name if it is an array operation
    # This regex will find scripts that match similar patterns such as: `im2feats_123.sh`
    # The important part here is that we are looking for `_***.sh`, if the script name has this
    # it indicates that the script is part of an job array operation.
    if re.match(r"^[a-zA-Z0-9]*_[0-9]*\.sh$", shell_script_name):
        # Great, this is an array job split the task id from the job type
        task_parts = shell_script_name.split("_")
        # Get the parent path
        original_path = "/".join(task_path_sep[:-1])

        # Use the job type to create formatted strings to be attached to sbatch
        # This will result in something like the following for task_name:
        # /path/to/original/parent/im2feats_$SLURM_ARRAY_TASK_ID.sh
        # and something like the following for out_err_format:
        # /path/to/original/parent/im2feats_%a.sh
        task_name = f"{original_path}/{task_parts[0]}_$SLURM_ARRAY_TASK_ID.sh"
        out_err_format = f"{original_path}/{task_parts[0]}_%a.sh"
    else:
        # This isn't part of a job array operation
        # The task name and out_err_format will then just be the filename
        task_name = files[0]
        out_err_format = files[0]

    # Retain max tasks for later
    max_tasks = None
    if len(files) > 1:
        # Split the file path, get the last component, split the name, get the suffix, split the suffix, get number
        # For a collection of files that look like the following:
        # ["/allen/aics/modeling/gregj/results/ipp/scp_2019_03_25/scripts/im2feats_0.sh",
        #  "/allen/aics/modeling/gregj/results/ipp/scp_2019_03_25/scripts/im2feats_1.sh"
        #  ...
        #  "/allen/aics/modeling/gregj/results/ipp/scp_2019_03_25/scripts/im2feats_746.sh"]
        # This will find the max integer value of these files. In the above example it would result in 746.
        # This is done by split the file by the os filepath sep,
        # retrieving the filename (the last item in the created list),
        # splitting the filename into its task type and task array value using "_"
        # retrieving the value by selecting the last item in the task details array
        # and finally removing the suffix by splitting my "." and selecting the first item
        max_tasks = max([int(file.split("/")[-1].split("_")[-1].split(".")[0]) for file in files])
        array_string = f"#SBATCH --array=0-{max_tasks}%{json_obj['max_parallel_jobs']}"
    else:
        array_string = ""

    # Create deps string
    if len(json_obj.get("deps", [])) > 0:
        # As dependecies are created and added to the json object as run_scp_jobs progresses,
        # this checks for the current value of that dependency list and if there is one, as in the actual depencency
        # key exists and has at least one item, it will generate an sbatch dependency string to be attached to the
        # sbatch headers.
        # sbatch dependencys follow the template "<JOB_ID>:<JOB_ID>:<JOB_ID>...:<JOB_ID>"
        deps_string = "#SBATCH --dependency=afterany:{}".format(
            ":".join([str(dep_job) for dep_job in json_obj["deps"]])
        )
    else:
        deps_string = ""

    # Create verbose conditional
    if json_obj.get("debug", "false").lower() == "true":
        debug = "--verbose"
    else:
        debug = ""

    sbatch_str = SBATCH_TEMPLATE.format(
        partition=json_obj["partition"],
        walltime=json_obj["walltime"],
        conditional_array_string=array_string,
        conditional_deps_string=deps_string,
        task_name=task_name,
        out_err_format=out_err_format,
        conditional_verbose=debug
    )

    tmp_file = json_obj["script_dir"] + os.sep + tmp_file_name
    with open(tmp_file, "w") as write_out:
        write_out.write(sbatch_str)

    # Push sbatch file to slurm queue
    proc = subprocess.Popen("sbatch " + tmp_file, stdout=subprocess.PIPE, shell=True)
    out, err = proc.communicate()

    # As slurm accepts jobs, it returns the job id in a string along with some other text
    # This will find the job id returned by spliting the string by space and getting the last one for each line ("\n")
    # of returned text from the slurm sbatch request.
    # However, as this is somewhat legacy code where previously multiple jobs were submitted by now in SLURM a single
    # job is submitted that spawns a lot of additional jobs due to array tasking, we really only care about the first
    # one (or really only a single job id will ever be returned).
    # Regardless, due to this change we need to construct all the actual job_ids that are created from the sbatch and
    # not just the original job that spawned all the sub jobs.
    # To do this we use the max_tasks value we stored earlier and construct a range over it.
    job_id = [int(token.split(" ")[-1]) for token in out.decode("utf8").split('\n') if token != ""][0]
    if max_tasks:
        job_ids = [f"{job_id}_{i}" for i in range(max_tasks + 1)]
    else:
        job_ids = [job_id]

    return job_ids
