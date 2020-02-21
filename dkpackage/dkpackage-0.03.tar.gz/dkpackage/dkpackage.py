'''dkpackage.py'''


class Davidsolution(object):
    def start(self, strs):
        return strs + "[thread:START]"

    def stop(self, strs):
        return strs + "[thread:STOP]"


'''myDavidSolution = Davidsolution()
print(myDavidSolution.start("DKpackage: Started!")+" and "+myDavidSolution.stop("DKpackage: Stopped!"))'''
