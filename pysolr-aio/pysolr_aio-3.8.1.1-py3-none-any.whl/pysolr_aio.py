# -*- coding: utf-8 -*-

import ast
import asyncio
import datetime
import html.entities as htmlentities
import logging
import os
import random
import re
import time
from xml.etree import ElementTree
from pkg_resources import DistributionNotFound, get_distribution, parse_version
from urllib.parse import urlencode, quote

import httpx

try:
    from kazoo.client import KazooClient, KazooState
except ImportError:
    KazooClient = KazooState = None

try:
    # Prefer simplejson, if installed.
    import simplejson as json
except ImportError:
    import json


__author__ = 'Daniel Lindsley, Joseph Kocherhans, Jacob Kaplan-Moss'
__all__ = ['Solr']

try:
    pkg_distribution = get_distribution(__name__)
    __version__ = pkg_distribution.version
    version_info = pkg_distribution.parsed_version
except DistributionNotFound:
    __version__ = '0.0.dev0'
    version_info = parse_version(__version__)


def get_version():
    return __version__


DATETIME_REGEX = re.compile(
    r'^(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})T'
    r'(?P<hour>\d{2}):(?P<minute>\d{2}):(?P<second>\d{2})(\.\d+)?Z$')
# dict key used to add nested documents to a document
NESTED_DOC_KEY = '_childDocuments_'


class NullHandler(logging.Handler):
    def emit(self, record):
        pass


# Add the ``NullHandler`` to avoid logging by default while still allowing
# others to attach their own handlers.
LOG = logging.getLogger('pysolr_aio')
h = NullHandler()
LOG.addHandler(h)

# For debugging...
if os.environ.get('DEBUG_PYSOLR_AIO', '').lower() in ('true', '1'):
    LOG.setLevel(logging.DEBUG)
    stream = logging.StreamHandler()
    LOG.addHandler(stream)


def force_unicode(value):
    """
    Forces a bytestring to become a Unicode string.
    """
    if isinstance(value, bytes):
        value = value.decode('utf-8', errors='replace')
    elif not isinstance(value, str):
        value = str(value)

    return value


def force_bytes(value):
    """
    Forces a Unicode string to become a bytestring.
    """
    if isinstance(value, str):
        value = value.encode('utf-8', 'backslashreplace')

    return value


def unescape_html(text):
    """
    Removes HTML or XML character references and entities from a text string.

    @param text The HTML (or XML) source text.
    @return The plain text, as a Unicode string, if necessary.

    Source: http://effbot.org/zone/re-sub.htm#unescape-html
    """
    def fixup(m):
        txt = m.group(0)
        if txt[:2] == '&#':
            # character reference
            try:
                if txt[:3] == '&#x':
                    return chr(int(txt[3:-1], 16))
                else:
                    return chr(int(txt[2:-1]))
            except ValueError:
                pass
        else:
            # named entity
            try:
                txt = chr(htmlentities.name2codepoint[txt[1:-1]])
            except KeyError:
                pass
        return txt  # leave as is
    return re.sub(r'&#?\w+;', fixup, text)


def safe_urlencode(params, doseq=0):
    """
    UTF-8-safe version of safe_urlencode

    The stdlib safe_urlencode prior to Python 3.x chokes on UTF-8 values
    which can't fail down to ascii.
    """
    return urlencode(params, doseq=bool(doseq))


def is_valid_xml_char_ordinal(i):
    """
    Defines whether char is valid to use in xml document

    XML standard defines a valid char as::

    Char ::= #x9 | #xA | #xD | [#x20-#xD7FF] | [#xE000-#xFFFD] | [#x10000-#x10FFFF]     # NOQA
    """
    # conditions ordered by presumed frequency
    return (
            0x20 <= i <= 0xD7FF
            or i in (0x9, 0xA, 0xD)
            or 0xE000 <= i <= 0xFFFD
            or 0x10000 <= i <= 0x10FFFF
    )


def clean_xml_string(s):
    """
    Cleans string from invalid xml chars

    Solution was found there::

    http://stackoverflow.com/questions/8733233/filtering-out-certain-bytes-in-python    # NOQA
    """
    return ''.join(c for c in s if is_valid_xml_char_ordinal(ord(c)))


class SolrError(Exception):
    pass


class Results(object):
    """
    Default results class for wrapping decoded (from JSON) solr responses.

    Required ``decoded`` argument must be a Solr response dictionary.
    Individual documents can be retrieved either through ``docs`` attribute
    or by iterating over results instance.

    Example::

        results = Results({
            'response': {
                'docs': [{'id': 1}, {'id': 2}, {'id': 3}],
                'numFound': 3,
            }
        })

        # this:
        for doc in results:
            print doc

        # ... is equivalent to:
        for doc in results.docs:
            print doc

        # also:
        list(results) == results.docs

    Note that ``Results`` object does not support indexing and slicing. If you
    need to retrieve documents by index just use ``docs`` attribute.

    Other common response metadata (debug, highlighting, qtime, etc.)
    are available as attributes.

    The full response from Solr is provided as the `raw_response` dictionary
    for use with features which change the response format.
    """

    def __init__(self, decoded):
        self.raw_response = decoded

        # main response part of decoded Solr response
        response_part = decoded.get('response') or {}
        self.docs = response_part.get('docs', ())
        self.hits = response_part.get('numFound', 0)

        # other response metadata
        self.debug = decoded.get('debug', {})
        self.highlighting = decoded.get('highlighting', {})
        self.facets = decoded.get('facet_counts', {})
        self.spellcheck = decoded.get('spellcheck', {})
        self.stats = decoded.get('stats', {})
        self.qtime = decoded.get('responseHeader', {}).get('QTime', None)
        self.grouped = decoded.get('grouped', {})
        self.nextCursorMark = decoded.get('nextCursorMark', None)

    def __len__(self):
        return len(self.docs)

    def __iter__(self):
        return iter(self.docs)


class Solr(object):
    """
    The main object for working with Solr.

    Optionally accepts ``decoder`` for an alternate JSON decoder instance.
    Default is ``json.JSONDecoder()``.

    Optionally accepts ``timeout`` for wait seconds until giving up on a
    request. Default is ``60`` seconds.

    Optionally accepts ``results_cls`` that specifies class of results object
    returned by ``.search()`` and ``.more_like_this()`` methods.
    Default is ``pysolr_aio.Results``.

    Usage::

        solr = pysolr_aio.Solr('http://localhost:8983/solr')
        # With a 10 second timeout.
        solr = pysolr_aio.Solr('http://localhost:8983/solr', timeout=10)

        # with a dict as a default results class instead of pysolr_aio.Results
        solr = pysolr_aio.Solr('http://localhost:8983/solr', results_cls=dict)

    """

    def __init__(self, url, decoder=None, timeout=60, results_cls=Results,
                 search_handler='select', use_qt_param=False,
                 always_commit=False, auth=None, verify=True):
        self.decoder = decoder or json.JSONDecoder()
        self.url = url
        self.timeout = timeout
        self.log = self._get_log()
        self.http_client = None
        self.results_cls = results_cls
        self.search_handler = search_handler
        self.use_qt_param = use_qt_param
        self.auth = auth
        self.verify = verify
        self.always_commit = always_commit

    def get_http_client(self):
        if self.http_client is None:
            self.http_client = httpx.AsyncClient(verify=self.verify)
        return self.http_client

    @staticmethod
    def _get_log():
        return LOG

    def _create_full_url(self, path=''):
        if len(path):
            return '/'.join([self.url.rstrip('/'), path.lstrip('/')])

        # No path? No problem.
        return self.url

    async def _send_request(self, method, path='', body=None, headers=None,
                            files=None):
        url = self._create_full_url(path)
        method = method.lower()
        log_body = body

        if headers is None:
            headers = {}

        if log_body is None:
            log_body = ''
        elif not isinstance(log_body, str):
            log_body = repr(body)

        self.log.debug("Starting request to '%s' (%s) with body '%s'...",
                       url, method, log_body[:10])
        start_time = time.time()

        http_client = self.get_http_client()

        try:
            requests_method = getattr(http_client, method)
        except AttributeError:
            raise SolrError(f"Unable to use unknown HTTP method '{method}'.")

        # Everything except the body can be Unicode. The body must be
        # encoded to bytes to work properly on Py3.
        bytes_body = body

        if bytes_body is not None:
            bytes_body = force_bytes(body)
        try:
            if method == 'get':
                resp = await requests_method(
                    url, params=bytes_body, headers=headers,
                    timeout=self.timeout, auth=self.auth)
            else:
                resp = await requests_method(
                    url, data=bytes_body, headers=headers, files=files,
                    timeout=self.timeout, auth=self.auth)
        except httpx.exceptions.TimeoutException as err:
            error_message = "Connection to server '%s' timed out: %s"
            self.log.error(error_message, url, err, exc_info=True)
            raise SolrError(error_message % (url, err))     # NOQA
        except httpx.exceptions.HTTPError as err:
            error_message = ("Failed to connect to server at '%s', "
                             'are you sure that URL is correct? '
                             'Checking it in a browser might help: %s')
            params = (url, err)
            self.log.error(error_message, *params, exc_info=True)
            raise SolrError(error_message % params)         # NOQA
        except Exception as err:
            error_message = 'Unhandled error: %s %s: %s'
            self.log.error(error_message, method, url, err, exc_info=True)
            raise SolrError(error_message % (method, url, err))     # NOQA

        end_time = time.time()
        self.log.info(
            "Finished '%s' (%s) with body '%s' in %0.3f seconds, "
            'with status %s',
            url, method, log_body[:10], end_time - start_time,
            resp.status_code)

        if int(resp.status_code) != 200:
            error_message = 'Solr responded with an error (HTTP %s): %s'
            solr_message = self._extract_error(resp)
            self.log.error(error_message, resp.status_code, solr_message,
                           extra={'data': {'headers': resp.headers,
                                           'response': resp.content,
                                           'request_body': bytes_body,
                                           'request_headers': headers}})
            raise SolrError(error_message % (resp.status_code, solr_message))   # NOQA

        return force_unicode(resp.content)

    async def _select(self, params, handler=None):
        """
        :param params:
        :param handler: defaults to self.search_handler (fallback to 'select')
        :return:
        """
        # specify json encoding of results
        params['wt'] = 'json'
        custom_handler = handler or self.search_handler
        handler = 'select'
        if custom_handler:
            if self.use_qt_param:
                params['qt'] = custom_handler
            else:
                handler = custom_handler

        params_encoded = safe_urlencode(params, True)

        if len(params_encoded) < 1024:
            # Typical case.
            path = f'{handler}/?{params_encoded}'
            return await self._send_request('get', path)
        else:
            # Handles very long queries by submitting as a POST.
            path = f'{handler}/'
            headers = {
                'Content-type': ('application/x-www-form-urlencoded; '
                                 'charset=utf-8'),
            }
            return await self._send_request(
                'post', path, body=params_encoded, headers=headers)

    async def _mlt(self, params, handler='mlt'):
        return await self._select(params, handler)

    async def _suggest_terms(self, params, handler='terms'):
        return await self._select(params, handler)

    async def _update(self, message, clean_ctrl_chars=True, commit=None,
                      softCommit=False, waitFlush=None, waitSearcher=None,      # NOQA
                      overwrite=None, handler='update'):
        """
        Posts the given xml message to http://<self.url>/update and
        returns the result.

        Passing `clean_ctrl_chars` as False will prevent the message from being
        cleaned of control characters (default True). This is done by default
        because these characters would cause Solr to fail to parse the XML.
        Only pass False if you're positive your data is clean.
        """

        # Per http://wiki.apache.org/solr/UpdateXmlMessages, we can append a
        # ``commit=true`` to the URL and have the commit happen without a
        # second request.
        query_vars = []

        path_handler = handler
        if self.use_qt_param:
            path_handler = 'select'
            query_vars.append(f'qt={safe_urlencode(handler, True)}')

        path = f'{path_handler}/'

        if commit is None:
            commit = self.always_commit

        if commit:
            query_vars.append(f'commit={str(bool(commit)).lower()}')
        elif softCommit:
            query_vars.append(f'softCommit={str(bool(softCommit)).lower()}')

        if waitFlush is not None:
            query_vars.append(f'waitFlush={str(bool(waitFlush)).lower()}')

        if overwrite is not None:
            query_vars.append(f'overwrite={str(bool(overwrite)).lower()}')

        if waitSearcher is not None:
            query_vars.append(
                f'waitSearcher={str(bool(waitSearcher)).lower()}')

        if query_vars:
            path = f'{path}?{"&".join(query_vars)}'

        # Clean the message of ctrl characters.
        if clean_ctrl_chars:
            message = sanitize(message)

        return await self._send_request(
            'post', path, message, {'Content-type': 'text/xml; charset=utf-8'})

    def _extract_error(self, resp):
        """
        Extract the actual error message from a solr response.
        """
        reason = resp.headers.get('reason', None)
        full_response = None

        if reason is None:
            try:
                # if response is in json format
                reason = resp.json()['error']['msg']
            except KeyError:
                # if json response has unexpected structure
                full_response = resp.content
            except ValueError:
                # otherwise we assume it's html
                reason, full_html = self._scrape_response(
                    resp.headers, resp.content)
                full_response = unescape_html(full_html)

        msg = f'[Reason: {reason}]'

        if reason is None:
            msg += f'\n{full_response}'

        return msg

    @staticmethod
    def _scrape_response(headers, response):
        """
        Scrape the html response.
        """
        # identify the responding server
        server_type = None
        server_string = headers.get('server', '')

        if server_string and 'jetty' in server_string.lower():
            server_type = 'jetty'

        if server_string and 'coyote' in server_string.lower():
            server_type = 'tomcat'

        reason = None
        full_html = ''

        # In Python3, response can be made of bytes
        if hasattr(response, 'decode'):
            response = response.decode()
        if response.startswith('<?xml'):
            # Try a strict XML parse
            try:
                soup = ElementTree.fromstring(response)

                reason_node = soup.find('lst[@name="error"]/str[@name="msg"]')
                tb_node = soup.find('lst[@name="error"]/str[@name="trace"]')
                if reason_node is not None:
                    full_html = reason = reason_node.text.strip()
                if tb_node is not None:
                    full_html = tb_node.text.strip()
                    if reason is None:
                        reason = full_html

                # Since we had a precise match, we'll return the results now:
                if reason and full_html:
                    return reason, full_html
            except ElementTree.ParseError:
                # XML parsing error,
                # so we'll let the more liberal code handle it.
                pass

        if server_type == 'tomcat':
            # Tomcat doesn't produce a valid XML response or consistent HTML:
            m = re.search(
                r'<(h1)[^>]*>\s*(.+?)\s*</\1>', response, re.IGNORECASE)
            if m:
                reason = m.group(2)
            else:
                full_html = f'{response}'
        else:
            # Let's assume others do produce a valid XML response
            try:
                dom_tree = ElementTree.fromstring(response)
                reason_node = None

                # html page might be different for every server
                if server_type == 'jetty':
                    reason_node = dom_tree.find('body/pre')
                else:
                    reason_node = dom_tree.find('head/title')

                if reason_node is not None:
                    reason = reason_node.text

                if reason is None:
                    full_html = ElementTree.tostring(dom_tree)
            except SyntaxError as err:
                LOG.warning(
                    'Unable to extract error message from invalid XML: %s',
                    err, extra={'data': {'response': response}})
                full_html = f'{response}'

        full_html = force_unicode(full_html)
        full_html = full_html.replace('\n', '')
        full_html = full_html.replace('\r', '')
        full_html = full_html.replace('<br/>', '')
        full_html = full_html.replace('<br />', '')
        full_html = full_html.strip()
        return reason, full_html

    # Conversion #############################################################

    @staticmethod
    def _from_python(value):
        """
        Converts python values to a form suitable for insertion into the xml
        we send to solr.
        """
        if hasattr(value, 'strftime'):
            if hasattr(value, 'hour'):
                offset = value.utcoffset()
                if offset:
                    value = value - offset
                value = value.replace(tzinfo=None).isoformat() + 'Z'
            else:
                value = f'{value.isoformat()}T00:00:00Z'
        elif isinstance(value, bool):
            if value:
                value = 'true'
            else:
                value = 'false'
        else:
            if isinstance(value, bytes):
                value = str(value, errors='replace')

            value = f'{value}'

        return clean_xml_string(value)

    @staticmethod
    def _to_python(value):
        """
        Converts values from Solr to native Python values.
        """
        if isinstance(value, (int, float, complex)):
            return value

        if isinstance(value, (list, tuple)):
            value = value[0]

        if value == 'true':
            return True
        elif value == 'false':
            return False

        is_string = False

        if isinstance(value, bytes):
            value = force_unicode(value)

        if isinstance(value, str):
            is_string = True

        if is_string:
            possible_datetime = DATETIME_REGEX.search(value)

            if possible_datetime:
                date_values = possible_datetime.groupdict()

                for dk, dv in date_values.items():
                    date_values[dk] = int(dv)

                return datetime.datetime(
                    date_values['year'], date_values['month'],
                    date_values['day'], date_values['hour'],
                    date_values['minute'], date_values['second'])

        try:
            # This is slightly gross but it's hard to tell otherwise what the
            # string's original type might have been.
            return ast.literal_eval(value)
        except (ValueError, SyntaxError):
            # If it fails, continue on.
            pass

        return value

    @staticmethod
    def _is_null_value(value):
        """
        Check if a given value is ``null``.

        Criteria for this is based on values that shouldn't be included
        in the Solr ``add`` request at all.
        """
        if value is None:
            return True

        if isinstance(value, str) and len(value) == 0:
            return True

        # TODO: This should probably be removed when solved in core Solr level?
        return False

    # API Methods ############################################################

    async def search(self, q, search_handler=None, **kwargs):
        """
        Performs a search and returns the results.

        Requires a ``q`` for a string version of the query to run.

        Optionally accepts ``**kwargs`` for additional options to be passed
        through the Solr URL.

        Returns ``self.results_cls`` class object (defaults to
        ``pysolr_aio.Results``)

        Usage::

            # All docs.
            results = solr.search('*:*')

            # Search with highlighting.
            results = solr.search('ponies', **{
                'hl': 'true',
                'hl.fragsize': 10,
            })

        """
        params = {'q': q}
        params.update(kwargs)
        response = await self._select(params, handler=search_handler)
        decoded = self.decoder.decode(response)

        self.log.debug(
            "Found '%s' search results.",
            # cover both cases: there is no response key or value is None
            (decoded.get('response', {}) or {}).get('numFound', 0))
        return self.results_cls(decoded)

    async def more_like_this(self, q, mltfl, handler='mlt', **kwargs):
        """
        Finds and returns results similar to the provided query.

        Returns ``self.results_cls`` class object (defaults to
        ``pysolr_aio.Results``)

        Requires Solr 1.3+.

        Usage::

            similar = solr.more_like_this('id:doc_234', 'text')

        """
        params = {
            'q': q,
            'mlt.fl': mltfl,
        }
        params.update(kwargs)
        response = await self._mlt(params, handler=handler)
        decoded = self.decoder.decode(response)

        self.log.debug(
            "Found '%s' MLT results.",
            # cover both cases: there is no response key or value is None
            (decoded.get('response', {}) or {}).get('numFound', 0))
        return self.results_cls(decoded)

    async def suggest_terms(self, fields, prefix, handler='terms', **kwargs):
        """
        Accepts a list of field names and a prefix

        Returns a dictionary keyed on field name containing a list of
        ``(term, count)`` pairs

        Requires Solr 1.4+.
        """
        params = {
            'terms.fl': fields,
            'terms.prefix': prefix,
        }
        params.update(kwargs)
        response = await self._suggest_terms(params, handler=handler)
        result = self.decoder.decode(response)
        terms = result.get('terms', {})
        res = {}

        # in Solr 1.x the value of terms is a flat list:
        #   ["field_name", ["dance",23,"dancers",10,"dancing",8,"dancer",6]]
        #
        # in Solr 3.x the value of terms is a dict:
        #   {"field_name": ["dance",23,"dancers",10,"dancing",8,"dancer",6]}
        if isinstance(terms, (list, tuple)):
            terms = dict(zip(terms[0::2], terms[1::2]))

        for field, values in terms.items():
            tmp = list()

            while values:
                tmp.append((values.pop(0), values.pop(0)))

            res[field] = tmp

        self.log.debug("Found '%d' Term suggestions results.",
                       sum(len(j) for i, j in res.items()))
        return res

    def _build_doc(self, doc, boost=None, fieldUpdates=None):   # NOQA
        doc_elem = ElementTree.Element('doc')

        for key, value in doc.items():
            if key == NESTED_DOC_KEY:
                for child in value:
                    doc_elem.append(
                        self._build_doc(child, boost, fieldUpdates))
                continue

            if key == 'boost':
                doc_elem.set('boost', force_unicode(value))
                continue

            # To avoid multiple code-paths we'd like to treat
            # all of our values as iterables:
            if isinstance(value, (list, tuple, set)):
                values = value
            else:
                values = (value, )

            for bit in values:
                if self._is_null_value(bit):
                    continue

                if key == '_doc':
                    child = self._build_doc(bit, boost)
                    doc_elem.append(child)
                    continue

                attrs = {'name': key}

                if fieldUpdates and key in fieldUpdates:
                    attrs['update'] = fieldUpdates[key]

                if boost and key in boost:
                    attrs['boost'] = force_unicode(boost[key])

                field = ElementTree.Element('field', **attrs)
                field.text = self._from_python(bit)

                doc_elem.append(field)

        return doc_elem

    async def add(self, docs, boost=None, fieldUpdates=None, commit=None,       # NOQA
                  softCommit=False, commitWithin=None, waitFlush=None,          # NOQA
                  waitSearcher=None, overwrite=None, handler='update'):         # NOQA
        """
        Adds or updates documents.

        Requires ``docs``, which is a list of dictionaries. Each key is the
        field name and each value is the value to index.

        Optionally accepts ``commit``. Default is ``None``.
        None signals to use default

        Optionally accepts ``softCommit``. Default is ``False``.

        Optionally accepts ``boost``. Default is ``None``.

        Optionally accepts ``fieldUpdates``. Default is ``None``.

        Optionally accepts ``commitWithin``. Default is ``None``.

        Optionally accepts ``waitFlush``. Default is ``None``.

        Optionally accepts ``waitSearcher``. Default is ``None``.

        Optionally accepts ``overwrite``. Default is ``None``.

        Usage::

            solr.add([
                {
                    "id": "doc_1",
                    "title": "A test document",
                },
                {
                    "id": "doc_2",
                    "title": "The Banana: Tasty or Dangerous?",
                },
            ])
        """
        start_time = time.time()
        self.log.debug('Starting to build add request...')
        message = ElementTree.Element('add')

        if commitWithin:
            message.set('commitWithin', commitWithin)

        for doc in docs:
            el = self._build_doc(doc, boost=boost, fieldUpdates=fieldUpdates)
            message.append(el)

        # This returns a bytestring. Ugh.
        m = ElementTree.tostring(message, encoding='utf-8')
        # Convert back to Unicode please.
        m = force_unicode(m)

        end_time = time.time()
        self.log.debug('Built add request of %s docs in %0.2f seconds.',
                       len(message), end_time - start_time)
        return await self._update(
            m, commit=commit, softCommit=softCommit, waitFlush=waitFlush,
            waitSearcher=waitSearcher, overwrite=overwrite, handler=handler)

    async def delete(self, id=None, q=None, commit=None, softCommit=False,      # NOQA
                     waitFlush=None, waitSearcher=None, handler='update'):      # NOQA
        """
        Deletes documents.

        Requires *either* ``id`` or ``query``. ``id`` is if you know the
        specific document id to remove. Note that ``id`` can also be a list of
        document ids to be deleted. ``query`` is a Lucene-style query
        indicating a collection of documents to delete.

        Optionally accepts ``commit``. Default is ``True``.

        Optionally accepts ``softCommit``. Default is ``False``.

        Optionally accepts ``waitFlush``. Default is ``None``.

        Optionally accepts ``waitSearcher``. Default is ``None``.

        Usage::

            solr.delete(id='doc_12')
            solr.delete(id=['doc_1', 'doc_3'])
            solr.delete(q='*:*')

        """
        if id is None and q is None:
            raise ValueError('You must specify "id" or "q".')
        if id is not None and q is not None:
            raise ValueError('You many only specify "id" OR "q", not both.')
        if id is not None:
            if not isinstance(id, (list, set, tuple)):
                id_list = [id]
            else:
                id_list = list(filter(None, id))
            if id_list:
                m = '<delete>{}</delete>'.format(
                    ''.join('<id>{}</id>'.format(i) for i in id_list))
            else:
                raise ValueError('The list of documents to delete was empty.')
        elif q is not None:
            m = f'<delete><query>{q}</query></delete>'

        return await self._update(
            m, commit=commit, softCommit=softCommit, waitFlush=waitFlush,
            waitSearcher=waitSearcher, handler=handler)

    async def commit(self, softCommit=False, waitFlush=None, waitSearcher=None, # NOQA
                     expungeDeletes=None, handler='update'):                    # NOQA
        """
        Forces Solr to write the index data to disk.

        Optionally accepts ``expungeDeletes``. Default is ``None``.

        Optionally accepts ``waitFlush``. Default is ``None``.

        Optionally accepts ``waitSearcher``. Default is ``None``.

        Optionally accepts ``softCommit``. Default is ``False``.

        Usage::

            solr.commit()

        """
        if expungeDeletes is not None:
            msg = ('<commit expungeDeletes='
                   f'"{str(bool(expungeDeletes)).lower()}" />')
        else:
            msg = '<commit />'

        return await self._update(
            msg, commit=not softCommit, softCommit=softCommit,
            waitFlush=waitFlush, waitSearcher=waitSearcher, handler=handler)

    async def optimize(self, commit=True, waitFlush=None, waitSearcher=None,    # NOQA
                       maxSegments=None, handler='update'):                     # NOQA
        """
        Tells Solr to streamline the number of segments used, essentially a
        defragmentation operation.

        Optionally accepts ``maxSegments``. Default is ``None``.

        Optionally accepts ``waitFlush``. Default is ``None``.

        Optionally accepts ``waitSearcher``. Default is ``None``.

        Usage::

            solr.optimize()

        """
        if maxSegments:
            msg = f'<optimize maxSegments="{maxSegments}" />'
        else:
            msg = '<optimize />'

        return await self._update(msg, commit=commit, waitFlush=waitFlush,
                                  waitSearcher=waitSearcher, handler=handler)

    async def extract(self, file_obj, extractOnly=True, handler='update/extract',     # NOQA
                      **kwargs):
        """
        POSTs a file to the Solr ExtractingRequestHandler so rich content can
        be processed using Apache Tika. See the Solr wiki for details:

            http://wiki.apache.org/solr/ExtractingRequestHandler

        The ExtractingRequestHandler has a very simple model: it extracts
        contents and metadata from the uploaded file and inserts it directly
        into the index. This is rarely useful as it allows no way to store
        additional data or otherwise customize the record. Instead, by default
        we'll use the extract-only mode to extract the data without indexing it
        so the caller has the opportunity to process it as appropriate; call
        with ``extractOnly=False`` if you want to insert with no additional
        processing.

        Returns None if metadata cannot be extracted; otherwise returns a
        dictionary containing at least two keys:

            :contents:
                        Extracted full-text content, if applicable
            :metadata:
                        key:value pairs of text strings
        """
        if not hasattr(file_obj, 'name'):
            raise ValueError('extract() requires file-like objects '
                             'which have a defined name property')

        params = {
            'extractOnly': 'true' if extractOnly else 'false',
            'lowernames': 'true',
            'wt': 'json',
        }
        params.update(kwargs)
        filename = quote(file_obj.name.encode('utf-8'))
        try:
            # We'll provide the file using its true name as Tika may use that
            # as a file type hint:
            resp = await self._send_request(
                'post', handler, body=params,
                files={'file': (filename, file_obj)})
        except (IOError, SolrError) as err:
            self.log.error('Failed to extract document metadata: %s', err,
                           exc_info=True)
            raise

        try:
            data = json.loads(resp)
        except ValueError as err:
            self.log.error('Failed to load JSON response: %s', err,
                           exc_info=True)
            raise

        data['contents'] = data.pop(filename, None)
        data['metadata'] = metadata = {}

        raw_metadata = data.pop(f'{filename}_metadata', None)

        if raw_metadata:
            # The raw format is somewhat annoying: it's a flat list of
            # alternating keys and value lists
            while raw_metadata:
                metadata[raw_metadata.pop()] = raw_metadata.pop()

        return data


class SolrCoreAdmin(object):
    """
    Handles core admin operations: see http://wiki.apache.org/solr/CoreAdmin

    This must be initialized with the full admin cores URL::

        solr_admin = SolrCoreAdmin('http://localhost:8983/solr/admin/cores')
        status = solr_admin.status()

    Operations offered by Solr are:
       1. STATUS
       2. CREATE
       3. RELOAD
       4. RENAME
       5. ALIAS
       6. SWAP
       7. UNLOAD
       8. LOAD (not currently implemented)
    """
    def __init__(self, url, *args, **kwargs):
        super(SolrCoreAdmin, self).__init__(*args, **kwargs)
        self.url = url

    async def _get_url(self, url, params=None, headers=None):
        params = params or dict()
        headers = headers or dict()
        resp = await httpx.get(
            url, params=safe_urlencode(params), headers=headers)
        return force_unicode(resp.content)

    async def status(self, core=None):
        """
        http://wiki.apache.org/solr/CoreAdmin
        #head-9be76f5a459882c5c093a7a1456e98bea7723953
        """
        params = {
            'action': 'STATUS',
        }

        if core is not None:
            params.update(core=core)

        return await self._get_url(self.url, params=params)

    async def create(self, name, instance_dir=None, config='solrconfig.xml',
                     schema='schema.xml'):
        """
        http://wiki.apache.org/solr/CoreAdmin
        #head-7ca1b98a9df8b8ca0dcfbfc49940ed5ac98c4a08
        """
        params = {
            'action': 'CREATE',
            'name': name,
            'config': config,
            'schema': schema,
        }

        if instance_dir is None:
            params.update(instanceDir=name)
        else:
            params.update(instanceDir=instance_dir)

        return await self._get_url(self.url, params=params)

    async def reload(self, core):
        """
        http://wiki.apache.org/solr/CoreAdmin
        #head-3f125034c6a64611779442539812067b8b430930
        """
        params = {
            'action': 'RELOAD',
            'core': core,
        }
        return await self._get_url(self.url, params=params)

    async def rename(self, core, other):
        """
        http://wiki.apache.org/solr/CoreAdmin
        #head-9473bee1abed39e8583ba45ef993bebb468e3afe
        """
        params = {
            'action': 'RENAME',
            'core': core,
            'other': other,
        }
        return await self._get_url(self.url, params=params)

    async def swap(self, core, other):
        """
        http://wiki.apache.org/solr/CoreAdmin
        #head-928b872300f1b66748c85cebb12a59bb574e501b
        """
        params = {
            'action': 'SWAP',
            'core': core,
            'other': other,
        }
        return await self._get_url(self.url, params=params)

    async def unload(self, core):
        """
        http://wiki.apache.org/solr/CoreAdmin
        #head-f5055a885932e2c25096a8856de840b06764d143
        """
        params = {
            'action': 'UNLOAD',
            'core': core,
        }
        return await self._get_url(self.url, params=params)

    def load(self, core):
        raise NotImplementedError(
            'Solr 1.4 and below do not support this operation.')


# Using two-tuples to preserve order.
REPLACEMENTS = (
    # Nuke nasty control characters.
    (b'\x00', b''),  # Start of heading
    (b'\x01', b''),  # Start of heading
    (b'\x02', b''),  # Start of text
    (b'\x03', b''),  # End of text
    (b'\x04', b''),  # End of transmission
    (b'\x05', b''),  # Enquiry
    (b'\x06', b''),  # Acknowledge
    (b'\x07', b''),  # Ring terminal bell
    (b'\x08', b''),  # Backspace
    (b'\x0b', b''),  # Vertical tab
    (b'\x0c', b''),  # Form feed
    (b'\x0e', b''),  # Shift out
    (b'\x0f', b''),  # Shift in
    (b'\x10', b''),  # Data link escape
    (b'\x11', b''),  # Device control 1
    (b'\x12', b''),  # Device control 2
    (b'\x13', b''),  # Device control 3
    (b'\x14', b''),  # Device control 4
    (b'\x15', b''),  # Negative acknowledge
    (b'\x16', b''),  # Synchronous idle
    (b'\x17', b''),  # End of transmission block
    (b'\x18', b''),  # Cancel
    (b'\x19', b''),  # End of medium
    (b'\x1a', b''),  # Substitute character
    (b'\x1b', b''),  # Escape
    (b'\x1c', b''),  # File separator
    (b'\x1d', b''),  # Group separator
    (b'\x1e', b''),  # Record separator
    (b'\x1f', b''),  # Unit separator
)


def sanitize(data):
    fixed_string = force_bytes(data)

    for bad, good in REPLACEMENTS:
        fixed_string = fixed_string.replace(bad, good)

    return force_unicode(fixed_string)


class SolrCloud(Solr):

    def __init__(self, zookeeper, collection, decoder=None, timeout=60,
                 retry_timeout=0.2, auth=None, verify=True, *args, **kwargs):
        url = zookeeper.getRandomURL(collection)
        self.auth = auth
        self.verify = verify

        super(SolrCloud, self).__init__(url, decoder=decoder, timeout=timeout,
                                        auth=self.auth, verify=self.verify,
                                        *args, **kwargs)

        self.zookeeper = zookeeper
        self.collection = collection
        self.retry_timeout = retry_timeout

    async def _randomized_request(self, method, path, body, headers, files):
        self.url = self.zookeeper.getRandomURL(self.collection)
        LOG.debug('Using random URL: %s', self.url)
        return await Solr._send_request(
            self, method, path, body, headers, files)

    async def _send_request(self, method, path='', body=None, headers=None,
                            files=None):
        # FIXME: this needs to have a maximum retry counter
        #  rather than waiting endlessly
        try:
            return await self._randomized_request(method, path, body, headers,
                                                  files)
        except httpx.exceptions.HTTPError:
            LOG.warning('RequestException, retrying after %fs',
                        self.retry_timeout, exc_info=True)
            # give zookeeper time to notice
            await asyncio.sleep(self.retry_timeout)
            return await self._randomized_request(
                method, path, body, headers, files)
        except SolrError:
            LOG.warning('SolrException, retrying after %fs',
                        self.retry_timeout, exc_info=True)
            # give zookeeper time to notice
            await asyncio.sleep(self.retry_timeout)
            return await self._randomized_request(
                method, path, body, headers, files)

    async def _update(self, *args, **kwargs):
        self.url = self.zookeeper.getLeaderURL(self.collection)
        LOG.debug('Using random leader URL: %s', self.url)
        return await Solr._update(self, *args, **kwargs)


class ZooKeeper(object):
    # Constants used by the REST API:
    LIVE_NODES_ZKNODE = '/live_nodes'
    ALIASES = '/aliases.json'
    CLUSTER_STATE = '/clusterstate.json'
    SHARDS = 'shards'
    REPLICAS = 'replicas'
    STATE = 'state'
    ACTIVE = 'active'
    LEADER = 'leader'
    BASE_URL = 'base_url'
    TRUE = 'true'
    FALSE = 'false'
    COLLECTION = 'collection'

    def __init__(self, zkServerAddress, timeout=15, max_retries=-1,     # NOQA
                 kazoo_client=None):
        if KazooClient is None:
            logging.error(
                'ZooKeeper requires the `kazoo` library to be installed')
            raise RuntimeError

        self.collections = {}
        self.liveNodes = {}
        self.aliases = {}
        self.state = None

        if kazoo_client is None:
            self.zk = KazooClient(
                zkServerAddress, read_only=True, timeout=timeout,
                command_retry={'max_tries': max_retries},
                connection_retry={'max_tries': max_retries})
        else:
            self.zk = kazoo_client

        self.zk.start()

        def connectionListener(state):  # NOQA
            if state == KazooState.LOST:
                self.state = state
            elif state == KazooState.SUSPENDED:
                self.state = state
        self.zk.add_listener(connectionListener)

        @self.zk.DataWatch(ZooKeeper.CLUSTER_STATE)
        def watchClusterState(data, *args, **kwargs):   # NOQA
            if not data:
                LOG.warning(
                    'No cluster state available: no collections defined?')
            else:
                self.collections = json.loads(data.decode('utf-8'))
                LOG.info('Updated collections: %s', self.collections)

        @self.zk.ChildrenWatch(ZooKeeper.LIVE_NODES_ZKNODE)
        def watchLiveNodes(children):   # NOQA
            self.liveNodes = children
            LOG.info('Updated live nodes: %s', children)

        @self.zk.DataWatch(ZooKeeper.ALIASES)
        def watchAliases(data, stat):   # NOQA
            if data:
                json_data = json.loads(data.decode('utf-8'))
                if ZooKeeper.COLLECTION in json_data:
                    self.aliases = json_data[ZooKeeper.COLLECTION]
                else:
                    LOG.warning('Expected to find %s in alias update %s',
                                ZooKeeper.COLLECTION, json_data.keys())
            else:
                self.aliases = None
            LOG.info('Updated aliases: %s', self.aliases)

    def getHosts(self, collname, only_leader=False, seen_aliases=None):     # NOQA
        if self.aliases and collname in self.aliases:
            return self.getAliasHosts(collname, only_leader, seen_aliases)

        hosts = []
        if collname not in self.collections:
            raise SolrError(f'Unknown collection: {collname}')
        collection = self.collections[collname]
        shards = collection[ZooKeeper.SHARDS]
        for shardname in shards.keys():
            shard = shards[shardname]
            if shard[ZooKeeper.STATE] == ZooKeeper.ACTIVE:
                replicas = shard[ZooKeeper.REPLICAS]
                for replicaname in replicas.keys():
                    replica = replicas[replicaname]

                    if replica[ZooKeeper.STATE] == ZooKeeper.ACTIVE:
                        leader = replica.get(ZooKeeper.LEADER, None)
                        if not only_leader or (leader == ZooKeeper.TRUE):
                            base_url = replica[ZooKeeper.BASE_URL]
                            if base_url not in hosts:
                                hosts.append(base_url)
        return hosts

    def getAliasHosts(self, collname, only_leader, seen_aliases):   # NOQA
        if seen_aliases:
            if collname in seen_aliases:
                LOG.warn('%s in circular alias definition - ignored', collname)
                return []
        else:
            seen_aliases = []
        seen_aliases.append(collname)
        collections = self.aliases[collname].split(',')
        hosts = []
        for collection in collections:
            for host in self.getHosts(collection, only_leader, seen_aliases):
                if host not in hosts:
                    hosts.append(host)
        return hosts

    def getRandomURL(self, collname, only_leader=False):    # NOQA
        hosts = self.getHosts(collname, only_leader=only_leader)
        if not hosts:
            raise SolrError('ZooKeeper returned no active shards!')
        return f'{random.choice(hosts)}/{collname}'

    def getLeaderURL(self, collname):   # NOQA
        return self.getRandomURL(collname, only_leader=True)
