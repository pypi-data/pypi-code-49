import fire


class Calculator(object):

    def solve(self, expression):
        evaluate = eval(expression)
        print(evaluate)
