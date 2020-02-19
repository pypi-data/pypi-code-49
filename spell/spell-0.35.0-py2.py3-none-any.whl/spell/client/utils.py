import requirements

from spell.api.models import RunRequest


def get_run_request(client, kwargs):
    """Converts an python API request's kwargs to a RunRequest"""
    # grab conda env file contents
    if "conda_file" in kwargs:
        with open(kwargs.pop("conda_file")) as conda_file:
            kwargs["conda_file"] = conda_file.read()

    # grab pip packages from requirements file
    pip_packages = []
    if "pip_packages" in kwargs:
        pip_packages = kwargs.pop("pip_packages")
    if "requirements_file" in kwargs:
        with open(kwargs.pop("requirements_file"), 'r') as rf:
            for req in requirements.parse(rf):
                pip_packages.append(req.line)

    # set workflow id
    if "workflow_id" not in kwargs and client.active_workflow:
        kwargs["workflow_id"] = client.active_workflow.id

    return RunRequest(run_type="user", pip_packages=pip_packages, **kwargs)
