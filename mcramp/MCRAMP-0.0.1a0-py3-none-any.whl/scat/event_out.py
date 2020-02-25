from .sprim import SPrim

import numpy as np
import pyopencl as cl
import pyopencl.array as clarr

class SEventOut(SPrim):

    def __init__(self, filename, idx=0, ctx=0, **kwargs):
        self.idx = np.uint32(idx)
        self.ctx = ctx
        self.filename = filename

    def scatter_prg(self, queue, N, neutron_buf, intersection_buf, iidx_buf):
        mf               = cl.mem_flags
        self.neutrons = np.zeros((N, ), dtype=clarr.vec.float16)

        cl.enqueue_copy(queue, self.neutrons, neutron_buf).wait()
        # np.savetxt(self.filename, self.neutrons)