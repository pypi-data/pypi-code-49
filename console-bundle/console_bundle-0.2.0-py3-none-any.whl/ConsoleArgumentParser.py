from argparse import ArgumentParser

class ConsoleArgumentParser(ArgumentParser):

    __commandName = None
    __commandNameMessage1 = 'usage: console [-h] [-e ENV] commandName'
    __commandNameMessage2 = 'console: error: the following arguments are required: commandName'

    def setCommandName(self, commandName: str):
        self.__commandName = commandName

    def exit(self, status=0, message=None):
        strippedMessage = message.strip()

        if strippedMessage == self.__commandNameMessage2:
            return

        super().exit(status, message)

    def _print_message(self, message, file=None):
        strippedMessage = message.strip()

        if strippedMessage in (self.__commandNameMessage1, self.__commandNameMessage1):
            return

        super()._print_message(message.replace('commandName', self.__commandName), file)
