import pytest

from rest_framework.reverse import reverse
from rest_framework.status import HTTP_201_CREATED, HTTP_403_FORBIDDEN

from django.contrib.auth.models import Permission

from huscy.rooms.models import Building


@pytest.mark.django_db
def test_admin_user_can_create_buildings(admin_client):
    response = create_building(admin_client)

    assert response.status_code == HTTP_201_CREATED
    assert Building.objects.filter(name='house_a').count() == 1


@pytest.mark.django_db
def test_user_with_permission_can_create_buildings(client, user):
    create_permission = Permission.objects.get(codename='add_building')
    user.user_permissions.add(create_permission)

    response = create_building(client)

    assert response.status_code == HTTP_201_CREATED
    assert Building.objects.filter(name='house_a').count() == 1


@pytest.mark.django_db
def test_user_without_permission_cannot_create_buildings(client):
    response = create_building(client)

    assert response.status_code == HTTP_403_FORBIDDEN
    assert not Building.objects.filter(name='house_a').exists()


@pytest.mark.django_db
def test_anonymous_user_cannot_create_buildings(anonymous_client):
    response = create_building(anonymous_client)

    assert response.status_code == HTTP_403_FORBIDDEN
    assert not Building.objects.filter(name='house_a').exists()


def create_building(client):
    return client.post(
        reverse('building-list'),
        data=dict(name='house_a')
    )
