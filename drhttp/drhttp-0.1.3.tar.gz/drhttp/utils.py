try:
    from urllib.parse import quote as quote
except ImportError:
    from urllib import pathname2url as quote
    
def extract_user_from_response_headers(headers, user_header_key):
    # Returns the tupe : user value, headers without user
    user = None
    for k, v in headers.items():
        if k.lower() == user_header_key.lower():
            user = v
            del headers[k]
            break
    return user, headers

def format_header_name(header):
    # HTTP_EXAMPLE_header -> Example-Header
    prefix = 'HTTP_'
    if header.startswith(prefix):
        header = header[len(prefix):]
    return header.replace('_', '-').capitalize()
    
def url_from_wsgi_env(environ):
    url = environ['wsgi.url_scheme'] + '://'

    if environ.get('HTTP_HOST'):
        url += environ['HTTP_HOST']
    else:
        url += environ['SERVER_NAME']

        if (environ['wsgi.url_scheme'] == 'https' and 
            environ['SERVER_PORT'] != '443') or \
            environ['SERVER_PORT'] != '80':
                url += ':' + environ['SERVER_PORT']
        
    url += quote(environ.get('SCRIPT_NAME', ''))
    url += quote(environ.get('PATH_INFO', ''))
    if environ.get('QUERY_STRING'):
        url += '?' + environ['QUERY_STRING']
    return url