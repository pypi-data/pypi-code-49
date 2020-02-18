# -*- coding: utf-8 -*-
"""Tests for downloader.py"""
from threedi_scenario_downloader import downloader
import configparser
import pytest
from requests.exceptions import HTTPError


def test_set_headers():
    config = configparser.ConfigParser()
    config.read("threedi_scenario_downloader/tests/testdata/realconfig.ini")
    downloader.set_headers(
        config["credentials"]["username"], config["credentials"]["password"]
    )


def test_get_headers():
    headers = downloader.get_headers()
    config = configparser.ConfigParser()
    config.read("threedi_scenario_downloader/tests/testdata/realconfig.ini")

    assert headers["username"] == config["credentials"]["username"]
    assert headers["password"] == config["credentials"]["password"]


def test_find_scenario():
    r1 = downloader.find_scenarios(name__icontains="exel_firs")
    # r2 = downloader.find_scenarios(
    #    name__icontains="API cursus 28 aug", model_revision=19
    # )
    # r3 = downloader.find_scenarios(
    #    name__icontains="API cursus 28 aug", model_revision=9
    # )

    assert (
        r1[0]["uuid"]
        == "97458c61-dbcd-41fd-a6f6-1a4e10418e00"
        # and r2[0]["uuid"] == "06c38953-31ec-4f6d-ae1f-ccdf31a348ae"
        # and len(r3) == 0
    )


def test_find_scenario_by_model_slug():
    r = downloader.find_scenarios_by_model_slug(
        "71407b2988ea075022d2095c2c942c0f5a7bac6e"
    )
    assert r[0]["uuid"] == "97458c61-dbcd-41fd-a6f6-1a4e10418e00"


def test_find_scenario_by_name():
    r = downloader.find_scenarios_by_name("exel_firs")
    assert r[0]["uuid"] == "97458c61-dbcd-41fd-a6f6-1a4e10418e00"


def test_get_netcdf_link():
    url = downloader.get_netcdf_link("97458c61-dbcd-41fd-a6f6-1a4e10418e00")
    assert url == "https://demo.lizard.net/api/v3/scenario-results/50681/results_3di.nc"


def test_get_raster():
    raster = downloader.get_raster(
        "97458c61-dbcd-41fd-a6f6-1a4e10418e00", "depth-max-dtri"
    )
    assert raster["uuid"] == "df512f0f-ccb1-4ee1-af68-0d2fdd8c6144"


def test_get_raster_temporal():
    raster = downloader.get_raster("97458c61-dbcd-41fd-a6f6-1a4e10418e00", "depth-dtri")
    assert raster["uuid"] == "9373c291-17e4-4ada-aed9-3d0beab8362e"


def test_get_raster_from_non_existing_scenario():
    with pytest.raises(HTTPError):
        raster = downloader.get_raster(
            "97458c61-dbcd-41fd-a6f6-1a4e10418e01", "depth-max-dtri"
        )
        assert raster is not None


def test_create_raster_task():
    task = downloader.create_raster_task(
        downloader.get_raster("97458c61-dbcd-41fd-a6f6-1a4e10418e00", "depth-max-dtri"),
        "EPSG:28992",
        "1000",
    )
    assert task is not None
