import pytest

from rest_framework import status
from rest_framework.reverse import reverse


@pytest.mark.django_db
def test_user_gets_feed(client, user, appointment, user_feed_token):
    response = client.get(reverse('feed', kwargs=dict(token=user_feed_token.key)))

    assert status.HTTP_200_OK == response.status_code

    # check if the appointment's start time is conainted in response
    start_string = 'DTSTART;VALUE=DATE-TIME:' + appointment.start.strftime("%Y%m%dT%H%M%S")
    end_string = 'DTEND;VALUE=DATE-TIME:' + appointment.end.strftime("%Y%m%dT%H%M%S")
    assert start_string in response.content.decode()
    assert end_string in response.content.decode()


@pytest.mark.django_db
def test_user_retrieves_existing_feedurl(client, user, user_feed_token):
    response = client.get(reverse('feed-url'))

    assert status.HTTP_200_OK == response.status_code

    json_response = response.json()
    assert json_response['feed'] == '/feed/' + user_feed_token.key


@pytest.mark.django_db
def test_user_retrieves_created_onthefly_feedurl(client, user):
    response = client.get(reverse('feed-url'))
    assert status.HTTP_200_OK == response.status_code

    token = response.json()['feed'].split('/')[-1]
    response2 = client.get(reverse('feed', kwargs=dict(token=token)))

    assert status.HTTP_200_OK == response2.status_code
    assert 'BEGIN:VCALENDAR' in response2.content.decode()


@pytest.mark.django_db
def test_anonymous_cannot_get_feed_url(anonymous_client):
    response = anonymous_client.get(reverse('feed-url'))

    assert status.HTTP_403_FORBIDDEN == response.status_code


@pytest.mark.django_db
def test_anonymous_can_get_feed_for_user(anonymous_client, user_feed_token, appointment):
    response = anonymous_client.get(reverse('feed', kwargs=dict(token=user_feed_token.key)))

    assert status.HTTP_200_OK == response.status_code

    # check if the appointment's start time is conainted in response
    start_string = 'DTSTART;VALUE=DATE-TIME:' + appointment.start.strftime("%Y%m%dT%H%M%S")
    assert start_string in response.content.decode()


@pytest.mark.django_db
def test_user_cannot_retrieve_feed_for_invalid_token(client, user, user_feed_token):
    # swap the last two chars
    invalid_token = user_feed_token.key[:-2] + user_feed_token.key[-1:] + user_feed_token.key[-2:-1]

    response = client.get(reverse('feed', kwargs=dict(token=invalid_token)))

    assert status.HTTP_200_OK == response.status_code
    # but ical is empty then:
    assert response.content.decode() == ('BEGIN:VCALENDAR\r\nVERSION:2.0\r\nCALSCALE:GREGORIAN\r\n'
                                         'METHOD:PUBLISH\r\nX-WR-TIMEZONE:UTC\r\nEND:VCALENDAR\r\n')


@pytest.mark.django_db
def test_all_appointments_are_in_feed(client, user, appointment, appointment_second, user_feed_token):
    response = client.get(reverse('feed', kwargs=dict(token=user_feed_token.key)))

    assert status.HTTP_200_OK == response.status_code

    # check if the appointment's start time is conainted in response
    start1_string = 'DTSTART;VALUE=DATE-TIME:' + appointment.start.strftime("%Y%m%dT%H%M%S")
    assert start1_string in response.content.decode()
    start2_string = 'DTSTART;VALUE=DATE-TIME:' + appointment_second.start.strftime("%Y%m%dT%H%M%S")
    assert start2_string in response.content.decode()


@pytest.mark.django_db
def test_post_method_for_feed_url_not_allowed(client, user):
    response = client.post(reverse('feed-url'))

    assert status.HTTP_405_METHOD_NOT_ALLOWED == response.status_code
