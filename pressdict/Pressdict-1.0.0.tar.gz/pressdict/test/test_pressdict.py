import unittest

from pressdict import Pressdict


class PressdictTests(unittest.TestCase):

    def test_basic_functionality(self):
        pd = Pressdict()
        pd["test"] = {"key": "value", "key2": 2}

        self.assertTrue("test" in pd)

        self.assertEqual(pd["test"], {"key": "value", "key2": 2})

        for key in pd:
            self.assertEqual(key, "test")

        self.assertEqual(len(pd), 1)

        self.assertEqual(pd.get("test"), {"key": "value", "key2": 2})
        self.assertEqual(pd.get("asdf"), None)
        default = object()
        self.assertEqual(pd.get("asdf", default=default), default)

        self.assertEqual(list(pd.items()), [("test", {"key": "value",
                                                      "key2": 2})])
        self.assertEqual(list(pd.keys()), ["test"])
        self.assertEqual(list(pd.values()), [{"key": "value", "key2": 2}])

        del pd["test"]
        self.assertTrue("test" not in pd)

        pd["test"] = {"key": "value", "key2": 2}
        self.assertRaises(KeyError, pd.pop, "asdf")
        self.assertEqual(pd.pop("test"), {"key": "value", "key2": 2})

        pd["test"] = {"key": "value", "key2": 2}
        default = object()
        self.assertEqual(pd.pop("asdf", default), default)
        self.assertEqual(pd.pop("test", default), {"key": "value", "key2": 2})

        pd["test"] = {"key": "value", "key2": 2}
        pd.clear()
        self.assertEqual(len(pd), 0)
