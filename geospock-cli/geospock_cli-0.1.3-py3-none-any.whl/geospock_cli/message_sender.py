# Copyright (c) 2014-2020 GeoSpock Ltd.

import http.client
import click
from urllib.parse import urlparse


class MessageSender:
    @staticmethod
    def parse_and_make_request(url: str, method: str, body: str, headers) -> dict:
        parsed_url = urlparse(url)
        response = MessageSender.make_request(parsed_url.netloc, parsed_url.path, method, body, headers,
                                                      parsed_url.scheme == "https")
        return response

    @staticmethod
    def make_request(endpoint: str, path: str, method: str, body: str, headers, ssl=True) -> dict:
        if ssl:
            conn = http.client.HTTPSConnection(endpoint)
        else:
            conn = http.client.HTTPConnection(endpoint)
        conn.request(method, path, body, headers)
        response = conn.getresponse().read().decode()

        if response == "Authentication Error":
            exit(click.secho(response, fg="red"))
        return response
