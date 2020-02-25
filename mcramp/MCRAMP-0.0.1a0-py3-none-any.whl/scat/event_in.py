from .sprim import SPrim

import numpy as np
import pyopencl as cl
import pyopencl.array as clarr

class SEventIn(SPrim):

    def __init__(self, filename, idx=0, ctx=0, **kwargs):
        self.idx = np.uint32(idx)
        
        self.filename = filename

    def scatter_prg(self, queue, N, neutron_buf, intersection_buf, iidx_buf):
        mf               = cl.mem_flags
        self.neutrons = np.zeros((N,), dtype=np.float32)
        self.neutrons_cl    = cl.Buffer(ctx,
                                     mf.READ_WRITE | mf.COPY_HOST_PTR,
                                     hostbuf=self.neutrons)

        cl.enqueue_copy(queue, self.neutrons, self.neutrons_cl).wait()
        