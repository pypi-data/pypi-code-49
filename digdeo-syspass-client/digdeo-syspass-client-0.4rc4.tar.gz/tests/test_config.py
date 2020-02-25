import unittest
import tempfile
import os

from syspassclient import Config

from yaml import load, dump

try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper


class TestConfig(unittest.TestCase):
    def test_property_data(self):
        config_obj = Config()
        self.assertIsNotNone(config_obj.data)
        self.assertTrue("account/search" in config_obj.data)
        self.assertTrue("account/viewPass" in config_obj.data)

        dict_to_test = {"account/search": {}, "account/viewPass": {}}

        self.assertNotEqual(dict_to_test, config_obj.data)
        config_obj.data = dict_to_test
        self.assertEqual(dict_to_test, config_obj.data)

    def test_property_api_version(self):
        config_obj = Config()
        self.assertTrue(isinstance(config_obj.api_version, str))
        self.assertTrue(3.0 <= float(config_obj.api_version))

        self.assertIsNotNone(config_obj.api_version)
        self.assertTrue(isinstance(config_obj.api_version, str))

        config_obj.api_version = "3.1"
        self.assertEqual(config_obj.api_version, "3.1")

        config_obj.api_version = "3.0"
        self.assertEqual(config_obj.api_version, "3.0")

        config_obj.api_version = None
        self.assertEqual(config_obj.api_version, "3.1")

    def test_property_api_extension(self):
        config_obj = Config()
        self.assertEqual(config_obj.api_filename_ext, ".yaml")

        config_obj.api_filename_ext = ".42"
        self.assertIsNotNone(config_obj.api_filename_ext)
        self.assertEqual(config_obj.api_filename_ext, ".42")

        config_obj.api_filename_ext = None
        self.assertEqual(config_obj.api_filename_ext, ".yaml")

    def test_property_api_filename_extension(self):
        config_obj = Config()
        self.assertTrue(isinstance(config_obj.api_filename_ext, str))
        self.assertEqual(".yaml", config_obj.api_filename_ext)

        config_obj.api_filename_ext = ".42"
        self.assertEqual(".42", config_obj.api_filename_ext)

        config_obj.api_filename_ext = None
        self.assertEqual(".yaml", config_obj.api_filename_ext)

        self.assertRaises(TypeError, setattr, config_obj, "api_filename_ext", 42)

    def test_config_api_directory(self):
        config_obj = Config()
        self.assertTrue(os.path.exists(config_obj.api_directory))
        config_obj.api_directory = "Hello"
        self.assertEqual(config_obj.api_directory, "Hello")
        config_obj.api_directory = None
        self.assertTrue(os.path.exists(config_obj.api_directory))
        self.assertRaises(TypeError, setattr, config_obj, "api_directory", 42)

    def test_config_api_filename(self):
        config_obj = Config()
        self.assertTrue(isinstance(config_obj.api_filename, str))
        self.assertTrue(config_obj.api_filename, config_obj.api_version + config_obj.api_filename_ext)

    def test_config_api_file(self):
        config_obj = Config()
        self.assertTrue(isinstance(config_obj.api_file, str))
        self.assertTrue(config_obj.api_file, os.path.join(config_obj.api_directory, config_obj.api_filename))

    def test_write(self):
        config_obj = Config()
        config_obj.verbose = True
        config_obj.verbose_level = 3
        config_obj.debug = True
        config_obj.debug_level = 3

        config_obj.reset()
        config_obj.write()

        config_obj.api_version = "3.0"
        config_obj.reset()
        config_obj.write()

        config_obj.api_version = "3.1"
        config_obj.reset()
        config_obj.write()

        config_obj.api_version = None
        config_obj.reset()
        config_obj.write()

        temp = tempfile.NamedTemporaryFile()

        config_obj.api_version = "3.1"
        config_obj.reset()
        config_obj.write(api_file=temp.name)
        self.assertTrue(os.path.isfile(temp.name))
        with open(temp.name) as f:
            data = load(f, Loader=Loader)
            f.close()
        self.assertEqual(config_obj.data, data)

        temp.close()

        temp = tempfile.NamedTemporaryFile()
        config_obj.api_version = "3.0"
        config_obj.reset()
        config_obj.write(api_file=temp.name)
        self.assertTrue(os.path.isfile(temp.name))
        with open(temp.name) as f:
            data = load(f, Loader=Loader)
            f.close()
        self.assertEqual(config_obj.data, data)

        temp.close()

    def test_read(self):
        config_obj = Config()

        temp = tempfile.NamedTemporaryFile()
        config_obj.reset()
        data = config_obj.data
        with open(temp.name, "w") as f:
            dump(data, f)
            f.close()

        config_obj.read(
            api_file=temp.name,
            debug=True,
            debug_level=3,
            verbose=True,
            verbose_level=3
        )
        self.assertEqual(config_obj.data, data)
        temp.close()

        config_obj.api_version = None
        config_obj.reset()
        config_obj.write()
        config_obj.verbose = True
        config_obj.verbose_level = 3
        config_obj.read()

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
