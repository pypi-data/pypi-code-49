from .dns_type import DNSType

import random
import subprocess
import logging

logger = logging.getLogger(__name__)

class Resolver:

    def __init__(self, executable='dig', nameservers=None, additional_args=None, encoding='utf-8'):
        """
        Stores some customisable options into this resolver instance
        """
        self.executable = executable
        self.nameservers = nameservers or []
        self.additional_args = additional_args or ['+short']
        self.encoding = encoding

    @property
    def nameserver(self):
        """
        Returns a random nameserver we should query against
        """
        return random.choice(self.nameservers)

    @staticmethod
    def _execute(args):
        """
        Calls out to subprocess with the passed in args
        This method is normally mocked in tests
        """
        logger.info(f"Executing subprocess.check_output({repr(args)})")
        return subprocess.check_output(args)

    def _args(self, domain, dns_type):
        """
        Builds up the final arguments to pass into subprocess
        dig @1.1.1.1 domain.tld A +short
        """
        yield self.executable

        # Add in a random nameserver
        if self.nameservers:
            yield f"@{self.nameserver}"

        # The record we want to query
        yield domain

        # Our query type
        yield dns_type.name

        # Add in any additional args
        yield from self.additional_args

    def query(self, domain, dns_type):
        """
        Queries the resolver for a specific domain and query type
        Returns a list of records
        """
        domain = domain.lower()
        dns_type = DNSType.get(dns_type)

        args = list(self._args(domain, dns_type))
        output = self._execute(args).decode(self.encoding).strip()

        return output.split('\n') if output else []
