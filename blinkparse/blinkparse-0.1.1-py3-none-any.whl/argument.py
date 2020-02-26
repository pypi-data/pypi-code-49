class Argument:
    def __init__(self, name, shortName=None, takesValue=False, required=False, description=None):
        self.name = name
        self.shortName = shortName
        self.takesValue = takesValue
        self.required = required
        self.description = description

    def check(self, inputArgs):
        outputArgs = {}

        for i, inputArg in enumerate(inputArgs):
            if f'--{self.name}' in inputArg:
                outputArgs[self.name] = None
                splitArg = inputArg.split('=')
                if self.takesValue:
                    if len(splitArg) == 2:
                        outputArgs[self.name] = splitArg[1]
                    else:
                        raise ValueError(f'The {self.name} argument takes input. Did you mean --{self.name}=myValue')
                else:
                    if len(splitArg) != 1:
                        raise ValueError(f'The {self.name} argument doesn\'t take input. Did you mean --{self.name}')
                inputArgs.pop(i)
                break

            elif self.shortName is not None and inputArg == f'-{self.shortName}':
                outputArgs[self.name] = None
                if self.takesValue:
                    try:
                        value = inputArgs[i + 1]
                    except IndexError:
                        raise ValueError(f'The {self.name} argument takes input. Did you mean -{self.shortName} myValue')
                    outputArgs[self.name] = value
                    inputArgs.pop(i)
                inputArgs.pop(i)
                break

        if self.required and len(outputArgs) == 0:
            raise ValueError(f'The {self.name} argument is required')

        return outputArgs