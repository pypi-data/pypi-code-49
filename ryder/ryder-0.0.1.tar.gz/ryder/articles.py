from .utils import request, to_str, bound_time, get_element_id, get_lang
from .clean import clean_str, remove_campaign_from_url
from .errors import ParseError
from collections import defaultdict
import dateparser
import datetime
import re


@clean_str
def get_title(html, root):
    t = root.xpath("//h1")
    if len(t) == 0:
        t = root.xpath("//title")
    if len(t) == 0:
        raise ParseError("title not found")

    return to_str(t[0])


@clean_str
def get_description(root):
    t = root.xpath("//p[@class='article__desc']")
    if len(t) > 0:
        return to_str(t[0])

    t = root.xpath("//meta[@name='description']")
    if len(t) > 0:
        return t[0].attrib.get("content", None)

    t = root.xpath("//div[contains(@class, 'gr-article-teaser')]")
    if len(t) > 0:
        return to_str(t[0])

    t = root.xpath("//meta[@property='og:description']")
    if len(t) > 0:
        return t[0].attrib.get("content", None)

    t = root.xpath("//meta[@property='twitter:description']")
    if len(t) > 0:
        return t[0].attrib.get("content", None)

    return None


@clean_str
def get_author(root):
    t = root.xpath("//meta[@name='author']")
    if len(t) > 0:
        return t[0].attrib.get("content", None)

    t = root.xpath("//meta[@itemprop='author']")
    if len(t) > 0:
        return t[0].attrib.get("content", None)

    t = root.xpath("//meta[@property='author']")
    if len(t) > 0:
        return t[0].attrib.get("content", None)


@bound_time
def get_created_time(html, root):
    t = root.xpath("//meta[@itemprop='dateModified']")
    if len(t) > 0:
        created_time = dateparser.parse(t[0].attrib["content"])
        return created_time

    t = root.xpath("//meta[@itemprop='datePublished']")
    if len(t) > 0:
        created_time = dateparser.parse(t[0].attrib["content"])
        return created_time

    t = root.xpath("//meta[@property='og:article:modified_time']")
    if len(t) > 0:
        created_time = dateparser.parse(t[0].attrib["content"])
        return created_time

    t = root.xpath("//meta[@property='article:modified_time']")
    if len(t) > 0:
        created_time = dateparser.parse(t[0].attrib["content"])
        return created_time

    t = root.xpath("//meta[@property='twitter:article:modified_time']")
    if len(t) > 0:
        created_time = dateparser.parse(t[0].attrib["content"])
        return created_time

    t = root.xpath("//meta[@property='og:article:published_time']")
    if len(t) > 0:
        created_time = dateparser.parse(t[0].attrib["content"])
        return created_time
    
    t = root.xpath("//meta[@property='article:published_time']")
    if len(t) > 0:
        created_time = dateparser.parse(t[0].attrib["content"])
        return created_time
    
    t = root.xpath("//meta[@property='twitter:article:published_time']")
    if len(t) > 0:
        created_time = dateparser.parse(t[0].attrib["content"])
        return created_time

    t = re.findall(r'dateModified\":[\s]+\"(.+?)\"', html)
    if len(t) > 0:
        created_time = dateparser.parse(t[0])
        return created_time

    t = re.findall(r'datePublished\":[\s]+\"(.+?)\"', html)
    if len(t) > 0:
        created_time = dateparser.parse(t[0])
        return created_time

    t = root.xpath("//*[@class='date']")
    if len(t) > 0:
        created_time = dateparser.parse(to_str(t[0]))
        return created_time

    t = root.xpath("//time")
    if len(t) > 0:
        created_time = dateparser.parse(t[-1].attrib.get("datetime", None))
        return created_time

    t = root.xpath("//*[contains(@class, 'date')]")
    if len(t) > 0:
        created_time = dateparser.parse(to_str(t[0]))
        return created_time

    t = re.findall(r"updat=([^\s]+)", html)
    if len(t) > 0:
        created_time = dateparser.parse(t[0])
        return created_time

    t = re.findall(r"publicationData\":\"([^\"]+)", html)
    if len(t) > 0:
        created_time = dateparser.parse(t[0])
        return created_time


def get_image(root):
    t = root.xpath("//meta[@property='og:image']")
    if len(t) > 0:
        t = t[0].attrib.get("content", None)
        return t

    t = root.xpath("//meta[@property='twitter:image']")
    if len(t) > 0:
        t = t[0].attrib.get("content", None)
        return t

    t = root.xpath("//meta[@property='facebook:image']")
    if len(t) > 0:
        t = t[0].attrib.get("content", None)
        return t


@clean_str
def get_content(root):
    t = root.xpath("//*/*[self::p or self::h2 or self::div[@class='article__body']]")
    paragraphs = defaultdict(list)
    length = defaultdict(int)
    max_length = 0
    id_max = None
    for item in t:
        parent = item.getparent()
        id_parent = get_element_id(parent)
        paragraphs[id_parent].append(item)

        content_strip = re.sub(r"[\s\n]", "", to_str(item))
        length[id_parent] += len(content_strip)
        if "article" in id_parent:
            length[id_parent] += len(content_strip)

        if length[id_parent] > max_length:
            max_length = length[id_parent]
            id_max = id_parent

    if id_max is not None:
        return "\n\n".join([to_str(y) for y in paragraphs[id_max]])
    return None


def read(url, lang=True):
    url = remove_campaign_from_url(url)

    try:
        html, root = request(url)
        
        title = get_title(html, root)
        desc = get_description(root)
        created_time = get_created_time(html, root)
        img = get_image(root)
        content = get_content(root)
        author = get_author(root)

        if lang:
            detected_lang = get_lang(title, desc, content)
        else:
            detected_lang = None

        return {
            "title": title,
            "description": desc,
            "created_time": created_time,
            "img": img,
            "content": content,
            "lang": detected_lang,
            "author": author
        }
    except ParseError:
        return None
