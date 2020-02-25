#!/usr/bin/env python
"""Extract info from DALTON/SIRIUS restart file stored under label BASINFO"""

import sys
import numpy
from fortran_binary import FortranBinary

class BasInfo(object):
    """Simple class for BASINFO data"""
    label = "BASINFO"
    def __init__(self, name="SIRIUS.RST"):
        self.name = name
        sirrst = FortranBinary(name)
        sirrst.find(BasInfo.label)
        sirrst.next()
        self.nsym, = sirrst.readbuf(1, 'i')
        self.nbas = numpy.array(sirrst.readbuf(8, 'i'))[:self.nsym]
        self.norb = numpy.array(sirrst.readbuf(8, 'i'))[:self.nsym]
        self.nrhf = numpy.array(sirrst.readbuf(8, 'i'))[:self.nsym]
        self.ioprhf, = sirrst.readbuf(1,'i')
        sirrst.close()

    def __repr__(self):
        """Print method for BasInfo objects"""
        printv = lambda v:  len(v)*"%3d" % tuple(v)
        retstr = ""
        retstr += "NSYM   : %3d\n" % self.nsym
        retstr += "NBAS   : %s\n" % printv(self.nbas)
        retstr += "NORB   : %s\n" % printv(self.norb)
        retstr += "NRHF   : %s\n" % printv(self.nrhf)
        retstr += "IOPRHF : %3d\n" % self.ioprhf
        return retstr

    @property
    def nbast(self):
        """Return total number of AO"""
        return self.nbas[:self.nsym].sum()

    @property
    def norbt(self):
        """Return total number of MO"""
        return self.norb[:self.nsym].sum()

    @property
    def ncmot(self):
        """Return numboer of MO coefficients"""
        return sum([i*j for i, j in zip(self.nbas, self.norb)])

def main():
    """main routine"""
    try:
        print(BasInfo(sys.argv[1]))
    except IndexError:
        print("Usage: %s [path]/SIRIUS.RST" % sys.argv[0])
        sys.exit(1)

if __name__ == "__main__":#pragma: no cover
    sys.exit(main())
