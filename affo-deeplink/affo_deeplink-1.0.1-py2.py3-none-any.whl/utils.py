from urllib.parse import (
    urlencode,
    urlparse,
    parse_qs,
    urlsplit,
    urlunsplit,
)


def urljoin(site, path):
    # FIXME: Hide unusual imports
    from urllib.parse import urljoin as abs_urljoin
    from posixpath import join as path_urljoin

    if isinstance(path, str):
        segments = [s for s in path.split("/") if s]
    else:
        segments = path  # assume list or tuple
    return abs_urljoin(site, path_urljoin(urlparse(site).path, *segments))


def set_query_parameter(url, param_name, param_value):
    """Given a URL, set or replace a query parameter and return the
    modified URL.

    >>> set_query_parameter('http://example.com?foo=bar&biz=baz', 'foo', 'stuff')
    'http://example.com?foo=stuff&biz=baz'

    """
    scheme, netloc, path, query_string, fragment = urlsplit(url)
    query_params = parse_qs(query_string)

    query_params[param_name] = [param_value]
    new_query_string = urlencode(query_params, doseq=True)

    return urlunsplit((scheme, netloc, path, new_query_string, fragment))
