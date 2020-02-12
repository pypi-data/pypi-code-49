import os
import sys

import numpy as np
import scipy.sparse as sparse
import pandas as pd

from lib5c.util.system import check_outdir
from hiclite.steps.filter import filter_sparse_rows_count
from hiclite.steps.balance import kr_balance

from hic3defdr import HiC3DeFDR
from hic3defdr.logging import eprint
from hic3defdr.clusters import load_clusters
from hic3defdr.progress import tqdm_maybe as tqdm
from hic3defdr.simulation import simulate


class NoBiasFast3DeFDR(HiC3DeFDR):
    def simulate(self, cond, chrom=None, beta=0.5, p_diff=0.4, trend='mean',
                 outdir='sim'):
        """
        Simulates raw contact matrices based on previously fitted scaled means
        and dispersions in a specific condition.

        This function will only work when the design has exactly two conditions
        and equal numbers of replicates per condition.

        Can only be run after ``estimate_dispersions()`` has been run.

        Parameters
        ----------
        cond : str
            Name of the condition to base the simulation on.
        chrom : str, optional
            Name of the chromosome to simulate. Pass None to simulate all
            chromosomes in series.
        beta : float
            The effect size of the loop perturbations to use when simulating.
            Perturbed loops will be strengthened or weakened by this fraction of
            their original strength.
        p_diff : float
            This fraction of loops will be perturbed across the simulated
            conditions. The remainder will be constitutive.
        trend : 'mean' or 'dist'
            The covariate against which dispersion was fitted when calling
            ``estimate_disp()``. Necessary for correct interpretation of the
            fitted dispersion function as a function of mean or of distance.
        outdir : str
            Path to a directory to store the simulated data to.
        """
        if chrom is None:
            for chrom in self.chroms:
                self.simulate(cond, chrom=chrom, beta=beta, p_diff=p_diff,
                              outdir=outdir)
            return
        eprint('simulating data for chrom %s' % chrom)
        # load everything
        bias = self.load_bias(chrom)
        size_factors = self.load_data('size_factors', chrom)
        row = self.load_data('row', chrom)
        col = self.load_data('col', chrom)
        scaled = self.load_data('scaled', chrom)[:, self.design[cond]]
        disp_fn = self.load_disp_fn(cond, chrom)
        clusters = load_clusters(
            self.loop_patterns[cond].replace('<chrom>', chrom))

        # compute pixel-wise mean of normalized data
        mean = np.mean(scaled, axis=1)

        # book keeping
        check_outdir('%s/' % outdir)
        n_sim = size_factors.shape[-1]
        repnames = sum((['%s%i' % (c, i+1) for i in range(n_sim/2)]
                        for c in ['A', 'B']), [])

        # write design to disk if not present
        design_file = '%s/design.csv' % outdir
        if not os.path.isfile(design_file):
            pd.DataFrame(
                {'A': [1]*(n_sim/2) + [0]*(n_sim/2),
                 'B': [0]*(n_sim/2) + [1]*(n_sim/2)},
                dtype=bool,
                index=repnames
            ).to_csv(design_file)

        # overwrite bias and size factors
        bias = np.ones_like(bias, dtype=float)
        size_factors = np.ones(size_factors.shape[1])

        # rewrite size_factor matrix in terms of distance
        if len(size_factors.shape) == 2:
            eprint('  converting size factors')
            dist = col - row
            n_dists = dist.max() + 1
            new_size_factors = np.zeros((n_dists, size_factors.shape[1]))
            for d in tqdm(range(n_dists)):
                idx = np.argmax(dist == d)
                new_size_factors[d, :] = size_factors[idx, :]
            size_factors = new_size_factors

        # scramble bias and size_factors
        bias = bias[:, (np.arange(n_sim)+1) % n_sim]
        if len(size_factors.shape) == 1:
            size_factors = size_factors[(np.arange(n_sim)+3) % n_sim]
        else:
            size_factors = size_factors[:, (np.arange(n_sim)+3) % n_sim]

        # simulate and save
        classes, sim_iter = simulate(
            row, col, mean, disp_fn, bias, size_factors, clusters, beta=beta,
            p_diff=p_diff, trend=trend)
        np.savetxt('%s/labels_%s.txt' % (outdir, chrom), classes, fmt='%s')
        for rep, csr in zip(repnames, sim_iter):
            sparse.save_npz('%s/%s_%s_raw.npz' % (outdir, rep, chrom), csr)


repnames = ['ES_1', 'ES_3', 'NPC_2', 'NPC_4']
chroms = ['chr19']
base_path = 'c:/lab-data/bonev/'
f = NoBiasFast3DeFDR(
    [base_path + '<rep>/<chrom>_raw.npz'.replace('<rep>', repname)
     for repname in repnames],
    [base_path + '<rep>/<chrom>_kr.bias'.replace('<rep>', repname)
     for repname in repnames],
    chroms, 'design.csv', 'output-test',
    loop_patterns={c: base_path + 'clusters_0.025/%s_<chrom>_clusters.json' % c
                   for c in ['ES', 'NPC']}
)
f.run_to_qvalues()
f.simulate('ES', beta=0.0)

infile_pattern = 'sim/<rep>_<chrom>_raw.npz'
repnames = ['A1', 'A2', 'B1', 'B2']
sim_path = 'sim/'

for repname in repnames:
    for chrom in chroms:
        sys.stderr.write('balancing rep %s chrom %s\n' % (repname, chrom))
        infile = infile_pattern.replace('<rep>', repname)\
            .replace('<chrom>', chrom)
        outfile = infile.replace('_raw.npz', '_kr.bias')
        _, bias, _ = kr_balance(
            filter_sparse_rows_count(sparse.load_npz(infile)), fl=0)
        np.savetxt(outfile, bias)

f_sim = HiC3DeFDR(
    raw_npz_patterns=[sim_path + '<rep>_<chrom>_raw.npz'.replace('<rep>', repname) for repname in repnames],
    bias_patterns=[sim_path + '<rep>_<chrom>_kr.bias'.replace('<rep>', repname) for repname in repnames],
    chroms=chroms,
    design=sim_path + 'design.csv',
    outdir='output-sim',
    loop_patterns={'ES': base_path + 'clusters_0.025/ES_<chrom>_clusters.json'}
)
f_sim.run_to_qvalues(estimator='cml')
f_sim.plot_pvalue_distribution(outfile='pvalues_nobias.png')
