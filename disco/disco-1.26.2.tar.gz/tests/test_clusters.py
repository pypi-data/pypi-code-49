from tests.base_test import BaseTest
import mock
import disco
from disco.models import ClusterDetails


class TestClusters(BaseTest):

    @BaseTest.with_config_and_env(authenticated=True)
    def test_list_clusters(self):
        with mock.patch('disco.gql.authentication.Authentication.query') as graphql_mock:
            graphql_mock.return_value = {'fetchProfile': {'defaultClusterId': '000000000000000000000000', 'clusters': [
                {'id': '000000000000000000000000', 'name': 'discoCloud', 'type': 'aws',
                 'cluster': {'region': 'us-west-2', 'externalAccountId': '651133521420',
                             'bucketName': 'disco-store-production'}, 'isLastConnectionCheckValid': True,
                 'isActive': True, 'enableCloudOffload': False},
                {'id': '5d877534fc4015000dd1df18', 'name': 'Itay', 'type': 'aws',
                 'cluster': {'region': 'us-west-1', 'externalAccountId': 'asfasf',
                             'bucketName': 'disco-store-63f7a91c7d7242d8fa3dae62dc249004'},
                 'isLastConnectionCheckValid': False, 'isActive': True, 'enableCloudOffload': False},
                {'id': '5d89d91698e7e4d4c542ad4e', 'name': 'complete-genomics', 'type': 'onPremise',
                 'cluster': {'region': 'us-west-2', 'externalAccountId': 'none',
                             'bucketName': 'disco-store-production'}, 'isLastConnectionCheckValid': True,
                 'isActive': False, 'enableCloudOffload': False}]}}

            result = disco.Cluster.list_clusters()

        assert isinstance(result, list)
        assert len(result) == 3
        assert isinstance(result[0], ClusterDetails)
        assert result[0].id == '000000000000000000000000'
        assert result[0].name == 'discoCloud'
        assert result[0].is_default
        assert result[0].type == 'aws'
        assert result[0].region == 'us-west-2'
        assert result[0].external_account_id == '651133521420'
        assert result[0].bucket_name == 'disco-store-production'
        assert result[0].is_last_connection_check_valid
        assert result[0].is_active
        assert not result[0].cloud_offload_enabled

    @BaseTest.with_config_and_env(authenticated=True)
    def test_fetch_and_validate_by_id_belongs_to_user(self):

        cluster_id = self.random_str('cluster_id')

        cluster_data = self._create_fake_cluster_response_data(cluster_id)

        clusters_list_data = [
            self._create_fake_cluster_response_data(),
            cluster_data,
            self._create_fake_cluster_response_data(),
        ]

        expected_cluster = ClusterDetails(cluster_data)

        with mock.patch('disco.gql.authentication.Authentication.query') as graphql_mock:
            graphql_mock.return_value = {
                'fetchProfile': {
                    'defaultClusterId': self.random_str('defaultClusterId'),
                    'clusters': clusters_list_data
                }
            }

            result = disco.Cluster.fetch_and_validate_by_id(cluster_id)

            assert isinstance(result, ClusterDetails)
            assert result.id == expected_cluster.id
            assert result.type == expected_cluster.type

    def _create_fake_cluster_response_data(self, cluster_id=None):
        return {
            'id': cluster_id or self.random_str('cluster_id'),
            'name': self.random_str('cluster_name'),
            'type': self.random_from(['aws', 'gcp', 'azure']),
            'cluster': {
                'region': self.random_str('region'),
                'externalAccountId': self.random_str('external_account_id'),
                'bucketName': self.random_str('bucket_name')
            },
            'isLastConnectionCheckValid': self.random_bool(),
            'isActive': self.random_bool(),
            'enableCloudOffload': self.random_bool()
        }
