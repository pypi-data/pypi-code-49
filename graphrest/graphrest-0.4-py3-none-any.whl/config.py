"""Configuration settings for running the Python auth samples locally.
In a production deployment, this information should be saved in a database or
other secure storage mechanism.
"""

CLIENT_ID = 'ENTER_YOUR'
CLIENT_SECRET = 'ENTER_YOUR'

# AUTHORITY_URL ending determines type of account that can be authenticated:
# /organizations = organizational accounts only
# /consumers = MSAs only (Microsoft Accounts - Live.com, Hotmail.com, etc.)
# /common = allow both types of accounts

TENANT_ID = 'TENANT_TO_AUTHENTICATED'
AUTHORITY_URL = 'https://login.microsoftonline.com/'

AUTH_ENDPOINT = '/oauth2/v2.0/authorize'
TOKEN_ENDPOINT = '/oauth2/v2.0/token'

RESOURCE = 'https://graph.microsoft.com/'
API_VERSION = 'v1.0'
SCOPES = ['https://graph.microsoft.com/.default'] # Add other scopes/permissions as needed.