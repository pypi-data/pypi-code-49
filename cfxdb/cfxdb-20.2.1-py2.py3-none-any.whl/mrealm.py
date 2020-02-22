###############################################################################
#
# Crossbar.io Fabric Center
# Copyright (c) Crossbar.io Technologies GmbH. All rights reserved.
#
###############################################################################

import six
import uuid
import pprint
from datetime import datetime
from typing import Dict

from cfxdb.common import ConfigurationElement


class ManagementRealm(ConfigurationElement):
    """
    CFC management realm database configuration object.
    """

    RTYPE_MREALM = 1
    RTYPE_APP = 2

    def __init__(self,
                 oid=None,
                 label=None,
                 description=None,
                 tags=None,
                 name=None,
                 created=None,
                 owner=None,
                 cf_node=None,
                 cf_router_worker=None,
                 cf_container_worker=None,
                 _unknown=None):
        """

        :param oid: Object ID of management realm
        :type oid: uuid.UUID

        :param label: Optional user label of management realm
        :type label: str

        :param description: Optional user description of management realm
        :type description: str

        :param tags: Optional list of user tags on management realm
        :type tags: list[str]

        :param name: Name of management realm
        :type name: str

        :param created: Timestamp when the management realm was created
        :type created: datetime.datetime

        :param owner: Owning user (object ID)
        :type owner: uuid.UUID

        :param cf_node: *INTERNAL USE* CFC hosting node for this management realm
        :type cf_node: str

        :param cf_router_worker: *INTERNAL USE* CFC hosting router worker for this management realm
        :type cf_router_worker: str

        :param cf_container_worker: *INTERNAL USE* CFC hosting container worker for this management realm
        :type cf_container_worker: str

        :param _unknown: Any unparsed/unprocessed data attributes
        :type _unknown: None or dict
        """
        ConfigurationElement.__init__(self, oid=oid, label=label, description=description, tags=tags)
        self.name = name
        self.created = created
        self.owner = owner
        self.cf_node = cf_node
        self.cf_router_worker = cf_router_worker
        self.cf_container_worker = cf_container_worker

        # private member with unknown/untouched data passing through
        self._unknown = _unknown

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if not ConfigurationElement.__eq__(self, other):
            return False
        if other.name != self.name:
            return False
        if other.created != self.created:
            return False
        if other.owner != self.owner:
            return False
        if other.cf_node != self.cf_node:
            return False
        if other.cf_router_worker != self.cf_router_worker:
            return False
        if other.cf_container_worker != self.cf_container_worker:
            return False
        return True

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        return '\n{}\n'.format(pprint.pformat(self.marshal()))

    def copy(self, other, overwrite=False):
        """
        Copy over other object.

        :param other: Other management realm to copy data from.
        :type other: instance of :class:`ManagementRealm`
        :return:
        """
        ConfigurationElement.copy(self, other, overwrite=overwrite)

        if (not self.name and other.name) or overwrite:
            self.name = other.name
        if (not self.created and other.created) or overwrite:
            self.created = other.created
        if (not self.owner and other.owner) or overwrite:
            self.owner = other.owner
        if (not self.cf_node and other.cf_node) or overwrite:
            self.cf_node = other.cf_node
        if (not self.cf_router_worker and other.cf_router_worker) or overwrite:
            self.cf_router_worker = other.cf_router_worker
        if (not self.cf_container_worker and other.cf_container_worker) or overwrite:
            self.cf_container_worker = other.cf_container_worker

        # _unknown is not copied!

    def marshal(self):
        """
        Marshal this object to a generic host language object.

        :return: dict
        """
        assert isinstance(self.oid, uuid.UUID)
        assert type(self.name) == six.text_type
        assert isinstance(self.created, datetime)
        assert isinstance(self.owner, uuid.UUID)
        assert self.cf_node is None or isinstance(self.cf_node, uuid.UUID)
        assert self.cf_router_worker is None or isinstance(self.cf_router_worker, uuid.UUID)
        assert self.cf_container_worker is None or isinstance(self.cf_container_worker, uuid.UUID)

        obj = ConfigurationElement.marshal(self)

        obj.update({
            'oid': str(self.oid),
            'name': self.name,
            'created': int(self.created.timestamp() * 1000000) if self.created else None,
            'owner': str(self.owner),
            'cf_node': str(self.cf_node) if self.cf_node else None,
            'cf_router_worker': str(self.cf_router_worker) if self.cf_router_worker else None,
            'cf_container_worker': str(self.cf_container_worker) if self.cf_container_worker else None,
        })

        if self._unknown:
            # pass through all attributes unknown
            obj.update(self._unknown)

        return obj

    @staticmethod
    def parse(data):
        """
        Parse generic host language object into an object of this class.

        :param data: Generic host language object
        :type data: dict

        :return: instance of :class:`ManagementRealm`
        """
        assert type(data) == dict

        obj = ConfigurationElement.parse(data)
        data = obj._unknown

        # future attributes (yet unknown) are not only ignored, but passed through!
        _unknown = {}
        for k in data:
            if k not in [
                    'oid', 'name', 'rtype', 'owner', 'created', 'cf_node', 'cf_router_worker',
                    'cf_container_worker'
            ]:
                _unknown[k] = data[k]

        name = data.get('name', None)
        assert name is None or type(name) == six.text_type

        owner = data.get('owner', None)
        assert owner is None or type(owner) == six.text_type
        if owner:
            owner = uuid.UUID(owner)

        created = data.get('created', None)
        assert created is None or type(created) == float or type(created) in six.integer_types
        if created:
            created = datetime.utcfromtimestamp(float(created) / 1000000.)

        cf_node = data.get('cf_node', None)
        assert cf_node is None or type(cf_node) == six.text_type
        if cf_node:
            cf_node = uuid.UUID(cf_node)

        cf_router_worker = data.get('cf_router_worker', None)
        assert cf_router_worker is None or type(cf_router_worker) == six.text_type
        if cf_router_worker:
            cf_router_worker = uuid.UUID(cf_router_worker)

        cf_container_worker = data.get('cf_container_worker', None)
        assert cf_container_worker is None or type(cf_container_worker) == six.text_type
        if cf_container_worker:
            cf_container_worker = uuid.UUID(cf_container_worker)

        obj = ManagementRealm(oid=obj.oid,
                              label=obj.label,
                              description=obj.description,
                              tags=obj.tags,
                              name=name,
                              owner=owner,
                              created=created,
                              cf_node=cf_node,
                              cf_router_worker=cf_router_worker,
                              cf_container_worker=cf_container_worker,
                              _unknown=_unknown)

        return obj


class Node(ConfigurationElement):
    """
    CFC Node database configuration object.
    """
    def __init__(self,
                 oid=None,
                 label=None,
                 description=None,
                 tags=None,
                 owner_oid=None,
                 pubkey=None,
                 mrealm_oid=None,
                 authid=None,
                 authextra=None,
                 _unknown=None):
        """

        :param oid: Object ID of node
        :type oid: uuid.UUID

        :param label: Optional user label of node
        :type label: str

        :param description: Optional user description of node
        :type description: str

        :param tags: Optional list of user tags on node
        :type tags: list[str]

        :param owner_oid: Object owner.
        :type owner_oid: uuid.UUID

        :param pubkey: The WAMP-cryptosign node public key (32 bytes as HEX encoded string).
        :type pubkey: str

        :param mrealm_oid: The management realm the node will be joined on.
        :type mrealm_oid: uuid.UUID

        :param authid: The WAMP ``authid`` the node will be authenticated as.
        :type authid: str

        :param authextra: Optional ``authextra`` the node will be sent to when authenticating.
        :type authextra: None or dict

        :param _unknown: Any unparsed/unprocessed data attributes
        :type _unknown: None or dict
        """
        ConfigurationElement.__init__(self, oid=oid, label=label, description=description, tags=tags)
        self.owner_oid = owner_oid
        self.pubkey = pubkey
        self.mrealm_oid = mrealm_oid
        self.authid = authid
        self.authextra = authextra

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if not ConfigurationElement.__eq__(self, other):
            return False
        if other.owner_oid != self.owner_oid:
            return False
        if other.pubkey != self.pubkey:
            return False
        if other.mrealm_oid != self.mrealm_oid:
            return False
        if other.authid != self.authid:
            return False
        if other.authextra != self.authextra:
            return False
        return True

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        return '\n{}\n'.format(pprint.pformat(self.marshal()))

    def copy(self, other, overwrite=False):
        """
        Copy over other object.

        :param other: Other management realm to copy data from.
        :type other: instance of :class:`ManagementRealm`
        :return:
        """
        ConfigurationElement.copy(self, other, overwrite=overwrite)

        if (not self.owner_oid and other.owner_oid) or overwrite:
            self.owner_oid = other.owner_oid
        if (not self.pubkey and other.pubkey) or overwrite:
            self.pubkey = other.pubkey
        if (not self.mrealm_oid and other.mrealm_oid) or overwrite:
            self.mrealm_oid = other.mrealm_oid
        if (not self.authid and other.authid) or overwrite:
            self.authid = other.authid
        if (not self.authextra and other.authextra) or overwrite:
            self.authextra = other.authextra

        # _unknown is not copied!

    def marshal(self):
        """
        Marshal this object to a generic host language object.

        :return: dict
        """
        obj = ConfigurationElement.marshal(self)

        assert self.owner_oid is None or isinstance(self.owner_oid, uuid.UUID)
        assert type(self.pubkey) == six.text_type and len(self.pubkey) == 64
        assert self.mrealm_oid is None or isinstance(self.mrealm_oid, uuid.UUID)
        assert self.authid is None or type(self.authid) == six.text_type
        assert self.authextra is None or type(self.authextra) == dict

        obj.update({
            'owner_oid': str(self.owner_oid) if self.owner_oid else None,
            'pubkey': self.pubkey,
            'mrealm_oid': str(self.mrealm_oid) if self.mrealm_oid else None,
            'authid': self.authid,
            'authextra': self.authextra,
        })

        return obj

    @staticmethod
    def parse(data):
        """
        Parse generic host language object into an object of this class.

        :param data: Generic host language object
        :type data: dict

        :return: instance of :class:`ManagementRealm`
        """
        assert type(data) == dict

        obj = ConfigurationElement.parse(data)
        data = obj._unknown

        # future attributes (yet unknown) are not only ignored, but passed through!
        _unknown = {}
        for k in data:
            if k not in ['owner_oid', 'pubkey', 'mrealm_oid', 'authid', 'authextra']:
                _unknown[k] = data[k]

        owner_oid = data.get('owner_oid', None)
        assert owner_oid is None or type(owner_oid) == six.text_type
        if owner_oid:
            owner_oid = uuid.UUID(owner_oid)

        pubkey = data.get('pubkey', None)
        assert pubkey is None or (type(pubkey) == six.text_type and len(pubkey) == 64)

        mrealm_oid = data.get('mrealm_oid', None)
        assert mrealm_oid is None or type(mrealm_oid) == six.text_type
        if mrealm_oid:
            mrealm_oid = uuid.UUID(mrealm_oid)

        authid = data.get('authid', None)
        assert authid is None or type(authid) == six.text_type

        authextra = data.get('authextra', None)
        assert authextra is None or type(authextra) == dict

        obj = Node(oid=obj.oid,
                   label=obj.label,
                   description=obj.description,
                   tags=obj.tags,
                   owner_oid=owner_oid,
                   pubkey=pubkey,
                   mrealm_oid=mrealm_oid,
                   authid=authid,
                   authextra=authextra,
                   _unknown=_unknown)

        return obj


class WebCluster(ConfigurationElement):
    """
    CFC Web Cluster database configuration object.
    """

    STATUS_BY_CODE = {
        0: 'NONE',
        1: 'STOPPED',
        2: 'STARTING',
        3: 'RUNNING',
        4: 'PAUSED',
        5: 'STOPPING',
    }

    STATUS_BY_NAME = {
        'NONE': 0,
        'STOPPED': 1,
        'STARTING': 2,
        'RUNNING': 3,
        'PAUSED': 4,
        'STOPPING': 5,
    }

    STATUS_STOPPED = 1
    STATUS_STARTING = 2
    STATUS_RUNNING = 3
    STATUS_PAUSED = 4
    STATUS_STOPPING = 5

    def __init__(self,
                 oid=None,
                 label=None,
                 description=None,
                 tags=None,
                 name=None,
                 status=None,
                 changed=None,
                 tcp_version=None,
                 tcp_port=None,
                 tcp_shared=None,
                 tcp_interface=None,
                 tcp_backlog=None,
                 tls_key=None,
                 tls_certificate=None,
                 tls_chain_certificates=None,
                 tls_ca_certificates=None,
                 tls_dhparam=None,
                 tls_ciphers=None,
                 http_client_timeout=None,
                 http_hsts=None,
                 http_hsts_max_age=None,
                 http_access_log=None,
                 http_display_tracebacks=None,
                 _unknown=None):
        """

        :param oid: Object ID of node
        :type oid: uuid.UUID

        :param label: Optional user label of node
        :type label: str

        :param description: Optional user description of node
        :type description: str

        :param tags: Optional list of user tags on node
        :type tags: list[str]

        :param tcp_version: IP version, either 4 for 6
        :type tcp_version: int

        :param tcp_port: IP listening port
        :type tcp_port: int

        :param tcp_shared: enable TCP port sharing
        :type tcp_shared: bool

        :param tcp_interface: listen on this interface
        :type tcp_interface: str

        :param tcp_backlog: TCP accept backlog queue size
        :type tcp_backlog: int

        :param tls_key: TLS server private key to use
        :type tls_key: str

        :param tls_certificate: TLS server certificate to use
        :type tls_certificate: str

        :param tls_chain_certificates: TLS certificate chain
        :type tls_chain_certificates: list[str]

        :param tls_ca_certificates: CA certificates to use
        :type tls_ca_certificates: list[str]

        :param tls_dhparam: DH parameter file
        :type tls_dhparam: str

        :param tls_ciphers: Ciphers list
        :type tls_ciphers: str

        :param http_client_timeout: HTTP client inactivity timeout
        :type http_client_timeout: int

        :param http_hsts: enable HTTP strict transport security (HSTS)
        :type http_hsts: bool

        :param http_hsts_max_age: HSTS maximum age to announce
        :type http_hsts_max_age: int

        :param http_access_log: enable Web request access logging
        :type http_access_log: bool

        :param http_display_tracebacks: enable tracebacks when running into Web errors
        :type http_display_tracebacks: bool

        :param _unknown: Any unparsed/unprocessed data attributes
        :type _unknown: None or dict
        """
        ConfigurationElement.__init__(self, oid=oid, label=label, description=description, tags=tags)
        self.name = name
        self.status = status
        self.changed = changed
        self.tcp_version = tcp_version
        self.tcp_port = tcp_port
        self.tcp_shared = tcp_shared
        self.tcp_interface = tcp_interface
        self.tcp_backlog = tcp_backlog
        self.tls_key = tls_key
        self.tls_certificate = tls_certificate
        self.tls_chain_certificates = tls_chain_certificates
        self.tls_ca_certificates = tls_ca_certificates
        self.tls_dhparam = tls_dhparam
        self.tls_ciphers = tls_ciphers
        self.http_client_timeout = http_client_timeout
        self.http_hsts = http_hsts
        self.http_hsts_max_age = http_hsts_max_age
        self.http_access_log = http_access_log
        self.http_display_tracebacks = http_display_tracebacks

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if not ConfigurationElement.__eq__(self, other):
            return False
        if other.name != self.name:
            return False
        if other.status != self.status:
            return False
        if other.changed != self.changed:
            return False
        if other.tcp_version != self.tcp_version:
            return False
        if other.tcp_port != self.tcp_port:
            return False
        if other.tcp_shared != self.tcp_shared:
            return False
        if other.tcp_interface != self.tcp_interface:
            return False
        if other.tcp_backlog != self.tcp_backlog:
            return False
        if other.tls_key != self.tls_key:
            return False
        if other.tls_certificate != self.tls_certificate:
            return False
        if other.tls_chain_certificates != self.tls_chain_certificates:
            return False
        if other.tls_ca_certificates != self.tls_ca_certificates:
            return False
        if other.tls_dhparam != self.tls_dhparam:
            return False
        if other.tls_ciphers != self.tls_ciphers:
            return False
        if other.http_client_timeout != self.http_client_timeout:
            return False
        if other.http_hsts != self.http_hsts:
            return False
        if other.http_hsts_max_age != self.http_hsts_max_age:
            return False
        if other.http_access_log != self.http_access_log:
            return False
        if other.http_display_tracebacks != self.http_display_tracebacks:
            return False
        return True

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        return '\n{}\n'.format(pprint.pformat(self.marshal()))

    def marshal(self):
        """
        Marshal this object to a generic host language object.

        :return: dict
        """
        assert self.name is None or type(self.name) == str
        assert self.status is None or type(self.status) == int
        assert self.changed is None or type(self.changed) == int
        assert self.tcp_version is None or type(self.tcp_version) == int
        assert self.tcp_port is None or type(self.tcp_port) == int
        assert self.tcp_shared is None or type(self.tcp_shared) == bool
        assert self.tcp_interface is None or type(self.tcp_interface) == str
        assert self.tcp_backlog is None or type(self.tcp_backlog) == int
        assert self.tls_key is None or type(self.tls_key) == str
        assert self.tls_certificate is None or type(self.tls_certificate) == str
        assert self.tls_chain_certificates is None or type(self.tls_chain_certificates) == list
        assert self.tls_ca_certificates is None or type(self.tls_ca_certificates) == list
        assert self.tls_dhparam is None or type(self.tls_dhparam) == str
        assert self.tls_ciphers is None or type(self.tls_ciphers) == str
        assert self.http_client_timeout is None or type(self.http_client_timeout) == int
        assert self.http_hsts is None or type(self.http_hsts) == bool
        assert self.http_hsts_max_age is None or type(self.http_hsts_max_age) == int
        assert self.http_access_log is None or type(self.http_access_log) == bool
        assert self.http_display_tracebacks is None or type(self.http_display_tracebacks) == bool

        obj = ConfigurationElement.marshal(self)

        obj.update({
            u'name': self.name,
            u'status': WebCluster.STATUS_BY_CODE[self.status],
            u'changed': self.changed,
            u'tcp_version': self.tcp_version,
            u'tcp_port': self.tcp_port,
            u'tcp_shared': self.tcp_shared,
            u'tcp_interface': self.tcp_interface,
            u'tcp_backlog': self.tcp_backlog,
            u'tls_key': self.tls_key,
            u'tls_certificate': self.tls_certificate,
            u'tls_chain_certificates': self.tls_chain_certificates,
            u'tls_ca_certificates': self.tls_ca_certificates,
            u'tls_dhparam': self.tls_dhparam,
            u'tls_ciphers': self.tls_ciphers,
            u'http_client_timeout': self.http_client_timeout,
            u'http_hsts': self.http_hsts,
            u'http_hsts_max_age': self.http_hsts_max_age,
            u'http_access_log': self.http_access_log,
            u'http_display_tracebacks': self.http_display_tracebacks,
        })

        return obj

    @staticmethod
    def parse(data):
        """
        Parse generic host language object into an object of this class.

        :param data: Generic host language object
        :type data: dict

        :return: instance of :class:`ManagementRealm`
        """
        assert type(data) == dict

        obj = ConfigurationElement.parse(data)
        data = obj._unknown

        # future attributes (yet unknown) are not only ignored, but passed through!
        _unknown = {}
        for k in data:
            if k not in [
                    'name', 'status', 'changed', 'tcp_version', 'tcp_port', 'tcp_shared', 'tcp_interface',
                    'tcp_backlog', 'tls_key', 'tls_certificate', 'tls_chain_certificates',
                    'tls_ca_certificates', 'tls_dhparam', 'tls_ciphers', 'http_client_timeout', 'http_hsts',
                    'http_hsts_max_age', 'http_access_log', 'http_display_tracebacks'
            ]:
                _unknown[k] = data[k]

        name = data.get('name', None)
        assert name is None or (type(name) == str)

        status = data.get('status', None)
        assert status is None or (type(status) == str)
        status = WebCluster.STATUS_BY_NAME.get(status, None)

        changed = data.get('changed', None)
        assert changed is None or (type(changed) == int)

        tcp_version = data.get('tcp_version', None)
        assert tcp_version is None or (type(tcp_version) == int)

        tcp_port = data.get('tcp_port', None)
        assert tcp_port is None or (type(tcp_port) == int)

        tcp_shared = data.get('tcp_shared', None)
        assert tcp_shared is None or (type(tcp_shared) == bool)

        tcp_interface = data.get('tcp_interface', None)
        assert tcp_interface is None or (type(tcp_interface) == str)

        tcp_backlog = data.get('tcp_backlog', None)
        assert tcp_backlog is None or (type(tcp_backlog) == int)

        tls_key = data.get('tls_key', None)
        assert tls_key is None or (type(tls_key) == str)

        tls_certificate = data.get('tls_certificate', None)
        assert tls_certificate is None or (type(tls_certificate) == str)

        tls_chain_certificates = data.get('tls_chain_certificates', None)
        assert tls_chain_certificates is None or (type(tls_chain_certificates) == list)

        tls_ca_certificates = data.get('tls_ca_certificates', None)
        assert tls_ca_certificates is None or (type(tls_ca_certificates) == list)

        tls_dhparam = data.get('tls_dhparam', None)
        assert tls_dhparam is None or (type(tls_dhparam) == str)

        tls_ciphers = data.get('tls_ciphers', None)
        assert tls_ciphers is None or (type(tls_ciphers) == str)

        http_client_timeout = data.get('http_client_timeout', None)
        assert http_client_timeout is None or (type(http_client_timeout) == int)

        http_hsts = data.get('http_hsts', None)
        assert http_hsts is None or (type(http_hsts) == bool)

        http_hsts_max_age = data.get('http_hsts_max_age', None)
        assert http_hsts_max_age is None or (type(http_hsts_max_age) == int)

        http_access_log = data.get('http_access_log', None)
        assert http_access_log is None or (type(http_access_log) == bool)

        http_display_tracebacks = data.get('http_display_tracebacks', None)
        assert http_display_tracebacks is None or (type(http_display_tracebacks) == bool)

        obj = WebCluster(oid=obj.oid,
                         label=obj.label,
                         description=obj.description,
                         tags=obj.tags,
                         name=name,
                         status=status,
                         changed=changed,
                         tcp_version=tcp_version,
                         tcp_port=tcp_port,
                         tcp_shared=tcp_shared,
                         tcp_interface=tcp_interface,
                         tcp_backlog=tcp_backlog,
                         tls_key=tls_key,
                         tls_certificate=tls_certificate,
                         tls_chain_certificates=tls_chain_certificates,
                         tls_ca_certificates=tls_ca_certificates,
                         tls_dhparam=tls_dhparam,
                         tls_ciphers=tls_ciphers,
                         http_client_timeout=http_client_timeout,
                         http_hsts=http_hsts,
                         http_hsts_max_age=http_hsts_max_age,
                         http_access_log=http_access_log,
                         http_display_tracebacks=http_display_tracebacks,
                         _unknown=_unknown)

        return obj


class WebClusterNodeMembership(object):
    def __init__(self, webcluster_oid=None, node_oid=None, parallel=None, standby=None, _unknown=None):
        self.webcluster_oid = webcluster_oid
        self.node_oid = node_oid
        self.parallel = parallel
        self.standby = standby
        self._unknown = _unknown

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if other.webcluster_oid != self.webcluster_oid:
            return False
        if other.node_oid != self.node_oid:
            return False
        if other.parallel != self.parallel:
            return False
        if other.standby != self.standby:
            return False
        return True

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        return '\n{}\n'.format(pprint.pformat(self.marshal()))

    def marshal(self):
        """
        Marshal this object to a generic host language object.

        :return: dict
        """
        obj = {
            'webcluster_oid': str(self.webcluster_oid),
            'node_oid': str(self.node_oid),
            'parallel': self.parallel,
            'standby': self.standby,
        }
        return obj

    @staticmethod
    def parse(data):
        """
        Parse generic host language object into an object of this class.

        :param data: Generic host language object
        :type data: dict

        :return: instance of :class:`WebService`
        """
        assert type(data) == dict

        # future attributes (yet unknown) are not only ignored, but passed through!
        _unknown = {}
        for k in data:
            if k not in ['webcluster_oid', 'node_oid', 'parallel', 'standby']:
                _unknown[k] = data[k]

        webcluster_oid = None
        if 'webcluster_oid' in data:
            assert type(data['webcluster_oid']) == six.text_type
            webcluster_oid = uuid.UUID(data['webcluster_oid'])

        node_oid = None
        if 'node_oid' in data:
            assert type(data['node_oid']) == six.text_type
            node_oid = uuid.UUID(data['node_oid'])

        parallel = None
        if 'parallel' in data and data['parallel']:
            assert type(data['parallel']) == int
            parallel = data['parallel']

        standby = None
        if 'standby' in data and data['standby']:
            assert data['standby'] is None or type(data['standby']) == bool
            standby = data['standby']

        assert webcluster_oid
        assert node_oid

        obj = WebClusterNodeMembership(webcluster_oid=webcluster_oid,
                                       node_oid=node_oid,
                                       parallel=parallel,
                                       standby=standby,
                                       _unknown=_unknown)

        return obj


_WEBSERVICE_TYPE_KLASSMAP = {}  # type: Dict[str, object]


class WebService(ConfigurationElement):
    """
    Web service:

    * check_web_path_service
    """
    def __init__(self,
                 oid=None,
                 label=None,
                 description=None,
                 tags=None,
                 service_type=None,
                 webcluster_oid=None,
                 path=None,
                 _unknown=None):
        """

        :param oid: Object ID of node
        :type oid: uuid.UUID

        :param label: Optional user label of node
        :type label: str

        :param description: Optional user description of node
        :type description: str

        :param tags: Optional list of user tags on node
        :type tags: list[str]

        :param path: HTTP URL path of the Web service, eg ``/myapp`` or ``/myapp/dashboard/72``.
        :type path: str
        """
        ConfigurationElement.__init__(self,
                                      oid=oid,
                                      label=label,
                                      description=description,
                                      tags=tags,
                                      _unknown=_unknown)
        self.service_type = service_type
        self.webcluster_oid = webcluster_oid
        self.path = path

    def other(self, key, default=None):
        return self._unknown.get(key, default)

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if not ConfigurationElement.__eq__(self, other):
            return False
        if other.service_type != self.service_type:
            return False
        if other.webcluster_oid != self.webcluster_oid:
            return False
        if other.path != self.path:
            return False
        return True

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        return '\n{}\n'.format(pprint.pformat(self.marshal()))

    def marshal(self):
        """
        Marshal this object to a generic host language object.

        :return: dict
        """
        assert self.path is None or type(self.path) == str

        obj = ConfigurationElement.marshal(self)

        obj.update({
            'webcluster_oid': str(self.webcluster_oid),
            'path': self.path,
            'type': self.service_type,
        })

        if self._unknown:
            obj.update(self._unknown)

        return obj

    @staticmethod
    def parse(data):
        """
        Parse generic host language object into an object of this class.

        :param data: Generic host language object
        :type data: dict

        :return: instance of :class:`WebService`
        """
        assert type(data) == dict

        obj = ConfigurationElement.parse(data)
        data = obj._unknown

        # future attributes (yet unknown) are not only ignored, but passed through!
        _unknown = {}
        for k in data:
            if k not in ['type', 'path', 'webcluster_oid']:
                _unknown[k] = data[k]

        webcluster_oid = data.get('webcluster_oid', None)
        assert webcluster_oid is None or (type(webcluster_oid) == str)
        if webcluster_oid:
            webcluster_oid = uuid.UUID(webcluster_oid)

        path = data.get('path', None)
        assert path is None or (type(path) == str)

        service_type = data.get('type', None)
        assert service_type is None or (type(service_type) == str)

        obj = WebService(oid=obj.oid,
                         label=obj.label,
                         description=obj.description,
                         tags=obj.tags,
                         service_type=service_type,
                         webcluster_oid=webcluster_oid,
                         path=path,
                         _unknown=_unknown)

        return obj


class WebServiceNodeInfo(WebService):
    """
    Web service: type "nodeinfo".

    * check_web_path_service_nodeinfo
    """
    def __init__(self, *args, **kwargs):
        WebService.__init__(self, *args, **kwargs)
        self.service_type = 'nodeinfo'

    @staticmethod
    def parse(data):
        obj = WebService.parse(data)
        return obj


_WEBSERVICE_TYPE_KLASSMAP['nodeinfo'] = WebService


class WebServiceStatic(WebService):
    """
    Web service: type "static".
    """

    # directory: Optional[str]
    # enable_directory_listing: Optional[bool]
    # mime_types: Optional[Dict[str, str]]
    # cache_timeout: Optional[int]
    def __init__(self, *args, **kwargs):
        WebService.__init__(self, *args, **kwargs)
        self.service_type = 'static'
        self.directory = '.'

    def marshal(self):
        obj = WebService.marshal(self)
        obj.update({'directory': self.directory})

    @staticmethod
    def parse(data):
        # obj = WebServiceStatic.__init__(WebService.parse(data))
        # obj.directory = data.get('directory', None)
        obj = WebService.parse(data)
        obj.directory = data.get('directory', None)
        return obj


_WEBSERVICE_TYPE_KLASSMAP['static'] = WebService


class WebServiceJson(WebService):
    """
    Web service: type "json".
    """

    # value: object
    # prettify: Optional[bool]
    # allow_cross_origin: Optional[bool]
    # discourage_caching: Optional[bool]
    def __init__(self, *args, **kwargs):
        WebService.__init__(self, *args, **kwargs)
        self.service_type = 'json'
        self.value = 23

    def marshal(self):
        obj = WebService.marshal(self)
        obj.update({'value': self.value})

    @staticmethod
    def parse(data):
        # obj = WebServiceJson()
        # WebServiceJson.__init__(WebService.parse(data))
        obj = WebService.parse(data)
        obj.value = data.get('value', None)
        return obj


_WEBSERVICE_TYPE_KLASSMAP['json'] = WebService


def _parse_webservice(webservice):
    """

    :param webservice:
    :return:
    """
    assert type(webservice) == dict
    assert 'type' in webservice

    if webservice['type'] not in _WEBSERVICE_TYPE_KLASSMAP:
        raise Exception('no webservice of type "{}"'.format(webservice['type']))

    klass = _WEBSERVICE_TYPE_KLASSMAP[webservice['type']]

    return klass.parse(webservice)


def parse_webservice(webservice):
    """

    :param webservice:
    :return:
    """
    assert type(webservice) == dict
    assert 'type' in webservice

    return WebService.parse(webservice)
