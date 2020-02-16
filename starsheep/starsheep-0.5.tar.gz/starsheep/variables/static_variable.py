from starsheep.variables.variable import Variable


class StaticVariable(Variable):
    _value = None

    def __init__(self, variable_name, document, context):
        super(StaticVariable, self).__init__(variable_name, document, context)
        self._value = document['value']

    @property
    def value(self):
        return self._value