# Author: Nathan Merrill

from blinkparse import *
from pathlib import Path
import yaml, os, sys, getpass

CONFIG_FILE = os.path.join(Path.home(), '.cmrc.yaml')

with open(CONFIG_FILE, 'r') as stream:
    config = yaml.safe_load(stream)

serverArg = CommandArgument('server', list(config.keys()))
args = Parser(
    commands=[
        Command('connect', [
            serverArg
        ], ['c']),
        Command('execute', [
            serverArg,
            CommandArgument('command')
        ], ['x']),
        Command('scp', [
            serverArg,
            CommandArgument('localfile'),
            CommandArgument('remotefile'),
        ], ['s']),
        Command('ping', [
            serverArg,
        ], ['p']),
        Command('trace', [
            serverArg
        ], ['t']),
        Command('edit', aliases=['e'])
    ],
    commandRequired=True
).parse()

defaultConfig = {
    'command': 'ssh',
    'user': getpass.getuser(),
    'ip': 'localhost',
    'port': '22',
    'key': None,
    'justRunCommand': False,
    'jump': None
}

if args.command == 'edit':
    os.system('nvim ' + CONFIG_FILE)
    sys.exit()

serverConfig = config[args.commandArgs['server']]
for option in defaultConfig:
    if option not in serverConfig:
        serverConfig[option] = defaultConfig[option]

if args.command == 'ping':
    os.system('ping -c 1 ' + serverConfig['ip'])

if args.command == 'trace':
    os.system('traceroute ' + serverConfig['ip'])

keyPart = ''
jumpPart = ''
if serverConfig['key'] is not None:
    keyPart = ' -i ' + '/home/nathan/.ssh/' + serverConfig['key'] + ' '
if serverConfig['jump'] is not None:
    jumpServerConfig = config[serverConfig['jump']]
    for option in defaultConfig:
        if option not in jumpServerConfig:
            jumpServerConfig[option] = defaultConfig[option]
    jumpUserIpPort = jumpServerConfig['user'] + '@' + jumpServerConfig['ip'] + ':' + jumpServerConfig['port']
    jumpPart = ' -J ' + jumpUserIpPort + ' '
userIpPort = serverConfig['user'] + '@' + serverConfig['ip'] + ':' + serverConfig['port']

if args.command == 'connect':
    os.system(serverConfig['command'] + keyPart + jumpPart + ' ssh://' + userIpPort)

if args.command == 'execute':
    os.system(serverConfig['command'] + keyPart + jumpPart + ' ssh://' + userIpPort + ' "' + args.commandArgs['command'] + '"')

if args.command == 'scp':
    os.system('scp ' + keyPart + args.commandArgs['localfile'] + ' scp://' + userIpPort + '/' + args.commandArgs['remotefile'])
