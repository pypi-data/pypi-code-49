#
# Module: spade-cli
#
# Description: SPADE command line interface
#

from __future__ import print_function

import sys

def _eprint(*args, **kwargs):
    """Prints to standard error"""
    print(*args, file=sys.stderr, **kwargs)


import os
from spade_client import Spade, Display, BundlesFunction, TicketsFunction, FatalError


def main():
    import sys
    import argparse
    parser = argparse.ArgumentParser(description='Command Line interface to SPADE.')
    parser.add_argument('-v',
                        '--version',
                        dest='VERSION',
                        help='print out the version information of the application.',
                        action='store_true',
                        default=False)
    parser.add_argument('-d',
                        '--debug',
                        dest='DEBUG',
                        help='print out RESTful documents.',
                        action='store_true',
                        default=False)
    parser.add_argument('-b',
                        '--bundle',
                        dest='BUNDLE',
                        help='applies the commands to the specified bundle, if applicable. May be specified multiple times for some commands.',
                        action='append')
    parser.add_argument('--cacert',
                        dest = 'CA_CERTIFICATE',
                        help = 'path to the file containing one or more CA x509 certificates, if different from the default,'
                        + ' ${HOME}/.spade/client/cert/cacert.pem',
                        default = None)
    parser.add_argument('--cert',
                        dest = 'CERTIFICATE',
                        help = 'path to the client\'s x509 certificate, if different from the default,'
                        + ' ${HOME}/.spade/client/cert/spade_client.pem',
                        default = None)
    parser.add_argument('--file_bundles',
                        dest='FILE_BUNDLES',
                        help='specified the file from which to read a set of bundles to which the commands will be applied.',
                        action='store')
    parser.add_argument('--file_tickets',
                        dest='FILE_TICKETS',
                        help='specified the file from which to read a set of tickets to which the commands will be applied.',
                        action='store')
    parser.add_argument('--key',
                        dest = 'KEY',
                        help = 'path to the client\'s private x509 key, if different from the default,'
                        + ' ${HOME}/.psquared/client/private/psquare_client.key',
                        default = None)
    parser.add_argument('-t',
                        '--ticket',
                        dest='TICKET',
                        help='applies the commands to the specified ticket, if applicable. May be specified multiple times for some commands.',
                        action='append')
    parser.add_argument('args', nargs=argparse.REMAINDER)
    options = parser.parse_args()
    args = options.args

    if 1 > len(args):
        commands = []
    else:
        commands = args[:]

    url = os.getenv('SPADE_APPLICATION', 'http://localhost:8080/spade/local/report/')
    spade = Spade(url, xml=options.DEBUG, cert = options.CERTIFICATE, key = options.KEY, cacert = options.CA_CERTIFICATE )
    if options.DEBUG:
        spade.debug_separator()


    try:
        application = spade.get_application()
        if 0 == len(commands):
            if options.VERSION:
                Display.version(application)
                sys.exit(0)
            Display.status(application)
            sys.exit(0)
        
        if (None != options.BUNDLE and 0 != len(options.BUNDLE)) or None != options.FILE_BUNDLES:
            if None == options.FILE_BUNDLES:
                bundles_function = BundlesFunction(options.BUNDLE, spade.session, options.DEBUG)
            else:
                bundles_file = open(options.FILE_BUNDLES)
                bundles = [x.strip('\n') for x in bundles_file.readlines()]
                if None != options.BUNDLE and 0 != len(options.BUNDLE):
                    bundles.extend(options.BUNDLE)
                bundles_function = BundleFunction(bundles, spade.session, options.DEBUG)
        else:
            bundles_function = BundlesFunction(None, None);

        if (None != options.TICKET and 0 != len(options.TICKET)) or None != options.FILE_TICKETS:
            if None == options.FILE_TICKETS:
                tickets_function = TicketsFunction(options.TICKET, spade.session, options.DEBUG)
            else:
                tickets_file = open(options.FILE_TICKETS)
                tickets = [x.strip('\n') for x in tickets_file.readlines()]
                if None != options.TICKET and 0 != len(options.TICKET):
                    tickets.extend(options.TICKET)
                tickets_function = TicketFunction(tickets, spade.session, options.DEBUG)
        else:
            tickets_function = TicketsFunction(None, None);

        for command in commands:
            if 'application_actions' == command:
                Display.named_resources(application, ['commands/[name="application"]/action'], 'Application Actions')
            elif 'bundles_actions' == command:
                Display.named_resources(application, ['reports/[name="bundles"]/action',
                								   'commands/[name="bundles"]/action'], 'Bundle Actions')
            elif 'stampers' == command:
                Display.named_resources(application, 'time_stampers/stamper', 'Time Stamp Reports')
            else:
                if spade.execute_named_resource(application, 'commands/[name="application"]/action', command, spade.application_action):
                    pass
                elif spade.execute_named_resource(application, 'reports/[name="bundles"]/action', command, bundles_function.report):
                    pass
                elif spade.execute_named_resource(application ,'commands/[name="bundles"]/action', command, bundles_function.command):
                    pass
                elif spade.execute_named_resource(application ,'commands/[name="tickets"]/action', command, tickets_function.command):
                    pass
                elif spade.execute_named_resource(application, 'time_stampers/stamper', command, spade.get_time_stampers):
                    pass
                else:
                    print("Unrecognized command : " + command)
                    sys.exit(1)

    except FatalError as e:
        _eprint(e.message)
        sys.exit(e.code)

if __name__ == '__main__':
    main()

