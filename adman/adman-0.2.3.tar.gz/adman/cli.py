import argparse
import logging
import sys
from functools import wraps

from .adman import ADManager
from .assign import PosixIdAssigner, AssignmentError, UpnAssigner
from .config import Config, ConfigError
from .paths import default_confpath
from .pwexpire import check_pw_expiry
from .state import DomainState
from .kerberos import setup_kerberos_environ, KerberosError
from .version import __version__


logger = logging.getLogger(__name__)


class AppError(Exception):
    pass



def confirm(question="Are you sure?"):
    while True:
        try:
            reply = input(question + " (yes/no): ").lower().strip()
        except (EOFError, KeyboardInterrupt):
            return False

        if reply[:1] == 'y':
            return True
        if reply[:1] == 'n':
            return False


def get_state(ad):
    s = DomainState.get(ad)
    logger.debug("DomainState: {}".format(s._data))
    if not s.complete:
        raise AppError("Domain ID number state not initialized. (Try 'state init')")
    return s


def get_posix_assigner(ad, args):
    def change_handler(message, data):
        args.changelog.write(message + '\n')

    return PosixIdAssigner(
            ad = ad,
            state = get_state(ad),
            uid_range = args.config.uid_range,
            gid_range = args.config.gid_range,
            replace_invalid = args.force,
            onchange = change_handler,
            )


def connect_ad(func):
    @wraps(func)
    def wrapper(args):

        domain = args.config.domain
        lc = args.config.ldap_auth

        if lc.mode != 'gssapi':
            raise NotImplementedError("Only gssapi mode is supported")

        # TODO: Does this belong in ADManager?
        setup_kerberos_environ(
                username = lc.username,
                realm = domain,
                keytab = lc.keytab,
                cache = lc.cache,
            )

        ad = ADManager.connect(domain)
        return func(ad, args)
    return wrapper


@connect_ad
def cmd_allmaint(ad, args):
    cmd_assignids.__wrapped__(ad, args)
    cmd_user_setupns.__wrapped__(ad, args)
    cmd_user_checkexpire.__wrapped__(ad, args)


@connect_ad
def cmd_assignids(ad, args):
    logger.info("Assigning POSIX IDs")
    a = get_posix_assigner(ad, args)
    a.assign_group_gidNumbers()
    a.assign_user_uidNumbers()
    a.update_user_gidNumbers()


@connect_ad
def cmd_clearids(ad, args):
    if not args.force:
        print("This command will clear *all* uidNumber/gidNumber attributes!")
        if not confirm():
            return

    a = get_posix_assigner(ad, args)
    a.clear_group_gidNumbers()
    a.clear_user_uidNumbers()
    a.clear_user_gidNumbers()


@connect_ad
def cmd_group_assign(ad, args):
    a = get_posix_assigner(ad, args)
    a.assign_group_gidNumbers()


@connect_ad
def cmd_group_list(ad, args):
    common_list(ad.get_groups(), args.verbose)


@connect_ad
def cmd_user_assign(ad, args):
    a = get_posix_assigner(ad, args)
    a.assign_user_uidNumbers()
    a.update_user_gidNumbers()


@connect_ad
def cmd_user_checkexpire(ad, args):
    cfg = args.config
    if not cfg.pwexp:
        logger.info("Password expiry notification not configured")
        return
    check_pw_expiry(ad, cfg)


@connect_ad
def cmd_user_setupns(ad, args):
    def change_handler(message, data):
        args.changelog.write(message + '\n')

    a = UpnAssigner(
        ad = ad,
        onchange = change_handler,
    )

    logger.info("Settings UPNs")
    for container, cfg in args.config.upn_suffixes.items():
        a.set_user_upn_suffixes(container, cfg.suffix, cfg.scope)



def common_list(things, verbose):
    for x in things:
        if verbose:
            print(x)
        else:
            print(x.cn)

@connect_ad
def cmd_user_list(ad, args):
    common_list(ad.get_users(), args.verbose)


@connect_ad
def cmd_state_list(ad, args):
    s = get_state(ad)
    print(s)


@connect_ad
def cmd_state_init(ad, args):
    ds = DomainState.get(ad)

    logger.info("Got DomainState ({}): {}".format(ds.dn, ds))

    def set_next_xid(objs, thing, ldap_attr, ds_attr, valid_range):
        # Try to find the max value within the valid range
        gen = (getattr(x, ldap_attr, None) for x in objs)
        try:
            maxval = max(x for x in gen if x in valid_range)
        except ValueError:
            useval = valid_range.start
            logger.info("No {} {} found in range {}-{}; using default {}".format(
                thing, ldap_attr, valid_range.start, valid_range.stop, useval))
        else:
            # The "correct" value (ignoring deletion of top ID's) is max + 1
            useval = maxval + 1
            logger.info("Maximum {} {}: {}; using {}".format(
                thing, ldap_attr, maxval, useval))


        # See if the DomainState already has this attribute set, and compare
        curval = getattr(ds, ds_attr)
        if curval == useval:
            logger.info("Domain state {} already correctly set to {}".format(
                ds_attr, useval))
            return
        elif curval is not None:
            # They don't match
            if args.behavior is None:
                raise AppError("Domain state {} already set to {}, doesn't match expected {}\n"
                               "Use --force or --ignore".format(
                                   ds_attr, curval, useval))
            elif args.behavior == "force":
                # set it anyway
                pass
            elif args.behavior == "ignore":
                return

        logger.info("Setting Domain state {} to {}".format(ds_attr, useval))
        setattr(ds, ds_attr, useval)


    set_next_xid(ad.get_users(),  'user',  'uidNumber', 'next_uid', args.config.uid_range),
    set_next_xid(ad.get_groups(), 'group', 'gidNumber', 'next_gid', args.config.gid_range),

    ds.commit()
    print(ds)


def setup_logging(args):
    logging.basicConfig(level=args.loglevel)


def parse_args():
    # <top-level>
    ap = argparse.ArgumentParser()
    ap.add_argument('--version', action='version', version='adman ' + __version__)
    ap.add_argument('--loglevel', type=str.upper, default="warning",
            choices=("DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"),
            help="Log level")
    ap.add_argument('--changelog', type=argparse.FileType('a'), default=sys.stderr,
            help="File to which changes are logged")
    ap.add_argument('-c', '--config', default=default_confpath(),
            help="Path to config file")
    ap.add_argument('-v', '--verbose', action='store_true',
            help="Show verbose output")

    sub = ap.add_subparsers(dest='command_name', metavar='COMMAND')
    sub.required = True     # https://stackoverflow.com/a/18283730/119527


    def add_assign_opts(parser):
        parser.add_argument('--force', action='store_true',
                help="Forcefully replace out-of-range uidNumber/gidNumber attributes")

    # allmaint
    p = sub.add_parser('allmaint',
            help="Perform all automated maintenance (assign IDs, UPNs)")
    p.set_defaults(func=cmd_allmaint)
    add_assign_opts(p)

    # assignids
    p = sub.add_parser('assignids',
            help="Assign all missing uidNumber / gidNumber attributes")
    p.set_defaults(func=cmd_assignids)
    add_assign_opts(p)

    # clearids
    p = sub.add_parser('clearids',
            help="Clear all uidNumber / gidNumber attributes")
    p.set_defaults(func=cmd_clearids)
    p.add_argument('--force', action='store_true',
            help="Forcefully clear uidNumber/gidNumber attributes")

    ######
    # group
    p_group = sub.add_parser('group',
            help="Group sub-commands")
    sp_group = p_group.add_subparsers(metavar='SUBCOMMAND')
    sp_group.required = True

    # group assign
    p = sp_group.add_parser('assign',
            help="Assign missing gidNumber attributes")
    p.set_defaults(func=cmd_group_assign)
    add_assign_opts(p)

    # group list
    p = sp_group.add_parser('list',
            help="List groups")
    p.set_defaults(func=cmd_group_list)


    #######
    # state
    p_state = sub.add_parser('state',
            help="State sub-commands")
    sp_state = p_state.add_subparsers(metavar='SUBCOMMAND')
    sp_state.required = True

    # state list
    p = sp_state.add_parser('list',
            help="List state information")
    p.set_defaults(func=cmd_state_list)

    # state init
    p = sp_state.add_parser('init',
            help="Initialize state information")
    mx = p.add_mutually_exclusive_group()
    mx.add_argument('--force', dest='behavior', action='store_const', const='force',
            help="Force re-initialization; overwrite existing values with max(xidNumber)+1")
    mx.add_argument('--ignore', dest='behavior', action='store_const', const='ignore',
            help="Ignore partially-initialized state and initialize other values")
    p.set_defaults(func=cmd_state_init)


    ######
    # user
    p_user = sub.add_parser('user',
            help="User sub-commands")
    sp_user = p_user.add_subparsers(metavar='SUBCOMMAND')
    sp_user.required = True

    # user assign
    p = sp_user.add_parser('assign',
            help="Assign missing uidNumber attributes")
    p.set_defaults(func=cmd_user_assign)
    add_assign_opts(p)

    # user checkexpire
    p = sp_user.add_parser('checkexpire',
            help="Check for expiring/expired passwords")
    p.set_defaults(func=cmd_user_checkexpire)

    # user fixupn
    p = sp_user.add_parser('setupns',
            help="Set userPrincipalName attributes")
    p.set_defaults(func=cmd_user_setupns)

    # user list
    p = sp_user.add_parser('list',
            help="List users")
    p.set_defaults(func=cmd_user_list)


    return ap.parse_args()


def run_app(args):
    try:
        args.func(args)
    except AssignmentError as e:
        raise AppError(e)
    except KerberosError as e:
        raise AppError(e)


def main():
    args = parse_args()

    setup_logging(args)

    # Load config
    try:
        args.config = Config.load(args.config)
    except ConfigError as e:
        print("Config file error:", e, file=sys.stderr)
        sys.exit(1)

    # Run command
    try:
        run_app(args)
    except AppError as e:
        # TODO: Just raise or show backtrace if --debug is given
        print("Error:", e, file=sys.stderr)
        sys.exit(1)
