
# [[file:~/Research/CFEDemands/Empirics/result.org::*Main%20description%20of%20%3DResult%3D][result_class]]

# Tangled on Tue Feb 25 14:12:19 2020
import numpy as np
import pandas as pd
from . import estimation 
import xarray as xr
import warnings
from collections import namedtuple
from cfe.df_utils import to_dataframe, is_none, from_dataframe, ols

Indices = namedtuple('Indices',['j','t','m','i','k'])

class Result(xr.Dataset):

    """A class which packages together data and results for the CFE demand system.

    Result inherits from xarray.Dataset, and stores data as xarray.DataArrays
    with (as necessary) coordinates i for goods, j for households, t for periods,
    m for markets, and k for household characteristics.

    Typical usage with xarray.DataArrays (y,z)

    >>> z.dims  # Household characteristics
    ('k','j','t','m')
    >>> y.dims  # log expenditures
    ('i', 'j', 't', 'm')
    >>> R = cfe.result.Result(y=y,z=z) 
    >>> R.get_predicted_log_expenditures()
    >>> R.get_loglambdas()
    >>> R.get_alpha()                                                
    >>> R.get_stderrs() # Expensive bootstrap!

    Ethan Ligon                                                 August 2018
    """

    def __init__(self,**kwargs):
        """To load data from a netcdf file, use cfe.result.from_dataset().

        To instantiate from data on log expenditures (y) and household
        characteristics (z), supply each as xarray.DataArrays, with
        coordinates for y (i,j,t,m), and for z (j,k,t,m).

        All xarray.DataArrays which may be supplied:

          - y : log expenditures with coordinates (i,j,t,m).

          - z/characteristics : Household characteristics with coordinates (k,j,t,m). 

          - prices : Prices for goods (in levels) with coordinates (i,t,m).
            Supply only one of prices and logp.

          - logp : Log prices for goods (in levels) with coordinates (i,t,m).
            Supply only one of prices and logp.

        The below can be passed or assigned to an instance of Result,
        but would ordinarily be computed.

          - delta : Parameters with coordinates (i,k); the dot product of
            (z,delta) is an additive shifter of log expenditures.
            Estimated by the method get_reduced_form().

          - alpha : Preference parameters with coordinates i; additive
            shifters of log expenditures.

          - beta : Frisch elasticities with coordinates i.
            Estimated by the method get_beta()

          - loglambdas : log of marginal utility of expenditures with
            coordinates (j,t,m).  Estimated by the method
            get_loglambdas()

          - a : Good-period-market fixed effects, indexed by (i,t,m).
            Estimated by the method get_reduced_form().

          - yhat : Predicted log expenditures, indexed by (i,j,t,m).
            Estimated by the method get_predicted_log_expenditures().

          - ce : Residuals from reduced form estimation, indexed by
            (i,j,t,m).  Estimated by the method get_reduced_form().

          - cehat : Optimal rank 1 approximation to ce, indexed by
            (i,j,t,m).  Estimated by the method get_cehat().

          - e : Unexplained residuals from log expenditure equations.
            Estimated by the method get_loglambdas().

          - delta_covariance : Covariance matrix of parameter
            estimates delta; coordinates (i,k,kp).  Estimated by
            get_reduced_form().

          - se_delta : Standard errors of parameter estimates delta;
            coordinates (i,k).  Estimated by get_reduced_form().

          - se_beta : Standard errors of parameter estimates beta,
            with coordinates i. Estimated via the bootstrap method
            get_stderrs().  Note that this may be expensive.

          - se_alpha : Standard errors of parameter estimates alpha
            with coordinates i.  Estimated by method get_alpha().

          - se_a : Standard errors of good-time-market effects a, with
            coordinates (i,t,m).  Estimated by get_reduced_form().

        The following are attributes that may affect estimation or
        interpretation of features of the instance:

          - firstround : The coordinate identifying the earliest round
            of data.  Set automatically if coordinate values for t are
            sensible.

          - min_proportion_items : If a given household (j,t,m) has
            non-missing data for a proportion of all goods less than
            this parameter the household will be dropped from
            estimation. Default is 1/8.

          - min_xproducts : If a given good contributes fewer than
            min_xproducts observations to the estimation of the
            covariance matrix of residuals from the reduced form then
            the good will be dropped.  Default is 30.

          - useless_expenditures : A boolean flag, set to True unless
            the method drop_useless_expenditures() has been invoked.

          - stderr_tol : A tolerance parameter governing the precision
            with which se_beta are estimated.  Default is 0.01.

          - indices : A named tuple meant to permit changes in the
            coordinates (j,t,m,i,k).  Not implemented.

          - verbose : A boolean; set to True for a more verbose
            description of progress during estimation.

        """ 

        arrs = dict(alpha=None, beta=None, delta=None,
                    prices=None,characteristics=None,loglambdas=None, a=None,
                    yhat=None, ce=None, cehat=None, e=None, delta_covariance=None,
                    se_delta=None, se_beta=None, se_alpha=None, se_a = None,
                    y=None,logp=None,z=None)

        attrs = dict(firstround=None,
                     min_proportion_items=1./8,min_xproducts=30,
                     useless_expenditures=True,
                     stderr_tol=0.01,
                     indices = Indices('j','t','m','i','k'),
                     verbose=False)

        try: # Maybe input is already an xarray.Dataset?
            ds = kwargs.pop('data')
            for k in arrs:
                try:
                    arrs[k] = ds.variables[k]
                except KeyError:
                    pass

            attrs.update(ds.attrs)
            coords = ds.coords

        except KeyError: # Or maybe it's just a tuple of arrays and attributes.
            for k in arrs:
                try:
                    thing = kwargs.pop(k)
                    try: # thing may be a dataframe?
                        thing = thing.to_xarray()
                        if k in ['y','yhat','ce','cehat','e','prices']:
                            thing = thing.to_array('i')
                        elif k in ['z','characteristics']:
                            thing = thing.to_array('k')
                    except AttributeError: # Guess not!
                        pass
                    arrs[k] = thing
                except KeyError:
                    pass

            attrs.update(kwargs)
            coords = None

        super(Result,self).__init__(data_vars=arrs, coords=coords, attrs=attrs)

        if is_none(self.z) and  not is_none(self.characteristics):
            self['z'] = self.characteristics
        elif not is_none(self.z) and  is_none(self.characteristics):
            self['characteristics'] = self.z
        elif is_none(self.characteristics) and not is_none(self.y):
            self['characteristics'] = pd.DataFrame(index=self.y.isel(i=0).index).to_xarray()
            self['z'] = self['characteristics']

        if is_none(self.logp) and not is_none(self.prices):
            self['logp'] = np.log(self.prices)
        elif not is_none(self.logp) and is_none(self.prices):
            self['prices'] = np.exp(self.logp)

        if not is_none(self.beta) and not is_none(self.alpha):
            assert(self.alpha.shape == self.beta.shape)

        if is_none(self.attrs['firstround']) and not is_none(self.y):
            self.attrs['firstround'] = self.y.coords['t'][0].item()


    def drop_useless_expenditures(self,VERBOSE=False):
        """Drop expenditure items with too few observations.

        "Too few" depends on the attributes min_proportion_items and min_xproducts.  
        Once called this method sets the attribute 'useless_expenditures' to False.
        """

        if self.attrs['useless_expenditures']:
            y = self.y
            min_proportion_items = self.attrs['min_proportion_items']
            min_xproducts = self.attrs['min_xproducts']

            use_goods=y.coords['i'].data

            # Convert to pd.DataFrame
            y = to_dataframe(y.sel(i=use_goods).rename({'m':'mkt'}),'i')
            J,n = y.shape

            # The criterion below (hh must have observations for at least min_proportion_items of goods) ad hoc
            using_goods=(y.T.count()>=np.floor(len(use_goods) * min_proportion_items))
            y=y.loc[using_goods] # Drop households with too few expenditure observations, keep selected goods

            if VERBOSE:
                print('min_proportion_items test drops %d households.' % (J-y.shape[0]))
                J,n = y.shape

            y = estimation.drop_columns_wo_covariance(y,min_obs=min_xproducts,VERBOSE=VERBOSE)

            if VERBOSE:
                print('drop_columns_wo_covariance test drops %d households and %d goods.' % (J-y.shape[0],n-y.shape[1]))
                J,n = y.shape

            # Only keep goods with observations in each (t,mkt)
            y = y.loc[:,(y.groupby(level=['t','mkt']).count()==0).sum()==0]

            if VERBOSE:
                print('good in every (t,m) test drops %d households and %d goods.' % (J-y.shape[0],n-y.shape[1]))
                J,n = y.shape

            y = from_dataframe(y).rename({'mkt':'m'}).dropna('i',how='all')

            try:
                self['prices'] = self.prices.sel(i=y.coords['i'])
                self['logp'] = np.log(self.prices)
            except ValueError:
                pass # No prices in self?

            new = self.sel(i=y.coords['i'],j=y.coords['j'])

            new.attrs['useless_expenditures'] = False

            self.__dict__.update(new.__dict__)

        return to_dataframe(self.y.rename({'m':'mkt'}),'i')

    def get_reduced_form(self,VERBOSE=False):
        """Estimate reduced form expression for system of log expenditures.

        Computes a, ce, delta, se_delta, delta_covariance.          
        """

        y = self.drop_useless_expenditures() # Returns a dataframe
        z = to_dataframe(self.z.rename({'m':'mkt'}),'k')

        a,ce,d,sed,sea,V = estimation.estimate_reduced_form(y,z,return_se=True,return_v=True,VERBOSE=VERBOSE)
        ce.dropna(how='all',inplace=True)

        self['a'] = from_dataframe(a,'i').rename({'mkt':'m'})
        try:
            self['delta'] = from_dataframe(d).to_array('k')
        except AttributeError:
            d.columns.name = 'k'
            foo = from_dataframe(d)
            self['delta'] = foo

        self['ce'] = from_dataframe(ce).rename({'mkt':'m'})
        self['se_delta'] = from_dataframe(sed)
        self['se_a'] = from_dataframe(sea).rename({'mkt':'m'})
        self['delta_covariance'] = V

    def get_loglambdas(self,as_df=False):
        """Estimate (beta,loglambda).

        Sets beta, loglambdas, and cehat.  Returns loglambdas.
        """
        if is_none(self.loglambdas):
            if is_none(self.ce):
                self.get_reduced_form()

            min_obs = self.attrs['min_xproducts']

            ce = to_dataframe(self.ce.rename({'m':'mkt'}),'i')

            bphi,logL = estimation.get_loglambdas(ce,TEST=False,min_obs=min_obs)

            assert np.abs(logL.groupby(level='t').std().iloc[0] - 1) < 1e-12, \
                "Problem with normalization of loglambdas"

            cehat=np.outer(pd.DataFrame(bphi),pd.DataFrame(-logL).T).T
            cehat=pd.DataFrame(cehat,columns=bphi.index,index=logL.index)

            self['cehat'] = from_dataframe(cehat).rename({'mkt':'m'})
            self['loglambdas'] = logL.to_xarray().rename({'mkt':'m'})
            self['beta'] = bphi.to_xarray()

        if as_df:
            df = self.loglambdas.to_dataframe().squeeze().unstack('t').dropna(how='all')
            return df
        else:
            return self.loglambdas

    def get_beta(self,as_df=False):
        if is_none(self.beta):
            self.get_loglambdas()

        if as_df:
            return self.beta.to_dataframe().squeeze()
        else:
            return self.beta

    def get_cehat(self,as_df=False):
        if is_none(self.beta):
            self.get_loglambdas()

        out = self.cehat

        if as_df:
            df = out.to_dataframe().squeeze().unstack('i').dropna(how='all')
            return df
        else:
            return out

    def get_stderrs(self,as_df=True):
        if is_none(self.se_beta):
            if is_none(self.ce):
                self.get_reduced_form()

            tol = self.attrs['stderr_tol']
            VB = self.attrs['verbose']

            ce = to_dataframe(self.ce.rename({'m':'mkt'}),'i')

            se = estimation.bootstrap_elasticity_stderrs(ce,tol=tol,VERBOSE=VB)
            self['se_beta'] = from_dataframe(se)

        out = self['se_beta']

        if as_df:
            df = out.to_dataframe().squeeze().dropna(how='all')
            return df
        else:
            return out

    def anova(self):
        """Returns pandas.DataFrame analyzing variance of expenditures.

        Columns are proportion of variance in log expenditures
        explained by prices, household characteristics, and
        loglambdas; finally the R^2 of the regression and total
        variance of log expenditures.
        """

        self.get_reduced_form()

        yhat = self.get_predicted_log_expenditures()

        y = self.drop_useless_expenditures() # A dataframe

        miss2nan = self.ce*0 

        df = pd.DataFrame({'Prices':to_dataframe(self.a.var(['t','m'],ddof=0)),
                          'Characteristics':to_dataframe(self.z.dot(self.delta.T).var(['j','t','m'],ddof=0)),
                          '$\log\lambda$':to_dataframe((self.cehat + miss2nan).var(['j','t','m'],ddof=0)),
                          '$R^2':to_dataframe(self.yhat.var(['j','t','m'],ddof=0)/self.y.var(['j','t','m'],ddof=0))})

        df = df.div(y.var(ddof=0),axis=0)
        df['Total var'] = y.var(ddof=0)

        df.sort_values(by=r'$\log\lambda$',inplace=True,ascending=False)

        return df

    def get_predicted_log_expenditures(self,as_df=False):
        """Return predicted log expenditures.

        Sets yhat and e.
        """
        cehat = self.get_cehat()
        self['yhat'] = cehat + self.z.dot(self.delta) + self.a

        self['e'] = self.y - self.yhat

        out = self.yhat

        if as_df:
            df = out.to_dataframe().squeeze().unstack('i').dropna(how='all')
            return df
        else:
            return out


    def get_predicted_expenditures(self,as_df=False):
        """Return predicted levels of expenditures.

        Assumes residuals e have normal distribution.
        """
        yhat = self.get_predicted_log_expenditures()
        e = self.e

        out = estimation.predicted_expenditures(yhat,e)

        if as_df:
            df = out.to_dataframe().squeeze().unstack('i').dropna(how='all')
            return df
        else:
            return out

    def get_alpha(self,as_df=False):
        """Return alpha parameters.  

        These are the averages of the first round of data on log
        expenditures, and assumed equal across markets and periods.
        """

        if is_none(self.loglambdas):
            self.get_loglambdas()

        self['alpha'] = self.a.sel(t=self.firstround,drop=True).mean('m')
        self['se_alpha'] = np.sqrt((self.se_a.sel(t=self.firstround,drop=True)**2).sum('m'))/len(self.se_a.coords['m'])

        out = self.alpha

        if as_df:
            df = out.to_dataframe().squeeze().dropna(how='all')
            return df
        else:
            return out

    def a_decomposition(self):
        """Decompose constant terms from reduced form regression.

        Yields an xr.Dataset containing estimates of differences in
        average \log\lambda and log price level across settings, along
        with standard errors of these estimates.  In addition we provide
        estimates of the "residual" prices.

        Ethan Ligon                                           August 2018
        """ 

        self.get_loglambdas() 
        alpha = self.get_alpha()

        Pbar=[0]
        Lbar=[0]
        SE=[np.zeros(2)]
        V=[np.zeros((2,2))]
        P=[np.zeros(self.a.shape[0])]
        b = self.beta - self.beta.mean('i')

        rhs = xr.concat([(1 - self.beta*0),-b],'l').T
        rhs = rhs.to_dataframe().unstack('l')
        rhs.columns = rhs.columns.droplevel(0)
        for t in self.coords['t'].values[1:]:
            for m in self.coords['m'].values:
                lhs = ((self.a - alpha)/self.se_a).sel(t=t,m=m,drop=True).to_dataframe('')
                rhs = rhs.div(self.se_a.sel(t=t,m=m,drop=True).to_dataframe().squeeze(),axis=0)  
                b,se,v,p = ols(rhs,lhs,return_se=True,return_v=True,return_e=True)
                p = (p.to_xarray()*self.se_a.sel(t=t,m=m,drop=True)).to_array()
                Pbar.append(b[0].values[0])
                P.append(p.values)
                Lbar.append(b[1].values[0])
                SE.append(se.values.T[0])
                V.append(v)

        Pbar = xr.DataArray([Pbar],dims=['m','t'],coords={'t':self.coords['t'],'m':self.coords['m']},name='pbar')
        Lbar = xr.DataArray([Lbar],dims=['m','t'],coords={'t':self.coords['t'],'m':self.coords['m']},name='lbar')
        Pse = xr.DataArray([np.array(SE)[:,0]],dims=['m','t'],coords={'t':self.coords['t'],'m':self.coords['m']},name='pbar_se')
        Lse = xr.DataArray([np.array(SE)[:,1]],dims=['m','t'],coords={'t':self.coords['t'],'m':self.coords['m']},name='lbar_se')
        P = xr.DataArray(np.array([[x.squeeze() for x in P]]),dims=['m','t','i'],coords=self.a.coords).transpose('i','t','m')

        return xr.Dataset({'pbar':Pbar,'lbar':Lbar,'pbar_se':Pse,'lbar_se':Lse,'p_resid':P})

    def optimal_index(self):
        """Household-specific exact price index.

        For a household j observed at (t,m)=(t0,m0) computes
        proportional change in total expenditures required to keep
        \lambda constant across all observed settings (t,m).
        """
        if is_none(self.yhat):
            self.get_predicted_log_expenditures()

        a = self.a                

        R = estimation.optimal_index(a,self.yhat,self.e)

        return R

    def resample_lambdas(self):
        """Resample loglambdas.

        This produces a new object with preference parameters drawn
        from self and a measurement error process for expenditures
        which is log-normal.
        """

        d = self.dims
        S = np.random.randint(0,d['j'],size=d['j'])

        R = Result(data=self)

        foo = self.loglambdas.isel(j=S)
        foo.coords['j'] = self.loglambdas.coords['j']
        R['loglambdas'] =  foo + self.loglambdas*0.

        foo = self.z.isel(j=S)
        foo.coords['j'] = self.z.coords['j']

        R['z'] = foo
        R['characteristics'] = R.z

        R['cehat'] = R.loglambdas * R.beta

        # Retrieve mean & std of errors
        foo = (self.ce - self.cehat).to_dataframe('e').dropna()
        mu = foo.mean()
        sigma = foo.std()

        # Generate new errors lognormally distributed
        R['e'] = xr.DataArray(np.random.normal(loc=mu,scale=sigma,size=(d['j'],d['t'],d['m'],d['i'])),coords=R.ce.coords)

        # Add missings back in where appropriate
        foo = self.y.isel(j=S)
        foo.coords['j'] = self.z.coords['j']
        R['e'] = R['e'] + 0*foo

        R['ce'] = R.cehat + R.e

        R['yhat'] = R.cehat + R.z.dot(R.delta) + R.a

        R['y'] = R.yhat + R.e

        return R

# result_class ends here

# [[file:~/Research/CFEDemands/Empirics/result.org::*Persistent%20%3DResult%3D][result_to_file]]

# Tangled on Tue Feb 25 14:12:20 2020
    def to_dataset(self,fn=None):
        """Convert Result instance to xarray.Dataset."""
        D = xr.Dataset(self)

        if fn is not None:
            D.to_netcdf(fn)

        return D

    def to_pickle(self,fn):
        """Pickle Result instance in file fn."""
        import pickle
      
        d = self.to_dict()
        with open(fn,'wb') as f:
            pickle.dump(d,f)

        return d

def from_dataset(fn):
    """
    Read persistent netcdf (xarray.Dataset) file to Result.
    """

    D = xr.open_dataset(fn)

    R = Result(data=D)

    return R

def from_shelf(fn):
    import shelve

    with shelve.open(fn):
        pass

def from_pickle(fn):
    import xarray as xr
    import pickle

    with open(fn,'rb') as f:
        X = pickle.load(f)

    D = xr.Dataset.from_dict(X)

    R = Result(data=D)

    return R

# result_to_file ends here

# [[file:~/Research/CFEDemands/Empirics/result.org::*Interface%20to%20demand%20module][result_demand_interface]]

# Tangled on Tue Feb 25 14:12:20 2020
from cfe import demands
import pandas as pd

def _demand_parameters(self,p=None,z=None):
    """Return tuple of (p,alpha,beta,phi) from result.

    Note that the alpha returned is exp(alpha + delta.T z).

    Suitable for passing to =cfe.demand= functions.
    """

    beta = self.get_beta()
    n = len(beta)

    if z is None:
        z = self.z.isel(j=0,t=0,m=0,drop=True).fillna(0)*0

    alpha = np.exp(self.get_alpha() + self.delta.dot(z))

    if p is None:
        p = beta*0 # Copy coords, etc from beta
        p.data = [1]*n   
        p.name = 'prices'

    # The following hijinks deal with missing values (e.g., in prices)
    foo = xr.Dataset({'beta':beta,'alpha':alpha,'prices':p}).to_dataframe().dropna(how='any')

    if len(foo)==0:
        raise ValueError("No goods have non-missing beta, alpha, and price; can't compute demands.")

    p = foo.prices
    beta = foo.beta
    alpha = foo.alpha 

    phi = 0 # phi not (yet?) an attribute of Result.

    return (p,alpha,beta,phi)
    
def _demands(self,x,p=None,z=None,type="Marshallian"):
    """Quantities demanded at prices p for household with observable
    characteristics z, having a utility function with parameters given
    by (possibly estimated) attributes from a Result (i.e., the
    vectors of parameters alpha, beta, delta).

    Default type is "Marshallian", in which case argument x is budget.

    Alternative types:
       - "Frischian" :: argument x is Marginal utility of expenditures
       - "Hicksian" :: argument x is level of utility

    Ethan Ligon                                    April 2019
    """

    pparms = _demand_parameters(self,p,z)

    Qs = {'Marshallian':demands.marshallian.demands,
          'Hicksian':demands.hicksian.demands,
          'Frischian':demands.frischian.demands}

    q = pd.Series(Qs[type](x,*pparms),index=pparms[1].index,name='quantities')

    return q

def _utility(self,x,p=None,z=None):
    """Indirect utility 

    Varies with prices p, budget x and observable characteristics z,
    having a utility function with parameters given by (possibly
    estimated) attributes from a Result (i.e., the vectors of
    parameters alpha, beta, delta).

    Ethan Ligon                                    April 2019
    """

    pparms = _demand_parameters(self,p,z)

    return demands.marshallian.indirect_utility(x,*pparms)

def _expenditurefunction(self,U,p=None,z=None):
    """Total Expenditures

    Varies with level of utility U, prices p, and observable
    characteristics z, with a utility function having parameters given
    by (possibly estimated) attributes from a Result (i.e., the
    vectors of parameters alpha, beta, delta).

    Ethan Ligon                                    April 2019
    """

    pparms = _demand_parameters(self,p,z)

    return demands.hicksian.expenditurefunction(U,*pparms)

Result.demands = _demands
Result.indirect_utility = _utility
Result.expenditure = _expenditurefunction

# result_demand_interface ends here
