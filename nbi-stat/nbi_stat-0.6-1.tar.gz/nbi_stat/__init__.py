# Copyright 2018 Christian Holm Christensen 
#
# This code is distributed under the GNU General Public License 
# version 3 or any later version 
# 
# Generated 2020-02-15 00:56:31.647478 UTC

# -------------------------------------------------
from __future__ import print_function, division

__doc__ = \
"""Module to help with various statistical choirs 

This module contains many different functions and classes for statistical tasks, including 

- Robust and online mean and (co)variance calculations 
- Scientific rounding 
- Representation of results 
- Representation of data 
- Visualisation of data 
- Propagation of uncertainty 
- Sampling of arbitrary PDF
- Histogramming 
- Fitting

Copyright © 2019 Christian Holm Christensen
"""

version = "0.6"

# -------------------------------------------------
def n_significant(num_or_string):
    s = str(num_or_string)
    try:
        float(s)
    except:
        raise ValueError(f"{num_or_stringg} not decimal")
    s = s.lstrip("0.")
    if "." not in s:
        s.rstrip("0")
    return len(s)

# -------------------------------------------------
def round(v,n=0):
    from numpy import abs, floor, where, int64, logical_and, power, sign
    if v is None:
        return None
    
    tens = power(10.,-int64(n))
    w    = floor(100*abs(v)/tens + .00001)
    m    = int64(w / 100)
    nxt  = int64(w) % 100
    m    = where(nxt > 50, m+1, m)
    m    = where(logical_and(nxt == 50, m % 2 == 1), m+1, m)
    return sign(v) * m * tens

# -------------------------------------------------
def round_result(x,deltas,nsign=1):
    from numpy import min, ceil, log10, abs, atleast_1d
    if nsign is None:
        return x, deltas, None
    if nsign < 1: 
        raise ValueError('Number of significant digits cannot be negative')

    def _inner(xx,ee):
        eps  = 1e-15
        aerr = abs(ee)
        aerr = aerr[aerr!=0]
        emin = int(min(ceil(log10(aerr)+eps)) if len(aerr)>0 else 1)-nsign
        return round(xx,-emin), emin
        
    err       = atleast_1d(x if deltas is None else deltas)
    rdeltas,_ = _inner(err, err)
    
    err       = atleast_1d(x if rdeltas is None else rdeltas)
    rx,emin   = _inner(x, err)
    
    return rx, None if deltas is None else rdeltas, max(0,-emin)

# -------------------------------------------------
def print_result(x,deltas,nsign=1,width=8):
    from numpy import atleast_1d
    
    rx, rdeltas, ndig = round_result(x,deltas,nsign)
    if ndig is None:
        ffmt = '{:{}f}'
    else:
        ffmt = f'{{:{{}}.{ndig}f}}'
        
    print(ffmt.format(rx, width), end='')
    if rdeltas is not None:
        rdeltas = atleast_1d(rdeltas)
        for d in rdeltas:
            print(" +/- "+ffmt.format(d, width), end='')
    print("")

# -------------------------------------------------
def round_result_expo(x,deltas,nsign=1,expo=None):
    from numpy import abs,log10,floor,atleast_1d
    if expo:
        if not isinstance(expo,int) or isinstance(expo,bool):
            varg = expo if isinstance(expo,float) else x
            expo = int(floor(log10(abs(varg))))
        x *= 10**-expo
        if deltas:
            deltas = atleast_1d(deltas) * 10**-expo
    else:
        expo=0
            
    return (*round_result(x,deltas,nsign), expo)

# -------------------------------------------------
def format_result(value,deltas=None,nsig=1,name=None,
                 expo=None,unit=None,latex=True,dnames=None):
    from numpy import floor, asarray, abs, sign, zeros_like

    rv, re, ndig, rex = round_result_expo(value,deltas,nsig,expo)
    
    if ndig is None:
        ffmt = '{}'
    else:
        ffmt = f'{{:.{ndig}f}}'
        
    sval = ffmt.format(rv)
    
    if re is not None:
        if dnames is None:
            ne = zeros_like(deltas,dtype='str')
        elif len(dnames) != len(re):
            raise ValueError('Delta values and labels not in sync')
        else:
            ne = [fr'({n})'          if n != '' else ''      for n in dnames]
            ne = [fr'\mathrm{{{n}}}' if latex   else fr'{n}' for n in ne]
        
        sep  = r'\pm' if latex else ' +/- '
        sval += ''.join([f'{sep}'+ffmt.format(ee)+f'{ll}' 
                          for ee,ll in zip(asarray(re),asarray(ne))])
    
    sexp = ''
    if rex != 0:
        sexp = fr'\times10^{{{rex}}}' if latex else f'*10**{rex}'
    
    sunit = ''
    if unit is not None:
        sunit = fr'\,\mathrm{{{unit}}}' if latex else f' {unit}'
    
    sname = ''
    if name is not None:
        sname = fr'{name}='
        
    
    if deltas is not None and (sexp != '' or unit is not None):
        sval = fr'\left({sval}\right)' if latex else f'({sval})'
    
    return f'{sname}{sval}{sexp}{sunit}'

# -------------------------------------------------
n_significant.__doc__ = \
    """Determine the number of significant digits 
    
    >>> nbi_stat.n_significant("0.0120")
    >>> nbi_stat.n_significant(12340)
    
    Parameters
    ----------
      num_or_string : float or string 
        The number to determine number of significant digits for. 
        Note, to investigate numbers 
        
        - 0001234
        - 0.01230 
        
        one need to pass these a strings 
        
    Return
    ------
      Number of significant digits in num_or_string 
    """


# -------------------------------------------------
round.__doc__ = \
    """Round value(s) to the precision given by nbi_stat.py
    
    This function round the value(s) in v to the %precision 10^(-n) 
    by rounding to nearest even number, while only considering the most 
    adjecent digits. 
    
    Parameters:
        v : float, scalar or array like 
            Values to round 
        n : int, scalar or array like 
            Precision to round to i.e., number of digts, possibly 
            negative.  Note, this can be an array of the same size 
            as v
    Returns:
        u : float, scalar or array-like 
            Rounded values
    """


# -------------------------------------------------
round_result.__doc__ =\
    """Round result and associated uncertainties
    
    The result value x and associated uncertainties deltas 
    are rounded to the same precision.  The precision is 
    set by the least exponent needed to represent all 
    uncertainties with at least nsign significant digits 
    
    Parameters
    ----------
    x : float 
        The result value 
    deltas : float, array_like
        List of uncertainties associated with x
    nsign : positive, int 
        Number of significant digits to round to
      
    Returns
    -------
    rx : float
        Rounded value 
    rdeltas : float, array_like 
        Rounded uncertainties 
    ndig : int, positive
        Number of digits to print value and uncertaineis with
        
    Examples
    --------
    
    >>> nbi_stat.round_result(12.345,[1.2345,0.1234,0.01234])
    (12.35, [1.23, 0.12, 0.01], 2)
    
    """


# -------------------------------------------------
print_result.__doc__ =\
    """Print a single result with uncertainties, properly rounded 
    
    Parameters
    ----------
        x : float  
            Value of result 
        deltas : array-like 
            List of uncertainties 
        nsign : int, non-negative 
            Number of significant digits to round to 
        width : int, non-negative 
            Width of results 
            
    Examples
    --------
    
    >>> print_result(12.345,[1.2345,0.1234,0.01234])
       12.35 +/-     1.23 +/-     0.12 +/-     0.01
    

    """

# -------------------------------------------------
format_result.__doc__ =\
    """Function to pretty-format results
    
    Parameters
    ----------
        value : float  
            Value of result 
        deltas : array-like 
            List of uncertainties 
        nsign : int, non-negative 
            Number of significant digits to round to 
        name : str, optional
            Value name (quantity)
        expo : bool, int, float, optional
            - if True, automatically add exponent 
            - if integer, add exponent to that power
            - if float, add exponent to nearest power 
            - if None, do not add exponent 
        unit : str, optional
            If given, the unit
        latex : bool
            If true, format as LaTeX
        dnames : str, array-like, optional
            If given, must be as large as delta and contains labels 
            for each uncertainty
            
    Returns
    -------
        s : str 
            Name, value, uncertainties, exponent, and unit formatted 
            
    Examples
    --------
    
    >>> format_result(42,1.2,1,'a',None,'a.u.')
    >>> format_result(42,[1.2,10],2,'a',None,'a.u.',latex=True)
    >>> format_result(42,[1.2,10],2,'a',True)
    >>> format_result(42,[1.2,10],2,'a',latex=False)
    >>> format_result(42,[1.2,10],2,'a',-1,latex=False)
    >>> format_result(42,nsig=1,expo=None)
    """

# -------------------------------------------------
def hist(data,**kwargs):
    from numpy import histogram, diff, sqrt 
    from matplotlib.pyplot import gca, errorbar
    hkw = { 'bins':    kwargs.pop('bins',   10),
            'density': False, 
            'weights': kwargs.pop('weights',None),
            'range':   kwargs.pop('range',  None) }
    density = kwargs.pop('density',True)
    norm    = kwargs.pop('normalize',True)
    nozero  = kwargs.pop('suppress_zeros',False)
    h, b = histogram(data,**hkw)
    x    = (b[1:]+b[:-1])/2 
    w    = diff(b)
    e    = sqrt(h)
    
    if density:
        s = h.sum() if norm else 1
        h = h/w/s 
        e = sqrt(h/w/s)
        
    if nozero:
        h = h[e > 0]
        x = x[e > 0]
        w = w[e > 0]
        e = e[e > 0]
        
    ax = kwargs.pop('ax',gca())
    return ax.errorbar(x,h,e,w/2,**kwargs)

# -------------------------------------------------
def format_data_table(data,columns=None,rows=None,
                      nsig=1,expo=None,
                      mode='latex',
                      dollar=None,
                      title=None,
                      fmt=None,borders='THBLR',
                      top=None,bottom=None):
    from numpy import atleast_1d, newaxis
    
    mode  = mode.lower()
    latex = 'latex' in mode
    html  = 'html' in mode
    mjax  = 'mathjax' in mode
    if mjax:
        html = True
    if latex and dollar is None:
        dollar = '$'
    if title is None:
        title = ''
    cltx  = mjax or latex 
    
    dat = atleast_1d(data)
    try:
        nr,*nc = dat.shape
    except:
        raise ValueError('could not extract table format')
        
    if nc is None:
        dat = dat[:,newaxis]
        nc  = 1
        
    try:
        if len(nc) > 1:
            nc, nv = nc
        else:
            nc = nc[0] 
    except:
        raise ValueError('could not extract table format')
    
    if columns is not None:
        if len(columns) != nc:
            raise ValueError(f'Number of column headers ({len(columns)}) '
                             f'does not match number of columns ({nc})')
            
    if columns is None and not (latex or html):
        columns = ['']*nc 
    
    hasRH = False
    if rows is not None:
        if len(rows) != nr:
            raise ValueError(f'Number of row headers ({len(rows)}) '
                             f'does not match number of rows ({nr})')
        hasRH = True
    else:
        rows = [None]*nr
    
    def _c(txt):
        if mjax:
            txt = f'${txt}$'
        if html:
            return f'<td>{txt}</td>'
        return txt 
    
    def _cs():
        return '&' if latex else ('|' if not html else '')
    
    def _l(txt):
        return (fr'{txt}\\' if latex else (f'<tr>{txt}</tr>' if html 
                                           else f'| {txt} |')) + '\n'
    
    def _tb(txt):
        if txt is None:
            return ''
        
        if latex:
            tl = fr'\rlap{{\text{{{txt}}}}}' \
                + '&'.join(['' for _ in range(nc+hasRH)])
        elif html:
            tl = f'<td colspan={nc+hasRH}>{txt}</td>\n'
        else:
            tl = f'{txt}'
        
        return _l(tl)
        
    hline = r'\hline' + '\n'
    inner = ''
    if latex:
        if fmt is None:
            fmt = ''
            if 'L' in borders: 
                fmt += '|'
            if hasRH:
                cs = '|' if 'H' in borders else ''
                fmt += 'c' + cs

            cs = '|' if 'c' in borders else ''
            fmt += cs.join(['c' for _ in range(nc)])

            if 'R' in borders:
                fmt += '|'

        inner = fr'\begin{{array}}{{{fmt}}}' + '\n'
    elif html:
        inner = '<table>'
    
    inner += _tb(top)
        
        
    if latex and 'T' in borders:
        inner += hline
    
    if columns is not None:
        cs = _cs()
        cl = ''
        if hasRH:
            cl += _c(f'{title}') + cs
        
        cl += cs.join([_c(h) for h in columns])
        inner += _l(cl)
        
        if latex and 'H' in borders:
            inner += hline
            
        if not (latex or html):
            inner += cs + cs.join([':---:' for _ in range(nc+hasRH)]) + '\n'
    
    def _v(v):
        vv = atleast_1d(v)
        if len(vv) == 1:
            return v,None 
        else:
            return vv[0],v[1:]
        
    rl = []
    for i, (r,h) in enumerate(zip(dat,rows)):
        row = ''
        
        cs = _cs()
        if h is not None:
            row += _c(h) + cs
        
        row += cs.join([_c(format_result(*_v(v),
                                           nsig=nsig,expo=expo,latex=cltx))
                         for v in r])
        
        rl.append(_l(row))
    
    rs = hline if latex and 'r' in borders else ''
    inner += rs.join(rl)
    
    if latex and 'B' in borders:
        inner += hline
     
    inner += _tb(bottom)
    
    if latex:
        inner += r'\end{array}'
    elif html:
        inner += '</table>'
    
    if latex and dollar:
        inner = dollar+inner+dollar
    return inner

# -------------------------------------------------
hist.__doc__=\
    """Calculates and plots a histogram of data
    
    Parameters
    ----------
    data : array-like 
        The data to histogram 
    kwargs : dict (optional)
        A mixture of keyword arguments for NumPy `histogram` 
        and Matplotlib `errorbar`.  A few common keywords are 
        
        
        bins : int, str, or array-like 
            Binning specification 
        range : (float,float)
            The range of values to include in histogram 
        weights : array-like 
            Weights for each observation in data 
        density : bool 
            If true, divide by bin-width to normalize to density
        normalize : bool 
            If true, normalize to so that the intergral is one
        fmt : string 
            Format for plotting 
        label : string 
            Plot label 
        suppress_zeros : bool 
            If true, do not draw zero (uncertainty) points
        ax : matplotlib.Axes 
            Axes to plot in 

    Returns
    -------
    ec : matplotlib.ErrorbarCollection
        Collection of artists 
    """

# -------------------------------------------------
format_data_table.__doc__=\
    """Formats data into a LaTeX table
    
    Parameters
    ----------
    data : array-like 
        The data to histogram 
    columsn : str, array-like (optional, default: None)
        Column headers 
    rows : str, array-like (optional, default: None)
        Row headers 
    borders : str 
        Border options (case sensitive)
        
        T : Top 
        B : Bottom 
        H : After headers 
        L : Left 
        R : Right 
        c : between columns 
        r : between rows 
        
    nsig : int (optional, default 1)
        Number of significant digits 
    expo : int, float or 'auto' (optional, default: None)
        If not None, set exponential factor to show 
    bottom : str 
        Text put below table 
    top : str 
        Text put above table 
    fmt : str 
        Explicit table formatting string 
        
    Returns
    --------
    table : str 
        Formatted table as a string.  Can be passed to IPython display system for rendering. 
    """

# -------------------------------------------------
def cov(x,w,ddof=0,frequency=True,component=False):
    """Calculated weighted covariance"""
    from numpy import any, average, outer, add, cov as npcov
    if any(x.shape != w.shape):
        raise ValueError("Incompatible shapes of sample {} and weights {}"
                         .format(x.shape,w.shape))
        
    if not component:
        if frequency:
            return npcov(x,fweights=w,rowvar=False,ddof=ddof)
        else:
            return npcov(x,aweights=w,rowvar=False,ddof=ddof)
        
    # Calculate the weighted average in each dimension
    mean = average(x,axis=0,weights=w)
    
    # Subtract off mean 
    xx = x - mean
    
    # Calculate outer product of weights
    ww = [outer(wi,wi) for wi in w]
    
    # and observation vectors and element-wise product
    # of those two matrices 
    def part(wi,oi):
        return wi*outer(oi,oi)
    
    # Multiply weights on centered observations, and sum
    cc = add.reduce([part(wi,oi) for wi,oi in zip(ww,xx)])
    
    # Calculate sum of weights 
    sw = add.reduce(ww,dtype=x.dtype)
    
    # Calculate normalisation 
    norm = sw
    if frequency:
        norm -= ddof
    else:
        norm -= ddof*add.reduce([wij**2 for wij in ww]) / sw
    return cc / norm

# -------------------------------------------------
def scatter_hist2d(x,y,*args,**kwargs):
    from numpy import histogram2d,meshgrid,diff,sqrt
    from matplotlib.pyplot import gca 
    ax = kwargs.pop('ax',gca())
    sc = kwargs.pop('scale',1)
    dn = kwargs.pop('density',True)
    bn = kwargs.pop('bins',10)
    
    h,bx,by = histogram2d(x,y,bins=bn,density=dn)
    cx,cy   = (bx[1:]+bx[:-1])/2, (by[1:]+by[:-1])/2
    wx,wy   = diff(bx), diff(by)
    xx, yy  = meshgrid(cx,cy)
    xw, yw  = meshgrid(wx,wy)
    e       = sqrt(h/(xw*yw*len(x)))

    return h,cx,cy,wx,wy,e,ax.scatter(xx.ravel(),yy.ravel(),h.ravel()*len(x)*sc,**kwargs)

# -------------------------------------------------
def corner_plot(*args,**kwargs):
    from numpy import tril_indices, triu_indices, ndarray, \
        histogram, diff, sqrt
    from matplotlib.pyplot import subplots,subplot2grid,\
        scatter,errorbar,sca
    from matplotlib.lines import Line2D
    
    if len(args) < 1:
        raise ValueError('No data given')
    
    d1 = args[0]
    try:
        _, n = d1.shape
    except:
        raise ValueError('1st argument not data')
    
    title = kwargs.pop('title','')
    leg   = kwargs.pop('legend',False)
    names = kwargs.pop('names', None)
    figkw = kwargs.pop('fig_kw',kwargs.pop('sub_kw',{}))
    if 'gridspec_kw' not in figkw:
        figkw['gridspec_kw']=dict(hspace=0,wspace=0)
    if 'sharex' not in figkw:
        figkw['sharex'] = 'col'
    if 'sharey' not in figkw:
        figkw['sharey'] = 'row'
    
    if isinstance(names,list) and len(names) < n:
        raise ValueError(f'Not enough {len(names)} '
                         f'names given, need {n}')
    elif isinstance(names,bool) and names:
        names = 'auto'
    
    if callable(names):
        tmp = [names(i) for i in range(n)]
        names = tmp   
    elif isinstance(names,str):
        fnam = lambda i,o : f'{chr(o+i)}'
        if (names == 'auto' and n < 4): 
            oo = ord('x')
        elif (names == 'auto' or names == 'alpha'):
            oo = ord('a')
        elif names == 'Alpha':
            oo = ord('A')
        else:
            oo  = ''
            fnam = lambda i,o : names.format(i)
            
        names = [fr'${fnam(i,oo)}$' for i in range(n)]
    
    fig, ax = subplots(ncols=n,nrows=n,**figkw)
    fig.suptitle(title)
    
    dax = [None]*n
    for i, j in zip(*triu_indices(n)):
        if i == j: 
            dax[i]  = ax[i,j].twinx()
            ax[i,j].yaxis.set_visible(False)
        else:
            ax[i,j].remove()
        
    def _one(v,ax,dax,n,names,cur,**kwargs):
        dia    = kwargs.pop('dia', hist)
        off    = kwargs.pop('off', scatter)
        grid   = kwargs.pop('grid', False)
        diakw  = kwargs.pop('dia_kw',{})
        offkw  = kwargs.pop('off_kw',{})
        varkw  = kwargs.pop('var_kw',[None]*n)
        try:
            nv = len(varkw)
            assert nv == n
        except:
            raise ValueError('Invalid var_kw argument - '
                             'not a sequence or wrong number of elements')
        diakw.update({k:kwargs[k] for k in kwargs if not hasattr(diakw,k)})
        offkw.update({k:kwargs[k] for k in kwargs if not hasattr(offkw,k)})
        if diakw.get('color','') == 'auto':
            diakw['color'] = 'C'+str(cur)
        if offkw.get('color','') == 'auto':
            offkw['color'] = 'C'+str(cur)
        
        for i, j in zip(*tril_indices(n)):
            a  = dax[i] if i == j else ax[i,j]
            f  = dia    if i == j else off 
            sca(a)
            
            if grid: a.grid()
                
            if names is not None:
                if i == n-1:
                    ax[i,j].set_xlabel(names[j])
                if j == 0 and i != 0:
                    ax[i,j].set_ylabel(names[i]) 
                    
            if i == j:
                if varkw[i] is not None:
                    diakw['var'] = varkw[i]
                ar = f(v[i],**diakw)
            else:
                if varkw[i] is not None:
                    diakw['yvar'] = varkw[i]
                if varkw[j] is not None:
                    diakw['xvar'] = varkw[i]
                f(v[j],v[i],**offkw)
                
        if kwargs.get('label',False):
            return ar
        
    
    skip = 0
    cur  = 0
    ll   = []
    for o, d in enumerate(args):
        if skip > 0:
            skip -= 1
            continue
            
        try:
            _, m = d.shape 
        except:
            raise ValueError('Argument is not data')
        
        if n != m:
            raise ValueError(f'Data set {cur+1} of {m} variables not '
                             f'consistent with data set 1 of {n} variables')
    
        lbl=None
        kw=kwargs.copy()
        for oo in (o+1,o+2):
            if oo < len(args):
                if isinstance(args[oo],str):
                    kw['label'] = args[oo]
                    skip += 1
                elif isinstance(args[oo],dict):
                    kw.update(args[oo])
                    skip += 1
                    
            
        l = _one(d.T,ax,dax,n,names,cur,**kw)
        if l is not None:
            ll.append(l)
        cur += 1    
        
    if leg:
        o = (n+1)//2
        s = n//2
        lax = subplot2grid((n,n),(0,o),rowspan=s,colspan=s)
        lax.axis('off')
        lax.legend(ll,[l.get_label() for l in ll])
        
    return fig, ax, dax

# -------------------------------------------------
scatter_hist2d.__doc__=\
    """Draw a two-dimensional sample histogrammed as a 
    scatter plot 
    
    Parameters
    ----------
    x : array-like 
        First variable observations 
    y : array-like 
        Second variable observations
    kwargs : dict 
        Keyword arguments.  
        
        ax : matplotlib.axes.Axes
            Axes to draw in.  If not given use current axes 
        scale : float 
            Scalar of marker sizes 
        density : bool 
            Density argument for `numpy.histogram2d` 
        bins : int, array-like, str 
            Bins argument for `numpy.histogram2d` 
        kwargs : dict 
            Other keywords are passed to `matplotlib.pyplot.scatter`
    
    Returns
    ------- 
    h : array-like, 2-dimensional
        Density 
    x, y : array-like, 1-dimensional 
        Center of bins 
    wx, wy : array-like, 1-dimensional
        width of bins 
    e : array-like, 2-dimensional 
        Uncertainties
    artist : 
        Scatter plot artist 
    """

# -------------------------------------------------
corner_plot.__doc__=\
    """Draw a corner plot of several variables.  
    
    This will produce a trianguler plot of the passed data. On the 
    diagonal the distribution of each variable is represented.  The 
    off-diagonal elements are the correlation between pair-wise 
    variables.  
    
    Exactly how the representations are made can be customized by 
    the keywords `dia` and `off`, for the diagnoal and off-diagonal 
    elements.  What ever function passed to these keywords must plot 
    in the current axes. 
    
    The function can plot multiple data sets, each which can be given a 
    label by passing a string after the data set.  Optionally, each 
    data set can be further customized by passing a full dictionary 
    of keywords after the data set. 
    
    Parameters
    ----------
    args : misc 
        Data sets to plot. 
        Each data set may be followed by a string (which will be the 
        label of that data set), or a dict of keywords, or both 
        
        The keywords can be any of the below, except legend, names, 
        title, and fig_kw 
        
    kwargs : dict, optional 
        Keywords 
        
        names : array-like or str 
            Name of each variable or an option string 
            
            'auto' : If the number of variables is less than 3, 
                then set names to be 'x', 'y', 'z'. Otherwise 
                the same as 'alpha'
            'alpha' : Label the variables 'a', 'b', ... 
            'Alpha' : Label the variables 'A', 'B', ... 
            str : A  format specifier, which must 
                accept a single integer argument.  For example 
                'v_{{{}}}' would produce 'v_{1}','v_{2}',...
        
        legend : bool 
            If true, produce a legend of each data set 
            
        title : str 
            Title of figure 
            
        fig_kw : dict 
            Keywords to pass to figure creation 
            
        sub_kw : dict 
            keywords to pass to sub-plot creation 
            
        dia : callable 
            Function to draw representation of a single variable. 
            The function must accect an array of a single variable 
            and keyword arguments.  That is 
            
            
                dia(x,**kwargs)
                
            The default is to draw a histogram of the variable 
                
        dia_kw : dict 
            Keyword arguments to pass to `dia` 
            
        off : callable 
            Funtion to draw representation of two variables.  The 
            function must accept two arrays of variables and 
            keyword arguments.  That is 
            
                off(x,y,**kwargs)
                
            The default is to draw a scatter plot of the variable 
                
        off_kw : dict 
            Keywords to pass to `off` 
            
        grid : bool 
            If true, draw grid on axes 
            
        color : color-spec or 'auto'
            If 'auto', use data sample color 
            
    """

# -------------------------------------------------
def welford_init(ndim=1,covar=None):
    from numpy import zeros, float
    if ndim < 1:
        raise ValueError("Number of dimension must be 1 or larger")
        
    mean = zeros(ndim,dtype=float)
    var  = zeros((ndim,ndim),dtype=float) if covar else zeros(ndim,dtype=float)
    n    = 0
    return mean, var, n    

# -------------------------------------------------
def _welford_merge(ma,cva,na,mb,cvb,nb,ddof=0):
    from numpy import multiply, outer
    
    if na == 0:
        return mb,cvb,nb
    if nb == 0:
        return ma,cva,na 

    x  = outer if cva.ndim == 2 else multiply 
    n  = na + nb
    dx = mb - ma 
    m  = ma + nb / n * dx 
    dy = mb - m 
    cv = (na - ddof) / (n - ddof) * cva + nb / (n - ddof) * (cvb + x(dx,dy))
    return m, cv, n

# -------------------------------------------------
def welford_merge(ma,cva,na,mb,cvb,nb,ddof=0):
    from numpy import atleast_1d
    
    ma  = atleast_1d(ma)
    mb  = atleast_1d(mb)
    cva = atleast_1d(cva)
    cvb = atleast_1d(cvb)
    assert ma .shape == mb .shape 
    assert cva.shape == cvb.shape
    
    return _welford_merge(ma,cva,na,mb,cvb,nb,ddof)

# -------------------------------------------------
def welford_update(x,mean,covar,n,ddof=0,z=None):
    if z is not None:
        return _welford_merge(mean,covar,n,x,z,1,ddof)
    
    from numpy import zeros
    cv = zeros(covar.shape)
    return welford_merge(mean,covar,n, x,cv,1,ddof)

# -------------------------------------------------
def west_init(ndim=1,covar=False,frequency=True,component=False):
    from numpy import zeros, zeros_like, float
    if ndim < 1:
        raise ValueError("Size must be at least 1")
       
    mean  = zeros(ndim,dtype=float)
    cv    = zeros((ndim,ndim),dtype=float) if covar else zeros(ndim)
    sumw  = zeros_like(cv) if component else zeros(1)
    sumw2 = zeros_like(cv) if component and not frequency \
            else (zeros(1) if not frequency else None)
    summw = None
    
    if covar:
        summw = zeros_like(mean) if component else None
    return mean, cv, sumw, sumw2, summw    

# -------------------------------------------------
def _west_merge(ma,cva,w1a,w2a,wa,
                mb,cvb,w1b,w2b,wb,ddof):
    from numpy import less_equal, abs, ones, zeros, ndim, outer, multiply, argmax

    def iszero(x): # Fastest possible 
        for t in abs(x.ravel()):
            if t > 1e-8:
                return False
        return True
    
    if iszero(w1b):
        return ma,cva,w1a,w2a,wa 
    if iszero(w1a):
        return mb,cvb,w1b,w2b,wb 
    
    def Delta(sumw,sumw2,delta):
        if iszero(sumw):
            return zeros(sumw.shape)
        
        if sumw2 is None:
            return sumw - delta 
        
        return sumw - delta * sumw2 / sumw
    
    def upd(num,den,base=0):
        if ndim(den) == 0 or len(den) == 1:
            return num / den if den != 0 else base * ones(num.shape)
        
        msk    = den != 0
        a      = base * ones(num.shape)
        a[msk] = num[msk] / den[msk]
        return a
    
    component = w1a.shape == cva.shape
    covar     = ndim(cva) == 2 
    x         = outer if covar else multiply 
    
    w1        = w1a + w1b
    w2        = None
    w         = w1 
    wbb       = w1b 
    if w2a is not None:
        w2    = w2a + w2b 
    if wa is not None:
        w     = wa + wb 
        wbb   = wb 
    
    deltaa    = Delta(w1a,w2a,ddof)
    delta     = Delta(w1,w2,ddof)
    dx        = (mb - ma)
    m         = ma + upd(wbb * dx, w)
    dy        = (mb - m)
    cv        = upd(deltaa,delta,1) * cva + upd(w1b,delta,1) * (cvb + x(dx,dy))
    
    return m,cv,w1,w2,(w if wa is not None else None)

# -------------------------------------------------
def west_merge(ma,cva,w1a,w2a,wa,
               mb,cvb,w1b,w2b,wb,ddof):
    from numpy import atleast_1d
    
    ma   = atleast_1d(ma)
    mb   = atleast_1d(mb)
    cva  = atleast_1d(cva)
    cvb  = atleast_1d(cvb)
    w1a  = atleast_1d(w1a)
    w1b  = atleast_1d(w1b)
    w2a  = None if w2a is None else atleast_1d(w2a)
    w2b  = None if w2b is None else atleast_1d(w2b)
    wa   = None if wa  is None else atleast_1d(wa)
    wb   = None if wb  is None else atleast_1d(wb)
    
    assert ma.shape  == mb.shape 
    assert cva.shape == cvb.shape 
    assert w1a.shape == w1b.shape 
    assert (w2a is None) == (w2b is None) 
    assert (wa  is None) == (wb is None)
    
    return _west_merge(ma,cva,w1a,w2a,wa,mb,cvb,w1b,w2b,wb,ddof)

# -------------------------------------------------
def west_update(x,w,mean,cv,sumw,sumw2=None,summw=None,ddof=0,z=None):
    from numpy import zeros, outer, ndim
    
    ww  = outer(w,w) if ndim(sumw) == 2 else w
    ww2 = ww**2 if sumw2 is not None else None 
    wm  = w if summw is not None else None
    if z is not None:
        return _west_merge(mean,cv,sumw,sumw2,summw,
                           x,z,ww,ww2,wm,ddof)

    cvb = zeros(cv.shape)
    return west_merge(mean,cv,sumw, sumw2, summw,
                      x,cvb,ww,ww2,wm,ddof=ddof)

# -------------------------------------------------
from abc import ABC, abstractmethod

class Stat(ABC):
    def __init__(self,covar=None,ddof=0):
        self._ddof  = ddof 
        self._state = None
    
    @abstractmethod
    def update(self,x,w=None):
        pass 
    
    @property
    def mean(self):
        if self._state is None:
            raise ValueError('No state defined')
        return self._state[0]
    
    @property
    def var(self):
        if self._state is None:
            raise ValueError('No state defined')
        if self._state[1].ndim == 2:    
            return self._state[1].diagonal()
        return self._state[1]
    
    @property 
    def cov(self):
        if self._state is None:
            raise ValueError('No state defined')
        if self._state[1].ndim == 2:
            return self._state[1]
        return None
    
    @property
    def std(self):
        from numpy import sqrt
        return sqrt(self.var)
    
    @property
    @abstractmethod
    def sem(self):
        pass
    
    def __len__(self):
        return len(self.mean)
    
    def __radd__(self,o):
        if o is None or not isinstance(o,self.__class__):
            return self 
        return self.__add__(o)
    
    def _array(self):
        from numpy import vstack
        return vstack((self.mean,self.sem,self._state[1])).T
        
    def __str__(self):
        return str(self._array())
    
    def _repr_mimebundle_(self,include,exclude):
        from numpy import atleast_1d
        a = [[[m,s],*atleast_1d(o)] for m,s,o in zip(self.mean,self.sem,self._state[1])]
        r = [f'v_{i+1}' for i in range(len(self))]
        c = ['Mean']
        if self.cov is None:
            c += ['Var']
        else:
            c += r
            
        return {f'text/{t}': format_data_table(a,rows=r,columns=c,mode=t)
                for t in ['markdown','html','latex']}

# -------------------------------------------------
class Welford(Stat):
    def __init__(self,ndim,covar=None,ddof=0):
        from numpy import zeros_like
        super(Welford,self).__init__(covar,ddof)
        self._state = welford_init(ndim,covar)
        self._zeros = zeros_like(self._state[1])
      
    def fill(self,x,w=None):
        self._state = welford_update(x,*self._state,self._ddof,z=self._zeros)
        
    def update(self,x,w=None):
        from numpy import atleast_2d
        for xx in atleast_2d(x):
            self.fill(xx)
            
    @property
    def sem(self):
        from numpy import sqrt 
        return sqrt(self.var/self.n)
    
    @property
    def n(self):
        return self._state[2]
    
    def __iadd__(self,o):
        if isinstance(o,Welford):
            assert len(o) == len(self)
        
            self._state = welford_merge(*self._state,*o._state,self._ddof)
        else:
            self.update(o)
            
        return self 
    
    def __add__(self,o):
        r = Welford(len(self),self._state[1].ndim == 2, self._ddof)
        r += self
        r += o
        return r 

# -------------------------------------------------
class West(Stat):
    def __init__(self,ndim,covar=None,frequency=True,component=False,ddof=0):
        from numpy import zeros_like
        
        super(West,self).__init__(covar,ddof)
        self._state = west_init(ndim,covar=covar,
                                frequency=frequency,
                                component=component)
        self._var   = None 
        self._zeros = zeros_like(self._state[1])
        if component:
            self._var = Welford(ndim,False,ddof=ddof)
        
    def fill(self,x,w):
        if self._var is not None:
            self._var.fill(x)
        self._state = west_update(x,w,*self._state,self._ddof,z=self._zeros)
        
    def update(self,x,w=None):
        from numpy import atleast_2d, ones 
        xx = atleast_2d(x)
        if w is None:
            ww = ones(xx.shape)
        else:
            ww = atleast_2d(w)
        
        for xxx,www in zip(xx,ww):
            self.fill(xxx,www)
            
    @property
    def sumw(self):
        return self._state[2]
    
    @property 
    def sumw2(self):
        return self._state[3]
    
    @property
    def sem(self):
        from numpy import sqrt 
        if self.is_frequency():
            return sqrt(self.var/self.sumw)
        elif not self.is_component():
            return sqrt(1/self.sumw2)
        corr = sqrt(self.sumw2 / self.sumw**2).diagonal()
        return corr * self._var.std() 
    
    def is_component(self): return self._state[4] is not None 
    def is_frequency(self): return self.sumw2 is None 
    
    def __iadd__(self,o):
        if isinstance(o,West):
            assert len(o) == len(self)
            self._state = west_merge(*self._state,*o._state,self._ddof)
        else:
            self.update(*o)
            
        return self 
    
    def __add__(self,o):
        r = West(len(self),self._state[1].ndim == 2, 
                 frequency=self.is_frequency(),
                 component=self.is_component(),
                 ddof=self._ddof)
        r += self
        r += o
        return r

# -------------------------------------------------
welford_update.__doc__=\
    """Calculates running average and (co)variance by Welfords algorithm
    
    Note, this function will _always_ return arrays, _even_ if the input state 
    variables are scalar.  This simplifies the algorithm a lot, and we can 
    defer the overhead of coercing to scalar to the user and the last 
    possible point of evaluation 
    
    Parameters
    ----------
    x: float
        Current observation 
    n: int
        Current number of previously registered observations 
        (i.e., must be one on first call)
    mean: array-like, float
        Current average 
    cv: array-like, float
        Current (co)variance 
    ddof: int 
        Delta degrees of freedom.  
        Pass 1 for unbiased estimator, 0 for biased estimator
        
    Returns
    -------
    mean: float
        Updated mean
    cv: float 
        Update (co)variance 
    n: int 
        Updated count
          
    Examples
    -------- 
    
        >>> state = (0, 0 0)
        >>> for _ in range(100):
        ...     state = nbi_stat.welford_update(np.random.normal(),*state)
        
    """

# -------------------------------------------------
welford_init.__doc__=\
    """Initialize a structure for use with welford_update 
    
    >>> stat = welford_init(1)
    >>> for _ in range(1000):
    ...     stat = welford_update(np.random.normal(),*stat)
    >>> print("Mean: {}, Variance: {}".format(stat[0],stat[1]))
    
    Parameters
    ----------
         ndim : int 
             Dimension of sample
         covar : optional, bool
             If true and ndim > 1, allocate space for covariance 
         
    Returns
    -------
         (mean,variance,count) : tuple (float,float,int)
            This tuple we will pass to welford_update 
"""

# -------------------------------------------------
west_update.__doc__=\
    """Do a West online update of mean and (co)variance of the weighted sample.
    
    Note, this function will _always_ return arrays, _even_ if the input state 
    variables are scalar.  This simplifies the algorithm a lot, and we can 
    defer the overhead of coercing to scalar to the user and the last 
    possible point of evaluation 
    
    Parameters
    ----------
    x : scalar or array-like, float 
        The observation 
    w : scalar or array-like, float 
        The weight associated with the observation x
    mean : array-like, float 
        Current mean 
    cv : array-like, float   
        Current (co)variance 
    sumw : array-like, float 
        Current sum of weights 
    sumw2 : array-like, float, or None
        Current sum of square weights or None.  If None, 
        we assume the weights are frequency weights and we calculate 
        the (co)variance accordingly 
    summw : array-like, float or None
        Current sum of weights.  If None, we assume non-component weights.
    ddof : int 
        Delta degrees of freedom.  Use 1 for the unbiased estimator
        of the variance, otherwise 0.  Note, this is only used if 
        sumw2 is None
        
    Returns
    -------
    mean : array-like, float 
        Updated mean 
    cv : array-like, float 
        Updated (co)variance
    sumw : scalar or array-like, float 
        Updated sum of weights 
    sumw2 : None or array-like, float 
        Updated sum of square weights
    summw : None or array-like, float 
        Updated sum of weights 
        
    Examples
    -------- 
    
        >>> state = (0,0,0,0)
        >>> for _ in range(100):
        ...     state = west_update(np.random.normal(),
        ...                        np.random.random(), *state)
        
    """

# -------------------------------------------------
west_init.__doc__=\
    """Initialize a data-structure for use with west_update
    
    Parameters
    ----------
    ndim : int, positive 
        Number of dimensions (size of each observation)
    covar: bool, optional 
        If true, allocate room for a covariance matrix 
    frequency: bool, optional 
        If true, assume we have frequency weights 
    component: bool, optional 
        If ndim > 1, and if true, allocate for extra structure for 
        component weights 

    Returns
    -------
    mean : float, array-like 
        To hold the calculated means.  
        Has size ndim (1: scalar, else array)
    cv : float, array-like 
        To hold the calculated variances or covariance (if covar=True).  
        If for variances then an array of size (ndim,).
        If for covariances an array of size (ndim,ndim)
    sumw : float, array-like 
        To hold sum of weights. Of same size as cv 
    sumw2 : float, array-like 
        If frequency=False, an array to hold sum of square weights of same 
        size as sumw 
    summw : float, array-like 
        If component=True, then an extra array of size (ndim,) 
        to hold direct sum of weights
    """

# -------------------------------------------------
welford_merge.__doc__ = \
    """Merge two statistics into one 
    
    Note, this function will _always_ return arrays, _even_ if the input state 
    variables are scalar.  This simplifies the algorithm a lot, and we can 
    defer the overhead of coercing to scalar to the user and the last 
    possible point of evaluation 
        
    Parameters
    ----------
    ma : array, float 
        Means of sample A 
    cva : array, float 
        (co)variance of sample A
    na : int 
        count in sample A
    mb : array, float 
        Means of sample A 
    cvb : array, float 
        (co)variance of sample A
    nb : int 
        count in sample A
    ddof : int 
        Delta degrees of freedom 
        
    Returns
    -------
    m : array 
        Combined means 
    cv : array 
        Combined (co)variance
    n : int 
        Combined count 
    """

# -------------------------------------------------
west_merge.__doc__ = \
    """Merge two statistics into one 
    
    Note, this function will _always_ return arrays, _even_ if the input state 
    variables are scalar.  This simplifies the algorithm a lot, and we can 
    defer the overhead of coercing to scalar to the user and the last 
    possible point of evaluation 
        
    Parameters
    ----------
    ma : array-like, float 
        Mean of sample A
    cva : array-like, float   
        (Co)variance of sample A
    w1a : array-like, float 
        Sum of weights of sample A
    w2a : array-like, float, or None
        Sum of square weights of sample A or None.  If None, 
        we assume the weights are frequency weights and we calculate 
        the (co)variance accordingly 
    wa : array-like, float or None
        Sum of weights of sample A.  If None, we assume non-component weights.
    mb : array-like, float 
        Mean of sample B
    cvb : array-like, float   
        (Co)variance of sample B
    w1b : array-like, float 
        Sum of weights of sample B
    w2b : array-like, float, or None
        Sum of square weights of sample B or None.  If None, 
        we assume the weights are frequency weights and we calculate 
        the (co)variance accordingly 
    wb : array-like, float or None
        Sum of weights of sample B.  If None, we assume non-component weights.
    ddof : int 
        Delta degrees of freedom.  Use 1 for the unbiased estimator
        of the variance, otherwise 0.  Note, this is only used if 
        sumw2 is None
    
    """

# -------------------------------------------------
Stat.__doc__ = \
"""Base class for statistics classes

Parameters
----------
ddof : int (>=0)
    Delta degrees of freedom (1 for unbiased sample estimators)
"""

Stat.update.__doc__ = \
"""Update statistics with observation x (and possible weight)

Parameters
----------
x : array 
    Observation.  If this is a two dimensional array, then 
    we interpret each row as a single observation 
w : array (optional)
    Weights
"""

Stat.mean.__doc__ = """Return the mean(s)"""
Stat.var.__doc__  = """Return the variance(s)"""
Stat.cov.__doc__  = """"Possible get covariance"""
Stat.std.__doc__  = """Get the standard deviation"""
Stat.sem.__doc__  = """Return the standard error on the mean(s)"""

Stat.__len__.doc  = """Get number of dimensions"""
Stat.__radd__.__doc__ = """Add this to another statistics"""
Stat.__str__.doc__ = \
"""Format statistics 

- Each row is a variable 
- First column is the means 
- Second is the standard error on the mean 
- Subsequent columns are the (co)variance 
"""

# -------------------------------------------------
Welford.__doc__ = \
"""An unweighted sample statistics

Parameters
----------
ndim : int 
    Number of variables (dimension of sample)
covar : bool 
    If true, calculate covariance 
ddof : int 
    Delta degrees of freedom (1 for unbiased sample estimators)
"""

Welford.fill.__doc__ = \
"""Update statistics with single observation x (and possible weight)

Parameters
----------
x : array 
    Observation.  Must be scalar or 1D array 
w : array (ignored)
    Weights
"""

Welford.update.__doc__ = \
"""Update statistics with observation x (and possible weight)

Parameters
----------
x : array 
    Observation.  If a 2D-array interpret 
    each row as an observation.   The last dimension must 
    equal the number of dimensions of this object. 
w : array (ignored)
    Weights
"""

Welford.n.__doc__ = """Number of observations"""
Welford.sem.__doc__ = "Standard error on the mean(s)"
Welford.__iadd__.doc = """
Add either observation(s) or another Welford object 
to this object. 

Parameters
----------
o : array or Welford 
    Either an observation (1D-array)
    or observations (2D-array)
    or another statistics object (Welford) to merge 
    into this 
    
Returns
-------
self 
"""    
Welford.__add__.doc = """Add two Welford objects"""

# -------------------------------------------------
West.__doc__ = \
    """An weighted sample statistics
    
    Parameters
    ----------
    ndim : int 
        Number of variables (dimension of sample)
    covar : bool 
        If true, calculate covariance 
    frequency : bool 
        If true, consider weights to be frequency weights
    component : bool 
        If true, consider weights to be per component 
    ddof : int 
        Delta degrees of freedom (1 for unbiased sample estimators)
    """

West.fill.__doc__ = \
"""Update statistics with single observation x (and possible weight)

Parameters
----------
x : array 
    Observation.  Must be scalar or 1D array 
w : array
    Weights. If not specified assume 1
"""

West.update.__doc__ = \
"""Update statistics with observation x (and possible weight)

Parameters
----------
x : array 
    Observation.  If a 2D-array interpret 
    each row as an observation.   The last dimension must 
    equal the number of dimensions of this object. 
w : array.
    Weights.  If not given, assume 1. 
    If a 2D-array, interpret each rows as an observation 
    weight.  The last dimension must be 1 or equal to the number of
    dimensions of this object if declared to contain component weights. 
"""

West.is_component.__doc__ = "True if component-specific weights"
West.is_frequency.__doc__ = "True if frequency weights"
West.sumw.__doc__ = """Sum of weights of observations"""
West.sumw2.__doc__ = """Sum of square weights of observations (non-frequency only)"""
West.sem.__doc__ = "Standard error on the mean(s)"
West.__iadd__.doc = """
Add either observation(s) or another West object 
to this object. 

Parameters
----------
o : array or West
    Either an observation (1D-array)
    or observations (2D-array)
    or another statistics object (West) to merge 
    into this 
    
Returns
-------
self 
"""    
West.__add__.doc = """Add two Welford objects"""

# -------------------------------------------------
def propagate_uncertainty(f,x,delta,step=None):
    from numpy import ndim, diagonal, diag, \
        sqrt, zeros_like, sum, isscalar, ones, array, inner, atleast_1d
    if not callable(f):
        raise ValueError("f is not callable")
        
    xa = atleast_1d(x)
    da = atleast_1d(delta)
    sa = step
    if step is not None:
        sa = atleast_1d(step)
        
    n = len(xa)
    if len(da) not in (n,n**2):
        raise ValueError("Inconsistent sizes of X ({})and Delta ({})"
                         .format(xa.shape,da.shape))
        
    if sa is not None and len(sa) != n:
        raise ValueError("Inconsitent sizes of step and X")
        
    if ndim(da) == 1:        # Uncertaintes only given
        covar = diag(da**2)  # Make covariance 
    elif ndim(da) == 2:      # Covariance given 
        covar = da           
        da    = sqrt(diagonal(da))  # Uncertainties
    else:
        raise ValueError("Delta must be uncertainties or covariance")
         
    if sa is None:  # Set differnetation step sizes
        sa = da 
    
    # Calculate partial derivatives 
    dx = diag(sa)
    df = array([(f(x+d)-f(x-d))/(2*s) for d,s in zip(dx,sa) if s > 0])
    v = df.T @ covar @ df
    
    if v.ndim == 2:  # Function evaluated at many X
        v = diagonal(v)
    return v if isscalar(v) or len(v) > 1 else v.item()

# -------------------------------------------------
def effective_variance(x,ex,f,p,ey,df=None,df_step=None):
    from scipy.misc import derivative as diff
    
    if callable(df):
        dfx = df(x,*p)
    else:
        ds  = 1 if df_step is None else df_step
        dfx = diff(f,x,dx=ds,n=1,args=p)[:len(x)]
        
    eff = dfx**2*ex**2+ey**2
    return eff

# -------------------------------------------------
propagate_uncertainty.__doc__=\
    """Propegate uncertainties on x to y
    
    The function is differentiated with respect to each input as 
    
        df = (f(x+dx) - (fx-dx))/(2*dx)
        
    where dx is by default the uncertainties.  However, one can
    specify a different step size (dx) if so needed.  The 
    uncertainty is then calculated as 
    
    
        u = df.T @ covar @ df 
        
    where covar is the covariance matrix.  Note, if the given 
    delta is 1-dimensional of the same size as x - i.e., we 
    are passing the parameter uncertainties, then the 
    covariance matrix is set to the diagonal matrix 
    
        covar = [[delta[0]**2, 0,           ...]
                 [0,           delta[1]**2, ...] 
                 [...                          ]]
    
    Parameters
    ----------
        f : callable 
            Mapping from x to y 
        x : scalar or array-like 
            Value or values of x 
        delta : scalar or array-like 
            Either: Uncertainty or uncertainties of x (_not_ squared)
            Or: Covariance matrix of x
        step : scalar or array-like (optional)
            Step size or sizes for numerical differentation of f.
            If none given then use standard deviation or standard 
            deviations of x
    Returns
    -------
        delta_f : float 
            Square-uncertainty on y=f(x)
            
    Examples
    -------- 
    
        >>> x = np.random.normal(2,1,size=100)
        >>> y = np.random.normal(3,1,size=100)
        >>> stat = nbi_stat.Welford(2,covar=True)
        >>> for xi,yi in zip(x,y):
        ...     stat.update([xi,yi])
        >>> def f(x,y):
        ...     return x * y
        >>> vf = f(stat.mean)
        >>> df = nbi_stat.propagate_uncertainty(f,stat.cov)
        >>> nbi_stat.print_result(vf,[df])
        
        >>> g = 980
        >>> m, M, dm, dM = 10.23, 154.34, 0.02, 0.02
        >>> 
        >>> def f(m,M,g):
        ...     return g*m/(m+M)
        >>> 
        >>> p  = np.array([m,M])
        >>> dp = np.array([dm,dM])
        >>> l  = lambda p:f(p[0],p[1],g)
        >>> v  = f(m,M,g)
        >>> dv = np.sqrt(nbi.propagate_uncertainty(l,p,dp))
        >>> 
        >>> nbi_stat.print_result(v,[dv])

        
    """

# -------------------------------------------------
effective_variance.__doc__ = \
    """Calculates the effective variance
    
    That is, the function calculates the square uncertainty on 
    
    d = y - f(x) 
    
    as 
    
    ed**2 = ey**2 + diff(f(x,p),x)**2 * ex**2 
    
    where `diff` is the derivative of f wrt to x.  The derivate can 
    be given as a callable, or be calculated numerically 
    
    Parameters
    ----------
    x : array 
        Independent variable 
    ex : array 
        Uncertainty on x 
    f : callable 
        A callable representing f, with the signature 
        
            f(x,*p)
            
    ey : array 
        Uncertainty on y 
    df : callable 
        The differential of f wrt x.  A function of the form 
        
            df(x,*p)
            
    df_step : None, float, array 
        The step size to use when evaluating the differential numerically 
        
    Returns
    -------
    ed2 : array 
        The squared effective variance 
    """

# -------------------------------------------------
def histogram(a,bins="auto",rnge=None,weights=None,frequency=True,normalize=False):
    from numpy import histogram as nphist
    from numpy import sqrt, diff
    
    if weights is not None and (weights < 0).any():
        raise ValueError("Negative weights does not make sense")
        
    if weights is None or frequency:
        if weights is not None and weights.dtype.kind != 'i':
            raise ValueError("Frequency weights are not integer")

        total = len(a) if weights is None else weights.sum()
        n, b = nphist(a,bins=bins,range=rnge,weights=weights,density=True)
        n *= total
        db = diff(b)
        e =  sqrt(n) / sqrt(db)
        
        if normalize:
            n /= total
            e /= total
    
        return n, 0.5*(b[1:]+b[:-1]), db, e
    
    try:
        from numpy import double as npdouble
        from numpy import complex as npcomplex
        from numpy import intp as npintp
        from numpy import can_cast, logical_and, bincount, zeros
        from numpy import argsort, concatenate, sqrt
        # These require NumPy 1.15 or better 
        # Note, this is a little dangerous as NumPy may change this around at any time
        from numpy.lib.histograms import _ravel_and_check_weights
        from numpy.lib.histograms import _search_sorted_inclusive
        from numpy.lib.histograms import _get_bin_edges, _unsigned_subtract
    except ImportError as e:
        from numpy.version import version as npversion
        raise ImportError("NumPy version 1.15 or newer needed, have {}: {}"
                         .format(npversion, e))
        
    a, weights = _ravel_and_check_weights(a,weights)
    bin_edges, uniform_bins = _get_bin_edges(a, bins, rnge, weights)
    ntype = weights.dtype
    
    simple_weights = can_cast(ntype,npdouble) or can_cast(ntype,npcomplex)
        
    BLOCK = 65536
    
    if uniform_bins is not None and simple_weights:
        first, last, nbin = uniform_bins
        
        n    = zeros(nbin, ntype)
        w2   = zeros(nbin, ntype)
        norm = nbin / _unsigned_subtract(last,first)
        
        for i in range(0,len(a),BLOCK):
            tmp_a = a[i:i+BLOCK]
            tmp_w = weights[i:i+BLOCK]
            
            keep  =  (tmp_a >= first)
            keep  &= (tmp_a <= last)
            if not logical_and.reduce(keep):
                tmp_a = tmp_a[keep]
                tmp_w = tmp_w[keep]
                
            tmp_a = tmp_a.astype(bin_edges.dtype, copy=False)
            
            f_indexes = _unsigned_subtract(tmp_a, first) * norm
            indexes   = f_indexes.astype(npintp)
            indexes[indexes == nbin] -= 1
            
            decrement = tmp_a < bin_edges[indexes]
            indexes[decrement] -= 1
            
            increment = ((tmp_a >= bin_edges[indexes+1]) 
                         & (indexes != nbin-1))
            
            if ntype.kind == 'c':
                n.real += bincount(indexes,weights=tmp_w.real,minlength=nbin)
                n.imag += bincount(indexes,weights=tmp_w.imag,minlength=nbin)
            else: 
                n += bincount(indexes,weights=tmp_w,minlength=nbin)
            w2 += bincount(indexes,weights=tmp_w**2,minlength=nbin)
    
    else:
        cum_n  = zeros(bin_edges.shape, ntype)
        cum_w2 = zeros(bin_edges.shape, ntype) 
        zero   = zeros(1, dtype=ntype)
        
        for i in range(0,len(a),BLOCK):
            tmp_a = a[i:i+BLOCK]
            tmp_w = weights[i:i+BLOCK]
            
            sortidx = argsort(tmp_a)
            sa  = tmp_a[sortidx]
            sw  = tmp_w[sortidx]
            cw  = concatenate((zero, sw.cumsum()))
            cw2 = concatenate((zero, (sw**2).cumsum()))
            bin_index = _search_sorted_inclusive(sa, bin_edges)
            cum_n  += cw[bin_index]
            cum_w2 += cw2[bin_index]
            
        n  = diff(cum_n)
        w2 = diff(cum_w2)
        
    
    db = diff(bin_edges)
    mb = (bin_edges[1:]+bin_edges[:-1]) / 2
    r  = n / db
    e  = sqrt(w2)
    
    if normalize:
        r /= n.sum()
        e /= n.sum()
        
    return r, mb, db, e

# -------------------------------------------------
def init_histogram(bins,weighted=False):
    from numpy import zeros, zeros_like
    if len(bins) < 2:
        raise ValueError("Must have at least 1 bin")
    if not all([f<l for f, l in zip(bins[:-1],bins[1:])]):
        raise ValueError('bins must be increasing')
        
    sumw = zeros(len(bins)-1)
    sumw2 = None
    
    if weighted:
        sumw2 = zeros_like(sumw)
        
    return bins, sumw, sumw2

# -------------------------------------------------
def fill_histogram(x,bins,sumw,sumw2=None,weight=1):
    from bisect import bisect_left, bisect_right
    
    if len(bins) != len(sumw)+1:
        raise ValueError("Inconsistent size of bins and sum weights")
    
    if sumw2 is not None and len(sumw) != len(sumw2):
        raise ValueError("Size of sum of weigts and sum of square weights inconsistent")
    
    if sumw2 is None and not isinstance(weight, int):
        raise ValueError("Sum squared weights not given, but weight is not integer")
    
    if weight < 0: 
        raise ValueError("Weight is negative")
        
    if not (bins[0] <= x <= bins[-1]):
        return bins, sumw, sumw2
    
    idx = bisect_right(bins,x)-1
    if idx == len(bins)-1:
        idx -= 1
          
    sumw[idx] += weight
    if sumw2 is not None:
        sumw2[idx] += weight**2
        
    return bins, sumw, sumw2

# -------------------------------------------------
def fini_histogram(bins,sumw,sumw2=None,normalize=False):
    from numpy import diff, sum, sqrt, asarray
    if len(bins) != len(sumw)+1:
        raise ValueError("Inconsistent sizes of bins and content")
        
    if sumw2 is not None and len(sumw) != len(sumw2):
        raise ValueError("Inconsistent sizes of sum weights and sum square weights")
        
        
    # Calculate bin centres and widths 
    b = asarray(bins)
    m = 0.5 * (b[1:]+b[:-1])
    w = diff(b)
    
    # Calculate integral 
    t = sum(sumw)
    
    # Calculate uncertainty 
    e = sqrt(sumw)
    if sumw2 is not None:
        e = sqrt(sumw2)
        
    # Scale by bin widts 
    h = sumw / w
    e /= w 
    
    if normalize:
        h /= t
        e /= t 
        
    return h, m, w, e

# -------------------------------------------------
class Histogram:
    def __init__(self,bins,weighted=False):
        self._state = init_histogram(bins,weighted)
        self._hist  = None
        self._uncer = None
        
    def fill(self,x,weight=1):
        if self._hist is not None:
            raise RuntimeError('Histogram already calculated')
        fill_histogram(x,*self._state,weight)
        
    def finalize(self,normalize=False):
        if self._hist is not None:
            raise RuntimeError('Histogram already calculated')
        self._hist,_,_,self._uncer = fini_histogram(*self._state,
                                                   normalize=normalize)
        return self._hist,self.centers,self.widths,self.uncertainties
 
    @property
    def bins(self): return self._state[0]
    
    @property
    def centers(self):  return (self.bins[:-1]+self.bins[1:])/2
    
    @property
    def heights(self): return self._hist
    
    @property
    def widths(self):
        from numpy import diff
        return diff(self.bins)
    
    @property
    def uncertainties(self): return self._uncer
    
    @property
    def sums(self): return self._state[1]
    
    @property
    def sumWeightsSquare(self): return self._state[2]
    
    def _repr_mimebundle_(self,include,exclude):
        if self._hist is None:
            return None 
        a = [[[c,w/2],[h,u]] for c,w,h,u in zip(self.centers,self.widths,
                                              self.heights,self.uncertainties)]
        c = ['x','dN/dx']
        return {f'text/{t}': format_data_table(a,columns=c,mode=t)
                for t in ['markdown','html','latex']}

# -------------------------------------------------
histogram.__doc__=\
    """Build a histogram of data in a
    
    Optionally, each observation in a can be weighted by giving 
    an array of equal size as the argument weights.  
    
    If weights are given and frequency is set to True, then we
    assume the weights are frequency weights (i.e., x_i was seen w_i 
    times), and we use the regular NumPy histogram funktion 
    
    If weights are given, but frequency is set to False, then we 
    need to calculate the sum of square weights in each bin, which
    - unfortunately - NumPy does not provide.  
    
    Parameters
    ----------
    a : array-like 
        Input data.  
    bins : int or sequence of scalars or str
        Defines the binning used by the histogram.  
        
        If a string, the corresponding binning method is used.
        Note, binning methods are not supported for weighted 
        observations 
        
        If an integer, specifies the number of bins between 
        rnge or minimum and maximum of a
        
        If a sequence of scalars, then that sequence defines 
        the bin edges 
    rnge : (float,float
        Least and largest values to consider.  If not set, 
        defaults to minimum and maximum of a, respectively 
    weights : array-like , optional
        An array of weights with the same shape as a
    frequency : bool, optional 
        If weights are given and this flag is set, assume that 
        the weights are integer frequency weights 
    normalize : bool, optional 
        If true, normalize this bins so that the total integral 
        (sum of heights times widhts) is 1. 
    
    Returns
    -------
    n : array-like 
        Bin height.  This times the width gives the (possibly normalized) 
        observed probability 
    mid : array-like 
        Mid-point of bins 
    widths : array-like 
        Widths of bins 
    uncer : array-like 
        Uncertainty of n in each bin
            
    Raises
    ------
    ValueError : 
        if weights are given and frequency=False and any 
        of the weights are negative 
    """

# -------------------------------------------------
init_histogram.__doc__=\
    """Initialize a histogram structure 
    
    The returned structure can be passed to fill_histogram as the second argument 
    unraveled by a *
    
    Parameters
    ---------- 
    bins : array-like 
        Array of bin borders of length N+1 
    weighted : bool, optional 
        If true, then also include space for weighted filling
        
    Returns
    -------
    bins : array-like 
        The bin borders. Returned here so we can pass to fill_histogram 
    sumw : array-like 
        The N bin content holders 
    sumw2 : array-like or None 
        The N bin squared weights
        
    Examples
    -------- 
    
    >>> hist = init_histogram(np.linspace(-3,3,31))
        
    """

# -------------------------------------------------
fill_histogram.__doc__=\
    """Fill a histogram 
    
    If the histogram structure was made with init_histogram, 
    we can do 
    
    >>> hist = init_histogram(bins)
    >>> for x in data: 
    ...     hist = fill_histogram(x,hist)
    
    Parameters
    ----------
    x : float 
        Observation to record 
    bins : array-like 
        Bin borders 
    sumw : array-like 
        Summed bin count (or weights) 
    sumw2 : array-like (optional)
        Summed squared bin count (or weights)
    weight : float (optional)
        Weight of observation x. The interpretation of 
        this depends on whether no sumw2 is given or not
        
        If sumw2 is None, then this weight is assumed to be 
        a frequency weight. 
        
        If sumw2 is given, then the weight is assumed to be 
        a non-frequency weight 
            
    Returns
    -------
    bins : array-like 
        The bin borders 
    sumw : array-like 
        The updated sum bin count 
    sumw2 : array-like or none 
        the updates sum squared bin count 
    """


# -------------------------------------------------
fini_histogram.__doc__=\
    """Finalize histogram
    
    If the histogram structure was made using init_histogram, then 
    we can pass that as the first argument 
    
    >>> hist = init_histogram(bins)
    >>> for x in data: 
    ....    hist = fill_histogram(x,*hist)
    >>> fini_histogram(hist)
    
    Parameters
    ----------
    bins : array-like 
        Bin borders 
    sumw : array-like 
        Sum of bin count (weights)
    sumw2 : array-like (optional)
        Sum of squared bin count (weights)
    
    Returns
    ------- 
    h : array-like 
        Histogram 
    m : array-like 
        Bin centers 
    w : array-like 
        Bin widths 
    e : array-like 
        Uncertainty on bins 
    """

# -------------------------------------------------
Histogram.__doc__=\
    """A 1 dimensional histogram class
    
    The internal state
    ------------------
    - bins : array-like 
      The bin borders. Returned here so we can pass to fill_histogram 
    - sumw : array-like 
      The N bin content holders 
    - sumw2 : array-like or None 
      The N bin squared weights
    - hist : array-like, or None 
      Only filled after finalize has been called
    - uncer : array-like, or None
      Only filled after finalize has been called
            
    Initializes the histogram object

    Parameters
    ---------- 
    bins : array-like 
        Array of bin borders of length N+1 
    weighted : bool, optional 
        If true, then also include space for weighted filling    
    
    """
    
Histogram.fill.__doc__=\
    """Fill a histogram 

    Parameters
    ----------
    x : float 
        Observation to record 
    weight : float (optional)
        Weight of observation x. The interpretation of 
        this depends on whether no sumw2 is initialized or not
    
        If sumw2 is None, then this weight is assumed to be 
        a frequency weight. 
    
        If sumw2 is given, then the weight is assumed to be 
        a non-frequency weight 
    """
        
Histogram.finalize.__doc__=\
    """Finalize histogram
    
    Returns
    ------- 
    h : array-like 
        Histogram 
    m : array-like 
        Bin centers 
    w : array-like 
        Bin widths 
    e : array-like 
        Uncertainty on bins
    """

Histogram.bins.__doc__=\
    """Return bin limits"""

Histogram.centers.__doc__=\
    """Return the bin centers"""

Histogram.heights.__doc__=\
    """Return bin heights, possibly None"""

Histogram.widths.__doc__=\
    """Return bin widths"""

Histogram.uncertainties.__doc__=\
    """Uncertainties on bin heights, possibly None"""

Histogram.sums.__doc__=\
    """Returns sum of (weighted) observations"""

Histogram.sumWeightsSquare.__doc__=\
    """Return sum of square weighted observations or None"""

# -------------------------------------------------
def chi2nu(x,y,f,p,delta=None,deltax=None,df=None,df_step=None):
    from numpy import ones_like, sum, array, gradient, asarray
    if delta is None:
        delta = ones_like(y)
        
    if len(x) != len(y):
        raise ValueError("Inconsistent sizes of X and Y")
    
    if len(delta) != len(y):
        raise ValueError("Inconsistent sizes of Y and Delta")
    
    d2 = asarray(delta)**2
    if deltax is not None and len(deltax) == len(delta):
        d2 = effective_variance(x,deltax,f,p,d2,df,df_step)
        
    xnz = asarray(x)[d2>0]
    ynz = asarray(y)[d2>0]
    dnz = d2[d2>0]
    ret = sum([(yy - f(xx,*p))**2/dd 
               for xx,yy,dd in zip(xnz,ynz,dnz)],axis=0) 
    return ret, len(y)-len(p)

# -------------------------------------------------
def linfit(f,x,y,delta=None):
    from numpy import ones_like, matrix, array, dot
    from numpy.linalg import lstsq
    
    if delta is None:
        delta = ones_like(y)
        
    if len(x) != len(y):
        raise ValueError("X and Y must have equal length")
        
    fx = array([[fj(xi)/ey for fj in f] 
                for xi,ey in zip(x,delta)])
    
    p, *_ = lstsq(fx, y/delta,rcond=-1)
    
    pcov = matrix(dot(fx.T, fx)).I
    
    return p, pcov

# -------------------------------------------------
def plot_fit_table(p,ep,nsig=1,
                   chi2nu=None,pvalue=None,
                   parameters=None,**kwargs):
    from matplotlib.pyplot import gca
    from numpy import floor, log10, abs
    from scipy.stats import chi2 
    
    cells = []
    
    title  = kwargs.pop('title',{})
    if title:
        if isinstance(title,str):
            title = {'label':title}
        
    tit = title.get('label',None)
    if tit:
        cells  += [[tit,'','','','','']]
        
    # Calculate chi^2 and nu, and add to lines
    if chi2nu is not None:
        chisq, nu = chi2nu
        cells += [[r"$\chi^2/\nu$", "=", 
                   fr"${chisq:.1f}/{nu}$", "=",
                   fr"${chisq/nu:.2f}$", ""]]

        if pvalue is not None and pvalue:
            prob  =  chi2.sf(*chi2nu)
            cells += [[r"$P(\chi^2,\nu)$", "=",
                       "", "",
                       fr"${100*prob:.1f}$", r"$\%$"]]

    # Add parameter values to lines 
    if parameters is None:
        pars = {'label':'auto'}
    if isinstance(parameters,dict):
        pars = [parameters.copy() for _ in range(len(p))]
    elif len(parameters) < len(p):
        pars = parameters.copy() + \
               [{'label':'auto'} for _ in range(len(p)-len(parameters))]
    else:
        pars = parameters.copy()
        
    for pi in range(len(pars)):
        if isinstance(pars[pi],str):
            pars[pi] = dict(label=pars[pi])
        if not isinstance(pars[pi],dict):
            print('Warning, parameter options not dict')
        if 'label' not in pars[pi] or pars[pi]['label'] == 'auto':
            pars[pi]['label'] = f'p_{{{pi+1}}}'
    
    if ep is None:
        ep = [None]*len(p)
        pass 
        
    for pi, (pv, pe, po) in enumerate(zip(p, ep, pars)):
        if isinstance(po,str):
            po = dict(label=po)

        ns             =  po.get('nsig', nsig)
        pn             =  po.get('label')
        pt             =  po.get('expo',po.get('scale',None))
        pu             =  po.get('unit', '')
        rv,re,ndig,rx  =  round_result_expo(pv,pe,ns,expo=pt)
        expo           =  rx is not None and rx != 0
        unit           =  pu is not None and pu != ''
        lp,rp          =  ('(',')') if (unit or expo) and pe else ('','')
        pu             =  fr'$\times10^{{{rx}}}$ {pu}' if expo else pu
        pm             =  r'$\pm$'                     if pe else ''
        te             =  fr"${re[0]:.{ndig}f}{rp}$"   if pe else ''
        cells += [[fr"${pn}$", "=", fr"${lp}{rv:.{ndig}f}$", pm, te, pu]]

    axes = kwargs.pop('ax',   kwargs.pop('axes',gca()))
    col  = kwargs.pop('color','k')
    if 'edges' not in kwargs: kwargs['edges'] = ''
    if 'loc'   not in kwargs: kwargs['loc']   = 'best'
        
    tab = axes.table(cellText=cells,axes=axes,**kwargs)                  

    for i in range(6):
        tab.auto_set_column_width(i)
    
    align = ['left','center','right','center','left','left']
    
    for c,r in tab.get_celld():
        # print(c,r)
        tab[c,r]._loc = align[r]
        tab[c,r].set_text_props(color=col)
        
    if title is not None:
        tab[0,0].set_text_props(**title)
        tab[0,0].get_required_width = lambda r: 0
        
    return tab

# -------------------------------------------------
def plot_fit_func(x,f,p,cov,**kwargs):
    from matplotlib.pyplot import gca 
    from numpy import ndim, sqrt, diagonal
    
    ax      = kwargs.pop('ax',     gca())
    band    = kwargs.pop('band',   kwargs.pop('band_kw',True))
    
    fy = f(x,*p)
    if band and cov is not None:
        band_kw = {}
        if isinstance(band,dict):
            band_kw = band 
            
        bs = band_kw.pop('step_factor',1)
        ef = band_kw.pop('factor',     1)
        if 'alpha' not in band_kw: band_kw['alpha'] = 0.5
        if 'color' not in band_kw: band_kw['color'] = 'y'
        
        ee = cov 
        if ndim(cov) == 2:
            ee = sqrt(diagonal(cov))
            
        # f is a function of the parameters for the purpose 
        # of propagating uncertainties from the parameters
        fe = sqrt(propagate_uncertainty(lambda p:f(x,*p),p,ef*cov,bs*ee))
        ax.fill_between(x,fy-fe,fy+fe,**band_kw)
    
    
    return ax.plot(x,fy,**kwargs) # Plot fit

# -------------------------------------------------
def fit_plot(x,y,delta,f,p,ep,xdelta=None,df=None,**kwargs):
    
    from numpy import sqrt, isscalar, diag, ndim, shape, array, \
        atleast_1d, asarray, concatenate, diagonal
    from matplotlib.pyplot import gca
    from scipy.stats import chi2 as chi2
    
    def v2kw(v,strkey='label'):
        if isinstance(v,dict):
            return v
        if isinstance(v,str):
            return {strkey:v}
        return dict()
    
    axes  = kwargs.pop('axes',   gca())
    axes  = kwargs.pop('ax',     axes)
    ochi2 = kwargs.pop('chi2',   True)
    opval = kwargs.pop('pvalue', True)
    nsig  = kwargs.pop('nsig',   1)
    xx    = kwargs.pop('xeval',  x)
    
    pars  = kwargs.pop('parameters', kwargs.pop('pnames', []))
    legn  = kwargs.pop('legend',     kwargs.pop('leg_kw', True))
    band  = kwargs.pop('band',       kwargs.pop('band_kw',True))
    fit   = kwargs.pop('fit',        kwargs.pop('fit_kw', True))
    table = kwargs.pop('table',      kwargs.pop('tbl_kw', True))
    data  = kwargs.pop('data',       kwargs.pop('data_kw',True))
    depc  = kwargs.pop('pscales', False)
    if depc:
        print('Warning: pscales is deprecated, use parameters instead')
    
    
    if delta is None:
        delta = sqrt(y)
    
    if len(x) != len(y):
        raise ValueError("Inconsistent sizes of X and Y")
    if len(delta) != len(y):
        raise ValueError("Inconsistent sizes of Y and Delta")
    if not callable(f):
        raise ValueError("F is not callable")
    
    p  = atleast_1d(p)
    ee = None
    if ep is not None:
        ep = atleast_1d(ep)
        if ndim(ep) > 2:
            raise ValueError('Passed uncertainty dimensions larger than 2')
        elif ndim(ep) == 1:
            if ep.shape != p.shape:
                raise ValueError(f'Inconsistent sizes of P ({p.shape}) '
                                 f'and uncertainty on P ({ep.shape})')
            ep = diag(ep**2)
        elif ep.shape != (len(p),len(p)):
            raise ValueError(f'Inconsistent sizes of P ({p.shape}) '
                             f'and covariance on P ({ep.shape})')
        ee = sqrt(diagonal(ep))
        
    data_kw = v2kw(data)
    if xdelta is not None and 'xerr' not in data_kw:
        data_kw['xerr'] = xdelta

    dat = None
    if data:
        dat = axes.errorbar(x,y,delta,**data_kw)  # Plot the data
        
    
    # Eval function at points
    if 'xerr' in data_kw and xdelta is None:
        xdelta = atleast_1d(data_kw['xerr'])

    if xdelta is not None and xx is x:
        xx = concatenate(([xx[0]-xdelta[0]],xx,[xx[-1]+xdelta[-1]]))
        
    fit_kw = v2kw(fit)
    ft     = None
    if fit:
        ft = plot_fit_func(xx,f,p,ep,ax=axes,band=band,**fit_kw)
    
    tab = None
    if table:
        chisqnu = None
        if ochi2 or opval:
            chisqnu = chi2nu(x,y,f,p,delta,xdelta,df)
            
        tab = plot_fit_table(p,ee,chi2nu=chisqnu,pvalue=opval,ax=axes,
                             parameters=pars,nsig=nsig,**v2kw(table,'title'))
        
    leg = None
    leg_kw = v2kw(legn)
    if legn and ("label" in data_kw or "label" in fit_kw):
        if 'loc' not in leg_kw: leg_kw['loc'] = 'best'
        leg = axes.legend(**leg_kw)
        
    return (dat, fit, tab, leg)

# -------------------------------------------------
def residuals(x,y,f,p,ey=None):
    from numpy import atleast_1d, ones_like
    ee = ones_like(x) if ey is None else atleast_1d(ey)
    mm = ee != 0
    ee = ee[mm]
    xx = atleast_1d(x)[mm]
    yy = atleast_1d(y)[mm]
    rr = (y - f(x,*p)) / ee 
    return xx, rr 

# -------------------------------------------------
def residual_plot(x,y,f,p,cov=None,ey=None,**kwargs):
    from matplotlib.pyplot import plot, fill_between, gca
    from numpy import atleast_1d, ones_like, sqrt
    
    res = kwargs.pop('residuals',True)
    fun = kwargs.pop('function', True)
    ax  = kwargs.pop('ax',kwargs.pop('axes', gca()))
    
    def v2kw(v,strkey='label'):
        if isinstance(v,dict):
            return v
        if isinstance(v,str):
            return {strkey:v}
        return dict()
    
    ra = None
    if res:
        res_kw = v2kw(res)
        rx, r = residuals(x,y,f,p,ey)
        ra = plot(rx, r, **res_kw)
        
    fa = None
    if fun and cov is not None:
        fun_kw = v2kw(fun)
        if 'color' not in fun_kw: fun_kw['color'] = 'y'
        if 'alpha' not in fun_kw: fun_kw['alpha'] = 0.5
            
        ee = ones_like(x) if ey is None else atleast_1d(ey)
        mm = ee != 0
        ee = ee[mm]
        xx = atleast_1d(x)[mm]
        yy = atleast_1d(y)[mm]
        ff = sqrt(propagate_uncertainty(lambda p : f(xx,*p), p, cov)) / ee
        
        fa = fill_between(xx,-ff,ff,**fun_kw)
        
    return ra, fa

# -------------------------------------------------
def nsigma_contour2(a,b,ea,eb,rho,n=1,nstep=100):
    from numpy import array, sqrt, linspace, \
        pi, cos, sin, newaxis, atleast_1d
    va  = sqrt(1+rho)*array([ 1,  1])
    vb  = sqrt(1-rho)*array([-1,  1])
    cc  = array([a,b])
    t   = linspace(0,2*pi,nstep)[:,newaxis]
    ns  = atleast_1d(n)
    ret = []
    for nn in ns:
        cnt = nn/sqrt(2)*(cos(t)*va - sin(t)*vb)
        cnt[:,0] *= ea
        cnt[:,1] *= eb 
        cnt      += cc
        ret.append(cnt)
        
    if len(ret) == 1:
        return ret[0]
    
    return ret

# -------------------------------------------------
def nsigma_contour(p,cov,n=1,nstep=100):
    from numpy import tril_indices_from, newaxis, sqrt, diagonal
    var = diagonal(cov)
    rho = cov/sqrt(var[:,newaxis].dot(var[newaxis,:]))
    ret = [list() for _ in range(len(cov)-1)]
    for i,j in zip(*tril_indices_from(cov,-1)):
        a,  b  = p[j], p[i]
        ea, eb = sqrt(var[j]), sqrt(var[i])
        rhoab  = rho[j,i] # cov[j,i]/ea/eb
        ret[i-1].append(nsigma_contour2(a,b,ea,eb,rhoab,n,nstep))
        
    return ret

# -------------------------------------------------
def plot_nsigma_contour(p,cov,ns=1,nstep=100,fig_kw={},**kwargs):
    from matplotlib.pyplot import clabel, subplot2grid, plot, gca, gcf
    from matplotlib.contour import ContourSet
    from numpy import triu_indices, atleast_1d, min, max, ptp
    from numpy.ma import asarray 
    
    n      = len(p)-1
    ns     = atleast_1d(ns)
    pars   = kwargs.pop('parameters',kwargs.pop('pnames',None))
    
    gs_kw = kwargs.pop('gridspec_kw',{})
    if not 'wspace' in gs_kw: gs_kw['wspace'] = 0
    if not 'hspace' in gs_kw: gs_kw['hspace'] = 0
    
    sub_kw = kwargs.pop('fig_kw',kwargs.pop('subplots',{}))
    if not 'sharex' in sub_kw: sub_kw['sharex'] = 'col'
    if not 'sharey' in sub_kw: sub_kw['sharey'] = 'row'
    
    clbl = kwargs.pop('clabel',True)
    cleg = kwargs.pop('legend',False)
    if not isinstance(clbl,str):
        clbl = r'\sigma'
    if cleg and not isinstance(cleg,str):
        cleg = 'n'
        
    title = kwargs.pop('title','')
    vals  = kwargs.pop('values',True)
    
    if 'colors' in kwargs:
        if kwargs['colors'] == 'auto':
            kwargs['colors'] = ['C'+str(i) for i in range(len(ns))]
    elif 'cmap' not in kwargs:
        kwargs['cmap'] = 'tab10'
    
    if pars is None:
        pars = ['']*(n+1)
        
    def _one(a,cc,ns,clbl,cleg,**kwargs):
        cs = ContourSet(a,ns,cc,None,**kwargs)

        yrng = (min([ci[0][:,1].min() for ci in cc]),
                max([ci[0][:,1].max() for ci in cc]))
        xrng = (min([ci[0][:,0].min() for ci in cc]),
                max([ci[0][:,0].max() for ci in cc]))
        xdel = ptp(xrng)
        ydel = ptp(yrng)
        a.set_ylim(yrng[0]-.05*ydel,yrng[1]+.05*ydel)
        a.set_xlim(xrng[0]-.05*xdel,xrng[1]+.05*xdel)
            
        if clbl:
            clabel(cs,ns,fmt=lambda l: f'${l}{clbl}$')
        if cleg:
            return cs.legend_elements(cleg)
        
    cont   = nsigma_contour(p,cov,ns,nstep)
    if len(cont) == 1:
        ax = kwargs.pop('ax',gca())
        ax.set_title(title)
        fig = ax.figure
        ax  = [[ax]]
    else:
        fig = kwargs.pop('fig',gcf())
        ax  = fig.subplots(ncols=n,nrows=n,squeeze=False,
                           gridspec_kw=gs_kw,**sub_kw)
        fig.suptitle(title)
        for i,j in zip(*triu_indices(n,1)):
            ax[i,j].remove()
    
    
    def paren(t):
        return t if t == '' else f'({t})'
    
    def lbl(l):
        if isinstance(l,dict):
            return ' '.join([fr'${l.get("label","")}$',
                             fr'{paren(l.get("unit",""))}'])
        if isinstance(l,str):
            return fr'${l}$'
        return ''
    
    cnta = None
    para = None
    for i, (l, ar, ny) in enumerate(zip(cont, ax, pars[1:])):
        for j, (c, a, nx),  in enumerate(zip(l, ar, pars[:-1])):
            if not isinstance(c,list):
                c = [c]
            cc   = [[asarray(ci)] for ci in c]
            cnta = _one(a,cc,ns,clbl,cleg,**kwargs)    
            if vals: 
                a.plot(p[j],p[i+1],'ok')
                     
            if j == 0:
                a.set_ylabel(lbl(ny))
            if i == n - 1:
                a.set_xlabel(lbl(nx))
                
    if cnta is not None:
        o = (n+1)//2
        s = n//2
        if s > 0:
            # lax = subplot2grid((n,n),(0,o),rowspan=s,colspan=s)
            x1,y1,w1,h1 = ax[s-1,o].get_position().bounds
            x2,y2,w2,h2 = ax[0  ,-1].get_position().bounds
            xx = x1+0.015
            yy = y1+0.015
            ww = x2+w2-xx
            hh = y2+h2-yy
            lax = fig.add_axes((xx,yy,ww,hh))
            lax.axis('off')
        else:
            lax = ax[0][0]
        lax.legend(cnta[0],cnta[1])


# -------------------------------------------------
chi2nu.__doc__=\
"""Calculate the chi-square over the sample (x,y)
   for the model f with parameters p. 

Note, points where delta<0 are explicitly ignored

Parameters
----------
x : array-like 
    Independent variable, N long 
y : array-like 
    Dependent variable, N long 
delta : array-like (optional)
    Uncertainty on y or None
f : callable
    Our model function with signature f(x,a...)
p : array-like 
    Model parameters 

Returns
-------
chi2 : float 
    Calculated schi-square 
nu : int
    Number degrees of freedom
"""

# -------------------------------------------------
linfit.__doc__=\
"""Fit a linear model f to data

Parameters
----------
x : array-like, float 
    Independent variable of length N
y : array-like, float 
    Dependent variable of length N 
delta : array-like, float (optional)
    Uncertainties on y 
f : array-like, callable 
    Array of length Nf, of callables that 
    evaluate each term in the linear model

Returns
-------
p : array-like 
    Estiamte of the Nf parameters 
pcov : array-like 
    Covarience matrix of p's
"""

# -------------------------------------------------
plot_fit_table.__doc__ =\
"""Plot a fit table in the current (or passed) axes

Parameters
----------
p : array-like 
    Best-fit parameter values 
ep : array-like 
    Best-fit parameter uncertainties 
nsig : int (optional, default: 1)
    Number of significant digits to show each uncertainty with. 
    Values are rounded to the same precision 
chi2nu : (float,int) (optional, default None)
    If a tuple, then it must contain the value of 
    the chi^2 and number of degrees of freedom.
pvalue : bool (optional, default: True)  
    If true, add chi^2 probability to table 
parameters : sequence (optional, default: None)
    List of names of parameters, or dictionary of options.  
    If an entry is a dict, then it can have the keys 
    - label: name of the parameter. If auto then a default name is chosen
    - scale: Power of 10, or auto to scale by orders of magnitude 
    - unit:  Unit of the parameter. 
    - nsig:  Number of significant digits to round to 
    Generic names are used if none is given 
ax : Axes (optional, default: None)
    Axes to draw table in.  If none, draw in current axes. 
tit_kw : dict (optional)
    Dictionary of title font options 
    
"""


# -------------------------------------------------
plot_fit_func.__doc__ = \
"""Plot fit function with found parameters and (optional uncertainty band)

Parameters
----------
x : array-like 
    Where to evaluate the function 
f : callable 
    Function to call 
p : array-like 
    Found best-fit parameter values 
cov : array-like 
    Parameter errors or covariance matrix 
band : bool or dict 
    IF false, do not draw uncertainty band, otherwise 
    keyword arguments passed to band drawing procedure 
    
    Some special keywords 
    
    - step_factor: Stepping factor for numerial differentiation
    - factor: Scale factor on uncertainties (e.g., 2 means draw 2-sigma
      uncertainty band)
ax : Axes 
    Axes to draw in. If none, current axes 
kwargs : dict
    passed on to drawing procedure 

Returns
-------
fit : Artist 
    Artist of fit function drawn 
"""

# -------------------------------------------------
fit_plot.__doc__=\
"""Plot data and a fitted funtion

Parameters
----------
x : array-like 
    Independent variable of length N
y : array-like 
    Dependent variable of length N
delta : array-like 
    Uncertainty in y of length N
f : callable 
    Fitted function with signature f(x,a,...) 
p : array-like 
    Best-fit parameter values of length Nf
ep : array-like 
    Best-fit parameter uncertainties of length Nf, 
    or the covariance of the fitted parameters of size (Nf,Nf)
xdelta : array-like (optional)
    Uncertainty on x of length N.  If specified, these uncertainties 
    will be part of the chi^2 calculation and shown on the plot. 
    If these uncertainties are not to be part of the chi^2 calculation,
    pass this array as the value of the keyword "xerr" in `data_kw`.  
    Note, unless `xeval` is pass, this will change the range over which 
    the function is evaluated to include the left and right most 
    uncertainties of the data. 
parameters : sequence (optional, default: None)
    List of names of parameters, or dictionary of options.  
    If an entry is a dict, then it can have the keys 
    - label: name of the parameter. If auto then a default name is chosen
    - scale: Power of 10, or auto to scale by orders of magnitude 
    - unit:  Unit of the parameter. 
    - nsig:  Number of significant digits to round to 
    Generic names are used if none is given 
fit : bool or dict 
    If false, do not plot fit. Otherwise if a dictionary pass 
    these as keyword arguments to the fit plot call 
band : bool or dict 
    If false, do not plot uncertainty band. Otherwise pass 
    value as keyword arguments to the drawing routine. 
    - The keyword 'factor' applies a multiplicative factor 
      to the uncertainty band (e.g., factor=2 will draw 2-sigma 
      contour)
    - The keyword 'step_factor' value is applied for differentiation 
data : bool or dict 
    If false do not draw data.  Otherwise, pass as keyword 
    arguments to the drawing procedure 
legend : bool or dict 
    If false, do not draw legend. Otherwise, pass as keyword 
    arguments to the drawing procedure
table : bool or dict     
     If false, do not draw parameter table. Otherwise, pass as keyword 
    arguments to the drawing procedure
**kwargs: dict (optional)
    Other keyword arguments:

    xeval : array-like (optional)
        Specifies the independent variable (`x`) locations to evaluate 
        the function at.  If not specified the passed `x` locations 
        are used.  Here, one can pass for example the result of 
        `np.linspace(min,max,steps)` to plot the function with better 
        resolution than the pass data-points would allow. 
    nsig : int (optional)
        Number of significant digits to show parameters with
    pvalue : bool (optional)
        If true, show the chi^2 probability 
    chi2 : bool (optional) 
        If true, show chi^2
    axes : matplotlib.pyplot.Axes (optional)
        Axes object to plot in. If none given, then in current axes

Returns
-------
dat : Artist 
    Data artist 
fit : Artist 
    Fit artist 
tab : Artist 
    Table artist 
leg : Artist 
    Legend artist 
    """

plot_fit = fit_plot
plot_fit.__doc__ = "Alias for fit_plot"

# -------------------------------------------------
residuals.__doc__ =\
    """Calculate the residuals with respect to some function
    
    This will calculate the residuals of the data sample 
    
        {x_,y_,delta_i | i=1,...N}
        
    with respect to the function f(x,p), where p are the parameters of the function 
    
    Note, points with delta_i=0 are explicitly ignored 
    
    Parameters
    ----------
    x : array-like 
        Independent variable 
    y : array-like 
        Dependent variable 
    ey : array-like 
        Uncertainty on y 
    f : callable 
        function 
    p : array-like 
        function parameters 
        
    Returns
    --------
    x : array-like 
        Places where the residuls have been evaluated 
    r : array-like 
        Residuals
    """

# -------------------------------------------------
residual_plot.__doc__ = \
"""Plot the residuls and uncertainty on function 


Parameters
----------
    x : array-like 
        Independent variable 
    y : array-like 
        Dependent variable 
    ey : array-like 
        Uncertainty on y 
    f : callable 
        function 
    p : array-like 
        function parameters
    cov : array-like 
        Uncertainty or covariance in parameters 
    **kwargs : dict 
    
        function : str or dict 
            Label or dictionary of keys for function drawing 
        residuals : str or dict 
            Label or dictionary of keys for residual drawing 
    
Returns
--------
    Tuple of drawn artist or none 
"""

plot_residuals = residual_plot
plot_residuals.__doc__ = "Alias for residual_plot"

# -------------------------------------------------
nsigma_contour2.__doc__=\
"""Calculate the two parameter n-sigma contour 

Parameters
----------
a : float 
    First parameter value 
b : float 
    Second parameter value 
ea : float 
    Uncertainty on the first parameter value 
eb : float 
    Uncertainty on the second parameter value 
rho : float 
    Correlation coefficient between a and b 
n : float 
    n times sigma contour to calculate 
nstep : int 
    Number of steps to take when evaluating ellipsis

Returns
-------
cont : 2-tuple of arrays 
    a and b coordinates of the contour 
"""

# -------------------------------------------------
nsigma_contour.__doc__=\
"""Calculate all n-sigma contours 

Parameters
----------
p : array like 
    Parameter valus 
cov : array-like 
    Covariance matrix of parameters 
n : float 
    Number of sigma contour to calculate 
nstep : int 
    Number of steps when calculating contour 
    
Returns
-------
cont : list 
    Triangular list of confidence contours for n-sigm 
"""

# -------------------------------------------------
plot_nsigma_contour.__doc__=\
"""Plot nsigma contour lines 

Parameters
----------
p : array-like 
    Parameter valus
cov : array-like 
    Covariance matrix of parameters 
ns : scalar, list 
    Factors of sigma to show 
nstep : int 
    Number of steps in parameterisation of ellipsis 
fig_kw : dict 
    Keywards to pass to subplots 
parameters : list of str or dict 
    Parameter names or parameters (see also fit_plot)
kwargs : dict 
    
    title : str 
        Title of plot_nsigma_contour
    values : bool 
        Whether to plot values aswell 
    clabel : bool, str 
        Whether to label contours directly in plot 
    legend : bool, str 
        Wheter to produce a legend 
    
    Other keywords are passed on to ContourSet 

"""

# -------------------------------------------------
def eval_cdf(f,x):
    from itertools import accumulate
    dxfx = (x[1:]-x[0:-1]) * f((x[0:-1]+x[1:])/2)
    cf   = list(accumulate(dxfx))
    mf   = min(cf)
    return [0]+[(s-mf) / (cf[-1]-mf) for s in cf]

# -------------------------------------------------
def sample_pdf(y,x,cdf):
    from bisect import bisect_left as bi
    from numpy import isclose
    def find_inter(y):
        if not (x[0] <= y <= x[-1]):
            raise ValueError
        
        i = bi(cdf,y)
        # print("{:.4g} -> {:3d}".format(y, i))
        
        if i >= len(cdf):
            raise ValueError
            
        if isclose(cdf[i],y):
            return x[i]
        
        yf = (y - cdf[i-1]) / (cdf[i]-cdf[i-1])
        return x[i-1]+yf*(x[i]-x[i-1])
        
        
    return [find_inter(yy) for yy in y]

# -------------------------------------------------
eval_cdf.__doc__=\
    """Integrates the PDF f over the range x to get a table of the CDF

    Parameters
    ----------
      f : callable 
        PDF to integrate 
      x : array-like
        Points to evalute the PDF af 

    Returns
    -------
      table of CDF values at the points x 
    """

# -------------------------------------------------
sample_pdf.__doc__=\
    """Sample a PDF given by the table of the CDF

    Parameters
    ----------
      y : scalar or array-like, float
        Uniformly distributed random variable 
      x : array-like
        Points where the CDF is evaluated 
      cdf : array-like 
        CDF evaluated at x 

    Return
    ------
      x : scalar or array-like, float 
        Random variable drawn from the PDF 
    """

# -------------------------------------------------
def mlefit(f,data,p0,*args,**kwargs):
    from scipy.optimize import minimize, LbfgsInvHessProduct
    from numpy import log, where, errstate, inf, atleast_1d, isnan
    
    logpdf  = kwargs.pop('logpdf',False)
    fullout = kwargs.pop('full_output',False)
    
    def llh(p,data=data):
        with errstate(all='ignore',invalid='ignore'):
            fx = atleast_1d(f(data,*p))
            if not logpdf:
                fx = where(fx>0,log(fx),-inf)
            fx[isnan(fx)] = -inf
            r = - fx.sum(axis=0)
        return r
    
    opt = minimize(llh, p0, *args, **kwargs)
    p   = opt.x 
    cov = getattr(opt,'hess_inv',None) 
    if isinstance(cov,LbfgsInvHessProduct):
        cov = cov.todense()
        
    if not fullout:
        return p, cov
    
    return p, cov, opt

# -------------------------------------------------
mlefit.__doc__=\
    """Do an MLE estimate of parameters of the PDF given data yield
    
    This will minimize the negative log-likelihood to find the most
    probable parameter values given the PDF `f` and the observations 
    `y`.  The parameter `x0` is the initial guess. If the keyword 
    `logpdf=True`, then `f` is assumed to return the logarithm of the 
    PDF 
    
    Parameters
    ----------
    f : callable 
        The PDF 
    x : array-like 
        The observations 
    p0 : array-like, size N 
        The initial guess of the parameter values 
    logpdf : bool 
        If set to true, assume `f` returns the logarithm of the PDF 
    full_output : bool 
        If set to true, return full minimizer output too 
    *args : tuple 
        Arguments passed on to `scipy.optimize.minimize` 
    **kwargs : dict 
        Keyword arguments passed on to `scipy.optimize.minimize`
    
    Returns
    -------
    p : array-like, size N 
        MLE of the parameter values 
    cov : array-like size N*N 
        Covariance matrix of parameters (inverse Hessian) if 
        available from the minimizer, otherwise Non 
    opt : dict-like 
        Full minimizer output of `full_output` is true 

    """

# -------------------------------------------------
def curve_fit(f,x,y,p0,dy=None,dx=None,df=None,df_step=None,
              ftol=1.49012e-8,ptol=1.49012e-8,**kwargs):
    from scipy.optimize import curve_fit as  cfit 
    from scipy.misc import derivative as diff
    from numpy import gradient as grad 
    from numpy import sqrt, isclose, allclose, hstack, isscalar, atleast_1d
    from scipy.linalg import norm
    
    kwargs['xtol'] = ptol
    kwargs['ftol'] = ftol
    rful = kwargs.get('return_full',None)
    
    xx  = atleast_1d(x) 
    yy  = atleast_1d(y) 
    ddy = atleast_1d(dy) if dy is not None else None
    ddx = atleast_1d(dx) if dx is not None else None
    if ddy is not None:
        mask = dy != 0
        xx   = xx[mask]
        yy   = yy[mask]
        ddy  = ddy[mask]
        ddx  = ddx[mask] if ddx is not None else None
        
    r0 = cfit(f,xx,yy,p0,sigma=ddy,**kwargs)
    
    if ddx is None:
        return r0
    
    if df_step is not None and isinstance(df_step,str):
        if df_step != 'deltax':
            raise ValueError('Unknown step method: '+df_step)
        df_step = dx
    elif df_step is None:
        df_step = 1
        
    dds    = df_step
    rold   = r0
    fold,_ = chi2nu(xx,yy,f,rold[0],ddy)
    while True:
        pold, covold, *_ = rold
        eff    = sqrt(effective_variance(xx,ddx,f,pold,ddy,df,df_step))
        rnew   = cfit(f,xx,yy,p0,sigma=eff,**kwargs)
        fnew,_ = chi2nu(xx,yy,f,rnew[0],eff)
        
        if isclose(fnew,fold,rtol=ftol,atol=0):
            return rnew 
        
        dp  = rnew[0]-pold 
        ndp = norm(dp)
        np  = norm(pold)
        
        if ndp < (ptol * (ptol + np)):
            return rnew 
        
        rold = rnew 
        fold = fnew

# -------------------------------------------------
def fit(f,*args,**kwargs):
    try:
        iter(f)
        return linfit(f,*args,**kwargs)
    except:
        pass 
    
    if len(args) < 3:
        return mlefit(f,*args,**kwargs)
    
    return curve_fit(f,*args,**kwargs)

# -------------------------------------------------
curve_fit.__doc__=\
    """Perform a non-linear least squares fit of f to data
    
    Note, if dy is given, then any element for which dy is zero 
    are filtered out of the fit (does not make sense to include,
    since the scaled residual would be infinite)
    
    Parameters
    ----------
    f : callable 
        The model to fit with the signature `f(x,...)`
    x : array-like shape=(M) or (k,M)
        Independent variable values or predictors and variable values
    y : array-like shape=(M)
        Dependent variable values 
    p0 : array-like shape=(N)
        Initial guess of parameter values 
    dy : array-like shape=(M) or shape=(M,M)
        Uncertainties in `y` or covariance matrix of uncertainties in `y`
    dx : array-like shape=(M), or None
        Uncertainties in `x`.  If specified, we will employ an 
        iterative procedure using the *effective variance* method 
        to include these uncertainties in the fit. 
    df : callable, or None 
        If `dx` is given, then this argument is supposed to 
        calculate the derivative of f with respect to x.  This 
        will then be evaluated at all `x` for the current 
        parameter values. 
    dx_step : scalar, array, string, or None 
        If given, the step size to use when calculating the derivative
        of f with respect to x for calculating the effective variance 
        (in case dx was given).   If the value is the string 'deltax', then
        use dx for the step size.  If None, use 1 as the step size.  If df 
        is given, then this is not used. 
    ftol : float, optional 
        Tolerance criteria for terminating iterative procedure. 
        If the change in the chi-square (dchi2) fulfills 
        
            dchi2 < ftol * chi2
          
        then the procedure is stopped.  This is also passed on to 
        `scipy.optimize.curve_fit` 
    ptol : float, optional 
        Tolerance criteria for terminating iterative procedure. 
        If the change in the parameter values (dp) fulfills 
        
            abs(dp) < ptol * (ptol + abs(p))
            
        then the procedure is stopped. This is also passed on to 
        `scipy.optimize.curve_fit` as the parameter `xtol`. 
    **kwargs : dict 
        Additional arguments passed to `scipy.optimize.curve_fit`
        
    Returns 
    -------
    p : array-like shape=(N) 
        Best estimate of parameter values 
    cov : array-like, shape=(N,N)
        Covariance matrix of parameters 
    """

# -------------------------------------------------
fit.__doc__=\
"""Unified interface for curve fitting 

This function provides a unified interface for fitting 
functions to data.  Exactly which kind of fit is used depends on 
the data passed.  

- If the function we provide is of the form
 
      f(x,p) = sum_i^M p_i f_i(x)
  
  given as the sequence (f_1,...,f_M), we perform a linear curve fitting, 
  where they follow arguments are 
  
  - The independent variable x
  - The dependent variable y 
  - Optionally, the uncertainties delta 
  
- Otherwise, if the number of the following arguments is less than 3, 
  then we perform an MLE curve fitting, where the arguments are
  
  - The observations p
  - The initial values p_0 of the parameters
  
- If none of the above conditions are met, we perform a least-squares curve fit with the
  subsequent arguments
  
  - The independent variable x
  - The dependent variable y 
  - The initial values p_0 of the parameters
  - Optionally, the uncertainties delta_y
  - Optionally, the uncertainties delta_x
  

Other arguments or keyword arguments are passed to the underlying functions. 

Parameters
----------
f : callable or sequence of callables 
    Function to fit to data 
args : tuple 
    Further arguments 
kwargs : dict 
    Keyword arguments
"""

if __doc__ is not None:

    __doc__ += \
"""
2020-02-15 00:56:31.648146 UTC
"""

#
# EOF
#
