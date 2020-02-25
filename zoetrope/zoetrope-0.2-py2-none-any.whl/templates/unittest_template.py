def headers(module):
    return 'import unittest\n' + 'import mock\n' + \
    "\n".join(("import {0}".format(x.__name__) for x in module.dependencies)) + "\n"

def function_test(function, indentation=0):
    return """
    def test_{0}(self):
        pass
    """.format(function.__name__)

def class_test(_class, indentation=0):
    return """class Test{0}(unittest.TestCase):
    """.format(_class[0].upper() + _class[1:])

def main():
    return """if __name__=="__main__":
    unittest.main()
    """.strip('\t')
