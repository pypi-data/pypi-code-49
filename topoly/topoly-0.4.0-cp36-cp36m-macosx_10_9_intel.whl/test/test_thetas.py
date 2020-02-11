from topoly import *

# importing the file 31.xyz. It is closed knot.
#curve31 = import_coords('data/31.xyz')
#curve = import_coords('data/2atg.xyz')
# IMPORTOWANIE TAKIE JUZ NIE DZIALA

def test_thetas():
    polynomials = {}
    polynomials['Alexander'] = alexander('data/31.xyz', closure=Closure.CLOSED, poly_reduce=False, translate=True)
 #   polynomials['Yamada'] = yamada('data/31.xyz', closure=Closure.CLOSED, poly_reduce=False, translate=True)

    # Printing the polynomials and matching knot from the dictionary. We need the short version of the polynomial
 #   print("Knot polynomials for the 3_1 knot:")
    for key in polynomials.keys():
        #print(key, polynomials[key], find_matching(polynomials[key]))
        print(key, polynomials[key])
#        assert polynomials[key].get('3_1')==1.0

test_thetas()