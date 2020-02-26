import re
import os
import json
import pytz
import requests
import datetime
from lxml import html
from lxml.etree import tostring


utc = pytz.UTC

directory = os.path.dirname(__file__)
headers_filename = os.path.join(
    directory, "ressources/headers.json")
with open(headers_filename) as f:
    headers = json.load(f)


def get_lang(title, desc, content):
    from langdetect import detect
    from langdetect.lang_detect_exception import LangDetectException
    try:
        if desc is not None:
            return detect(title)
        if title is not None:
            return detect(title)
        if content is not None:
            return detect(content)
    except LangDetectException:
        return None


def request(url):
    req = requests.get(url, headers=headers)
    if req.status_code == 200:
        text = req.text
        root = html.fromstring(text)
        return text, root
    raise ConnectionError


def get_source(url):
    source = re.match(
        r'^(?:https?:\/\/)?(?:[^@\/\n]+@)?(?:www\.)?([^:\/?\n]+)', url)
    if source is not None:
        return source.group(0).strip()
    return None


def get_stop_urls():
    stop_urls_filename = os.path.join(
        directory, "ressources/stop_urls.txt")
    with open(stop_urls_filename) as f:
        return set(f.read().split())


def to_str(element):
    return element.text_content().strip()


def bound_time(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        if res is not None:
            now = utc.localize(
                        datetime.datetime.now())
            try:
                if utc.localize(res) > now:
                    res = datetime.datetime.now()
                return res
            except ValueError:
                if res > now:
                    res = datetime.datetime.now()
                return res
        else:
            print("date is None")
            return datetime.datetime.now()
    return wrapper


def get_element_id(element):
    idx = str(element)
    css_class = element.attrib.get("class", "")
    css_id = element.attrib.get("id", "")
    return idx + css_class + css_id
