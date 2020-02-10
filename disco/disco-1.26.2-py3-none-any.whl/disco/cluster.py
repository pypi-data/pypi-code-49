from disco.base_controller import BaseController
from disco.models import ClusterDetails


class Cluster(BaseController):
    """
    Cluster methods
    """

    @classmethod
    def list_clusters(cls, limit=None, next_=None):
        """Show a list of all the clusters applicable for this user.

                Args:
                    limit (int): pagination limit
                    next_: pagination next

                Returns:
                    list(ClusterDetails): List of the clusters belonging to this user.
                """

        res = cls.query('fetchProfileClusters', limit=limit,
                        id=cls.get_current_user(), next=next_)

        if res is None:
            return []
        return [ClusterDetails(cluster, res['fetchProfile']['defaultClusterId'] == cluster['id'])
                for cluster in res['fetchProfile']['clusters']]

    @classmethod
    def fetch_and_validate_by_id(cls, cluster_id):
        """
        Validate that the cluster_id belongs to the user

        Args:
            cluster_id (str):

        Returns:
            False if invalid or ClusterDetails if valid
        """
        user_clusters = cls.list_clusters()
        cluster = next(cluster for cluster in user_clusters if cluster.id == cluster_id)

        if not cluster:
            return False

        return cluster
