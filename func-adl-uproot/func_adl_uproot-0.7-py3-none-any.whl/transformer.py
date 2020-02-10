import ast
import urllib

import awkward
import uproot

input_filenames_argument_name = 'input_filenames'
tree_name_argument_name = 'tree_name'

unary_op_dict = {ast.UAdd: '+',
                 ast.USub: '-',
                 ast.Not: 'not ',
                 ast.Invert: '~'}

bin_op_dict = {ast.Add: '+',
               ast.Sub: '-',
               ast.Mult: '*',
               ast.Div: '/',
               ast.FloorDiv: '//',
               ast.Mod: '%',
               ast.Pow: '**',
               ast.LShift: '<<',
               ast.RShift: '>>',
               ast.BitOr: '|',
               ast.BitXor: '^',
               ast.BitAnd: '&'}

bool_op_dict = {ast.And: 'and',
                ast.Or: 'or'}

compare_op_dict = {ast.Eq: '==',
                   ast.NotEq: '!=',
                   ast.Lt: '<',
                   ast.LtE: '<=',
                   ast.Gt: '>',
                   ast.GtE: '>=',
                   ast.Is: 'is',
                   ast.IsNot: 'is not',
                   ast.In: 'in',
                   ast.NotIn: 'not in'}


class PythonSourceGeneratorTransformer(ast.NodeTransformer):
    def __init__(self):
        self._id_scopes = {}

    def visit(self, node):
        if hasattr(node, 'rep'):
            return node
        else:
            return super(PythonSourceGeneratorTransformer, self).visit(node)

    def generic_visit(self, node):
        if hasattr(node, 'rep'):
            return node
        else:
            return super(PythonSourceGeneratorTransformer, self).generic_visit(node)

    def get_rep(self, node):
        if node is None:
            return ''
        if not hasattr(node, 'rep'):
            node = self.visit(node)
        return node.rep

    def visit_Module(self, node):
        if len(node.body) < 1:
            node.rep = ''
        else:
            node.rep = self.get_rep(node.body[0])
        return node

    def visit_Expr(self, node):
        node.rep = self.get_rep(node.value)
        return node

    def visit_Constant(self, node):
        node.rep = repr(node.value)
        return node

    def visit_Num(self, node):
        node.rep = repr(node.n)
        if node.n < 0:
            node.rep = '(' + node.rep + ')'
        return node

    def visit_Str(self, node):
        node.rep = repr(node.s)
        return node

    def visit_List(self, node):
        node.rep = '[' + ', '.join(self.get_rep(element) for element in node.elts) + ']'
        return node

    def visit_Tuple(self, node):
        node.rep = '(' + ', '.join(self.get_rep(element) for element in node.elts)
        if len(node.elts) == 1:
            node.rep += ','
        node.rep += ')'
        return node

    def visit_Dict(self, node):
        node.rep = ('{'
                    + ', '.join(self.get_rep(key)
                                + ': '
                                + self.get_rep(value) for key, value in zip(node.keys,
                                                                            node.values))
                    + '}')
        return node

    def get_globals(self):
        return globals()

    def resolve_id(self, id):
        if id in self._id_scopes or id in self.get_globals() or id in ('True', 'False', 'None'):
            return id
        else:
            raise NameError('Unknown id: ' + id)

    def visit_Name(self, node):
        if hasattr(node, 'ctx') and isinstance(node.ctx, ast.Param):
            node.rep = node.id
        else:
            node.rep = self.resolve_id(node.id)
        return node

    def visit_NameConstant(self, node):
        node.rep = repr(node.value)
        return node

    def visit_UnaryOp(self, node):
        if type(node.op) not in unary_op_dict:
            raise SyntaxError('Unimplemented unary operation: ' + node.op)
        operator_rep = unary_op_dict[type(node.op)]
        operand_rep = self.get_rep(node.operand)
        node.rep = '(' + operator_rep + operand_rep + ')'
        return node

    def visit_BinOp(self, node):
        left_rep = self.get_rep(node.left)
        if type(node.op) not in bin_op_dict:
            raise SyntaxError('Unimplemented binary operation: ' + node.op)
        operator_rep = bin_op_dict[type(node.op)]
        right_rep = self.get_rep(node.right)
        node.rep = '(' + left_rep + ' ' + operator_rep + ' ' + right_rep + ')'
        return node

    def visit_BoolOp(self, node):
        if type(node.op) not in bool_op_dict:
            raise SyntaxError('Unimplemented boolean operation: ' + node.op)
        operator_rep = bool_op_dict[type(node.op)]
        node.rep = ('('
                    + (' ' + operator_rep + ' ').join(self.get_rep(value) for value in node.values)
                    + ')')
        return node

    def visit_Compare(self, node):
        left_rep = self.get_rep(node.left)
        node.rep = '(' + left_rep
        for operator, comparator in zip(node.ops, node.comparators):
            if type(operator) not in compare_op_dict:
                raise SyntaxError('Unimplemented comparison operation: ' + operator)
            operator_rep = compare_op_dict[type(operator)]
            comparator_rep = self.get_rep(comparator)
            node.rep += ' ' + operator_rep + ' ' + comparator_rep
        node.rep += ')'
        return node

    def visit_Index(self, node):
        node.rep = self.get_rep(node.value)
        return node

    def visit_Slice(self, node):
        lower_rep = self.get_rep(node.lower)
        upper_rep = self.get_rep(node.upper)
        node.rep = lower_rep + ':' + upper_rep
        step_rep = self.get_rep(node.step)
        if step_rep != '':
            node.rep += ':' + step_rep
        return node

    def visit_ExtSlice(self, node):
        node.rep = ', '.join(self.get_rep(dimension) for dimension in node.dims)
        return node

    def visit_Subscript(self, node):
        value_rep = self.get_rep(node.value)
        slice_rep = self.get_rep(node.slice)
        node.rep = value_rep + '[' + slice_rep + ']'
        return node

    def visit_Attribute(self, node):
        value_rep = self.get_rep(node.value)
        node.rep = ('(' + value_rep + '.' + node.attr
                    + ' if hasattr(' + value_rep + ", '" + node.attr
                    + "') else " + value_rep + "['" + node.attr + "'])")
        return node

    def visit_Lambda(self, node):
        arg_strs = [self.get_rep(arg_node) for arg_node in node.args.args]
        args_rep = ', '.join(arg_strs)
        for arg_str in arg_strs:
            if arg_str in self._id_scopes:
                self._id_scopes[arg_str] += 1
            else:
                self._id_scopes[arg_str] = 1
        body_rep = self.get_rep(node.body)
        node.rep = '(lambda'
        if args_rep != '':
            node.rep += ' '
        node.rep += args_rep + ': ' + body_rep + ')'
        for arg_str in arg_strs:
            self._id_scopes[arg_str] -= 1
            if self._id_scopes[arg_str] == 0:
                del self._id_scopes[arg_str]
        return node

    def visit_arg(self, node):
        node.rep = node.arg
        return node

    def visit_Call(self, node):
        if isinstance(node.func, ast.Name) and node.func.id == 'EventDataset':
            if len(node.args) > 2:
                raise TypeError('EventDataset() should have no more than two arguments, found '
                                + str(len(node.args)))

            if len(node.args) >= 1:
                if hasattr(node.args[0], 'elts'):
                    urls = node.args[0].elts
                else:
                    urls = [node.args[0]]
                paths = [''.join(urllib.parse.urlparse(ast.literal_eval(url))[1:]) for url in urls]
                source_rep = (input_filenames_argument_name + ' '
                              + 'if ' + input_filenames_argument_name + ' is not None '
                              + 'else ' + repr(paths))
            else:
                source_rep = input_filenames_argument_name

            if len(node.args) >= 2:
                local_tree_name_rep = self.get_rep(node.args[1])
            else:
                local_tree_name_rep = ('(lambda key_array: '
                                       + "key_array[key_array[:, 1] == 'TTree'][:, 0])("
                                       + 'awkward.Table(uproot.open(input_files[0]).classnames())'
                                       + '.unzip()[0])[0]')
            tree_name_rep = (tree_name_argument_name + ' '
                             + 'if ' + tree_name_argument_name + ' is not None '
                             + 'else ' + local_tree_name_rep)

            node.rep = ('(lambda input_files: '
                        + 'uproot.lazyarrays(input_files, '
                        + tree_name_rep
                        + '))(' + source_rep + ')')
        else:
            func_rep = self.get_rep(node.func)
            args_rep = ', '.join(self.get_rep(arg) for arg in node.args)
            node.rep = func_rep + '(' + args_rep + ')'
        return node

    def visit_Select(self, node):
        if type(node.selector) is not ast.Lambda:
            raise TypeError('Argument to Select() must be a lambda function, found '
                            + node.selector)
        if len(node.selector.args.args) != 1:
            raise TypeError('Lambda function in Select() must have exactly one argument, found '
                            + len(node.selector.args.args))
        if type(node.selector.body) in (ast.List, ast.Tuple):
            node.selector.body = ast.Call(ast.Attribute(ast.Name('awkward'), 'Table'),
                                          node.selector.body.elts)
        if type(node.selector.body) is ast.Dict:
            node.selector.body = ast.Call(ast.Attribute(ast.Name('awkward'), 'Table'),
                                          [node.selector.body])
        call_node = self.visit(ast.Call(node.selector, [node.source]))
        node.rep = self.get_rep(call_node)
        return node

    def visit_SelectMany(self, node):
        node = self.visit_Select(node)
        call_node = self.visit(ast.Call(ast.Attribute(node, 'flatten'), []))
        node.rep = self.get_rep(call_node)
        return node

    def visit_Where(self, node):
        if type(node.predicate) is not ast.Lambda:
            raise TypeError('Argument to Where() must be a lambda function, found '
                            + node.predicate)
        if len(node.predicate.args.args) != 1:
            raise TypeError('Lambda function in Where() must have exactly one argument, found '
                            + len(node.predicate.args.args))
        node.predicate.body = ast.Subscript(ast.Name(node.predicate.args.args[0].arg),
                                            ast.Index(node.predicate.body))
        call_node = self.visit(ast.Call(node.predicate, [node.source]))
        node.rep = self.get_rep(call_node)
        return node
