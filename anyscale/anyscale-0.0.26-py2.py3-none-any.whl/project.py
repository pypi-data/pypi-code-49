from click import ClickException
import os


# Pathnames specific to Ray's project directory structure.
PROJECT_ID_BASENAME = 'project-id'
RAY_PROJECT_DIRECTORY = 'ray-project'


def get_project_id(project_dir):
    """
    Args:
        project_dir: Project root directory.

    Returns:
        The ID of the associated Project in the database.

    Raises:
        ValueError: If the current project directory does
            not contain a project ID.
    """
    project_id_filename = os.path.join(
        project_dir, RAY_PROJECT_DIRECTORY, PROJECT_ID_BASENAME)
    if not os.path.isfile(project_id_filename):
        raise ClickException(
            "Ray project in {} not registered yet. "
            "Did you run 'any project create'?".format(project_dir))
    with open(project_id_filename, 'r') as f:
        project_id = f.read()
    try:
        project_id = int(project_id)
    except ValueError:
        raise ClickException(
            "{} does not contain a valid project ID"
            .format(project_id_filename))
    return project_id
