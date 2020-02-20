import tempfile
import os
import subprocess
import logging


class Script(object):
    context = None
    script_name = None
    interpreter = None
    variables = None
    script_contents = None
    timeout = None

    def __init__(self, script_name, document, variables, context):
        self.context = context
        self.script_name = script_name
        self.interpreter = document['interpreter']
        self.script_contents = document['script']
        self.variables = variables

        if 'timeout' in document:
            self.timeout = document['timeout']
        else:
            timeout = 60

        logging.info('Created script ' + self.script_name)

    def __str__(self):
        return self.script_name

    def execute(self, variables={}, for_variable=None):
        '''
        :param variables: List of additional, local variables for this script
        :param for_variable: Name of variable. Used only by ScriptVariable class to aviod recursion
        :return:
        '''
        path_t = tempfile.mkstemp(prefix='starsheep-script-')
        os.close(path_t[0])
        f = open(path_t[1], 'w')
        f.write(self.script_contents)
        f.close()

        env = {}
        for v in self.context.variables:
            if v != for_variable:
                env['' + v.upper()] = self.context.variables[v].value
        for v in self.variables:
            if v != for_variable:
                env['' + v.upper()] = self.variables[v].value
        for v in variables:
            env['' + v.upper()] = variables[v]

        output = ''

        if os.path.exists(self.interpreter):
            call = subprocess.Popen([self.interpreter, path_t[1]], env=env, stdout=subprocess.PIPE)
            try:
                rc = call.wait(timeout=self.timeout)
            except subprocess.TimeoutExpired as e:
                raise Exception('Script ' + self.script_name + ' timeout ' + str(self.timeout) + 's')

            if call.wait() != 0:
                raise Exception('Script ' + self.script_name + ' failed')
            output = call.stdout.read().decode('utf-8')

        os.remove(path_t[1])

        return output

    @staticmethod
    def load(document, context):
        from starsheep.variables.variable import Variable

        scripts = {}
        for script_name in document.keys():
            if 'script' not in document[script_name]:
                logging.error('Missing "script" in ' + script_name)
                continue
            if 'interpreter' not in document[script_name]:
                logging.error('Missing "interpreter" in ' + script_name)
                continue

            variables = {}

            if 'variables' in document[script_name]:
                variables.update(Variable.load(document[script_name]['variables'], context))

            scripts[script_name] = Script(script_name, document[script_name], variables, context)

        context.scripts = scripts
