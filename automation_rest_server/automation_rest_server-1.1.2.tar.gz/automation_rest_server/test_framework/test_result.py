# coding=utf-8
import  xml.dom.minidom


class TestResult(object):


    def __init__(self):
        pass

    def _get_log_txt(self, log_path):
        file_ = open(log_path)
        txt_ = file_.read()
        file_.close()
        return txt_

    def _get_xml_report_txt(self, xml_path):
        dom = xml.dom.minidom.parse(xml_path)
        root = dom.documentElement
        fail_element = root.getElementsByTagName('failure')
        fail_txt = fail_element[0].firstChild.wholeText if fail_element else ""
        error_element = root.getElementsByTagName('error')
        error_txt = error_element[0].firstChild.wholeText if error_element else ""
        xml_logs = fail_txt + error_txt
        return xml_logs


    def get_test_suite_test_msg(self, test_results):
        msg = ""
        if test_results is not None:
            for test_result in test_results:
                if "msg" not in test_result.keys():
                    logs = self._get_log_txt(test_result["log_path"])
                    fail_log = self._get_xml_report_txt(test_result["xml_path"])
                    msg = msg + "\n \n ****************************************** \n \n"
                    msg = msg + test_result["name"] + "\n"
                    msg = msg + logs + "\n" + fail_log
                else:
                    msg = msg + test_result["msg"]
        return msg
