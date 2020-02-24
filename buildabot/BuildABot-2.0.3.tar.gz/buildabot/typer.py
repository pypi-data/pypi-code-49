import re
import json


class Typer:
    """
    Typer is a utility to check valid types and dictionaries. It is helpful when attempting to convert user inputted
    strings to the types you want.

    Valid types:

    - int
    - float
    - number
    - bool
    - str
    - user
    - member
    - channel
    - role
    - mention
    - guild
    """
    types = {}
    serializable = {}

    @staticmethod
    def define_type(name: str, check, serializable=False):
        """
        Define a type
        :param name: Name of the type
        :param check: Check to convert to this type
        """
        Typer.types.setdefault(name.lower(), check)
        Typer.serializable.setdefault(name.lower(), serializable)

    @staticmethod
    def is_valid_type(expected_type):
        """
        Check if a type is defined
        :param expected_type: The expected type
        :return: boolean
        """
        if isinstance(expected_type, str):
            expected_type = expected_type.lower()
            is_list = expected_type.endswith('[]')
            if is_list:
                expected_type = expected_type[:-2]
            if expected_type not in Typer.types:
                return False
            return True
        elif isinstance(expected_type, type):
            return True
        return False

    @staticmethod
    def check_arg(arg, expected_type, context=None):
        """
        Check if an argument is a type
        :param arg: Argument to check
        :param expected_type: Type to check against, must be already defined
        :param context: Context is required for some types, can either be the bot object or object with the "bot" attrib
        :return: boolean
        """
        if isinstance(expected_type, str):
            expected_type = expected_type.lower()

            is_list = expected_type.endswith('[]')
            if is_list:
                expected_type = expected_type[:-2]

            if expected_type not in Typer.types:
                raise ValueError('Type "{}" not found'.format(expected_type))

            check = Typer.types[expected_type]

            bot = None

            from .bot import Bot
            if context is not None:
                if hasattr(context, 'workshop'):
                    bot = context.workshop
                elif hasattr(context, 'bot'):
                    bot = context.bot
                elif isinstance(context, Bot):
                    bot = context

            rtn = []

            if is_list:
                if not isinstance(arg, list):
                    raise TypeError('Argument is not a list'.format(expected_type))
                for i in range(len(arg)):
                    v = check(arg[i], context, bot=bot)

                    if not v:
                        raise TypeError('Argument[{}] is not type "{}"'.format(i, expected_type))

                    if not isinstance(v, list):
                        raise ValueError('Invalid return for "{}" type check'.format(expected_type))

                    rtn.append(v[0])
                return rtn

            rtn = check(arg, context, bot=bot)

            if not rtn:
                raise TypeError('Argument is not type "{}"'.format(expected_type))

            if not isinstance(rtn, list):
                raise ValueError('Invalid return for "{}" type check'.format(expected_type))

            return rtn[0]
        elif isinstance(expected_type, type):
            rtn = isinstance(arg, expected_type)

            if not rtn:
                raise TypeError('Argument is not type "{}"'.format(expected_type))

            return arg

    @staticmethod
    def verify_dict(template: dict, arg: dict, place="~", context=None):
        """
        Check a dict against a template. * = required, [] = list
        :param template: The template
        :param arg: Argument to check
        :param place: Ignore
        :param context: Context is required for some types, can either be the bot object or object with the "bot" attrib
        :return:
        """
        for key in template:
            type: str = template[key]
            required = False

            if key.endswith('*'):
                required = True
                key = key[:len(key) - 1]
            if isinstance(type, str):
                if type.endswith('*'):
                    required = True
                    type = type[:len(type) - 1]

            if key not in arg:
                if required:
                    raise ValueError('Key "{}" not found in "{}" and is required'.format(key, place))
                continue

            if isinstance(arg[key], dict):
                Typer.verify_dict(template[key], arg[key], place='{}/{}'.format(place, key), context=context)
                continue

            try:
                check = Typer.check_arg(arg[key], type, context=context)
            except TypeError:
                raise TypeError('Argument "{}/{}" is not type "{}"'.format(place, key, type))
        return True


# Regular stuff
def check_int(arg, context, bot=None):
    try:
        return [int(arg)]
    except ValueError:
        return False


def check_float(arg, context, bot=None):
    try:
        return [float(arg)]
    except ValueError:
        return False


def check_number(arg, context, bot=None):
    try:
        num = float(arg)
    except ValueError:
        return False
    if num % int(num) != 0:
        return [num]
    return [int(num)]


def check_bool(arg, context, bot=None):
    arg = str(arg).lower()
    yes = ['y', 'yes', 'true']
    no = ['n', 'no', 'false']

    if arg in yes:
        return [True]
    if arg in no:
        return [False]
    return False


def check_str(arg, context, bot=None):
    return [arg]


# Discord stuff
def check_user(arg, context, bot=None):
    arg = str(arg)
    if not 17 <= len(arg) <= 22:
        return False
    match = re.match(r"^(<(@|@!))?([0-9]{17,18})(>)?$", arg)
    if not match:
        return False
    id = int(match.group(3))
    return [bot.client.get_user(id)]


def check_member(arg, context, bot=None):
    arg = str(arg)
    if not 17 <= len(arg) <= 22:
        return False
    match = re.match(r"^(<(@!|@))?([0-9]{17,18})(>)?$", arg)
    if not match:
        return False
    id = int(match.group(3))
    if not hasattr(context, 'guild'):
        return [None]
    return [context.guild.get_member(id)]


def check_channel(arg, context, bot=None):
    arg = str(arg)
    if not 17 <= len(arg) <= 22:
        return False
    match = re.match(r"^(<#)?([0-9]{17,18})(>)?$", arg)
    if not match:
        return False
    id = int(match.group(2))
    return [bot.client.get_channel(id)]


def check_role(arg, context, bot=None):
    arg = str(arg)
    if not 17 <= len(arg) <= 22:
        return False
    match = re.match(r"^(<@&)?([0-9]{17,18})(>)?$", arg)
    if not match:
        return False
    id = int(match.group(2))
    for role in context.guild.roles:
        if role.id == id:
            return [role]
    return [None]


def check_mention(arg, context, bot=None):
    arg = str(arg)
    if not 17 <= len(arg) <= 22:
        return False
    match = re.match(r"^(<(@!|#|@&|@))?([0-9]{17,18})(>)?$", arg)
    if not match:
        return False
    id = int(match.group(3))

    member = context.guild.get_member(id)
    channel = context.guild.get_channel(id)
    role = None
    for r in context.guild.roles:
        if r.id == id:
            role = r

    return [member or channel or role]


def check_guild(arg, context, bot=None):
    arg = str(arg)
    if not 17 <= len(arg) <= 22:
        return False
    match = re.match(r"^([0-9]{17,18})$", arg)
    if not match:
        return False
    id = int(match.group(1))
    return [bot.client.get_guild(id)]

# Other stuff
def check_json(arg, context, bot=None):
    arg = str(arg)
    try:
        data = json.loads(arg)
        return data
    except:
        return False


Typer.define_type('int', check_int, serializable=True)
Typer.define_type('float', check_float, serializable=True)
Typer.define_type('number', check_number, serializable=True)
Typer.define_type('bool', check_bool, serializable=True)
Typer.define_type('str', check_str, serializable=True)

Typer.define_type('user', check_user)
Typer.define_type('member', check_member)
Typer.define_type('channel', check_channel)
Typer.define_type('role', check_role)
Typer.define_type('mention', check_mention)
Typer.define_type('guild', check_guild)

Typer.define_type('json', check_json, serializable=True)
