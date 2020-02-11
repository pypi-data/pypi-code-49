from unittest import mock

import pytest

from flywheel_cli.bulk_import.process import ProcessQueue
from flywheel_cli.bulk_import.executor import AbstractQueue
from flywheel_cli.bulk_import.exceptions import EmptyQueue

MODULE_PATH = "flywheel_cli.bulk_import.process"


def test_bulk_import_process_queue_implements_abstract_queue(mocker):
    mocker.patch(MODULE_PATH + ".create_drone_client")
    mocker.patch(MODULE_PATH + ".create_flywheel_client")
    mocker.patch(MODULE_PATH + ".SdkUploadWrapper")

    assert isinstance(ProcessQueue(None), AbstractQueue)


def test_bulk_import_process_queue_get(mocker):
    mocker.patch(MODULE_PATH + ".create_drone_client")
    mocker.patch(MODULE_PATH + ".create_flywheel_client")
    mock_uploader = mocker.patch(MODULE_PATH + ".SdkUploadWrapper", return_value="uploader")
    mock_work_queue_mapper = mock.Mock(**{
        "get.return_value": "item"
    })
    mock_context = mock.Mock(work_queue_mapper=mock_work_queue_mapper)
    mock_processing_task = mocker.patch(MODULE_PATH + ".ProcessingTask")
    process_queue = ProcessQueue(mock_context)

    assert process_queue.get() == mock_processing_task.return_value
    mock_processing_task.assert_called_once_with(
        "item",
        mock_context.ingest_factory,
        "uploader",
        mock_context.config,
    )


def test_bulk_import_process_queue_get_timeout(mocker):
    mocker.patch(MODULE_PATH + ".create_drone_client")
    mocker.patch(MODULE_PATH + ".create_flywheel_client")
    mocker.patch(MODULE_PATH + ".SdkUploadWrapper")
    mock_work_queue_mapper = mock.MagicMock(**{
        "get.return_value": None
    })
    mock_context = mock.MagicMock(**{
        "work_queue_mapper": mock_work_queue_mapper,
    })
    process_queue = ProcessQueue(mock_context)

    assert process_queue.get() is None
