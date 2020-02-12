import sys

import numpy as np
import scipy.sparse as sparse

from hiclite.steps.filter import filter_sparse_rows_count
from hiclite.steps.balance import kr_balance

from hic3defdr import HiC3DeFDR
from hic3defdr import plot_roc, plot_fdr

from hic3defdr.alternatives import Poisson3DeFDR, Unsmoothed3DeFDR, Global3DeFDR


repnames = ['ES_1', 'ES_3', 'NPC_2', 'NPC_4']
#chroms = ['chr%i' % i for i in range(1, 20)] + ['chrX']
chroms = ['chr18', 'chr19']
base_path = 'c:/lab-data/bonev/'
h = HiC3DeFDR(
    [base_path + '<rep>/<chrom>_raw.npz'.replace('<rep>', repname)
     for repname in repnames],
    [base_path + '<rep>/<chrom>_kr.bias'.replace('<rep>', repname)
     for repname in repnames],
    chroms, 'design.csv', 'output-small',
    loop_patterns={c: base_path + 'clusters_0.025/%s_<chrom>_clusters.json' % c
                   for c in ['ES', 'NPC']},
    dist_thresh_max=500,
    mean_thresh=5.0
)
h = HiC3DeFDR.load('output-small')
#h.run_to_qvalues()
#h.prepare_data()
#h.estimate_disp()
#h.lrt()
#h.bh()
#h.classify()
#h.plot_dispersion_fit('ES', xaxis='dist', yaxis='disp', logx=False, logy=False, outfile='test_ddr.png')
#h.plot_dispersion_fit('ES', xaxis='dist', yaxis='var', logx=False, outfile='test_dvr.png')
#h.plot_dispersion_fit('ES', xaxis='mean', yaxis='disp', logy=False, outfile='test_mdr.png')
#h.plot_dispersion_fit('ES', xaxis='mean', yaxis='var', outfile='test_mvr.png')
#for d in [5, 10, 25, 50, 75, 100]:
#    h.plot_dispersion_fit('ES', xaxis='mean', yaxis='var', distance=d, logx=True,
#                          xlim=(5, 500), ylim=(1e-5, 1e3),
#                          outfile='mvr_es_%i.png' % d)
#h.plot_dispersion_fit('ES', ylim=(0, 0.25), outfile='ddr_real.png')


for r in ['all', 'short', 'mid', 'long']:
    loop_pattern = 'ES_<chrom>_%s_clusters.json' % r
    #h.simulate('ES', loop_pattern=loop_pattern, outdir='sim-small-%s' % r)

    infile_pattern = 'sim-small-%s/<rep>_<chrom>_raw.npz' % r
    repnames = ['A1', 'A2', 'B1', 'B2']
    if False:
        for repname in repnames:
            for chrom in chroms:
                sys.stderr.write('balancing rep %s chrom %s\n' % (repname, chrom))
                infile = infile_pattern.replace('<rep>', repname)\
                    .replace('<chrom>', chrom)
                outfile = infile.replace('_raw.npz', '_kr.bias')
                _, bias, _ = kr_balance(
                    filter_sparse_rows_count(sparse.load_npz(infile)), fl=0)
                np.savetxt(outfile, bias)

    base_path = 'sim-small-%s/' % r
    h_sim = HiC3DeFDR(
        [base_path + '<rep>_<chrom>_raw.npz'.replace('<rep>', repname)
         for repname in repnames],
        [base_path + '<rep>_<chrom>_kr.bias'.replace('<rep>', repname)
         for repname in repnames],
        chroms, base_path + 'design.csv', 'output-sim-small-%s' % r,
        loop_patterns={'ES': loop_pattern}
    )
    h_sim = HiC3DeFDR.load('output-sim-small-%s' % r)
    #h_sim.run_to_qvalues()
    #h_sim.plot_dispersion_fit('A', ylim=(0, 0.25), outfile='ddr_sim.png')
    #h_sim.plot_pvalue_distribution(outfile='null_sim_pvalues.png')
    #h_sim.evaluate('ES', 'sim-small-%s/labels_<chrom>.txt' % r)

    h_sim_pois = Poisson3DeFDR(
        [base_path + '<rep>_<chrom>_raw.npz'.replace('<rep>', repname)
         for repname in repnames],
        [base_path + '<rep>_<chrom>_kr.bias'.replace('<rep>', repname)
         for repname in repnames],
        chroms, base_path + 'design.csv', 'output-sim-small-%s-pois' % r,
        loop_patterns={'ES': loop_pattern}
    )
    h_sim_pois = Poisson3DeFDR.load('output-sim-small-%s-pois' % r)
    #h_sim_pois.run_to_qvalues()
    #h_sim_pois.evaluate('ES', 'sim-small-%s/labels_<chrom>.txt' % r)

    h_sim_unsmooth = Unsmoothed3DeFDR(
        [base_path + '<rep>_<chrom>_raw.npz'.replace('<rep>', repname)
         for repname in repnames],
        [base_path + '<rep>_<chrom>_kr.bias'.replace('<rep>', repname)
         for repname in repnames],
        chroms, base_path + 'design.csv', 'output-sim-small-%s-unsmooth' % r,
        loop_patterns={'ES': loop_pattern}
    )
    h_sim_unsmooth = Unsmoothed3DeFDR.load('output-sim-small-%s-unsmooth' % r)
    #h_sim_unsmooth.run_to_qvalues()
    #h_sim_unsmooth.evaluate('ES', 'sim-small-%s/labels_<chrom>.txt' % r)

    h_sim_global = Global3DeFDR(
        [base_path + '<rep>_<chrom>_raw.npz'.replace('<rep>', repname)
         for repname in repnames],
        [base_path + '<rep>_<chrom>_kr.bias'.replace('<rep>', repname)
         for repname in repnames],
        chroms, base_path + 'design.csv', 'output-sim-small-%s-global' % r,
        loop_patterns={'ES': loop_pattern}
    )
    h_sim_global = Global3DeFDR.load('output-sim-small-%s-global' % r)
    #h_sim_global.run_to_qvalues()
    #h_sim_global.evaluate('ES', 'sim-small-%s/labels_<chrom>.txt' % r)

    plot_roc([np.load('output-sim-small-%s/eval.npz' % r),
              np.load('output-sim-small-%s-pois/eval.npz' % r),
              np.load('output-sim-small-%s-unsmooth/eval.npz' % r),
              np.load('output-sim-small-%s-global/eval.npz' % r)],
             ['3DeFDR-HiC', 'Poisson', 'Sample Variance', 'Global NB'],
             outfile='roc_%s.png' % r)

    plot_fdr([np.load('output-sim-small-%s/eval.npz' % r),
              np.load('output-sim-small-%s-pois/eval.npz' % r),
              np.load('output-sim-small-%s-unsmooth/eval.npz' % r),
              np.load('output-sim-small-%s-global/eval.npz' % r)],
             ['3DeFDR-HiC', 'Poisson', 'Sample Variance', 'Global NB'],
             outfile='fdr_%s.png' % r)

    plot_roc([np.load('output-sim-small-%s/eval.npz' % r),
              np.load('output-sim-small-%s-unsmooth/eval.npz' % r)],
             ['3DeFDR-HiC', 'Sample Variance'],
             outfile='roc_twolines_%s.png' % r)

    plot_fdr([np.load('output-sim-small-%s/eval.npz' % r),
              np.load('output-sim-small-%s-unsmooth/eval.npz' % r)],
             ['3DeFDR-HiC', 'Sample Variance'],
             outfile='fdr_twolines_%s.png' % r)
#f.process_chrom('chr19')
#f.process_all()
#f.bh()
#f.threshold_chrom('chr19')
#f.threshold_all()
#base_path = 'c:/lab-data/bonev/'
#f.simulate('ES', base_path + 'clusters/ES_<chrom>_clusters.json', chrom='chr19')
#f.simulate('ES', base_path + 'clusters/ES_<chrom>_clusters.json')

#from hic3defdr import HiC3DeFDR
#f = HiC3DeFDR.load('output')
#f.estimate_disp('chr19')
#f.estimate_disp('chrX')
#f.prepare_data('chrX')
#f.plot_dispersion_fit('chr19', 'ES', outfile='disp.png')
#f.plot_dispersion_fit('chr19', 'ES', yaxis='var', outfile='var.png')
#f.plot_qvalue_distribution(outfile='qvalue_dist.png')
#f.process_chrom('chr19')
#f.lrt('chr19')

#f.threshold_chrom('chr19')

#f.plot_grid('chr1', 1303, 1312, 50, outfile='grid.png')
#f.plot_dispersion_fit('chr19', 'ES', outfile='disp_es_2.png')
#f.plot_dispersion_fit('chr19', 'NPC', outfile='disp_npc_2.png')
#f.classify_sig_pixels('chr19')


#import matplotlib.pyplot as plt
#_, ax, outline_clusters = f.plot_grid('chr1', 1303, 1312, 50)
#ax[0, 2].plot([0, 100], [0, 100])
#plt.savefig('grid.png', bbox_inches='tight')
#plt.clf()

#cluster_idx = np.array([True if any((r, c in cluster for cluster in clusters)) else False
#                        for r, c in zip(row[disp_idx][loop_idx], col[disp_idx][loop_idx])])

#from hic3defdr import HiC3DeFDR
#f = HiC3DeFDR.load('output')
#f.plot_dispersion_fit('chr19', 'ES', outfile='disp_es.png')

#import numpy as np
#import scipy.stats as stats
#from hic3defdr import HiC3DeFDR
#from hic3defdr.scaled_nb import inverse_mvr
#f = HiC3DeFDR.load('output')
#cond = 'ES'
#chrom = 'chr1'
#disp_idx = f.load_data('disp_idx', 'chr1')
#row = f.load_data('row', chrom)[disp_idx]
#col = f.load_data('col', chrom)[disp_idx]
#scaled = f.load_data('scaled', chrom)[disp_idx, :][:, f.design[cond]]
#mean = np.mean(scaled, axis=1)
#var = np.var(scaled, ddof=1, axis=1)
#disp = inverse_mvr(mean, var)
#dist = col - row
#stats.spearmanr(mean, disp)
#stats.spearmanr(dist, disp)
