from unittest import TestCase
from k9.core import *
from k9.rbac import *

class TestRbac(TestCase):

    ###########################################################################
    # Roles
    ###########################################################################

    def test_role(self):
        try:
            set_default_namespace('default')

            ############
            # Arrange

            role_name = 'pod-reader-role'
            role = {
                'apiVersion': 'rbac.authorization.k8s.io/v1',
                'kind': 'Role',
                'metadata': {
                    'name': role_name,
                    'namespace': 'default'
                    },
            'rules': [
                    {
                        'apiGroups': [''],
                        'resources': ['pods'],
                        'verbs': ['get', 'watch', 'list']
                    }
                ]
            }

            ############
            # Act
            result = create_role(role)

            ############
            # Assert
            self.assertEqual(role_name, result.metadata.name)

            # test role_exists()
            self.assertTrue(role_exists(role_name))

            # test get_role()
            result = get_role(role_name)
            self.assertEqual(role_name, result.metadata.name)

            # test list_roles()
            found = [
                role
                for role in list_roles()
                if role['name'] == role_name
            ]
            self.assertEqual(1, len(found))

            # test delete_role()
            result = delete_role(role_name)
            self.assertEqual('Success', result.status)

            self.assertFalse(role_exists(role_name))

        finally:
            delete_role(role_name)

    def test_role_exists_fail(self):
        self.assertFalse(role_exists('bogus'))

    def test_role_binding(self):
        try:
            ############
            # Arrange
            set_default_namespace('default')

            sa_name = "xx-pod-reader-sa"
            role_name = "xx-pod-reader-role"
            binding_name = "xx-pod-reader-binding"

            # create the service account
            result = create_service_account(sa_name)
            sa_name = result.metadata.name

            # create role
            body = read_yaml(abs_path('../test/xx-pod-reader-role.yml'))
            result = create_role(body)

            ############
            # Act

            # create cluster role binding
            result = create_role_binding(binding_name, role_name, sa_name)

            ############
            # Assert
            self.assertEqual(binding_name, result.metadata.name)

            # test get_role_binding()
            result = get_role_binding(binding_name)

            # test role_binding_exists()
            self.assertTrue(role_binding_exists(binding_name))

        finally:
            delete_role_binding(binding_name)
            self.assertFalse(role_binding_exists(binding_name))

            delete_role(role_name)
            self.assertFalse(role_exists(role_name))

            delete_service_account(sa_name)
            self.assertFalse(service_account_exists(sa_name))

    def test_delete_bogus_role(self):
        set_default_namespace('default')
        self.assertEqual(None, delete_role('bogus'))

    def test_delete_bogus_role_binding(self):
        set_default_namespace('default')
        self.assertEqual(None, delete_role_binding('bogus'))

    ###########################################################################
    # Cluster Roles
    ###########################################################################

    def test_cluster_role(self):
        try:
            ############
            # Arrange

            role_name = 'ecr-login-role'
            role = {
                'apiVersion': 'rbac.authorization.k8s.io/v1',
                'kind': 'ClusterRole',
                'metadata': {'name': f'{role_name}'},
                'rules': [
                     {
                         'apiGroups': [''],
                         'resources': ['secrets'],
                         'verbs': ['create', 'delete']
                     },
                     {
                         'apiGroups': [''],
                         'resources': ['serviceaccounts'],
                         'verbs': ['get', 'patch']
                     }
                 ]
            }

            ############
            # Act
            result = create_cluster_role(role)

            ############
            # Assert
            self.assertEqual(role_name, result.metadata.name)

            # test cluster_role_exists()
            self.assertTrue(cluster_role_exists(role_name))

            # test list_cluster_roles()
            role_list = [
                role
                for role in list_cluster_roles()
                    if role['name'] == role_name
            ]
            self.assertEqual(role_name, role_list[0]['name'])

            # test delete_cluster_role()
            result = delete_cluster_role(role_name)
            self.assertEqual('Success', result.status)

            self.assertFalse(cluster_role_exists(role_name))

        finally:
            delete_cluster_role(role_name)

    def test_cluster_role_binding(self):
        try:
            ############
            # Arrange
            set_default_namespace('default')

            sa_name = "unit-test-tomcat-sa"
            cr_name = "unit-test-jenkins-access"
            cr_bind_name = "unit-test-jenkins-binding"

            # create the service account
            result = create_service_account(sa_name)
            sa_name = result.metadata.name

            # create cluster role
            body = read_yaml(abs_path('../test/unittest-jenkins-access.yml'))
            result = create_cluster_role(body)

            ############
            # Act

            # create cluster role binding
            result = create_cluster_role_binding(cr_bind_name, cr_name, sa_name)

            ############
            # Assert
            self.assertEqual(cr_bind_name, result.metadata.name)

            # test get_cluster_role_binding()
            result = get_cluster_role_binding(cr_bind_name)

            # test cluster_role_binding_exists()
            self.assertTrue(cluster_role_binding_exists(cr_bind_name))

        finally:
            delete_cluster_role_binding(cr_bind_name)
            self.assertFalse(cluster_role_binding_exists(cr_bind_name))

            delete_cluster_role(cr_name)
            self.assertFalse(cluster_role_exists(cr_name))

            delete_service_account(sa_name)
            self.assertFalse(service_account_exists(sa_name))

    def test_delete_bogus_cluster_role(self):
        self.assertEqual(None, delete_cluster_role('bogus'))

    def test_delete_bogus_cluster_role_binding(self):
        self.assertEqual(None, delete_cluster_role_binding('bogus'))
