import random
import time
import os
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from highcharts import Highchart
from pathlib import Path


def __render_chart(chart: Highchart, ttw=1) -> str:
    """
    Render chart

    :param chart:
    :param ttw: time to wait in seconds
    :return:
    """
    fname = f'chart_{random.randint(0, 100000000)}'
    workdir = os.getenv("SVG_RENDERER_WORKDIR", "/tmp/ut2svg/static/chart")
    Path(workdir).mkdir(parents=True, exist_ok=True, mode=666)
    filepath = f"{workdir}/{fname}"
    chart.save_file(filename=filepath)
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome("/usr/bin/chromedriver", port=random.randint(49152, 65535), chrome_options=chrome_options)
    driver.get(f"file://{filepath}.html")
    driver.set_page_load_timeout(time_to_wait=ttw+3)
    driver.set_script_timeout(time_to_wait=ttw+3)

    svg_xml = False
    _waited = 0

    while not svg_xml:
        _waited += 1
        svg_xml = __parse_svg_root(driver.page_source)

        if _waited > 5:
            raise Exception(f"Waited more than 5 seconds, no svg")

        if not svg_xml:
            time.sleep(1)

    time.sleep(1)
    svg_xml = __parse_svg_root(driver.page_source)

    svg_header = '<?xml version="1.0" standalone="no"?><!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" ' \
                 '"http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">'

    os.remove(f'{filepath}.html')

    driver.close()

    return f'{svg_header}{svg_xml}'


def __parse_svg_root(page_source):
    soup = BeautifulSoup(page_source, features="html.parser")
    cont = soup.find(class_="highcharts-point")
    if not cont or len(str(cont)) == 0:
        return False

    print("found point, sleep 3 sec")
    time.sleep(3)

    return str(soup.find(class_="highcharts-root"))
