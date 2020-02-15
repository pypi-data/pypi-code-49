from .pbstools import submit_jobs
import os
import string
import json
import shutil


def scatter(ndat, prefs, template_str):
    verbose = prefs["verbose"]

    # Get the template string
    template = string.Template(prefs[template_str]["template"])

    myjob = dict()

    save_files = list()

    if verbose:
        print("Printing jobs scatter jobs for " + template_str)

    # Slurm maxes out at ~32000 task array size
    # This changes how rows are selected by multiplying by tasks_per_job instead of creating a range using it
    reduced_range = int(ndat / prefs["job_prefs"]["tasks_per_job"]) + 1

    # For every cell
    for i in range(reduced_range):

        job_top = i * prefs["job_prefs"]["tasks_per_job"] + prefs["job_prefs"]["tasks_per_job"]
        if job_top > ndat:
            job_top = ndat

        job_range = range(i * prefs["job_prefs"]["tasks_per_job"], job_top)

        # Get the info required to build that job from the data spreadsheet
        myjob["prefs_path"] = prefs["my_path"]
        myjob["save_log_path"] = prefs["save_log_path"]
        myjob["row_index"] = " ".join([str(job_id) + " " for job_id in job_range])

        # Apply job info to the template
        outstr = prefs["prefix"] + "\n" + template.substitute(myjob)

        save_file = (
            prefs["job_prefs"]["script_dir"]
            + os.sep
            + template_str
            + "_"
            + str(i)
            + ".sh"
        )

        text_file = open(save_file, "w")
        text_file.write(outstr)
        text_file.close()

        save_files.append(save_file)

        tmp_file = "tmp_" + template_str + ".sh"

    return submit_jobs(save_files, prefs["job_prefs"], tmp_file_name=tmp_file)


def gather(prefs, template_str):
    verbose = prefs["verbose"]

    # Get the template string
    template = string.Template(prefs[template_str]["template"])

    if verbose:
        print("Printing " + template_str)

    # Get the info required to build that job from the data spreadsheet
    myjob = dict()
    myjob["prefs_path"] = prefs["my_path"]
    myjob["save_log_path"] = prefs["save_log_path"]

    # Apply job info to the template
    outstr = prefs["prefix"] + "\n" + template.substitute(myjob)

    save_file = prefs["job_prefs"]["script_dir"] + os.sep + template_str + ".sh"

    text_file = open(save_file, "w")
    text_file.write(outstr)
    text_file.close()

    tmp_file = "tmp_" + template_str + ".sh"

    return submit_jobs(save_file, prefs["job_prefs"], tmp_file_name=tmp_file)


def setup_prefs(json_path):
    with open(json_path) as f:
        prefs = json.load(f)

    #     pdb.set_trace()
    if "save_parent" not in prefs["global_vars"]:
        prefs["global_vars"]["save_parent"] = os.getcwd()

    prefs["save_parent"] = os.path.abspath(prefs["global_vars"]["save_parent"])

    with open(json_path, "w") as f:
        json.dump(prefs, f, indent=4, separators=(",", ": "))

    # make the parent directory if it doesnt exist
    if not os.path.exists(prefs["save_parent"]):
        os.makedirs(prefs["save_parent"])

    json_path_local = prefs["save_parent"] + os.sep + "prefs.json"
    if not os.path.exists(json_path_local):
        # make a copy of the json object in the parent directory
        shutil.copyfile(json_path, json_path_local)
    else:
        # use the local copy
        print("Local copy of preference file already exists at " + json_path_local)
        with open(json_path_local) as f:
            prefs = json.load(f)

    # record the location of the json object
    prefs["my_path"] = json_path_local
    # record the location of the data object
    prefs["save_log_path"] = prefs["save_parent"] + os.sep + prefs["data_log_name"]
    prefs["job_prefs"]["script_dir"] = (
        prefs["save_parent"] + os.sep + prefs["script_dir"]
    )

    if not os.path.exists(prefs["job_prefs"]["script_dir"]):
        os.makedirs(prefs["job_prefs"]["script_dir"])

    prefs["verbose"] = prefs["global_vars"]["verbose"]

    return prefs
