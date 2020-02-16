from starsheep.variables.variable import Variable


class CmdLineVariable(Variable):
    _value = None

    def __init__(self, variable_name, document, context):
        super(CmdLineVariable, self).__init__(variable_name, document, context)
        if 'from_cmdline' not in document:
            raise Exception('Missing "option" in variable')

        for o in context.cmdline:
            if o.startswith('--' + document['from_cmdline']):
                self._value = o.split('=')[1]
        if self._value is None:
            raise Exception('Missing option for variable ' + variable_name + " --" + document['from_cmdline'] + '=...')

    @property
    def value(self):
        return self._value