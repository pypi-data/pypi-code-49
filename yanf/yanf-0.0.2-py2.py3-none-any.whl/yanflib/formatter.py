import json
import platform
import re

from yapf.yapflib.yapf_api import FormatCode


class NotebookFormatter:
    def __init__(self, file, style='pep8'):
        self.__file = file
        self.__style = style
        self.__read_notebook()
        self.__check_lang()

        self.__format_ok = False

    def __read_notebook(self):
        with open(self.__file) as infile:
            self.__notebook = json.load(infile)

    def __check_lang(self):
        lang = self.__notebook['metadata']['kernelspec']['language']
        if lang != 'python':
            exit("This formatter can only format Python notebooks, found %s" % lang)

    def __comment_magic_commands(self, source):
        for i, line in enumerate(source):
            if re.match("^%\w+.*", line.lstrip()):
                source[i] = '##MAGIC##' + line
        return source

    def __uncomment_magic_commands(self, source):
        for i, line in enumerate(source):
            if line.lstrip().startswith('##MAGIC##'):
                source[i] = line.replace('##MAGIC##', '')
        return source

    def __format_cell(self, source):
        commented = self.__comment_magic_commands(source)
        formatted, changed = FormatCode(''.join(commented), style_config=self.__style)

        # We strip any ending newlines of the snippet and add one back at the end
        split_source = formatted.rstrip('\n').split('\n')
        lastidx = len(split_source) - 1
        for i, line in enumerate(split_source):
            # Don't add newline to last line
            if i < lastidx:
                split_source[i] = line + '\n'

        uncommented = self.__uncomment_magic_commands(split_source)
        return uncommented

    def format(self):
        for cell in self.__notebook['cells']:
            cell_type = cell['cell_type']
            if cell_type == 'code':
                cell['source'] = self.__format_cell(cell['source'])
        self.__format_ok = True
        return self

    def write(self):
        if not self.__format_ok:
            exit("Could not write formatted notebook, format failed or not executed")

        with open(self.__file, 'w') as outfile:
            json.dump(self.__notebook, outfile, indent=1)
