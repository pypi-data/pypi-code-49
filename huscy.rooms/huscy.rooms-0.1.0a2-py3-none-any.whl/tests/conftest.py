import pytest

from model_bakery import baker

from rest_framework.test import APIClient


@pytest.fixture
def user(django_user_model):
    return django_user_model.objects.create_user(username='user', password='password',
                                                 first_name='Lars', last_name='Agne')


@pytest.fixture
def admin_client(admin_user):
    client = APIClient()
    client.login(username=admin_user.username, password='password')
    return client


@pytest.fixture
def client(user):
    client = APIClient()
    client.login(username=user.username, password='password')
    return client


@pytest.fixture
def anonymous_client():
    return APIClient()


@pytest.fixture
def building():
    return baker.make('rooms.Building')


@pytest.fixture
def floor(building):
    return baker.make('rooms.Floor', building=building)


@pytest.fixture
def room(floor):
    return baker.make('rooms.Room', floor=floor)
