import pytest

import disco
from tests.live import env


@pytest.mark.skipif(env.skip, reason=env.reason)
class TestClustersLive(object):
    def test_list_jobs(self):
        clusters = disco.Cluster.list_clusters()
        assert isinstance(clusters, list)
        if clusters:
            assert clusters[0].name == 'discoCloud'
            assert isinstance(clusters[0].is_default, bool)
            assert clusters[0].id is not None
            assert clusters[0].type == 'aws'
            assert clusters[0].region is not None
            assert clusters[0].external_account_id is not None
            assert clusters[0].bucket_name is not None
            assert clusters[0].is_last_connection_check_valid
            assert clusters[0].is_active
