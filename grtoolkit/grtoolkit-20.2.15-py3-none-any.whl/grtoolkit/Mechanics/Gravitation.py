from grtoolkit.Python import dictionary_add_modify
from grtoolkit.Math import solveEqs

def gravitationAttraction(find="F_g", printEq=False, **kwargs):
    """variables:
            F_g = force of attraction due to gravity
            G = 6.67e-11 N*m**2/kg**2
            m1, m2 = mass1, mass2
            r = distance between masses"""
    dictionary_add_modify(kwargs,G=6.67e-11)
    eq = list()
    eq.append("Eq(F_g,G*m1*m2/r**2)")
    return solveEqs(eq, find, printEq=printEq, **kwargs)


