#!/usr/bin/env python

import os
import sys
import random

import radical.pilot as rp


# ------------------------------------------------------------------------------
#
if __name__ == '__main__':

    with rp.Session() as session:

        pmgr    = rp.PilotManager(session=session)
        pd_init = {'resource'      : 'local.localhost',
                   'runtime'       : 60,
                   'exit_on_error' : True,
                   'cores'         : 4
                  }
        pdesc = rp.ComputePilotDescription(pd_init)
        pilot = pmgr.submit_pilots(pdesc)
     #  pilot.wait(rp.PMGR_ACTIVE)
     #  print('pilot is active')
        umgr  = rp.UnitManager(session=session)
        umgr.add_pilots(pilot)

        n    = 256
        cuds = list()
        for i in range(0, n):

            cud = rp.ComputeUnitDescription()
            cud.executable       = '%s/examples/hello_rp.sh' % os.getcwd()
            cud.arguments        = [random.randint(1, 10) * 0]
            cud.gpu_processes    = 0  # random.randint(0, 2)
            cud.cpu_processes    = 1  # random.randint(1, 8)
            cud.cpu_threads      = 1  # random.randint(1, 8)
            cud.gpu_process_type = rp.POSIX
            cud.cpu_process_type = rp.POSIX
            cud.cpu_thread_type  = rp.POSIX
            cuds.append(cud)

        umgr.submit_units(cuds)
        umgr.wait_units()

        sys.exit()

        n    = 256
        cuds = list()
        for i in range(0, n):

            cud = rp.ComputeUnitDescription()
            cud.executable       = '%s/examples/hello_rp.sh' % os.getcwd()
            cud.arguments        = [random.randint(1, 10) * 0]
            cud.gpu_processes    = 0  # random.randint(0, 2)
            cud.cpu_processes    = 1  # random.randint(1, 8)
            cud.cpu_threads      = 1  # random.randint(1, 8)
            cud.gpu_process_type = rp.POSIX
            cud.cpu_process_type = rp.POSIX
            cud.cpu_thread_type  = rp.POSIX
            cuds.append(cud)

        umgr.submit_units(cuds)
        umgr.wait_units()


# ------------------------------------------------------------------------------

