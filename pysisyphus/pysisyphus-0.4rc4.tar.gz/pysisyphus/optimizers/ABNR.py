#!/usr/bin/env python3

# [1] 

import numpy as np

from pysisyphus.optimizers.Optimizer import Optimizer
# from pysisyphus.intcoords.findbonds import get_bond_mat
# from pysisyphus.optimizers.step_restriction import scale_by_max_step


class ABNR(Optimizer):

    def __init__(self, geometry, **kwargs):
        super().__init__(geometry, **kwargs)

        self.alpha = 1.0
        self.hist_max = 5

    def optimize(self):
        gradient = self.geometry.gradient
        energy = self.geometry.energy
        self.forces.append(-gradient)
        self.energies.append(energy)
        self.log(f"norm(forces)={np.linalg.norm(gradient):.4e}")


        if len(self.forces) > 4:
            old_coords = self.coords[-self.hist_max-1:-1]
            old_grads = -np.array(self.forces[-self.hist_max-1:-1])
            grad_diffs = old_grads - gradient
            coord_diffs = old_coords - self.geometry.coords
            rhs = -np.einsum("ij,j->i", coord_diffs, gradient)
            # mat = np.einsum("ij,", coord_diffs, grad_diffs)
            mat = coord_diffs @ grad_diffs.T
            m = np.zeros_like(mat)
            for i, cd in enumerate(coord_diffs):
                for j, gd in enumerate(grad_diffs):
                    m[i,j] = cd.dot(gd)

            import pdb; pdb.set_trace()
        else:
            # SD step
            self.log("Took pure steepest descent step.")
            step = self.alpha * -gradient


        # scale_by_max_step(step, self.trust_radius)

        return step
