import re


class StringUtils:
    @staticmethod
    def camel2line(camel: str):
        p = re.compile(r'([a-z]|\d)([A-Z])')
        line = re.sub(p, r'\1_\2', camel).lower()
        return line
