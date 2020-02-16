"""
Pykrete calls tests
Author: Shai Bennathan - shai.bennathan@gmail.com
(C) 2020
"""
import unittest

from src.pykrete.calls import CheckedCall


class PykreteCallsUnitTests(unittest.TestCase):
    """Test pykrete's call module"""
    def test_checked_command_success(self):
        """Verifies successful call and correct passing of normal and quoted parameters
        with different quote types
        """
        for is_vector in [False, True]:
            target = self._make_checked_call_to_listargs_cmd_with(
                ['1', 'two', 'three and some', 'four',
                 'middle',
                 'four', 'three and some', 'two', '1',
                 '1 two "three and some" \'four\' middle four \'three and some\' \'two\' "1"'
                 ],
                is_vector)
            print(str(target))
            self.__assert_true(target.success, 'command failed', is_vector)
            self.__assert_true('PASSED' in target.stdout, 'stdout did not contain PASSED',
                               is_vector)

    def test_checked_command_failure(self):
        """Verifies failing call and correct passing of arguments with mixed quotes
        """
        args = ['start "middle" end', '2',
                '3', '4', '5', '6', '7', '8', 'start \'middle\' end',
                '\'start "middle" end\' 2 3 4 5 6 7 8 "start \'middle\' end"']
        for is_vector in [False, True]:
            target = self._make_checked_call_to_listargs_cmd_with(args, is_vector)
            print(str(target))
            self.__assert_true(not target.success, 'command succeeded', is_vector)
            self.__assert_true('FAILED' in target.stderr, 'stderr did not contain FAILED',
                               is_vector)

    @staticmethod
    def _make_checked_call_to_listargs_cmd_with(params, is_vector):
        listargs = r'src\pykrete\tests\src\listargs.cmd'
        if is_vector:
            cmd = [listargs]
            cmd.extend(params[:-1])
        else:
            cmd = f'{listargs} {params[9]}'
        return CheckedCall(cmd)

    def __assert_true(self, expr, message, is_vector):
        self.assertTrue(expr, f'{message} [{"vector" if is_vector else "string"} call]')


if __name__ == '__main__':
    unittest.main()
