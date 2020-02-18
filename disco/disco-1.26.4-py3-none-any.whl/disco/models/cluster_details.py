from disco.core.constants import ClusterType
from .base_model import BaseModel

REGISTER_FILES_FROM_BUCKET_SUPPORTED_CLUSTER_TYPES = [ClusterType.AWS, ClusterType.GCP, ClusterType.Azure]


class ClusterDetails(BaseModel):
    """
    Cluster Details
    """

    def __init__(self, data, is_default_cloud=False):
        super(ClusterDetails, self).__init__(data)
        self._is_default = is_default_cloud

    @property
    def is_default(self):
        """
        Is this the default cluster, is it???
        Returns: True if this is the default cluster

        """
        return self._is_default

    @property
    def id(self):
        """
        Returns:
            str
        """
        return self._data.get('id')

    @property
    def name(self):
        """
        Cluster name
        Returns (str): cluster name

        """
        return self._data.get('name')

    @property
    def type(self):
        """
        Cluster cloud type
        Returns (str): cluster cloud name

        """
        return self._data.get('type')

    @property
    def region(self):
        """
        Cluster region
        Returns (str): cluster region

        """
        return self._data.get('cluster', {}).get('region')

    @property
    def external_account_id(self):
        """
        External cloud account id
        Returns (str): external account id

        """
        return self._data.get('cluster', {}).get('externalAccountId')

    @property
    def bucket_name(self):
        """
        The name of the bucket for storage
        Returns (str): Cloud storage bucket name

        """
        return self._data.get('cluster', {}).get('bucketName')

    @property
    def is_last_connection_check_valid(self):
        """
        Did the last connection check pass
        Returns (boolean): true is last connection test passed

        """
        return self._data.get('isLastConnectionCheckValid')

    @property
    def is_active(self):
        """
        Is the cloud active or disabled
        Returns (boolean): True is the cloud is not disabled

        """
        return self._data.get('isActive')

    @property
    def cloud_offload_enabled(self):
        """
        For on-prem if cloud offload is enabled
        Returns (boolean): True if cloud offload is enabled

        """
        return self._data.get('enableCloudOffload')

    @property
    def supports_register_files_from_bucket(self):
        """
        Is the cluster supports registering files directly from a cloud bucket

        Returns: bool
        """
        return ClusterType(self.type) in REGISTER_FILES_FROM_BUCKET_SUPPORTED_CLUSTER_TYPES
