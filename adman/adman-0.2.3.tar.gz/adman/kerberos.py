# https://wiki.samba.org/index.php/Configure_DHCP_to_update_DNS_records_with_BIND9
from datetime import datetime, timedelta
import subprocess
import logging
import re
import os

DEFAULT_CCACHE_MINTIME = 300    # seconds

logger = logging.getLogger(__name__)

class KerberosError(Exception):
    pass

def request_new_tgt(principal, keytab, cache):
    logger.info("Requesting new ticket")
    args = [
        'kinit',

        # request non-forwardable tickets
        '-F',

        # request a ticket using a key in this local keytab file
        '-k', '-t', str(keytab),

        # store tickets in this cache
        '-c', str(cache),

        principal,
    ]
    logger.debug("Running `{}`".format(' '.join(args)))

    try:
        cp = subprocess.run(args, check=True)
    except subprocess.CalledProcessError:
        raise KerberosError("Failed to request new Kerberos ticket")


# MIT output for 'klist -c test.cc'
"""
Ticket cache: FILE:test.cc
Default principal: joe@AD-TEST.VX

Valid starting       Expires              Service principal
12/30/2019 12:05:58  12/30/2019 22:05:58  krbtgt/AD-TEST.VX@AD-TEST.VX
	renew until 12/31/2019 12:05:58
"""

# Heimdal output for 'klist -c test.cc'
"""
Credentials cache: FILE:test.cc
        Principal: joe@AD-TEST.VX

  Issued                Expires               Principal
Dec 30 12:05:58 2019  Dec 30 22:05:58 2019  krbtgt/AD-TEST.VX@AD-TEST.VX
"""
# or
"""
Credentials cache: FILE:test.cc
        Principal: joe@AD-TEST.VX

  Issued                Expires        Principal
Dec 30 12:05:58 2019  >>>Expired<<<  krbtgt/AD-TEST.VX@AD-TEST.VX
"""


def parse_time(s):
    # TODO: Do either of these use locale?
    try:
        # MIT: 12/30/2019 12:05:58
        return datetime.strptime(s, '%m/%d/%Y %H:%M:%S')
    except ValueError:
        pass

    try:
        # Heimdal: Dec 30 12:05:58 2019
        return datetime.strptime(s, '%b %d %H:%M:%S %Y')
    except ValueError:
        pass

    raise ValueError("Unknown time format: {}".format(s))


class CredCache:
    def __init__(self):
        self.tickets = {}    # keyed by principal

def load_cred_cache(ccache):
    """Load a krb5 credential cache
    """
    args = [
        'klist',
        '-c', str(ccache),
    ]
    logger.debug("Running `{}`".format(' '.join(args)))
    cp = subprocess.run(args, check=True,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE,
                        universal_newlines=True)

    result = CredCache()

    meta_pat = re.compile(r'([\w\s]+): (.*)')

    def handle_meta(line):
        if not line:
            # This is the blank line
            return handle_header

        # Metadata line?
        m = meta_pat.match(line)
        if not m:
            raise Exception("Unexpected line: " + line)
        k, v = m.groups()
        k = {
            'Credentials cache':    'cache',        # Heimdal
            'Ticket cache':         'cache',        # MIT
            'Principal':            'principal',    # Heimdal
            'Default principal':    'principal',    # MIT
        }.get(k)
        if not k:
            raise Exception("Unexpected line: " + line)
        setattr(result, k, v)
        return handle_meta

    def handle_header(line):
        parts = [x.strip() for x in line.split('  ') if x]
        if not parts[0] in ('Issued', 'Valid starting'):
            raise Exception("Unexpected line: " + line)
        if not parts[1] == 'Expires':
            raise Exception("Unexpected line: " + line)
        if not parts[2] in ('Principal', 'Service principal'):
            raise Exception("Unexpected line: " + line)
        return handle_ticket

    def handle_ticket(line):
        # Ticket/credential line?
        if line.startswith('renew until'):
            return handle_ticket

        parts = line.split('  ')

        issued = parse_time(parts[0])

        if 'expire' in parts[1].lower():
            expires = datetime.now()
        else:
            expires = parse_time(parts[1])

        principal = parts[2]

        result.tickets[principal] = (issued, expires)

        return handle_ticket

    state = handle_meta
    for line in cp.stdout.splitlines():
        line = line.strip()
        state = state(line)
        if not state:
            break

    return result


def check_cred_cache(cache, realm, mintime=None):
    """Checks that a credential cache is valid

    This function ensures that the given credential cache has a ticket-granting
    ticket (TGT) valid for a sufficient amount of time.

    Parameters:
    cache   Kerberos credential cache to check
    realm   Kerberos realm to check for TGT
    mintime Minimum amount of time (in seconds) for which TGT must be valid
    """
    if mintime is None:
        mintime = DEFAULT_CCACHE_MINTIME
    mintime = timedelta(seconds=mintime)

    try:
        cc = load_cred_cache(cache)
    except subprocess.CalledProcessError:
        return False

    spn = make_principal('krbtgt', realm, realm)
    try:
        issued_at, expire_at = cc.tickets[spn]
    except KeyError:
        logger.info("{} not found in {}".format(spn, cache))
        return False

    expire_in = expire_at - datetime.now()
    if expire_in < mintime:
        # Expired
        logger.info("{} expired at {}".format(spn, expire_at))
        return False
    else:
        logger.info("{} expires in {} at {}".format(spn, expire_in, expire_at))
        return True


def ensure_valid_tgt(username, realm, keytab, cache, mintime=None):
    principal = make_principal(username, realm)
    logger.info("Using kerberos principal {}".format(principal))

    if not check_cred_cache(cache, realm, mintime=mintime):
        request_new_tgt(principal, keytab, cache)


def make_principal(primary, realm, instance=None):
    result = primary
    if instance:
        result += '/' + instance
    result += '@' + realm.upper()
    return result


def setup_kerberos_environ(username, realm, keytab, cache):
    ensure_valid_tgt(
            username = username,
            realm = realm,
            keytab = keytab,
            cache = cache,
        )
    os.environ['KRB5CCNAME'] = str(cache)


if __name__ == '__main__':
    def parse_args():
        import argparse
        ap = argparse.ArgumentParser()
        ap.add_argument('username')
        ap.add_argument('realm', type=str.upper)
        ap.add_argument('-k', dest='keytab', required=True)
        ap.add_argument('-c', dest='cache', required=True)
        ap.add_argument('-m', dest='mintime', type=int)
        return ap.parse_args()

    def main():
        logging.basicConfig(level=logging.DEBUG)

        args = parse_args()

        ensure_valid_tgt(
                username = args.username,
                realm = args.realm,
                keytab = args.keytab,
                cache = args.cache,
                mintime = args.mintime,
            )

    main()
