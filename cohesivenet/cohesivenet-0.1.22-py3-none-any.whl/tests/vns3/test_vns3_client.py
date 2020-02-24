from __future__ import absolute_import

import pytest

from tests.rest_mock import RestClientMock

import cohesivenet
from cohesivenet import VNS3Client, models, Configuration
from cohesivenet.rest import ApiException


class TestVNS3Client(object):
    """MonitoringAlertingApi unit test stubs"""

    def test_api_properties(self):
        """Test all API groups are accessible as properties
        """
        api_client = VNS3Client(
            configuration=Configuration(
                host="0.0.0.0:8000",
                username="api",
                password="password",
                verify_ssl=False,
            )
        )

        assert hasattr(api_client, "bgp") and type(api_client.bgp) is cohesivenet.BGPApi
        assert (
            hasattr(api_client, "config")
            and type(api_client.config) is cohesivenet.ConfigurationApi
        )
        assert (
            hasattr(api_client, "firewall")
            and type(api_client.firewall) is cohesivenet.FirewallApi
        )
        assert (
            hasattr(api_client, "high_availability")
            and type(api_client.high_availability) is cohesivenet.HighAvailabilityApi
        )
        assert (
            hasattr(api_client, "ipsec")
            and type(api_client.ipsec) is cohesivenet.IPsecApi
        )
        assert (
            hasattr(api_client, "interfaces")
            and type(api_client.interfaces) is cohesivenet.InterfacesApi
        )
        assert (
            hasattr(api_client, "licensing")
            and type(api_client.licensing) is cohesivenet.LicensingApi
        )
        assert (
            hasattr(api_client, "monitoring")
            and type(api_client.monitoring) is cohesivenet.MonitoringAlertingApi
        )
        assert (
            hasattr(api_client, "network_edge_plugins")
            and type(api_client.network_edge_plugins)
            is cohesivenet.NetworkEdgePluginsApi
        )
        assert (
            hasattr(api_client, "overlay_network")
            and type(api_client.overlay_network) is cohesivenet.OverlayNetworkApi
        )
        assert (
            hasattr(api_client, "peering")
            and type(api_client.peering) is cohesivenet.PeeringApi
        )
        assert (
            hasattr(api_client, "routing")
            and type(api_client.routing) is cohesivenet.RoutingApi
        )
        assert (
            hasattr(api_client, "snapshots")
            and type(api_client.snapshots) is cohesivenet.SnapshotsApi
        )
        assert (
            hasattr(api_client, "sys_admin")
            and type(api_client.sys_admin) is cohesivenet.SystemAdministrationApi
        )

    def test_get_controller_state(self):
        api_client = VNS3Client(
            configuration=Configuration(
                host="0.0.0.0:8000",
                username="api",
                password="password",
                verify_ssl=False,
            )
        )

        state = api_client.controller_state
        assert type(state) is dict
        assert len(state) == 0

    def test_add_controller_state(self):
        api_client = VNS3Client(
            configuration=Configuration(
                host="0.0.0.0:8000",
                username="api",
                password="password",
                verify_ssl=False,
            )
        )

        api_client.add_to_state("private_ip", "10.0.24.30")
        state = api_client.controller_state
        assert "private_ip" in state and state["private_ip"] == "10.0.24.30"
        assert len(state) == 1

    def test_update_controller_state(self):
        api_client = VNS3Client(
            configuration=Configuration(
                host="0.0.0.0:8000",
                username="api",
                password="password",
                verify_ssl=False,
            )
        )

        updates = {"container_network": "192.169.16.0/28", "subnet": "10.0.2.0/24"}
        api_client.update_state(updates)
        state = api_client.controller_state
        assert set(updates.keys()).issubset(set(state.keys()))
        assert state["subnet"] == updates["subnet"]
        assert len(state) == 2

    def test_query_state(self):
        api_client = VNS3Client(
            configuration=Configuration(
                host="0.0.0.0:8000",
                username="api",
                password="password",
                verify_ssl=False,
            )
        )

        test_value = 12312
        updates = {
            "container_network": "192.169.16.0/28",
            "subnet": "10.0.2.0/24",
            "test_key": test_value,
        }

        api_client.update_state(updates)
        assert api_client.query_state("test_key") == test_value

    def test_host_uri_property(self):
        api_client = VNS3Client(
            configuration=Configuration(
                host="0.0.0.0:8000",
                username="api",
                password="password",
                verify_ssl=False,
            )
        )
        assert api_client.host_uri == "0.0.0.0"
