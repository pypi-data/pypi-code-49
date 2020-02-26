import copy
import pytest


@pytest.fixture
def empty_package_request():
    return {
            "class": ["Access Requests", "collection"],
            "properties": {"page": 1, "pages_count": 1},
            "entities": []
           }


class TestPaginator:
    def test_retrieve_zero_packages(self, test_client, empty_package_request,
                                    dataset_request):
        test_client._session.get.return_value.json.side_effect = [
            empty_package_request, dataset_request]

        pp = test_client.packages(search_term="")
        assert len(pp) == 0

    def test_threaded_paginator(self, test_client,
                                package_request, dataset_request):

        p = {
            'class': ['Access Requests', 'collection'],
            'properties': {'page': 1, 'pages_count': 2},
            'entities': [{
                'properties': {
                    'packageId': '8137dec0-8569-11e9-8727-f64112f300c3',
                    'name': 'Test Package',
                    'data': {
                        'name': 'Test Package',
                        'topic': 'Test Topic',
                        'keywords': ['test'],
                        'hasAccess': True,
                        'description': 'DESC',
                        'documentation': 'href',
                        'dataSensitivity': 'Private',
                    },
                    'total_records': 1,
                }
            }]
           }
        p2 = {
            'class': ['Access Requests', 'collection'],
            'properties': {'page': 2, 'pages_count': 2},
            'entities': [{
                'properties': {
                    'packageId': '8137dec0-8569-11e9-8727-f64112f300c3',
                    'name': 'Test Package 2',
                    'data': {
                        'name': 'Test Package 2',
                        'topic': 'Test Topic',
                        'keywords': ['test'],
                        'hasAccess': True,
                        'description': 'DESC',
                        'documentation': 'href',
                        'dataSensitivity': 'Private',
                    },
                    'total_records': 1,
                }
            }]
           }

        # Note: there is no side-effect call to dataset because the call that was
        # previously made in the constructor by .shape has now been made lazy to
        # avoid an explosion of calls.
        test_client._session.get.return_value.json.side_effect = [p, p2]

        pp = test_client.packages(search_term="")

        assert len(pp) == 2

