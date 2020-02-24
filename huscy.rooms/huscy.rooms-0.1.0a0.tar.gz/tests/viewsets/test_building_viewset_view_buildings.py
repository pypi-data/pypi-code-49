import pytest

from rest_framework.reverse import reverse
from rest_framework.status import HTTP_200_OK, HTTP_403_FORBIDDEN


@pytest.mark.django_db
def test_admin_user_can_retrieve_buildings(admin_client, building):
    response = retrieve_building(admin_client, building)

    assert response.status_code == HTTP_200_OK


@pytest.mark.django_db
def test_admin_user_can_list_buildings(admin_client):
    response = list_buildings(admin_client)

    assert response.status_code == HTTP_200_OK


@pytest.mark.django_db
def test_user_without_permission_can_retrieve_buildings(client, building):
    response = retrieve_building(client, building)

    assert response.status_code == HTTP_200_OK


@pytest.mark.django_db
def test_user_without_permission_can_list_buildings(client, building):
    response = list_buildings(client)

    assert response.status_code == HTTP_200_OK


@pytest.mark.django_db
def test_anonymous_user_cannot_retrieve_buildings(anonymous_client, building):
    response = retrieve_building(anonymous_client, building)

    assert response.status_code == HTTP_403_FORBIDDEN


@pytest.mark.django_db
def test_anonymous_user_cannot_list_buildings(anonymous_client, building):
    response = list_buildings(anonymous_client)

    assert response.status_code == HTTP_403_FORBIDDEN


def retrieve_building(client, building):
    return client.get(reverse('building-detail', kwargs=dict(pk=building.id)))


def list_buildings(client):
    return client.get(reverse('building-list'))
