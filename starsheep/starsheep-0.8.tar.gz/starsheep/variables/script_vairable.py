from starsheep.variables.variable import Variable


class ScriptVariable(Variable):
    script_name = None
    now_calculated = False

    def __init__(self, variable_name, document, context):
        super(ScriptVariable, self).__init__(variable_name, document, context)
        if 'script_name' not in document['from_script']:
            raise Exception('Missing "script_name" in variable definition ' + variable_name)

        self.script_name = document['from_script']['script_name']

    @property
    def value(self):
        # TODO: change to locks/mutex/atomic
        if self.now_calculated:
            return ''
        else:
            self.now_calculated = True
        if self.script_name not in self.context.scripts:
            raise Exception('Missing script ' + self.script_name + ' to calculate variable ' + self.variable_name)

        script = self.context.scripts[self.script_name]
        value = script.execute(for_variable=self.variable_name)
        self.now_calculated = False
        return value
