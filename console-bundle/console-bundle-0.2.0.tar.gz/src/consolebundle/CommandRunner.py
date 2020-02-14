import sys
from consolebundle.CommandManager import CommandManager
from consolebundle.ConsoleArgumentParser import ConsoleArgumentParser
from pyfonybundles.appContainerInit import initAppContainer

def runCommand():
    argumentsParser = ConsoleArgumentParser()
    argumentsParser.add_argument(dest='commandName')
    argumentsParser.add_argument('-e', '--env', required=False, default='dev', help='Environment')

    knownArgs = argumentsParser.parse_known_args()[0]

    container = initAppContainer(knownArgs.env)
    commandManager = container.get('consolebundle.CommandManager')  # type: CommandManager

    logger = container.get('consolebundle.logger')
    logger.warning('Running command in {} environment'.format(knownArgs.env.upper()))

    if len(sys.argv) < 2:
        logger.error('Command not specified, example usage: console mynamespace:mycommand')

        print('\n[Available commands]:')

        for existingCommand in commandManager.getCommands():
            logger.info(existingCommand.getCommand() + ' - ' + existingCommand.getDescription())

        sys.exit(1)

    try:
        command = commandManager.getByName(knownArgs.commandName)
    except Exception as e: # pylint: disable = broad-except
        logger.error(str(e))
        sys.exit(1)

    command.configure(argumentsParser)
    argumentsParser.setCommandName(knownArgs.commandName)

    knownArgs = argumentsParser.parse_known_args()[0]
    command.run(knownArgs)
