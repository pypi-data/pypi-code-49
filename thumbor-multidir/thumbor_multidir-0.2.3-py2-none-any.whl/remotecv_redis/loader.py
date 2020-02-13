# coding: utf-8

from redis import Redis
from remotecv.utils import config
import urllib2
import re
import os

import logging

logger = logging.getLogger('remotecv_redis')
loglevel = getattr(logging, config.log_level.upper())
if not isinstance(loglevel, int):
    raise ValueError('Invalid config.log_level: %s' % config.log_level)
logger.setLevel(loglevel)


host = os.environ.get('REMOTECV_REDIS_LOADER_HOST', 'localhost')
port = os.environ.get('REMOTECV_REDIS_LOADER_PORT', '6379')
db = os.environ.get('REMOTECV_REDIS_LOADER_DATABASE', 0)
password = os.environ.get('REMOTECV_REDIS_LOADER_PASSWORD')
http_fallback = os.environ.get('REMOTECV_REDIS_LOADER_HTTP_FALLBACK', True)
http_agent = os.environ.get('REMOTECV_REDIS_LOADER_HTTP_USER_AGENT', 'RemoteCV/1')


def load_sync(path):
    """
    Loads image from Redis
    :param string path: Path to load
    """
    logger.debug("remotecv_redis.loader: Connecting to Redis(host=%s, port=%s, db=%s, password=%s)", host, port, db, password)
    redis = Redis(host=host, port=port, db=db, password=password)
    image = redis.get(path)

    if image:
        logger.debug("remotecv_redis.loader: Loaded %s" % path)
        return image

    if http_fallback:
        if not re.match(r'^https?', path):
            path = 'http://%s' % path
        path = urllib2.unquote(path)
        logger.info("remotecv_redis.loader: Image not found, falling back to http with %s" % path)

        opener = urllib2.build_opener()
        opener.addheaders = [('User-Agent', http_agent)]
        response = opener.open(path)
        return response.read()

    raise Exception("remotecv_redis.loader: Image not found at %s" % path)


