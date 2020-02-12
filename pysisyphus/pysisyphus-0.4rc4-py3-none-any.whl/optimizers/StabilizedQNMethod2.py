#!/usr/bin/env python3

# [1] https://aip.scitation.org/doi/pdf/10.1063/1.4905665?class=pdf

import numpy as np

from pysisyphus.optimizers.Optimizer import Optimizer


class StabilizedQNMethod(Optimizer):

    def __init__(self, geometry, alpha=0.1, eps=1e-4, **kwargs):
        super().__init__(geometry, **kwargs)

        self.alpha = alpha
        self.eps = eps

        self.step_norms = list()
        self.steps_normed = list()
        self.grad_diffs = list()

    def prepare_opt(self):
        pass

    @property
    def n_hist(self):
        return len(self.steps_normed)

    def precondition_gradient(self):
        # Overlap matrix
        # As self.steps_normed is a list and not an array we can't
        # easily transpose it. So we swap jk to kj.
        # The call with transposed self.steps_normed would be
        #    np.einsum("ij,jk->ik", self.steps_normed, self.steps_normed.T)
        S = np.einsum("ij,kj->ik", self.steps_normed, self.steps_normed)
        w, v = np.linalg.eigh(S)
        # Significant subspace indices
        significant = (w/w.max()) > self.eps
        ndim = np.sum(significant)
        eigvals = w[significant]
        eigvecs = v[:,significant]
        norm_fac = 1/eigvals**(1/2)
        # Transform steps and gradient differences to significant subspace
        # ss = np.zeros((self.coords[-1].size, ndim))
        # for i in range(ndim):
            # tmp = 0
            # for k, sn in enumerate(self.steps_normed):
                # tmp += eigvecs[k,i] * sn
            # tmp *= (1/eigvals[i])**(0.5)
            # ss[:,i] = tmp
        # Eq. (8) in [1]
        sig_subspace = norm_fac * \
                       np.einsum("ki,kj->ji", eigvecs, self.steps_normed)

        # Eq. (11) in [1]
        eigvecs_weighted = eigvecs / np.array(self.step_norms)[:, None]
        sig_grad_diffs = norm_fac * \
                         np.einsum("ki,kj->ji", eigvecs_weighted, self.grad_diffs)
        # gd = np.zeros((self.coords[-1].size, ndim))
        # for i in range(ndim):
            # tmp = 0
            # for k, gd_ in enumerate(self.grad_diffs):
                # tmp += eigvecs[k,i] * gd_ / self.step_norms[k]
            # tmp *= (1/eigvals[i])**(0.5)
            # gd[:,i] = tmp
        # sig_grad_diffs = gd

        # h = np.zeros((ndim, ndim))
        # for i, gd in enumerate(sig_grad_diffs.T):
            # for j, ss in enumerate(sig_subspace.T):
                # h[i,j] = gd.dot(ss)

        hess_approx = np.einsum("ij,ik->jk", sig_grad_diffs, sig_subspace)
        hess_approx = (hess_approx + hess_approx.T) / 2
        hess_w, hess_v = np.linalg.eigh(hess_approx)

        # Eq. (15)
        proj_v = np.einsum("ki,jk->ji", hess_v, sig_subspace)
        proj_dg = np.einsum("ki,jk->ji", hess_v, sig_grad_diffs)
        residuals = np.linalg.norm(proj_dg - hess_w*proj_v, axis=0)
        # pv = np.zeros((self.coords[-1].size, ndim))
        # for i in range(ndim):
            # tmp = 0
            # for k, ss_ in enumerate(sig_subspace.T):
                # tmp += hess_v[k,i] * ss_
            # pv[:,i] = tmp
        eigvals_mod = np.sqrt(hess_w**2 + residuals**2)
        cur_grad = -self.forces[-1]
        precon_grad = np.einsum("i,j,ij,ij->i", cur_grad, 1/eigvals_mod, proj_v, proj_v)

        # projector = proj_v @ proj_v.T
        projector = proj_v.dot(proj_v.T)
        perp_projector = np.eye(cur_grad.size) - projector
        perp_grad = perp_projector.dot(cur_grad)
        grad_ovlp = (cur_grad.dot(precon_grad)
                     / np.linalg.norm(cur_grad) / np.linalg.norm(precon_grad)
        )
        if grad_ovlp > 0.2:
            self.alpha *= 1.1
        else:
            self.alpha *= 0.85
        self.log("Overlap between total gradient and preconditioned gradient "
                 "is {grad_ovlp:.4f}. New alpha={self.alpha:.4f}.")
        tot_precon_gradient = precon_grad + self.alpha*perp_grad
        return tot_precon_gradient

    def optimize(self):
        forces = self.geometry.forces
        energy = self.geometry.energy
        self.forces.append(forces)
        self.energies.append(energy)

        if len(self.forces) > 1:
            grad_diff = -self.forces[-1] + self.forces[-2]
            self.grad_diffs.append(grad_diff)

        # if len(self.steps_normed) > 2:
        if False:
            precon_grad = self.precondition_gradient()
            step = -precon_grad
        else:
            dir_ = forces / np.linalg.norm(forces)
            step = forces
            if np.linalg.norm(step) > 0.1:
                step = self.alpha * dir_


        step_norm = np.linalg.norm(step)
        self.step_norms.append(step_norm)
        step_normed = step / step_norm
        self.steps_normed.append(step_normed)

        return step
        # import pdb; pdb.set_trace()
