from tests.base_test import BaseTest
from disco.models import JobDetails


class TestJobDetailsModel(BaseTest):

    def test_job_create(self):

        job_id = self.random_str('job-id')
        job_name = self.random_str('job-name')
        job_status = self.random_str('Working')

        tasks_summary = {
            'timeout': self.random_int(),
            'queued': self.random_int(),
            'running': self.random_int(),
            'failed': self.random_int(),
            'success': self.random_int(),
            'all': self.random_int()
        }

        job_data = {
            'id': job_id,
            'request': {'meta': {'name': job_name}},
            'status': job_status,
            'tasksSummary': tasks_summary
        }

        job_details = JobDetails(job_data)
        assert job_details.id == job_id
        assert job_details.name == job_name
        assert job_details.status == job_status
        assert job_details.tasks_summary.timeout == tasks_summary['timeout']
        assert job_details.tasks_summary.queued == tasks_summary['queued']
        assert job_details.tasks_summary.running == tasks_summary['running']
        assert job_details.tasks_summary.failed == tasks_summary['failed']
        assert job_details.tasks_summary.success == tasks_summary['success']
        assert job_details.tasks_summary.all == tasks_summary['all']

    def test_job_create_without_tasks_summary(self):

        job_id = self.random_str('job-id')
        job_name = self.random_str('job-name')
        job_status = self.random_str('Working')

        job_data = {
            'id': job_id,
            'request': {'meta': {'name': job_name}},
            'status': job_status,
        }

        job_details = JobDetails(job_data)
        assert job_details.id == job_id
        assert job_details.name == job_name
        assert job_details.status == job_status
        assert job_details.tasks_summary is None
