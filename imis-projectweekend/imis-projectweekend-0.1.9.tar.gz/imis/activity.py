import requests

from imis.utils import dict_to_generic_property_data_collection, generic_property_data_collection_to_dict


def create(client, data):
    headers = {
        'Authorization': client.auth.authorization_header
    }
    body = {
        '$type': 'Asi.Soa.Core.DataContracts.GenericEntityData, Asi.Contracts',
        'PrimaryParentEntityTypeName': 'Party',
        'Properties': dict_to_generic_property_data_collection(data)
    }
    url = client.url + '/api/Activity'
    response = requests.post(url, headers=headers, json=body)
    response.raise_for_status()
    return generic_property_data_collection_to_dict(response.json()['Properties'])
