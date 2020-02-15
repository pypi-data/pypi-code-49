'''
quick httpx.get
'''
import sys

import argparse
# from asyncio import get_event_loop, new_event_loop, set_event_loop
from pprint import pprint
import httpx

import pytest
from loguru import logger

from .make_url import make_url
# from arun import arun

HEADERS = {
    'User-Agent':
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1309.0 Safari/537.17'  # noqa
}


async def httpx_get(url, proxy=None, timeout=4, verify=False, connect_timeout=8.0, headers=None, cookies=None):  # pylint: disable=too-many-arguments
    ''' quick httpx.get

    >>> arun(httpx_get('http://httpbin.org/user-agent')).json()['user-agent'][:6] in ['python', 'Mozill']  # noqa
    True
    >>> arun(httpx_get('http://httpbin.org/user-agent', headers={'User-Agent': 'xxx'})).json()['user-agent']  # noqa
    'xxx'

    loop = get_event_loop()
    if loop.is_closed():
        loop = new_event_loop()
        set_event_loop(loop)
    '''

    # logger.debug(f'args: {args}')
    # logger.debug(f'kwargs: {kwargs}')

    # for creating httpx.Response in case Exception
    req = httpx.models.Request('GET', url)

    timeo = httpx.Timeout(timeout, connect_timeout=connect_timeout)

    if headers is None:
        headers = HEADERS

    # timeout exception
    try:
        async with httpx.AsyncClient(
                proxies=proxy,
                timeout=timeo,
                trust_env=False,
                headers=headers,
                verify=verify,
                cookies=cookies,
        ) as client:
            try:
                # resp = loop.run_until_complete(client.get(*args))
                resp = await client.get(url)
                # resp.raise_for_status()
            except Exception as exc:
                logger.error(exc)
                resp = httpx.Response(
                    status_code=499,
                    request=req,
                    content=str(exc).encode(),
                )

    except Exception as exc:
        logger.error('timeout: %s' % exc)
        resp = httpx.Response(
            status_code=499,
            request=req,
            content=str(exc).encode(),
        )
    finally:
        logger.debug('resp: %s' % resp.text[:10])

    return resp

    # return loop.run_until_complete(httpx.get(*args, **kwargs))


# @pytest.mark.asyncio
async def test_noproxy_baidu():
    ''' test_noproxy_baidu '''

    # resp = arun(httpx_get('http://www.baidu.com'))
    resp = await httpx_get('http://www.baidu.com')
    assert 'baidu.com' in resp.headers.__str__()
    assert 'via' not in resp.headers


# @pytest.mark.asyncio
async def test_localhost8889_baidu():
    ''' test_localhost8889_baidu '''

    proxy = 'http://127.0.0.1:8889'
    # resp = arun(httpx_get('http://www.baidu.com', proxy=proxy))
    resp = await httpx_get('http://www.baidu.com', proxy=proxy)
    assert 'baidu.com' in resp.headers.__str__()
    assert 'via' in resp.headers


@pytest.mark.xfail
# @pytest.mark.asyncio
async def test_socks5_baidu():
    ''' test_noproxy_baidu '''

    proxy = 'socks5://127.0.0.1:1080'

    try:
        # resp = arun(httpx_get('http://www.baidu.com', proxy=proxy))
        resp = await httpx_get('http://www.baidu.com', proxy=proxy)

        assert 'baidu.com' in resp.headers.__str__()
        assert 'via' not in resp.headers
    except Exception:
        assert 0


def main():
    ''' main
    '''
    from asyncio import get_event_loop

    args = argparse.ArgumentParser()
    args.add_argument(
        dest='urls', nargs='*', help='urls (0 or more)', type=str)

    args.add_argument('-p', '--proxy', dest='proxy', help='proxy', type=str)
    args.add_argument(
        '-d', '--debug', dest='debug', action='store_true', help='debug mode')

    # merge into locals()
    _ = args.parse_args()
    # locals().update(vars(_))
    # globals().update(vars(_))

    # for elm in vars(_):
    # globals()[elm] = getattr(_, elm)
    debug, proxy, urls = _.debug, _.proxy, _.urls

    # default to INFO
    # if not _.debug:
    if not debug:
        logger.remove()
        logger.add(sys.stderr, level='INFO')

    logger.debug(f'\n\t args: {_}')

    logger.info(f'proxy: {proxy}')
    for url in urls:
        logger.info(f'url: {url}')
    for url in urls:
        coro = httpx_get(make_url(url), {'proxies': {'all': make_url(proxy)}})
        resp = get_event_loop().run_until_complete(coro)
        if resp:
            logger.debug(f'\n\t resp: {resp.text[:120]}')
            pprint(f'\n\t resp: {resp.text[:50]}')
            pprint(resp.headers)
    # return resp


if __name__ == '__main__':

    # import shlex
    # in ipython testrun
    # sys.argv = sys.argv[:1]
    # sys.argv.extend(shlex.split('www.baidu.com -d'))
    # sys.argv = sys.argv[:1]
    # sys.argv.extend(shlex.split('www.baidu.com -d -p 127.0.0.1:8889'))

    # pprint(main().text)

    main()
