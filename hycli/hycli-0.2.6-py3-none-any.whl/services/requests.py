import requests


def request_token(token_endpoint, username, password):
    """ Request invoice extractor token """
    response = requests.post(
        url=token_endpoint,
        data={
            "username": username,
            "password": password,
            "grant_type": "password",
            "client_id": "extractionapi",
        },
        headers={"Content-Type": "application/x-www-form-urlencoded"},
    )
    # TODO: check status response
    token_dict = response.json()
    try:
        return token_dict["access_token"]
    except KeyError:
        quit("Credentials not correct")


def extract_invoice(file, extractor_endpoint, content_type, token=None):
    """ Request invoice extractor """
    response = requests.post(
        url=extractor_endpoint,
        data=file[1],
        params={"rasterization": "true", "probabilities": "true"},
        timeout=1800,
        headers={"Content-type": content_type, "Authorization": f"Bearer {token}"},
    )
    return file[0], response.json()


def validation(result, endpoint_url):
    """ Request validaton service """
    response = requests.post(
        url=endpoint_url,
        json=result["invoiceExtractor"],
        headers={"Content-type": "application/json"},
    )
    result["validation"] = response.json()


def validate_vat(result, endpoint_url):
    """ Request vat validator """
    response = requests.post(
        url=endpoint_url,
        json=result["invoiceExtractor"],
        headers={"Content-type": "application/json"},
    )
    result["vatValidator"] = response.json()
