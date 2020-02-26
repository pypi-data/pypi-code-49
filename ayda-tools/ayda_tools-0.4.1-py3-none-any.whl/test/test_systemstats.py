from ayda_tools.client.systemstats import get_sys_info, SystemMonitor
from ayda_tools.interfaces import JobInfo, TrainingOptions
from ayda_tools.client.connection import ServerConnection
from ayda_tools.client.callbacks import SystemMonitorSender
from mock import MagicMock, patch
import pytest


def test_get_sys_info():
    info = get_sys_info()
    print(info)


def test_sys_monitor_start_stop():
    s = SystemMonitor()
    with s:
        s.pull_collected_stats()


@pytest.fixture()
def system_status_sender():
    with patch("ayda_tools.client.callbacks.Queue", autospec=True), patch(
        "ayda_tools.client.callbacks.Process", autospec=True
    ):
        conn = MagicMock(spec=ServerConnection)
        epoch_size = 10
        epochs = 10
        job = JobInfo(0, TrainingOptions(epochs, epoch_size, 0, 0), {}, {})
        job.obj_ref = "FakeID"

        sender = SystemMonitorSender(conn, job)
        yield sender


def test_sys_monitor_sender(system_status_sender):
    system_status_sender.on_train_begin()
    for e in range(10):
        for b in range(10):
            system_status_sender.on_batch_end(b)
        system_status_sender.on_epoch_end(e)
    system_status_sender.on_train_end()


def test_sys_monitor_sender_process_loop(system_status_sender):
    with patch.object(
        system_status_sender, "system_monitor", autospec=True
    ), patch.object(system_status_sender, "get_queued_data"):
        system_status_sender.system_monitor.pull_collected_stats.return_value = {
            "gpu": {},
            "cpu": {},
            "mem": {},
            "timestamp": 0,
        }
        system_status_sender.get_queued_data.return_value = [
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
            [21, 22, 23, 24],
        ]
        system_status_sender.get_stats()
        data = (
            '{"_no_index": null, "cpu": {}, "finished_batches": 4, '
            '"finished_epochs": 1, "gpu": {}, "job_ref": "FakeID", '
            '"mem": {}, "obj_ref": "FakeID.1.4", "py/object": '
            '"ayda_tools.interfaces.SystemStats", "time_per_batch": 1.0, '
            '"timestamp": 0, "total_batches": 10, "total_epochs": 10}'
        )
        system_status_sender.connection.send_server_request.assert_called_with(
            "send_stats", data
        )
