"""
Fortran
=====
Fortran code used to build package extensions.
"""

try:
    # for local testing
    from . import types
    from . import ran_num_gen
    from . import spcl_fnc
    from . import dist
except:
    # when installed
    pass

# Fortran Conventions
# subroutines return none
# functions return something
# use return statements for clarity

# Style guides
# https://www.clawpack.org/v5.2.1/pyclaw/rulesProposal.html
# https://www.fortran.com/Fortran_Style.pdf
# https://www.fortran90.org/src/best-practices.html

# Tips and Tricks
# * don't vectorize within functions, its a waste of time at this level
# * "Symbol not found: _ran0_" or "Expected in: flat namespace" is a usually a
#   naming issue in your code
