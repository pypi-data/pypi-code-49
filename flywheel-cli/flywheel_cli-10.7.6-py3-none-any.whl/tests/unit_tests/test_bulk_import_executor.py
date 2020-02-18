from unittest import mock

import pytest

from flywheel_cli.bulk_import.executor import BulkImportExecutor, AbstractQueue

MODULE_PATH = "flywheel_cli.bulk_import.executor"


class TestQueue(AbstractQueue):
    def get(self, timetout=None):
        pass


def test_bulk_import_executor_add_queue_valid_queue():
    executor = BulkImportExecutor()
    test_queue = TestQueue()

    executor.add_queue("test", test_queue)
    assert executor._queues["test"] == test_queue


def test_bulk_import_executor_add_queue_invalid_queue():
    executor = BulkImportExecutor()
    class Queue:
        pass
    test_queue = Queue()

    with pytest.raises(Exception):
        executor.add_queue("test", test_queue)
    assert executor._queues == {}


def test_bulk_import_executor_start_idempotent(mocker):
    executor = BulkImportExecutor()
    executor.add_queue("test", TestQueue())
    mock__start_single_worker = mocker.patch.object(executor, "_start_single_worker")

    executor.start(8)
    assert mock__start_single_worker.call_count == 8
    executor.start(1)
    assert mock__start_single_worker.call_count == 8


def test_bulk_import_executor_shutdown(mocker):
    executor = BulkImportExecutor()
    for _ in range(2):
        mock_event = mock.MagicMock(**{
            "set.return_value": None
        })
        executor._work_processes.append((None, mock_event))
    mock_join = mocker.patch.object(executor, "join")

    executor.shutdown()
    for _, mock_event in executor._work_processes:
        mock_event.set.assert_called_once()
    mock_join.assert_called_once()


def test_bulk_import_executor_join(mocker):
    executor = BulkImportExecutor()
    for _ in range(2):
        mock_proc = mock.MagicMock(**{
            "join.return_value": None
        })
        executor._work_processes.append((mock_proc, None))

    executor.join()
    for mock_proc, _ in executor._work_processes:
        mock_proc.join.assert_called_once()
