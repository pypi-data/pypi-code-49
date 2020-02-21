
class Polynomial: 
    def __init__(self, coef=[]): 
        """ inputs: array of coefficients in decending order (array)"""
        values = coef[::-1]
        self.coefs = values

    def evaluate(self, x): 
        value=0
        for i, co in enumerate(self.coefs):
            value+=co*(x**(i))

        return value 
        print(value)

    def power_rule(self): 

        if len(self.coefs)==0: 
            return None
        derivative =[]
        for i, co in enumerate(self.coefs):
            if i==0: 
                derivative.append(0)
            else: 
                value = co*(i)
                derivative.append(value)
                print("{}x^{}".format(value,(i)))
        derivative= derivative[1:]
        return derivative

    def integral(self): 
            """ inputs: none

            output: integral using power rule (array)"""
            
            if len(self.coefs)==0:
                print("value is constant")
                return None
            integral=[0]
            for i, co in enumerate(self.coefs): 
                value = co /(i+1)
                integral.append(value)
                print("{}x^{}".format(value, (i+1)))
            
            return integral



