import six
import uuid
import struct
from pprint import pformat
from datetime import datetime

from cfxdb.common import ConfigurationElement

from cfxdb.gen import oid_t
from cfxdb.gen.user import User as UserGenFbs
# from cfxdb.gen.user import UserMrealmRoles as UserMrealmRolesGenFbs
from cfxdb.gen.user import ActivationToken as ActivationTokenGenFbs
from cfxdb.gen.user import Organization as OrganizationGenFbs

from cfxdb.gen.user.ActivationStatus import ActivationStatus
from cfxdb.gen.user.ActivationType import ActivationType
from cfxdb.gen.user.UserRole import UserRole
from cfxdb.gen.user.OrganizationType import OrganizationType

import txaio
txaio.use_twisted()

__all__ = (
    'User',
    'UserFbs',
    'UserMrealmRole',
    'UserMrealmRoleFbs',
    'ActivationToken',
    'ActivationTokenFbs',
    'Organization',
    'OrganizationFbs',
)


class User(ConfigurationElement):
    """
    CFC user database class using CBOR.
    """

    # oid: uuid.UUID

    # label: Optional[str]
    # description: Optional[str]
    # tags: Optional[List[str]]

    # email: str
    # registered: datetime
    # pubkey: six.text_type

    def __init__(self,
                 oid=None,
                 label=None,
                 description=None,
                 tags=None,
                 email=None,
                 registered=None,
                 pubkey=None,
                 _unknown=None):
        """

        :param oid: Object ID of the user
        :type oid: uuid.UUID

        :param label: Optional user label of the user
        :type label: str

        :param description: Optional user description of the user
        :type description: str

        :param tags: Optional list of user tags on the user
        :type tags: list[str]

        :param email: User email
        :type email: str

        :param registered: Timestamp when the user registered
        :type registered: datetime.datetime

        :param pubkey: Public key of user (HEX encoded Ed25519 32 byte public key).
        :type pubkey: str

        :param _unknown: Any unparsed/unprocessed data attributes
        :type _unknown: None or dict
        """

        ConfigurationElement.__init__(self, oid=oid, label=label, description=description, tags=tags)

        self.email = email
        self.registered = registered
        self.pubkey = pubkey

        # private member with unknown/untouched data passing through
        self._unknown = _unknown

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False

        if not ConfigurationElement.__eq__(self, other):
            return False

        if other.email != self.email:
            return False
        if other.registered != self.registered:
            return False
        if other.pubkey != self.pubkey:
            return False

        return True

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        return '\n{}\n'.format(pformat(self.marshal()))

    def copy(self, other):
        self.oid = other.oid
        self.label = other.label
        self.description = other.description
        self.tags = other.tags
        self.email = other.email
        self.registered = other.registered
        self.pubkey = other.pubkey

        # _unknown is not copied!

    def marshal(self):
        obj = ConfigurationElement.marshal(self)

        assert self.email is None or type(self.email) == six.text_type
        assert self.registered is None or isinstance(self.registered, datetime)
        assert self.pubkey is None or (type(self.pubkey) == six.text_type and len(self.pubkey) == 64)

        registered = int(self.registered.timestamp() * 1000000) if self.registered else None
        obj.update({
            'email': self.email,
            'registered': registered,
            'pubkey': self.pubkey,
        })

        if self._unknown:
            # pass through all attributes unknown
            obj.update(self._unknown)

        return obj

    @staticmethod
    def parse(data):
        assert type(data) == dict

        obj = ConfigurationElement.parse(data)
        data = obj._unknown

        # future attributes (yet unknown) are not only ignored, but passed through!
        _unknown = {}
        for k in data:
            if k not in ['email', 'registered', 'pubkey']:
                val = data.pop(k)
                _unknown[k] = val

        email = data.get('email', None)
        assert email is None or type(email) == six.text_type

        registered = data.get('registered', None)
        assert registered is None or type(registered) == float or type(registered) in six.integer_types
        if registered:
            # registered = datetime.utcfromtimestamp(float(registered) / 1000000.)
            registered = datetime.fromtimestamp(float(registered) / 1000000.)

        # hex string with 256 bit Ed25519 WAMP-cryptosign public key
        pubkey = data.get('pubkey', None)
        assert pubkey is None or (type(pubkey) == six.text_type and len(pubkey) == 64)

        obj = User(oid=obj.oid,
                   label=obj.label,
                   description=obj.description,
                   tags=obj.tags,
                   email=email,
                   registered=registered,
                   pubkey=pubkey,
                   _unknown=_unknown)
        return obj


class UserFbs(object):
    """
    CFC user database class using Flatbuffers.
    """

    # oid: uuid.UUID

    # label: Optional[str]
    # description: Optional[str]
    # tags: Optional[List[str]]

    # email: str
    # registered: datetime
    # pubkey: six.text_type

    def __init__(self, from_fbs=None):
        self._from_fbs = from_fbs

        self._oid = None

        self._label = None
        self._description = None
        self._tags = None

        self._email = None
        self._registered = None
        self._pubkey = None

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False

        if other.oid != self.oid:
            return False

        if other.label != self.label:
            return False
        if other.description != self.description:
            return False
        if (other.tags and not self.tags) or (not other.tags and self.tags):
            return False
        if other.tags:
            if not set(other.tags).intersection(set(self.tags)):
                return False

        if other.email != self.email:
            return False
        if other.registered != self.registered:
            return False
        if other.pubkey != self.pubkey:
            return False

        return True

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        return '\n{}\n'.format(pformat(self.marshal()))

    def copy(self, other):
        self.oid = other.oid
        self.label = other.label
        self.description = other.description
        self.tags = other.tags
        self.email = other.email
        self.registered = other.registered
        self.pubkey = other.pubkey

        # _unknown is not copied!

    @property
    def oid(self):
        if self._oid is None and self._from_fbs:
            oid = self._from_fbs.Oid()
            if oid:
                bytes = struct.pack('>Q', oid.Lsb()) + struct.pack('>Q', oid.Msb())
                self._oid = uuid.UUID(bytes=bytes)
        return self._oid

    @oid.setter
    def oid(self, value):
        assert isinstance(value, uuid.UUID)

        self._oid = value

    @property
    def label(self):
        if self._label is None and self._from_fbs:
            s = self._from_fbs.Label()
            if s:
                self._label = s.decode()
        return self._label

    @label.setter
    def label(self, value):
        assert type(value) == six.text_type

        self._label = value

    @property
    def description(self):
        if self._description is None and self._from_fbs:
            s = self._from_fbs.Description()
            if s:
                self._description = s.decode()
        return self._description

    @description.setter
    def description(self, value):
        assert type(value) == six.text_type

        self._description = value

    @property
    def tags(self):
        if self._tags is None and self._from_fbs:
            if self._from_fbs.TagsLength() > 0:
                tags = []
                for i in range(self._from_fbs.TagsLength()):
                    s = self._from_fbs.Tags(i)
                    tags.append(s.decode())
                self._tags = tags
        return self._tags

    @tags.setter
    def tags(self, value):
        assert type(value) == list
        assert (type(tag) == six.text_type for tag in value)

        self._tags = value

    @property
    def email(self):
        if self._email is None and self._from_fbs:
            s = self._from_fbs.Email()
            if s:
                self._email = s.decode()
        return self._email

    @email.setter
    def email(self, value):
        assert type(value) == six.text_type

        self._email = value

    @property
    def registered(self):
        if self._registered is None and self._from_fbs:
            val = self._from_fbs.Registered()
            if val:
                # utcfromtimestamp
                # self._registered = datetime.utcfromtimestamp(float(val) / 1000000.)
                # calendar.timegm(dt.utctimetuple())
                self._registered = datetime.fromtimestamp(float(val) / 1000000.)

        return self._registered

    @registered.setter
    def registered(self, value):
        assert isinstance(value, datetime)

        self._registered = value

    @property
    def pubkey(self):
        if self._pubkey is None and self._from_fbs:
            self._pubkey = self._from_fbs.Pubkey().decode()

        return self._pubkey

    @pubkey.setter
    def pubkey(self, value):
        # hex string with 256 bit Ed25519 WAMP-cryptosign public key
        assert type(value) == six.text_type
        assert len(value) == 64

        self._pubkey = value

    @staticmethod
    def cast(buf):
        return UserFbs(UserGenFbs.User.GetRootAsUser(buf, 0))

    def build(self, builder):

        # serialize all stuff we need later first (because we cannot build nested) ..

        # label: string
        label = self.label
        if label:
            label = builder.CreateString(label)

        # description: string
        description = self.description
        if description:
            description = builder.CreateString(description)

        # email: string
        email = self.email
        if email:
            email = builder.CreateString(email)

        # pubkey: string
        pubkey = self.pubkey
        if pubkey:
            pubkey = builder.CreateString(pubkey)

        # tags: [string]
        tags = self.tags
        if tags:
            _tags = []
            for tag in tags:
                _tags.append(builder.CreateString(tag))

            UserGenFbs.UserStartTagsVector(builder, len(_tags))

            for o in reversed(_tags):
                builder.PrependUOffsetTRelative(o)

            tags = builder.EndVector(len(_tags))

        # now start and build a new object ..
        UserGenFbs.UserStart(builder)

        # oid: uuid.UUID
        if self.oid:
            bytes = self.oid.bytes
            msb = struct.unpack('>Q', bytes[8:])[0]
            lsb = struct.unpack('>Q', bytes[:8])[0]
            oid = oid_t.Createoid_t(builder, msb=msb, lsb=lsb)
            UserGenFbs.UserAddOid(builder, oid)

        if label:
            UserGenFbs.UserAddLabel(builder, label)
        if description:
            UserGenFbs.UserAddDescription(builder, description)
        if tags:
            UserGenFbs.UserAddTags(builder, tags)
        if email:
            UserGenFbs.UserAddEmail(builder, email)

        # registered: datetime
        if self.registered:
            registered = int(self.registered.timestamp() * 1000000)
            UserGenFbs.UserAddRegistered(builder, registered)

        if pubkey:
            UserGenFbs.UserAddPubkey(builder, pubkey)

        # finish the object.
        final = UserGenFbs.UserEnd(builder)

        return final


class UserMrealmRole(object):
    """
    Database class for CFC user roles on a management realm using CBOR.
    """
    def __init__(self, roles=None, _unknown=None):
        self.roles = roles

        # private member with unknown/untouched data passing through
        self._unknown = _unknown

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if other.roles != self.roles:
            return False
        return True

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        return '\n{}\n'.format(pformat(self.marshal()))

    def copy(self, other):
        self.roles = other.roles[:]

        # _unknown is not copied!

    def marshal(self):
        assert type(self.roles) == list
        for role in self.roles:
            assert type(role) in six.integer_types
            assert role in [UserRole.OWNER, UserRole.ADMIN, UserRole.USER, UserRole.GUEST]

        obj = {
            'roles': self.roles,
        }

        if self._unknown:
            # pass through all attributes unknown
            obj.update(self._unknown)
        else:
            return obj

        return obj

    @staticmethod
    def parse(data):
        assert type(data) == dict

        # future attributes (yet unknown) are not only ignored, but passed through!
        _unknown = {}
        for k in data:
            if k not in ['roles']:
                _unknown[k] = data[k]

        roles = data.get('roles', None)
        assert type(roles) == list

        for role in roles:
            assert type(role) in six.integer_types
            assert role in [UserRole.OWNER, UserRole.ADMIN, UserRole.USER, UserRole.GUEST]

        obj = UserMrealmRole(roles=roles, _unknown=_unknown)
        return obj


class UserMrealmRoleFbs(object):
    """
    Database class for CFC user roles on a management realm using Flatbuffers.
    """
    def __init__(self):
        raise NotImplementedError('not yet implemented')


class ActivationToken(object):
    """
    CFC user activation token database class for CBOR.
    """
    def __init__(self,
                 oid=None,
                 atype=None,
                 status=None,
                 created=None,
                 completed=None,
                 code=None,
                 email=None,
                 pubkey=None,
                 _unknown=None):
        self.oid = oid
        self.atype = atype
        self.status = status
        self.created = created
        self.completed = completed
        self.code = code
        self.email = email
        self.pubkey = pubkey

        self._unknown = _unknown

    def __str__(self):
        return pformat(self.marshal())

    def copy(self, other):
        self.oid = other.oid
        self.atype = other.atype
        self.status = other.status
        self.created = other.created
        self.completed = other.completed
        self.code = other.code
        self.email = other.email
        self.pubkey = other.pubkey

        # _unknown is not copied!

    def marshal(self):
        assert isinstance(self.oid, uuid.UUID)
        assert self.atype in [ActivationType.LOGIN, ActivationType.REGISTRATION]
        assert self.status in [ActivationStatus.EXPIRED, ActivationStatus.PENDING, ActivationStatus.ACTIVE]
        assert isinstance(self.created, datetime)
        assert self.completed is None or isinstance(self.completed, datetime)
        assert self.code is None or type(self.code) == six.text_type
        assert self.email is None or type(self.email) == six.text_type
        assert self.pubkey is None or (type(self.pubkey) == six.text_type and len(self.pubkey) == 64)
        assert self._unknown is None or type(self._unknown) == dict

        created = float(self.created.timestamp()) * 1000000.
        completed = None
        if self.completed:
            completed = float(self.completed.timestamp()) * 1000000.

        obj = {
            u'oid': str(self.oid),
            u'atype': self.atype,
            u'status': self.status,
            u'created': created,
            u'completed': completed,
            u'code': self.code,
            u'email': self.email,
            u'pubkey': self.pubkey
        }

        if self._unknown:
            # pass through all attributes unknown
            obj.update(self._unknown)
        else:
            return obj

    @staticmethod
    def parse(data):
        assert type(data) == dict

        # future attributes (yet unknown) are not only ignored, but passed through!
        _unknown = {}
        for k in data:
            if k not in ['oid', 'atype', 'status', 'created', 'completed', 'code', 'email', 'pubkey']:
                val = data.pop(k)
                _unknown[k] = val

        oid = data.get('oid', None)
        assert type(oid) == six.text_type
        oid = uuid.UUID(oid)

        atype = data.get('atype', None)
        assert type(atype) in six.integer_types

        status = data.get('status', None)
        assert type(status) in six.integer_types

        created = data.get('created', None)
        assert type(created) == float or type(created) in six.integer_types

        created = datetime.fromtimestamp(float(created) / 1000000.)
        # created = datetime.utcfromtimestamp(float(created) / 1000000.)

        completed = data.get('completed', None)
        assert completed is None or type(completed) == float or type(completed) in six.integer_types
        if completed:
            # https://docs.python.org
            # /3/library/time.html#time.time_ns
            # https://docs.python.org/3/library/datetime.html#datetime.datetime.timestamp

            completed = datetime.fromtimestamp(float(completed) / 1000000.)
            # completed = datetime.utcfromtimestamp(float(completed) / 1000000.)

        code = data.get('code', None)
        assert type(code) == six.text_type

        email = data.get('email', None)
        assert email is None or type(email) == six.text_type

        pubkey = data.get('pubkey', None)
        assert pubkey is None or type(pubkey) == six.text_type
        if pubkey:
            assert len(pubkey) == 64

        obj = ActivationToken(oid=oid,
                              atype=atype,
                              status=status,
                              created=created,
                              completed=completed,
                              code=code,
                              email=email,
                              pubkey=pubkey,
                              _unknown=_unknown)
        return obj


class ActivationTokenFbs(object):
    """
    CFC user activation token database class for Flatbuffers.
    """
    def __init__(self, from_fbs=None):
        self._from_fbs = from_fbs

        self._oid = None
        self._atype = None
        self._status = None
        self._created = None
        self._completed = None
        self._code = None
        self._email = None
        self._pubkey = None

    def copy(self, other):
        self._oid = other.oid
        self._atype = other.atype
        self._status = other.status
        self._created = other.created
        self._completed = other.completed
        self._code = other.code
        self._email = other.email
        self._pubkey = other.pubkey

    @property
    def oid(self):
        if self._oid is None and self._from_fbs:
            s = self._from_fbs.Oid()
            if s:
                self._oid = uuid.UUID(s.decode())

        return self._oid

    @oid.setter
    def oid(self, value):
        assert isinstance(value, uuid.UUID)

        self._oid = value

    @property
    def atype(self):
        if self._atype is None and self._from_fbs:
            self._atype = self._from_fbs.Atype()

        return self._atype

    @atype.setter
    def atype(self, value):
        assert type(value) in six.integer_types
        assert value in [ActivationType.REGISTRATION, ActivationType.LOGIN]

        self._atype = value

    @property
    def status(self):
        if self._status is None and self._from_fbs:
            self._status = self._from_fbs.Status()

        return self._status

    @status.setter
    def status(self, value):
        assert type(value) in six.integer_types
        assert value in [ActivationStatus.PENDING, ActivationStatus.ACTIVE, ActivationStatus.EXPIRED]

        self._status = value

    @property
    def created(self):
        if self._created is None and self._from_fbs:
            val = self._from_fbs.Created()
            if val:
                self._created = datetime.utcfromtimestamp(float(val) / 1000000.)

        return self._created

    @created.setter
    def created(self, value):
        assert isinstance(value, datetime)

        self._created = value

    @property
    def completed(self):
        if self._completed is None and self._from_fbs:
            val = self._from_fbs.Completed()
            if val:
                self._completed = datetime.utcfromtimestamp(float(val) / 1000000.)

        return self._completed

    @completed.setter
    def completed(self, value):
        assert value is None or isinstance(value, datetime)

        self._completed = value

    @property
    def code(self):
        if self._code is None and self._from_fbs:
            self._code = self._from_fbs.Code().decode()

        return self._code

    @code.setter
    def code(self, value):
        assert type(value) == six.text_type

        self._code = value

    @property
    def email(self):
        if self._email is None and self._from_fbs:
            self._email = self._from_fbs.Email().decode()

        return self._email

    @email.setter
    def email(self, value):
        assert type(value) == six.text_type

        self._email = value

    @property
    def pubkey(self):
        if self._pubkey is None and self._from_fbs:
            self._pubkey = self._from_fbs.Pubkey().decode()

        return self._pubkey

    @pubkey.setter
    def pubkey(self, value):
        # hex string with 256 bit Ed25519 WAMP-cryptosign public key
        assert type(value) == six.text_type
        assert len(value) == 64

        self._pubkey = value

    @staticmethod
    def cast(buf):
        return ActivationTokenFbs(ActivationTokenGenFbs.ActivationToken.GetRootAsActivationToken(buf, 0))

    def build(self, builder):

        oid = self.oid
        if oid:
            oid = builder.CreateString(str(oid))

        code = self.code
        if code:
            code = builder.CreateString(code)

        email = self.email
        if email:
            email = builder.CreateString(email)

        pubkey = self.pubkey
        if pubkey:
            pubkey = builder.CreateString(pubkey)

        ActivationTokenGenFbs.ActivationTokenStart(builder)

        if oid:
            ActivationTokenGenFbs.ActivationTokenAddOid(builder, oid)

        ActivationTokenGenFbs.ActivationTokenAddAtype(builder, self.atype)
        ActivationTokenGenFbs.ActivationTokenAddStatus(builder, self.status)

        if self.created:
            ActivationTokenGenFbs.ActivationTokenAddCreated(builder, int(self.created.timestamp() * 1000000))

        if self.completed:
            ActivationTokenGenFbs.ActivationTokenAddCompleted(builder,
                                                              int(self.completed.timestamp() * 1000000))

        if code:
            ActivationTokenGenFbs.ActivationTokenAddCode(builder, code)

        if email:
            ActivationTokenGenFbs.ActivationTokenAddEmail(builder, email)

        if pubkey:
            ActivationTokenGenFbs.ActivationTokenAddPubkey(builder, pubkey)

        final = ActivationTokenGenFbs.ActivationTokenEnd(builder)

        return final


class Organization(ConfigurationElement):
    """
    CFC organization database class.
    """

    # oid: uuid.UUID
    # label: Optional[str]
    # description: Optional[str]
    # tags: Optional[List[str]]
    # name: str
    # otype: int
    # registered: Optional[datetime]

    OTYPES = [
        OrganizationType.NONE, OrganizationType.BUSINESS, OrganizationType.ACADEMICS,
        OrganizationType.PERSONAL
    ]

    def __init__(self,
                 oid=None,
                 label=None,
                 description=None,
                 tags=None,
                 name=None,
                 otype=None,
                 registered=None,
                 _unknown=None):
        """

        :param oid: Object ID of the organization
        :type oid: uuid.UUID

        :param label: Optional user label of the organization
        :type label: str

        :param description: Optional user description of the organization
        :type description: str

        :param tags: Optional list of user tags on the organization
        :type tags: list[str]

        :param name: Name of the organization
        :type name: str

        :param otype: Type of the organization.
        :type otype: int

        :param registered: Timestamp when the organization was created
        :type registered: datetime.datetime

        :param _unknown: Any unparsed/unprocessed data attributes
        :type _unknown: None or dict
        """
        ConfigurationElement.__init__(self, oid=oid, label=label, description=description, tags=tags)

        self.name = name
        self.otype = otype
        self.registered = registered

        # private member with unknown/untouched data passing through
        self._unknown = _unknown

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if not ConfigurationElement.__eq__(self, other):
            return False
        if other.name != self.name:
            return False
        if other.otype != self.otype:
            return False
        if other.registered != self.registered:
            return False
        return True

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        return '\n{}\n'.format(pformat(self.marshal()))

    def copy(self, other):
        ConfigurationElement.copy(self, other)

        self.name = other.name
        self.otype = other.otype
        self.registered = other.registered

        # _unknown is not copied!

    def marshal(self):
        obj = ConfigurationElement.marshal(self)

        assert self.name is None or type(self.name) == six.text_type
        assert self.otype is None or self.otype in Organization.OTYPES
        assert self.registered is None or isinstance(self.registered, datetime)

        registered = int(self.registered.timestamp() * 1000000) if self.registered else None
        obj.update({
            'name': self.name,
            'otype': self.otype,
            'registered': registered,
        })

        if self._unknown:
            # pass through all attributes unknown
            obj.update(self._unknown)

        return obj

    @staticmethod
    def parse(data):
        assert type(data) == dict

        obj = ConfigurationElement.parse(data)
        data = obj._unknown

        # future attributes (yet unknown) are not only ignored, but passed through!
        _unknown = {}
        for k in data:
            if k not in ['name', 'otype', 'registered']:
                _unknown[k] = data[k]

        name = data.get('name', None)
        assert name is None or type(name) == six.text_type

        otype = data.get('otype', None)
        assert otype is None or otype in Organization.OTYPES

        registered = data.get('registered', None)
        assert registered is None or type(registered) == float or type(registered) in six.integer_types
        if registered:
            # registered = datetime.utcfromtimestamp(float(registered) / 1000000.)
            registered = datetime.fromtimestamp(float(registered) / 1000000.)

        obj = Organization(oid=obj.oid,
                           label=obj.label,
                           description=obj.description,
                           tags=obj.tags,
                           name=name,
                           otype=otype,
                           registered=registered,
                           _unknown=_unknown)
        return obj


class OrganizationFbs(object):
    """
    CFC user database class using Flatbuffers.
    """

    # oid: uuid.UUID

    # label: Optional[str]
    # description: Optional[str]
    # tags: Optional[List[str]]

    # name: str
    # registered: datetime
    # otype: int

    def __init__(self, from_fbs=None):
        self._from_fbs = from_fbs

        self._oid = None

        self._label = None
        self._description = None
        self._tags = None

        self._name = None
        self._otype = None
        self._registered = None

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False

        if other.oid != self.oid:
            return False

        if other.label != self.label:
            return False
        if other.description != self.description:
            return False
        if (other.tags and not self.tags) or (not other.tags and self.tags):
            return False
        if other.tags:
            if not set(other.tags).intersection(set(self.tags)):
                return False

        if other.name != self.name:
            return False
        if other.otype != self.otype:
            return False
        if other.registered != self.registered:
            return False

        return True

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        return '\n{}\n'.format(pformat(self.marshal()))

    def copy(self, other):
        self.oid = other.oid
        self.label = other.label
        self.description = other.description
        self.tags = other.tags
        self.name = other.name
        self.otype = other.otype
        self.registered = other.registered

        # _unknown is not copied!

    @property
    def oid(self):
        if self._oid is None and self._from_fbs:
            oid = self._from_fbs.Oid()
            if oid:
                bytes = struct.pack('>Q', oid.Lsb()) + struct.pack('>Q', oid.Msb())
                self._oid = uuid.UUID(bytes=bytes)
        return self._oid

    @oid.setter
    def oid(self, value):
        assert value is None or isinstance(value, uuid.UUID)

        self._oid = value

    @property
    def label(self):
        if self._label is None and self._from_fbs:
            s = self._from_fbs.Label()
            if s:
                self._label = s.decode()
        return self._label

    @label.setter
    def label(self, value):
        assert value is None or type(value) == six.text_type

        self._label = value

    @property
    def description(self):
        if self._description is None and self._from_fbs:
            s = self._from_fbs.Description()
            if s:
                self._description = s.decode()
        return self._description

    @description.setter
    def description(self, value):
        assert value is None or type(value) == six.text_type

        self._description = value

    @property
    def tags(self):
        if self._tags is None and self._from_fbs:
            if self._from_fbs.TagsLength() > 0:
                tags = []
                for i in range(self._from_fbs.TagsLength()):
                    s = self._from_fbs.Tags(i)
                    tags.append(s.decode())
                self._tags = tags
        return self._tags

    @tags.setter
    def tags(self, value):
        assert value is None or (type(value) == list and (type(tag) == six.text_type for tag in value))

        self._tags = value

    @property
    def name(self):
        if self._name is None and self._from_fbs:
            s = self._from_fbs.Name()
            if s:
                self._name = s.decode()
        return self._name

    @name.setter
    def name(self, value):
        assert value is None or type(value) == six.text_type

        self._name = value

    @property
    def registered(self):
        if self._registered is None and self._from_fbs:
            val = self._from_fbs.Registered()
            if val:
                # utcfromtimestamp
                # self._registered = datetime.utcfromtimestamp(float(val) / 1000000.)
                # calendar.timegm(dt.utctimetuple())
                self._registered = datetime.fromtimestamp(float(val) / 1000000.)

        return self._registered

    @registered.setter
    def registered(self, value):
        assert value is None or isinstance(value, datetime)

        self._registered = value

    @property
    def otype(self):
        if self._otype is None and self._from_fbs:
            self._otype = self._from_fbs.Otype()

        return self._otype

    @otype.setter
    def otype(self, value):
        assert value is None or type(value) in six.integer_types

        self._otype = value

    @staticmethod
    def cast(buf):
        return OrganizationFbs(OrganizationGenFbs.Organization.GetRootAsOrganization(buf, 0))

    def build(self, builder):

        # serialize all stuff we need later first (because we cannot build nested) ..

        # label: string
        label = self.label
        if label:
            label = builder.CreateString(label)

        # description: string
        description = self.description
        if description:
            description = builder.CreateString(description)

        # name: string
        name = self.name
        if name:
            name = builder.CreateString(name)

        # tags: [string]
        tags = self.tags
        if tags:
            _tags = []
            for tag in tags:
                _tags.append(builder.CreateString(tag))

            OrganizationGenFbs.OrganizationStartTagsVector(builder, len(_tags))

            for o in reversed(_tags):
                builder.PrependUOffsetTRelative(o)

            tags = builder.EndVector(len(_tags))

        # now start and build a new object ..
        OrganizationGenFbs.OrganizationStart(builder)

        # oid: uuid.UUID
        if self.oid:
            bytes = self.oid.bytes
            msb = struct.unpack('>Q', bytes[8:])[0]
            lsb = struct.unpack('>Q', bytes[:8])[0]
            oid = oid_t.Createoid_t(builder, msb=msb, lsb=lsb)
            OrganizationGenFbs.OrganizationAddOid(builder, oid)

        if label:
            OrganizationGenFbs.OrganizationAddLabel(builder, label)
        if description:
            OrganizationGenFbs.OrganizationAddDescription(builder, description)
        if tags:
            OrganizationGenFbs.OrganizationAddTags(builder, tags)
        if name:
            OrganizationGenFbs.OrganizationAddName(builder, name)

        # registered: datetime
        if self.registered:
            registered = int(self.registered.timestamp() * 1000000)
            OrganizationGenFbs.OrganizationAddRegistered(builder, registered)

        if self.otype:
            OrganizationGenFbs.OrganizationAddOtype(builder, self.otype)

        # finish the object.
        final = OrganizationGenFbs.OrganizationEnd(builder)

        return final
