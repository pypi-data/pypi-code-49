from rest_framework import status
from rest_framework.reverse import reverse


def test_admin_user_can_get_resources(admin_client):
    response = admin_client.get(reverse('resource-list'))

    assert status.HTTP_200_OK == response.status_code


def test_user_without_permission_can_get_resources(client):
    response = client.get(reverse('resource-list'))

    assert status.HTTP_200_OK == response.status_code


def test_anonymous_user_cannot_get_resources(anonymous_client):
    response = anonymous_client.get(reverse('resource-list'))

    assert status.HTTP_403_FORBIDDEN == response.status_code
