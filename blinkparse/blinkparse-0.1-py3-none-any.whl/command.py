class Command:
    def __init__(self, name, args=[], aliases=[]):
        self.name = name
        self.args = args
        self.aliases = aliases

    def check(self, inputCommand, inputArgs):
        if inputCommand == self.name or inputCommand in self.aliases:
            inputArgs.pop(0)
            commandArgs = {}
            for i, commandArg in enumerate(self.args):
                try:
                    value = inputArgs[0]
                except IndexError:
                    if commandArg.required:
                        raise ValueError(f'Argument {commandArg.name} is required')
                    else:
                        continue
                if commandArg.required or value[0] != '-':
                    if commandArg.options is not None and value not in commandArg.options:
                        raise ValueError(f'{value} is not a valid argument option. The valid options are {commandArg.options}')
                    inputArgs.pop(0)
                    commandArgs[commandArg.name] = value
            return commandArgs
        return None
