#!/usr/bin/env python3

from radical.saga.utils import pty_process as pp
from radical.saga.utils import pty_shell_factory as psf
from radical.utils.logger import Logger

cfg = {'ssh_share_mode': 'auto',
        'ssh_copy_mode': 'sftp',
        'ssh_timeout': '10.0',
        'shell': None,
        'connection_pool_size': '10',
        'connection_pool_wait': '600',
        'prompt_pattern': '[\\$#%>\\]]\\s*$',
        'connection_pool_ttl': '600'
        }
pty = pp.PTYProcess("/usr/bin/env TERM=vt100  \"/bin/tcsh\"  -i", cfg)
pty.alive()

f = psf.PTYShellFactory()

log = Logger('test')

info                = dict()
info['posix']       = True
info['key_pass']    = dict()
info['host_str']    = 'localhost'
info['pass']        = ''
info['prompt']      = '[\$#%>\]]\s*$'
info['latency']     = 0.25
info['ssh_timeout'] = 10.0
info['logger']      = log

f._initialize_pty(pty, info)

pty.write('ls\n')
print(pty.read())
print(pty.read())
print(pty.read())

