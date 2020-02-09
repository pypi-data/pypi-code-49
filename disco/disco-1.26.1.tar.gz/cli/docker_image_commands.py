import click

from cli.command_utils import info_message, list_to_table
from disco import DockerImage

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


@click.group(context_settings=CONTEXT_SETTINGS)
def docker():
    """
    Manage docker images.
    """


@docker.command('list', context_settings=CONTEXT_SETTINGS, short_help="List of docker images of the current user.")
def list_dockers():
    """
    List of docker images of the current user.

    $ disco docker list
    """
    docker_images = DockerImage.list_docker_images()
    if len(docker_images) > 0:
        _display_docker_images(docker_images)
    else:
        info_message("There are no set docker images for your account")


def _display_docker_images(docker_images_list):
    """
    Display docker images as table
    Args:
        docker_images_list: list of docker images details

    Returns:
    """
    docker_images_table = [[docker_img.id, docker_img.name, docker_img.repository_type, docker_img.path,
                            docker_img.entry_point] for docker_img in docker_images_list]
    info_message(list_to_table(docker_images_table, headers=["ID", "Name", "Repository Type", "Path", "Entry Point"]))
