import qastle

from .translation import generate_function


def ast_executor(ast):
    qastle.insert_linq_nodes(ast)
    query_function = generate_function(ast)
    return query_function()
