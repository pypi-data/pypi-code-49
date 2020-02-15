"""My logic circuit parser and evaluation utility.

Implements bitwise operator overloads for circuit expression parsing,
so you can write something like `A & B | ~C` and it will be evaluated
into a circuit like `((A AND B) OR (NOT C))`.

Example usage of logic circuit module
```
>>> # Create a circuit with bitwise operators.
>>> from logic_circuit.params import A, B
>>> my_circuit = ~A & B
>>>
>>> # Set variable states (default 0)
>>> B.state = 1  # A: 0, B: 1
>>> A.switch()  # A: 1, B: 1
>>>
>>> print("%s = %s" % (my_circuit, my_circuit.evaluate()))
(Not (A And B)) = 0
```


It is also possible to parse a circuit expressed in a string. This can
be done using the `parse_circuit` function. However, this currently
does not support parentheses in the expression and internally will use
Python's eval function instead of a dedicated logic circuit parser.

Example of parsing a circuit from a string
```
>>> from logic_circuit import parse_circuit
>>> print(parse_circuit("~A & B"))
(Not(A) And B)
```


To evaluate a circuit using the current state of variables, use the
`evaluate` method on any node. It will recursively evaluate its input
nodes and return the result as either a 0 or 1.

Example of evaluating a circuit
```
>>> from logic_circuit.params import A, B
>>> my_circuit = A & B
>>> my_circuit.evaluate()
0
```


The state of any variable may be changed in two ways: setting the state
variable directly to either 0 or 1, or using the `switch` method to
invert its current state (1 becomes 0 and vice versa). The default
state of all variables is zero. All instances of the variable will be
affected, including uses across different circuits. However, variables
defined from `parse_circuit` are separate from those defined in
`logic_circuit.params`. The `parse_circuit` function uses classes that
were declared dynamically in the `logic_circuit.core` module.

Example of changing variable state
```
>>> from logic_circuit.params import A
>>> A.state = 1
>>> A.state
1
>>> A.switch()
>>> A.state
0
```
"""

from logic_circuit.core import parse_circuit
