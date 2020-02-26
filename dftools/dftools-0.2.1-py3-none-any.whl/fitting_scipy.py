import copy
import numpy as np
import pandas as pd
import scipy.stats
import scipy.optimize

class NLLModel(object):
    def __init__(
        self, data, mc, config, same_bin_widths=False,
        shape_type="shape", smooth_region=1.,
        observable_function = "bin_min, bin_max: (bin_min + bin_max)/2."
    ):
        self.verbose = False
        self.dfdata = data
        self.dfmc = mc
        self.config = config

        self.shape_type = shape_type
        self.smooth_region = smooth_region

        self.asimov = False
        self.toy = -1
        self.seed = 123456
        self.saturated = False

        self.norm_nuisances = [
            p["name"]
            for p in config["parameters"]
            if p["constraint"] == "gaussian"
        ]
        self.morph_nuisances = [
            p["name"]
            for p in config["parameters"]
            if p["constraint"] == "gaussian"
        ]

        region_procs = config["regions"]
        self.region_procs = region_procs
        self.regions = list(region_procs.keys())

        self.mcstat_nuisances = {
            r: [p["name"] for p in config["parameters"] if r in p["name"] and p["constraint"]=="gamma"]
            for r in self.regions
        }

        self.param_names = []
        self.param_inits = []
        #self.param_fixes = []
        self.param_limit = []
        for params in config["parameters"]:
            self.param_names.append(params["name"])
            self.param_inits.append(params["value"])
            #self.param_fixes.append(params["fixed"])
            self.param_limit.append(params["limit"])

        self.bins = {}
        self.data = {}
        self.obs = {}
        self.dbins = {}
        for r in self.regions:
            self.data[r] = data.loc[(r,),"sum_w"].values
            bins = data.loc[(r,),:].reset_index()[["bin_min", "bin_max"]].values
            self.obs[r] = eval("lambda "+observable_function)(bins[:,0], bins[:,1])
            self.dbins[r] = bins[:,1] - bins[:,0]
            if same_bin_widths:
                self.dbins[r][:] = 1.
            self.bins[r] = (bins[:,0], bins[:,1])

        # self.data_asimov[r,b]
        # self.data_toy[r,b]

        self.scale_functions = {}
        for r in self.regions:
            self.scale_functions[r] = []
            functions = []
            for p in region_procs[r]:
                self.scale_functions[r].append(
                    config["scale_functions"].get((r, p), "x, w, p: 1.")
                )

        self.sumw = {}
        self.sumww = {}
        for r in self.regions:
            self.sumw[r] = []
            self.sumww[r] = []
            for p in region_procs[r]:
                self.sumw[r].append(mc.loc[(r,p,""),"sum_w"].values)
                self.sumww[r].append(mc.loc[(r,p,""),"sum_ww"].values)
            self.sumw[r] = np.array(self.sumw[r])
            self.sumww[r] = np.array(self.sumww[r])

        self.nom_sum = {}
        self.up_sum = {}
        self.do_sum = {}
        for r in self.regions:
            self.nom_sum[r] = []
            self.up_sum[r] = []
            self.do_sum[r] = []
            for p in region_procs[r]:
                self.nom_sum[r].append(mc.loc[(r,p,""),"sum_w"].sum())

                self.up_sum[r].append([])
                self.do_sum[r].append([])
                for n in self.norm_nuisances:
                    try:
                        self.up_sum[r][-1].append(
                            mc.loc[(r,p,n+"Up"),"sum_w"].sum()
                        )
                        self.do_sum[r][-1].append(
                            mc.loc[(r,p,n+"Down"),"sum_w"].sum()
                        )
                    except KeyError:
                        self.up_sum[r][-1].append(self.nom_sum[r][-1])
                        self.do_sum[r][-1].append(self.nom_sum[r][-1])
            self.nom_sum[r] = np.array(self.nom_sum[r])
            self.up_sum[r] = np.array(self.up_sum[r])
            self.do_sum[r] = np.array(self.do_sum[r])

        self.delta_sum = {}
        self.delta_diff = {}
        for r in self.regions:
            self.delta_sum[r] = []
            self.delta_diff[r] = []
            for p in region_procs[r]:
                self.delta_sum[r].append([])
                self.delta_diff[r].append([])

                nom = mc.loc[(r, p, ""), "sum_w"].values
                nom_norm = nom/(nom*self.dbins[r]).sum()
                for n in self.morph_nuisances:
                    skip = False
                    try:
                        up = mc.loc[(r,p,n+"Up"),"sum_w"].values
                        do = mc.loc[(r,p,n+"Down"),"sum_w"].values
                    except KeyError:
                        delta_sum = np.zeros_like(nom_norm)
                        delta_diff = np.zeros_like(nom_norm)
                        skip = True

                    if not skip:
                        up_norm = up/(up*self.dbins[r]).sum()
                        do_norm = do/(do*self.dbins[r]).sum()

                        if self.shape_type == "shape":
                            up_del = up_norm - nom_norm
                            do_del = do_norm - nom_norm
                        elif self.shape_type == "shapeN":
                            up_del = np.where(
                                (up_norm>0)&(nom_norm>0),
                                np.log(up_norm/nom_norm),
                                np.zeros_like(nom_norm),
                            )
                            do_del = np.where(
                                (do_norm>0)&(nom_norm>0),
                                np.log(do_norm/nom_norm),
                                np.zeros_like(nom_norm),
                            )
                        delta_diff = up_del - do_del
                        delta_sum = up_del + do_del
                    self.delta_diff[r][-1].append(delta_diff)
                    self.delta_sum[r][-1].append(delta_sum)
            self.delta_diff[r] = np.swapaxes(np.array(self.delta_diff[r]), 1, 2)
            self.delta_sum[r] = np.swapaxes(np.array(self.delta_sum[r]), 1, 2)

        self.sumw_procsum = {
            r: (
                mc.loc[(r, pd.IndexSlice[:], ""), "sum_w"]
                .groupby(["bin_min", "bin_max"]).sum().values
            ) for r in self.regions
        }
        self.sumww_procsum = {
            r: (
                mc.loc[(r, pd.IndexSlice[:], ""), "sum_ww"]
                .groupby(["bin_min", "bin_max"]).sum().values
            ) for r in self.regions
        }
        self.neff_procsum = {
            r: self.sumw_procsum[r]**2/self.sumww_procsum[r]
            for r in self.regions
        }

        self.parameters = {}
        self.set_parameters({p["name"]: p["value"] for p in config["parameters"]})

    def _shape_norm(self, region):
        norm = np.ones_like(self.up_sum[region])
        condition = (self.theta_norm>=0.)
        norm[:,condition] = (self.up_sum[region]/self.nom_sum[region][:,np.newaxis])[:,condition]
        norm[:,~condition] = (self.do_sum[region]/self.nom_sum[region][:,np.newaxis])[:,~condition]
        val = np.power(norm, np.abs(self.theta_norm[np.newaxis,:]))
        val[np.isinf(val)] = 0.
        return val

    def shape_norm(self, region):
        df = pd.DataFrame(
            self._shape_norm(region),
            columns=self.norm_nuisances,
            index=self.region_procs[region],
        ).stack()
        df.index.names = ["process", "nuisance"]
        df.columns = ["norm"]
        return df

    def _shape_norms(self, region):
        val = self._shape_norm(region)
        if np.isnan(val).any():
            raise RuntimeError("NaN in shape_norm({}): {}".format(region, val))
        if np.isinf(val).any():
            raise RuntimeError("Inf in shape_norm({}): {}".format(region, val))
        return np.prod(self._shape_norm(region), axis=1)

    def shape_norms(self, region):
        df = pd.DataFrame(
            self._shape_norms(region),
            columns=["norm"],
            index=self.region_procs[region],
        )
        df.index.names = ["process"]
        return df

    def _shape_morph(self, region):
        theta_norm = self.theta_morph/self.smooth_region
        theta_norm2 = (theta_norm)**2

        # smooth step function
        step = np.sign(theta_norm)
        condition = (np.abs(theta_norm)<1.)
        step[condition] = (0.125*theta_norm*(theta_norm2*(3.*theta_norm2-10.)+15.))[condition]

        # theta * (diff + sum*smooth_step_function)
        _theta = self.theta_morph[np.newaxis,np.newaxis,:]
        step = step[np.newaxis,np.newaxis,:]
        return 0.5*_theta*(self.delta_diff[region] + self.delta_sum[region]*step)

    def shape_morph(self, region):
        results = self._shape_morph(region)

        df = pd.DataFrame()
        for i1 in range(results.shape[0]):
            for i2 in range(results.shape[2]):
                tdf = pd.DataFrame(results[i1,:,i2], columns=["morph"])
                tdf["process"] = self.region_procs[region][i1]
                tdf["nuisance"] = self.morph_nuisances[i2]
                tdf["bin_min"] = self.bins[region][0]
                tdf["bin_max"] = self.bins[region][1]
                tdf = tdf.set_index(["process", "nuisance", "bin_min", "bin_max"])
                df = pd.concat([df, tdf], axis=0)
        return df

    def _shape_morphs(self, region):
        sumw_norm = np.sum(self.sumw[region]*self.dbins[region][np.newaxis,:], axis=1)[:,np.newaxis]
        shape_vals_norm = self.sumw[region]/sumw_norm
        if self.shape_type=="shapeN":
            shape_vals_norm = np.log(shape_vals_norm)

        shape_vals_norm += np.sum(self._shape_morph(region), axis=2)
        if np.isnan(shape_vals_norm).any():
            raise RuntimeError("NaN in shape_morph({}): {}".format(region, shape_vals_norm))
        if np.isinf(shape_vals_norm).any():
            raise RuntimeError("Inf in shape_morph({}): {}".format(region, shape_vals_norm))

        if self.shape_type=="shapeN":
            shape_vals_norm = np.exp(shape_vals_norm)
        shape_vals_norm = np.maximum(1e-10, shape_vals_norm)

        return shape_vals_norm*sumw_norm #/sumw

    def shape_morphs(self, region):
        results = self._shape_morphs(region)/self.sumw[region]
        df = pd.DataFrame(results.T, columns=self.region_procs[region])
        df["bin_min"] = self.bins[region][0]
        df["bin_max"] = self.bins[region][1]
        df = df.set_index(["bin_min", "bin_max"]).stack()
        df.index.names = ["bin_min", "bin_max", "process"]
        df.columns = ["morph"]
        df = df.reorder_levels(["process", "bin_min", "bin_max"]).sort_index()
        return df

    def _prediction(self, region):
        nom_scale = np.ones_like(self.sumw[region])
        for idx, function in enumerate(self.scale_functions[region]):
            nom_scale[idx,:] = eval('lambda '+function)(
                self.obs[region], self.sumw[region][idx,:], self.parameters,
            )

        syst_scale = self._shape_morphs(region)*(self._shape_norms(region)[:,np.newaxis])

        #mcstat_scale = (1 + np.sqrt(self.sumww)/self.sumw)**(self.theta_mcstat[:,np.newaxis,:])
        mcstat_scale = np.power(
            (1 + np.sqrt(self.sumww_procsum[region])/self.sumw_procsum[region]),
            self.theta_mcstat[region]
        )[np.newaxis,:]

        # return sumw*nom_scale*syst_scale*mcstat_scale
        # syst_scale already includes sumw
        return nom_scale*syst_scale*mcstat_scale

    def prediction(self, region):
        results = self._prediction(region)
        df = pd.DataFrame(results.T, columns=self.region_procs[region])
        df["bin_min"] = self.bins[region][0]
        df["bin_max"] = self.bins[region][1]
        df = df.set_index(["bin_min", "bin_max"]).stack()
        df.index.names = ["bin_min", "bin_max", "process"]
        df.columns = ["prediction"]
        df = df.reorder_levels(["process", "bin_min", "bin_max"]).sort_index()
        return df

    def _predictions(self, region):
        val = self._prediction(region)
        if np.isnan(val).any():
            raise RuntimeError("NaN in prediction({}): {}".format(region, val))
        if np.isinf(val).any():
            raise RuntimeError("Inf in prediction({}): {}".format(region, val))
        return np.sum(self._prediction(region), axis=0)

    def predictions(self, region):
        results = self._predictions(region)
        df = pd.DataFrame(results, columns=["prediction"])
        df["bin_min"] = self.bins[region][0]
        df["bin_max"] = self.bins[region][1]
        df = df.set_index(["bin_min", "bin_max"])
        return df

    def poisson_pdfs(self, region):
        pred = np.maximum(1e-10, self._predictions(region))

        if self.asimov:
            if self.saturated:
                pred = self.data_asimov[region]
            pdfs = scipy.stats.gamma.logpdf(pred, self.data_asimov[region]+1.)
        elif self.toy>=0:
            if self.saturated:
                pred = self.data_toy[region]
            pdfs = scipy.stats.poisson.logpmf(self.data_toy[region], pred)
        else:
            if self.saturated:
                pred = self.data[region]
            pdfs = scipy.stats.poisson.logpmf(self.data[region], pred)
        if np.isnan(pdfs).any():
            raise RuntimeError("NaN in poisson_pdfs({}): {}".format(region, pdfs))
        if np.isinf(pdfs).any():
            raise RuntimeError("Inf in poisson_pdfs({}): {}".format(region, pdfs))
        return np.sum(pdfs)

    def gaussian_pdfs(self):
        pdfs = scipy.stats.norm.logpdf(self.theta_gaus)
        if np.isnan(pdfs).any():
            raise RuntimeError("NaN in gaussian_pdfs({}): {}".format(region, pdfs))
        if np.isinf(pdfs).any():
            raise RuntimeError("Inf in gaussian_pdfs({}): {}".format(region, pdfs))
        return np.sum(pdfs)

    def gamma_pdfs(self, region):
        sumw = self.sumw_procsum[region]
        sumww = self.sumww_procsum[region]
        neff = self.neff_procsum[region]
        theta = self.theta_mcstat[region]

        scale = np.power((1 + np.sqrt(sumww)/sumw), theta)
        pdfs = scipy.stats.gamma.logpdf(scale*neff, neff+1)
        pdfs[sumww==0.] = 0.
        if np.isnan(pdfs).any():
            raise RuntimeError("NaN in gamma_pdfs({}): {}".format(region, pdfs))
        if np.isinf(pdfs).any():
            raise RuntimeError("Inf in gamma_pdfs({}): {}".format(region, pdfs))
        return np.sum(pdfs)

    def nll(self):
        pois = sum(self.poisson_pdfs(r) for r in self.regions)
        gaus = self.gaussian_pdfs()
        gamm = sum(self.gamma_pdfs(r) for r in self.regions)
        val = -2*(pois+gaus+gamm)
        if self.verbose:
            print("pois: {}\ngaus: {}\ngamm: {}\nnll: {}".format(pois, gaus, gamm, val))
        if np.isnan(val):
            raise RuntimeError("NLL is nan")
        if np.isinf(val):
            raise RuntimeError("NLL is inf")
        return val

    def set_parameters(self, params, init=False):
        if isinstance(params, dict):
            params = np.array([
                params.get(name, init)
                for init, name in zip(self.param_inits, self.param_names)
            ])

        if np.isnan(params).any():
            raise RuntimeError(
                "NaN in input parameters. Previous values:\n{}\nNew values:\n{}".format(
                    self.parameters, params,
                )
            )
        if np.isinf(params).any():
            raise RuntimeError(
                "Inf in input parameters. Previous values:\n{}\nNew values:\n{}".format(
                    self.parameters, params,
                )
            )

        for name, val in zip(self.param_names, params):
            self.parameters[name] = val

        self.theta_mcstat = {}
        for r in self.regions:
            self.theta_mcstat[r] = []
            for name in self.mcstat_nuisances[r]:
                self.theta_mcstat[r].append(self.parameters[name])
            self.theta_mcstat[r] = np.array(self.theta_mcstat[r])

        self.theta_gaus = []
        self.theta_norm = []
        self.theta_morph = []
        for name in set(self.norm_nuisances+self.morph_nuisances):
            self.theta_gaus.append(self.parameters[name])
        for name in self.norm_nuisances:
            self.theta_norm.append(self.parameters[name])
        for name in self.morph_nuisances:
            self.theta_morph.append(self.parameters[name])
        self.theta_gaus = np.array(self.theta_gaus)
        self.theta_norm = np.array(self.theta_norm)
        self.theta_morph = np.array(self.theta_morph)

        if init:
            self.param_inits[:] = params

    def __call__(self, params, *args):
        if len(args)>0:
            params = np.array([params]+list(args))
        self.set_parameters(params)
        return self.nll()

    def minimize(self, *args, asimov=False, toy=-1, **kwargs):
        self.asimov = asimov
        self.data_asimov = {
            r: np.maximum(0., self._predictions(r))
            for r in self.regions
        }

        np.random.seed(self.seed+toy)
        self.toy = toy
        self.data_toy = {
            r: scipy.stats.poisson.rvs(np.maximum(1e-10, self._predictions(r)))
            for r in self.regions
        }

        result = scipy.optimize.minimize(self, *args, **kwargs)
        return result
