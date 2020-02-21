import regex
import re

import json


class CodeContentClassification:
    Label_Unknown = -1
    Label_Code = 0
    Label_Stacktrace = 1
    Label_XML_or_JSON = 2
    Label_Number = 3
    Label_text = 4

    def __init__(self):
        # 注释
        self.comment_pattern = re.compile(r'/\*\*.+?\*/', re.DOTALL)
        # 在文本后面直接加括号，没有空格将其分开
        self.brackets_pattern = re.compile(r'\S\(', re.DOTALL)
        # 两个单词之间的点
        self.point_pattern = re.compile(r'\S\.\S', re.DOTALL)
        # 两个单词之间的箭头
        self.arrow_pattern = re.compile(r'\S\.\S', re.DOTALL)
        self.CAMEL_CASE_TEST_RE = re.compile(r'^[a-zA-Z]*([a-z]+[A-Z]+|[A-Z]+[a-z]+)[a-zA-Z\d]*$')
        # 日期
        self.data_pattern = re.compile(r'\d{2}-\d{1,2} \d{1,2}:\d{1,2}:\d{1,2}')
        # 错误行:247
        self.error_row_pattern = re.compile(r':\d+\)')
        #     [INFO]
        self.info_pattern = re.compile(r'\[INFO\] ')
        #     [ERROR]
        self.error_pattern = re.compile(r'\[ERROR\] ')
        #     [WARNING]
        self.warning_pattern = re.compile(r'\[WARNING\] ')
        self.api_pattern = re.compile(r'\w+\.\w+\.\w+')
        self.xml_end = re.compile(r'</\w+>')

    def so_text_label(self, text):
        pass

    def count_upper(self, word):
        c = 0
        for e in word:
            if e.isupper():
                c += 1
        return c

    def all_camel_case(self, text):
        """
        Checks if a string is formatted as camel case.
        A string is considered camel case when:
        - it's composed only by letters ([a-zA-Z]) and optionally numbers ([0-9])
        - it contains both lowercase and uppercase letters
        - it does not start with a number
        :param text: String to test.
        :type text: str
        """
        have = set()
        af = re.split('[.( \s]', text)
        for each in af:
            if len(each) > 0 and each[0].isupper() and self.count_upper(each) == 1:
                continue
            if bool(self.CAMEL_CASE_TEST_RE.search(each)):
                have.add(each)
        return have

    def check_is_trace(self, text: str):
        # 含有这种日期格式 06-03 15:05:29
        data_len = len(self.data_pattern.findall(text))
        af = text.splitlines()
        line_num = 1.0 * len(af)
        if data_len / line_num >= 0.4:
            return True
        error_row_len = len(self.error_row_pattern.findall(text))
        if error_row_len / line_num >= 0.3:
            return True
        log_len = len(self.info_pattern.findall(text))
        log_len += len(self.error_pattern.findall(text))
        log_len += len(self.warning_pattern.findall(text))
        if log_len / line_num >= 0.3:
            return True
        for each in af:
            if text.find("Error:") >= 0 and len(self.api_pattern.findall(each)) >= 1:
                return True
        return False

    def check_json(self, text: str):
        if self.is_json(text):
            if not self.check_nums(text):
                return True

        return False

    def is_json(self, myjson):
        try:
            json.loads(myjson)
        except ValueError:
            return False
        return True

    def check_nums(self, text: str):
        text = "".join(text.split())
        all_size = 1.0 * len(text)
        count = 0
        for c in text:
            if c.isdigit():
                count += 1
        if count / all_size >= 0.32:
            return True
        return False

    def check_xml(self, text: str):
        if text.find("</groupId>") >= 0:
            return True
        depth = self.maxDepth(text, '<', '>')

        af = text.splitlines()
        line_num = 1.0 * len(af)
        end_count = len(self.xml_end.findall(text))

        if 0 < depth <= end_count:
            return True

        return False

    def get_label(self, text: str):

        if self.check_is_trace(text):
            return CodeContentClassification.Label_Stacktrace
        if self.check_xml(text) or self.check_json(text):
            return CodeContentClassification.Label_XML_or_JSON
        if self.check_is_code(text):
            return CodeContentClassification.Label_Code
        if self.check_nums(text):
            return CodeContentClassification.Label_Number
        return CodeContentClassification.Label_text

    def check_is_code(self, text: str):
        # 行尾的分号。
        # 在文本后面直接加括号，没有空格将其分开： myFunc()
        # 两个单词之间的点或箭头： foo.bar = ptr->val
        # 花括号，方括号的存在： while (true) { bar[i]; }
        # 存在“注释”语法（/ *，//等）： /* multi-line comment */
        # 不常见的字符/运算符： +, *, &, &&, |, ||, <, >, ==, !=, >=, <=, >>, <<, ::, __
        # 帖子中的驼峰文本。
        # 嵌套的括号，大括号。
        num_of_end_char = 0
        af = text.splitlines()
        line_num = len(af)
        for each_line in af:
            if each_line.strip().endswith(";"):
                num_of_end_char += 1.0
        depth_1 = self.maxDepth(text, "{", "}")
        depth_2 = self.maxDepth(text, "(", ")")
        counter_1 = max(
            text.count("{"), text.count("["), text.count("&&"),
            text.count("||"), text.count(">>"), text.count("<<"),
            text.count("::"), text.count("!="), text.count("=="), text.count(".*"),
        )
        counter_3 = len(self.brackets_pattern.findall(text))
        counter_4 = self.comment_nums(text)
        counter_5 = max(len(self.arrow_pattern.findall(text)), len(self.point_pattern.findall(text)))

        camel_list = self.all_camel_case(text)
        if (depth_1 >= 2 or depth_2 >= 2) and num_of_end_char / line_num > 0.2:
            return True
        if num_of_end_char / line_num > 0.3:
            return True
        if counter_3 >= 2:
            return True
        if counter_4 >= 1:
            return True
        if (depth_1 >= 2 or depth_2 >= 2) and len(camel_list) >= 2 and counter_3 >= 1:
            return True
        if counter_5 >= 2 and num_of_end_char / line_num > 0.1:
            return True
        if counter_1 >= 5 and num_of_end_char / line_num > 0.1:
            return True
        if counter_1 / line_num >= 0.1 and len(camel_list) >= 2:
            return True
        return False

    def maxDepth(sefl, S, p, q):
        current_max = 0
        max_d = 0
        n = len(S)
        # Traverse the input string
        for i in range(n):
            if S[i] == p:
                current_max += 1
                if current_max > max_d:
                    max_d = current_max
            elif S[i] == q:
                if current_max > 0:
                    current_max -= 1
                else:
                    return -1
        return max_d

    def comment_nums(self, text):
        m = self.comment_pattern.findall(text)
        return len(m)
