import subprocess as sp


class GitCommand:
    @staticmethod
    def executeCommand(self, cmd):
        proc = sp.Popen(cmd, shell=True, stdin=sp.PIPE, stdout=sp.PIPE, stderr=sp.STDOUT)
        output = proc.communicate()[0]
        return output

    @staticmethod
    def commit(self, msg=None):
        output = None
        if msg is None:
            output = self.executeCommand('git commit')
        else:
            output = self.executeCommand('git commit -m '+msg)
        return output

    @staticmethod
    def push(self, branch=None):
        output = None
        if branch is None:
            output = self.executeCommand('git push -f')
        else:
            output = self.executeCommand('git push origin '+branch)
        return output

    @staticmethod
    def status(self):
        return self.executeCommand('git status')

    @staticmethod
    def pull(self):
        return self.executeCommand('git pull')

    @staticmethod
    def branch(self):
        return self.executeCommand('git branch')

    @staticmethod
    def checkout(self, branch):
        return self.executeCommand('git checkout '+branch)

    @staticmethod
    def branchAll(self):
        return self.executeCommand('git branch -a')

    @staticmethod
    def createBranch(self, branch):
        return self.executeCommand('git checkout -b '+branch)

    @staticmethod
    def fetch(self):
        return self.executeCommand('git fetch')

    @staticmethod
    def currentBranch(self):
        return self.executeCommand('git rev-parse --abbrev-ref HEAD')


