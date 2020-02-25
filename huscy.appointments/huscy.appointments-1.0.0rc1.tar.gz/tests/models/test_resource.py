from huscy.appointments.models import Resource


def test_str_method():
    resource = Resource(name='resource name')

    assert str(resource) == 'resource name'
