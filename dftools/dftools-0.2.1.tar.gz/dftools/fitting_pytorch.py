import numpy as np
import pandas as pd
import torch

class NLLModel(object):
    def __init__(
        self,
        parameters,
        theta_norm_idx_range,
        up_sum, do_sum, nom_sum,
    ):
        self.parameters = torch.from_numpy(parameters)
        self.parameters.requires_grad = True

        self.theta_norm_idx_range = theta_norm_idx_range

        self.up_sum = {r: torch.from_numpy(a) for r, a in up_sum.items()}
        self.do_sum = {r: torch.from_numpy(a) for r, a in do_sum.items()}
        self.nom_sum = {r: torch.from_numpy(a) for r, a in nom_sum.items()}

    def theta_norm(self):
        return self.parameters.narrow(
            0, self.theta_norm_idx_range[0],
            self.theta_norm_idx_range[1] - self.theta_norm_idx_range[0],
        )

    def _shape_norm(self, region):
        norm = torch.ones_like(self.up_sum[region])
        condition = (self.theta_norm()>=0.)
        norm[:,condition] = (self.up_sum[region]/self.nom_sum[region].unsqueeze(1))[:,condition]
        norm[:,~condition] = (self.do_sum[region]/self.nom_sum[region].unsqueeze(1))[:,~condition]
        val = torch.pow(norm, torch.abs(self.theta_norm().unsqueeze(0)))
        val[torch.isinf(val)] = 0.
        return val

#class NLLModel(object):
#    def _shape_norm(self, region):
#        norm = np.ones_like(self.up_sum[region])
#        condition = (self.theta_norm>=0.)
#        norm[:,condition] = (self.up_sum[region]/self.nom_sum[region][:,np.newaxis])[:,condition]
#        norm[:,~condition] = (self.do_sum[region]/self.nom_sum[region][:,np.newaxis])[:,~condition]
#        val = np.power(norm, np.abs(self.theta_norm[np.newaxis,:]))
#        val[np.isinf(val)] = 0.
#        return val
#
#    def shape_norm(self, region):
#        df = pd.DataFrame(
#            self._shape_norm(region),
#            columns=self.norm_nuisances,
#            index=self.region_procs[region],
#        ).stack()
#        df.index.names = ["process", "nuisance"]
#        df.columns = ["norm"]
#        return df
#
#    def _shape_norms(self, region):
#        val = self._shape_norm(region)
#        if np.isnan(val).any():
#            raise RuntimeError("NaN in shape_norm({}): {}".format(region, val))
#        if np.isinf(val).any():
#            raise RuntimeError("Inf in shape_norm({}): {}".format(region, val))
#        return np.prod(self._shape_norm(region), axis=1)
#
#    def shape_norms(self, region):
#        df = pd.DataFrame(
#            self._shape_norms(region),
#            columns=["norm"],
#            index=self.region_procs[region],
#        )
#        df.index.names = ["process"]
#        return df
#
#    def _shape_morph(self, region):
#        theta_norm = self.theta_morph/self.smooth_region
#        theta_norm2 = (theta_norm)**2
#
#        # smooth step function
#        step = np.sign(theta_norm)
#        condition = (np.abs(theta_norm)<1.)
#        step[condition] = (0.125*theta_norm*(theta_norm2*(3.*theta_norm2-10.)+15.))[condition]
#
#        # theta * (diff + sum*smooth_step_function)
#        _theta = self.theta_morph[np.newaxis,np.newaxis,:]
#        step = step[np.newaxis,np.newaxis,:]
#        return 0.5*_theta*(self.delta_diff[region] + self.delta_sum[region]*step)
#
#    def shape_morph(self, region):
#        results = self._shape_morph(region)
#
#        df = pd.DataFrame()
#        for i1 in range(results.shape[0]):
#            for i2 in range(results.shape[2]):
#                tdf = pd.DataFrame(results[i1,:,i2], columns=["morph"])
#                tdf["process"] = self.region_procs[region][i1]
#                tdf["nuisance"] = self.morph_nuisances[i2]
#                tdf["bin_min"] = self.bins[region][0]
#                tdf["bin_max"] = self.bins[region][1]
#                tdf = tdf.set_index(["process", "nuisance", "bin_min", "bin_max"])
#                df = pd.concat([df, tdf], axis=0)
#        return df
#
#    def _shape_morphs(self, region):
#        sumw_norm = np.sum(self.sumw[region]*self.dbins[region][np.newaxis,:], axis=1)[:,np.newaxis]
#        shape_vals_norm = self.sumw[region]/sumw_norm
#        if self.shape_type=="shapeN":
#            shape_vals_norm = np.log(shape_vals_norm)
#
#        shape_vals_norm += np.sum(self._shape_morph(region), axis=2)
#        if np.isnan(shape_vals_norm).any():
#            raise RuntimeError("NaN in shape_morph({}): {}".format(region, shape_vals_norm))
#        if np.isinf(shape_vals_norm).any():
#            raise RuntimeError("Inf in shape_morph({}): {}".format(region, shape_vals_norm))
#
#        if self.shape_type=="shapeN":
#            shape_vals_norm = np.exp(shape_vals_norm)
#        shape_vals_norm = np.maximum(1e-10, shape_vals_norm)
#
#        return shape_vals_norm*sumw_norm #/sumw
#
#    def shape_morphs(self, region):
#        results = self._shape_morphs(region)/self.sumw[region]
#        df = pd.DataFrame(results.T, columns=self.region_procs[region])
#        df["bin_min"] = self.bins[region][0]
#        df["bin_max"] = self.bins[region][1]
#        df = df.set_index(["bin_min", "bin_max"]).stack()
#        df.index.names = ["bin_min", "bin_max", "process"]
#        df.columns = ["morph"]
#        df = df.reorder_levels(["process", "bin_min", "bin_max"]).sort_index()
#        return df
#
#    def _prediction(self, region):
#        nom_scale = np.ones_like(self.sumw[region])
#        for idx, function in enumerate(self.scale_functions[region]):
#            nom_scale[idx,:] = eval('lambda '+function)(
#                self.obs[region], self.sumw[region][idx,:], self.parameters,
#            )
#
#        syst_scale = self._shape_morphs(region)*(self._shape_norms(region)[:,np.newaxis])
#
#        #mcstat_scale = (1 + np.sqrt(self.sumww)/self.sumw)**(self.theta_mcstat[:,np.newaxis,:])
#        mcstat_scale = np.power(
#            (1 + np.sqrt(self.sumww_procsum[region])/self.sumw_procsum[region]),
#            self.theta_mcstat[region]
#        )[np.newaxis,:]
#
#        # return sumw*nom_scale*syst_scale*mcstat_scale
#        # syst_scale already includes sumw
#        return nom_scale*syst_scale*mcstat_scale
#
#    def prediction(self, region):
#        results = self._prediction(region)
#        df = pd.DataFrame(results.T, columns=self.region_procs[region])
#        df["bin_min"] = self.bins[region][0]
#        df["bin_max"] = self.bins[region][1]
#        df = df.set_index(["bin_min", "bin_max"]).stack()
#        df.index.names = ["bin_min", "bin_max", "process"]
#        df.columns = ["prediction"]
#        df = df.reorder_levels(["process", "bin_min", "bin_max"]).sort_index()
#        return df
#
#    def _predictions(self, region):
#        val = self._prediction(region)
#        if np.isnan(val).any():
#            raise RuntimeError("NaN in prediction({}): {}".format(region, val))
#        if np.isinf(val).any():
#            raise RuntimeError("Inf in prediction({}): {}".format(region, val))
#        return np.sum(self._prediction(region), axis=0)
#
#    def predictions(self, region):
#        results = self._predictions(region)
#        df = pd.DataFrame(results, columns=["prediction"])
#        df["bin_min"] = self.bins[region][0]
#        df["bin_max"] = self.bins[region][1]
#        df = df.set_index(["bin_min", "bin_max"])
#        return df
#
#    def poisson_pdfs(self, region):
#        pred = np.maximum(1e-10, self._predictions(region))
#
#        if self.asimov:
#            if self.saturated:
#                pred = self.data_asimov[region]
#            pdfs = scipy.stats.gamma.logpdf(pred, self.data_asimov[region]+1.)
#        elif self.toy>=0:
#            if self.saturated:
#                pred = self.data_toy[region]
#            pdfs = scipy.stats.poisson.logpmf(self.data_toy[region], pred)
#        else:
#            if self.saturated:
#                pred = self.data[region]
#            pdfs = scipy.stats.poisson.logpmf(self.data[region], pred)
#        if np.isnan(pdfs).any():
#            raise RuntimeError("NaN in poisson_pdfs({}): {}".format(region, pdfs))
#        if np.isinf(pdfs).any():
#            raise RuntimeError("Inf in poisson_pdfs({}): {}".format(region, pdfs))
#        return np.sum(pdfs)
#
#    def gaussian_pdfs(self):
#        pdfs = scipy.stats.norm.logpdf(self.theta_gaus)
#        if np.isnan(pdfs).any():
#            raise RuntimeError("NaN in gaussian_pdfs({}): {}".format(region, pdfs))
#        if np.isinf(pdfs).any():
#            raise RuntimeError("Inf in gaussian_pdfs({}): {}".format(region, pdfs))
#        return np.sum(pdfs)
#
#    def gamma_pdfs(self, region):
#        sumw = self.sumw_procsum[region]
#        sumww = self.sumww_procsum[region]
#        neff = self.neff_procsum[region]
#        theta = self.theta_mcstat[region]
#
#        scale = np.power((1 + np.sqrt(sumww)/sumw), theta)
#        pdfs = scipy.stats.gamma.logpdf(scale*neff, neff+1)
#        pdfs[sumww==0.] = 0.
#        if np.isnan(pdfs).any():
#            raise RuntimeError("NaN in gamma_pdfs({}): {}".format(region, pdfs))
#        if np.isinf(pdfs).any():
#            raise RuntimeError("Inf in gamma_pdfs({}): {}".format(region, pdfs))
#        return np.sum(pdfs)
#
#    def nll(self):
#        pois = sum(self.poisson_pdfs(r) for r in self.regions)
#        gaus = self.gaussian_pdfs()
#        gamm = sum(self.gamma_pdfs(r) for r in self.regions)
#        val = -2*(pois+gaus+gamm)
#        if self.verbose:
#            print("pois: {}\ngaus: {}\ngamm: {}\nnll: {}".format(pois, gaus, gamm, val))
#        if np.isnan(val):
#            raise RuntimeError("NLL is nan")
#        if np.isinf(val):
#            raise RuntimeError("NLL is inf")
#        return val
#
#    def __call__(self, params, *args):
#        if len(args)>0:
#            params = np.array([params]+list(args))
#        self.set_parameters(params)
#        return self.nll()
#
#    def minimize(self, *args, asimov=False, toy=-1, **kwargs):
#        self.asimov = asimov
#        self.data_asimov = {
#            r: np.maximum(0., self._predictions(r))
#            for r in self.regions
#        }
#
#        np.random.seed(self.seed+toy)
#        self.toy = toy
#        self.data_toy = {
#            r: scipy.stats.poisson.rvs(np.maximum(1e-10, self._predictions(r)))
#            for r in self.regions
#        }
#
#
#
#        result = scipy.optimize.minimize(self, *args, **kwargs)
#        return result
