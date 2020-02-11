# # -*- coding: utf-8 -*-
# import asyncio
#
# import pytest
# from aiohttp import ClientSession
#
# from aioresponses import aioresponses
#
#
# @pytest.yield_fixture
# def foo():
#     print('foo')
#     with aioresponses() as m:
#         yield m
#     print('')
#
#
# @pytest.fixture
# def session():
#     print('session')
#     return ClientSession()
#
#
# @pytest.yield_fixture()
# def event_loop():
#     loop = asyncio.new_event_loop()
#     asyncio.set_event_loop(loop)
#     yield loop
#     loop.close()
#
#
# @pytest.mark.asyncio
# async def test_me(foo, session):
#     url = 'http://example.com/api?foo=bar#fragment'
#     foo.get(url, status=204)
#     response = await session.get(url)
#
#     assert response.status == 204
