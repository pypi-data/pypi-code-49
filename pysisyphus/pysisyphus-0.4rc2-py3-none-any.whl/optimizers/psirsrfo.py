#!/usr/bin/env python3

from math import sqrt, fabs
from . import optparams as op
from . import v3d

import numpy as np
np.set_printoptions(suppress=True, precision=4, linewidth=120)

rfo_normalization_max = 100
rsrfo_alpha_max = 1e8

STEPS = list()


def DE_projected(model, step, grad, hess):
    """ Compute anticpated energy change along one dimension """
    if model == 'NR':
        return (step * grad + 0.5 * step * step * hess)
    elif model == 'RFO':
        return (step * grad + 0.5 * step * step * hess) / (1 + step * step)
    else:
        raise OptError("DE_projected does not recognize model.")

def symmMatEig(mat):
    eigvals, eigvecs = np.linalg.eigh(mat)
    return eigvals, eigvecs.T


def asymmMatEig(mat):
    """Compute the eigenvalues and right eigenvectors of a square array.
    Wraps numpy.linalg.eig to sort eigenvalues, put eigenvectors in rows, and suppress complex.
    Parameters
    ----------
    mat : ndarray
        (n, n) Square matrix to diagonalize.
    Returns
    -------
    ndarray, ndarray
        (n, ), (n, n) sorted eigenvalues and normalized corresponding eigenvectors in rows.
    Raises
    ------
    OptError
        When eigenvalue computation does not converge.
    """
    try:
        evals, evects = np.linalg.eig(mat)
    except np.LinAlgError as e:
        raise OptError("asymmMatEig: could not compute eigenvectors") from e

    idx = np.argsort(evals)
    evals = evals[idx]
    evects = evects[:, idx]

    return evals.real, evects.real.T


def absMax(V):
    return max(abs(elem) for elem in V)


def Dq_RFO(E, fq, H, trust=0.3, rfo_root=0):

    dim = len(fq)
    dq = np.zeros((dim), float)  # To be determined and returned.
    trust = trust
    max_projected_rfo_iter = 25  # max. # of iterations to try to converge RS-RFO
    rfo_follow_root = False  # whether to follow root

    # Determine the eigenvectors/eigenvalues of H.
    Hevals, Hevects = symmMatEig(H)
    np.savetxt("psi_eigvals", Hevals)

    # Build the original, unscaled RFO matrix.
    RFOmat = np.zeros((dim + 1, dim + 1), float)
    for i in range(dim):
        for j in range(dim):
            RFOmat[i, j] = H[i, j]
        RFOmat[i, dim] = RFOmat[dim, i] = -fq[i]

    symm_rfo_step = False
    SRFOmat = np.zeros((dim + 1, dim + 1), float)  # For scaled RFO matrix.
    converged = False
    dqtdq = 10  # square of norm of step
    alpha = 1.0  # scaling factor for RS-RFO, scaling matrix is sI

    last_iter_evect = np.zeros((dim), float)

    # Iterative sequence to find alpha
    alphaIter = -1
    while not converged and alphaIter < max_projected_rfo_iter:
        alphaIter += 1

        # If we exhaust iterations without convergence, then bail on the
        #  restricted-step algorithm.  Set alpha=1 and apply crude scaling instead.
        if alphaIter == max_projected_rfo_iter:
            logger.warning("\tFailed to converge alpha. Doing simple step-scaling instead.")
            alpha = 1.0
            
        print("alphaIter", alphaIter, "alpha", f"{alpha:.6f}")
        # Scale the RFO matrix.
        for i in range(dim + 1):
            for j in range(dim):
                SRFOmat[j, i] = RFOmat[j, i] / alpha
            SRFOmat[dim, i] = RFOmat[dim, i]

        # Find the eigenvectors and eigenvalues of RFO matrix.
        SRFOevals, SRFOevects = asymmMatEig(SRFOmat)

        # Do intermediate normalization.  RFO paper says to scale eigenvector
        # to make the last element equal to 1. Bogus evect leads can be avoided
        # using root following.
        for i in range(dim + 1):
            # How big is dividing going to make the largest element?
            # Same check occurs below for acceptability.
            if fabs(SRFOevects[i][dim]) > 1.0e-10:
                tval = absMax(SRFOevects[i] / SRFOevects[i][dim])
                if tval < rfo_normalization_max:
                    for j in range(dim + 1):
                        SRFOevects[i, j] /= SRFOevects[i, dim]
                else:
                    # print(f"dont scale sfro eigenvector {i}")
                    pass
            else:
                # raise Exception("yoho")
                # print("yoho")
                pass

        # Use input rfo_root
        # If root-following is turned off, then take the eigenvector with the
        # rfo_root'th lowest eigvenvalue. If its the first iteration, then do the same.
        # In subsequent steps, overlaps will be checked.
        # if not rfo_follow_root or len(STEPS) < 2:
        if not rfo_follow_root:

            # Determine root only once at beginning ?
            if alphaIter == 0:
                for i in range(rfo_root, dim + 1):
                    # Check symmetry of root.
                    dq[:] = SRFOevects[i, 0:dim]
                    
                    # Check normalizability of root.
                    if fabs(SRFOevects[i][dim]) < 1.0e-10:  # don't even try to divide
                        continue
                    tval = absMax(SRFOevects[i] / SRFOevects[i][dim])
                    if tval > rfo_normalization_max:
                        continue
                    rfo_root = i  # This root is acceptable.
                    break
                # Save initial root. 'Follow' during the RS-RFO iterations.
                rfo_follow_root = True
        else:  # Do root following.
            # Find maximum overlap. Dot only within H block.
            dots = np.array(
                [v3d.dot(SRFOevects[i], last_iter_evect, dim) for i in range(dim)], float)
            bestfit = np.argmax(dots)
            if bestfit != rfo_root:
                logger.info("\tRoot-following has changed rfo_root value to %d."
                            % (bestfit + 1))
                rfo_root = bestfit
        # print("using root", rfo_root)

        last_iter_evect[:] = SRFOevects[rfo_root][0:dim]  # omit last column on right

        dq[:] = SRFOevects[rfo_root][0:dim]  # omit last column

        dqtdq = np.dot(dq, dq)
        # If alpha explodes, give up on iterative scheme
        if fabs(alpha) > rsrfo_alpha_max:
            converged = False
            alphaIter = max_projected_rfo_iter - 1
        elif sqrt(dqtdq) < (trust + 1e-5):
            converged = True

        Lambda = -1 * v3d.dot(fq, dq, dim)
        
        # Calculate derivative of step size wrt alpha.
        ftrans = Hevects.dot(fq)
        tval = 0
        tval_ = 0
        for i in range(dim):
            tval += (pow(v3d.dot(Hevects[i], fq, dim), 2)) / (pow(
                (Hevals[i] - Lambda * alpha), 3))
            tval_ += (pow(ftrans[i], 2)) / (pow(
                (Hevals[i] - Lambda * alpha), 3))
        denum = ftrans**2
        denom = (Hevals - Lambda*alpha)**3
        quot = np.sum(denum/denom)
        # print(f"quot={quot:.6f}")

        rest = 2 * Lambda / (1 + alpha * dqtdq)
        analyticDerivative = 2 * Lambda / (1 + alpha * dqtdq) * tval
        # print("analyticalDeriv", analyticDerivative)
        # import pdb; pdb.set_trace()

        # Calculate new scaling alpha value.
        # Equation 20, Besalu and Bofill, Theor. Chem. Acc., 1998, 100:265-274
        alpha += 2 * (trust * sqrt(dqtdq) - dqtdq) / analyticDerivative

    # end alpha RS-RFO iterations

    # Get norm |dq|, unit vector, gradient and hessian in step direction
    # TODO double check Hevects[i] here instead of H ? as for NR
    rfo_dqnorm = sqrt(np.dot(dq, dq))
    rfo_u = dq.copy() / rfo_dqnorm
    rfo_g = -1 * np.dot(fq, rfo_u)
    rfo_h = np.dot(rfo_u, np.dot(H, rfo_u))
    DEprojected = DE_projected('RFO', rfo_dqnorm, rfo_g, rfo_h)

    # Scale fq into aJ for printing
    # For now, saving RFO unit vector and using it in projection to match C++ code,
    # could use actual Dq instead.
    dqnorm_actual = sqrt(np.dot(dq, dq))

   
    if sqrt(np.dot(dq, dq)) > 10 * trust:
        raise AlgError("opt.py: Step is far too large.")

    STEPS.append(dq)
    dq_norm = np.linalg.norm(dq)
    print("norm(dq): ", dq_norm)
    return dq

