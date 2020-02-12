from unittest import TestCase, mock
from k9.core import *
from k9.rbac import *
from k9.apps import *

import io
import base64
import os.path
import pprint

import time

from datetime import datetime, timedelta

from k9.pretty_object import PrettyObject

po = PrettyObject()
pp = pprint.PrettyPrinter(indent=2, width=120)

class TestCore(TestCase):

    ###########################################################################
    # Util
    ###########################################################################

    def test_run_command_success(self):
        set_run_output(True)
        result = run_command('ls', '-la')
        self.assertTrue('charts' in result.stdout)

    def test_run_command_fail(self):
        with self.assertRaisesRegex(FileNotFoundError, 'No such file or directory'):
            run_command('bogus -la')

    def test_last_word(self):
        self.assertEqual('my-pod', last_word('pods/my-pod'))

    @mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_view_yaml(self, mock_stdout):
        view_yaml(abs_path('../test/tomcat-deploy-dev.yml'))
        self.assertTrue('tomcat-dev' in mock_stdout.getvalue())

    def test_read_yaml(self):
        body = read_yaml(abs_path('../test/tomcat-deploy-dev.yml'))
        self.assertEqual('tomcat-dev', body['metadata']['name'])

    def test_age(self):
        now = datetime.now(timezone.utc)

        diff = timedelta(hours=14, minutes=4, seconds=22)
        then = now - diff
        self.assertEqual('14:04:22', get_age(then))

        diff = timedelta(hours=4, minutes=14, seconds=2)
        then = now - diff
        self.assertEqual('04:14:02', get_age(then))

        diff = timedelta(hours=23, minutes=14, seconds=2)
        then = now - diff
        self.assertEqual('23:14:02', get_age(then))

        diff = timedelta(days=1, hours=23, minutes=14, seconds=2)
        then = now - diff
        self.assertEqual('1d', get_age(then))

        diff = timedelta(days=25, hours=23, minutes=14, seconds=2)
        then = now - diff
        self.assertEqual('25d', get_age(then))

    def test_absolute_dir(self):
        result = abs_path('test')

        self.assertTrue(len(result) > 4)
        self.assertTrue('/' in result)
        self.assertEqual('test', last_word(result))


    ###########################################################################
    # Namespace
    ###########################################################################

    def test_list_namespaces(self):
        result = list_namespaces()
        self.assertTrue(len(result)>0)

    def test_default_namespace(self):
        set_default_namespace("test")
        self.assertEqual("test", get_default_namespace())

    def test_create_namespace(self):
        try:
            ns = "namespace-unit-test"
            set_default_namespace(ns)

            create_namespace()
            self.assertTrue(namespace_exists())

            result = get_namespace()
            self.assertEqual(ns, result.metadata.name)

        finally:
            delete_namespace()
            self.assertFalse(namespace_exists())

    def test_delete_bogus_namespace(self):
        self.assertEqual(None, delete_namespace('bogus'))

    def test_get_bogus_namespace(self):
        with self.assertRaisesRegex(Exception, 'You must call set_default_namespace()'):
            set_default_namespace('bogus')
            set_default_namespace()
            get_default_namespace()

    ###########################################################################
    # Pods
    ###########################################################################

    def test_list_pods(self):
        result = list_pods("kube-system")
        self.assertIsNotNone(result)
        self.assertTrue(len(result) > 0)

        set_default_namespace("default")
        result = list_pods()
        self.assertTrue(len(result) == 0)

    def test_wait_for_pod(self):
        try:
            set_default_namespace("wait-test")
            if not namespace_exists("wait-test"):
                create_namespace("wait-test")

            if not deployment_exists("tomcat"):
                secret_name = "tomcat-dev"
                secrets = {
                    'ds-url': 'https://some/url',
                    'password': 'My1SecretPassword',
                    'username': 'postgres'
                }
                create_secret(secret_name, secrets)
                body = read_yaml(abs_path('../test/tomcat-deploy-dev.yml'))
                create_deployment(body)
                time.sleep(1)

            pods = list_pods()
            print(pods)
            self.assertEqual(pods[0]['status'], 'Pending')
            wait_for_pod(pods[0]['name'])
            pods = list_pods()
            self.assertEqual(pods[0]['status'], 'Running')
        finally:
            delete_deployment('tomcat-dev')
            delete_secret('tomcat-dev')
            delete_namespace('wait-test')

    def test_copy_to_from_pod(self):
        try:
            # uses example-file.txt
            set_default_namespace("copy-test")
            if not namespace_exists("copy-test"):
                create_namespace("copy-test")
            if not deployment_exists("tomcat"):
                secret_name = "tomcat-dev"
                secrets = {
                    'ds-url': 'https://some/url',
                    'password': 'My1SecretPassword',
                    'username': 'postgres'
                }
                create_secret(secret_name, secrets)
                body = read_yaml(abs_path('../test/tomcat-deploy-dev.yml'))
                create_deployment(body)
                time.sleep(1)
            pods = list_pods()
            print(f'pods are {pods}')
            self.assertIsNotNone(pods)
            wait_for_pod(pods[0]['name'])
            copy_to_pod(pods[0]['name'], abs_path('../test/example-file.txt'), '/var/example-file.txt')
            copy_from_pod(pods[0]['name'], '/var/example-file.txt', abs_path('../test/newex.txt'))
            self.assertTrue(os.path.exists(abs_path('../test/newex.txt')))

        finally:
            delete_deployment('tomcat-dev')
            delete_secret('tomcat-dev')
            delete_namespace('copy-test')
            run_command('rm', '-f', abs_path('../test/newex.txt'))


    ###########################################################################
    # Secrets
    ###########################################################################

    def test_create_secret(self):
        try:
            set_default_namespace("default")

            secret_name = "tomcat-dev"
            secrets = {
                'ds-url': 'https://some/url',
                'password': 'My1SecretPassword',
                'username': 'postgres'
            }

            # Test create_secret()
            result = create_secret(secret_name, secrets)
            self.assertEqual(secret_name, result.metadata.name)

            # Test get_secret()
            result = get_secret(secret_name)
            self.assertEqual(secret_name, result.metadata.name)

            # Check secret values
            for key, value in result.data.items():
                self.assertEqual(secrets[key], base64.b64decode(value).decode('utf8'))

            # Test secret_exists()
            self.assertTrue(secret_exists(secret_name))

            # Test list_secret()
            result = list_secrets()

            secret_list = [
                s['name']
                for s in result
                if s['name'] == secret_name
            ]

            self.assertEqual(1, len(secret_list))
            self.assertEqual(secret_name, secret_list[0])

        finally:
            delete_secret(secret_name)

    def test_secret_exists(self):
        set_default_namespace('default')
        self.assertFalse(secret_exists('bogus-secret'))

    def test_delete_bogus_secret(self):
        set_default_namespace('default')
        self.assertEqual(None, delete_secret('bogus'))

    ###########################################################################
    # Deployments
    ###########################################################################

    def test_deployments(self):
        try:
            secret_name = "tomcat-dev"
            deploy_name = 'tomcat-dev'

            set_default_namespace("deployment-unit2-test")
            if not namespace_exists("deployment-unit2-test"):
                create_namespace()

            secrets = {
                'ds-url': 'https://some/url',
                'password': 'My1SecretPassword',
                'username': 'postgres'
            }

            # Test create_secret()
            create_secret(secret_name, secrets)

            body = read_yaml('tomcat-deploy-dev.yml')
            create_deployment(body)
            self.assertTrue(deployment_exists(deploy_name))

            result = get_deployment(deploy_name)
            self.assertEqual(deploy_name, result.metadata.name)

            result = [
                d
                for d in list_deployments()
                if d['name'] == deploy_name
            ]
            self.assertEqual(1, len(result))
            self.assertFalse(deployment_exists('bogus'))

            # Update deployment
            update_deployment_image(deploy_name, 'tomcat', 'tomcat:8')

            # Confirm that deployment image has been updated.
            result = get_deployment(deploy_name)
            self.assertEqual(deploy_name, result.metadata.name)
            found = [
                container.image
                for container in result.spec.template.spec.containers
                if container.name == 'tomcat'
            ]
            self.assertEqual('tomcat:8', found[0])


            # Scale deployment
            spec = {
                'replicas': 3
            }
            scale_deployment(deploy_name, spec)
            result = get_deployment(deploy_name)
            self.assertEqual(deploy_name, result.metadata.name)
            self.assertEqual(3, result.spec.replicas)


        finally:

            delete_deployment(deploy_name)
            delete_secret(secret_name)
            delete_namespace()


    def test_delete_bogus_deployment(self):
        set_default_namespace('default')
        self.assertEqual(None, delete_deployment('bogus'))

    ###########################################################################
    # Services
    ###########################################################################
    def test_service(self):
        try:
            # Arrange
            svc_name = 'tomcat-svc-dev'
            secret_name = "tomcat-dev"
            deploy_name = 'tomcat-dev'

            set_default_namespace("service-unit-test")
            if not namespace_exists("service-unit-test"):
                create_namespace()

            secrets = {
                'ds-url': 'https://some/url',
                'password': 'My1SecretPassword',
                'username': 'postgres'
            }

            create_secret(secret_name, secrets)
            body = read_yaml(abs_path('../test/tomcat-deploy-dev.yml'))
            create_deployment(body)

            # Act
            body = read_yaml(abs_path('../test/tomcat-svc-dev.yml'))

            create_service(body)

            # Assert
            result = get_service(svc_name)
            self.assertEqual(svc_name, result.metadata.name)

            result = list_services()
            found = [
                svc['name']
                for svc in result
                if svc_name in svc['name']
            ]
            self.assertEqual(1, len(found))

        finally:
            if service_exists(svc_name):
                delete_service(svc_name)

            delete_deployment(deploy_name)

            delete_secret(secret_name)
            delete_namespace()

    def test_service_exists_fail(self):
        set_default_namespace('default')
        self.assertFalse(service_exists('bogus'))

    def test_delete_bogus_service(self):
        set_default_namespace('default')
        self.assertEqual(None, delete_service('bogus'))

    ###########################################################################
    # Service Accounts
    ###########################################################################

    def test_service_accounts(self):
        try:
            ############
            # Arrange
            set_default_namespace('default')
            sa_name = "unit-test-tomcat-sa"

            ############
            # Act
            result = create_service_account(sa_name)

            ############
            # Assert

            self.assertEqual(sa_name, result.metadata.name)

            # test get_service_account()
            result = get_service_account(sa_name)
            self.assertEqual(sa_name, result.metadata.name)

            # test service_account_exists()
            self.assertTrue(service_account_exists(sa_name))

            # test_list_service_accounts()
            result = list_service_accounts()

            result = [
                sa['name']
                for sa in result
                if sa['name'] == sa_name
            ]
            self.assertEqual(1, len(result))

        finally:
            delete_service_account(sa_name)


    def test_service_account_exists_fail(self):
        set_default_namespace('default')
        self.assertFalse(service_account_exists('bogus'))
        self.assertTrue(service_account_exists('default'))

    def test_list_service_account_fail(self):
        self.assertEqual(0, len(list_service_accounts('bogus')))

    def test_delete_bogus_service_account(self):
        set_default_namespace('default')
        self.assertEqual(None, delete_service_account('bogus'))

