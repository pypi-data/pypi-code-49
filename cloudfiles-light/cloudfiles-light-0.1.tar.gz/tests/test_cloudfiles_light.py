import datetime
from cloudfiles_light import CloudFilesSession


def add_identity_response(responses, expires):
    identity_response = {
        "access": {
            "serviceCatalog": [
                {
                    "endpoints": [
                        {"region": "my_region", "publicURL": "http://example.com"},
                        {"region": "other-region", "publicURL": ""},
                    ],
                    "type": "object-store",
                },
                {"type": "other", "endpoints": []},
            ],
            "token": {"id": "returned_tokenid", "expires": expires},
        }
    }
    responses.add(
        responses.POST,
        "https://identity.api.rackspacecloud.com/v2.0/tokens",
        json=identity_response,
        status=200,
    )


def test_basic(responses):
    add_identity_response(responses, "2018-01-01T00:00:00.0Z")

    session = CloudFilesSession(
        username="my_username", apikey="my_apikey", region="my_region"
    )

    assert session

    responses.add(
        responses.GET, "http://example.com/foo", json={"some": "data"}, status=200
    )
    response = session.get("foo")
    assert response.json() == {"some": "data"}

    token_call, object_call = responses.calls
    assert "identity.api.rackspacecloud.com" in token_call.request.url
    assert object_call.request.headers["X-Auth-Token"] == "returned_tokenid"


def test_refresh_required(responses):
    # expiry is in the past; keeps refreshing
    add_identity_response(responses, "2018-01-01T00:00:00.0Z")
    session = CloudFilesSession(
        username="my_username", apikey="my_apikey", region="my_region"
    )
    responses.add(
        responses.GET, "http://example.com/foo", json={"some": "data"}, status=200
    )
    for _ in range(5):
        session.get("foo")
    assert len(responses.calls) == 10


def test_refresh_not_required(responses):
    # expiry is in the future; no need to refresh token
    year = datetime.datetime.now().year
    add_identity_response(responses, f"{year + 1}-01-01T00:00:00.0Z")
    session = CloudFilesSession(
        username="my_username", apikey="my_apikey", region="my_region"
    )
    responses.add(
        responses.GET, "http://example.com/foo", json={"some": "data"}, status=200
    )
    for _ in range(5):
        session.get("foo")
    assert len(responses.calls) == 6
