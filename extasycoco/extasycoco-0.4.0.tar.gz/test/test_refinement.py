import mdtraj as mdt
from extasycoco import refinement

t = mdt.load('1cfc.dcd', top='1cfc.pdb')

refiner = refinement.Refiner()
refiner.fit(t.xyz)
print(refiner.d_thresh)
xnew = refiner.transform(t.xyz[0])
print(t)
