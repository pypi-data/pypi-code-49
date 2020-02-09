"""
    sphinx.addnodes
    ~~~~~~~~~~~~~~~

    Additional docutils nodes.

    :copyright: Copyright 2007-2020 by the Sphinx team, see AUTHORS.
    :license: BSD, see LICENSE for details.
"""

import warnings
from typing import Any, Dict, List, Sequence

from docutils import nodes
from docutils.nodes import Node

from sphinx.deprecation import RemovedInSphinx30Warning, RemovedInSphinx40Warning

if False:
    # For type annotation
    from sphinx.application import Sphinx


class translatable(nodes.Node):
    """Node which supports translation.

    The translation goes forward with following steps:

    1. Preserve original translatable messages
    2. Apply translated messages from message catalog
    3. Extract preserved messages (for gettext builder)

    The translatable nodes MUST preserve original messages.
    And these messages should not be overridden at applying step.
    Because they are used at final step; extraction.
    """

    def preserve_original_messages(self) -> None:
        """Preserve original translatable messages."""
        raise NotImplementedError

    def apply_translated_message(self, original_message: str, translated_message: str) -> None:
        """Apply translated message."""
        raise NotImplementedError

    def extract_original_messages(self) -> Sequence[str]:
        """Extract translation messages.

        :returns: list of extracted messages or messages generator
        """
        raise NotImplementedError


class not_smartquotable:
    """A node which does not support smart-quotes."""
    support_smartquotes = False


class toctree(nodes.General, nodes.Element, translatable):
    """Node for inserting a "TOC tree"."""

    def preserve_original_messages(self) -> None:
        # toctree entries
        rawentries = self.setdefault('rawentries', [])
        for title, docname in self['entries']:
            if title:
                rawentries.append(title)

        # :caption: option
        if self.get('caption'):
            self['rawcaption'] = self['caption']

    def apply_translated_message(self, original_message: str, translated_message: str) -> None:
        # toctree entries
        for i, (title, docname) in enumerate(self['entries']):
            if title == original_message:
                self['entries'][i] = (translated_message, docname)

        # :caption: option
        if self.get('rawcaption') == original_message:
            self['caption'] = translated_message

    def extract_original_messages(self) -> List[str]:
        messages = []  # type: List[str]

        # toctree entries
        messages.extend(self.get('rawentries', []))

        # :caption: option
        if 'rawcaption' in self:
            messages.append(self['rawcaption'])
        return messages


# domain-specific object descriptions (class, function etc.)

class desc(nodes.Admonition, nodes.Element):
    """Node for object descriptions.

    This node is similar to a "definition list" with one definition.  It
    contains one or more ``desc_signature`` and a ``desc_content``.
    """


class desc_signature(nodes.Part, nodes.Inline, nodes.TextElement):
    """Node for object signatures.

    The "term" part of the custom Sphinx definition list.

    As default the signature is a single line signature,
    but set ``is_multiline = True`` to describe a multi-line signature.
    In that case all child nodes must be ``desc_signature_line`` nodes.
    """


class desc_signature_line(nodes.Part, nodes.Inline, nodes.FixedTextElement):
    """Node for a line in a multi-line object signatures.

    It should only be used in a ``desc_signature`` with ``is_multiline`` set.
    Set ``add_permalink = True`` for the line that should get the permalink.
    """
    sphinx_cpp_tagname = ''


# nodes to use within a desc_signature or desc_signature_line

class desc_addname(nodes.Part, nodes.Inline, nodes.FixedTextElement):
    """Node for additional name parts (module name, class name)."""


# compatibility alias
desc_classname = desc_addname


class desc_type(nodes.Part, nodes.Inline, nodes.FixedTextElement):
    """Node for return types or object type names."""


class desc_returns(desc_type):
    """Node for a "returns" annotation (a la -> in Python)."""
    def astext(self) -> str:
        return ' -> ' + super().astext()


class desc_name(nodes.Part, nodes.Inline, nodes.FixedTextElement):
    """Node for the main object name."""


class desc_parameterlist(nodes.Part, nodes.Inline, nodes.FixedTextElement):
    """Node for a general parameter list."""
    child_text_separator = ', '


class desc_parameter(nodes.Part, nodes.Inline, nodes.FixedTextElement):
    """Node for a single parameter."""


class desc_optional(nodes.Part, nodes.Inline, nodes.FixedTextElement):
    """Node for marking optional parts of the parameter list."""
    child_text_separator = ', '

    def astext(self) -> str:
        return '[' + super().astext() + ']'


class desc_annotation(nodes.Part, nodes.Inline, nodes.FixedTextElement):
    """Node for signature annotations (not Python 3-style annotations)."""


class desc_content(nodes.General, nodes.Element):
    """Node for object description content.

    This is the "definition" part of the custom Sphinx definition list.
    """


# new admonition-like constructs

class versionmodified(nodes.Admonition, nodes.TextElement):
    """Node for version change entries.

    Currently used for "versionadded", "versionchanged" and "deprecated"
    directives.
    """


class seealso(nodes.Admonition, nodes.Element):
    """Custom "see also" admonition."""


class productionlist(nodes.Admonition, nodes.Element):
    """Node for grammar production lists.

    Contains ``production`` nodes.
    """


class production(nodes.Part, nodes.Inline, nodes.FixedTextElement):
    """Node for a single grammar production rule."""


# math nodes


class math(nodes.math):
    """Node for inline equations.

    .. warning:: This node is provided to keep compatibility only.
                 It will be removed in nearly future.  Don't use this from your extension.

    .. deprecated:: 1.8
       Use ``docutils.nodes.math`` instead.
    """

    def __getitem__(self, key):
        """Special accessor for supporting ``node['latex']``."""
        if key == 'latex' and 'latex' not in self.attributes:
            warnings.warn("math node for Sphinx was replaced by docutils'. "
                          "Therefore please use ``node.astext()`` to get an equation instead.",
                          RemovedInSphinx30Warning, stacklevel=2)
            return self.astext()
        else:
            return super().__getitem__(key)


class math_block(nodes.math_block):
    """Node for block level equations.

    .. warning:: This node is provided to keep compatibility only.
                 It will be removed in nearly future.  Don't use this from your extension.

    .. deprecated:: 1.8
    """

    def __getitem__(self, key):
        if key == 'latex' and 'latex' not in self.attributes:
            warnings.warn("displaymath node for Sphinx was replaced by docutils'. "
                          "Therefore please use ``node.astext()`` to get an equation instead.",
                          RemovedInSphinx30Warning, stacklevel=2)
            return self.astext()
        else:
            return super().__getitem__(key)


class displaymath(math_block):
    """Node for block level equations.

    .. warning:: This node is provided to keep compatibility only.
                 It will be removed in nearly future.  Don't use this from your extension.

    .. deprecated:: 1.8
    """


# other directive-level nodes

class index(nodes.Invisible, nodes.Inline, nodes.TextElement):
    """Node for index entries.

    This node is created by the ``index`` directive and has one attribute,
    ``entries``.  Its value is a list of 5-tuples of ``(entrytype, entryname,
    target, ignored, key)``.

    *entrytype* is one of "single", "pair", "double", "triple".

    *key* is categorization characters (usually a single character) for
    general index page. For the details of this, please see also:
    :rst:dir:`glossary` and issue #2320.
    """


class centered(nodes.Part, nodes.TextElement):
    """Deprecated."""


class acks(nodes.Element):
    """Special node for "acks" lists."""


class hlist(nodes.Element):
    """Node for "horizontal lists", i.e. lists that should be compressed to
    take up less vertical space.
    """


class hlistcol(nodes.Element):
    """Node for one column in a horizontal list."""


class compact_paragraph(nodes.paragraph):
    """Node for a compact paragraph (which never makes a <p> node)."""


class glossary(nodes.Element):
    """Node to insert a glossary."""


class only(nodes.Element):
    """Node for "only" directives (conditional inclusion based on tags)."""


# meta-information nodes

class start_of_file(nodes.Element):
    """Node to mark start of a new file, used in the LaTeX builder only."""


class highlightlang(nodes.Element):
    """Inserted to set the highlight language and line number options for
    subsequent code blocks.
    """


class tabular_col_spec(nodes.Element):
    """Node for specifying tabular columns, used for LaTeX output."""


class meta(nodes.Special, nodes.PreBibliographic, nodes.Element):
    """Node for meta directive -- same as docutils' standard meta node,
    but pickleable.
    """
    rawcontent = None


# inline nodes

class pending_xref(nodes.Inline, nodes.Element):
    """Node for cross-references that cannot be resolved without complete
    information about all documents.

    These nodes are resolved before writing output, in
    BuildEnvironment.resolve_references.
    """


class number_reference(nodes.reference):
    """Node for number references, similar to pending_xref."""


class download_reference(nodes.reference):
    """Node for download references, similar to pending_xref."""


class literal_emphasis(nodes.emphasis, not_smartquotable):
    """Node that behaves like `emphasis`, but further text processors are not
    applied (e.g. smartypants for HTML output).
    """


class literal_strong(nodes.strong, not_smartquotable):
    """Node that behaves like `strong`, but further text processors are not
    applied (e.g. smartypants for HTML output).
    """


class abbreviation(nodes.abbreviation):
    """Node for abbreviations with explanations.

    .. deprecated:: 2.0
    """

    def __init__(self, rawsource: str = '', text: str = '',
                 *children: Node, **attributes: Any) -> None:
        warnings.warn("abbrevition node for Sphinx was replaced by docutils'.",
                      RemovedInSphinx40Warning, stacklevel=2)

        super().__init__(rawsource, text, *children, **attributes)


class manpage(nodes.Inline, nodes.FixedTextElement):
    """Node for references to manpages."""


def setup(app: "Sphinx") -> Dict[str, Any]:
    app.add_node(toctree)
    app.add_node(desc)
    app.add_node(desc_signature)
    app.add_node(desc_signature_line)
    app.add_node(desc_addname)
    app.add_node(desc_type)
    app.add_node(desc_returns)
    app.add_node(desc_name)
    app.add_node(desc_parameterlist)
    app.add_node(desc_parameter)
    app.add_node(desc_optional)
    app.add_node(desc_annotation)
    app.add_node(desc_content)
    app.add_node(versionmodified)
    app.add_node(seealso)
    app.add_node(productionlist)
    app.add_node(production)
    app.add_node(displaymath)
    app.add_node(index)
    app.add_node(centered)
    app.add_node(acks)
    app.add_node(hlist)
    app.add_node(hlistcol)
    app.add_node(compact_paragraph)
    app.add_node(glossary)
    app.add_node(only)
    app.add_node(start_of_file)
    app.add_node(highlightlang)
    app.add_node(tabular_col_spec)
    app.add_node(meta)
    app.add_node(pending_xref)
    app.add_node(number_reference)
    app.add_node(download_reference)
    app.add_node(literal_emphasis)
    app.add_node(literal_strong)
    app.add_node(manpage)

    return {
        'version': 'builtin',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
