import logging

import requests
from django_countries import countries

from . import config
from .graph import SyncResult
from .models import BusinessArea, Region

logger = logging.getLogger(__name__)

c = dict(countries)


def load_region():
    url = "{}businessareas".format(config.INSIGHT_URL)
    response = requests.get(url, headers={'Ocp-Apim-Subscription-Key': config.INSIGHT_SUB_KEY})
    if response.status_code in [401, 403]:
        raise PermissionError('%s - %s: Invalid credentials' % (url, response.status_code))
    data = response.json()['ROWSET']['ROW']
    results = SyncResult()
    regions = set((e['REGION_CODE'], e['REGION_NAME']) for e in data)

    for entry in regions:
        region, created = Region.objects.update_or_create(code=entry[0],
                                                          defaults={
                                                              'name': entry[1]}
                                                          )
        results.log(region, created)
    logger.info(f"Region sync completed: {results}")
    return results


def load_business_area():
    url = "{}businessareas".format(config.INSIGHT_URL)
    response = requests.get(url, headers={'Ocp-Apim-Subscription-Key': config.INSIGHT_SUB_KEY})
    if response.status_code in [401, 403]:
        raise PermissionError('%s - %s: Invalid credentials' % (url, response.status_code))
    data = response.json()['ROWSET']['ROW']
    results = SyncResult()
    for entry in data:
        defaults = {'name': entry['BUSINESS_AREA_NAME'],
                    'country': countries.by_name(entry['BUSINESS_AREA_NAME']),
                    'region': Region.objects.get_or_create(code=entry['REGION_CODE'],
                                                           defaults={
                                                               'name': entry['REGION_NAME']}
                                                           )[0]
                    }
        area, created = BusinessArea.objects.update_or_create(code=entry['BUSINESS_AREA_CODE'],
                                                              defaults=defaults)
        results.log(area, created)
    logger.info(f"BusinessArea sync completed: {results}")
    return results
