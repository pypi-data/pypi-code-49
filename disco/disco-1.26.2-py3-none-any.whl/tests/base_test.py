import json
import os
import random
import string
import sys
from contextlib import contextmanager
from pathlib import Path
from tempfile import TemporaryDirectory

from disco.core import Credentials, constants
import mock

random_str = string.ascii_lowercase + string.ascii_uppercase + string.digits


class RandomDataMixin:
    @classmethod
    def random_str(cls, prefix='', length=10):
        return prefix + ''.join(random.choice(random_str) for _ in range(length))

    @classmethod
    def random_int63(cls):
        return random.getrandbits(63)

    @classmethod
    def random_int32(cls):
        return random.getrandbits(32)

    @classmethod
    def random_int16(cls):
        return random.getrandbits(16)

    @classmethod
    def random_int(cls, minimum=0, maximum=sys.maxsize):
        return random.randint(minimum, maximum)

    random_from = random.choice
    random_bytes = os.urandom

    @classmethod
    def random_dict(cls, length=10, key_prefix='', value_prefix=''):
        return {cls.random_str(key_prefix): cls.random_str(value_prefix) for _ in range(length)}

    @classmethod
    def random_list(cls, prefix='', length=10):
        return [cls.random_str(prefix) for _ in range(length)]

    @classmethod
    def random_bool(cls):
        return cls.random_from([True, False])

    @classmethod
    def random_email(cls, prefix='', length=10):
        return f"{cls.random_str(prefix, length)}@{cls.random_str(prefix, length)}.{cls.random_str(prefix, 3)}"

    @classmethod
    def random_url(cls, prefix='', length=10, relative=False):
        if relative:
            return cls.random_str(prefix, length)

        return f"https://{cls.random_str(prefix, length)}.{cls.random_str(prefix, length)}.{cls.random_str(prefix, 3)}"


class AssertionsMixin:
    @classmethod
    def assert_not_called(cls, name):
        def _f(*args, **kwargs):
            raise AssertionError(f"fn: {name} was not supposed to be called, but was invoked with {args}, {kwargs}")

        return _f

    @classmethod
    def any_instance_of(cls, target_type):
        class Any(cls):
            def __eq__(self, other):
                return isinstance(other, target_type)

        return Any()

    @classmethod
    def any(cls):
        class Any(cls):
            def __eq__(self, other):
                return True

        return Any()

    @classmethod
    def is_function(cls):
        class Any(cls):
            def __eq__(self, other):
                return callable(other)

        return Any()


class BaseTest(RandomDataMixin, AssertionsMixin):

    @staticmethod
    def disable_progress_bar():
        os.environ[constants.ENV_VAR_DISABLE_PROGRESS_BAR] = "1"

    @classmethod
    @contextmanager
    def _mock_auth(cls, apply=False):
        if apply:
            with mock.patch('disco.gql.authentication.Authentication.refresh') as _refresh:
                yield
        else:
            yield

    @classmethod
    def _reset_auth(cls):
        Credentials.username = None
        Credentials.userid = None
        Credentials.token = None
        Credentials.credentials = (None, None)

    @classmethod
    @contextmanager
    def with_config_and_env(cls, config=None, env=None, authenticated=True):
        config = {} if config is None else config
        env = {} if env is None else env
        os_env = {k: v for k, v in os.environ.items() if not k.startswith('DISCO_')}
        os_env.update(env)
        cls._reset_auth()
        if authenticated:
            Credentials.username = cls.random_str('default_username')
            Credentials.userid = cls.random_str('default_userid')
            Credentials.token = cls.random_str('default_token')
            Credentials.credentials = (cls.random_str('default_cred_username'), cls.random_str('default_pass'))

        with TemporaryDirectory() as d:
            conf_path = Path(d) / f"{cls.random_str('config_')}.json"
            conf_path.write_text(json.dumps(config))
            with mock.patch('disco.core.constants.DISCO_CONFIG_PATH', conf_path):
                old_env = os.environ
                with cls._mock_auth(authenticated):
                    try:
                        os.environ = env

                        yield

                    finally:
                        os.environ = old_env
                        cls._reset_auth()
