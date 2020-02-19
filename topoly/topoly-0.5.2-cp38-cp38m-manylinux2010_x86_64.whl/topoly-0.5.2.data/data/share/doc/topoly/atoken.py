#!/usr/bin/python
# -*- coding: utf-8 -*-

from oauth2client.service_account import ServiceAccountCredentials

# The scope for the OAuth2 request.
SCOPE = 'https://www.googleapis.com/auth/analytics.readonly'
# The location of the key file with the key data.
KEY_FILEPATH = 'urg_files/PyLasso-c6c0843936c1.json'

# Load the key file's private data.
# Construct a credentials objects from the key data and OAuth2 scope.
_credentials = ServiceAccountCredentials.from_json_keyfile_name(KEY_FILEPATH, scopes=SCOPE)

# Defines a method to get an access token from the credentials object.
# The access token is automatically refreshed if it has expired.
def get_access_token():
  return _credentials.get_access_token().access_token
