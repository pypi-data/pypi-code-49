# Deals with assigning uidNumber / gitNumber values
import ldap
import logging

from contextlib import contextmanager
from copy import copy

from .ldapfilter import Filter, OrGroup, BitAndFilter
from .util import single


logger = logging.getLogger(__name__)


# We exclude certain users and groups from id assignment.
# See "Automatically assigning uidNumber / gidNumber attributes"
# https://lists.samba.org/archive/samba/2019-June/223499.html

# Guidance: Exclude Administrator
EXCLUDE_CN_USERS = [
    'Administrator',
    'Guest',
]

# Guidance: Exclude all groups provided by provision, with the exception of
# Domain Users.
#
# Domain Admins is explicitly excluded to avoid problems with ownership of
# files in Sysvol on Samba DCs:
#  - https://lists.samba.org/archive/samba/2015-February/189287.html
#  - https://lists.samba.org/archive/samba/2020-January/227972.html
EXCLUDE_CN_GROUPS = [
    'Allowed RODC Password Replication Group',
    'Schema Admins',
    'Denied RODC Password Replication Group',
    'Cert Publishers',
    #'Domain Users',
    'Enterprise Admins',
    'Domain Computers',
    'DnsAdmins',
    'Domain Controllers',
    'Enterprise Read-only Domain Controllers',
    #'Domain Guests',
    'DnsUpdateProxy',
    'Read-only Domain Controllers',
    'Domain Admins',
    'RAS and IAS Servers',
    'Group Policy Creator Owners',
]

BUILTIN_LOCAL_GROUP = 0x00000001


class AssignmentError(Exception):
    pass


class AssignerBase:
    def __init__(self, ad, onchange=None):
        self.ad = ad
        self.onchange = onchange

        self.user_filt  = ~OrGroup(*(Filter('CN={}'.format(u)) for u in EXCLUDE_CN_USERS))
        self.group_filt = ( ~OrGroup(*(Filter('CN={}'.format(g)) for g in EXCLUDE_CN_GROUPS))
                            & ~BitAndFilter('groupType', BUILTIN_LOCAL_GROUP)
                          )


    def get_users(self, attrs=None, all_users=False, rdn=None, scope=None):
        filt = None if all_users else self.user_filt
        return self.ad.get_users(filt=filt, attrs=attrs, rdn=rdn, scope=scope)


    def get_groups(self, attrs=None, all_groups=False):
        filt = None if all_groups else self.group_filt
        return self.ad.get_groups(filt=filt, attrs=attrs)


    def _log_change(self, object_type, dn, attribute, value):
        data = dict(
            object_type = object_type,
            dn = dn,
            attribute = attribute,
            value = value,
        )

        message = "Set {attribute}={value} for {object_type} '{dn}'".format(**data)
        logger.info(message)

        if self.onchange:
            self.onchange(message=message, data=data)



class PosixIdAssigner(AssignerBase):
    def __init__(self, ad, state, uid_range, gid_range, replace_invalid=False, onchange=None):
        super().__init__(ad=ad, onchange=onchange)

        self.state = state
        self.uid_range = uid_range
        self.gid_range = gid_range
        self.replace_invalid = replace_invalid

        self._validate_next_uid()
        self._validate_next_gid()

        logger.info("Next uidNumber={} in {}".format(self.state.next_uid, self.uid_range))
        logger.info("Next gidNumber={} in {}".format(self.state.next_gid, self.gid_range))


    def _validate_next_uid(self):
        if not self.state.next_uid in self.uid_range:
            raise AssignmentError("Next uidNumber={} is not in uid_range={}".format(
                    self.state.next_uid, self.uid_range))


    def _validate_next_gid(self):
        if not self.state.next_gid in self.gid_range:
            raise AssignmentError("Next gidNumber={} is not in gid_range={}".format(
                    self.state.next_gid, self.gid_range))


    def _ensure_uid_unused(self, uid):
        u = self.ad.get_user_by_uid(uid, ['dn'])   # TODO: How to specify no attrs at all, just dn?
        if u:
            raise AsssignmentError("User with uidNumber={} already exists: {}".format(uid, dn))


    def _ensure_gid_unused(self, gid):
        grp = self.ad.get_group_by_gid(gid, ['dn'])   # TODO: How to specify no attrs at all, just dn?
        if grp:
            raise AssignmentError("Group with gidNumber={} already exists: {}".format(gid, grp.dn))


    def _need_assign_xidNumber(self, objtype, obj, attr, valid_range):
        # Check for existing xidNumber
        xid = getattr(obj, attr, None)
        if xid is None:
            # Doesn't exist; needs assigned
            logger.info("Found {} without {}: {}".format(objtype, attr, obj.dn))
            return True

        # Valid?
        if not xid in valid_range:
            logger.warning("{} {} {} {} not in {}".format(
                objtype, obj.dn, attr, xid, valid_range))
            # Exists but invalid; needs assigned if we're replacing invalid xids
            return self.replace_invalid

        return False


    def assign_user_uidNumbers(self):
        logger.info("Assigning User uidNumbers")
        for user in self.get_users():
            if self._need_assign_xidNumber('User', user, 'uidNumber', self.uid_range):
                self._assign_user_uidNumber(user)


    def _assign_user_uidNumber(self, user):
        with self.next_uid() as new_uid:
            # TODO: How do we make the LDAP part transactional, too?
            logger.info("Assigning new uidNumber to user %s, assigning %d", user.dn, new_uid)

            self._ensure_uid_unused(new_uid)

            user.uidNumber = new_uid
            user.commit()

            self._log_change("user", user.dn, 'uidNumber', new_uid)


    def update_user_gidNumbers(self):
        """Ensure all user gidNumber attributes match their primary group"""
        logger.info("Setting User gidNumbers")

        attrs = ['gidNumber', 'objectSid', 'primaryGroupID']
        for user in self.get_users(attrs=attrs):
            # Construct the group SID from the domain SID and primaryGroupID attr
            # https://support.microsoft.com/en-us/help/297951
            groupsid = copy(user.objectSid)
            groupsid.rid = user.primaryGroupID

            grp = self.ad.get_group_by_sid(groupsid)
            if not grp:
                logger.warning("Couldn't find primary group %s for user %s", groupsid, user.dn)
                continue

            group_gidNumber = getattr(grp, 'gidNumber', None)
            if group_gidNumber is None:
                logger.warning("User %s primary group %s has no gidNumber", user.dn, grp.dn)
                continue

            user_gidNumber = getattr(user, 'gidNumber', None)
            if user_gidNumber == group_gidNumber:
                # No changes needed
                continue

            logger.info("User %s gidNumber (%s) does not match their primary group %s gidNumber (%d)",
                    user.dn, user_gidNumber, groupsid, group_gidNumber)

            user.gidNumber = group_gidNumber
            user.commit()

            self._log_change("user", user.dn, 'gidNumber', group_gidNumber)


    def assign_group_gidNumbers(self):
        logger.info("Assigning Group gidNumbers")
        for group in self.get_groups():
            if self._need_assign_xidNumber('Group', group, 'gidNumber', self.gid_range):
                self._assign_group_gidNumber(group)


    def _assign_group_gidNumber(self, group):
        with self.next_gid() as new_gid:
            # TODO: How do we make the LDAP part transactional, too?
            logger.info("Assigning new gidNumber to group %s: %d", group.dn, new_gid)

            self._ensure_gid_unused(new_gid)

            group.gidNumber = new_gid
            group.commit()

            self._log_change("group", group.dn, 'gidNumber', new_gid)


    def clear_group_gidNumbers(self):
        logger.info("Clearing Group gidNumbers")
        for group in self.get_groups(all_groups=True):
            if getattr(group, 'gidNumber', None) is None:
                continue

            logger.info("Clearing gidNumber for group %s", group.dn)
            group.gidNumber = None
            group.commit()
            self._log_change("group", group.dn, 'gidNumber', None)


    def _clear_user_attr(self, attr):
        for user in self.get_users(all_users=True):
            if getattr(user, attr, None) is None:
                continue

            logger.info("Clearing %s for user %s", attr, user.dn)
            setattr(user, attr, None)
            user.commit()
            self._log_change("user", user.dn, attr, None)


    def clear_user_uidNumbers(self):
        logger.info("Clearing User uidNumbers")
        self._clear_user_attr('uidNumber')


    def clear_user_gidNumbers(self):
        logger.info("Clearing User gidNumbers")
        self._clear_user_attr('gidNumber')


    @contextmanager
    def next_uid(self):
        self._validate_next_uid()
        yield self.state.next_uid

        self.state.next_uid += 1
        self.state.commit()


    @contextmanager
    def next_gid(self):
        self._validate_next_gid()
        yield self.state.next_gid

        self.state.next_gid += 1
        self.state.commit()



class UpnAssigner(AssignerBase):
    def __init__(self, ad, onchange=None):
        super().__init__(ad, onchange=onchange)

        self.upn_suffixes = self.get_alt_upn_suffixes()
        self.upn_suffixes.append(self.ad.dnsdomain)
        logger.debug("Domain UPN suffixes: {}".format(self.upn_suffixes))


    def get_alt_upn_suffixes(self):
        r = self.ad._search(
            base_rdn='CN=Partitions,CN=Configuration',
            attrs=['uPNSuffixes'],
            scope=ldap.SCOPE_BASE,
            )

        dn, attrvals = single(r)
        return [s.decode() for s in attrvals.get('uPNSuffixes', [])]   # TODO: encoding?


    def set_user_upn_suffixes(self, container, conf_suffix, scope='subtree'):
        logger.info("Setting UPN suffix to {} for container {}".format(conf_suffix, container))

        # Map scope string to ldap scope
        scope = {
            'subtree':  ldap.SCOPE_SUBTREE,
            'one':      ldap.SCOPE_ONELEVEL,
        }[scope]

        # First ensure that suffix is a valid UPN suffix
        if not conf_suffix in self.upn_suffixes:
            raise AssignmentError("UPN suffix '{}' not configured in Domain".format(conf_suffix))

        # Now iterate over all users in that container
        for user in self.get_users(rdn=container, scope=scope):
            username, cur_suffix = user.userPrincipalName.split('@')

            if cur_suffix == conf_suffix:
                continue

            logger.info("UPN {} does not match configured suffix {}".format(
                user.userPrincipalName, conf_suffix))

            new_upn = '@'.join((username, conf_suffix))
            user.userPrincipalName = new_upn
            user.commit()
            self._log_change("user", user.dn, 'userPrincipalName', new_upn)
