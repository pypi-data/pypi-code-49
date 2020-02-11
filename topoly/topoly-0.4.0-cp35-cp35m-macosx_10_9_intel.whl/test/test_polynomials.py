from topoly import *

# importing the file 31.xyz. It is closed knot.
curve = 'data/31.xyz'

def test_polynomials():
    polynomials = {}
    # calculating the polynomials
    polynomials['Alexander'] = alexander(curve, closure=Closure.CLOSED, translate=True)
    # print(alexander(curve, closure=Closure.CLOSED, poly_reduce=False, boundaries=[(0,20), (15,60), (18,90), (-3,50)], hide_trivial=False))
    polynomials['Conway'] = conway(curve, closure=Closure.CLOSED, translate=True)
    # print(conway(curve, closure=Closure.CLOSED, poly_reduce=False))
    polynomials['Jones'] = jones(curve, closure=Closure.CLOSED, translate=True)
    # print(jones(curve, closure=Closure.CLOSED, poly_reduce=False))
    polynomials['HOMFLY-PT'] = homfly(curve, closure=Closure.CLOSED, translate=True)
    # print(homfly(curve, closure=Closure.CLOSED, poly_reduce=False))
    polynomials['Kauffman bracket'] = kauffman_bracket(curve, closure=Closure.CLOSED, translate=True)
    # print(kauffman_bracket(curve, closure=Closure.CLOSED, poly_reduce=False))
    polynomials['Kauffman polynomial'] = kauffman_polynomial(curve, closure=Closure.CLOSED, translate=True)
    # print(kauffman_polynomial(curve, closure=Closure.CLOSED, poly_reduce=False))
    polynomials['BLM/Ho'] = blmho(curve, closure=Closure.CLOSED, translate=True)
    # print(blmho(curve, closure=Closure.CLOSED, poly_reduce=False))
    polynomials['Yamada'] = yamada(curve, closure=Closure.CLOSED, translate=True)
    # print(yamada(curve, closure=Closure.CLOSED, poly_reduce=False))



    # Printing the polynomials and matching knot from the dictionary. We need the short version of the polynomial
    print("Knot polynomials for the 3_1 knot:")
    for key in polynomials.keys():
        #print(key, polynomials[key], find_matching(polynomials[key]))
        print(key, polynomials[key])
        assert polynomials[key].get('3_1') == 1.0

test_polynomials()