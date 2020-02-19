
class dataset_urls:
    instance = '/__api/datasets/{id}/'
    index = '/__api/datasets/'
    datafiles = '/__api/datasets/{id}/datafiles/'
    latest_datafile = '/__api/datasets/{id}/latest-datafile/'
    keys = '/__api/datasets/{id}/keys/'
    access_keys = '/__api/request-access-keys/'

    # dli_v2
    v2_index = '/__api_v2/datasets/'
    v2_instance = '/__api_v2/datasets/{id}/'
    v2_by_short_code = '/__api_v2/by_short_code/dataset/{dataset_short_code}'
    v2_sample_data_schema = '/__api_v2/datasets/{id}/sample_data'
    v2_sample_data_file = '/__api_v2/datasets/{id}/sample_data/file'

    schemas_many = '/__api/datasets/{id}/schemas/'
    schema_instance = '/__api/datasets/{id}/schema/'
    schema_instance_version = '/__api/datasets/{id}/schema/{version}'

    # V2 API
    dictionary_index =  '/__api_v2/dictionaries/'
    dictionary_instance = '/__api_v2/dictionaries/{id}/'
    dictionary_by_dataset = '/__api_v2/datasets/{id}/dictionaries/'
    dictionary_by_dataset_lastest = '/__api_v2/datasets/{id}/current_dictionary/'
    dictionary_fields = '/__api_v2/dictionaries/{id}/fields/'


class autoreg_urls:
    autoreg_index = '/__api/auto-reg-metadata/'
    autoreg_instance = '/__api/auto-reg-metadata/{id}/'


class datafile_urls:
    datafiles_index = '/__api/datafiles/'
    datafiles_instance = '/__api/datafiles/{id}/'


class me_urls:
    my_packages = '/__api/me/my-packages/'
    consumed_packages = '/__api/me/consumed_packages/'
    my_accounts = '/__api/me/my_accounts/'


class package_urls:
    package_index = '/__api/packages/'
    package_edit = '/__api/packages/{id}/'
    # For some reason these are 'package' not 'package*s*'
    package_datasets = '/__api/package/{id}/datasets/'
    v2_package_datasets = '/__api_v2/packages/{id}/datasets'

class search_urls:
    search_root = '/__api/search/'
    search_packages = '/__api/search/packages/'
    search_datasets = '/__api/search/datasets/'

class consumption_urls:
    consumption_download = '/datafile/{id}/download/binary/{path}'
    consumption_manifest = '/datafile/{id}/manifest/'
    consumption_dataframe = '/dataset/{id}/dataframe/'
    consumption_analytics = '/analytics/'
    consumption_partitions = '/dataset/{id}/partitions/'

class accounts_urls:
    account_instance = '/__api/account/{id}/'
