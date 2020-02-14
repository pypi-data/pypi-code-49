import requests


def _get_name_fin_data(client, imis_id):
    headers = {
        'Authorization': client.auth.authorization_header
    }
    url = client.url + f'/api/CsNameFin/{imis_id}'
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()


def _update_name_fin_data(client, imis_id, payload):
    headers = {
        'Authorization': client.auth.authorization_header
    }
    url = client.url + f'/api/CsNameFin/{imis_id}'
    response = requests.put(url, json=payload, headers=headers)
    response.raise_for_status()
    return response.json()


def update_renewed_thru(client, imis_id, renewed_thru):
    if renewed_thru is not None:
        renewed_thru = renewed_thru.isoformat()
    headers = {
        'Authorization': client.auth.authorization_header
    }
    name_fin_data = _get_name_fin_data(client, imis_id)
    for index, element in enumerate(name_fin_data['Properties']['$values']):
        if element['Name'] == 'RENEWED_THRU':
            name_fin_data['Properties']['$values'][index]['Value'] = renewed_thru
    _update_name_fin_data(client, imis_id, name_fin_data)
