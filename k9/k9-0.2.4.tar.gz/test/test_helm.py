from unittest import TestCase
from k9.helm import *
from k9.core import set_default_namespace, delete_namespace

from k9.pretty_object import PrettyObject

po = PrettyObject()


class TestHelm(TestCase):

    def test_helm_repo_add(self):
        set_default_namespace('unittest')
        result = helm_repo_add('simoncomputing', 'http://charts.simoncomputing.com')
        self.assertTrue("has been added" in result.stdout)

        helm_repo_update()

        result = helm_repo_ls()

        found = [
            repo['name']
            for repo in result
            if repo['name'] == 'simoncomputing'
        ]

        self.assertEqual(1, len(found))

        result = helm_repo_remove('simoncomputing')
        self.assertTrue("has been removed" in result.stdout)

    def test_helm_repo_add_fail(self):
        with self.assertRaisesRegex(Exception, "non-zero exit status 1."):
            helm_repo_add('simoncomputing', 'http://bogus')

    def test_helm_repo_remove_fail(self):
        with self.assertRaisesRegex(Exception, "non-zero exit status 1."):
            helm_repo_remove('bogus')

    def test_helm_install(self):
        try:
            set_default_namespace('tomcat')

            helm_repo_add('stable', 'https://kubernetes-charts.storage.googleapis.com/')

            # Test helm_install()
            helm_install('stable/tomcat', {'domain': 'sandbox.simoncomputing.com'})

            # test helm_ls()
            release_name = 'tomcat'
            result = helm_ls()
            found = [
                release
                for release in result
                if release['name'] == release_name
            ]
            self.assertIsNotNone(found)
            self.assertEqual(release_name, found[0]['name'])

            # test helm_exists()
            self.assertTrue(helm_exists(release_name))

        finally:
            # test helm_uninstall()
            result = helm_uninstall(release_name)
            print(f'result={result.stdout}')
            self.assertTrue('uninstalled' in result.stdout)
            self.assertFalse(helm_exists(release_name))

            helm_repo_remove('stable')
            delete_namespace()

    def test_helm_uninstall_fail(self):
        with self.assertRaisesRegex(Exception, 'returned non-zero exit status'):
            helm_uninstall('bogus')



