import mdtraj as mdt
from logging import log
from extasycoco import complement

t = mdt.load('1cfc.dcd', top='1cfc.pdb')
print(t)
t_comp_crude = complement(t, selection='mass > 2', npoints=10, refine=False)
print(t_comp_crude)
t_comp_refined = complement(t, selection='mass > 2', npoints=10, refine=True)
print(t_comp_refined)
