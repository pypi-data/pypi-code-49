"""
smarty.utils
~~~~~~~~~~~~

This module implements all utility methods.
"""

import json
import random

import names
import requests

from smarty_py.resources.source_data import DATA as SOURCE_DATA


BASE = "https://api.smartrecruiters.com"


def call(endpoint, method="GET", expected_code=200, **kwargs):
    """ Call a given endpoint.

    :param endpoint: a `str` indicating the target endpoint.
    :param method: a `str` indicating the HTTP method to use.
    """
    url = "".join([BASE, endpoint])

    for key in kwargs:
        if key not in ("headers", "data", "params"):
            kwargs.pop(key)
    else:
        response = getattr(requests, method.lower())(url, **kwargs)

    if response.status_code == expected_code:
        try:
            return json.loads(response.text)
        except json.JSONDecodeError:
            return response.text
    else:
        raise Exception(f"Error: {response.status_code}")


def create_candidate(instance):
    """ Generates candidate object for API submission
    
    :return candidate_json: a JSON object of candidate data.
    """
    if instance["type"] == "US":
        companies = SOURCE_DATA["companies_us"]
        locations = SOURCE_DATA["locations_us"]
    elif instance["type"] == "EU":
        companies = SOURCE_DATA["companies_eu"]
        locations = SOURCE_DATA["locations_eu"]

    first_name = names.get_first_name()
    last_name = names.get_last_name()
    location = random.choice(locations)
    uni_start = random.randint(1980, 2000)
    work_start = uni_start + random.randint(3, 6)
    source = random.choice(SOURCE_DATA["sources"])
    candidate = {
        "firstName": first_name,
        "lastName": last_name,
        "email": "".join(
            [
                first_name,
                ".",
                last_name,
                str(random.randint(100, 9999)),
                "@mailinator.com",
            ]
        ),
        "phone": str(random.randint(1000000, 9999999)),
        "location": {
            "country": location[0],
            "countryCode": location[1],
            "regionCode": "",
            "region": location[4],
            "city": location[3],
            "address": "",
            "postalCode": "",
        },
        "web": {
            "skype": "",
            "linkedin": "",
            "facebook": "",
            "twitter": "",
            "website": "",
        },
        "tags": [random.choice(SOURCE_DATA["tags"]) for _ in range(3)],
        "education": [
            {
                "institution": random.choice(SOURCE_DATA["schools"]),
                "degree": "B.A.",
                "major": random.choice(SOURCE_DATA["majors"]),
                "current": False,
                "location": "",
                "startDate": str(uni_start),
                "endDate": str(uni_start + random.randint(4, 6)),
            }
        ],
        "experience": [
            {
                "title": random.choice(SOURCE_DATA["titles"]),
                "company": random.choice(companies),
                "current": True,
                "startDate": str(work_start),
                "endDate": str(work_start + 2),
                "location": "",
                "description": ", ".join(
                    [random.choice(SOURCE_DATA["descriptions"]) for _ in range(2)]
                ),
            },
            {
                "title": random.choice(SOURCE_DATA["titles"]),
                "company": random.choice(companies),
                "current": True,
                "startDate": str(work_start + 2),
                "endDate": str(work_start + 4),
                "location": "",
                "description": ", ".join(
                    [random.choice(SOURCE_DATA["descriptions"]) for _ in range(2)]
                ),
            },
            {
                "title": random.choice(SOURCE_DATA["titles"]),
                "company": random.choice(companies),
                "current": True,
                "startDate": str(work_start + 4),
                "endDate": str(work_start + 6),
                "location": "",
                "description": ", ".join(
                    [random.choice(SOURCE_DATA["descriptions"]) for _ in range(2)]
                ),
            },
        ],
        "sourceDetails": {"sourceTypeId": source[0], "sourceId": source[1]},
    }

    return candidate


def get_instance(token):
    """ Gets and returns instance data from the configuration API.

    :param token: a `str` SmartToken.
    :return instance: a `dict` of instance information.
    """
    endpoint = "/configuration/company"
    headers = {"X-SmartToken": token}

    response = call(endpoint, headers=headers)

    instance = response
    instance["type"] = (
        "US" if instance["location"]["country"] == "United States" else "EU"
    )

    return instance


def get_tokens():
    """ Gets and returns all saved SmartTokens from tokens.txt

    :return tokens: a `list` of tokens.
    """
    try:
        token_file = open("smarty_py/resources/tokens.txt", "r")
    except FileNotFoundError:
        open("smarty_py/resources/tokens.txt", "w+")
        token_file = open("smarty_py/resources/tokens.txt", "r")

    tokens = []
    for line in token_file.readlines():
        vals = line.split(" | ")
        tokens.append([vals[0], vals[1]])

    return tokens


def save_token(token, name):
    """ Saves a token and its instance name in tokens.txt.

    :param token: a `str` SmartToken.
    :param name: a `str` name for the token.
    """
    token_file = open("smarty_py/resources/tokens.txt", "a+")
    token_file.write("".join([name, " | ", token]))
