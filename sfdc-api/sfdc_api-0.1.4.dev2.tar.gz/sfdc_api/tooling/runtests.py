from urllib import parse
from urllib import request
from json import dumps
"""
# Class: runTestsAsynchronous
#   Purpose: Implements the runTests Interface
"""
class RunTests:
    __CONNECTION = None
    __ENDPOINT = None

    def __init__(self, conn):
        self.__CONNECTION = conn
        self.__ENDPOINT = self.__CONNECTION.CONNECTION_DETAILS["instance_url"] + '/services/data/v43.0/tooling/runTestsAsynchronous'

    """
    #Function run_specified_tests(self,skip_code_coverage = False, test_cases = None,  max_failed_tests=-1)
    #   Purpose: Implements the runTests call with the specified tests
    """
    def run_specified_tests(self,  test_cases = None, skip_code_coverage = False, max_failed_tests=-1):
        body = test_cases
        if(len(test_cases) == 0):
            print("No tests specified, in order to use the run specified tests")
        if isinstance(test_cases, list):
            body = list(test_cases)
            body.append({"testLevel": "RunSpecifiedTests"})
            body.append({"skipCodeCoverage": skip_code_coverage})
            body.append({"maxFailedTests": max_failed_tests})
        elif isinstance(test_cases, dict):
            body = test_cases
            body["testLevel"] = "RunSpecifiedTests"
            body["skipCodeCoverage"] = skip_code_coverage
            body["maxFailedTests"] = max_failed_tests
        else:
            print("Unsupported test_cases type, this function as per documentation only supports:\n")
            print("\t1.) A list containing dictionaries keyed with testclass names and valued with a list of test methods")
            print("\t2.) A dictionary keyed with test types and valued with a list test classes")
            print("Please refer to the documentation for this API call")
            #raise an error here
        return self.__CONNECTION.send_http_request(self.__ENDPOINT, 'POST', self.__CONNECTION.HTTPS_HEADERS['rest_authorized_headers'], dumps(body).encode('utf8'))

    def run_local_tests(self, skip_code_coverage = False):
        body = {'testLevel': "RunLocalTests", 'skipCodeCoverage' : skip_code_coverage}
        return self.__CONNECTION.send_http_request(self.__ENDPOINT, 'POST', self.__CONNECTION.HTTPS_HEADERS['rest_authorized_headers'], dumps(body).encode('utf8'))

    def run_all_tests_in_org(self, skip_code_coverage = False):
        body = {'testLevel': "RunAllTestsInOrg", 'skipCodeCoverage': skip_code_coverage}
        return self.__CONNECTION.send_http_request(self.__ENDPOINT, 'POST', self.__CONNECTION.HTTPS_HEADERS['rest_authorized_headers'], dumps(body).encode('utf8'))