#! /usr/bin/env python3

import re
import csv
import sys
import itertools
import concurrent.futures
from collections import deque
from typing import Optional, Dict, Tuple
from concurrent.futures import ThreadPoolExecutor

import click
import logbook
import requests
from parsel import Selector
from named_enum import NamedEnum
from terminaltables import SingleTable
from logbook.more import ColorizedStderrHandler

# Starting page http://www.gdt.gov.vn/wps/portal/home/hct

URL_FOR_CODE = 'http://www.gdt.gov.vn/TTHKApp/jsp/json.jsp'
URL_FOR_BUSINESSOWNER = 'http://www.gdt.gov.vn/TTHKApp/jsp/results.jsp'
REGEX_AREA_CODE = re.compile(r'(?P<d>(?P<p>\d{3})\d{2})\d{2}$')
REGEX_PROVINCE_CODE = re.compile(r'\d{3}$')
REGEX_DISTRICT_CODE = re.compile(r'(?P<p>\d{3})\d{2}$')
logger = logbook.Logger(__name__)

# Currently, the version string is scattered among 3 different files. I wanted to reduce
# them, but due to limitation of Windows packaging tool, it is not possbile for now.
__version__ = '2.0.1'


class MyColorizedStderrHandler(ColorizedStderrHandler):
    default_format_string = '{record.level_name}: {record.message}'

    def get_color(self, record):
        color = super().get_color(record)
        if logbook.DEBUG < record.level <= logbook.INFO:
            return 'darkteal'
        return color


class ChoiceType(click.Choice):
    def __init__(self, enum):
        super().__init__(map(str, enum))
        self.enum = enum

    def convert(self, value, param, ctx):
        value = super().convert(value, param, ctx)
        return next(v for v in self.enum if str(v) == value)


class TaxDuty(NamedEnum):
    _field_names_ = ('strcode', 'numcode')

    NORMAL = ('normal', '11')
    VAT_EXEMPTED = ('vat-exempted', '10')
    SUSPENDED = ('suspended', '12')
    CLOSED = ('closed', '04')
    ADJUSTING = ('adjusting', '03')

    def __str__(self):
        return str(self.value.strcode)


def configure_logging(verbose):
    levels = (logbook.WARNING, logbook.INFO, logbook.DEBUG)
    l = min(verbose, len(levels) - 1)  # noqa
    colored_handler = MyColorizedStderrHandler(level=levels[l])
    colored_handler.push_application()


def get_province_name(code: str, http_session: requests.Session) -> Optional[str]:
    resp = http_session.get(URL_FOR_CODE, params={'cmd': 'GET_DS_TINH'}, timeout=2)
    return next((p['title'] for p in resp.json() if p['id'] == code), None)


def get_district_name(code: str, province_code: str, http_session: requests.Session) -> Optional[str]:
    resp = http_session.get(URL_FOR_CODE,
                            params={'cmd': 'GET_DS_HUYEN', 'maTinh': province_code}, timeout=2)
    return next((d['title'] for d in resp.json() if d['id'] == code), None)


def get_businesses_in_ward(ward: Dict[str, str], tax_duty: TaxDuty,
                           district: Dict[str, str], province: Dict[str, str]) -> Tuple[str, ...]:
    data = deque()
    with requests.Session() as http_session:
        params = {
            'maTinh': province['code'],
            'maHuyen': district['code'],
            'maXa': ward['id'],
            'searchType': tax_duty.numcode,
        }
        counter = itertools.count(1)
        while True:
            params['pageNumber'] = next(counter)
            logger.info('Retrieve with: {}', params)
            try:
                resp = http_session.get(URL_FOR_BUSINESSOWNER, params=params, timeout=2)
            except requests.exceptions.Timeout:
                logger.error('Server is blocking us.')
                break
            except requests.exceptions.ProxyError:
                logger.error('Proxy refuses to help us.')
                break
            content = resp.text
            logger.debug('URL: {}', resp.request.url)
            doc = Selector(content)
            rows = doc.css('table tr')
            logger.debug('Page: {} -> Number of rows: {}', params['pageNumber'], len(rows))
            if len(rows) < 3:
                break
            for r in rows[2:]:
                idx = r.css('td:first-child::text').get()
                name = r.css('td:nth-child(2)::text').get()
                address = r.css('td:nth-child(5)::text').get()
                business = r.css('td:nth-child(6)::text').get()
                data.append(
                    (idx, name, business, address, ward['title'], district['name'], province['name'])
                )
    return tuple(data)


@click.group()
@click.version_option(__version__, '-V', '--version')
@click.option('-v', '--verbose', count=True, default=False, help='Show more log to debug (verbose mode).')
def cli(verbose: int):
    if verbose:
        configure_logging(verbose)


@cli.command(help='Get province, district codes')
@click.argument('area_code', required=False)
@click.option('-v', '--verbose', count=True, default=False, help='Show more log to debug (verbose mode).')
def codes(area_code: Optional[str] = None, verbose: int = 0):
    configure_logging(verbose)
    if not area_code:
        params = {'cmd': 'GET_DS_TINH'}
        administration_name = 'Province'
    else:
        params = {}
        m_province = REGEX_PROVINCE_CODE.match(area_code)
        if m_province:
            params = {'cmd': 'GET_DS_HUYEN', 'maTinh': area_code}
            administration_name = 'District'
        m_district = REGEX_DISTRICT_CODE.match(area_code)
        if m_district:
            params = {'cmd': 'GET_DS_XA', 'maCQThue': area_code}
            administration_name = 'Ward'
        if not params:
            logger.error("Unrecognozed code: {}", area_code)
            sys.exit(1)
    try:
        resp = requests.get(URL_FOR_CODE, params, timeout=3)
    except requests.exceptions.Timeout:
        logger.error('Server is blocking us')
        sys.exit(2)
    logger.debug('Retrieved: {}', resp.request.url)
    data = tuple((r['title'], r['id']) for r in resp.json() if r['id'] != '000')
    table_data = (
        (click.style(administration_name, fg='green'), click.style('Code', fg='green')),
    ) + data
    click.echo(SingleTable(table_data).table)


@cli.command(help='Get business owners')
@click.argument('area_code')
@click.option('-t', '--tax-duty', 'tax_duty', type=ChoiceType(TaxDuty),
              default=TaxDuty.NORMAL.strcode, show_default=True)
@click.option('-o', '--out', 'output_file', required=True, type=click.File('w', encoding='utf-8'))
@click.option('-v', '--verbose', count=True, default=False, help='Show more log to debug (verbose mode).')
def businessowners(area_code: str, tax_duty: TaxDuty, output_file: click.File, verbose: int):
    configure_logging(verbose)
    while True:
        m = REGEX_AREA_CODE.match(area_code)
        if m:
            province_code = m.group('p')
            district_code = m.group('d')
            break
        # Maybe district code?
        m = REGEX_DISTRICT_CODE.match(area_code)
        if m:
            province_code = m.group('p')
            district_code = area_code
            break
        area_code = click.prompt('Please give a district/ward code', type=int)
    csv_writer = csv.writer(output_file, quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow(('ID', 'Name', 'Business', 'Address', 'Ward', 'District', 'Province'))
    with requests.Session() as http_session:
        try:
            # Verify data
            province_name = get_province_name(province_code, http_session)
            if not province_name:
                logger.error('Unknown province code: {}', province_code)
                sys.exit(1)
            district_name = get_district_name(district_code, province_code, http_session)
            if not district_name:
                logger.error('Unknown district code: {}', district_code)
                sys.exit(1)
            # Get ward codes
            params = {'cmd': 'GET_DS_XA', 'maCQThue': district_code}
            resp = http_session.get(URL_FOR_CODE, params=params, timeout=2)
        except requests.exceptions.Timeout:
            logger.error('Server is blocking us')
            sys.exit(2)
    logger.info('Retrieved: {}', resp.request.url)
    wards = tuple(resp.json())
    if REGEX_AREA_CODE.match(area_code):
        wards = tuple(w for w in wards if w['id'] == area_code)
    businesses = deque()
    district = {
        'code': district_code,
        'name': district_name
    }
    province = {
        'code': province_code,
        'name': province_name
    }
    # Split the tasks to run in parallel
    with ThreadPoolExecutor(max_workers=4) as executor:
        futures = tuple(executor.submit(get_businesses_in_ward, ward, tax_duty, district, province)
                        for ward in wards)
        for future in concurrent.futures.as_completed(futures):
            rows = future.result(timeout=60)
            businesses.extend(rows)
    csv_writer.writerows(businesses)

    click.secho(f'Wrote to file: {output_file.name}', fg='green')


if __name__ == '__main__':
    cli()
