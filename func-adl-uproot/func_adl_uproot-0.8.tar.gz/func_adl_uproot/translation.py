import qastle

from .transformer import PythonSourceGeneratorTransformer
from .transformer import input_filenames_argument_name, tree_name_argument_name


def python_ast_to_python_source(python_ast):
    return PythonSourceGeneratorTransformer().get_rep(python_ast)


def generate_python_source(ast, function_name='run_query'):
    if isinstance(ast, str):
        ast = qastle.text_ast_to_python_ast(ast)
    qastle.insert_linq_nodes(ast)
    source = ('def ' + function_name
              + '(' + input_filenames_argument_name + '=None, '
              + tree_name_argument_name + '=None):\n')
    source += '    import awkward, uproot\n'
    source += '    return ' + python_ast_to_python_source(ast) + '\n'
    return source


def generate_function(ast, function_name='run_query'):
    source = generate_python_source(ast)
    exec(source)
    return eval(function_name)
