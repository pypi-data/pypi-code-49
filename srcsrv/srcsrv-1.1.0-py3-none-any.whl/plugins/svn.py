'''SVN plugin
'''
# Python modules
import os
import sys
import svn.local
import argparse
# Source index modules
from .. import base


class SVN(base.Base):
    '''SVN processing
    '''
    def __init__(self, args, namespace):
        super(SVN, self).__init__(namespace)

        # Add plugin specific arguments
        parser = argparse.ArgumentParser()
        parser.add_argument('-I', '--uri',    help='SVN repository server URI')
        parser.add_argument('-V', '--revision', help='SVN revision')
        # Pares remaining  unrecognized args
        namespace = parser.parse_args(args)
        self.args.__dict__.update(namespace.__dict__)
        if not self.args.revision:
            self.repo = svn.local.LocalClient(self.args.build_base)
            info = self.repo.info()
            self.args.revision = info['commit_revision']

    def process(self, src=None, code=None, md5=None):
        ''' Process .PDB content
        '''
        if not src:
            # called without arguments; Print SRCSRV variables block
            self.args.output.write(rf'''SRCSRVTRG=%svn_extract_target%
SRCSRVCMD=%svn_cmd%
SVN_EXTRACT_TARGET=%svn_extract_target_dir%\%var3%
SVN_EXTRACT_TARGET_DIR=%svn_cache%\%fnbksl%(%svn_project%)%fnbksl%(%var2%)\%var3%\%var4%
SVN_CMD=(md "%svn_extract_target_dir%" > nul 2> nul) & %svn_exe% export -r {self.args.revision} %svn_creds% --no-auth-cache %svn_url%%svn_path% %SRCSRVTRG%
SVN_EXE=svn.exe
SVN_URL=%svn_scheme%{self.args.uri}/%svn_branch%
SVN_SCHEME={self.args.scheme}
SVN_BRANCH={self.args.branch}
SVN_PROJECT={self.args.project}
SVN_PATH=%var2%/%var3%
SVN_CACHE=%userprofile%
SVN_CREDS=%subversion_creds%
''')
            return True

        dir = os.path.dirname(code.path)
        base = os.path.basename(code.path)
        # called with source file path; Print SRCSRV file entry
        self.args.output.write(f'{src}*{dir}*{base}*{md5}\n')
        return True


__all__ = ['SVN']
