"""
This script updates module, class, and function docs in a `README.md` file,
based on their corresponding docstrings (so that documentation does not need to
be manually written in two places).

>>> import readme_md_docstrings
... readme_md_docstrings.update('./README.md')
"""
import argparse
import functools
import importlib
import re
import urllib.parse
import pydoc
from typing import Optional, Iterable, List, Pattern

README_PATH: str = urllib.parse.urljoin(__file__, '../README.md')


Module: type = type(urllib.parse)

MARKDOWN_SECTIONS_RE: str = (
    # Group 1: Text preceding a header
    r'(.*?(?:\n|^))'
    # Group 2: Markup indicating the start of a header
    r'(#+)'
    # Group 3: Spaces, punctuation, etc. preceding the name-space key
    r'([^\w]*'  
    # Group 3: ...include any tags wrapping the name-space in group 3
    r'(?:<[^\>]+>[^\w]*)?)'  
    # Group 4: The name-space key (module/class/function name)
    r'([A-Za-z][A-Za-z_\.]*)'  
    # Group 5: The remainder of the header line
    r'([^\n]*(?:\n|$))'
    # Group 6: Text up to (but not including) the next header of the same level
    r'(.*?(?=(?:\n\2[^#]|$)))'

)
MARKDOWN_SECTIONS_PATTERN: Pattern = re.compile(
    MARKDOWN_SECTIONS_RE,
    re.DOTALL
)


class ReadMe:
    """
    This class parses a markdown-formatted README file and updates sections
    to reflect a corresponding package's class, method, and function
    docstrings.

    Parameters:

        - markdown (str): Markdown text
    """

    def __init__(
        self,
        markdown: str
    ) -> None:
        self.markdown = markdown
        self.name_space: Optional[object] = None
        self.before: str = ''
        self.header: str = ''
        self.name: str = ''

    @property
    def text(self) -> str:
        """
        This is the text preceding any sub-sections
        """
        if self.name_space is not None:
            docstring: str = pydoc.getdoc(self.name_space).strip()
            if docstring:
                return f'\n{docstring}\n'
            else:
                return ''
        else:
            return ''

    def _get_name_space(self, name: str) -> Optional[object]:
        """
        Get a name-space from an attribute name, relative to the current
        name-space, or return `None` if the attribute is not found
        """
        name_space: Optional[object] = None
        try:
            name_space = importlib.import_module(
                name,
                package=self.name_space
            )
        except ImportError:
            if self.name_space is not None:
                try:
                    name_space = getattr(self.name_space, name)
                except AttributeError:
                    pass
        return name_space

    def __iter__(self) -> Iterable['ReadMe']:
        """
        Yield an iterable collection of `ReadMe` instances representing
        sub-sections of this document or document-section.
        """
        # Only include the first "before" if it's not being replaced by a
        # docstring
        include_before: bool = False if self.text else True
        before: str
        start_header: str
        before_name: str
        name: str
        after_name: str
        body: str
        for (
            before,
            start_header,
            before_name,
            name,
            after_name,
            body
        ) in self._split():
            section: 'ReadMe' = ReadMe(markdown=body)
            section.before = before if include_before else ''
            section.header = start_header + before_name + name + after_name
            # Assign a name-space object to the section
            section.name_space = self._get_name_space(name)
            yield section
            # Only exclude before for the first section
            include_before = True

    @functools.lru_cache()
    def _split(self) -> List[str]:
        """
        Split the markdown into sections
        """
        return MARKDOWN_SECTIONS_PATTERN.findall(
            self.markdown
        )

    def __str__(self) -> str:
        """
        Render the document as markdown, updated to reflect any docstrings
        that were found
        """
        return ''.join((
            self.before,
            self.header,
            self.text,
            *(
                str(section)
                for section in self
            )
        ))


def update(path: str = './README.md') -> None:
    """
    Update an existing README.md file located at `path`.
    """
    # Read the existing markdown
    with open(path, 'r') as readme_io:
        read_me: ReadMe = ReadMe(
            readme_io.read()
        )
    # Update and save
    with open(path, 'w') as readme_io:
        readme_io.write(str(read_me))


if __name__ == '__main__':
    parser: argparse.ArgumentParser = argparse.ArgumentParser(
        description='Parse command-line arguments'
    )
    parser.add_argument(
        'path',
        default='./README.md',
        nargs=argparse.OPTIONAL,
        help='Where is the README file (defaults to "./README.md")?'
    )
    arguments = parser.parse_args()
    update(arguments.path)