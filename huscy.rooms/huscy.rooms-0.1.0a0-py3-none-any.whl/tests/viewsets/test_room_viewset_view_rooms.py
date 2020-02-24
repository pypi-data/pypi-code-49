import pytest

from rest_framework.reverse import reverse
from rest_framework.status import HTTP_200_OK, HTTP_403_FORBIDDEN


@pytest.mark.django_db
def test_admin_user_can_retrieve_rooms(admin_client, room):
    response = retrieve_room(admin_client, room)

    assert response.status_code == HTTP_200_OK


@pytest.mark.django_db
def test_admin_user_can_list_rooms(admin_client):
    response = list_rooms(admin_client)

    assert response.status_code == HTTP_200_OK


@pytest.mark.django_db
def test_user_without_permission_can_retrieve_rooms(client, room):
    response = retrieve_room(client, room)

    assert response.status_code == HTTP_200_OK


@pytest.mark.django_db
def test_user_without_permission_can_list_rooms(client):
    response = list_rooms(client)

    assert response.status_code == HTTP_200_OK


@pytest.mark.django_db
def test_anonymous_user_cannot_retrieve_rooms(anonymous_client, room):
    response = retrieve_room(anonymous_client, room)

    assert response.status_code == HTTP_403_FORBIDDEN


@pytest.mark.django_db
def test_anonymous_user_cannot_list_rooms(anonymous_client):
    response = list_rooms(anonymous_client)

    assert response.status_code == HTTP_403_FORBIDDEN


def retrieve_room(client, room):
    return client.get(reverse('room-detail', kwargs=dict(pk=room.id)))


def list_rooms(client):
    return client.get(reverse('room-list'))
