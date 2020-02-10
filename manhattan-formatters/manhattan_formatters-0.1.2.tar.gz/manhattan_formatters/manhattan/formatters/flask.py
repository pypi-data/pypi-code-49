from flask import current_app

__all__ = ['path_to_url']


def path_to_url(path):
    """Convert local path to a full URL and return it"""
    if '://' not in path:
        return '{0}://{1}{2}'.format(
            current_app.config['PREFERRED_URL_SCHEME'],
            current_app.config['SERVER_NAME'],
            path
        )

    return path
