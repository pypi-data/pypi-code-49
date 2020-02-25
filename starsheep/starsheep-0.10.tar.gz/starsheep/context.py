class Context(object):
    debug = False
    variables = None
    scripts = None
    listeners = None
    models = None

    cmdline = []

    current_model = None
    current_field = None

    def __init__(self, debug=False):
        self.debug = debug

        self.variables = {}
        self.scripts = {}
        self.listeners = {}
        self.models = {}

    def __str__(self):
        r = ''
        r += 'Variables:\n'
        for v in self.variables:
            r += str(self.variables[v]) + '\n'

        r += '\nScripts:\n'
        for s in self.scripts:
            r += str(self.scripts[s]) + '\n'

        r += '\nListeners:\n'
        for l in self.listeners:
            r += str(self.listeners[l]) + '\n'

        r += '\nModels:\n'
        for m in self.models:
            r += str(self.models[m]) + '\n'

        return r