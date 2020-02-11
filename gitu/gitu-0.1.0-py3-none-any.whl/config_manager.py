import json
import os

CONF_ENV = 'GITU_CONF'
CONF_FILE = 'config.json'
LINUX_CONF_LOC = '/etc/gitu'
NT_CONF_LOC = os.path.join(os.path.expanduser("~"), 'gitu')

DEFAULT_CONFIG = {
    'users': {
    },
    'aliases': {
    }
}


def get_conf_file() -> str:
    for conf_loc in (os.environ.get(CONF_ENV), os.curdir, NT_CONF_LOC, LINUX_CONF_LOC):
        if conf_loc is None:
            continue
        conf_file = os.path.join(conf_loc, CONF_FILE)
        if os.path.exists(conf_file):
            return conf_file
    return None


def get_default_conf_loc() -> str:
    loc_map = {
        'posix': LINUX_CONF_LOC,
        'nt': NT_CONF_LOC
    }
    return loc_map.get(os.name, os.curdir)


class ConfigManager:
    def __init__(self):
        self.conf_file = get_conf_file()
        if self.conf_file is None:
            self.conf_file = os.path.join(get_default_conf_loc(), CONF_FILE)
            self.config = {}
        else:
            self.config = self._read_conf_file()
        for k, v in DEFAULT_CONFIG.items():
            self.config.setdefault(k, v)

    def _read_conf_file(self) -> dict:
        if self.conf_file is None:
            return None
        with open(self.conf_file, 'r') as f:
            return json.load(f, encoding='utf-8')

    def save(self) -> None:
        os.makedirs(os.path.dirname(self.conf_file), exist_ok=True)
        with open(self.conf_file, 'w')as f:
            json.dump(self.config, f, indent=2)

    def get(self, name: str, default=None):
        return self.config.get(name, default)

    def get_user(self, name_or_alias: str) -> dict:
        user = self.get('users').get(name_or_alias)
        if user is None:
            name_or_alias = self.get('aliases').get(name_or_alias)
            return self.get('users').get(name_or_alias)
        else:
            return user

    def add_user(self, user: dict):
        self.get('users')[user['user.name']] = user
        self.save()

    def get_users(self) -> list:
        return self.get('users').values()

    def remove_user(self, name):
        users = self.get('users')
        if name not in users:
            return
        users.pop(name)
        # Remove all aliases of the user
        aliases = self.get('aliases')
        new_aliases = {}
        for alias, orig in aliases.items():
            if name != orig:
                new_aliases[alias] = orig
        self.config['aliases'] = new_aliases
        self.save()

    def update_user(self, name, user):
        self.get('users')[name] = user
        self.save()

    def update_user_name(self, name, new_name):
        users = self.get('users')
        user = users[name]
        user['user.name'] = new_name
        users[new_name] = user
        users.pop(name)
        aliases = self.get('aliases')
        for alias, orig in aliases.items():
            if name == orig:
                aliases[alias] = new_name
        self.save()

    def append_alias(self, name, alias):
        self.get('aliases')[alias] = name
        self.save()

    def remove_alias(self, alias):
        aliases = self.get('aliases')
        if alias in aliases:
            aliases.pop(alias)
        self.save()

    def get_aliases_of_users(self):
        res = {}
        for alias, name in self.get('aliases').items():
            res.setdefault(name, [])
            res[name].append(alias)
        return res
