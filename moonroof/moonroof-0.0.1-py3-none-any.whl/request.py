import requests
import json
from django.conf import settings

MOONROOF_URL = 'https://moonroof-api-prod.herokuapp.com/api/events-bulk'

HEADERS = {
    'Authorization': 'Bearer {0}'.format(settings.MOONROOF_API_KEY),
    'Content-Type': 'application/json'
}

def post(items):
    # TODO: gzip data
    requests.post(
        MOONROOF_URL,
        data=json.dumps({'events': [{'data': i for i in items}]}),
        headers=HEADERS
    )
