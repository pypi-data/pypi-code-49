import re


def camel_to_snake_case(in_string):
    regex_str = r"(.+?)([A-Z])"

    def match_to_snake(match):
        return match.group(1).lower() + '_' + match.group(2).lower()

    return re.sub(regex_str, match_to_snake, in_string, 0)
