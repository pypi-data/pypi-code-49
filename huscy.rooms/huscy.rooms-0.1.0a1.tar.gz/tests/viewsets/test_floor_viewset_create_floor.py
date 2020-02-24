import pytest

from rest_framework.reverse import reverse
from rest_framework.status import HTTP_201_CREATED, HTTP_403_FORBIDDEN

from django.contrib.auth.models import Permission

from huscy.rooms.models import Floor


@pytest.mark.django_db
def test_admin_user_can_create_floors(admin_client, building):
    response = create_floor(admin_client, building)

    assert response.status_code == HTTP_201_CREATED
    assert Floor.objects.filter(level=1).count() == 1


@pytest.mark.django_db
def test_user_with_permission_can_create_floors(client, user, building):
    create_permission = Permission.objects.get(codename='add_floor')
    user.user_permissions.add(create_permission)

    response = create_floor(client, building)

    assert response.status_code == HTTP_201_CREATED
    assert Floor.objects.filter(level=1).count() == 1


@pytest.mark.django_db
def test_user_without_permission_cannot_create_floors(client, building):
    response = create_floor(client, building)

    assert response.status_code == HTTP_403_FORBIDDEN
    assert not Floor.objects.filter(level=1).exists()


@pytest.mark.django_db
def test_anonymous_user_cannot_create_floors(anonymous_client, building):
    response = create_floor(anonymous_client, building)

    assert response.status_code == HTTP_403_FORBIDDEN
    assert not Floor.objects.filter(level=1).exists()


def create_floor(client, building):
    return client.post(reverse('floor-list'), data=dict(level=1, building=building.pk))
