from unittest import TestCase, mock
from k9.core import *
from k9.rbac import *
from k9.batch import *

class TestBatch(TestCase):

    ###########################################################################
    # cron job
    ###########################################################################
    def test_cron_job(self):
        try:
            ###############
            # Arrange
            set_default_namespace('default')
            sa_name = 'xx-ecr-cron-sa'
            bind_name = 'xx-ecr-cron-sa-bind'
            secret_name = 'aws-info'
            cj_name = 'xx-ecr-login-cron'
            role_name = 'ecr-login-role'

            create_service_account(sa_name)
            self.assertTrue(service_account_exists(sa_name))

            role = {
                'apiVersion': 'rbac.authorization.k8s.io/v1',
                'kind': 'ClusterRole',
                'metadata': {'name': f'{role_name}'},
                'rules': [
                    {
                        'apiGroups': [''],
                        'resources': ["serviceaccounts"],
                        'verbs': ["get", "patch"]

                    },
                    {
                        'apiGroups': [''],
                        'resources': ['secrets'],
                        'verbs': ['create', 'delete']
                    }
                 ]
            }
            create_cluster_role(role)
            self.assertTrue(cluster_role_exists(role_name))

            create_cluster_role_binding(bind_name, role_name, sa_name)
            self.assertTrue(cluster_role_binding_exists(bind_name))

            secrets = {
                'ecr-url': 'https://some-url',
                'aws-account': 'bogus account value',
                'aws-region': 'us-east-1'
            }
            create_secret(secret_name, secrets)
            self.assertTrue(secret_exists(secret_name))

            ###############
            # Act
            body = read_yaml(abs_path('../test/ecr-login-cron.yml'))
            result = create_cron_job(body)

            ###############
            # Assert
            self.assertEqual(cj_name, result.metadata.name)
            self.assertTrue(cron_job_exists(cj_name))

            # test list_cron_jobs()
            found = [
                cj['name']
                for cj in list_cron_jobs()
                if cj['name'] == cj_name
            ]
            self.assertEqual(1, len(found))

            # test get_cron_job()
            result = get_cron_job(cj_name)
            self.assertEqual(cj_name, result.metadata.name)

        finally:
            delete_cron_job(cj_name)
            delete_secret(secret_name)
            delete_cluster_role_binding(bind_name)
            delete_cluster_role(role_name)
            delete_service_account(sa_name)


    def test_cron_job_exists_fail(self):
        self.assertFalse(cron_job_exists('bogus'))

    def test_delete_bogus_cron_job(self):
        set_default_namespace('default')
        self.assertEqual(None, delete_cron_job('bogus'))
