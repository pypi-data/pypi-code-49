# -*- coding: utf-8 -*-
"""Auth class file."""

import os
import sys

from bits.secrets import Secrets

# import bits-api-python-client
mypath = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(mypath, "bits-api-python-client"))

# pylama: ignore=E402


class Auth(object):
    """Auth class."""

    def __init__(self, settings, verbose=False, yes=False):
        """Initialize an Auth class instance."""
        self.settings = settings
        self.verbose = verbose
        self.yes = yes

        self.smproject = 'broad-bits-vault'
        self.secrets = Secrets(default_project=self.smproject)

    def accounts(
            self,
            ad=None,
            google=None,
            mongo=None,
            nis=None,
            people=None,
            slack=None,
            verbose=False,
            yes=False,
    ):
        """Connect to accounts class and all subclasses."""
        from bitsapiclient.services.accounts import Accounts
        if not ad:
            ad = self.ad()
        if not google:
            google = self.google()
        if not mongo:
            mongo = self.mongo()
        if not nis:
            nis = self.nis()
        if not people:
            people = self.people()
        if not slack:
            slack = self.slack()
        if not verbose:
            verbose = self.verbose
        if not yes:
            yes = self.yes

        return Accounts(
            ad=ad,
            google=google,
            mongo=mongo,
            nis=nis,
            people=people,
            slack=slack,
            verbose=verbose,
            yes=yes
        )

    def ad(self):
        """Connect to Active Directory LDAP."""
        from bitsapiclient.services.ad import AD
        params = self.secrets.resolve({
            'ldap_uri': self.settings['ldap_servers']['ad_ldap']['uri'],
            'ldap_bind_dn': self.settings['ldap_servers']['ad_ldap']['bind_dn'],
            'ldap_bind_pw': self.settings['ldap_servers']['ad_ldap']['bind_pw'],
            'ldap_base_dn': self.settings['ldap_servers']['ad_ldap']['base_dn'],
            'verbose': self.verbose,
        })
        return AD(**params)

    def angus(self):
        """Connect to Angus."""
        from bitsapiclient.services.angus import Angus
        params = self.secrets.resolve({
            'host': self.settings['angus']['host'],
            'user': self.settings['angus']['user'],
            'password': self.settings['angus']['pass'],
            'path': self.settings['angus']['path'],
            'verbose': self.verbose,
        })
        return Angus(**params)

    def aws(self):
        """Connect to AWS API."""
        from bitsapiclient.services.aws import AWS
        params = self.secrets.resolve({
            'auth': self,
            'aws_access_key_id': self.settings['aws']['access_key_id'],
            'aws_secret_access_key': self.settings['aws']['secret_access_key'],
            'root_account': self.settings['aws']['root_account'],
            'verbose': self.verbose,
        })
        return AWS(**params)

    def backupify(self):
        """Connect to Backupify API."""
        from bits.backupify import Backupify
        params = self.secrets.resolve({
            'client_id': self.settings['backupify']['clientid'],
            'client_secret': self.settings['backupify']['clientsecret'],
            'verbose': self.verbose,
        })
        return Backupify(**params)

    def bettercloud(self):
        """Connect to BetterCloud API."""
        from bitsapiclient.services.bettercloud import BetterCloud
        params = self.secrets.resolve({
            'token': self.settings['bettercloud']['token'],
            'verbose': self.verbose,
        })
        return BetterCloud(**params)

    def bit(self):
        """Connect to BIT app."""
        from bitsapiclient.services.bit import BIT
        params = self.secrets.resolve({
            'user': self.settings['bit']['user'],
            'group': self.settings['bit']['group'],
            'workday_dir': self.settings['bit']['workday_dir'],
            'verbose': self.verbose,
        })
        return BIT(**params)

    def bitsbot_cloud(self):
        """Connect to BITSbot cloud API."""
        from bitsapiclient.services.endpoints import Endpoints
        params = self.secrets.resolve({
            'host': self.settings['bitsbot']['api_host'],
            'api_key': self.settings['bitsbot']['api_key'],
        })
        return Endpoints(**params)

    def bitsdb_cloud(self):
        """Connect to BITSdb cloud API."""
        from bitsapiclient.services.endpoints import Endpoints
        params = self.secrets.resolve({
            'host': self.settings['bitsdb']['endpoints']['api_host'],
            'api_key': self.settings['bitsdb']['endpoints']['api_key'],
        })
        return Endpoints(**params)

    def bitsdb_local(self):
        """Connect to BITSdb local API."""
        from bitsapiclient.services.endpoints import Endpoints
        params = self.secrets.resolve({
            'host': self.settings['bitsdb']['local']['api_host'],
            'api_key': self.settings['bitsdb']['local']['api_key'],
        })
        return Endpoints(**params)

    def bitsdb_mongo(self):
        """Connect to BITSdb Mongo DB."""
        from bitsapiclient.services.bitsdb import BITSdb
        params = self.secrets.resolve({
            'mongo_uri': self.settings['mongo']['bitsdb']['uri'],
            'mongo_db': self.settings['mongo']['bitsdb']['db'],
            # 'verbose': self.verbose,
        })
        return BITSdb().MongoDb(**params)

    def bitsdb_update(self):
        """Connect to BITSdb Mongo DB."""
        from bitsapiclient.services.bitsdb import BITSdb
        params = self.secrets.resolve({
            'mongo_uri': self.settings['mongo']['bitsdb']['uri'],
            'mongo_db': self.settings['mongo']['bitsdb']['db'],
            # 'verbose': self.verbose,
        })
        return BITSdb().MongoDb(**params)

    def bitsdbapi(self):
        """Connect to BITSdb API."""
        from bitsapiclient.services.bitsdbapi import BitsdbApi
        params = self.secrets.resolve({
            'api_key': self.settings['bitsdbapi']['api_key'],
            'base_url': self.settings['bitsdbapi']['base_url'],
            'api': self.settings['bitsdbapi']['api'],
            'version': self.settings['bitsdbapi']['version'],
            'verbose': self.verbose,
        })
        return BitsdbApi(**params)

    def bitsdbupdate(self, auth):
        """Connect to BITSdb Update class."""
        from bitsapiclient.services.bitsdb_update import BitsdbUpdate
        params = self.secrets.resolve({
            'auth': auth,
            'project': self.settings['datastore']['project'],
            # 'verbose': self.verbose,
        })
        return BitsdbUpdate(**params)

    def bitstore(self):
        """Connect to currrent BITStore DB."""
        from bitsapiclient.services.bitstore import BITStore
        params = self.secrets.resolve({
            'server': self.settings['mysql_servers']['bitstore']['db_host'],
            'port': self.settings['mysql_servers']['bitstore']['db_port'],
            'user': self.settings['mysql_servers']['bitstore']['db_user'],
            'password': self.settings['mysql_servers']['bitstore']['db_pass'],
            'db': self.settings['mysql_servers']['bitstore']['db'],
            'verbose': self.verbose,
        })
        return BITStore(**params)

    def bitstoreapi(self):
        """Connect to BITSdb API."""
        from bitsapiclient.services.bitstoreapi import BITStoreApi
        params = self.secrets.resolve({
            'api_key': self.settings['bitstoreapi']['api_key'],
            'host': self.settings['bitstoreapi']['host'],
            'name': self.settings['bitstoreapi']['name'],
            'sa_json_file': self.settings['google']['service_account']['json'],
            'version': self.settings['bitstoreapi']['version'],
            'verbose': self.verbose,
        })
        return BITStoreApi(**params)

    def broad_io(self):
        """Connect to currrent Broad.io DB."""
        from bitsapiclient.services.broad_io import BroadIo
        params = self.secrets.resolve({
            'server': self.settings['mysql_servers']['broad_io']['db_host'],
            'port': self.settings['mysql_servers']['broad_io']['db_port'],
            'user': self.settings['mysql_servers']['broad_io']['db_user'],
            'password': self.settings['mysql_servers']['broad_io']['db_pass'],
            'db': self.settings['mysql_servers']['broad_io']['db'],
            'verbose': self.verbose,
        })
        return BroadIo(**params)

    def broadaccounts(self):
        """Connect to currrent Broad Accounts."""
        from bitsapiclient.services.broadaccounts import BroadAccounts
        params = self.secrets.resolve({
            'auth': self,
            'verbose': self.verbose,
        })
        return BroadAccounts(**params)

    def calendar(self):
        """Connect to currrent Calendar DB."""
        from bitsapiclient.services.calendar import Calendar
        params = self.secrets.resolve({
            'server': self.settings['mysql_servers']['calendar']['db_host'],
            'port': self.settings['mysql_servers']['calendar']['db_port'],
            'user': self.settings['mysql_servers']['calendar']['db_user'],
            'password': self.settings['mysql_servers']['calendar']['db_pass'],
            'db': self.settings['mysql_servers']['calendar']['db'],
            'verbose': self.verbose,
        })
        return Calendar(**params)

    def calendar_new(self):
        """Connect to new Calendar DB."""
        from bitsapiclient.services.calendar import Calendar
        params = self.secrets.resolve({
            'server': self.settings['mysql_servers']['calendar_new']['db_host'],
            'port': self.settings['mysql_servers']['calendar_new']['db_port'],
            'user': self.settings['mysql_servers']['calendar_new']['db_user'],
            'password': self.settings['mysql_servers']['calendar_new']['db_pass'],
            'db': self.settings['mysql_servers']['calendar_new']['db'],
            'api_host': self.settings['calendar']['api_host'],
            'email_from': self.settings['calendar']['email_from'],
            'email_from_name': self.settings['calendar']['email_from_name'],
            'email_to': self.settings['calendar']['email_to'],
            'email_to_name': self.settings['calendar']['email_to_name'],
            'verbose': self.verbose,
        })
        return Calendar(**params)

    def casper(self):
        """Connect to Casper DB."""
        from bitsapiclient.services.casper import Casper
        params = self.secrets.resolve({
            'server': self.settings['mysql_servers']['casper']['db_host'],
            'port': self.settings['mysql_servers']['casper']['db_port'],
            'user': self.settings['mysql_servers']['casper']['db_user'],
            'password': self.settings['mysql_servers']['casper']['db_pass'],
            'db': self.settings['mysql_servers']['casper']['db'],
            'verbose': self.verbose,
        })
        return Casper(**params)

    def cloudaccounts(self):
        """Connect to Cloud Accounts API."""
        from bits.cloudaccounts import CloudAccounts
        return CloudAccounts(self.google())

    def ccure(self):
        """Connect to CCURE DB."""
        from bitsapiclient.services.ccure import CCURE
        params = self.secrets.resolve({
            'server': '%s:%s' % (
                self.settings['mssql_servers']['ccure']['db_host'],
                self.settings['mssql_servers']['ccure']['db_port'],
            ),
            'user': self.settings['mssql_servers']['ccure']['db_user'],
            'password': self.settings['mssql_servers']['ccure']['db_pass'],
            'database': self.settings['mssql_servers']['ccure']['db'],
            'credentials_file': self.settings['ccure']['credentials'],
            'personnel_file': self.settings['ccure']['personnel'],
            'new_personnel_file': self.settings['ccure']['newpersonnel'],
            'photos': self.settings['ccure']['photos'],
            'workday_photos': self.settings['ccure']['workday_photos'],
            'verbose': self.verbose,
        })
        return CCURE(**params)

    def ccure_dev(self):
        """Connect to CCURE dev DB."""
        from bitsapiclient.services.ccure import CCURE
        params = self.secrets.resolve({
            'server': '%s:%s' % (
                self.settings['mssql_servers']['ccure_dev']['db_host'],
                self.settings['mssql_servers']['ccure_dev']['db_port'],
            ),
            'user': self.settings['mssql_servers']['ccure_dev']['db_user'],
            'password': self.settings['mssql_servers']['ccure_dev']['db_pass'],
            'database': self.settings['mssql_servers']['ccure_dev']['db'],
            'credentials_file': self.settings['ccure_dev']['credentials'],
            'personnel_file': self.settings['ccure_dev']['personnel'],
            'new_personnel_file': self.settings['ccure_dev']['newpersonnel'],
            'photos': self.settings['ccure_dev']['photos'],
            'workday_photos': self.settings['ccure']['workday_photos'],
            'verbose': self.verbose,
        })
        return CCURE(**params)

    def ccure_prod(self):
        """Connect to CCURE prod DB."""
        from bitsapiclient.services.ccure import CCURE
        params = self.secrets.resolve({
            'server': '%s:%s' % (
                self.settings['mssql_servers']['ccure_prod']['db_host'],
                self.settings['mssql_servers']['ccure_prod']['db_port'],
            ),
            'user': self.settings['mssql_servers']['ccure_prod']['db_user'],
            'password': self.settings['mssql_servers']['ccure_prod']['db_pass'],
            'database': self.settings['mssql_servers']['ccure_prod']['db'],
            'credentials_file': self.settings['ccure_prod']['credentials'],
            'personnel_file': self.settings['ccure_prod']['personnel'],
            'new_personnel_file': self.settings['ccure_prod']['newpersonnel'],
            'photos': self.settings['ccure_prod']['photos'],
            'workday_photos': self.settings['ccure']['workday_photos'],
            'verbose': self.verbose,
        })
        return CCURE(**params)

    def datawarehouse(self, dataset):
        """Connect to data warehouse."""
        from bitsapiclient.services.datawarehouse import DataWarehouse
        params = self.secrets.resolve({
            'auth': self,
            'bucket': 'broad-bitsdb-bigquery-import',
            'project': 'broad-bitsdb-api',
            'dataset': dataset,
            'verbose': self.verbose,
        })
        return DataWarehouse(**params)

    def dialpad(self):
        """Connect to Dialpad API."""
        from bits.dialpad import Dialpad
        params = self.secrets.resolve({
            'token': self.settings['dialpad']['token'],
            'verbose': self.verbose,
        })
        return Dialpad(**params)

    def disclosure(self):
        """Connect to Disclosure DB."""
        from bits.disclosure import Disclosure
        params = self.secrets.resolve({
            'mongo_uri': self.settings['mongo']['disclosure']['uri'],
            'mongo_db': self.settings['mongo']['disclosure']['db']
        })
        return Disclosure(**params)

    def disclosure_dev(self):
        """Connect to Disclosure dev DB."""
        from bits.disclosure import Disclosure
        params = self.secrets.resolve({
            'mongo_uri': self.settings['mongo']['disclosure_dev']['uri'],
            'mongo_db': self.settings['mongo']['disclosure_dev']['db']
        })
        return Disclosure(**params)

    def disclosure_prod(self):
        """Connect to Disclosure prod DB."""
        from bits.disclosure import Disclosure
        params = self.secrets.resolve({
            'mongo_uri': self.settings['mongo']['disclosure_prod']['uri'],
            'mongo_db': self.settings['mongo']['disclosure_prod']['db']
        })
        return Disclosure(**params)

    def dockerhub(self):
        """Connect to DockerHub API."""
        from bitsapiclient.services.dockerhub import DockerHub
        params = self.secrets.resolve({
            'username': self.settings['dockerhub']['username'],
            'password': self.settings['dockerhub']['password'],
            'org': self.settings['dockerhub']['org'],
        })
        return DockerHub(**params)

    def ecs(self):
        """Connect to the ECS API."""
        from bitsapiclient.services.ecs import ECS
        params = self.secrets.resolve({
            'username': self.settings['ecs']['username'],
            'password': self.settings['ecs']['password'],
            'host': self.settings['ecs']['host'],
            'verbose': self.verbose,
        })
        return ECS(**params)

    def fox(self):
        """Connect to fox."""
        from bitsapiclient.services.fox import Fox
        params = self.secrets.resolve({
            'server': self.settings['fox']['server'],
            'username': self.settings['fox']['username'],
            'password': self.settings['fox']['password'],
            'verbose': self.verbose,
        })
        return Fox(**params)

    def firehose(self):
        """Connect to Firehose."""
        from bitsapiclient.services.firehose import Firehose
        return Firehose(
            verbose=self.verbose,
        )

    def github(self, token=None):
        """Return an authenticated GitHub object."""
        from bitsapiclient.services.github import GitHub
        if not token:
            token = self.settings['github']['token']
        params = self.secrets.resolve({
            'app_project': self.settings['github']['app_project'],
            'org': self.settings['github']['org'],
            'owner_team': self.settings['github']['owner_team'],
            'role_team': self.settings['github']['role_team'],
            'token': token,
            'verbose': self.verbose,
        })
        return GitHub(**params)

    def google(self):
        """Connect to new Google API class."""
        settings = self.settings['google']
        from bits.google import Google
        params = self.secrets.resolve({
            'api_key': settings['api_key'],
            'client_scopes': settings['client_secrets']['scopes'],
            'client_secrets_file': settings['client_secrets']['json'],
            'credentials_file': settings['client_secrets']['credentials'],
            'gsuite_licenses': settings['gsuite_licenses'],
            'scopes': settings['service_account']['scopes'],
            'service_account_email': settings['service_account']['email'],
            'service_account_file': settings['service_account']['json'],
            'subject': settings['service_account']['sub_account'],
            'verbose': self.verbose,
        })
        return Google(**params)

    def help(self):
        """Connect to RequestTracker DB."""
        from bitsapiclient.services.rt import RequestTracker
        params = self.secrets.resolve({
            'server': self.settings['mysql_servers']['help']['db_host'],
            'port': self.settings['mysql_servers']['help']['db_port'],
            'user': self.settings['mysql_servers']['help']['db_user'],
            'password': self.settings['mysql_servers']['help']['db_pass'],
            'db': self.settings['mysql_servers']['help']['db'],
            'charset': 'latin1',
            'verbose': self.verbose,
        })
        return RequestTracker(**params)

    def hosts(self):
        """Connect to Hosts App."""
        from bitsapiclient.services.hosts import Hosts
        params = self.secrets.resolve({
            'master_host_listing': self.settings['mhl']['hosts_file'],
            'lockfile': self.settings['mhl']['lock_file'],
            'verbose': self.verbose,
        })
        return Hosts(**params)

    def intranet(self):
        """Connect to Intranet DB."""
        from bitsapiclient.services.iwww import IWWW
        params = self.secrets.resolve({
            'server': self.settings['mysql_servers']['intranet']['db_host'],
            'port': self.settings['mysql_servers']['intranet']['db_port'],
            'user': self.settings['mysql_servers']['intranet']['db_user'],
            'password': self.settings['mysql_servers']['intranet']['db_pass'],
            'db': self.settings['mysql_servers']['intranet']['db'],
            'verbose': self.verbose,
        })
        return IWWW(**params)

    def ippia(self):
        """Connect to IPPIA Mongo DB."""
        from bits.mongo import Mongo
        params = self.secrets.resolve({
            'uri': self.settings['mongo']['ippia']['uri'],
            'db': self.settings['mongo']['ippia']['db'],
            'verbose': self.verbose,
        })
        return Mongo(**params)

    def isilon(self):
        """Connect to Isilon API."""
        from bitsapiclient.services.isilon import Isilon
        params = self.secrets.resolve({
            'username': self.settings['isilon']['username'],
            'password': self.settings['isilon']['password'],
            'clusters': self.settings['isilon']['clusters'],
            'verbose': self.verbose,
        })
        return Isilon(**params)

    def jenkins(self):
        """Connect to Jenkins."""
        from bits.jenkins import Jenkins
        params = self.secrets.resolve({
            'url': self.settings['jenkins']['url'],
            'username': self.settings['jenkins']['username'],
            'password': self.settings['jenkins']['password'],
        })
        return Jenkins(**params)

    def jira_cloud(self):
        """Connect to JIRA cloud instance."""
        from bitsapiclient.services.jira import Jira
        params = self.secrets.resolve({
            'username': self.settings['jira']['cloud']['username'],
            'password': self.settings['jira']['cloud']['password'],
            'server': self.settings['jira']['cloud']['server'],
            'verbose': self.verbose,
        })
        return Jira(**params)

    def jira_onprem(self):
        """Connect to JIRA onprem instance."""
        from bitsapiclient.services.jira import Jira
        params = self.secrets.resolve({
            'username': self.settings['jira']['onprem']['username'],
            'password': self.settings['jira']['onprem']['password'],
            'server': self.settings['jira']['onprem']['server'],
            'verbose': self.verbose,
        })
        return Jira(**params)

    def keyserver(self):
        """Connect to Keyserver instance."""
        from bitsapiclient.services.keyserver import Keyserver
        params = self.secrets.resolve({
            'url': self.settings['keyserver']['url'],
            'username': self.settings['keyserver']['username'],
            'password': self.settings['keyserver']['password'],
            'verbose': self.verbose,
        })
        return Keyserver(**params)

    def labinspection(self):
        """Connect to Lab Inspection DB."""
        from bitsapiclient.services.labinspection import LabInspection
        params = self.secrets.resolve({
            'server': self.settings['mysql_servers']['labinspection']['db_host'],
            'port': self.settings['mysql_servers']['labinspection']['db_port'],
            'user': self.settings['mysql_servers']['labinspection']['db_user'],
            'password': self.settings['mysql_servers']['labinspection']['db_pass'],
            'db': self.settings['mysql_servers']['labinspection']['db'],
            'verbose': self.verbose,
        })
        return LabInspection(**params)

    def ldapupdate(self):
        """Connect to the LDAPUpdate class."""
        from bits.ldap.update import LDAPUpdate
        for key in self.settings['ldap_servers']:
            settings = self.settings['ldap_servers'][key]
            self.settings['ldap_servers'][key] = self.secrets.resolve(settings)
        params = self.secrets.resolve({
            'auth': self,
            'settings': self.settings,
            # verbose: self.verbose,
        })
        return LDAPUpdate(**params)

    def leankit(self):
        """Connect to the Leankit class."""
        from bits.leankit import Leankit
        params = self.secrets.resolve({
            'host': self.settings['leankit']['host'],
            'username': self.settings['leankit']['username'],
            'password': self.settings['leankit']['password'],
            'verbose': self.verbose
        })
        return Leankit(**params)

    def localmail(self):
        """Connect to the localmail LDAP class."""
        from bitsapiclient.services.localmail import Localmail
        params = self.secrets.resolve({
            'ldap_uri': self.settings['ldap_servers']['localmail']['uri'],
            'ldap_bind_dn': self.settings['ldap_servers']['localmail']['bind_dn'],
            'ldap_bind_pw': self.settings['ldap_servers']['localmail']['bind_pw'],
            'ldap_base_dn': self.settings['ldap_servers']['localmail']['base_dn'],
            'verbose': self.verbose,
        })
        return Localmail(**params)

    def mhl(self, people: None):
        """Connect to MHL file."""
        from bitsapiclient.services.mhl import MHL
        params = self.secrets.resolve({
            'path': self.settings['mhl']['hosts_file'],
            'lockfile': self.settings['mhl']['lock_file'],
            'people': people,
            'verbose': self.verbose,
        })
        return MHL(**params)

    def mongo(self):
        """Connect to BITSdb Mongo DB."""
        from bitsapiclient.services.mongo import Mongo
        params = self.secrets.resolve({
            'mongo_uri': self.settings['mongo']['bitsdb']['uri'],
            'mongo_db': self.settings['mongo']['bitsdb']['db'],
            'auth': self,
            'verbose': self.verbose,
        })
        return Mongo(**params)

    def mongo_dev(self):
        """Connect to BITSdb dev Mongo DB."""
        from bitsapiclient.services.mongo import Mongo
        params = self.secrets.resolve({
            'mongo_uri': self.settings['mongo']['bitsdb_dev']['uri'],
            'mongo_db': self.settings['mongo']['bitsdb_dev']['db'],
            'auth': self,
            'verbose': self.verbose
        })
        return Mongo(**params)

    def mongo_prod(self):
        """Connect to BITSdb prod Mongo DB."""
        from bitsapiclient.services.mongo import Mongo
        params = self.secrets.resolve({
            'mongo_uri': self.settings['mongo']['bitsdb_prod']['uri'],
            'mongo_db': self.settings['mongo']['bitsdb_prod']['db'],
            'auth': self,
            'verbose': self.verbose,
        })
        return Mongo(**params)

    def mx(self):
        """Return an MX instance."""
        from bits.mx import MX
        params = self.secrets.resolve({
            'aliases_puppetdir': self.settings['mx']['aliases_puppetdir'],
            'transports_puppetdir': self.settings['mx']['transports_puppetdir'],
            'extension': self.settings['mx']['extension'],
            'auth': self,
        })
        return MX(**params)

    def netbox(self):
        """Connect to Netbox."""
        from bits.netbox import Netbox
        params = self.secrets.resolve({
            'token': self.settings['netbox']['token'],
            'url': self.settings['netbox']['url'],
            'verbose': self.verbose,
        })
        return Netbox(**params)

    def nis(self):
        """Connect to NIS."""
        from bitsapiclient.services.nis import NIS
        params = self.secrets.resolve({
            'verbose': self.verbose,
        })
        return NIS(**params)

    def orbitera(self):
        """Connect to Orbitera."""
        from bitsapiclient.services.orbitera import Orbitera
        params = self.secrets.resolve({
            # api v1
            'url': self.settings['orbitera']['url'],
            'api_key': self.settings['orbitera']['api_key'],
            'api_secret': self.settings['orbitera']['api_secret'],
            # api v2
            'account': self.settings['orbitera']['account'],
            'credentials_file': self.settings['orbitera']['credentials_file'],
            'host': self.settings['orbitera']['host'],
            # verbose
            'verbose': self.verbose,
        })
        return Orbitera(**params)

    def people(self):
        """Connect to People DB."""
        from bitsapiclient.services.people import PeopleDB
        params = self.secrets.resolve({
            'server': self.settings['mysql_servers']['people']['db_host'],
            'port': self.settings['mysql_servers']['people']['db_port'],
            'user': self.settings['mysql_servers']['people']['db_user'],
            'password': self.settings['mysql_servers']['people']['db_pass'],
            'db': self.settings['mysql_servers']['people']['db'],
            'csvs': self.settings['people']['csvs'],
            'verbose': self.verbose,
        })
        return PeopleDB(**params)

    def people_dev(self):
        """Connect to People dev DB."""
        from bitsapiclient.services.people import PeopleDB
        params = self.secrets.resolve({
            'server': self.settings['mysql_servers']['people_dev']['db_host'],
            'port': self.settings['mysql_servers']['people_dev']['db_port'],
            'user': self.settings['mysql_servers']['people_dev']['db_user'],
            'password': self.settings['mysql_servers']['people_dev']['db_pass'],
            'db': self.settings['mysql_servers']['people_dev']['db'],
            'csvs': self.settings['people']['csvs'],
            'verbose': self.verbose,
        })
        return PeopleDB(**params)

    def people_prod(self):
        """Connect to People prod DB."""
        from bitsapiclient.services.people import PeopleDB
        params = self.secrets.resolve({
            'server': self.settings['mysql_servers']['people_prod']['db_host'],
            'port': self.settings['mysql_servers']['people_prod']['db_port'],
            'user': self.settings['mysql_servers']['people_prod']['db_user'],
            'password': self.settings['mysql_servers']['people_prod']['db_pass'],
            'db': self.settings['mysql_servers']['people_prod']['db'],
            'csvs': self.settings['people']['csvs'],
            'verbose': self.verbose,
        })
        return PeopleDB(**params)

    def pivotaltracker(self):
        """Connect to Pivotal Tracker API."""
        from bitsapiclient.services.pivotaltracker import PivotalTracker
        params = self.secrets.resolve({
            'token': self.settings['pivotaltracker']['token'],
            'verbose': self.verbose
        })
        return PivotalTracker(**params)

    def quay(self):
        """Connect to Quay API."""
        from bits.quay import Quay
        params = self.secrets.resolve({
            'token': self.settings['quay']['token'],
            'orgname': self.settings['quay']['orgname'],
            'clientid': self.settings['quay']['clientid'],
            'secret': self.settings['quay']['secret'],
            'role_team': self.settings['quay']['role_team'],
            'verbose': self.verbose,
        })
        return Quay(**params)

    def redlock(self):
        """Connect to RedLock API."""
        from bitsapiclient.services.redlock import RedLock
        params = self.secrets.resolve({
            'username': self.settings['redlock']['username'],
            'password': self.settings['redlock']['password'],
            'customerName': self.settings['redlock']['customerName'],
        })
        return RedLock(**params)

    def rt(self):
        """Connect to RequestTracker DB."""
        from bitsapiclient.services.rt import RequestTracker
        params = self.secrets.resolve({
            'server': self.settings['mysql_servers']['rt']['db_host'],
            'port': self.settings['mysql_servers']['rt']['db_port'],
            'user': self.settings['mysql_servers']['rt']['db_user'],
            'password': self.settings['mysql_servers']['rt']['db_pass'],
            'db': self.settings['mysql_servers']['rt']['db'],
            'charset': 'latin1',
            'verbose': self.verbose,
        })
        return RequestTracker(**params)

    def sap(self):
        """Connect to SAP DB."""
        from bitsapiclient.services.sap import SAP
        params = self.secrets.resolve({
            'server': '%s:%s' % (
                self.settings['mssql_servers']['sap']['db_host'],
                self.settings['mssql_servers']['sap']['db_port'],
            ),
            'user': self.settings['mssql_servers']['sap']['db_user'],
            'password': self.settings['mssql_servers']['sap']['db_pass'],
            'db': self.settings['mssql_servers']['sap']['db'],
            'verbose': self.verbose,
        })
        return SAP(**params)

    def servicenow(self):
        """Connect to ServiceNow."""
        from bitsapiclient.services.servicenow import ServiceNow
        params = self.secrets.resolve({
            'base_url': self.settings['servicenow']['base_url'],
            'params': self.settings['servicenow']['params'],
            'user': self.settings['servicenow']['username'],
            'passwd': self.settings['servicenow']['password'],
            'buildings': self.settings['servicenow']['buildings'],
            'verbose': self.verbose,
        })
        return ServiceNow(**params)

    def slack(self):
        """Connect to Slack API."""
        from bitsapiclient.services.slack import Slack
        params = self.secrets.resolve({
            'token': self.settings['slack']['token'],
            'env': self.settings['configuration']['environment'],
            'notifications': self.settings['slack']['notifications'],
        })
        return Slack(**params)

    def space(self):
        """Connect to Space DB."""
        from bitsapiclient.services.space import SpaceDB
        params = self.secrets.resolve({
            'server': self.settings['mysql_servers']['space']['db_host'],
            'port': self.settings['mysql_servers']['space']['db_port'],
            'user': self.settings['mysql_servers']['space']['db_user'],
            'password': self.settings['mysql_servers']['space']['db_pass'],
            'db': self.settings['mysql_servers']['space']['db'],
            'verbose': self.verbose,
        })
        return SpaceDB(**params)

    def space_dev(self):
        """Connect to Space dev DB."""
        from bitsapiclient.services.space import SpaceDB
        params = self.secrets.resolve({
            'server': self.settings['mysql_servers']['space_dev']['db_host'],
            'port': self.settings['mysql_servers']['space_dev']['db_port'],
            'user': self.settings['mysql_servers']['space_dev']['db_user'],
            'password': self.settings['mysql_servers']['space_dev']['db_pass'],
            'db': self.settings['mysql_servers']['space_dev']['db'],
            'verbose': self.verbose,
        })
        return SpaceDB(**params)

    def space_prod(self):
        """Connect to Space prod DB."""
        from bitsapiclient.services.space import SpaceDB
        params = self.secrets.resolve({
            'server': self.settings['mysql_servers']['space_prod']['db_host'],
            'port': self.settings['mysql_servers']['space_prod']['db_port'],
            'user': self.settings['mysql_servers']['space_prod']['db_user'],
            'password': self.settings['mysql_servers']['space_prod']['db_pass'],
            'db': self.settings['mysql_servers']['space_prod']['db'],
            'verbose': self.verbose,
        })
        return SpaceDB(**params)

    def stash(self):
        """Connect to Stash API."""
        from bitsapiclient.services.stash import Stash
        params = self.secrets.resolve({
            'host': self.settings['stash']['host'],
            'username': self.settings['stash']['username'],
            'password': self.settings['stash']['password']
        })
        return Stash(**params)

    def swoogo(self):
        """Connect to Swoogo API."""
        from bitsapiclient.services.swoogo import Swoogo
        params = self.secrets.resolve({
            'api_key': self.settings['swoogo']['api_key'],
            'api_secret': self.settings['swoogo']['api_secret'],
            'verbose': self.verbose,
        })
        return Swoogo(**params)

    def tableau(self):
        """Return an authenticated Tableau object."""
        from bitsapiclient.services.tableau import Tableau
        dn = self.settings['ldap_servers']['ad_ldap']['bind_dn']
        username = dn.split(',')[0].split('=')[1]
        params = self.secrets.resolve({
            'username': r'CHARLES\%s' % (username),
            'password': self.settings['ldap_servers']['ad_ldap']['bind_pw'],
            'verbose': self.verbose,
        })
        return Tableau(**params)

    def travis(self):
        """Return an authenticated Travis object."""
        from bitsapiclient.services.travis import Travis
        params = self.secrets.resolve({
            'token': self.settings['github']['token'],
            'verbose': self.verbose,
        })
        return Travis(**params)

    def vmware(self):
        """Connect to VMWare API."""
        from bitsapiclient.services.vmware import VMWare
        params = self.secrets.resolve({
            'username': self.settings['vmware']['username'],
            'password': self.settings['vmware']['password'],
            'url': self.settings['vmware']['url'],
            'port': self.settings['vmware']['port'],
            'verbose': self.verbose,
        })
        return VMWare(**params)

    def welcome(self):
        """Connect to the Welcome app."""
        from bitsapiclient.services.welcome import Welcome
        return Welcome()

    def workday(self):
        """Connect to Workday API."""
        from bitsapiclient.services.workday import Workday
        params = self.secrets.resolve({
            'base_url': self.settings['workday']['base_url'],
            'tenant': self.settings['workday']['tenant'],
            'username': self.settings['workday']['username'],
            'password': self.settings['workday']['password'],
            'feed_username': self.settings['workday']['feed_username'],
            'feed_password': self.settings['workday']['feed_password'],
            'provisioning_username': self.settings['workday']['provisioning_username'],
            'provisioning_password': self.settings['workday']['provisioning_password'],
            'provisioning_url': self.settings['workday']['provisioning_url'],
            'verbose': self.verbose,
        })
        return Workday(**params)
