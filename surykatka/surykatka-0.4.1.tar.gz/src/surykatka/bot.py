# Copyright (C) 2019  Nexedi SA and Contributors.
#                     Romain Courteaud <romain@nexedi.com>
#
# This program is free software: you can Use, Study, Modify and Redistribute
# it under the terms of the GNU General Public License version 3, or (at your
# option) any later version, as published by the Free Software Foundation.
#
# You can also Link and Combine this program with other software covered by
# the terms of any of the Free Software licenses or any of the Open Source
# Initiative approved licenses and Convey the resulting work. Corresponding
# source of such a combination shall include the source code for all other
# software used.
#
# This program is distributed WITHOUT ANY WARRANTY; without even the implied
# warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
#
# See COPYING file for full licensing terms.
# See https://www.nexedi.com/licensing for rationale and options.

import time
from .db import LogDB
from .configuration import createConfiguration, logConfiguration
from .status import logStatus, reportStatus
from .dns import (
    getReachableResolverList,
    expandDomainList,
    getDomainIpDict,
    reportDnsQuery,
)
from .http import getRootUrl, getUrlHostname, checkHttpStatus, reportHttp
from .network import isTcpPortOpen, reportNetwork
import json
import email.utils
from collections import OrderedDict
from .ssl import hasValidSSLCertificate, reportSslCertificate


__version__ = "0.4.1"


class BotError(Exception):
    pass


def rfc822(date):
    return email.utils.format_datetime(date)


class WebBot:
    def __init__(self, **kw):
        self.config_kw = kw
        self.config = createConfiguration(**kw)

    def closeDB(self):
        if hasattr(self, "_db"):
            self._db.close()

    def initDB(self):
        self._db = LogDB(self.config["SQLITE"])
        self._db.createTables()

    def calculateUrlList(self):
        return self.config["URL"].split()

    def calculateFullDomainList(self):
        # Calculate the full list of domain to check
        domain_list = self.config["DOMAIN"].split()

        # Extract the list of URL domains
        url_list = self.calculateUrlList()
        for url in url_list:
            domain = getUrlHostname(url)
            if domain is not None:
                domain_list.append(domain)
        domain_list = list(set(domain_list))

        # Expand with all parent domains
        return expandDomainList(domain_list)

    def iterateLoop(self):
        status_id = logStatus(self._db, "loop")

        if self.config["RELOAD"] == "True":
            self.config = createConfiguration(**self.config_kw)

        timeout = int(self.config["TIMEOUT"])
        elapsed_fast = float(self.config["ELAPSED_FAST"])
        elapsed_moderate = float(self.config["ELAPSED_moderate"])
        # logPlatform(self._db, __version__, status_id)

        # Calculate the resolver list
        resolver_ip_list = getReachableResolverList(
            self._db, status_id, self.config["NAMESERVER"].split(), timeout
        )
        if not resolver_ip_list:
            return

        # Get list of all domains
        domain_list = self.calculateFullDomainList()

        # Get the list of server to check
        # XXX Check DNS expiration
        server_ip_dict = getDomainIpDict(
            self._db, status_id, resolver_ip_list, domain_list, "A", timeout
        )

        # Check TCP port for the list of IP found
        # XXX For now, check http/https only
        server_ip_list = [x for x in server_ip_dict.keys()]
        url_dict = {}
        for server_ip in server_ip_list:
            # XXX Check SSL certificate expiration
            for port, protocol in [(80, "http"), (443, "https")]:
                if isTcpPortOpen(
                    self._db, server_ip, port, status_id, timeout
                ):
                    for hostname in server_ip_dict[server_ip]:
                        if port == 443:
                            # Store certificate information
                            if not hasValidSSLCertificate(
                                self._db,
                                server_ip,
                                port,
                                hostname,
                                status_id,
                                timeout,
                            ):
                                # If certificate is not valid,
                                # no need to do another query
                                continue
                        url = "%s://%s" % (protocol, hostname)
                        if url not in url_dict:
                            url_dict[url] = []
                        url_dict[url].append(server_ip)

        # XXX put back orignal url list
        for url in self.calculateUrlList():
            if url not in url_dict:
                root_url = getRootUrl(url)
                if root_url in url_dict:
                    url_dict[url] = url_dict[root_url]

        # Check HTTP Status
        for url in url_dict:
            for ip in url_dict[url]:
                checkHttpStatus(
                    self._db,
                    status_id,
                    url,
                    ip,
                    __version__,
                    timeout,
                    elapsed_fast,
                    elapsed_moderate,
                )
                # XXX Check location header and check new url recursively
                # XXX Parse HTML, fetch found link, css, js, image
                # XXX Check HTTP Cache

    def status(self):
        result_dict = OrderedDict()

        # Report the bot status
        result_dict["bot_status"] = []
        try:
            status = reportStatus(self._db).get()
        except self._db.Status.DoesNotExist:
            pass
        else:
            result_dict["bot_status"].append(
                {"text": status.text, "date": rfc822(status.timestamp)}
            )

        # Report the list of DNS server status
        query = reportNetwork(
            self._db,
            port="53",
            transport="UDP",
            ip=self.config["NAMESERVER"].split(),
        )
        resolver_ip_list = []
        result_dict["dns_server"] = []
        for network_change in query.dicts().iterator():
            if network_change["state"] == "open":
                resolver_ip_list.append(network_change["ip"])
            result_dict["dns_server"].append(
                {
                    "ip": network_change["ip"],
                    "state": network_change["state"],
                    "date": rfc822(network_change["status"]),
                }
            )

        domain_list = self.calculateFullDomainList()
        # Report list of DNS query
        query = reportDnsQuery(
            self._db,
            domain=domain_list,
            resolver_ip=resolver_ip_list,
            rdtype="A",
        )
        server_ip_dict = {}
        result_dict["dns_query"] = []
        for dns_change in query.dicts().iterator():
            result_dict["dns_query"].append(
                {
                    "domain": dns_change["domain"],
                    "resolver_ip": dns_change["resolver_ip"],
                    "date": rfc822(dns_change["status"]),
                    "response": dns_change["response"],
                }
            )
            for server_ip in dns_change["response"].split(", "):
                if not server_ip:
                    # drop empty response
                    continue
                if server_ip not in server_ip_dict:
                    server_ip_dict[server_ip] = []
                if dns_change["domain"] not in server_ip_dict[server_ip]:
                    server_ip_dict[server_ip].append(dns_change["domain"])

        # Report the list of CDN status
        query = reportNetwork(
            self._db,
            port=["80", "443"],
            transport="TCP",
            ip=[x for x in server_ip_dict.keys()],
        )
        url_dict = {}
        result_dict["http_server"] = []
        for network_change in query.dicts().iterator():
            result_dict["http_server"].append(
                {
                    "ip": network_change["ip"],
                    "state": network_change["state"],
                    "port": network_change["port"],
                    "date": rfc822(network_change["status"]),
                    "domain": ", ".join(server_ip_dict[network_change["ip"]]),
                }
            )
            if network_change["state"] == "open":
                for hostname in server_ip_dict[network_change["ip"]]:
                    protocol = (
                        "http" if (network_change["port"] == 80) else "https"
                    )
                    url = "%s://%s" % (protocol, hostname)
                    if url not in url_dict:
                        url_dict[url] = []
                    url_dict[url].append(network_change["ip"])

        # Report the SSL status
        query = reportSslCertificate(
            self._db,
            ip=[x for x in server_ip_dict.keys()],
            port=443,
            hostname=domain_list,
        )
        result_dict["ssl_certificate"] = []
        for ssl_certificate in query.dicts().iterator():
            result_dict["ssl_certificate"].append(
                {
                    "hostname": ssl_certificate["hostname"],
                    "ip": ssl_certificate["ip"],
                    "port": ssl_certificate["port"],
                    "sha1_fingerprint": ssl_certificate["sha1_fingerprint"],
                    "subject": ssl_certificate["subject"],
                    "issuer": ssl_certificate["issuer"],
                    "not_before": rfc822(ssl_certificate["not_before"])
                    if (ssl_certificate["not_before"] is not None)
                    else None,
                    "not_after": rfc822(ssl_certificate["not_after"])
                    if (ssl_certificate["not_after"] is not None)
                    else None,
                    "date": rfc822(ssl_certificate["status"]),
                }
            )

        # XXX put back orignal url list
        for url in self.calculateUrlList():
            if url not in url_dict:
                root_url = getRootUrl(url)
                if root_url in url_dict:
                    url_dict[url] = url_dict[root_url]

        # Get the list of HTTP servers to check
        query = reportHttp(
            self._db,
            ip=[x for x in server_ip_dict.keys()],
            url=[x for x in url_dict.keys()],
        )
        result_dict["http_query"] = []
        for network_change in query.dicts().iterator():
            result_dict["http_query"].append(
                {
                    "status_code": network_change["status_code"],
                    "total_seconds": network_change["total_seconds"],
                    "url": network_change["url"],
                    "ip": network_change["ip"],
                    "date": rfc822(network_change["status"]),
                }
            )

        return result_dict

    def stop(self):
        self._running = False
        logStatus(self._db, "stop")

    def crawl(self):
        status_id = logStatus(self._db, "start")
        logConfiguration(self._db, status_id, self.config)

        self._running = True
        try:
            while self._running:
                self.iterateLoop()
                interval = int(self.config.get("INTERVAL"))
                if interval < 0:
                    self.stop()
                else:
                    time.sleep(interval)
        except KeyboardInterrupt:
            self.stop()
        except:
            # XXX Put traceback in the log?
            logStatus(self._db, "error")
            raise

    def run(self, mode):
        status_dict = None
        if mode not in ["crawl", "status"]:
            raise NotImplementedError("Unexpected mode: %s" % mode)

        if self.config["SQLITE"] == ":memory:":
            # Crawl/report are mandatory when using memory
            mode = "all"

        self.initDB()

        try:
            if mode in ["crawl", "all"]:
                self.crawl()
            if mode in ["status", "all"]:
                status_dict = self.status()
        except:
            self.closeDB()
            raise
        else:
            self.closeDB()

        if status_dict is not None:
            if self.config["FORMAT"] == "json":
                print(json.dumps(status_dict))
            else:
                for table_key in status_dict:
                    print("# %s" % table_key)
                    print("")
                    table = status_dict[table_key]
                    if table:
                        # Print the header
                        table_key_list = [x for x in table[0].keys()]
                        table_key_list.sort()
                        print(" | ".join(table_key_list))
                        for line in table:
                            print(
                                " | ".join(
                                    ["%s" % (line[x]) for x in table_key_list]
                                )
                            )
                        print("")


def create_bot(**kw):
    return WebBot(**kw)
