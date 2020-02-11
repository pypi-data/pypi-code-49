#!/usr/bin/env python3

from operator import itemgetter



from requests.structures import CaseInsensitiveDict


import argparse
import json
# import nltk
import re
import certifi
import requests

import time
import os

try:
    from seoanalyzer.stemmer import stem
except ImportError:
    from stemmer import stem

##
# python 3.6+ support.
import sys

if list(sys.version_info)[:2] >= [3, 6]:
    unicode = str
##





SESSION_TESTING_URL = 'https://httpbin.org/get'


def get_default_headers():
    """This method must come before class-var declaration or referencing it gets wonky."""
    return  CaseInsensitiveDict(
        {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml',
            'Accept-Language': 'en-US,en',
            'Upgrade-Insecure-Requests': '1',
            'Cache-Control': 'max-age=0',
        }
    )

class Manifest(object):
    """
    Pretty much what it sounds like...
    This is a singleton class which *should*:
    - allow for easy namespace-separation
    &
    - reinitialization of what were previously global vars.
    """
    # class vars
    wordcount = Counter()
    bigrams = Counter()
    trigrams = Counter()
    pages_crawled = []
    pages_to_crawl = []
    stem_to_word = {}
    page_titles = []
    page_descriptions = []
    session = requests.Session()
    session.headers = get_default_headers()
    # session.cert = certifi.where()

    # b/c this is necessary for persistence...I think...it is in python2...
    def __init__(self):
        super(Manifest, self).__init__()

    @classmethod
    def modify_session(cls,**kwargs):
        """Use **kwargs to enter arbitrary k/v pairs and load them as request.Session() attributes."""
        session_param_dict = kwargs
        for param_name, param in session_param_dict.items():
            try:
                assert param_name in requests.Session.__attrs__
                # this is dangerous as all hell:
                #TODO: Find an elegant way to run type & content checks on `param`.
                cls.session.__dict__[param_name] = param
            except AssertionError as err:
                print("You've passed in {} as param to modify your requests session.".format(param_name))
                print("Options are: {}".format(requests.Session.__attrs__))
                print("Bypassing {}...".format(param_name) + os.linesep)
                # explicit garbage collection. This is implied but whateva.
                del session_param_dict[param_name]
                continue

    @classmethod
    def test_session_modifications(cls):
        try:
            information = cls.session.get(SESSION_TESTING_URL)
        except Exception as err:
            information = 'ERROR'
            print(err.args)
            print(err)
        return information

    @classmethod
    def clear_cache(cls):
        # called at the end of the global `analyze()` function to make a fresh manifest.
        cls.wordcount = Counter()
        cls.bigrams = Counter()
        cls.trigrams = Counter()
        cls.pages_crawled = []
        cls.pages_to_crawl = []
        cls.stem_to_word = {}
        cls.page_titles = []
        cls.page_descriptions = []
        cls.session = requests.Session()
        cls.session.headers = get_default_headers()
        # cls.session.cert = certifi.where()


def do_ignore(url_to_check):
    # todo: add blacklist of url types
    return False


def clean_up():
    # close our client-session
    Manifest.session.close()
    # garbage-collect & reinit the whole manifest
    Manifest.clear_cache()


def analyze_old(site, sitemap=None, verbose=False, **session_params):
    """Session params are  headers, default cookies, etc...

       To quickly see your options, go into python and type:
       >>> print(requests.Session.__attrs__)
    """
    start_time = time.time()

    # Init our HTTP session
    if session_params:
        Manifest.modify_session(**session_params)
    else:
        Manifest()

    def calc_total_time():
        return time.time() - start_time

    crawled = []
    output = {'pages': [], 'keywords': [], 'errors': [], 'total_time': calc_total_time()}

    if check_dns(site) == False:
        output['errors'].append('DNS Lookup Failed')
        output['total_time'] = calc_total_time()
        return output



    Manifest.pages_to_crawl.append(site)
    on_page = 0
    for page in Manifest.pages_to_crawl:
        on_page += 1
        if verbose:
            print('Analyzing page {} out of {}...'.format(on_page, len(Manifest.pages_to_crawl)))
        if page.strip().lower() in crawled:
            continue

        if '#' in page:
            if page[:page.index('#')].strip().lower() in crawled:
                continue

        if do_ignore(page) == True:
            continue

        crawled.append(page.strip().lower())

        pg = Page(page, site)

        pg.analyze()

        output['pages'].append(pg.talk())

    sorted_words = sorted(Manifest.wordcount.items(), key=itemgetter(1), reverse=True)
    sorted_bigrams = sorted(Manifest.bigrams.items(), key=itemgetter(1), reverse=True)
    sorted_trigrams = sorted(Manifest.trigrams.items(), key=itemgetter(1), reverse=True)

    output['keywords'] = []

    for w in sorted_words:
        if w[1] > 4:
            output['keywords'].append({
                'word': Manifest.stem_to_word[w[0]],
                'count': w[1],
            })

    for w, v in sorted_bigrams:
        if v > 4:
            output['keywords'].append({
                'word': w,
                'count': v,
            })

    for w, v in sorted_trigrams:
        if v > 4:
            output['keywords'].append({
                'word': w,
                'count': v,
            })

    # Sort one last time...
    output['keywords'] = sorted(output['keywords'], key=itemgetter('count'), reverse=True)

    output['total_time'] = calc_total_time()

    return output


def print_output(output, output_format='json'):
    if output_format == 'html':
        from jinja2 import Environment
        from jinja2 import PackageLoader

        env = Environment(loader=PackageLoader('seoanalyzer'))
        template = env.get_template('index.html')
        output_from_parsed_template = template.render(result=output)

        print(output_from_parsed_template)
    elif output_format == 'json':
        print(json.dumps(output, indent=4, separators=(',', ': ')))
