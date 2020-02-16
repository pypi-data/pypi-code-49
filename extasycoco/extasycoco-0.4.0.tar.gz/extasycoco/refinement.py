# refinement.py - 'SHAKE"-like routines to improve geometry.
from .fast import make_dx
import mdtraj as mdt
import numpy as np
from sklearn.decomposition import PCA
from scipy.spatial.distance import pdist

def procrustes(X, max_its=10, drmsd=0.01):
    """
    Procrustes lest-squares fitting of a trajectory.

    Args:
        X: [n_frames, n_atoms, 3] numpy array
        max_its: maximum number of cycles of least-squares fitting
        drmsd: target value for RMSD change before/after fitting cycle.

    Returns:
        [n_frames, n_atoms, 3] numpy array of fitted coordinates
    """
    x_mean = X[0]
    t = mdt.Trajectory(X, None)
    t_oldmean = mdt.Trajectory(x_mean, None)
    t_newmean = mdt.Trajectory(x_mean, None)
    err = drmsd + 1.0
    it = 0
    while err > drmsd and it < max_its:
        it += 1
        t.superpose(t_oldmean)
        t_newmean.xyz = t.xyz.mean(axis=0)
        err = mdt.rmsd(t_oldmean, t_newmean)[0]
        t_oldmean.xyz = t_newmean.xyz
    return t.xyz
    
def xfix(Xin, Dref, pca, known, gtol=0.001, dtol=0.001, max_its=1000):
    """
    SHAKE-style real-space refinement, with adaptive conjugate gradient minimization approach
    
    Args:
        Xin: The original coordinates
        Dref: Target distances, D[known] where D is a condensed distance matrix
        pca: An sklearn PCA model
        known: Boolean matrix, True where values from Dref are the targets
        dtol: stopping criterion for RMD distance violations
        gtol: stopping criterion for the force gradient
        tol: convergence tolerance
        max_its: maximum number of refinement cycles

    Returns:
        Xnew: Optimised coordinates
    """
    
    Dold = pdist(Xin)[known]
    Xold = Xin
    DX = np.zeros_like(Xold)
    C = np.zeros_like(Xold)
    n = len(Xin)
    
    ij = []
    k = -1
    for i in range(n - 1):
        for j in range(i+1, n):
            k += 1
            if known[k]:
                ij.append((i, j))
                C[i] += 1
                C[j] += 1
    C = 1.0 / np.where(C == 0, 1, C)
    grad = gtol + 0.1
    d = dtol + 0.1
    it = 0
    ij = np.array(ij, dtype=np.int)
    DXold = None
    alpha = 1.0
    while it < max_its and grad > gtol and d > dtol:
        it += 1
        dd = 0.5 * (Dref - Dold) / Dold
        DX = make_dx(Xold.astype(np.float32), dd.astype(np.float32), ij)
        DX = DX * C
        if DXold is not None:
            v0 = DXold.flatten()
            v1 = DX.flatten()
            gamma = np.dot(v1, v1)/ np.dot(v0, v0)
            DX = DX + gamma * DXold
        
        DX_embedded = (pca.inverse_transform(pca.transform([pca.mean_ + DX.flatten()])) - pca.mean_).reshape((-1, 3))
        DX = DX - DX_embedded
        Xnew = Xold + DX * alpha
        Dnew = pdist(Xnew)[known]
        newerr = np.linalg.norm(Dref - Dnew)
        
        if DXold is None:
            olderr = newerr + 1.0
        while newerr > olderr:
            alpha = alpha * 0.5
            Xnew = Xold + DX * alpha
            Dnew = pdist(Xnew)[known]
            newerr = np.linalg.norm(Dref - Dnew)
        
        alpha = alpha * 1.1
        DD = Dnew - Dold
        grad = np.linalg.norm(DD) / np.linalg.norm(Dold)
        Dold = Dnew
        Xold = Xnew
        DXold = DX
        olderr = newerr
        d = np.sqrt((DD * DD).mean())
   
    if grad > gtol and d > dtol:
        print('warning: tolerance limit {} not reached in {} iterations'.format(gtol, max_its))
    return Xnew

class Refiner(object):

    def __init__(self, bond_order=6.0, max_its=1000, dtol=0.0001, gtol=0.0001):
        """
        Initialise a Refiner.

        Args:
            bond_order: float, sets the distance variance cutoff to
                        give a total of bond_order * n_atoms bonds.
                        The default value of 6 comes from assuming each
                        atom has 4 bonded neighbours, and each of these
                        has 3 further neighbours, so (4*3/2)  unique bonds.
            max_its:    maximum number of refinement iterations.
            dtol:       stopping criterion for RMD distance violations
            gtol:       stopping criterion for the force gradient
        """
        self.bond_order = bond_order
        self.max_its = max_its
        self.dtol = dtol
        self.gtol = gtol

    def fit(self, X):
        """
        Train the refiner.

        Args:
            X: [N_frames, N_atoms, 3] numpy array of coordinates.
        """
        X_fitted = procrustes(X)
        n_frames = len(X_fitted)
        n_atoms = X_fitted.shape[1]
        self.pca = PCA()
        self.pca.fit(X_fitted.reshape((n_frames, -1)))

        d = np.array([pdist(x) for x in X_fitted])
        d_mean = d.mean(axis=0)
        d_var = d.var(axis=0)
        self.d_thresh = sorted(d_var)[int(n_atoms * self.bond_order)]
        self.restrained = d_var <= self.d_thresh
        self.d_ref = d_mean[self.restrained]

    def transform(self, X):
        """
        Refine sets of coordinates.

        Args:
            X: [n_frames, n_atoms_3] or [n_atoms, 3] numpy array of coordinates

        Returns:
           [n_frames, n_atoms, 3] numpy array of refioned coordinates.
        """
        if len(X.shape) == 2:
            X = np.array([X])
        Xout = []
        for Xc in X:
            Xout.append(xfix(Xc, self.d_ref, self.pca, 
                        self.restrained, self.gtol, self.dtol, self.max_its))
        return np.array(Xout)
