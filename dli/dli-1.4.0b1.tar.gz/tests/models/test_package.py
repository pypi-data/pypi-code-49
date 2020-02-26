

class TestPackageModule:
    def test_retrieve_packages(
        self, test_client, package_request, dataset_request
    ):

        test_client._session.get.return_value.json.side_effect = [
            package_request, dataset_request]

        pp = test_client.packages(search_term='')
        assert len(pp) == 1

    def test_display_package(
        self, capsys, test_client, package_request, dataset_request
    ):
        test_client._session.get.return_value.json.side_effect = [
            package_request, dataset_request
        ]

        pp = test_client.packages(search_term='')
        pp['Test Package'].display()
        captured = capsys.readouterr()
        assert captured.out == \
            '\nDATASET "TestDataset" [PARQUET]\n' \
            '>> Available Date Range: 2019-05-06 to 2020-01-01\n' \
            '>> ID: 5b01376e-975d-11e9-8832-7e5ef76d533f\n' \
            '>> Published: Monthly by IHS Markit\n' \
            '>> Accessible: False\n' \
            '\ndescription' \
            '\n---------------------------------------' \
            '-----------------------------------------\n'

    def test_retrieve_datasets_given_package(self, test_client,
                                             package_request, dataset_request):
        test_client._session.get.return_value.json.side_effect = [
            package_request, dataset_request
        ]

        pp = test_client.packages(search_term='')
        ds = pp['Test Package'].datasets()
        assert len(ds) == 1

    def test_retrieve_package_by_get(
        self, test_client, package_request, dataset_request
    ):

        test_client._session.get.return_value.json.side_effect = [
            package_request, dataset_request
        ]

        pp = test_client.packages(search_term='')
        a = pp.get('Test Package')
        assert(a.name == package_request['entities'][0]['properties']['name'])
