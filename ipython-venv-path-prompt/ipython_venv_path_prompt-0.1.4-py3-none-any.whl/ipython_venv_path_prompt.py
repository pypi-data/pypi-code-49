"""Virtual env and cwd prompt.
"""

import sys
import os
from pathlib import Path
from IPython.terminal.prompts import Prompts, Token

def get_venv_prompt_prefix():
    if 'CONDA_DEFAULT_ENV' in os.environ:
        return '({}) '.format(os.environ['CONDA_DEFAULT_ENV'])
    elif hasattr(sys, 'real_prefix') or sys.base_prefix != sys.prefix:
        return '({}) '.format(Path(sys.prefix).parts[-1])
    else:
        return ''

class EnvPathPrompts(Prompts):
    PATH_FMT = '{}{{}}\n'.format(get_venv_prompt_prefix())
    def __init__(self, shell, parent_prompts):
        super().__init__(shell)
        self.parent_prompts = parent_prompts
    def in_prompt_tokens(self):
        return [(Token.Comment, self.PATH_FMT.format(os.getcwd()))] + self.parent_prompts.in_prompt_tokens()

def load_ipython_extension(shell):
    shell.prompts = EnvPathPrompts(shell, shell.prompts)

def unload_ipython_extension(shell):
    if not isinstance(shell.prompts, EnvPathPrompts):
        print("cannot unload")
    else:
        shell.prompts = shell.prompts.parent_prompts
