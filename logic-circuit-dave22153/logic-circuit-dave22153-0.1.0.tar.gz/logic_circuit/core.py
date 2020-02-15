"""Core circuit classes and logic.
"""


## Whether to dynamically create circuit inputs A-Z.
CREATE_DYNAMIC_INPUT_CLASSES = True


class LogicMetaNode(type):
    """A node in a logic tree, possible with children.
    """

    def __str__(cls):
        try:
            # Working with an instance with inputs.
            num_inputs = len(cls.inputs)

        except AttributeError:
            try:
                # Working with a class by itself.
                return cls.__name__

            except AttributeError:
                # Working with an instance with no children.
                # Should not encounter this in a tree.
                return type(cls).__name__

        else:
            # Recursively find all operations under this node instance.
            if num_inputs == 1:
                return "(%s %s)" % (type(cls), cls.inputs[0])


            elif num_inputs == 2:
                return "(%s)" % (
                    str.join(" %s " % type(cls), map(str,cls.inputs)))

    ## Return a new AND gate with two sides as inputs.
    __and__ = lambda cls, other: And(cls, other)
    ## Return a new AND gate with two sides as inputs.
    __or__ = lambda cls, other: Or(cls, other)
    ## Return a new NOT gate with one input.
    __invert__ = lambda cls: Not(cls)
    ## Return a new XOR gate with two sides as inputs.
    __xor__ = lambda cls, other: Xor(cls, other)

    def __new__(cls, name, bases, dct):
        """Constructor for new classes.
        """

        # Assign given operators to the class.
        logic_options = dct.pop("__logiccircuit__", None)
        if logic_options is not None:
            all(map(lambda kvp: setattr(cls, *kvp), logic_options.items()))

        # Construct a class and return it.
        a = super().__new__(cls, name, bases, dct)
        a.__str__ = cls.__str__
        a.__and__ = cls.__and__
        a.__or__ = cls.__or__
        a.__invert__ = cls.__invert__
        a.__xor__ = cls.__xor__
        return a


def logicable(cls):
    """Decorator for classes that can be part of a logic circuit.
    """

    # Define any additional class level attribute here.
    my_opts = {}

    dct = dict(cls.__dict__)
    dct["__logiccircuit__"] = my_opts
    return LogicMetaNode(cls.__name__, (cls,), dct)


@logicable
class LogicGateBase:
    """Internal base class for representing logic gates.

    Do not use directly. Instead use bitwise operators, eg,
    `A & (B | C)`
    """

    def __init__(self, *inputs):
        self.inputs = inputs

    def evaluate(self):
        """Return result of circuit nodes into this node.
        """
        return 0


class LogicGate_OneParam(LogicGateBase):
    """Internal class for gates with one input.
    """

    _eval_one_param = lambda self, v: 0

    def evaluate(self):
        try:
            value = self.inputs[0].evaluate()
        except (AttributeError, IndexError):
            return 0
        else:
            return self._eval_one_param(value)


class LogicGate_TwoParams(LogicGateBase):
    """Internal class for gates with two inputs.
    """

    _eval_two_params = lambda self, l, r: 0

    def evaluate(self):
        try:
            left = self.inputs[0].evaluate()
            right = self.inputs[1].evaluate()
        except (AttributeError, IndexError):
            return 0
        else:
            return self._eval_two_params(left, right)


class And(LogicGate_TwoParams):
    """Internal logical AND gate."""
    _eval_two_params = lambda self, l, r: l & r


class Or(LogicGate_TwoParams):
    """Internal logical OR gate."""
    _eval_two_params = lambda self, l, r: l | r


class Not(LogicGate_OneParam):
    """Internal logical NOT gate."""
    _eval_one_param = lambda self, v: int(not v)


class Xor(LogicGate_TwoParams):
    """Internal logical XOR gate."""
    _eval_two_params = lambda self, l, r: l ^ r


@logicable
class LogicVariableBase:
    """Base class for variable as input to a circuit.

    Use as many times as you like in your circuit expression. Each
    variable will get its own switch for changing its state, and all
    instances of the same variable will be controlled by the same
    switch.

    Modify each child variable's state using the state variable or use
    the switch function to invert state. This is reflected across all
    uses of the variable. Default state is 0.

    ```
    A.state = 1  # A.evaluate() = 1
    B.switch()  # B.evaluate() = 1
    B.switch()  # B.evaluate() = 0
    ```
    """

    ## State of this input across all uses (0 or 1).
    state = 0

    @classmethod
    def evaluate(cls): return cls.state

    @classmethod
    def switch(cls): cls.state = int(not cls.state)


def declare_dynamic_inputs(dct):
    """Declares classes A-Z usable in circuit expressions.

    Use `globals()` as dct to put variable in global scope.
    """

    dct.update({
        n: type(n, (LogicVariableBase,),
            { "__doc__": "Logical input variable called %s." % n
        }) for n in map(chr, range(65, 97))
    })
# Variables will be created in this module's scope.
if CREATE_DYNAMIC_INPUT_CLASSES: declare_dynamic_inputs(globals())

def parse_circuit(circuit_string):
    """Return the parsed circuit using A-Z variables.

    Currently parentheses (()) are unsupported.

    Input is validated by the following rules:
    The expression must start with a variable or not (~).
    Spaces ( ) are allowed between symbols.
    A variable (A-Z) or not (~) must follow each operator.
    Multiple nots (~~) are allowed.
    Variables are: A-Z (capital only). Operators are: &|~^.

    Warning: Uses Python's built in `eval` function which could have
    undesired effects (although only used if validation passed).

    Returns the parsed circuit or False if validation failed.
    """

    # Perform validation on input.
    allowed_operators = set("&|~^")
    allowed_variables = set(map(chr, range(65, 91)))

    # Remove spaces.
    circuit_string = circuit_string.replace(" ", "")
    if circuit_string == "":
        # Can't evaluate empty string.
        return False

    last_symbol = None
    symbol_operator = 0
    symbol_variable = 1
    for char in circuit_string:
        if (char in allowed_operators
            and ((last_symbol is None and char == "~") # Can start with not
                or last_symbol == symbol_variable
                or char == "~"
        )):
            last_symbol = symbol_operator
            continue

        elif (char in allowed_variables
            and (last_symbol is None
                or last_symbol == symbol_operator)
        ):
            last_symbol = symbol_variable
            continue

        # Unexpected symbol encountered
        return False

    if last_symbol == symbol_operator:
        # Cannot end with an operator.
        return False

    return eval(circuit_string)

def main():
    my_circuit = A | B

    A.state = 0
    B.state = 1
    A.switch()
    print("%s = %s" % (my_circuit, my_circuit.evaluate()))

if __name__ == '__main__':
    main()
