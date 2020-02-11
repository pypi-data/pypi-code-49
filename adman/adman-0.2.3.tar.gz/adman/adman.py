import ldap
import logging

from .ldapfilter import Filter
from .ldapobj import LdapObject, IntAttr, StrAttr, SIDAttr, FILETIMEAttr
from .locate import get_domain_ldap_servers
from .util import single_or
from .version import __version__

from ldap.filter import escape_filter_chars


logger = logging.getLogger(__name__)


USER_SEARCH_FILTER = Filter('objectClass=user') & Filter('objectCategory=Person') & ~Filter('sAMAccountName=krbtgt*')

GROUP_SEARCH_FILTER = Filter('objectClass=group')



def get_dc_info(l):
    attrs = ['defaultNamingContext', 'dnsHostName']
    r = l.search_s('', ldap.SCOPE_BASE, None, attrs)[0]
    dn, attr_vals = r
    return {k: v[0].decode() for k, v in attr_vals.items()}


def ldap_initialize(domain, proto=None):
    uri = ' '.join(get_domain_ldap_servers(domain, proto=proto))

    logger.debug("ldap.initialize(uri={!r})".format(uri))
    return ldap.initialize(uri)


def ldap_connect_gssapi(domain):
    l = ldap_initialize(domain)

    # https://github.com/python-ldap/python-ldap/issues/275
    l.set_option(ldap.OPT_REFERRALS, 0)


    # Perform an anonymous bind first to get server info
    l.simple_bind_s()
    info = get_dc_info(l)

    # Perform a GSSAPI (Kerberos) secure SASL bind
    l.sasl_gssapi_bind_s()

    return l, info


class ADManager:
    def __init__(self, dnsdomain, ldapconn, base=None):
        self.dnsdomain = dnsdomain
        self.ldapconn = ldapconn
        self.base = base


    @classmethod
    def connect(cls, dnsdomain):
        ldapconn, ldapinfo = ldap_connect_gssapi(dnsdomain)
        logger.info("Connected to {dnsHostName} ({defaultNamingContext})".format(**ldapinfo))

        ad = cls(
                dnsdomain = dnsdomain,
                ldapconn = ldapconn,
                base = ldapinfo['defaultNamingContext'],
            )

        return ad


    def _search(self, base_rdn=None, filt=None, attrs=None, scope=None):
        base = self.base
        if base_rdn is not None:
            base = base_rdn + ',' + base

        if filt is not None:
            filt = str(filt)

        if scope is None:
            scope = ldap.SCOPE_SUBTREE

        logger.debug("Search base: {}".format(base))
        logger.debug("Search scope: {}".format(scope))
        logger.debug("Search filter: {}".format(filt))
        logger.debug("Search attrs: {}".format(attrs))
        results = self.ldapconn.search_s(base, scope, filt, attrs)

        for dn, attrs in results:
            if dn is None:
                # Filter out referrals
                # https://mail.python.org/pipermail/python-ldap/2014q1/003350.html
                uri = attrs
                logger.debug("Received referral: %s", uri)
                continue
            yield dn, attrs


    def _modify(self, dn, modlist):
        rc = self.ldapconn.modify_s(dn, modlist)
        logger.debug("modify_s({!r}, {!r}) returned {}".format(
            dn, modlist, rc))


    def get_users(self, rdn=None, filt=None, attrs=None, scope=None):
        if attrs is None:
            attrs = AdUser.default_ldap_attrs()

        f = USER_SEARCH_FILTER
        if filt is not None:    # Append caller filter
            f = f & filt

        userlist = self._search(base_rdn=rdn, filt=f, attrs=attrs, scope=scope)
        for dn, attrvals in userlist:
            yield AdUser(self, dn, **attrvals)


    def get_user_by_uid(self, uid, attrs=None):
        filt = Filter('uidNumber={}'.format(uid))
        return single_or(self.get_users(filt=filt, attrs=attrs), None)


    def get_groups(self, rdn=None, filt=None, attrs=None):
        if attrs is None:
            attrs = AdGroup.default_ldap_attrs()

        f = GROUP_SEARCH_FILTER
        if filt is not None:    # Append caller filter
            f = f & filt

        grouplist = self._search(rdn, f, attrs)
        for dn, attrvals in grouplist:
            yield AdGroup(self, dn, **attrvals)


    def get_group_by_gid(self, gid, attrs=None):
        filt = Filter('gidNumber={}'.format(gid))
        return single_or(self.get_groups(filt=filt, attrs=attrs), None)

    def get_group_by_sid(self, sid, attrs=None):
        filt = Filter('objectSid={}'.format(escape_filter_chars(str(sid), 1)))
        return single_or(self.get_groups(filt=filt, attrs=attrs), None)


class AdUser(LdapObject):
    _known_attrs = (
        StrAttr('cn'),
        IntAttr('uidNumber', writable=True),
        IntAttr('gidNumber', writable=True),
        IntAttr('primaryGroupID'),
        SIDAttr('objectSid'),
        StrAttr('userPrincipalName', writable=True),
        StrAttr('mail'),
        FILETIMEAttr('pwdLastSet'),
        FILETIMEAttr('PasswordExpiryTime', ldapattr='msDS-UserPasswordExpiryTimeComputed'),
    )


class AdGroup(LdapObject):
    _known_attrs = (
        StrAttr('cn'),
        IntAttr('gidNumber', writable=True),
        SIDAttr('objectSid'),
    )
