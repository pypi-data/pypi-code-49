import pytest

from rest_framework.reverse import reverse
from rest_framework.status import HTTP_200_OK, HTTP_403_FORBIDDEN


@pytest.mark.django_db
def test_admin_user_can_retrieve_floors(admin_client, floor):
    response = retrieve_floor(admin_client, floor)

    assert response.status_code == HTTP_200_OK


@pytest.mark.django_db
def test_admin_user_can_list_floors(admin_client):
    response = list_floors(admin_client)

    assert response.status_code == HTTP_200_OK


@pytest.mark.django_db
def test_user_without_permission_can_retrieve_floors(client, floor):
    response = retrieve_floor(client, floor)

    assert response.status_code == HTTP_200_OK


@pytest.mark.django_db
def test_user_without_permission_can_list_floors(client):
    response = list_floors(client)

    assert response.status_code == HTTP_200_OK


@pytest.mark.django_db
def test_anonymous_user_cannot_retrieve_floors(anonymous_client, floor):
    response = retrieve_floor(anonymous_client, floor)

    assert response.status_code == HTTP_403_FORBIDDEN


@pytest.mark.django_db
def test_anonymous_user_cannot_list_floors(anonymous_client):
    response = list_floors(anonymous_client)

    assert response.status_code == HTTP_403_FORBIDDEN


def retrieve_floor(client, floor):
    return client.get(reverse('floor-detail', kwargs=dict(pk=floor.id)))


def list_floors(client):
    return client.get(reverse('floor-list'))
