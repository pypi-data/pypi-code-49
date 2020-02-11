from topoly import make_surface, lasso_type, GLN

# importing the file 31.xyz. It is closed knot.
curve1 = 'data/lasso_01.xyz'


def test_lassos():
    S = make_surface(curve1, loop_indices=[1, 35])
    print(S)

    res = lasso_type('data/lasso_01.xyz', loop_indices=[1, 35])
    print(res)
    print(type(res))

    loop = [[0,0,0,0],[1,0,1,0],[2,1,1,-1]]
    tail = [[0,1,1,1],[1,3,7,1],[2,7,4,0],[3,5,2,3]]

    #M = GLN.gln_matrix(loop, tail)
    #print(M)

    #res = gln_max(loop, tail, chain1_beg = -1, chain1_end = -1, chain2_beg = -1,
    #        chain2_end = -1, density = -1, precision_out = 3)
    #print("max:",res)

test_lassos()
