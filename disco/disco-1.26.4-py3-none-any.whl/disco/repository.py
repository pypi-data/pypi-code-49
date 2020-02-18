from disco.base_controller import BaseController
from disco.models import RepositoryDetails


class Repository(BaseController):
    """
    Repository methods
    """

    @classmethod
    def list_repositories(cls, limit=None, next_=None):
        """Show a list of all the repositories of this user.

                Args:
                    limit (int): pagination limit
                    next_: pagination next

                Returns:
                    list(): List of the repositories of this user.
                """

        res = cls.query('getArtifactsRepositories', limit=limit,
                        ownerId=cls.get_current_user_id(), next=next_)

        if res is None:
            return []

        active_repositories = [RepositoryDetails(repository) for repository in res['getArtifactsRepositories']
                               if repository['isActive']]

        return active_repositories
