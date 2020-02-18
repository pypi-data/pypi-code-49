from disco.base_controller import BaseController
from disco.models import DockerImageDetails


class DockerImage(BaseController):
    """
    Docker image methods
    """

    @classmethod
    def list_docker_images(cls, limit=None, next_=None):
        """Show a list of all the docker images of this user.

                Args:
                    limit (int): pagination limit
                    next_: pagination next

                Returns:
                    list(): List of the docker images of this user.
                """

        res = cls.query('getDockerImagesByOwnerId', limit=limit,
                        ownerId=cls.get_current_user(), next=next_)

        if res is None:
            return []

        docker_images = [DockerImageDetails(docker_image) for docker_image in res['getDockerImagesByOwnerId']
                         if docker_image['isActive']]

        return docker_images
