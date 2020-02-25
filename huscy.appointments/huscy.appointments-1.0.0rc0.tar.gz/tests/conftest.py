from datetime import datetime, timedelta

import pytest

from rest_framework.test import APIClient

from huscy.appointments.models import Appointment, Resource, Token


@pytest.fixture
def user(django_user_model):
    return django_user_model.objects.create_user(username='user', password='password',
                                                 first_name='Lars', last_name='Krismes')


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
def resource():
    return Resource.objects.create(name='C222')


@pytest.fixture
def resource_second():
    return Resource.objects.create(name='C223')


@pytest.fixture
def appointment(user, resource):
    return Appointment.objects.create(
        owner=user,
        resource=resource.name,
        start=datetime.now(),
        end=datetime.now() + timedelta(hours=3))


@pytest.fixture
def appointment_second(user, resource_second):
    return Appointment.objects.create(
        owner=user,
        resource=resource_second.name,
        start=datetime.now() + timedelta(hours=4),
        end=datetime.now() + timedelta(hours=7))


@pytest.fixture
def user_feed_token(user):
    return Token.objects.create(user=user)
