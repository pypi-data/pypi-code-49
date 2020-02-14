from typing import List
from consolebundle.ConsoleCommand import ConsoleCommand

class CommandManager:

    def __init__(self, commands: List[ConsoleCommand]):
        self.__commands = commands

    def getCommands(self):
        return self.__commands

    def getByName(self, name: str) -> ConsoleCommand:
        for command in self.__commands:
            if command.getCommand() == name:
                return command

        raise Exception('No command with name "{}" found'.format(name))
