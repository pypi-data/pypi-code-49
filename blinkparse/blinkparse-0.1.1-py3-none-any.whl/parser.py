import sys

from blinkparse.argument import Argument
from blinkparse.arguments import Arguments

class Parser:
    def __init__(self, args=[], commands=[], description='', commandRequired=False, noOperands=False):
        self.args = args
        self.commands = commands
        self.description = description
        self.commandRequired = commandRequired
        self.noOperands = noOperands
        self.args.append(Argument('help', 'h', description='Show this help page'))

    def displayHelpPage(self, exit=True):
        if self.description != '':
            print(self.description.strip())

        if len(self.commands) != 0:
            if self.commandRequired:
                print('Commands - Required')
            else:
                print('Commands')

            for command in self.commands:
                print('    ', command.name)
                for commandArg in command.args:
                    print(f'        {commandArg.name}: {commandArg.options if commandArg.options is not None else "anything"}{" - Required" if commandArg.required else ""}')

        print('Arguments')
        for arg in self.args:
            argText = ''
            if arg.takesValue:
                argText += f'--{arg.name}=myValue'
                if arg.shortName is not None:
                    argText += f', -{arg.shortName} myValue'
            else:
                argText += f'--{arg.name}'
                if arg.shortName is not None:
                    argText += f', -{arg.shortName}'
            print(f'    {argText}')
            print(f'        {arg.description}')
            if arg.required:
                print('        Required')
        if exit:
            sys.exit()

    def parse(self, inputArgs=None):
        if inputArgs is None:
            inputArgs = sys.argv[1:]

        if '-h' in inputArgs or '--help' in inputArgs:
            self.displayHelpPage()

        if len(self.commands) != 0:
            try:
                inputCommand = inputArgs[0]
            except IndexError:
                raise ValueError(f'This program requires a command. The options are {list(loopCommand.name for loopCommand in self.commands)}')
            for command in self.commands:
                commandArgs = command.check(inputCommand, inputArgs)
                if commandArgs is not None:
                    break
                else:
                    command = None
        else:
            command = None
            commandArgs = None

        if command is None and self.commandRequired:
            raise ValueError(f'This program requires a command. The options are {list(loopCommand.name for loopCommand in self.commands)}')

        outputArgs = {}
        for arg in self.args:
            outputArgs.update(arg.check(inputArgs))

        if self.noOperands and len(inputArgs) != 0:
            raise ValueError(f'This program doesn\'t take operands.')

        return Arguments(outputArgs, inputArgs, command.name if command is not None else None, commandArgs)