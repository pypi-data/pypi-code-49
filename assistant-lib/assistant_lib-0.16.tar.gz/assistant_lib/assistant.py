#!/usr/bin/python3
# -*- coding: utf-8 -*-

import logging
import logging.config

from datetime import datetime
import socket
from contextlib import closing
from netifaces import interfaces, ifaddresses, AF_INET, AF_INET6
import platform
import os
import sys
import traceback
from threading import Thread, Event
import time
import json
from setuptools_scm import get_version

class AssistantClient:

    def __init__(self):
        """
        Check if Python 3
        Init logging engine
        """
        self.check_if_python3()
        self.init_logging()

    def check_if_python3(self):
        """
        We check if we are running Python 3.
        It may work in python 2.7 but we want to be sure to avoid issues ;)
        """
        if sys.version_info.major != 3:
            logging.error("This program must be run with Python 3.x! Exiting...")
            sys.exit(1)

    def get_version(self):
        """
        Get the version from the SCM (git)
        """
        return get_version(root='..', relative_to=__file__)

    def init_logging(self):
        """
        Depending on the following variables, the logging will be different :
        LOG_OUTPUT
          - TTY : if TTY, log on the standard output (the console)
          - others values : log in a file
        LOG_FILE : the name of the file to log in. Default : ./assistant.log
          When we log in a file, we log in json format by default.
        LOG_LEVEL : the log level
          - DBEUG
          - INFO
          - WARNING
          - ERROR

        Sample of a Go part json log message :
        {"application":"webguiserver","component":"WebSocket client lib","component_version":"0.1","discussion_id":"","host_id":"n/a","host_os_arch":"linux-amd64","level":"in
        fo","msg":"Your name is : root","time":"2019-12-16T14:43:54Z"}

        Sample of a default python-json-logger message :
        {"asctime": "2020-01-08 11:30:57,615", "levelname": "WARNING", "name": "root", "message": "A warning message"}

        /!\ We can see that the fields name are not the same as the python default ones...
            We can also see that the datetime format is not ISO 8601 in python

        => we will change the default python behaviour in order to have similar logs in Python and Go parts.
        """
        self.log_type = None
        if 'LOG_OUTPUT' in os.environ:
            log_output = os.environ['LOG_OUTPUT']
            if log_output == "TTY":
                handler = "TTY"
            else:
                handler = "FILE"
        else:
            log_output = None
            handler = "FILE"

        if 'LOG_FILE' in os.environ:
            log_file = os.environ['LOG_FILE']
        else:
            log_file = 'assistant.log'

        if 'LOG_LEVEL' in os.environ:
            log_level = os.environ['LOG_LEVEL'].upper()
        else:
            log_level = 'DEBUG'

        if handler == "FILE":
            print("The application will log in the file '{0}'. To log in the console, set this variable : export LOG_OUTPUT=TTY".format(log_file))
            self.log_type = "json"


        # inspired from https://stackoverflow.com/questions/7507825/where-is-a-complete-example-of-logging-config-dictconfig
        # and : https://bitbucket.org/bear_belly/json_log_formatter/src/master/python3_json_log_formatter/__init__.py
        config = {
            'version': 1,
            'formatters': {
                'standard': {
                    'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
                },
                'json': {
                    'format': '%(message)s',
                    'class': 'assistant_lib.jsonlogger.JsonFormatter',
                },
            },
            'handlers': {
                'TTY': {
                    'formatter': 'standard',
                    'class': 'logging.StreamHandler',
                    'stream': 'ext://sys.stdout',  # Default is stderr
                },
                'FILE': {
                    'formatter': 'json',
                    'class': 'logging.handlers.RotatingFileHandler',
                    'filename': log_file,
                    'mode': 'a',
                    'maxBytes': 1048576,
                    'backupCount': 10
                },
            },
            'loggers': {
                '': {  # root logger
                    'handlers': [handler],
                    'level': log_level,
                    'propagate': False
                },
            }
        }

        logging.config.dictConfig(config)
        logging.info("---- STARTING ----")


    def build_server_informations(self, address, roles):
        """
        Build the message to send for discovery

        Parameters:

        address (string): ip:port
        roles (list of string) : ocr, motion.detection, ...

        Returns:

        (json as string) : {"address" : <ip>:<port>, "roles": [<role1>, <role2>, ....], "name": <role1>@<hostname>}
        """
        hostname = self.get_hostname()
        name = "{0}@{1}".format(roles[0], hostname)
        return json.dumps({"address" : address, "roles" : roles, "name" : name})

    class ShowMeToTheLan (Thread):

        def __init__(self, message):
            self.discovery_srv_addr         = ('224.0.0.1', 9999)
            # TODO : not needed for now : used only for reading
            # discovery_max_datagramSize = 8192
            self.discovery_delay_seconds    = 5
            self.message = message
            self.evt = Event()
            Thread.__init__(self)

        def run(self):
            try:
                logging.info("Start ShowMeToTheLAN : we will emit a 'alive' message each {0} seconds".format(self.discovery_delay_seconds))
                logging.info("The alive message will be : {0}".format(self.message))

                # Create a UDP socket
                sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
                sock.settimeout(5)

            except:
                logging.error("ShowMeToTheLAN : Error while initiating UDP dialog : {0}".format(traceback.format_exc()))
                sys.exit(1)

            while not self.evt.is_set():
                #logging.debug("ShowMeToTheLAN : send '{0}'".format(self.message))
                sock.sendto(self.message.encode(), self.discovery_srv_addr)
                self.evt.wait(self.discovery_delay_seconds)

    def get_hostname(self):
        return platform.node().split('.')[0]

    def get_main_ip(self):
        """
        Return the first ip which is not 127.*

        Parameters:

        n/a

        Returns:

        (string): ip address
        """
        for intf in interfaces():
            for addr in ifaddresses(intf)[AF_INET]:   # TODO : upgrade here to handle ipv6
                ip = addr['addr']
                if not ip.startswith("127.0"):
                    logging.info("Main ip is : {0}".format(ip))
                    return ip
        return None

    def find_free_port(self):
        """
        Find a free port and return it

        Parameters:

        n/a

        Returns:

        (int): a free port
        """
        with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as s:
            s.bind(('', 0))
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            logging.info("Free port found : '{0}'".format(s.getsockname()))
            return s.getsockname()[1]

    def generate_selfsigned_cert(self, cert_file, key_file, hostname, public_ip, private_ip):
        """
        Generate a self signed certificate for the webserver.
        If the files already exist, do nothing

        Parameters:

        cert_file (string): path to the cert file
        key_file (string): path to the key file
        hostname (string): the hostname
        public_ip (string): the public ip
        private_ip (string): the private ip

        Returns:

        n/a
        """
        try:
            # 1. check if the both files exist
            if os.path.isfile(cert_file) and os.path.isfile(key_file):
                logging.info("SSL : certificate and key files are already generated :)")
                return

            # 2. if not, generate the data
            logging.info("SSL : no certificate and key file are present. Generating them...")
            cert, key = self.get_selfsigned_cert(hostname, public_ip, private_ip)

            # 3. and write the files :)
            fp = open(cert_file, "w")
            fp.write(cert.decode("utf-8") )
            fp.close()

            fp = open(key_file, "w")
            fp.write(key.decode("utf-8") )
            fp.close()

            logging.info("SSL : files generated!")
        except:
            logging.error("SSL : Unable to generate the certificate and key files. The error is : {0}".format(traceback.format_exc()))

    # From : https://gist.github.com/bloodearnest/9017111a313777b9cce5
    def get_selfsigned_cert(self, hostname, public_ip, private_ip):
        from cryptography import x509
        from cryptography.x509.oid import NameOID
        from cryptography.hazmat.primitives import hashes
        from cryptography.hazmat.backends import default_backend
        from cryptography.hazmat.primitives import serialization
        from cryptography.hazmat.primitives.asymmetric import rsa

        # Fritz - patch to allow just string as input :)
        import ipaddress
        from datetime import datetime, timedelta
        #public_ip = ipaddress.ip_address(public_ip)
        #private_ip = ipaddress.ip_address(private_ip)
        # Fritz - end patch

        # Generate our key
        key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
            backend=default_backend()
        )

        name = x509.Name([
            x509.NameAttribute(NameOID.COMMON_NAME, hostname)
        ])
        alt_names = x509.SubjectAlternativeName([
            # best practice seem to be to include the hostname in the SAN, which *SHOULD* mean COMMON_NAME is ignored.
            x509.DNSName(hostname),
            # allow addressing by IP, for when you don't have real DNS (common in most testing scenarios)
            # openssl wants DNSnames for ips...
            x509.DNSName(public_ip),
            x509.DNSName(private_ip),
            # ... whereas golang's crypto/tls is stricter, and needs IPAddresses
            x509.IPAddress(ipaddress.IPv4Address(public_ip)),
            x509.IPAddress(ipaddress.IPv4Address(private_ip)),
        ])
        # path_len=0 means this cert can only sign itself, not other certs.
        basic_contraints = x509.BasicConstraints(ca=True, path_length=0)
        now = datetime.utcnow()
        cert = (
            x509.CertificateBuilder()
            .subject_name(name)
            .issuer_name(name)
            .public_key(key.public_key())
            .serial_number(1000)
            .not_valid_before(now)
            .not_valid_after(now + timedelta(days=10*365))
            .add_extension(basic_contraints, False)
            .add_extension(alt_names, False)
            .sign(key, hashes.SHA256(), default_backend())
        )
        cert_pem = cert.public_bytes(encoding=serialization.Encoding.PEM)
        key_pem = key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.NoEncryption(),
        )

        #print(cert_pem)
        #print(key_pem)
        return cert_pem, key_pem



# Just some manuel tests
if __name__ == "__main__":
    #ac = AssistantClient("test", "1.0")
    COMPONENT = "TEST"
    VERSION = "1.0"
    ac = AssistantClient()
    ac.find_free_port()
    logging.info("Version: {0}".format(ac.get_version()))
    thread_show_me_to_the_lan = ac.ShowMeToTheLan(ac.build_server_informations("0.1.2.3", ["Role"]))
    thread_show_me_to_the_lan.start()
    logging.info("A log line out of AssistantClient")
    logging.info("A log line out of AssistantClient with a percent arg: '%s'".format("tststr"))
    logging.info("A log line out of AssistantClient with a hymen arg: '{0}'".format("tststr"))
