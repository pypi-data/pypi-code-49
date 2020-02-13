#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#    jhSitemapgenerator.py
#    A multithreaded commandline tool to create sitemap.xml|.gz|.txt files from a website.
#
#    Copyright (C) 2014 by Jan Helbling <jan.helbling@mailbox.org>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

import urllib.request
import urllib.parse
import urllib.error
import http
import re
import gzip
from threading import Thread, Lock
from optparse import OptionParser

VERSION = "0.1.2"

scanned_urls = []
urls_to_scan = []
not_html_urls = []

exit_success = True

url_regex = re.compile(
    '[>< ]{1,4}[aA]{1,1}[ ]{0,4}[hrefHREF]{4}[ ]{0,4}\="([a-zA-Z0-9\.,_\-/~\\=\?\(\)\+\[\]\{\}<>\|@\*;: %\&\$£€üäöÖÄÜéàèç!\^]+)"[ ><]{0,4}'
)
bad_urlschemes_regex = re.compile(
    "(aaa|aaas|about|acap|acct|adiumxtra|afp|afs|aim|app|apt|attachment|aw|barion|beshare|bitcoin|bolo|callto|cap|chrome|chrome-extension|com-eventbrite-attendee|cid|coap|coaps|content|crid|cvs|data|dav|dict|dlna-playsingle|dlna-playcontainer|dns|dtn|dvb|ed2k|facetime|fax|feed|file|finger|fish|ftp|geo|git|gizmoproject|go|gopher|gt|gtalk|h323|hcp|iax|icap|icon|im|imap|info|ipn|ipp|irc|irc6|ircs|iris|iris.beep|iris.xpc|iris.xpcs|iris.iws|itms|jabber|jar|jms|keyparc|lastfm|ldap|ldaps|magnet|mailserver|mailto|maps|market|message|mms|modem|ms-help|ms-settings-power|msnim|msrp|msrps|mtqp|mumble|mupdate|mvn|news|nfs|ni|nih|nntp|notes|oid|opaquelocktoken|outlook|pack|palm|paparazzi|pkcs11|platform|pop|prospero|proxy|psyc|query|reload|res|ressource|rmi|rsync|rtmfp|rtmp|rtsp|samp|secondlife|service|session|sftp|sgn|shttp|sieve|sip|sips|skype|smb|snews|snmp|soap.beep|soap.beeps|soldat|spotify|ssh|steam|stun|stuns|svn|tag|teamspeak|tel|telnet|tftp|things|thismessage|tn3270|tip|turn|turns|tv|udp|unreal|urmn|ut2004|vemmi|ventrillo|videotex|view-source|wais|webcal|ws|wss|wtai|wyciwyg|xcon|xcon-userid|xfire|xmlrpc.beep|xmlrpc.beeps|xmpp|xri|ymsgr|z39.50|z39.50r|z39.50s|doi|jdbc|stratum|javascript):"
)


class jhSitemapgenerator:
    def __init__(self, url, thread_cnt, gz, plaintext, lock):
        global urls_to_scan
        tmp_url_parsed = urllib.parse.urlparse(url)
        if bad_urlschemes_regex.match(url):
            print(
                "What's '{}://' for a scheme? Try http:// or https://!".format(
                    tmp_url_parsed.scheme
                )
            )
            exit(1)
        elif tmp_url_parsed.scheme not in ["http", "https"]:
            print("You need to add https:// or http:// bevore the url!")
            exit(1)
        else:
            url = tmp_url_parsed.scheme + "://"
        if not tmp_url_parsed.netloc:
            print("Error: You must provide a hostname or a ipaddress!")
            exit(1)
        else:
            url = url + tmp_url_parsed.netloc
        if tmp_url_parsed.path:
            url = url + tmp_url_parsed.path
        else:
            url = url + "/"
        if tmp_url_parsed.params:
            url = url + ";" + tmp_url_parsed.params
        if tmp_url_parsed.query:
            url = url + "?" + tmp_url_parsed.query
        del tmp_url_parsed
        urls_to_scan = [url]
        self.thread_cnt = thread_cnt
        self.threads = []
        self.gz = gz
        self.plaintext = plaintext
        self.lock = lock
        self.__run__()

    def __run__(self):
        self.parsedurl = urllib.parse.urlparse(urls_to_scan[0])
        self.host = self.parsedurl.netloc
        self.path = self.parsedurl.path
        while True:
            self.threads = []
            if urls_to_scan.__len__() == 0:
                break
            if urls_to_scan.__len__() == 1:
                self.threads.append(Thread(target=self.__run_thread__))
            elif self.thread_cnt > urls_to_scan.__len__() - 1:
                for i in range(0, urls_to_scan.__len__() - 1):
                    self.threads.append(Thread(target=self.__run_thread__))
            else:
                for i in range(0, self.thread_cnt):
                    self.threads.append(Thread(target=self.__run_thread__))
            for thread in self.threads:
                thread.start()
            for thread in self.threads:
                thread.join()
            del self.threads
        self.__write_urls__(scanned_urls)

    def __run_thread__(self):
        global urls_to_scan, scanned_urls, not_html_urls
        with self.lock:
            current_url = urls_to_scan.pop()
        if current_url in urls_to_scan:
            with self.lock:
                urls_to_scan.remove(current_url)
        content = self.__get_page__(current_url)
        if content != None and current_url not in scanned_urls:
            print("Scanned URL:", current_url)
            with self.lock:
                scanned_urls.append(current_url)
            tmp_urls = self.__extract_urls__(content)
            for url in tmp_urls:
                if (
                    url not in scanned_urls
                    and url not in urls_to_scan
                    and url not in not_html_urls
                ):
                    with self.lock:
                        urls_to_scan.append(url)
        else:
            with self.lock:
                not_html_urls.append(current_url)

    def __extract_urls__(self, content):
        tmp_urls = url_regex.findall(content)
        urls_to_return = []
        for url_to_parse in tmp_urls:
            if not bad_urlschemes_regex.match(url_to_parse):
                url_to_parse = self.__replace_html_chars__(url_to_parse)
                if url_to_parse.startswith("http"):
                    p = urllib.parse.urlparse(url_to_parse)
                    if p.scheme == "":
                        parsed_url = "http://"
                    else:
                        parsed_url = p.scheme + "://"
                    if p.netloc == "":
                        parsed_url = parsed_url + self.host
                    elif self.host in p.netloc:
                        parsed_url = parsed_url + p.netloc
                    if (
                        p.path != ""
                        and not p.path.startswith("/")
                        and not p.path.startswith(".")
                    ):
                        parsed_url = parsed_url + "/" + p.path
                    elif p.path.startswith("/"):
                        parsed_url = parsed_url + p.path
                    else:
                        parsed_url = parsed_url + "/"
                    if p.params != "":
                        parsed_url = parsed_url + ";" + p.params
                    if p.query != "":
                        parsed_url = parsed_url + "?" + p.query
                    if self.host in parsed_url:
                        urls_to_return.append(parsed_url)
                else:
                    if url_to_parse.startswith("/"):
                        urls_to_return.append("http://" + self.host + url_to_parse)
                    else:
                        urls_to_return.append(
                            "http://" + self.host + "/" + url_to_parse
                        )
        return urls_to_return

    def __write_urls__(self, url_list):
        global exit_success
        if url_list.__len__() != 0:
            try:
                self.fd = open("sitemap.xml", "w")
                self.fd.write('<?xml version="1.0" encoding="UTF-8"?>\n')
                self.fd.write("<urlset\n")
                self.fd.write(
                    '      xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"\n'
                )
                self.fd.write(
                    '      xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"\n'
                )
                self.fd.write(
                    '      xsi:schemaLocation="http://www.sitemaps.org/schemas/sitemap/0.9\n'
                )
                self.fd.write(
                    '            http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd">\n'
                )
                for url in scanned_urls:
                    self.fd.write("<url>\n")
                    self.fd.write("  <loc>{}</loc>\n".format(url))
                    self.fd.write("</url>\n")
                self.fd.write("</urlset>\n")
                self.fd.close()
                print("Written {} URL's to sitemap.xml".format(len(scanned_urls)))
            except OSError as e:
                print("Failed to open {}: {}.".format(e.filename, e.strerror))
                exit_successs = False
            if self.gz:
                try:
                    self.fd = gzip.open("sitemap.xml.gz", "wb")
                    self.fd.write(
                        '<?xml version="1.0" encoding="UTF-8"?>\n'.encode(
                            "utf-8", "strict"
                        )
                    )
                    self.fd.write("<urlset\n".encode("utf-8", "strict"))
                    self.fd.write(
                        '      xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"\n'.encode(
                            "utf-8", "strict"
                        )
                    )
                    self.fd.write(
                        '      xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"\n'.encode(
                            "utf-8", "strict"
                        )
                    )
                    self.fd.write(
                        '      xsi:schemaLocation="http://www.sitemaps.org/schemas/sitemap/0.9\n'.encode(
                            "utf-8", "strict"
                        )
                    )
                    self.fd.write(
                        '            http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd">\n'.encode(
                            "utf-8", "strict"
                        )
                    )
                    for url in scanned_urls:
                        self.fd.write("<url>\n".encode("utf-8", "strict"))
                        self.fd.write(
                            "  <loc>{}</loc>\n".format(url).encode("utf-8", "strict")
                        )
                        self.fd.write("</url>\n".encode("utf-8", "strict"))
                    self.fd.write("</urlset>\n".encode("utf-8", "strict"))
                    self.fd.close()
                    print(
                        "Written {} URL's to sitemap.xml.gz".format(len(scanned_urls))
                    )
                except OSError as e:
                    print("Failed to open {}: {}.".format(e.filename, e.strerror))
                    exit_success = False
            if self.plaintext:
                try:
                    self.fd = open("urllist.txt", "w")
                    for url in scanned_urls:
                        self.fd.write("{}\n".format(url))
                    self.fd.close()
                    print("Written {} URL's to urllist.txt".format(len(scanned_urls)))
                except OSError as e:
                    print("Failed to open {}: {}.".format(e.filename, e.strerror))
                    exit_success = False
        if exit_success:
            exit(0)
        exit(1)

    def __get_page__(self, url):
        global exit_success
        try:
            fd = urllib.request.urlopen(url)
            if "text/html" not in fd.getheader("content-type"):
                fd.close()
                return None
            return (fd.read()).decode("utf-8", "ignore")
        except urllib.error.HTTPError as e:
            print("Error opening {}: {}.".format(e.geturl(), e.reason))
        except UnicodeEncodeError:
            return None
        except IOError as e:
            print("Error: {0}".format(e.args[0]))
            exit_success = False
        except http.client.InvalidURL:
            pass

    def __replace_html_chars__(self, url):
        return (
            url.replace("&AMP;", "&")
            .replace("&LT;", "<")
            .replace("&GT;", ">")
            .replace("&NBSP;", " ")
            .replace("&EURO;", "€")
            .replace("&amp;", "&")
            .replace("&lt;", "<")
            .replace("&gt;", ">")
            .replace("&nbsp;", " ")
            .replace("&euro;", "€")
            .replace("%3f", "?")
            .replace("%2B", "+")
            .replace("%2F", "/")
            .replace("%3D", "=")
            .replace("%7C", "|")
            .replace("%26", "&")
            .replace("%25", "%")
            .replace("%2C", ",")
            .replace("%3A", ":")
            .replace("%3B", ";")
            .replace("%3f", "?")
            .replace("%2b", "+")
            .replace("%2f", "/")
            .replace("%3d", "=")
            .replace("%7c", "|")
            .replace("%2c", ",")
            .replace("%3a", ":")
            .replace("%3b", ";")
        )


if __name__ == "__main__":
    parser = OptionParser(
        usage="%prog <http://|https:// -URL> [args]",
        version="%prog version {}\nLicense: GPL3+\nAuthor: Jan Helbling <jan.helbling@mailbox.org>".format(
            VERSION
        ),
    )
    parser.add_option(
        "-t",
        "--threads",
        type="int",
        dest="threads",
        default=10,
        help="Number of threads, default 10.",
    )
    parser.add_option(
        "-g",
        "--gz",
        action="store_true",
        dest="gz",
        default=False,
        help="Also create a sitemap.xml.gz",
    )
    parser.add_option(
        "-p",
        "--plaintext",
        action="store_true",
        dest="plaintext",
        default=False,
        help="Also create a urllist.txt",
    )
    (options, args) = parser.parse_args()

    if len(args) != 1:
        print("You must provide one url! Use -h to display options.")
        exit(1)
    lock = Lock()
    jhS = jhSitemapgenerator(
        args[0], options.threads, options.gz, options.plaintext, lock
    )
