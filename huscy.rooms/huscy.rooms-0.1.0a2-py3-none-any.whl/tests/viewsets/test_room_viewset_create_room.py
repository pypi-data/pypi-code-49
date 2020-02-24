import pytest

from rest_framework.reverse import reverse
from rest_framework.status import HTTP_201_CREATED, HTTP_403_FORBIDDEN

from django.contrib.auth.models import Permission

from huscy.rooms.models import Room


@pytest.mark.django_db
def test_admin_user_can_create_rooms(admin_client, floor):
    response = create_room(admin_client, floor)

    assert response.status_code == HTTP_201_CREATED
    assert Room.objects.filter(name='conference_room_1').count() == 1


@pytest.mark.django_db
def test_user_with_permission_can_create_rooms(client, user, floor):
    create_permission = Permission.objects.get(codename='add_room')
    user.user_permissions.add(create_permission)

    response = create_room(client, floor)

    assert response.status_code == HTTP_201_CREATED
    assert Room.objects.filter(name='conference_room_1').count() == 1


@pytest.mark.django_db
def test_user_without_permission_cannot_create_rooms(client, floor):
    response = create_room(client, floor)

    assert response.status_code == HTTP_403_FORBIDDEN
    assert not Room.objects.filter(name='conference_room_1').exists()


@pytest.mark.django_db
def test_anonymous_user_cannot_create_rooms(anonymous_client, floor):
    response = create_room(anonymous_client, floor)

    assert response.status_code == HTTP_403_FORBIDDEN
    assert not Room.objects.filter(name='conference_room_1').exists()


def create_room(client, floor):
    return client.post(
        reverse('room-list'),
        data=dict(name='conference_room_1', floor=floor.pk)
    )
