import requests


class UserExistsError(Exception):
    pass


class ImisError(Exception):
    pass


def create(client, username, imis_id):
    headers = {
        'Authorization': client.auth.authorization_header
    }
    data = {
        '$type': 'Asi.Soa.Membership.DataContracts.UserData, Asi.Contracts',
        'UserName': username,
        'UserId': imis_id
    }
    url = client.url + '/api/User'
    response = requests.post(url, json=data, headers=headers)
    try:
        response.raise_for_status()
    except:
        error_response_body = response.content.decode()
        if 'DuplicateProviderUserKey' in error_response_body:
            raise UserExistsError(f'{username} exists')
        raise ImisError(error_response_body)
