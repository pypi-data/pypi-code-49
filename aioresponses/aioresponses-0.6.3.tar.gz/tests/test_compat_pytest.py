# # -*- coding: utf-8 -*-
# from typing import Union
#
# import pytest
# from yarl import URL
#
# from aioresponses.compat import merge_params
#
#
# @pytest.fixture
# def url_with_parameters():
#     return 'http://example.com/api?foo=bar#fragment'
#
#
# @pytest.fixture
# def url_without_parameters():
#     return 'http://example.com/api?#fragment'
#
#
# def get_url(url: str, as_str: bool) -> Union[URL, str]:
#     return url if as_str else URL(url)
#
#
# @pytest.mark.parametrize("as_str", (True, False))
# def test_no_params_returns_same_url__as_str(as_str, url_with_parameters):
#     url = get_url(url_with_parameters, as_str)
#     assert merge_params(url, None) == URL(url_with_parameters)
#
#
# @pytest.mark.parametrize("as_str", (True, False))
# def test_empty_params_returns_same_url__as_str(as_str, url_with_parameters):
#     url = get_url(url_with_parameters, as_str)
#     assert merge_params(url, {}) == URL(url_with_parameters)
#
#
# @pytest.mark.parametrize("as_str", (True, False))
# def test_both_with_params_returns_corrected_url__as_str(as_str,
#                                                         url_with_parameters):
#     url = get_url(url_with_parameters, as_str)
#     assert (
#             merge_params(url, {'x': 42}) == URL('http://example.com/api?foo=bar&x=42#fragment')
#     )
