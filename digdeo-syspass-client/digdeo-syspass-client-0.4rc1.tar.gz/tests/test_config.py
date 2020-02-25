import unittest
import os
import tempfile
import os

from syspassclient.config import Config

from yaml import load, dump

try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper


class TestConfig(unittest.TestCase):
    def test_property_data(self):
        config = Config()
        self.assertIsNotNone(config.data)
        self.assertTrue("account/search" in config.data)
        self.assertTrue("account/viewPass" in config.data)

        dict_to_test = {"account/search": {}, "account/viewPass": {}}

        self.assertNotEqual(dict_to_test, config.data)
        config.data = dict_to_test
        self.assertEqual(dict_to_test, config.data)

    def test_property_api_version(self):
        config = Config()
        self.assertTrue(isinstance(config.api_version, str))
        self.assertTrue(3.0 <= float(config.api_version))

        self.assertIsNotNone(config.api_version)
        self.assertTrue(isinstance(config.api_version, str))

        config.api_version = "3.1"
        self.assertEqual(config.api_version, "3.1")

        config.api_version = "3.0"
        self.assertEqual(config.api_version, "3.0")

        config.api_version = None
        self.assertEqual(config.api_version, "3.1")

    def test_property_api_extension(self):
        config = Config()
        self.assertEqual(config.api_filename_ext, ".yaml")

        config.api_filename_ext = ".42"
        self.assertIsNotNone(config.api_filename_ext)
        self.assertEqual(config.api_filename_ext, ".42")

        config.api_filename_ext = None
        self.assertEqual(config.api_filename_ext, ".yaml")

    def test_property_api_filename_extension(self):
        config = Config()
        self.assertTrue(isinstance(config.api_filename_ext, str))
        self.assertEqual(".yaml", config.api_filename_ext)

        config.api_filename_ext = ".42"
        self.assertEqual(".42", config.api_filename_ext)

        config.api_filename_ext = None
        self.assertEqual(".yaml", config.api_filename_ext)

        self.assertRaises(TypeError, setattr, config, "api_filename_ext", 42)

    def test_config_api_directory(self):
        config = Config()
        self.assertTrue(os.path.exists(config.api_directory))
        config.api_directory = "Hello"
        self.assertEqual(config.api_directory, "Hello")
        config.api_directory = None
        self.assertTrue(os.path.exists(config.api_directory))
        self.assertRaises(TypeError, setattr, config, "api_directory", 42)

    def test_config_api_filename(self):
        config = Config()
        self.assertTrue(isinstance(config.api_filename, str))
        self.assertTrue(config.api_filename, config.api_version + config.api_filename_ext)

    def test_config_api_file(self):
        config = Config()
        self.assertTrue(isinstance(config.api_file, str))
        self.assertTrue(config.api_file, os.path.join(config.api_directory, config.api_filename))

    def test_write(self):
        config = Config()
        config.verbose = True
        config.verbose_level = 3
        config.debug = True
        config.debug_level = 3

        config.reset()
        config.write()

        config.api_version = "3.0"
        config.reset()
        config.write()

        config.api_version = "3.1"
        config.reset()
        config.write()

        config.api_version = None
        config.reset()
        config.write()

        temp = tempfile.NamedTemporaryFile()

        config.api_version = "3.1"
        config.reset()
        config.write(api_file=temp.name)
        self.assertTrue(os.path.isfile(temp.name))
        with open(temp.name) as f:
            data = load(f, Loader=Loader)
            f.close()
        self.assertEqual(config.data, data)

        temp.close()

        temp = tempfile.NamedTemporaryFile()
        config.api_version = "3.0"
        config.reset()
        config.write(api_file=temp.name)
        self.assertTrue(os.path.isfile(temp.name))
        with open(temp.name) as f:
            data = load(f, Loader=Loader)
            f.close()
        self.assertEqual(config.data, data)

        temp.close()

    def test_read(self):
        config = Config()

        temp = tempfile.NamedTemporaryFile()
        config.reset()
        data = config.data
        with open(temp.name, "w") as f:
            dump(data, f)
            f.close()

        config.read(
            api_file=temp.name,
            debug=True,
            debug_level=3,
            verbose=True,
            verbose_level=3
        )
        self.assertEqual(config.data, data)
        temp.close()

        config.api_version = None
        config.reset()
        config.write()
        config.verbose = True
        config.verbose_level = 3
        config.read()

    def test_singleton(self):
        conf1 = Config()
        conf2 = Config()
        self.assertEqual(conf1, conf2)

    def test_get_empty_config_dict(self):
        conf = Config()
        what_i_need = {
            'syspassclient': {
                'api_url': None,
                'api_version': '3.1',
                'authToken': None,
                'tokenPass': None,
                'debug': True,
                'debug_level': 3,
                'verbose': False,
                'verbose_level': 0
            }
        }
        self.assertEqual(what_i_need, conf.get_empty_config_dict())

    def test_config_directory(self):
        conf = Config()
        if 'DD_SYSPASS_CLIENT_CONFIG_DIR' in os.environ:
            self.assertEqual(os.environ['DD_SYSPASS_CLIENT_CONFIG_DIR'], conf.config_directory)
        else:

            default_path = os.path.abspath(
                os.path.join(
                    os.path.join(
                        os.environ['HOME'],
                        '.config'),
                    'digdeo-syspass-client'
                )
            )
            self.assertEqual(default_path, conf.config_directory)
            os.environ['DD_SYSPASS_CLIENT_CONFIG_DIR'] = '/tmp'
            self.assertEqual('/tmp', conf.config_directory)
            del os.environ['DD_SYSPASS_CLIENT_CONFIG_DIR']

    def test_get_config_file(self):
        conf = Config()
        wanted_value = os.path.join(conf.config_directory, 'config.yml')
        self.assertEqual(wanted_value, conf.get_config_file())

    def test_get_empty_config_dict(self):
        conf = Config()
        self.assertEqual(
            {
                'syspassclient': {
                    'api_url': None,
                    'api_version': '3.1',
                    'authToken': None,
                    'tokenPass': None,
                    'debug': True,
                    'debug_level': 3,
                    'verbose': False,
                    'verbose_level': 0
                }
            },
            conf.get_empty_config_dict()
        )

    def test_config_file(self):
        conf = Config()
        conf.config_file = 'Lulu'
        self.assertEqual('Lulu', conf.config_file)


if __name__ == "__main__":
    unittest.main()
