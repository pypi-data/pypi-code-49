from starsheep.variables.variable import Variable


class ContextVariable(Variable):
    def __init__(self, variable_name, document, context):
        super(ContextVariable, self).__init__(variable_name, document, context)

    @property
    def value(self):
        pass
