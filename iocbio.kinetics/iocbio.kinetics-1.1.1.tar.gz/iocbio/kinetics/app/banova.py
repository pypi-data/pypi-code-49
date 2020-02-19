# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
#  Copyright (C) 2019-2020
#   Laboratory of Systems Biology, Department of Cybernetics,
#   School of Science, Tallinn University of Technology
#  This file is part of project: IOCBIO Kinetics
#
#!/usr/bin/env python3

"""Analysis of the models using Bayes ANOVA

Application and routines for analysis of statistical significance
using Bayes ANOVA. Routines provide convinient interface for R
routines through Python.
"""

from rpy2.robjects.packages import importr
import rpy2.robjects as robjects
from tabulate import tabulate
import copy, textwrap

# r imports
base = importr('base')
bf = importr('BayesFactor')
dplyr = importr('dplyr')
ftools = importr('formula.tools')
gg = importr('ggplot2')
stats = importr('stats')
utils = importr('utils')

def star(v):
    """
    Statistical evidence categories for Bayes Factor

    Returns
    -------
    str
      For Bayes Factors larger than 1, returns a string
      with the number of stars corresponding to common interpretation
      of the Bayes Factor.
    """
    if v > 100: return "***"
    elif v > 30: return "**"
    elif v > 10: return "*"
    # elif v < 1.0/100: return "***"
    # elif v < 1.0/30: return "**"
    # elif v < 1.0/10: return "*"
    return " "

class _Model:

    def index(i):
        mi = []
        for sl in i.split('+'):
            s = sl.strip()
            mt = [k for k in s.split(':')]
            mt = set(mt)
            mi.append(mt)
        mi.sort()
        return mi

    def __init__(self, i, v):
        self.i = i
        self.v = v
        self.ind = _Model.index(i)

    def _has_factor(self, fi):
        for k in self.ind:
            if fi == k: return True
        return False

    def has_max_factor(self, f):
        fi = _Model.index(f)[0]
        if not self._has_factor(fi): return False
        for k in self.ind:
            if fi < k: return False
        return True

    def conjugate(self, f, other):
        fi = _Model.index(f)[0]
        if len(other.ind) != len(self.ind)-1: return False
        if other._has_factor(fi): return False
        for i in other.ind:
            if not self._has_factor(i):
                return False
        return True

def _printTable(res, colsIni = []):
    cols = list(res.names)
    tab = []
    for i in res:
        c = []
        vlast = None
        for j in range(len(i)):
            if hasattr(i, 'levels'): v = i.levels[i[j]-1]
            else: v = i[j]
            if len(c) > 0 and vlast == v: v = ''
            else: vlast = v
            c.append(v)
        tab.append(c)
    order = [cols.index(c) for c in colsIni]
    for i,c in enumerate(cols):
        if c not in colsIni:
            order.append(i)
    tab = [tab[i] for i in order]
    cols = [cols[i] for i in order]
    print(tabulate(list(map(list, zip(*tab))), headers=cols), '\n')


def analyze_r(robj):
    """Analyze BANOVA results as obtained in R

    As an input, use result from anovaBF. This routine is written for
    internal use by the other functions in the module.
    """
    result = base.as_vector(robj)
    models = result.names
    res = { 'id': _Model('id', 1) }
    table = [ ["Model", "BF", ""] ]
    best = None
    for i in models:
        v = result.rx(i)[0]
        res[i] = _Model(i, v)
        table.append([i, v, star(v)])
        if best is None or res[i].v > best.v:
            best = res[i]

    if best.v < 1:
        best.i = None
        best.v = 1

    print(tabulate(table[1:], headers=table[0], floatfmt='.2g') + "\n")

    print('Best model')
    print(best.i, '    ', '{:.2g}'.format(best.v), '\n')

    factors = set()
    for k in res:
        for s in k.split('+'):
            factors.add(s.strip())

    factors = list(factors)
    factors.sort()
    mkeys = list(res.keys())
    mkeys.sort()

    ftable = [ ['Factor', 'BF', ''] ]
    for f in factors:
        fin = 0
        fout = 0
        for m in mkeys:
            if res[m].has_max_factor(f):
                win = m
                wout = None
                for o in mkeys:
                    if res[m].conjugate(f, res[o]):
                        wout = o
                if wout is not None:
                    fin += res[win].v
                    fout += res[wout].v

        if fin > 0:
            v= fin/fout
            ftable.append([f, v, star(v)])

    print(tabulate(ftable[1:], headers=ftable[0], floatfmt='.2g') + "\n")

    return best, ftable, tabulate(ftable[1:], headers=ftable[0], floatfmt='.2g')


def print_stats(keys, sample_id, value):
    skeys = copy.copy(keys)
    if sample_id is not None: skeys.remove(sample_id)
    groupnames = skeys[0]
    for i in skeys[1:]: groupnames += ", " + i

    print('\nMinimal values')
    _printTable(robjects.r('data %>% group_by(' + groupnames + ') %>% top_n(n=-3,' +
                           value + ') %>% arrange(' + groupnames + ", desc(" + value + '))'), colsIni = skeys)
    print('\nMaximal values')
    _printTable(robjects.r('data %>% group_by(' + groupnames + ') %>% top_n(n=3,' +
                           value + ') %>% arrange(' + groupnames + "," + value + ')'), colsIni = skeys)

    rcmd = 'data %>% group_by('
    rcmd += groupnames + ') %>% ' +  ('summarize(mean=mean(%s), sd=sd(%s), med=median(%s), min=min(%s), max=max(%s), n=n())' % (value, value, value, value, value))
    print('Mean values across the groups\n')
    _printTable(robjects.r(rcmd))


def plot_stats(plot, keys, sample_id, value, caption):
    robjects.r('pdf(file="%s")' % plot)

    skeys = copy.copy(keys)
    if sample_id is not None: skeys.remove(sample_id)

    rcmd = "ggplot(data=data, mapping = aes(y=" + value + ", x=" + skeys[0]
    jitter = ""
    if len(skeys) > 1:
        rcmd += ", fill=" + skeys[1]
        jitter = "position=position_jitterdodge()"
    rcmd += ")) + theme(plot.caption = element_text(hjust=0, family = 'mono')) + labs(title='" + value + "', caption='" + caption + "')"
    point =  "+ geom_point(" + jitter + ")"
    boxplot = " + geom_boxplot(outlier.shape = NA)"
    facet = ""
    if len(skeys) >= 3:
        facet = ' + facet_grid(' + skeys[2] + '~'
        if len(skeys) >= 4:
            facet += skeys[3]
        else:
            facet += '.'
        if len(skeys) >= 5:
            for i in skeys[4:]: facet += '*' + i
        facet += ')'

    plt = robjects.r(rcmd + boxplot + point + facet)
    base.print(plt)

    plt = robjects.r(rcmd + boxplot + facet)
    base.print(plt)

    plt = robjects.r(rcmd + " + geom_violin(draw_quantiles = c(0.5)) " + facet)
    base.print(plt)

    if len(facet) > 0:
        plt = robjects.r(rcmd + boxplot + facet[:-1] + ', shrink=TRUE, scales="free_y")')
        base.print(plt)

    robjects.r('dev.off()')


def analyze_dict(data, keys = None, sample_id = None, value = None, nullmodel = None, plot = None):
    """BANOVA analysis of a dataset in the form of dictionary with list of vectors"""

    if value is None:
        raise NameError('Specify value key for analysis')

    if keys is None or len(keys)==0:
        keys = list(data.keys())

    if value in keys: keys.remove(value)
    if sample_id is not None and sample_id not in keys:
        keys.append(sample_id)

    if len(keys) > 5:
        raise NotImplementedError('I have found too many keys for analysis. Keys found: ' + str(keys))

    dataFrame = {}
    for k in data.keys():
        if isinstance(data[k][0], int):
            rrr = robjects.IntVector(data[k])
        elif isinstance(data[k][0], str):
            rrr = robjects.StrVector(data[k])
        else:
            rrr = robjects.FloatVector(data[k])
        if k in keys:
            dataFrame[k] = base.factor(rrr)
        else:
            dataFrame[k] = rrr

    dataFrame[value] = robjects.FloatVector(data[value])
    dataFrame = robjects.DataFrame(dataFrame)
    robjects.globalenv['data'] = robjects.DataFrame(dataFrame)

    if nullmodel is None and sample_id is None:
        return _analyze_dict_banova(keys=keys, sample_id=sample_id, value=value, plot=plot)

    def model_terms(m, null=None):
        nt = model_terms(null) if null is not None else []
        terms = []
        for t in base.attr(stats.terms(m), "term.labels"):
            l = t.split(':')
            l.sort()
            tt = ':'.join(l)
            if tt not in nt: terms.append(tt)
        terms.sort(key = lambda val: str(val.count(':')) + ' ' + val)
        return terms

    def model_name(m, null=None):
        t = model_terms(m, null)
        if len(t) == 0: return model_name(m)
        val = ftools.lhs_vars(m)[0]
        name = val + ' ~ ' + ' + '.join(t)
        if null is not None: name += ' + NULL'
        return name

    # prepare formulas
    wR = sample_id
    studied_model = value + " ~ " + keys[0]
    for k in keys[1:]:
        if k != sample_id:
            studied_model += "*" + k
    if sample_id is not None:
        studied_model += " + " + sample_id

    null_model = value + " ~ "
    null_model_terms = []
    if nullmodel is not None: null_model_terms.append(nullmodel)
    if sample_id is not None: null_model_terms.append(sample_id)
    null_model += ' + '.join(null_model_terms)

    studied_model = stats.formula(studied_model)

    # set null_model as a most expanded version of it
    nm = []
    for i in bf.enumerateGeneralModels(stats.formula(null_model), whichModels = "withmain"):
        m = model_terms(i)
        if len(m) > len(nm):
            null_model = i
            nm = m

    # find models that are more complicated than the null_model
    models = [null_model]
    null_set = set(model_terms(null_model))
    for i in bf.enumerateGeneralModels(studied_model, whichModels = "withmain"):
        m = set(model_terms(i))
        if null_set.issubset(m) and null_set != m:
            models.append(i)

    print('Random factor, sample_ID:', wR)
    print('Models to study:', len(models))

    lmbf_args = dict(data=dataFrame, progress=False)
    if wR is not None: lmbf_args['whichRandom'] = wR

    null_bf = bf.lmBF(null_model, **lmbf_args)
    print('Null calculated:',  model_name(null_model))

    # Calculate model BFs
    results = {}
    robjects.globalenv['nullBF'] = null_bf
    for m in models:
        mbf = bf.lmBF(m, **lmbf_args)
        pretty = model_name(m, null_model)
        robjects.globalenv['mbf'] = mbf
        robjects.r('relmbf = as.vector(mbf/nullBF)')
        factor = robjects.globalenv['relmbf'].rx(1)[0]
        print(pretty, '{:.3g}'.format(factor))
        results[pretty] = { 'factor': factor,
                            'name': pretty,
                            'short': pretty.split('~')[1].strip(),
                            'terms': set(model_terms(m)) }

    print()
    print_stats(keys=keys, sample_id=sample_id, value=value)

    # print BANOVA results
    table = [ ["Model", "BF", ""] ]
    best = None
    for i,v in results.items():
        f = v['factor']
        table.append([v['short'], f, star(f)])
        if best is None or f > best['factor']:
            best = v

    if best['factor'] < 1:
        best['name'] = 'Null: ' + model_name(null_model)
        best['factor'] = 1

    print('Null model:', model_name(null_model), '\n')
    print(tabulate(table[1:], headers=table[0], floatfmt='.2g') + "\n")

    print('Best model:', 'BF = {:.2g}'.format(best['factor']), '\n')
    print(best['name'], '\n')

    # get factors
    factors = set()
    for i,v in results.items():
        factors.update(v['terms'])
    factors.difference_update(null_set)
    factors = list(factors)
    factors.sort(key = lambda val: str(val.count(':')) + ' ' + val)

    def hasmaxfactor(f, terms):
        if f not in terms: return False
        fset = set(f.split(':'))
        for k in terms:
            kset = set(k.split(':'))
            if fset != kset and fset.issubset(kset):
                return False
        return True

    ftable = [ ['Factor', 'BF', ''] ]
    for f in factors:
        fin = 0
        fout = 0
        for i,v in results.items():
            terms = copy.copy(v['terms'])
            if hasmaxfactor(f, terms):
                terms.remove(f)
                for k,c in results.items():
                    if c['terms'] == terms:
                        fin += v['factor']
                        fout += c['factor']
        if fin > 0:
            v = fin/fout
            ftable.append([f, v, star(v)])
        else:
            print('Something is wrong, cannot calculate contribution of', f)

    print(tabulate(ftable[1:], headers=ftable[0], floatfmt='.2g') + "\n")

    if plot is not None:
        caption = 'Null model: ' + model_name(null_model) + '\n\n' + \
            'Best model: BF = {:.2g}\n\n'.format(best['factor'])+ "\n".join(textwrap.wrap(best['name'])) + '\n\n' + \
            tabulate(ftable[1:], headers=ftable[0], floatfmt='.2g')
        plot_stats(plot=plot, keys=keys, sample_id=sample_id, value=value, caption=caption)


def _analyze_dict_banova(keys = None, sample_id = None, value = None, plot = None):
    """BANOVA analysis of a dataset in the form of dictionary with list of vectors"""

    rcmd = "av = anovaBF(" + value + " ~ " + keys[0]
    for k in keys[1:]:
        if k != sample_id:
            rcmd += "*" + k
    if sample_id is not None:
        rcmd += " + " + sample_id + (", whichRandom='%s'" % sample_id)
    rcmd += ",progress=TRUE, data=data)"
    print(rcmd)
    robjects.r(rcmd)
    print(robjects.r['av'], '\n')

    # tables
    print()
    print_stats(keys=keys, sample_id=sample_id, value=value)

    best, _, fprint = analyze_r(robjects.r['av'])

    if plot is not None:

        caption = 'Best model:\n'
        if best.i is None:
            caption += 'Null model was the best'
        else:
            caption += "\n".join(textwrap.wrap(value + " ~ " + best.i)) + '\nBF = {:.2g}'.format(best.v) + '\n' + fprint
        plot_stats(plot=plot, keys=keys, sample_id=sample_id, value=value, caption=caption)

def analyze_rows(rdict, keys = None, sample_id = None, value = None, nullmodel = None, plot = None):
    """BANOVA analysis of BANOVA a dataset in the form of iterative of dictionaries

    Analysis is performed on the iterative, as returned by DictReader and records SQL query
    """

    import collections

    # copy data
    data = collections.defaultdict(list)
    for r in rdict:
        for k in r.keys():
            data[k].append(r[k])

    return analyze_dict(data, keys = keys, sample_id = sample_id, value = value, nullmodel = nullmodel, plot = plot)


def analyze_sql(sql, keys = None, sample_id = None, value = None, nullmodel = None, plot = None):
    """BANOVA analysis of a dataset loaded from the database"""
    from iocbio.kinetics.app.fetch import fetch

    return analyze_rows( fetch(sql),
                         keys = keys, sample_id = sample_id, value = value, nullmodel = nullmodel, plot = plot )


def main():
    import argparse
    parser = argparse.ArgumentParser(description='Analyze data using Bayes ANOVA',
                                     epilog = 'To specify database, user name and password, ' + \
                                     'use "iocbio-kinetics --db"',
                                     formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('sql_file', type=str, help='Input SQL query file')
    parser.add_argument('--id', type=str, help='Column name with sample ID (cellid or similar which is the same for repeated measures)')
    parser.add_argument('-v', '--value', type=str, required=True, help='Column name measurement value')
    parser.add_argument('-n', '--nullmodel', type=str, default=None, help='Null model, excluding sample ID. Only the right side is specified. For example, amp*iso will expand into amp + iso + amp*iso + sample_ID')
    parser.add_argument('-p', '--plot', type=str, help='Plot filename')
    parser.add_argument('keys', nargs='*', type=str, help='Column names with fixed variables')

    args = parser.parse_args()

    # opening sql file
    with open(args.sql_file, 'r') as f:
        s = f.read()

    analyze_sql( sql=s, keys = args.keys, sample_id = args.id,
                 value = args.value, nullmodel = args.nullmodel, plot = args.plot )



# if run as a script
if __name__ == '__main__':
    main()
