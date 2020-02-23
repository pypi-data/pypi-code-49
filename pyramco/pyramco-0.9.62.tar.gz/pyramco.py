'''
pyramco
version 0.9.6
2-23-2020

RAMCO API Documentation permalink:
https://api.ramcoams.com/api/v2/ramco_api_v2_doc.pdf

Requires the "requests" module:
https://pypi.org/project/requests/

your RAMCO API key should be set as an environment variable 
import it as: os.environ['RAMCO_API_KEY']
'''

import requests
import json
import base64
import os

# RAMCO API URL is always the same
url = 'https://api.ramcoams.com/api/v2/'

# deal with api key
api_key = os.environ['RAMCO_API_KEY']

# response code/error handling
code_200 = {
    'DescriptionShort': 'OK',
    'DescriptionVerbose': 'The request was successfully processed and data is included in the response.'
}

code_204 = {
    'DescriptionShort': 'OK - No Data',
    'DescriptionVerbose': 'The request was successfully processed but no data is included in the response.'
}

code_206 = {
    'DescriptionShort': 'OK - Partial Data',
    'DescriptionVerbose': 'The request was successfully processed and partial data is included in the response. A StreamToken will be returned to fetch the remaining data.'
}

code_400 = {
    'DescriptionShort': 'Bad Request',
    'DescriptionVerbose': 'The request was not understood. See the response text for more information.'
}

code_401 = {
    'DescriptionShort': 'Unauthorized',
    'DescriptionVerbose': 'The request was understood but it will not be fulfilled due to a lack of user permissions. See the response text for more information.'
}

code_404 = {
    'DescriptionShort': 'Not Found',
    'DescriptionVerbose': 'The request is understood but no matching data is found to return.'
}

code_422 = {
    'DescriptionShort': 'Invalid User',
    'DescriptionVerbose': 'No user exists with provided username and password combination. This error is specific to the AuthenticateUser request.'
}

code_500 = {
    'DescriptionShort': 'Server Error',
    'DescriptionVerbose': 'Something is not working correctly server-side. This is not an issue that can be resolved by modifying query syntax.'
}

code_unknown = {
    'ResponseCode': 999,
    'DescriptionShort': 'Unknown Internal/pyramco Error',
    'DescriptionVerbose': 'No code or response returned from RAMCO. The error is likely in your code or pyramco itself.'
}


# all replies from RAMCO are passed through the handler
def handler(reply):

    if reply['ResponseCode'] == 200 or reply['ResponseCode'] == 206:

        # all replies contain a section 'Data' with the information
        full_dict = reply
        full_list = full_dict['Data']

        # Accounts for streamtoken responses from RAMCO
        while 'StreamToken' in reply:
            reply = resume_streamtoken(reply['StreamToken'])
            reply_list = reply['Data']

            # continue adding the 'Data' section to the full list
            full_list.extend(reply_list)

        # return the original reply header and combined 'Data'
        full_dict['Data'] = full_list
        return(full_dict)

    # return unmodified results
    elif reply['ResponseCode'] == 204:
        return(reply)

    # return results plus additional error text from documentation
    elif reply['ResponseCode'] == 400:
        reply = {**reply, **code_400}
        return(reply)

    elif reply['ResponseCode'] == 404:
        reply = {**reply, **code_404}
        return(reply)

    elif reply['ResponseCode'] == 422:
        reply = {**reply, **code_422}
        return(reply)

    elif reply['ResponseCode'] == 500:
        reply = {**reply, **code_500}
        return(reply)

    # return the text for other/unknown errors
    else:
        return(code_unknown)


# metadata operations
def get_entity_types():
    '''
    No arguments are accepted
    Returns all entity names as a dict of 'fieldname':'SchemaName'
    '''

    payload = {
        'key': api_key,
        'Operation': 'GetEntityTypes'
    }

    reply = handler(requests.post(url, payload).json())
    return(reply)


def get_entity_metadata(entity):
    '''
    Accepts a valid entity schema name as a string
    Returns all metadata on that entity
    '''

    payload = {
        'key': api_key,
        'Operation': 'GetEntityMetadata',
        'Entity': entity
    }

    reply = handler(requests.post(url, payload).json())
    return(reply)


def get_option_set(entity, attribute):
    '''
    Accepts a valid entity schema name and a single attribute name
    Returns a dict of 'value': 'label' pairs for the specified OptionSet
    '''

    payload = {
        'key': api_key,
        'Operation': 'GetOptionSet',
        'Entity': entity,
        'Attribute': attribute
    }
    reply = handler(requests.post(url, payload).json())
    return(reply)


def clear_cache():
    '''
    No arguments are accepted
    Clears the server-side metadata cache
    '''

    payload = {
        'key': api_key,
        'Operation': 'ClearCache'
    }

    reply = handler(requests.post(url, payload).json())
    return(reply)


# data querying operations
def get_entity(entity, guid, *attributes):
    '''
    Accepts an entity name, GUID, and a tuple of attribute names
    Returns attribute values for the specified entity matching the GUID
    '''

    payload = {
        'key': api_key,
        'Operation': 'GetEntity',
        'Entity': entity,
        'GUID': guid,
        'Attributes': attributes
    }

    reply = handler(requests.post(url, payload).json())
    return(reply)


def get_entities(entity, *attributes, filters='',
                 string_delimiter='', max_results=''):
    '''
    Accepts an entity name, a tuple of attribute names, (optionally) a filter string, a string delimiter character, and an int value for max results
    Returns all matches or the first n results for max results
    '''

    payload = {
        'key': api_key,
        'Operation': 'GetEntities',
        'Entity': entity,
        'Filter': filters,
        'Attributes': attributes,
        'StringDelimiter': string_delimiter,
        'MaxResults': max_results
    }

    reply = handler(requests.post(url, payload).json())
    return(reply)


def resume_streamtoken(streamtoken):
    '''
    Accepts a valid streamtoken as a string and resumes the get_entities request that generated it
    Returns resumed results
    '''

    payload = {
        'key': api_key,
        'Operation': 'GetEntities',
        'StreamToken': streamtoken
    }

    reply = handler(requests.post(url, payload).json())
    return(reply)


def validate_user(username, password):
    '''
    Accepts a username and password
    if valid - Returns that Contact's guid
    if invalid - returns 422 error
    '''

    payload = {
        'key': api_key,
        'Operation': 'ValidateUser',
        'cobalt_username': username,
        'cobalt_password': password
    }

    reply = handler(requests.post(url, payload).json())
    return(reply)


# data transformation operations
def update_entity(entity, guid, *attributes, string_delimiter=''):
    '''
    Accepts a valid entity name + guid, a tuple of comma separated
    attribute=value pairs, and optionally a string delimiter character
    '''

    payload = {
        'key': api_key,
        'Operation': 'UpdateEntity',
        'Entity': entity,
        'Guid': guid,
        'AttributeValues': attributes,
        'StringDelimiter': string_delimiter
    }

    reply = handler(requests.post(url, payload).json())
    return(reply)


def create_entity(entity, *attributes, string_delimiter=''):
    '''
    Accepts a valid entity name, a tuple of comma separated attribute=value
    pairs, and optionally a string delimiter character
    '''

    payload = {
        'key': api_key,
        'Operation': 'CreateEntity',
        'Entity': entity,
        'AttributeValues': attributes,
        'StringDelimiter': string_delimiter
    }

    reply = handler(requests.post(url, payload).json())
    return(reply)


def delete_entity(entity, guid):
    '''
    Accepts a guid and deletes the corresponding record
    '''

    payload = {
        'key': api_key,
        'Operation': 'DeleteEntity',
        'Entity': entity,
        'GUID': guid
    }

    reply = handler(requests.post(url, payload).json())
    return(reply)

# end pyramco wrapper operations


# base64 encoder/decoder for attachments
def base64_encode(input):
    output = str(base64.standard_b64encode(input))
    return(output)

def base64_decode(input):
    output = base64.standard_b64decode(input)
    return(output)
