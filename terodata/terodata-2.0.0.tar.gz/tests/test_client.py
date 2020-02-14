# pylint: disable=C0111 # (no docstrings)
# pylint: disable=C0413 # (allow importing local modules below sys path config)

import sys
import shutil
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
from terodata import TeroDataClient


def test_get_datasets():
    cli = TeroDataClient(username="test")
    results = cli.get_datasets()
    assert "sentinel1" in results["datasets"]


# ====================================
# Dataset metadata
# ====================================
def test_get_dataset():
    cli = TeroDataClient(username="test")
    results = cli.get_dataset("sentinel1")
    assert results["id"] == "sentinel1"


def test_get_dataset_not_found():
    cli = TeroDataClient(username="test")
    with pytest.raises(Exception) as err:
        cli.get_dataset("INVALID_DATASET")
    assert "DATASET_NOT_FOUND" in str(err.value)


# ====================================
# Queries
# ====================================
def test_create_query_job():
    cli = TeroDataClient(username="test")
    attrs = {
        "mission": "jason3",
        "productType": "IGDR-SSHA",
        "tStart": "2016-05-01",
        "tEnd": "2016-05-10",
        "aoi": "POLYGON((2 41,3 41,3 42,2 42,2 41))",
    }
    results = cli.create_query_job("jason23", attrs)
    assert results["id"]
    assert results["attrs"]
    assert results["status"]


def test_create_query_job_dataset_not_found():
    cli = TeroDataClient(username="test")
    attrs = {
        "mission": "jason3",
        "productType": "IGDR-SSHA",
        "tStart": "2016-05-01",
        "tEnd": "2016-05-10",
        "aoi": "POLYGON((2 41,3 41,3 42,2 42,2 41))",
    }
    with pytest.raises(Exception) as err:
        cli.create_query_job("INVALID_DATASET", attrs)
    assert "DATASET_NOT_FOUND" in str(err.value)


def test_create_query_job_invalid_query_product_type():
    cli = TeroDataClient(username="test")
    attrs = {
        "mission": "jason3",
        "productType": "INVALID_PRODUCT_TYPE",
    }
    with pytest.raises(Exception) as err:
        cli.create_query_job("jason23", attrs)
    assert "INVALID_QUERY" in str(err.value)


def test_create_query_job_invalid_query_date():
    cli = TeroDataClient(username="test")
    attrs = {
        "mission": "jason3",
        "tStart": "INVALID_DATE",
    }
    with pytest.raises(Exception) as err:
        cli.create_query_job("jason23", attrs)
    assert "INVALID_QUERY" in str(err.value)


def test_create_query_job_invalid_query_date_range():
    cli = TeroDataClient(username="test")
    attrs = {"mission": "jason3", "tStart": "2018-10-05", "tEnd": "2018-10-01"}
    with pytest.raises(Exception) as err:
        cli.create_query_job("jason23", attrs)
    assert "INVALID_QUERY" in str(err.value)


# Launch a huge query job, then cancel it
def test_create_get_cancel_query_job():
    cli = TeroDataClient(username="test")
    attrs = {"aoi": "POINT(2 41)"}
    results = cli.create_query_job("sentinel1", attrs)
    assert results["status"] == "RUNNING"
    id = results["id"]
    results = cli.get_query_job("sentinel1", id)
    assert results["status"] == "RUNNING"
    results = cli.cancel_query_job("sentinel1", id)
    assert results is None
    results = cli.get_query_job("sentinel1", id)
    assert results["status"] == "CANCELED"


def test_query():
    cli = TeroDataClient(username="test", log=False)
    attrs = {
        "mission": "jason2",
        "productType": "IGDR-SSHA",
        "tStart": "2016-05-01",
        "tEnd": "2016-05-10",
        "aoi": "POLYGON((2 41,3 41,3 42,2 42,2 41))",
    }
    results = cli.query("jason23", attrs)
    assert results["id"]
    assert results["status"] == "FINISHED"
    assert results["progress"] == 100


# ====================================
# Downloads
# ====================================
def test_create_download_job():
    results = None
    try:
        cli = TeroDataClient(username="test")
        granule_ids = ["JA3_IPR_2PdP070_020_20180102_083513_20180102_093126.nc"]
        results = cli.create_download_job(
            "jason23", granule_ids, output_path="testSession"
        )
        assert results["id"]
        assert results["maxSize"]
        assert results["status"]
    finally:
        if results:
            cli.cancel_download_job("jason23", results["id"])
            if "granulePaths" in results:
                granule_paths = results["granulePaths"].values()
                if len(granule_paths) > 0:
                    shutil.rmtree(os.path.dirname(granule_paths[0]))


def test_create_download_job_too_large():
    results = None
    try:
        cli = TeroDataClient(username="test")
        granule_ids = ["JA3_IPR_2PdP070_020_20180102_083513_20180102_093126.nc"]
        with pytest.raises(Exception) as err:
            results = cli.create_download_job(
                "jason23", granule_ids, output_path="testSession", max_size=0.1
            )
        assert "JOB_TOO_LARGE" in str(err.value)
    finally:
        if results:
            cli.cancel_download_job("jason23", results["id"])
            if "granulePaths" in results:
                granule_paths = results["granulePaths"].values()
                if len(granule_paths) > 0:
                    shutil.rmtree(os.path.dirname(granule_paths[0]))


# Launch a large download job, then cancel it
def test_create_get_cancel_download_job():
    results = None
    try:
        cli = TeroDataClient(username="test")
        granule_ids = [
            "eyJncmFudWxlTmFtZSI6IlMxQl9JV19HUkRIXzFTRFZfMjAxODA5MDRUMDYwMDQ0XzIwMTgwOTA0VDA2MDEwOV8wMTI1NjFfMDE3MkNGXzcyNDciLCJwcm9jZXNzaW5nTGV2ZWwiOiJHUkRfSEQiLCJkb3dubG9hZFVybCI6Imh0dHBzOi8vZGF0YXBvb2wuYXNmLmFsYXNrYS5lZHUvR1JEX0hEL1NCL1MxQl9JV19HUkRIXzFTRFZfMjAxODA5MDRUMDYwMDQ0XzIwMTgwOTA0VDA2MDEwOV8wMTI1NjFfMDE3MkNGXzcyNDcuemlwIn0="
        ]
        results = cli.create_download_job(
            "sentinel1-asf", granule_ids, output_path="testSession"
        )
        assert results["status"] == "RUNNING"
        id = results["id"]
        results = cli.get_download_job("sentinel1-asf", id)
        assert results["status"] == "RUNNING"
        results = cli.cancel_download_job("sentinel1-asf", id)
        assert results is None
        results = cli.get_download_job("sentinel1-asf", id)
        assert results["status"] == "CANCELED"
    finally:
        if results:
            cli.cancel_download_job("sentinel1-asf", results["id"])
            if "granulePaths" in results:
                granule_paths = results["granulePaths"].values()
                if len(granule_paths) > 0:
                    shutil.rmtree(os.path.dirname(granule_paths[0]))


def test_download():
    def on_progress(id, status, progress):
        print("on_progress called!")
        if status == "RUNNING":
            cli.cancel_download_job("sentinel1-asf", id)

    results = None
    try:
        cli = TeroDataClient(username="test")
        granule_ids = [
            "eyJncmFudWxlTmFtZSI6IlMxQl9JV19HUkRIXzFTRFZfMjAxODA5MDRUMDYwMDQ0XzIwMTgwOTA0VDA2MDEwOV8wMTI1NjFfMDE3MkNGXzcyNDciLCJwcm9jZXNzaW5nTGV2ZWwiOiJHUkRfSEQiLCJkb3dubG9hZFVybCI6Imh0dHBzOi8vZGF0YXBvb2wuYXNmLmFsYXNrYS5lZHUvR1JEX0hEL1NCL1MxQl9JV19HUkRIXzFTRFZfMjAxODA5MDRUMDYwMDQ0XzIwMTgwOTA0VDA2MDEwOV8wMTI1NjFfMDE3MkNGXzcyNDcuemlwIn0="
        ]
        with pytest.raises(Exception) as err:
            results = cli.download(
                "sentinel1-asf",
                granule_ids,
                output_path="testSession",
                on_progress=on_progress,
            )
        assert "JOB_CANCELED" in str(err.value)
    finally:
        if results:
            cli.cancel_download_job("sentinel1-asf", results["id"])
            if "granulePaths" in results:
                granule_paths = results["granulePaths"].values()
                if len(granule_paths) > 0:
                    shutil.rmtree(os.path.dirname(granule_paths[0]))
