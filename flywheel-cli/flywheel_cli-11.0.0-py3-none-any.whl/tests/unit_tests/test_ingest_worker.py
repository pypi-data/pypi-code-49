from unittest import mock

import pytest

from flywheel_cli.ingest.worker import IngestWorker


def test_ingest_worker_name_from_config():
    config = MockConfig()
    worker = IngestWorker(config)
    assert worker.name == config.worker_name


def test_ingest_worker_name_explicit():
    config = MockConfig()
    worker = IngestWorker(config, name="explicit-name")
    assert worker.name == "explicit-name"


class MockConfig:
    worker_name = "mock-worker-name"
