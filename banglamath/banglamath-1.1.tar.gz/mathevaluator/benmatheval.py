"""
    Bangla math evaluator calculates the result of any bengali mathematical
    expression and returns it.

    Author: Saimon
    Email: saimoncse19@gmail.com

"""


class Evaluator:

    def __init__(self):
        self._digits = ["০", "১", "২", "৩", "৪", "৫", "৬", "৭", "৮", "৯"]
        self._operators = ["=", "+", "-", "*", "/", "%", "<", ">", "×", "÷"]

    def bengali_to_english(self, expression: str):

        exp_len = len(expression)
        temp = 0

        for i in expression:
            if i in self._digits or i in self._operators or i in ["(", ")", "{", "}", "[", "]"]:
                temp += 1

        if exp_len == temp:
            validity = True
        else:
            validity = False

        if validity:
            sub = "".join(self._digits) + "".join(self._operators) + "[]{}()."
            sub_with = "0123456789=+-*/%<>*+" + "()()()."

            trans_table = str.maketrans(sub, sub_with)
            exp = expression.translate(trans_table)

            try:
                result = eval(exp)

            except (SyntaxError, TypeError) as e:
                return f"Invalid Syntax. Try again."

            else:
                return result

    def bengali_to_bengali(self, expression: str):
        exp_len = len(expression)
        temp = 0

        for i in expression:
            if i in self._digits or i in self._operators or i in ["(", ")", "{", "}", "[", "]", "."]:
                temp += 1

        if exp_len == temp:
            validity = True
        else:
            validity = False

        if validity:
            sub = "".join(self._digits) + "".join(self._operators) + "[]{}()."
            sub_with = "0123456789=+-*/%<>*+" + "()()()."

            trans_table = str.maketrans(sub, sub_with)
            exp = expression.translate(trans_table)

            try:
                result = eval(exp)

            except (SyntaxError, TypeError) as e:
                return f"Invalid Syntax. Try again."

            else:
                sub = "0123456789."
                sub_with = "".join(self._digits) + "."
                trans_table = str.maketrans(sub, sub_with)
                result_in_bengali = str(result).translate(trans_table)
                return result_in_bengali


if __name__ == '__main__':

    ben_math = Evaluator()

    exp1 = "((৫+৬+৮)/৭*৪-৯%৩)"
    new_ex = ben_math.bengali_to_english(exp1)
    print(new_ex)

    exp2 = "৩*(৩+৬)"
    new_ex2 = ben_math.bengali_to_bengali(exp2)
    print(new_ex2)
