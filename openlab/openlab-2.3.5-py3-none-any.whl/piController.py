"""
Translation of Sonja Moi's PIController.m
"""
class Controler(object):
    measuredLast = None
    outputLast = None
    error = None
    errorLast = None
    
    resetStatus = True
    measured = None

    def __init__(self, kp, ki, ts, reference, initialOutput):
        print("Initializing PI Controller")
        self.kp = kp
        self.ki = ki
        self.ts = ts
        self.reference = reference
        self.initialOutput = initialOutput


    def reset(self, reference, initialOutput):
        print("Resetting PI Controller")
        self.resetStatus = True
        self.reference = reference/100000 
        self.outputLast = initialOutput

    def getOutput(self, measured):
        self.measured = measured/100000
        if self.resetStatus:
            self.error = self.reference - self.measured
            self.errorLast   = self.error
            self.resetStatus = False
        else:
            self.error = self.reference - self.measured
            self.errorLast= self.reference - self.measuredLast
           
        output = self.outputLast + (self.kp+self.ki*self.ts)*self.error-(self.kp-self.ki*self.ts/2)*self.errorLast
        
        if output > 1:
            output = 1
        if output < 0:
            output = 0

        self.measuredLast = self.measured
        self.outputLast = output

        return output