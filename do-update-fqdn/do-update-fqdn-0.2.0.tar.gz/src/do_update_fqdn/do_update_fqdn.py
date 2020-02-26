#!/bin/env python3

import json
import sys
import logging
import urllib.request
import argparse

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(name)s: %(message)s',
                    handlers=[logging.StreamHandler(sys.stdout)])
logger = logging.getLogger('do-update-fqdn')


def _get_api_response_pages(do_token, url):
    headers = {'Content-Type': 'application/json', 'Authorization': f'Bearer {do_token}'}
    while url:
        api_request = urllib.request.Request(url, headers=headers)
        api_response = urllib.request.urlopen(api_request).read()
        jsondata = json.loads(api_response.decode('utf-8'))
        try:
            url = jsondata['links']['pages']['next']
        except KeyError:
            url = None
        yield jsondata


def get_records_by_hostname(do_token, hostname, dns_domain, rtype):
    url = f'https://api.digitalocean.com/v2/domains/{dns_domain}/records'
    for rpage in _get_api_response_pages(do_token, url):
        for do_api_record in rpage['domain_records']:
            if do_api_record['name'] == hostname and do_api_record['type'] == rtype:
                yield do_api_record


def _api_action(do_token, url, method, http_body=None):
    headers = {'Content-Type': 'application/json', 'Authorization': f'Bearer {do_token}'}
    if http_body:
        api_request = urllib.request.Request(url, headers=headers, method=method, data=http_body.encode('utf-8'))
    else:
        api_request = urllib.request.Request(url, headers=headers, method=method)
    return urllib.request.urlopen(api_request).read()


def update_record(do_token, record_id, hostname, dns_domain, rtype, data, ttl):
    # need to use double brackets to get single brackets within a formatted string
    http_body = f'{{"name": "{hostname}", "type": "{rtype}", "data": "{data}", "ttl": "{ttl}"}}'
    url = f'https://api.digitalocean.com/v2/domains/{dns_domain}/records/{record_id}'
    api_response = _api_action(do_token, url, 'PUT', http_body).decode('utf-8')
    return json.loads(api_response)


def delete_record(do_token, record_id, dns_domain):
    url = f'https://api.digitalocean.com/v2/domains/{dns_domain}/records/{record_id}'
    # delete does not generate a response
    _api_action(do_token, url, 'DELETE').decode('utf-8')


def create_record(do_token, hostname, dns_domain, rtype, data, ttl):
    # need to use double brackets to get single brackets within a formatted string
    http_body = f'{{"name": "{hostname}", "type": "{rtype}", "data": "{data}", "ttl": "{ttl}"}}'
    url = f'https://api.digitalocean.com/v2/domains/{dns_domain}/records'
    api_response = _api_action(do_token, url, 'POST', http_body).decode('utf-8')
    return json.loads(api_response)


def cli_interface():
    exitcode = 255

    # the parser raises SystemExit when used with --help or nonsense-parameters.
    # catching that inside the blanket-except down there does not make sense,
    # and I don't want to catch other, possibly unknown occurrences of SystemExit.
    parser = argparse.ArgumentParser(description='update DigitalOcean dns record')
    parser.add_argument('--token', metavar='your_token', type=str, required=True, help='DO API token')
    parser.add_argument('--fqdn', metavar='foo.example.com', type=str, required=True, help='the fqdn to work on')
    parser.add_argument('--type', metavar='type', type=str, required=True, help='A or AAAA or whatever')
    parser.add_argument('--ttl', metavar='30', type=int, required=False, default=30,
                        help='30 is default and minimum at DO')
    parser.add_argument('--data', metavar='IP or whatever', type=str, required=False, help='content for the record')
    parser.add_argument('--action', metavar='[delete | upsert]', type=str, required=False, default='upsert',
                        help='delete or update/insert record')
    cliargs = parser.parse_args()
    try:
        assert (cliargs.action in ['upsert', 'delete']), 'action has to be either upsert or delete'
        hostname, dns_domain = cliargs.fqdn.split('.', maxsplit=1)
        assert hostname, 'hostname part of fqdn seems to be empty, check your input'
        assert dns_domain, 'domain part of fqdn seems to be empty, check your input'
        logger.info(f'{cliargs.action} {cliargs.type} record for {hostname} in domain {dns_domain}')

        modified_records = []
        if cliargs.action == 'upsert':
            for record in get_records_by_hostname(cliargs.token, hostname, dns_domain, cliargs.type):
                update_record(cliargs.token, record['id'], record['name'], dns_domain, record['type'], cliargs.data,
                              cliargs.ttl)
                modified_records.append(record)
                logger.info(f'updated record with DO id %s, data: {cliargs.data}', record['id'])
            if len(modified_records) == 0:
                response = create_record(cliargs.token, hostname, dns_domain, cliargs.type, cliargs.data, cliargs.ttl)
                modified_records.append(response)
                logger.info(f'created record with DO id %s, data: {cliargs.data}', response['domain_record']['id'])

        if cliargs.action == 'delete':
            for record in get_records_by_hostname(cliargs.token, hostname, dns_domain, cliargs.type):
                delete_record(cliargs.token, record['id'], dns_domain)
                modified_records.append(record)
                logger.info('deleted record with DO id %s', record['id'])
            if len(modified_records) == 0:
                logger.info(f'no {cliargs.type} records found in {dns_domain} for hostname {hostname}, nothing to do')

        if len(modified_records) > 1:
            logger.warning(f'warning, multiple records found for {hostname}, ran {cliargs.action} on all of them')
        exitcode = 0

    except urllib.error.HTTPError as err:
        logger.info(f'DO API did not cooperate, error was {err}')
        exitcode = 2
    except BaseException as e:
        logger.exception(e)
    finally:
        logging.shutdown()
        sys.exit(exitcode)


if __name__ == '__main__':
    cli_interface()
