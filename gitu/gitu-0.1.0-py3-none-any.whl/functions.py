import subprocess
import sys

from gitu import git_config
from gitu.config_manager import ConfigManager

config = ConfigManager()

USER_NOT_FOUND = 1
USER_EXISTS = 2
GIT_ERROR = 3


def panic(msg: str, code: int):
    print(msg, file=sys.stderr)
    sys.exit(code)


def check_git():
    try:
        ver = git_config.version()
        return ver
    except subprocess.CalledProcessError as ex:
        if ex.stderr is not None:
            print('git: ' + ex.stderr.rstrip('\n'), file=sys.stderr)
        panic('Please make sure that your git has been installed and configured correctly.', GIT_ERROR)


def get_user(name_or_alias) -> dict:
    user = config.get_user(name_or_alias)
    if user is None:
        panic('User %s not found.' % name_or_alias, USER_NOT_FOUND)
    return user


def get_cur_user(file: str = 'local') -> (str, str):
    check_git()
    try:
        user = git_config.get('user.name', file)
        email = git_config.get('user.email', file)
        return user, email
    except subprocess.CalledProcessError as ex:
        if ex.stderr is not None:
            print('git: ' + ex.stderr.rstrip('\n'), file=sys.stderr)
        panic('To get global user, use -g/--global.', GIT_ERROR)


def check_name_conflict(name_or_alias: str, replace: bool):
    user = config.get_user(name_or_alias)
    if user is not None:
        if replace:
            config.remove_user(user['user.name'])
        else:
            panic('User %s already exists.' % name_or_alias, USER_EXISTS)


def login(args):
    check_git()
    user = get_user(args.name)
    try:
        for k, v in user.items():
            git_config.replace_all(k, str(v), args.git_conf_file)
        print('You are now logged in as %s <%s>.' % (user['user.name'], user['user.email']))
    except subprocess.CalledProcessError as ex:
        if ex.stderr is not None:
            print('git: ' + ex.stderr.rstrip('\n'), file=sys.stderr)
        panic('To login as a global user, use -g/--global.', GIT_ERROR)


def register(args):
    check_name_conflict(args.name, args.replace)
    user = {
        'user.name': args.name,
        'user.email': args.email,
        'commit.gpgsign': args.gpgsign
    }
    config.add_user(user)
    if args.alias is not None:
        check_name_conflict(args.alias, args.replace)
        config.append_alias(user['user.name'], args.alias)
    print('%s <%s> registered.' % (args.name, args.email))


def view(args):
    if args.list:
        print('Registered users:')
        aliases = {}
        if args.all:
            aliases = config.get_aliases_of_users()
        users = config.get_users()
        for i, user in enumerate(users):
            name = user['user.name']
            print('%s <%s>' % (name, user['user.email']))
            if not args.all:
                continue
            alias = aliases.get(name, [])
            if len(alias) > 0:
                print('%s: %s' % ('Alias' if len(alias) == 1 else 'Aliases', ', '.join(alias)))
            print('GPG Sign: %s' % user.get('commit.gpgsign', False))
            if i != len(users) - 1:
                print()
        if len(users) == 0:
            print('(none)')
    else:
        print('You are now logged in as %s <%s>.' % get_cur_user(args.git_conf_file))


def remove(args):
    user = get_user(args.name)
    config.remove_user(user['user.name'])


def edit(args):
    user = get_user(args.name)
    if args.email is not None:
        user['user.email'] = args.email
        config.update_user(user['user.name'], user)
    if args.new_name is not None:
        check_name_conflict(args.new_name, args.replace)
        config.update_user_name(user['user.name'], args.new_name)
    if args.alias is not None:
        check_name_conflict(args.alias, args.replace)
        config.append_alias(user['user.name'], args.alias)
    if args.remove_alias is not None:
        config.remove_alias(args.remove_alias)
    user['commit.gpgsign'] = args.gpgsign
    config.update_user(user['user.name'], user)
