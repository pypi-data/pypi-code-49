from numpy import *
import matplotlib.pyplot as plt
def get_functions(x):
    operators = ['+','-','*','/','**','%','^']
    functions = ['sin','cos','exp','log','1.*']
    constants = ['pi','e']
    variate=  ['x']
    c = random.choice(constants)
    o = random.choice(operators)
    f = random.choice(functions)
    v = random.choice(variate)
    
    out = c + o + f + '(' + c + o + v+')'
    return eval(out), out

if __name__ == '__main__':
    x = linspace(0, 2*pi, 100)
    y, sy = get_functions(x=x)
    plt.plot(x, y)
    plt.show()
    