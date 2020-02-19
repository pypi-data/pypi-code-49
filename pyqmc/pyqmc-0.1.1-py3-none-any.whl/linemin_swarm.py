import numpy as np
import pandas as pd
import scipy
import h5py
import pyqmc


def swarm_hdf(hdf_file, data, attr, configs, wfs):
    import pyqmc.hdftools as hdftools

    if hdf_file is not None:
        with h5py.File(hdf_file, "a") as hdf:
            if "configs" not in hdf.keys():
                hdftools.setup_hdf(hdf, data, attr)
                hdf.create_dataset("configs", configs.configs.shape)
                for i,parameters in enumerate(wfs):
                    hdf.create_group(f"wf{i}")
                    for k, it in parameters.items():
                        hdf.create_dataset(f"wf{i}/" + k, data=it)
            hdftools.append_hdf(hdf, data)
            hdf["configs"][:, :, :] = configs.configs
            for i,parameters in enumerate(wfs):
                for k, it in parameters.items():
                    hdf[f"wf{i}/" + k][...] = it.copy()


class Repulsor:
    def __init__(self, alpha = 1.0, mask = None):
        if mask is None:
            self.mask = np.ones(x_in.shape, dtype=bool)
        else:
            self.mask = mask
        self.alpha = alpha

    def value(self, x_in):
        """ 
        x is nreplica x nparm 

        returns the total penalty 
        """
        x = x_in[:,self.mask] 
        mat = scipy.spatial.distance_matrix(x,x)
        return np.sum(1.0/(mat[mat>0]+self.alpha))*0.5/np.sum(self.mask)

    def gradient(self, x_in):
        """ 
        x is nreplica x nparm 

        returns the derivative with respect to each parameter 
        """
        x = x_in[:, self.mask]
        mat = scipy.spatial.distance_matrix(x,x)
        mask = mat > 0.0
        mat[mask] = -1.0/((mat[mask]+self.alpha)**2*mat[mask])
        d = np.einsum("i,ik -> ik",np.sum(mat,axis=1),x)-np.einsum("ij,jk->ik", mat, x)
        dret = np.zeros(x_in.shape)
        dret[:,self.mask] = d
        return dret/np.sum(self.mask)


class ApproximateOverlap:
    def __init__(self, mask = None):
        if mask is None:
            self.mask = np.ones(x_in.shape, dtype=bool)
        else:
            self.mask = mask
        self.alpha = alpha

    def value(self, x_in):
        """ 
        x is nreplica x nparm 

        returns the total penalty 
        """
        x = x_in[:,self.mask] 
        M = np.einsum('ik,jk->ij', x,x)
        return np.sum(np.abs(M))

    def gradient(self, x_in):
        """ 
        x is nreplica x nparm 

        returns the derivative with respect to each parameter 
        """
        x = x_in[:, self.mask]
        mat = scipy.spatial.distance_matrix(x,x)
        mask = mat > 0.0
        mat[mask] = -1.0/((mat[mask]+self.alpha)**2*mat[mask])
        d = np.einsum("i,ik -> ik",np.sum(mat,axis=1),x)-np.einsum("ij,jk->ik", mat, x)
        dret = np.zeros(x_in.shape)
        dret[:,self.mask] = d
        return dret/np.sum(self.mask)


def gradient_energy_function(x, coords, wf, pgrad_acc, vmc, vmcoptions, warmup):
    newparms = pgrad_acc.transform.deserialize(x)
    for k in newparms:
        wf.parameters[k] = newparms[k]
    data, coords = vmc(wf, coords, accumulators={"pgrad": pgrad_acc}, **vmcoptions)
    df = pd.DataFrame(data)[warmup:]
    en = np.mean(df["pgradtotal"])
    en_err = np.std(df["pgradtotal"]) / np.sqrt(len(df))
    dpH = np.mean(df["pgraddpH"], axis=0)
    dp = np.mean(df["pgraddppsi"], axis=0)
    dpdp = np.mean(df["pgraddpidpj"], axis=0)
    grad = 2 * (dpH - en * dp)
    Sij = dpdp - np.einsum("i,j->ij", dp, dp)  # + eps*np.eye(dpdp.shape[0])
    return coords, df["pgradtotal"].values[-1], grad, Sij, en, en_err


def simple_update(x, tau, grad):
        return  x-tau*grad

def swarm_minimization(
    wf,
    coords,
    pgrad_acc,
    penalizer,
    steprange=0.2,
    warmup=10,
    maxiters=10,
    vmc=None,
    vmcoptions=None,
    lm=None,
    lmoptions=None,
    update=pyqmc.linemin.sr_update,
    update_kws=None,
    verbose=False,
    npts=5,
    hdf_file=None,
    replicas = 10,
    forcing = .0001,
    randomization = None,
):
    """Optimizes energy by determining gradients with stochastic reconfiguration
        and minimizing the energy along gradient directions using correlated sampling.

    Args:

      wf: initial wave function

      coords: initial configurations

      pgrad_acc: A PGradAccumulator-like object

      steprange: How far to search in the line minimization

      warmup: number of steps to use for vmc warmup; if None, same as in vmcoptions

      maxiters: (maximum) number of steps in the gradient descent

      vmc: A function that works like mc.vmc()

      vmcoptions: a dictionary of options for the vmc method

      lm: the correlated sampling line minimization function to use

      lmoptions: a dictionary of options for the lm method

      update: A function that generates a parameter change 

      update_kws: Any keywords 

      npts: number of points to fit to in each line minimization

      replicas: How many replicas to use

      forcing: How much to push the replicas apart

    """
    if vmc is None:
        import pyqmc.mc
        vmc = pyqmc.mc.vmc
    if vmcoptions is None:
        vmcoptions = {}
    if lm is None:
        lm = pyqmc.linemin.lm_sampler
    if lmoptions is None:
        lmoptions = {}
    if update_kws is None:
        update_kws = {}

    attr = dict(maxiters=maxiters, npts=npts, steprange=steprange)
    x0_0 = pgrad_acc.transform.serialize_parameters(wf.parameters)
    if randomization is None: 
        for randomization in np.logspace(-2, -0.5, 50):
            x0 = np.concatenate([x0_0 + randomization*np.random.random(x0_0.shape) for _ in range(replicas)]).reshape((replicas,-1))
            est_penalty = penalizer.value(x0)
            print("randomization, penalty", randomization, est_penalty)
            if est_penalty < 1:
                break
    else:
        x0 = np.concatenate([x0_0 + randomization*np.random.random(x0_0.shape) for _ in range(replicas)]).reshape((replicas,-1))
        est_penalty = penalizer.value(x0)
        print("randomization, penalty", randomization, est_penalty)


    if verbose:
        print("starting warmup")
    data, coords = vmc(wf, coords, accumulators={}, **vmcoptions)

    for it in range(maxiters):
        pgrad_energy = np.zeros(x0.shape)
        ens = np.zeros(replicas)
        ens_err = np.zeros(replicas)
        for i,x in enumerate(x0):
            coords, last_en, pgrad, Sij, en, en_err = gradient_energy_function(x, coords, wf, pgrad_acc, vmc, vmcoptions, warmup)
            pgrad_energy[i,:] = pgrad
            ens[i] = en
            ens_err[i] = en_err
    
        pgrad_penalty = forcing*penalizer.gradient(x0)
        save_data = dict(
            penalty= forcing*penalizer.value(x0),
            energies = ens,
            energies_err = ens_err,
            p = x0,
            pgrad_penalty = pgrad_penalty,
            pgrad_energy = pgrad_energy)

        print("objective function", np.sum(ens) + forcing*penalizer.value(x0))
        print("ens", ens)
        print("errs", ens_err)
        grad = pgrad_penalty+pgrad_energy
        
        taus = np.linspace(-0.1*steprange, steprange, npts)
        allupdates = [simple_update(x0, tau, grad) for tau in taus]
        allupdates = np.array(allupdates)
        line_en = np.zeros(npts)
        line_penalty = np.zeros(npts)
        for i in range(replicas):
            newparms = pgrad_acc.transform.deserialize(x0[i,:])
            for k in newparms:
                wf.parameters[k] = newparms[k]
            _, coords = vmc(wf, coords, accumulators={}, **vmcoptions)
            tmp_data = lm(wf, coords, allupdates[:,i,:], pgrad_acc)
            for j, data in enumerate(tmp_data):
                line_en[j] += np.mean(data["total"] * data["weight"]) / np.mean(data["weight"])
                print("weight variance", np.std(data['weight']))
        
        for j,update in enumerate(allupdates):
            line_penalty[j] = forcing*penalizer.value(update)


        save_data['line_en'] = line_en
        save_data['line_penalty'] = line_penalty
        print("line_en", line_en)
        print("line_penalty", line_penalty)
        yfit = line_en + line_penalty
        print("yfit", yfit)
        est_min = pyqmc.linemin.stable_fit(taus, yfit)

        x0 = simple_update(x0,est_min, grad)
        swarm_hdf(hdf_file, save_data, attr, coords,
            [pgrad_acc.transform.deserialize(x) for x in x0]
        )
    return [pgrad_acc.transform.deserialize(x) for x in x0]

def test_penalty():
    nrep = 2
    nparm = 10
    p = np.random.random((nrep,nparm))
    mask = np.ones(p.shape[1], dtype=bool)
    mask[4] = False
    mask[-1] = False
    repulse = Repulsor(alpha=0.5, mask = mask)
    d = repulse.gradient(p)
    step = 1e-4
    for r in range(nrep):
        for k in range(nparm):
            for step in [1e-4, 1e-5, 1e-6, 1e-7]:

                save = p[r,k]
                p[r,k] += step
                plus = repulse.value(p)
                p[r,k] -= 2*step
                minus = repulse.value(p)
                p[r,k] = save
                numerical = (plus - minus)/(2*step)
                print(step, d[r,k], numerical, plus-minus)

if __name__ == "__main__":
    test_penalty()