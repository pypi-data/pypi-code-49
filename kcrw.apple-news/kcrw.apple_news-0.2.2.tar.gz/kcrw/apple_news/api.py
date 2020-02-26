"""Library for making Apple News API requests"""
import base64
import hashlib
import hmac
import json
import logging
import os
import random
import requests
import six
from datetime import datetime


logger = logging.getLogger('kcrw.apple_news' + __name__)

EXT_MAPPING = {
    '.json': b'application/json',
    '.jpg': b'image/jpeg',
    '.jpeg': b'image/jpeg',
    '.gif': b'image/gif',
    '.png': b'image/png',
}


class AppleNewsError(Exception):
    """Exception class for errors related to Apple News API requests"""
    code = None
    data = None

    def __init__(self, *args, **kw):
        super(AppleNewsError, self).__init__(*args)
        if 'code' in kw:
            self.code = kw['code']
        if 'data' in kw:
            self.data = kw['data']


class API(object):
    """Apple News API object"""

    key_id = None
    key_secret = None
    channel_id = None
    url_base = 'https://news-api.apple.com'

    def __init__(self, key_id, key_secret, channel_id):
        """
        :param key_id: Apple News API Key Id
        :type key_id: str
        :param key_secret: Apple News API Secret
        :type key_secret: str
        :param channel_id: Apple News Channel Id
        :type channel_id: str

        """
        self.key_id = key_id
        self.key_secret = key_secret
        self.channel_id = channel_id

    def send_request(self, method, route, body=None, content_type=None):
        """Sends a signed request to the Apple News Publisher API.

        :param method: The HTTP method for the request (e.g. GET, POST, ...)
        :type method: str
        :param route: The API route for the request
        :type route: str
        :param body: The request body
        :type body: str
        :param content_type: The request content type
        :type content_type: str

        :returns: dict -- the JSON data returned by the API.
        :raises: AppleNewsException

        """
        date = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')
        url = self.url_base
        route = route.rstrip('/')
        if route:
            url = url + '/' + route
        canonical_request = (
            six.ensure_binary(method, 'utf8') +
            six.ensure_binary(url, 'utf8') +
            six.ensure_binary(date, 'utf8')
        )
        if body:
            canonical_request += (
                six.ensure_binary(content_type, 'utf8') +
                six.ensure_binary(body, 'utf8')
            )

        signature = self._create_signature(canonical_request)
        authorization = "HHMAC; key={}; signature={}; date={}".format(
            self.key_id, signature, date
        )
        headers = {"Authorization": authorization}
        if body:
            headers["Content-Type"] = content_type

        resp = data = code = reason = None
        try:
            resp = requests.request(method, url, headers=headers, data=body)
            resp.raise_for_status()
        except requests.exceptions.RequestException:
            logger.exception('Requests error')
            if resp is not None:
                data = resp.json()
                code = resp.status_code
                reason = resp.reason
            raise AppleNewsError(
                'Error during Apple News request to {} ({}: {})'.format(
                    url, code, reason
                ), code=code, data=data
            )
        if method != 'DELETE':
            return resp.json()
        else:
            return {'result': 'Deleted item at url: {}'.format(url)}

    def _create_signature(self, canonical_request):
        key_bytes = base64.b64decode(self.key_secret)
        message = canonical_request

        signature = base64.b64encode(
            hmac.new(key_bytes, message,
                     digestmod=hashlib.sha256).digest()
        )
        return signature

    def read_channel(self):
        """Read basic information about the current Apple News Channel

        :returns: dict -- the JSON data returned by the API.
        :raises: AppleNewsException

        """
        method = "GET"
        route = 'channels/' + self.channel_id
        return self.send_request(method, route)

    def create_article(self, article, metadata=None, assets=None):
        """Creates and uploads a multi-part article. See `Create an Article`_

        ``article`` and ``metadata`` should contain JSON-serializable
        dictionaries according the API specification for
        `article data`_ and optional `article creation metadata`_.
        ``assets`` should contain a dict mapping of filenames to file
        data for all supplemental assets needed for the article.

        :param article: Article data in JSON serializable python dict
        :type article: dict
        :param metadata: Optional metadata in JSON serializable python dict
        :type article: dict -- or None
        :param assets: Dict with filename -> data mapping of additional assets
        :type assets: dict -- or None

        :returns: dict -- the JSON data returned by the API.
        :raises: AppleNewsException

        .. _Create an Article: https://developer.apple.com/documentation/apple_news/create_an_article
        .. _article data: https://developer.apple.com/documentation/apple_news/articledocument
        .. _article creation metadata: https://developer.apple.com/documentation/apple_news/create_article_metadata_fields

        """  # noqa: E501
        if not article:
            raise AppleNewsError('No article body found for article')
        if assets:
            files = list(sorted(assets.items(),
                                key=lambda e: six.ensure_text(e[0], 'utf8')))
        else:
            files = []
        files.insert(0, ('article.json', json.dumps(article)))
        if metadata:
            files.insert(0, ('metadata', json.dumps(metadata)))
        body, content_type = self._build_article_body(files)
        method = "POST"
        route = 'channels/{}/articles'.format(self.channel_id)
        return self.send_request(method, route, body, content_type)

    def update_article(self, identifier, metadata, article=None, assets=None):
        """Updates an existing a article. See `Update an Article`_.

        Requires an ``identifier`` for an existing article, and `metadata`_
        containing the current article ``revision`` identifier. All
        other arguments are optional.

        :param identifier: An identifier for an existing Apple News article
        :type identifier: str
        :param metadata: JSON formatted article metadata
        :type metadata: dict
        :param article: Article data in JSON serializable python dict
        :type article: dict -- or None
        :param assets: Dict with filename -> data mapping of additional assets
        :type assets: dict -- or None

        :returns: dict -- the JSON data returned by the API.
        :raises: AppleNewsException

        .. _Update an Article: https://developer.apple.com/documentation/apple_news/update_an_article
        .. _metadata: https://developer.apple.com/documentation/apple_news/metadata

        """  # noqa: E501
        if not metadata or 'revision' not in metadata.get('data', {}):
            raise AppleNewsError(
                'No valid metadata data found for article update'
            )
        if assets:
            files = list(sorted(assets.items(),
                                key=lambda e: six.ensure_text(e[0], 'utf8')))
        else:
            files = []
        files.insert(0, ('metadata', json.dumps(metadata)))
        if article:
            files.insert(1, ('article.json', json.dumps(article)))
        body, content_type = self._build_article_body(files)
        method = "POST"
        path = "articles/{}".format(identifier)
        return self.send_request(method, path, body, content_type)

    def read_article(self, identifier):
        """Retrieves information about an existing a article.
        See `Read Article Information`_.

        Requires an ``identifier`` for an existing article.

        :param identifier: An identifier for an existing Apple News article
        :type identifier: str

        :returns: dict -- the JSON data returned by the API.
        :raises: AppleNewsException

        .. _Read Article Information: https://developer.apple.com/documentation/apple_news/read_article_information

        """  # noqa: E501
        method = "GET"
        path = "articles/{}".format(identifier)
        return self.send_request(method, path)

    def delete_article(self, identifier):
        """Deletes an existing a article. See `Delete an Article`_.

        Requires an ``identifier`` for an existing article.

        :param identifier: An identifier for an existing Apple News article
        :type identifier: str

        :returns: dict -- the JSON data returned by the API.
        :raises: AppleNewsException

        .. _Delete an Article: https://developer.apple.com/documentation/apple_news/delete_an_article

        """  # noqa: E501
        method = "DELETE"
        path = "articles/{}".format(identifier)
        return self.send_request(method, path)

    def _build_article_body(self, files):
        boundary = six.text_type(random.getrandbits(64))
        boundary = boundary.encode('utf8')
        content_type = b"multipart/form-data; boundary=%s" % boundary
        parts = filter(
            None, map(lambda f: self._build_mime_part(boundary, *f),
                      files)
        )
        body = b"\r\n".join(parts)
        body += b"\r\n--%s--" % boundary

        return body, content_type

    def _build_mime_part(self, boundary, filename, file_data):
        content_type = self._guess_content_type(filename)
        if content_type is None:
            return None
        filename = six.ensure_binary(filename, 'utf8')
        file_data = six.ensure_binary(file_data, 'utf8')
        content_type = content_type
        part = b"--%s\r\n" % boundary
        part += b"Content-Type: %s\r\n" % content_type
        f_size = len(file_data)
        part += b"Content-Disposition: form-data; filename=%s; size=%d\r\n\r\n" % (
            filename, f_size
        )
        part += file_data
        return part

    @staticmethod
    def _guess_content_type(filename):
        extension = os.path.splitext(filename)[-1].lower()
        if filename == 'metadata':
            return b"application/json"
        return EXT_MAPPING.get(extension, None)
