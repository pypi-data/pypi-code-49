import pytest

from fares import SubscriptionOffering, is_subscription_offering_applicable_for_clusters
from fares.dimension import ClusterDimensions


@pytest.fixture
def subscription_offering():
    return {
        "id": "first_sub",
        "name": "Morning sub",
        "rides": "10",
        "currency": "INR",
        "validity_in_days": "20",
        "is_carry_forward": "True",
        "activation_date": "2019-02-28T12:56:41.589953+00:00",
        "deactivation_date": "2019-02-28T12:56:41.589953+00:00",
        "zone_id": "zone1",
        "amount": "1000",
        "subscription_type": "STANDARD",
        "applicability": {
            "type": "INTER_CLUSTER",
            "rules": [
                {
                    "origin_cluster_id": "cluster_1",
                    "destination_cluster_id": "cluster_2",
                    "session": "MORNING",
                }
            ],
        },
        "created_at": "2019-02-28T12:56:41.589953+00:00",
    }


@pytest.fixture
def subscription_offering_zone_applicability():
    return {
        "id": "first_sub",
        "name": "Morning sub",
        "rides": "10",
        "currency": "INR",
        "validity_in_days": "20",
        "is_carry_forward": "True",
        "activation_date": "2019-02-28T12:56:41.589953+00:00",
        "deactivation_date": "2019-02-28T12:56:41.589953+00:00",
        "zone_id": "zone-1",
        "amount": "1000",
        "subscription_type": "TRIAL",
        "applicability": {"type": "ZONE_WIDE", "rules": [{"zone_id": "zone_1"}]},
        "created_at": "2019-02-28T12:56:41.589953+00:00",
    }


@pytest.fixture
def valid_clusters():
    return {
        ClusterDimensions.ORIGIN_CLUSTER_ID: "cluster_1",
        ClusterDimensions.DESTINATION_CLUSTER_ID: "cluster_2",
        ClusterDimensions.ZONE_ID: "zone_1",
    }


@pytest.fixture
def valid_reverse_clusters():
    return {
        ClusterDimensions.ORIGIN_CLUSTER_ID: "cluster_2",
        ClusterDimensions.DESTINATION_CLUSTER_ID: "cluster_1",
        ClusterDimensions.ZONE_ID: "zone_1",
    }


@pytest.fixture
def invalid_clusters():
    return {
        ClusterDimensions.ORIGIN_CLUSTER_ID: "cluster_1",
        ClusterDimensions.DESTINATION_CLUSTER_ID: "cluster_3",
        ClusterDimensions.ZONE_ID: "zone_1",
    }


@pytest.fixture
def invalid_zone_clusters():
    return {
        ClusterDimensions.ORIGIN_CLUSTER_ID: "cluster_1",
        ClusterDimensions.DESTINATION_CLUSTER_ID: "cluster_3",
        ClusterDimensions.ZONE_ID: "zone_2",
    }


def test_cluster_are_applicable(subscription_offering, valid_clusters):
    assert is_subscription_offering_applicable_for_clusters(
        SubscriptionOffering.from_json(subscription_offering), valid_clusters
    )


def test_reverse_clusters_are_applicable(subscription_offering, valid_reverse_clusters):
    assert is_subscription_offering_applicable_for_clusters(
        SubscriptionOffering.from_json(subscription_offering), valid_reverse_clusters
    )


def test_invalid_clusters_are_not_applicable(subscription_offering, invalid_clusters):
    assert not is_subscription_offering_applicable_for_clusters(
        SubscriptionOffering.from_json(subscription_offering), invalid_clusters
    )


def test_zone_applicability(subscription_offering_zone_applicability, valid_clusters):
    assert is_subscription_offering_applicable_for_clusters(
        SubscriptionOffering.from_json(subscription_offering_zone_applicability),
        valid_clusters,
    )


def test_zone_applicability_fails(
    subscription_offering_zone_applicability, invalid_zone_clusters
):
    assert not is_subscription_offering_applicable_for_clusters(
        SubscriptionOffering.from_json(subscription_offering_zone_applicability),
        invalid_zone_clusters,
    )
