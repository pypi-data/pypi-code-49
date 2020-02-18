from ayda_tools.client.trainingservice import TrainingService
from ayda_tools.interfaces import JobInfo, TrainingOptions
from ayda_tools.client.resultservice import ResultService
from ayda_tools.client.connection import ServerConnection
from mock import patch, MagicMock


def test_train():
    job = JobInfo(1, TrainingOptions(), {}, {})
    conn = MagicMock(specs=ServerConnection)
    result = MagicMock(specs=ResultService)
    with patch(
        "ayda_tools.client.trainingservice.create_object", autospec=True
    ) as create_object:
        tr = TrainingService(conn, result)
        tr.train_job(job)
        create_object.assert_called_with({})
