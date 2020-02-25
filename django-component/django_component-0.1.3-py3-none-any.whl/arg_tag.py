from django import template


class IllegalArgParentException(Exception):
    pass


class ArgAlreadyDefinedException(Exception):
    pass


def arg_tag(parser, token):
    [arg_tag_name] = token.split_contents()[1:]
    nodelist = parser.parse(("endarg",))
    parser.delete_first_token()
    return ArgNode(arg_tag_name, nodelist)


class ArgNode(template.Node):
    def __init__(self, name, nodelist):
        self.name = name
        self.nodelist = nodelist

    def render_arg_tag(self, context):
        output = self.nodelist.render(context)
        return output

    def render(self, context):
        raise IllegalArgParentException(
            "An arg tag can only appear as a direct child of a component"
        )
