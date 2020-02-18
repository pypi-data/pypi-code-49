# -*- coding: UTF-8 -*-
import json
import re
import warnings
from datetime import datetime
from json.decoder import JSONDecodeError
from operator import itemgetter
from typing import List, Tuple, Mapping
import yaml

import pytest
# Reference: http://docs.gurock.com/testrail-api2/reference-statuses
from _pytest.python import Function
from yaml.scanner import ScannerError

TESTRAIL_TEST_STATUS = {
    "passed": 1,
    "blocked": 2,
    "untested": 3,
    "retest": 4,
    "failed": 5
}

PYTEST_TO_TESTRAIL_STATUS = {
    "passed": TESTRAIL_TEST_STATUS["passed"],
    "failed": TESTRAIL_TEST_STATUS["failed"],
    "skipped": TESTRAIL_TEST_STATUS["blocked"],
}

DT_FORMAT = '%d-%m-%Y %H:%M:%S'

TESTRAIL_PREFIX = 'testrail'
TESTRAIL_DEFECTS_PREFIX = 'testrail_defects'
ADD_RESULTS_URL = 'add_results_for_cases/{}'
ADD_TESTRUN_URL = 'add_run/{}'
CLOSE_TESTRUN_URL = 'close_run/{}'
CLOSE_TESTPLAN_URL = 'close_plan/{}'
GET_TESTRUN_URL = 'get_run/{}'
GET_TESTPLAN_URL = 'get_plan/{}'
GET_TESTS_URL = 'get_tests/{}'
GET_CASES_URL = 'get_cases/{}&section_id={}'
ADD_CASE_URL = 'add_case/{}'
ADD_SECTION = 'add_section/{}'
GET_ALL_SECTIONS = 'get_sections/{}'
CREATE_SECTION_URL = 'add_section/{}'
UPDATE_CASE = 'update_case/{}'
DELETE_CASE = 'delete_case/{}'
DELETE_SECTION_URL = 'delete_section/{}'

COMMENT_SIZE_LIMIT = 4000


class DeprecatedTestDecorator(DeprecationWarning):
    pass


warnings.simplefilter(action='once', category=DeprecatedTestDecorator, lineno=0)


class pytestrail(object):
    '''
    An alternative to using the testrail function as a decorator for test cases, since py.test may confuse it as a test
    function since it has the 'test' prefix
    '''

    @staticmethod
    def case(*ids):
        """
        Decorator to mark tests with testcase ids.

        ie. @pytestrail.case('C123', 'C12345')

        :return pytest.mark:
        """
        return pytest.mark.testrail(ids=ids)

    @staticmethod
    def defect(*defect_ids):
        """
                Decorator to mark defects with defect ids.

                ie. @pytestrail.defect('PF-513', 'BR-3255')

                :return pytest.mark:
                """
        return pytest.mark.testrail_defects(defect_ids=defect_ids)


def testrail(*ids):
    """
    Decorator to mark tests with testcase ids.

    ie. @testrail('C123', 'C12345')

    :return pytest.mark:
    """
    deprecation_msg = ('pytest_testrail: the @testrail decorator is deprecated and will be removed. Please use the '
                       '@pytestrail.case decorator instead.')
    warnings.warn(deprecation_msg, DeprecatedTestDecorator)
    return pytestrail.case(*ids)


def get_test_outcome(outcome):
    """
    Return numerical value of test outcome.

    :param str outcome: pytest reported test outcome value.
    :returns: int relating to test outcome.
    """
    return PYTEST_TO_TESTRAIL_STATUS[outcome]


def testrun_name():
    """Returns testrun name with timestamp"""
    now = datetime.utcnow()
    return 'Automated Run {}'.format(now.strftime(DT_FORMAT))


def clean_test_ids(test_ids):
    """
    Clean pytest marker containing testrail testcase ids.

    :param list test_ids: list of test_ids.
    :return list ints: contains list of test_ids as ints.
    """
    return [int(re.search('(?P<test_id>[0-9]+$)', test_id).groupdict().get('test_id')) for test_id in test_ids]


def clean_test_defects(defect_ids):
    """
        Clean pytest marker containing testrail defects ids.

        :param list defect_ids: list of defect_ids.
        :return list ints: contains list of defect_ids as ints.
        """
    return [(re.search('(?P<defect_id>.*)', defect_id).groupdict().get('defect_id')) for defect_id in defect_ids]


def get_testrail_keys(items):
    """Return Tuple of Pytest nodes and TestRail ids from pytests markers"""
    testcaseids = []
    for item in items:
        if item.get_closest_marker(TESTRAIL_PREFIX):
            testcaseids.append(
                (
                    item,
                    clean_test_ids(
                        item.get_closest_marker(TESTRAIL_PREFIX).kwargs.get('ids')
                    )
                )
            )
    return testcaseids


class PyTestRailPlugin(object):
    def __init__(self, client, assign_user_id, project_id, suite_id, include_all, cert_check, tr_name, root_section,
                 tr_description='', run_id=0,
                 plan_id=0, version='', close_on_complete=False, publish_blocked=True, skip_missing=False,
                 milestone_id=None, custom_comment=None, unsafe=False):
        self.assign_user_id = assign_user_id
        self.cert_check = cert_check
        self.client = client
        self.project_id = project_id
        self.results = []
        self.suite_id = suite_id
        self.include_all = include_all
        self.testrun_name = tr_name
        self.testrun_description = tr_description
        self.testrun_id = run_id
        self.testplan_id = plan_id
        self.version = version
        self.close_on_complete = close_on_complete
        self.publish_blocked = publish_blocked
        self.skip_missing = skip_missing
        self.milestone_id = milestone_id
        self.custom_comment = custom_comment
        self.cases = {}
        self.root_section = root_section
        self.sections = self.get_all_sections()
        self.unsafe = unsafe

    def get_all_sections(self):
        url = GET_ALL_SECTIONS.format(self.project_id)
        all_sections = self.client.send_get(url)
        root_section = self.get_or_create_root_section(all_sections)
        res = {'id': root_section['id'],
               'to_delete': False,
               'nested': self.make_nested(all_sections, root_id=root_section['id'])}
        return res

    def get_or_create_root_section(self, all_sections):
        for section in all_sections:
            if (section['name'] == self.root_section) and (section['parent_id'] is None):
                return section
        return self.create_section(self.root_section)

    def create_section(self, name, parent_id=None):
        url = CREATE_SECTION_URL.format(self.project_id)
        res = self.client.send_post(url, data={'parent_id': parent_id, 'name': name})
        return res

    def delete_section(self, section_id):
        try:
            self.client.send_post(DELETE_SECTION_URL.format(section_id), data=None)
        except JSONDecodeError:
            pass

    def make_nested(self, sections, root_id=None):
        res = {item['name']: item for item in sections if item['parent_id'] == root_id}
        for k, v in res.items():
            res[k]['to_delete'] = True
            res[k]['nested'] = self.make_nested(sections, res[k]['id'])
        return res

    # pytest hooks

    def pytest_report_header(self, config, startdir):
        """ Add extra-info in header """
        message = 'pytest-testrail: '
        if self.testplan_id:
            message += 'existing testplan #{} selected'.format(self.testplan_id)
        elif self.testrun_id:
            message += 'existing testrun #{} selected'.format(self.testrun_id)
        else:
            message += 'a new testrun will be created'
        return message

    def get_or_create_section(self, item):
        dirs = item.parent.nodeid[:-3].split('/')[1:]
        section = self.sections
        for dir in dirs:
            if section['nested'].get(dir) is None:
                new_section = self.create_section(parent_id=section['id'], name=dir)
                section['nested'][new_section['name']] = {**new_section, 'nested': {}}
            section = section['nested'][dir]
            section['to_delete'] = False
        return section['id']

    def get_section_cases(self, section_id):
        if self.cases.get(section_id) is not None:
            return self.cases[section_id]
        url = GET_CASES_URL.format(self.project_id, section_id)
        res = self.client.send_get(url)
        res = {item['title']: {**item, 'to_delete': True} for item in res}
        self.cases[section_id] = res
        return res

    def delete_test_case(self, case_id, **kwargs):
        try:
            self.client.send_post(DELETE_CASE.format(case_id), data=None)
        except JSONDecodeError:
            pass

    def update_test_case(self, case_id, custom_preconds=None, custom_steps=None, custom_expected=None, **kwargs):
        return self.client.send_post(
            UPDATE_CASE.format(case_id),
            data={
                'custom_preconds': custom_preconds,
                'custom_steps': custom_steps,
                'custom_expected': custom_expected,
            }
        )

    def create_test_case(self, title, section_id, custom_preconds=None, custom_steps=None, custom_expected=None,
                         **kwargs):
        url = ADD_CASE_URL.format(section_id)
        res = self.client.send_post(
            url,
            data={'title': title,
                  'custom_state': 3,
                  'section_id': section_id,
                  'custom_preconds': custom_preconds,
                  'custom_steps': custom_steps,
                  'custom_expected': custom_expected,
                  }
        )
        self.cases[section_id][res['title']] = res
        return res['id']

    @staticmethod
    def get_test_case_info(item):
        def yaml_parser(st: str):
            try:
                return yaml.load(st, Loader=yaml.BaseLoader)
            except ScannerError:
                pass

        def json_parser(st: str):
            try:
                return json.loads(st)
            except JSONDecodeError:
                pass

        docstring = item.obj.__doc__ or ''
        res = yaml_parser(docstring) or json_parser(docstring) or {}
        res['title'] = res.get('title') or item.name

        return res

    @staticmethod
    def check_eq_cases(test_case: Mapping, test_info: Mapping) -> bool:
        for key in ('title', 'custom_preconds', 'custom_steps', 'custom_expected'):
            if test_case.get(key) != test_info.get(key):
                return False
        return True

    def get_or_create_test_case_for_func(self, item: Function):
        section_id = self.get_or_create_section(item)
        cases = self.get_section_cases(section_id)
        test_info = self.get_test_case_info(item)

        test_case = cases.get(test_info['title'])

        if test_case is not None:
            if not self.check_eq_cases(test_case, test_info):
                self.update_test_case(test_case['id'], **test_info)
            test_case['to_delete'] = False
            return test_case['id']
        return self.create_test_case(**test_info, section_id=section_id)

    def get_or_create_test_cases(self, items: List[Tuple[Function, List[int]]]):
        for item in items:
            if not item[1]:
                item[1].append(self.get_or_create_test_case_for_func(item[0]))
        return items

    def delete_unused_test_cases(self):
        for section, cases in self.cases.items():
            for case_name, case_description in cases.items():
                if case_description.get('to_delete'):
                    self.delete_test_case(**case_description)

    def delete_unused_sections(self, section=None):
        if section is None:
            section = self.sections
        if section.get('to_delete'):
            return self.delete_section(section['id'])
        for section_name, section_description in section.get('nested').items():
            self.delete_unused_sections(section_description)

    @pytest.hookimpl(trylast=True)
    def pytest_collection_modifyitems(self, session, config, items):
        items_with_tr_keys = get_testrail_keys(items)
        items_with_tr_keys = self.get_or_create_test_cases(items_with_tr_keys)
        tr_keys = [case_id for item in items_with_tr_keys for case_id in item[1]]
        if self.testplan_id and self.is_testplan_available():
            self.testrun_id = 0
        elif self.testrun_id and self.is_testrun_available():
            self.testplan_id = 0
            if self.skip_missing:
                tests_list = [
                    test.get('case_id') for test in self.get_tests(self.testrun_id)
                ]
                for item, case_id in items_with_tr_keys:
                    if not set(case_id).intersection(set(tests_list)):
                        mark = pytest.mark.skip('Test is not present in testrun.')
                        item.add_marker(mark)
        else:
            if self.testrun_name is None:
                self.testrun_name = testrun_name()
            self.create_test_run(
                self.assign_user_id,
                self.project_id,
                self.suite_id,
                self.include_all,
                self.testrun_name,
                tr_keys,
                self.milestone_id,
                self.testrun_description
            )

    @pytest.hookimpl(tryfirst=True, hookwrapper=True)
    def pytest_runtest_makereport(self, item, call):
        """ Collect result and associated testcases (TestRail) of an execution """
        outcome = yield
        rep = outcome.get_result()
        defectids = None
        if item.get_closest_marker(TESTRAIL_DEFECTS_PREFIX):
            defectids = item.get_closest_marker(TESTRAIL_DEFECTS_PREFIX).kwargs.get('defect_ids')
        if item.get_closest_marker(TESTRAIL_PREFIX):
            testcaseids = item.get_closest_marker(TESTRAIL_PREFIX).kwargs.get('ids')
            if not testcaseids:  # new
                testcaseids = [str(self.get_or_create_test_case_for_func(item))]
            if rep.when == 'call' and testcaseids:
                if defectids != None:
                    self.add_result(
                        clean_test_ids(testcaseids),
                        get_test_outcome(outcome.get_result().outcome),
                        comment=rep.longrepr,
                        duration=rep.duration,
                        defects=str(clean_test_defects(defectids)).replace('[', '').replace(']', '').replace("'", '')
                    )
                else:
                    self.add_result(
                        clean_test_ids(testcaseids),
                        get_test_outcome(outcome.get_result().outcome),
                        comment=rep.longrepr,
                        duration=rep.duration
                    )

    def pytest_sessionfinish(self, session, exitstatus):
        """ Publish results in TestRail """
        print('[{}] Start publishing'.format(TESTRAIL_PREFIX))
        if self.unsafe:
            self.delete_unused_test_cases()
            self.delete_unused_sections()
        if self.results:
            tests_list = [str(result['case_id']) for result in self.results]
            print('[{}] Testcases to publish: {}'.format(TESTRAIL_PREFIX, ', '.join(tests_list)))

            if self.testrun_id:
                self.add_results(self.testrun_id)
            elif self.testplan_id:
                testruns = self.get_available_testruns(self.testplan_id)
                print('[{}] Testruns to update: {}'.format(TESTRAIL_PREFIX, ', '.join([str(elt) for elt in testruns])))
                for testrun_id in testruns:
                    self.add_results(testrun_id)
            else:
                print('[{}] No data published'.format(TESTRAIL_PREFIX))

            if self.close_on_complete and self.testrun_id:
                self.close_test_run(self.testrun_id)
            elif self.close_on_complete and self.testplan_id:
                self.close_test_plan(self.testplan_id)
        print('[{}] End publishing'.format(TESTRAIL_PREFIX))

    # plugin

    def add_result(self, test_ids, status, comment='', defects=None, duration=0):
        """
        Add a new result to results dict to be submitted at the end.

        :param defects: Add defects to test result
        :param list test_ids: list of test_ids.
        :param int status: status code of test (pass or fail).
        :param comment: None or a failure representation.
        :param duration: Time it took to run just the test.
        """
        for test_id in test_ids:
            data = {
                'case_id': test_id,
                'status_id': status,
                'comment': comment,
                'duration': duration,
                'defects': defects
            }
            self.results.append(data)

    def add_results(self, testrun_id):
        """
        Add results one by one to improve errors handling.

        :param testrun_id: Id of the testrun to feed

        """
        converter = lambda s, c: str(bytes(s, "utf-8"), c)
        # Results are sorted by 'case_id' and by 'status_id' (worst result at the end)

        # Comment sort by status_id due to issue with pytest-rerun failures, for details refer to issue https://github.com/allankp/pytest-testrail/issues/100
        # self.results.sort(key=itemgetter('status_id'))
        self.results.sort(key=itemgetter('case_id'))

        # Manage case of "blocked" testcases
        if self.publish_blocked is False:
            print('[{}] Option "Don\'t publish blocked testcases" activated'.format(TESTRAIL_PREFIX))
            blocked_tests_list = [
                test.get('case_id') for test in self.get_tests(testrun_id)
                if test.get('status_id') == TESTRAIL_TEST_STATUS["blocked"]
            ]
            print('[{}] Blocked testcases excluded: {}'.format(TESTRAIL_PREFIX,
                                                               ', '.join(str(elt) for elt in blocked_tests_list)))
            self.results = [result for result in self.results if result.get('case_id') not in blocked_tests_list]

        # prompt enabling include all test cases from test suite when creating test run
        if self.include_all:
            print('[{}] Option "Include all testcases from test suite for test run" activated'.format(TESTRAIL_PREFIX))

        # Publish results
        data = {'results': []}
        for result in self.results:
            entry = {'status_id': result['status_id'], 'case_id': result['case_id'], 'defects': result['defects']}
            if self.version:
                entry['version'] = self.version
            comment = result.get('comment', '')
            if comment:
                if self.custom_comment:
                    entry['comment'] = self.custom_comment + '\n'
                    # Indent text to avoid string formatting by TestRail. Limit size of comment.
                    entry['comment'] += u"# Pytest result: #\n"
                    entry['comment'] += u'Log truncated\n...\n' if len(str(comment)) > COMMENT_SIZE_LIMIT else u''
                    entry['comment'] += u"    " + converter(str(comment), "utf-8")[-COMMENT_SIZE_LIMIT:].replace('\n',
                                                                                                                 '\n    ')
                else:
                    # Indent text to avoid string formatting by TestRail. Limit size of comment.
                    entry['comment'] = u"# Pytest result: #\n"
                    entry['comment'] += u'Log truncated\n...\n' if len(str(comment)) > COMMENT_SIZE_LIMIT else u''
                    entry['comment'] += u"    " + converter(str(comment), "utf-8")[-COMMENT_SIZE_LIMIT:].replace('\n',
                                                                                                                 '\n    ')
            elif comment == '':
                entry['comment'] = self.custom_comment
            duration = result.get('duration')
            if duration:
                duration = 1 if (duration < 1) else int(round(duration))  # TestRail API doesn't manage milliseconds
                entry['elapsed'] = str(duration) + 's'
            data['results'].append(entry)

        response = self.client.send_post(
            ADD_RESULTS_URL.format(testrun_id),
            data,
            cert_check=self.cert_check
        )
        error = self.client.get_error(response)
        if error:
            print('[{}] Info: Testcases not published for following reason: "{}"'.format(TESTRAIL_PREFIX, error))

    def create_test_run(self, assign_user_id, project_id, suite_id, include_all, testrun_name, tr_keys, milestone_id,
                        description=''):
        """
        Create testrun with ids collected from markers.
        """
        data = {
            'suite_id': suite_id,
            'name': testrun_name,
            'description': description,
            'assignedto_id': assign_user_id,
            'include_all': include_all,
            'case_ids': tr_keys,
            'milestone_id': milestone_id
        }
        print(data)
        response = self.client.send_post(
            ADD_TESTRUN_URL.format(project_id),
            data,
            cert_check=self.cert_check
        )
        error = self.client.get_error(response)
        if error:
            print('[{}] Failed to create testrun: "{}"'.format(TESTRAIL_PREFIX, error))
        else:
            self.testrun_id = response['id']
            print('[{}] New testrun created with name "{}" and ID={}'.format(TESTRAIL_PREFIX,
                                                                             testrun_name,
                                                                             self.testrun_id))

    def close_test_run(self, testrun_id):
        """
        Closes testrun.
        """
        response = self.client.send_post(
            CLOSE_TESTRUN_URL.format(testrun_id),
            data={},
            cert_check=self.cert_check
        )
        error = self.client.get_error(response)
        if error:
            print('[{}] Failed to close test run: "{}"'.format(TESTRAIL_PREFIX, error))
        else:
            print('[{}] Test run with ID={} was closed'.format(TESTRAIL_PREFIX, self.testrun_id))

    def close_test_plan(self, testplan_id):
        """
        Closes testrun.
        """
        response = self.client.send_post(
            CLOSE_TESTPLAN_URL.format(testplan_id),
            data={},
            cert_check=self.cert_check
        )
        error = self.client.get_error(response)
        if error:
            print('[{}] Failed to close test plan: "{}"'.format(TESTRAIL_PREFIX, error))
        else:
            print('[{}] Test plan with ID={} was closed'.format(TESTRAIL_PREFIX, self.testplan_id))

    def is_testrun_available(self):
        """
        Ask if testrun is available in TestRail.

        :return: True if testrun exists AND is open
        """
        response = self.client.send_get(
            GET_TESTRUN_URL.format(self.testrun_id),
            cert_check=self.cert_check
        )
        error = self.client.get_error(response)
        if error:
            print('[{}] Failed to retrieve testrun: "{}"'.format(TESTRAIL_PREFIX, error))
            return False

        return response['is_completed'] is False

    def is_testplan_available(self):
        """
        Ask if testplan is available in TestRail.

        :return: True if testplan exists AND is open
        """
        response = self.client.send_get(
            GET_TESTPLAN_URL.format(self.testplan_id),
            cert_check=self.cert_check
        )
        error = self.client.get_error(response)
        if error:
            print('[{}] Failed to retrieve testplan: "{}"'.format(TESTRAIL_PREFIX, error))
            return False

        return response['is_completed'] is False

    def get_available_testruns(self, plan_id):
        """
        :return: a list of available testruns associated to a testplan in TestRail.

        """
        testruns_list = []
        response = self.client.send_get(
            GET_TESTPLAN_URL.format(plan_id),
            cert_check=self.cert_check
        )
        error = self.client.get_error(response)
        if error:
            print('[{}] Failed to retrieve testplan: "{}"'.format(TESTRAIL_PREFIX, error))
        else:
            for entry in response['entries']:
                for run in entry['runs']:
                    if not run['is_completed']:
                        testruns_list.append(run['id'])
        return testruns_list

    def get_tests(self, run_id):
        """
        :return: the list of tests containing in a testrun.

        """
        response = self.client.send_get(
            GET_TESTS_URL.format(run_id),
            cert_check=self.cert_check
        )
        error = self.client.get_error(response)
        if error:
            print('[{}] Failed to get tests: "{}"'.format(TESTRAIL_PREFIX, error))
            return None
        return response
