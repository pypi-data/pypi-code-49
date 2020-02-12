import codecs
import os
import re

from latextomd import config

from latextomd.postpandoc import Postpandoc
from latextomd.soup import Latex
from latextomd.text_manipulation import LatexString


def _process_preamble(latex_string):
    """Detect Latex Preamble

    Arguments:
        latex_string {string} -- Latex Source

    Returns:
        tupple -- preamble, content
    """
    if r"\begin{document}" in latex_string:
        preamble, content = latex_string.split(r"\begin{document}")
        if r"\end{document}" in content:
            content = content.split(r"\end{document}")[0]
    else:
        preamble = "\\documentclass{article}\n"
        content = latex_string
    return preamble, content


def _strip_lines(latex_string):
    """Strip Lines in Latex Source

    Arguments:
        latex_string {string} -- LateX Source

    Returns:
        string -- Latex with lines striped
    """
    lines = latex_string.splitlines()
    result = []
    for line in lines:
        result.append(line.strip())
    return "\n".join(result)


def _clean_lines(latex_string):
    lines = latex_string.splitlines()
    while lines[0] == "":
        lines = lines[1:]
    while lines[-1] == "":
        lines = lines[:-1]
    content = "\n".join(lines)
    while "\n\n\n" in content:
        content = content.replace("\n\n\n", "\n\n")
    return content


def _delete_blocks(latex_string):
    """delete blocks define in config.del_environnements

    Arguments:
        latex_string {string} -- Latex string

    Returns:
        string -- Latex string
    """
    content = latex_string
    for env in config.del_environnements:
        content = content.replace(env, "")
    return content


def _pandoc(preamble, content):
    """Convert latex to md with pandoc

    Arguments:
        preamble {string} -- Latex preamble: documentclass{...}...
        content {string} -- Latex content

    Returns:
        string -- Markdown
    """
    total = "\n\\begin{document}\n".join([preamble, content]) + "\n\\end{document}"
    f = codecs.open("temp.tex", "w", "utf-8")
    f.write(total)
    f.close()
    # os.system("pandoc temp.tex -o temp.md --katex --from latex --to gfm")
    os.system("pandoc temp.tex -o temp.md")
    with codecs.open("temp.md", "r", "utf-8") as f:
        content = f.read()
    return content
    # os.system(f"dvisvgm temp.dvi")


def to_markdown(latex_string, export_file_name=""):
    content = latex_string
    content = _strip_lines(content)

    preamble, content = _process_preamble(content)
    content = LatexString(content, preamble, export_file_name).process()
    content = _pandoc(preamble, content)
    # content = Latex(content).process()
    content = Postpandoc(content).process()
    content = _delete_blocks(content)
    # content = _strip_lines(content)

    content = _clean_lines(content)
    return content


class LatexToMd(object):
    def __init__(self, latex_string, export_file_name=""):
        """Initialisation LatexToMd
        
        Arguments:
            latex_string {str} -- latex string
        
        Keyword Arguments:
            export_file_name {str} -- export file name (default: {""})
        """
        self.content = latex_string

    def process(self):
        """Convert Latex String in Markdown String
        
        Returns:
            {str} -- Markdown String
        """
        self.prepandoc()
        return self.content

    def prepandoc(self):
        self._remove_comments()
        self._replace_simple()
        self._strip_lines()
        self.preamble, self.content = _process_preamble(self.content)
        self.content = _clean_lines(self.content)

    def _remove_comments(self):
        """Remove comments in latex_string
        """
        self.content = re.sub("(?<!\\\\)%.*$", "", self.content, flags=re.M)

    def _replace_simple(self):
        """Replace without regex
        use config.replace_simple
        """
        for replace_simple in config.replace_simple:
            self.content = self.content.replace(replace_simple[0], replace_simple[1])

    def _strip_lines(self):
        """Strip lines in latex string
        """
        lines = self.content.splitlines()
        result = []
        for line in lines:
            result.append(line.strip())
        self.content = "\n".join(result)
