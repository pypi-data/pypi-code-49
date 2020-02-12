#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from requests.exceptions import ConnectionError
from chime_frb_api import distributor
from chime_frb_api import frb_master
from chime_frb_api import core

bad_distributor = distributor.Distributor(base_url="http://localhost:8888")
bad_frb_master = frb_master.FRBMaster(base_url="http://localhost:8888")


def test_get_exception():
    with pytest.raises(ConnectionError):
        bad_distributor.get_status()


def test_post_exception():
    with pytest.raises(ConnectionError):
        bad_distributor.create_distributor(distributor_name="bad_distributor")


def test_delete_exception():
    with pytest.raises(ConnectionError):
        bad_distributor.delete_distributor(distributor_name="bad_distributor")


def test_put_exception():
    with pytest.raises(ConnectionError):
        parameters = {
            "pipeline": {
                "name": "test",
                "status": "test",
                "log": "test",
                "version": "test",
            },
            "beam_number": 1,
        }
        bad_frb_master.events.add_measured_parameters(
            event_number=1, measured_parameters=parameters
        )


def test_bad_initialization():
    with pytest.raises(Exception):
        core.API()


def test_authorization_with_userpass():
    master = core.API(base_url="http://localhost:8001")
    auth = master.authorize(username="debug", password="debug")
    assert auth == True
    reauth = master.reauthorize()
    assert reauth == True


def test_authorize_with_token():
    master = core.API(base_url="http://localhost:8001")
    response = master._session.post(
        url=master.base_url + "/auth", json={"username": "debug", "password": "debug"}
    )
    tokens = response.json()
    access_token = tokens.get("access_token", None)
    refresh_token = tokens.get("refresh_token", None)
    auth = master.authorize(access_token=access_token, refresh_token=refresh_token)
    assert auth == True


def test_auth_with_bad_values():
    master = core.API(base_url="http://localhost:8001")
    with pytest.raises(Exception):
        master.authorize(
            access_token="bad_access_token",
            refresh_token="bad_refresh_token",
            username="bad",
            password="also_bad",
        )


def test_reauth_with_bad_tokens():
    master = core.API(base_url="http://localhost:8001")
    with pytest.raises(Exception):
        master.reauthorize(
            access_token="bad_access_token", refresh_token="bad_refresh_token"
        )


def test_reauth_without_tokens():
    master = core.API(base_url="http://localhost:8001")
    with pytest.raises(Exception):
        master.reauthorize()
