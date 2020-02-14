import ast
import codecs

import astor

from .macros import get_macro


def encode(input):
    return input, len(input)


class Macro(ast.NodeTransformer):
    def visit_BinOp(self, node):
        if isinstance(node.op, ast.MatMult) and isinstance(node.left, ast.Name) and isinstance(node.right, ast.Tuple):
            macro_name = node.left.id
            macro_args = node.right.elts
            macro = get_macro(macro_name)
            return macro(macro_args, node)


def decode(input):
    code_string = codecs.decode(input)
    tree = ast.parse(code_string)
    new_tree = ast.fix_missing_locations(Macro().visit(tree))
    return astor.to_source(new_tree), len(input)


def search_function(name):
    if name == "macro":
        return codecs.CodecInfo(encode=encode, decode=decode)
