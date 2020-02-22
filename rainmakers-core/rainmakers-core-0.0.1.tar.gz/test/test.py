import unittest
from core.function import version
from core.gitCommands import GitCommand as gc


class Test(unittest.TestCase):
    def testVersion(self):
        ver = version()
        self.assertTrue(ver == '0.0.1')

    def testExecuteCommand(self):
        cmd = gc.executeCommand(self, 'git -C "D:/Rainmakers/chess" log')
        print(cmd)

    if __name__ == '__main__':
        unittest.main()
