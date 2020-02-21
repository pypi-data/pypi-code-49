import unittest
import os
import pickle

dir = "/home/jessica/GitHub/Checklist/checklist/"
pkg = "/home/jessica/miniconda3/envs/Profiles/lib/python3.7/site-packages/checklist/"
python = "/home/jessica/miniconda3/envs/Profiles/bin/python"


def run(pyfile, infile):
    os.system(python + " " + dir +
              pyfile + " < " + dir + infile)


def install(version):
    os.system("pip install /home/jessica/GitHub/Checklist/dist/oucass_"
              "checklist-" + version + "-py3-none-any.whl")


def load(pkl):
    return pickle.load(open(pkg + "user_settings/" + pkl, "rb"))

class MyTestCase(unittest.TestCase):

    def test_uninstall(self):
        os.system("pip uninstall -y oucass-checklist")
        install("0.2.0")
        # Add a test copter
        run("checklist.py", "update_test_1.txt")
        ndict = load("ndict.pkl")
        self.assertIn('N0000UA_Tester_One', ndict.keys())
        os.system("pip uninstall -y oucass-checklist")
        install("0.2.0")
        ndict = load("ndict.pkl")
        with self.assertRaises(KeyError):
            ndict["N0000UA_Tester_One"]

    def test_update(self):
        # Add a test copter
        run("checklist.py", "update_test_2.txt")
        # Update package
        install("0.2.1")
        ndict = load("ndict.pkl")
        known_locations = load("known_locations.pkl")
        objectives = load("objectives.pkl")
        self.assertIn("N0000UA_Tester_Two", ndict.keys())
        self.assertIn("Test State", known_locations)
        self.assertIn("Test Location", known_locations["Test State"])


if __name__ == '__main__':
    unittest.main()
