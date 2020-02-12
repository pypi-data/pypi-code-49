"""Test Session functionality with Batfish service backend."""
from os import walk
from os.path import abspath, dirname, join, realpath

import pytest
from requests import HTTPError
import tempfile

from pybatfish.util import zip_dir
from pybfe.client.session import Session
from tests.common_util import requires_bfe

_this_dir = abspath(dirname(realpath(__file__)))

CURRENT_SNAPSHOT = "current_snapshot"
PREVIOUS_SNAPSHOT = "previous_snapshot"
SNAPSHOT_DIR = join(_this_dir, "snapshots", "basic")


@pytest.fixture(scope="module")
def session():
    s = Session()
    # Snapshot which can be referenced by name
    other_name = s.init_snapshot(
        join(_this_dir, "snapshots", "basic2"), PREVIOUS_SNAPSHOT
    )
    # Current snapshot
    name = s.init_snapshot(join(_this_dir, "snapshots", "basic"), CURRENT_SNAPSHOT)
    yield s
    s.delete_snapshot(name)
    s.delete_snapshot(other_name)


@requires_bfe("2019.09.01")
def test_network_object(session):
    """Confirm network object up/download works as expected."""
    key = "key"
    data = "data"

    # No error putting the object
    session.put_network_object(key, data)

    # Reading the object back should result in the data we put there
    assert session.get_network_object_text(key) == data

    session.delete_network_object(key)
    # Should get 404 when trying to get an object after it was deleted
    with pytest.raises(HTTPError) as e:
        session.get_network_object_text(key)
        assert e.response.status_code == 404


def test_snapshot_object(session):
    """Confirm snapshot object up/download works as expected."""
    key = "key"
    data = "data"

    # No error putting the object
    session.put_snapshot_object(key, data, snapshot=session.snapshot)

    # Reading the object back should result in the data we put there
    assert session.get_snapshot_object_text(key, snapshot=session.snapshot) == data


def test_snapshot_input_object(session):
    """Confirm snapshot input-object download works as expected."""
    key = join("configs", "basic.cfg")
    # Get the config content from disk
    with open(join(SNAPSHOT_DIR, key), "r") as f:
        data = f.read()

    # Reading a config input-object from backend should match original config
    assert (
        session.get_snapshot_input_object_text(key, snapshot=session.snapshot) == data
    )


@requires_bfe("2019.12.06")
def test_snapshot_input(session):
    """Confirm snapshot input download works as expected."""
    # Get the bytes for the original input
    tmp_input_zip_dir = tempfile.TemporaryDirectory()
    tmp_input_zip_file = join(tmp_input_zip_dir.name, "tmp.zip")
    zip_dir(SNAPSHOT_DIR, tmp_input_zip_file)
    with open(tmp_input_zip_file, "rb") as f:
        input_data = f.read()

    # get the input now
    tmp_output_zip_dir = tempfile.TemporaryDirectory()
    tmp_output_zip_file = join(tmp_output_zip_dir.name, "tmp.zip")
    session.get_snapshot_input(tmp_output_zip_file, snapshot=session.snapshot)
    with open(tmp_input_zip_file, "rb") as f:
        output_data = f.read()

    assert input_data == output_data

    # supplying the same file name without overwrite should fail
    with pytest.raises(ValueError) as e:
        session.get_snapshot_input(tmp_output_zip_file, snapshot=session.snapshot)
        assert "already exists" in e.value

    # the request should succeed with overwrite
    session.get_snapshot_input(
        tmp_output_zip_file, snapshot=session.snapshot, overwrite=True
    )
    with open(tmp_input_zip_file, "rb") as f:
        output_data2 = f.read()

    assert input_data == output_data2


def test_validate_facts(session):
    """Confirm fact validation returns the expected dictionary of mismatched facts."""
    validation_results = session.validate_facts(
        expected_facts=join(_this_dir, "facts", "basic_fail")
    )

    assert validation_results == {
        "basic": {
            "Syslog.Logging_Servers": {"actual": [], "expected": ["1.2.3.5"]},
            "Extra_Key": {"expected": "something", "key_present": False},
        }
    }, "Logging_Servers should be different and Extra_Key should be missing"


@requires_bfe("2019.09.01")
def test_validate_facts_specific_snapshot(session):
    """Confirm fact validation works when a snapshot is specified."""
    # Non-current snapshot should match facts in facts/basic2/ but not facts/basic/
    validation_results = session.validate_facts(
        expected_facts=join(_this_dir, "facts", "basic2"), snapshot=PREVIOUS_SNAPSHOT
    )

    assert validation_results == {}, "No differences between expected and actual facts"


@requires_bfe("2019.10.21")
def test_topology_aggregates(session):
    put_aggs = {"a": ["b", "c"]}
    session.put_topology_aggregates(put_aggs)
    get_aggs = session.get_topology_aggregates()
    assert put_aggs == get_aggs

    session.delete_topology_aggregates()
    with pytest.raises(HTTPError) as e:
        session.get_topology_aggregates()
        assert e.response.status_code == 404


@requires_bfe("2019.10.21")
def test_topology_positions(session):
    put_pos = {"a": {"x": 1, "y": 2}}
    session.put_topology_positions(put_pos)
    get_pos = session.get_topology_positions()
    assert put_pos == get_pos

    session.delete_topology_positions()
    with pytest.raises(HTTPError) as e:
        session.get_topology_positions()
        assert e.response.status_code == 404


@requires_bfe("2019.10.29")
def test_snapshot_object(session):
    """Test that snapshot objects CRUD works."""
    session.put_snapshot_object("name", "goodbye")
    assert session.get_snapshot_object_text("name") == "goodbye"
    session.put_snapshot_object("name", "something_new")
    assert session.get_snapshot_object_text("name") == "something_new"
    session.delete_snapshot_object("name")
    with pytest.raises(HTTPError, match="404"):
        session.get_snapshot_object_text("name")


@requires_bfe("2019.11.11")
def test_get_config_diffs(session):
    """Test that we can get configuration diffs as a path string."""
    diff = session.get_configuration_diffs(CURRENT_SNAPSHOT, PREVIOUS_SNAPSHOT)
    assert isinstance(diff, str)
    assert len(diff) != 0
