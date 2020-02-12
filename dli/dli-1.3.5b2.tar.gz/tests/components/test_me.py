import pytest

from tests.common import SdkIntegrationTestCase


@pytest.mark.integration
class MeTestCase(SdkIntegrationTestCase):

    def assert_my_entities_are_returned(self, func):
        assert len(func()) > 0
        assert len(func(count=1)) == 1

    def test_get_my_consumed_packages_validates_page_size(self):
        self.assert_page_count_is_valid_for_paginated_resource_actions(
            lambda c: self.client.get_my_consumed_packages(count=c)
        )

    def test_my_consumed_packages_returns_my_consumed_packages(self):
        package_id = self.create_package('test_consumed_packages', access="Unrestricted")
        package = self.client.get_package.__self__._get_package(package_id=package_id)

        self.client.session.put(
            f'/__api/packages/{package_id}/access/',
            json={
                'accountId': 'iboxx',
                'operation': 'request',
                'comment': 'Hello there!'
            }
        )

        self.assert_my_entities_are_returned(self.client.get_my_consumed_packages)

    def test_get_my_packages_validates_page_size(self):
        self.assert_page_count_is_valid_for_paginated_resource_actions(
            lambda c: self.client.get_my_packages(count=c)
        )

    def test_get_my_packages_returns_packages(self):
        self.create_package("test_me_functions")
        self.assert_my_entities_are_returned(self.client.get_my_packages)
