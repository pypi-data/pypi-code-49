import os
import shlex
import sys

import scopeagent

argv = shlex.split(os.getenv('SCOPE_COMMAND'))
if len(argv) >= 3 and argv[0] == 'python':
    if argv[1] == '-m':
        argv = ['python -m %s' % argv[2]] + argv[3:]
    else:
        argv = argv[1:]
sys.argv = argv


agent = scopeagent.Agent()

agent.install()
