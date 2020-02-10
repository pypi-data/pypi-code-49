#!/usr/bin/env python3
#
# Nagios plugin to check an EIDA 'auth' endpoint
#
# Copyright (C) 2020 Javier Quinteros, GEOFON team
# <javier@gfz-potsdam.de>
#
# ----------------------------------------------------------------------

"""Nagios plugin to check an EIDA 'auth' endpoint

   :Platform:
       Linux
   :Copyright:
       GEOFON, Helmholtz-Zentrum Potsdam - Deutsches GeoForschungsZentrum GFZ
       <geofon@gfz-potsdam.de>
   :License:
       GNU General Public License, Version 3, 29 June 2007

   This program is free software; you can redistribute it and/or modify it
   under the terms of the GNU General Public License as published by the Free
   Software Foundation; either version 3, or (at your option) any later
   version. For more information, see http://www.gnu.org/

.. moduleauthor:: Javier Quinteros <javier@gfz-potsdam.de>, GEOFON, GFZ Potsdam
"""

import requests
import os
import sys
import time
import argparse
import xml.etree.ElementTree as ET


def nagios_output(service, status, message, perfvalues, multiline=None, verbose=0):
    if (multiline is None) or not len(multiline) or not verbose:
        print('%s %s: %s | %s' % (service, status, message, perfvalues))
    else:
        print('%s %s: %s | %s\n%s' % (service, status, message, perfvalues, multiline))


def check_EIDA_auth(url, timeout=9, token=None, verbose=0):
    """ Check a URL to be a valid EIDA auth method

        A file containing a token is expected in the home folder
        of the user running this script with filename '.eidatoken'
        Return 0: OK; 1: WARNING; 2: CRITICAL
    """

    # Default location for token
    if token is None:
        token = os.path.expanduser('~/.eidatoken')

    headers = {
        'User-Agent': 'check_EIDA_auth python-requests/' + requests.__version__,
    }

    # Save starting time to measure performance
    start_time = time.time()

    # First test if the "auth" method is present in application.wadl
    wadl = url.replace('https:', 'http:').replace('/1/auth', '/1/application.wadl')
    try:
        r = requests.get(wadl, headers=headers)
    except Exception:
        nagios_output('AUTH', 'FAILED', 'Error while reading from %s' % wadl,
                      'time=%fs' % (time.time() - start_time),
                      verbose=verbose)
        return 2

    # Parse application.wadl
    try:
        root = ET.fromstring(r.text)
    except ET.ParseError:
        nagios_output('AUTH', 'FAILED', 'Error parsing %s' % wadl,
                      'time=%fs' % (time.time() - start_time),
                      verbose=verbose)
        return 2

    namesp = root.tag[:-len('application')]

    # Search the "auth" resource
    authenabled = False
    for resources in root.findall(namesp+'resources'):
        if authenabled:
            break
        for resource in resources.findall(namesp+'resource'):
            if 'path' in resource.attrib:
                if resource.attrib['path'] == 'auth':
                    authenabled = True
                    break

    if not authenabled:
        nagios_output('AUTH', 'DISABLED', url,
                      'time=%fs' % (time.time() - start_time),
                      verbose=verbose)
        return 0

    # This is actually a critical part. A token is expected in the home folder
    # of the user running this script with filename '.eidatoken'
    files = {'file': open(token, 'rb')}
    try:
        r = requests.post(url, files=files, headers=headers, timeout=timeout)
        # Close file with token
        files['file'].close()

        if r.status_code != 200:
            nagios_output('AUTH', 'FAILED', url, 'time=%fs' % (time.time() - start_time),
                          'HTTP error code: %s\nText: %s' % (r.status_code, r.text),
                          verbose=verbose)
            return 2
    except requests.exceptions.ConnectTimeout:
        nagios_output('AUTH', 'TIMEOUT', url, 'time=%fs' % (time.time() - start_time))
        return 2
    except requests.exceptions.SSLError:
        r = requests.post(url, files=files, headers=headers, timeout=10, verify=False)
        # Close file with token
        files['file'].close()

        if r.status_code == 200:
            nagios_output('AUTH', 'INVALID_CERTIFICATE', url, 'time=%fs' % (time.time() - start_time))
            return 1
        else:
            nagios_output('AUTH', 'FAILED_AND_INVALID_CERTIFICATE', url,
                          'time=%fs' % (time.time() - start_time))
            return 2

    resp = r.text.split(':')
    if len(resp) != 2:
        nagios_output('AUTH', 'WRONG_FORMAT', url, 'time=%fs' % (time.time() - start_time),
                      'Response= "%s"' % resp, verbose=verbose)
        return 2

    nagios_output('AUTH', 'OK', url, 'time=%fs' % (time.time() - start_time))
    return 0


def main():
    """Nagios plugin to check an EIDA 'auth' endpoint

    Following Nagios specifications, the value returned can be
    0: OK
    1: WARNING
    2: CRITICAL
    3: UNKNOWN
    and the output line is something like

    AUTH OK: https://eida.bgr.de/fdsnws/dataselect/1/auth | time=0.133321s
    """

    version = '0.1a6'

    # URLs pointing to the "auth" method for each data centre
    urls = dict()
    urls['BGR'] = 'https://eida.bgr.de/fdsnws/dataselect/1/auth'
    urls['ETH'] = 'https://eida.ethz.ch/fdsnws/dataselect/1/auth'
    urls['GFZ'] = 'https://geofon.gfz-potsdam.de/fdsnws/dataselect/1/auth'
    urls['INGV'] = 'https://webservices.ingv.it/fdsnws/dataselect/1/auth'
    urls['KOERI'] = 'https://eida-service.koeri.boun.edu.tr/fdsnws/dataselect/1/auth'
    urls['LMU'] = 'https://erde.geophysik.uni-muenchen.de/fdsnws/dataselect/1/auth'
    urls['NIEP'] = 'https://eida-sc3.infp.ro/fdsnws/dataselect/1/auth'
    urls['NOA'] = 'https://eida.gein.noa.gr/fdsnws/dataselect/1/auth'
    urls['ODC'] = 'https://www.orfeus-eu.org/fdsnws/dataselect/1/auth'
    urls['RESIF'] = 'https://ws.resif.fr/fdsnws/dataselect/1/auth'
    urls['UIB'] = 'https://eida.geo.uib.no/fdsnws/dataselect/1/auth'

    desc = ('Nagios plugin to check an EIDA auth endpoint. '
            'If no arguments are passed all EIDA nodes are tested.')
    parser = argparse.ArgumentParser(description=desc)

    group = parser.add_mutually_exclusive_group()
    group.add_argument('-H', '--hostname', default=None,
                       help=('Hostname providing the "auth" method at the default location. '
                             'Valid values are domain names (e.g. geofon.gfz-potsdam.de) or '
                             'the data centre ID (%s)' % ', '.join(urls.keys())))
    group.add_argument('-u', '--url', default=None,
                       help='URL pointing to the "auth" method to check. Use with non-standard locations')
    parser.add_argument('-t', '--timeout', default=9, type=int,
                        help='Number of seconds to be used as a timeout for the HTTP calls.')
    parser.add_argument('-a', '--authentication', default=os.path.expanduser('~/.eidatoken'),
                        help='File containing the token to use during the authentication process')
    parser.add_argument('-V', '--version', action='version', version='%(prog)s ' + version,
                        help='Show version information.')
    parser.add_argument('-v', '--verbose', action='count', default=0,
                        help='If this option is enabled more lines with details will follow the expected one-line message')
    args = parser.parse_args()

    requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)

    if args.hostname is not None:
        if args.hostname in urls:
            sys.exit(check_EIDA_auth(urls[args.hostname], timeout=args.timeout,
                                     token=args.authentication,
                                     verbose=args.verbose))
        sys.exit(check_EIDA_auth('https://%s/fdsnws/dataselect/1/auth' % args.hostname,
                                 timeout=args.timeout, token=args.authentication,
                                 verbose=args.verbose))

    if args.url is not None:
        sys.exit(check_EIDA_auth(args.url, timeout=args.timeout,
                                 token=args.authentication,
                                 verbose=args.verbose))

    retcode = 0
    for dc, url in urls.items():
        retcode = max(retcode, check_EIDA_auth(url, timeout=args.timeout,
                                               token=args.authentication,
                                               verbose=args.verbose))

    sys.exit(retcode)


if __name__ == '__main__':
    main()
