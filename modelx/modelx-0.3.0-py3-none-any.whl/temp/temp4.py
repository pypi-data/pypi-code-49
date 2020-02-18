import modelx as mx

"""
A <- B -> C
|    |    |
X    X*   X
|         |
M         N
"""

mx.new_space("A").new_space("X").new_cells("M")
mx.new_space("B")
mx.new_space("C").new_space("X").new_cells("N")

A = mx.Model1.A
B = mx.Model1.B
C = mx.Model1.C
B.add_bases(A, C)

B.remove_bases(A)

print(hasattr(B.X, "N"))