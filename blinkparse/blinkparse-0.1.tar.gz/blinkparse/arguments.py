class Arguments:
    def __init__(self, args, operands, command, commandArgs):
        self.args = args
        self.operands = operands
        self.command = command
        self.commandArgs = commandArgs

    def getDict(self):
        return self.__dict__