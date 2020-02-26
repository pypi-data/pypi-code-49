def rev_comp(seq):
    comp = str.maketrans("ATGC", "TACG")
    return seq.translate(comp)[::-1]
