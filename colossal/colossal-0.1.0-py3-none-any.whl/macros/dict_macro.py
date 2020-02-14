import ast

from .registry import register


@register("dict")
def dict_macro(args, node):
    return ast.Call(
        func=ast.Name(id="dict"),
        args=[],
        keywords=[
            ast.keyword(arg=arg.id, value=ast.Name(id=arg.id))
            for arg in args
        ]
    )
