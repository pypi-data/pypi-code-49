from .version import VERSION
from .dns_type import DNSType, InvalidDNSType
from .resolver import Resolver
from .table import Table

import argparse
import re
import sys

def main():
    parser = argparse.ArgumentParser(description='Get relative DNS information.')
    parser.add_argument('-t', '--type', type=str, help='set DNS record type', default='ANY')
    parser.add_argument('domains', metavar='domain.tld', type=str, nargs='+', help='domains to lookup')
    parser.add_argument('-v', '--version', help='show program version', action='version', version=f"%(prog)s v{VERSION}")

    args = parser.parse_args()

    lookup = []

    for domain in args.domains:
        # Get nameservers
        resolver = Resolver()
        nameservers = resolver.query(domain, 'NS')

        # Get DNS lookup
        resolver = Resolver(nameservers=nameservers, additional_args=['+noall', '+nocmd', '+answer'])
        for row in resolver.query(domain, args.type):
            tmp_row = re.split(r'\t+', row)
            del tmp_row[2]
            if tmp_row[2] in ['A', 'AAAA', 'MX', 'NS', 'TXT', 'SRV', 'CNAME']:
                lookup.append(tmp_row)

    print(Table(['Domain', 'TTL', 'Type', 'Data'], lookup))

if __name__ == '__main__':
    main()
