from starsheep.variables.variable import Variable


class ScriptVariable(Variable):
    script_name = None

    def __init__(self, variable_name, document, context):
        super(ScriptVariable, self).__init__(variable_name, document, context)
        if 'script_name' not in document['from_script']:
            raise Exception('Missing "script_name" in variable definition ' + variable_name)

        self.script_name = document['from_script']['script_name']

    @property
    def value(self):
        if self.script_name not in self.context.scripts:
            raise Exception('Missing script ' + self.script_name + ' to calculate variable ' + self.variable_name)

        script = self.context.scripts[self.script_name]
        return script.execute(for_variable=self.variable_name)
