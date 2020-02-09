"""
    sphinx.transforms.post_transforms.compat
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Post transforms for compatibility

    :copyright: Copyright 2007-2020 by the Sphinx team, see AUTHORS.
    :license: BSD, see LICENSE for details.
"""

import warnings
from typing import Any, Dict

from docutils import nodes
from docutils.writers.docutils_xml import XMLTranslator

from sphinx.addnodes import math_block, displaymath
from sphinx.application import Sphinx
from sphinx.deprecation import RemovedInSphinx30Warning
from sphinx.transforms import SphinxTransform
from sphinx.util import logging


logger = logging.getLogger(__name__)


class MathNodeMigrator(SphinxTransform):
    """Migrate a math node to docutils'.

    For a long time, Sphinx uses an original node for math. Since 1.8,
    Sphinx starts to use a math node of docutils'.  This transform converts
    old and new nodes to keep compatibility.
    """
    default_priority = 999

    def apply(self, **kwargs: Any) -> None:
        for math_node in self.document.traverse(nodes.math):
            # case: old styled ``math`` node generated by old extensions
            if len(math_node) == 0:
                warnings.warn("math node for Sphinx was replaced by docutils'. "
                              "Please use ``docutils.nodes.math`` instead.",
                              RemovedInSphinx30Warning)
                equation = math_node['latex']
                math_node += nodes.Text(equation, equation)

        translator = self.app.builder.get_translator_class()
        if hasattr(translator, 'visit_displaymath') and translator != XMLTranslator:
            # case: old translators which does not support ``math_block`` node
            warnings.warn("Translator for %s does not support math_block node'. "
                          "Please update your extension." % translator,
                          RemovedInSphinx30Warning)
            for old_math_block_node in self.document.traverse(math_block):
                alt = displaymath(latex=old_math_block_node.astext(),
                                  number=old_math_block_node.get('number'),
                                  label=old_math_block_node.get('label'),
                                  nowrap=old_math_block_node.get('nowrap'),
                                  docname=old_math_block_node.get('docname'))
                old_math_block_node.replace_self(alt)
        elif getattr(self.app.builder, 'math_renderer_name', None) == 'unknown':
            # case: math extension provides old styled math renderer
            for math_block_node in self.document.traverse(nodes.math_block):
                math_block_node['latex'] = math_block_node.astext()

        # case: old styled ``displaymath`` node generated by old extensions
        for math_block_node in self.document.traverse(math_block):
            if len(math_block_node) == 0:
                warnings.warn("math node for Sphinx was replaced by docutils'. "
                              "Please use ``docutils.nodes.math_block`` instead.",
                              RemovedInSphinx30Warning)
                if isinstance(math_block_node, displaymath):
                    newnode = nodes.math_block('', math_block_node['latex'],
                                               **math_block_node.attributes)
                    math_block_node.replace_self(newnode)
                else:
                    latex = math_block_node['latex']
                    math_block_node += nodes.Text(latex, latex)


def setup(app: Sphinx) -> Dict[str, Any]:
    app.add_post_transform(MathNodeMigrator)

    return {
        'version': 'builtin',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
