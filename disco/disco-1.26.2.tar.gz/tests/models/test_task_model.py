from tests.base_test import BaseTest
from disco.models import Task


class TestTaskModel(BaseTest):

    def test_task_create(self):

        task_id = self.random_str('task_id')
        task_status = 'Success'
        task_duration = self.random_int()
        task_input_file_id = self.random_str('input_file_id')
        artifact_ids = [self.random_str('artifact_id1'), self.random_str('artifact_id2')]

        task_data = {
            'id': task_id,
            'status': task_status,
            'stats': {'duration': task_duration},
            'request': {'inputFile': {'id': task_input_file_id}},
            'result': {'artifactIds': artifact_ids}
        }

        task = Task(task_data)
        assert task.id == task_id
        assert task.status == task_status
        assert task.duration == task_duration
        assert task.input_file_id == task_input_file_id
        assert task.artifact_ids == artifact_ids

    def test_task_create_without_artifact_ids(self):

        task_id = self.random_str('task_id')
        task_status = 'Success'

        task_data = {
            'id': task_id,
            'status': task_status,
        }

        task = Task(task_data)
        assert task.id == task_id
        assert task.status == task_status
        assert task.artifact_ids == []
