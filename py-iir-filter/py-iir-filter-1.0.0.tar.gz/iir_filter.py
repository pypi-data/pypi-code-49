import numpy as np

class IIR2_filter:
    def __init__(self,s):
        self.numerator = s[0:3]
        self.denominator = s[3:6]
        self.buffer1 = 0
        self.buffer2 = 0

    def filter(self,v):
        input=0.0
        output=0.0
        input=v
        output=(self.numerator[1]*self.buffer1)
        input=input-(self.denominator[1]*self.buffer1)
        output=output+(self.numerator[2]*self.buffer2)
        input=input-(self.denominator[2]*self.buffer2)
        output=output+input*self.numerator[0]
        self.buffer2=self.buffer1
        self.buffer1=input
        return output

class IIR_filter:
    def __init__(self,sos):
        self.cascade = []
        for s in sos:
            self.cascade.append(IIR2_filter(s))

    def filter(self,v):
        for f in self.cascade:
            v = f.filter(v)
        return v
