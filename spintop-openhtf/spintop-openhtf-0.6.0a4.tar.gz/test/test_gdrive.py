import pytest
import os
import mock

from collections import namedtuple

from oauth2client.service_account import ServiceAccountCredentials

import openhtf as htf
from spintop_openhtf.callbacks.gdrive import create_google_drive_outputs, load_credentials_file_with_scope
from spintop_openhtf.util.gdrive import GoogleDrive



HERE = os.path.abspath(os.path.dirname(__file__))

CREDS_FILENAME = os.path.expanduser(os.path.join('~', 'tack-infra-af44c5fee082.json'))# os.getenv('GS_CREDS_FILENAME')
DUMMY_ACCESS_TOKEN = '<ACCESS_TOKEN>'


class DummyCredentials(object):
    def __init__(self, dummy_token):
        self.access_token = dummy_token

    def authorize(self, *args, **kwargs):
        pass

# import vcr
# vcr = vcr.VCR(
#     filter_headers=['authorization'],
#     cassette_library_dir=os.path.join(HERE, 'cassettes')
# )

def sanitize_token(interaction, current_cassette):
    headers = interaction.data['request']['headers']
    token = headers.get('Authorization')

    if token is None:
        return

    interaction.data['request']['headers']['Authorization'] = [
        'Bearer %s' % DUMMY_ACCESS_TOKEN
    ]


def get_credentials():
    if CREDS_FILENAME:
        credentials = load_credentials_file_with_scope(CREDS_FILENAME)
    else:
        credentials = DummyCredentials(DUMMY_ACCESS_TOKEN)
    
    return credentials

@pytest.fixture()
def gwrap():
    credentials = get_credentials()
    gwrap = GoogleDrive(credentials)
    return gwrap
