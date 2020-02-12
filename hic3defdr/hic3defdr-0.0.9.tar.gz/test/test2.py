from hic3defdr import HiC3DeFDR

repnames = ['ES_1', 'ES_3', 'NPC_2', 'NPC_4']
#chroms = ['chr%i' % i for i in range(1, 20)] + ['chrX']
chroms = ['chr19']
base_path = 'c:/lab-data/bonev/'
f = HiC3DeFDR(
    [base_path + '<rep>/<chrom>_raw.npz'.replace('<rep>', repname)
     for repname in repnames],
    [base_path + '<rep>/<chrom>_kr.bias'.replace('<rep>', repname)
     for repname in repnames],
    chroms, 'design.csv', 'output-test',
    loop_patterns={c: base_path + 'clusters/%s_<chrom>_clusters.json' % c
                   for c in ['ES', 'NPC']}
)
f = HiC3DeFDR.load('output')
f.run_to_qvalues()
f.classify()
f.process_chrom('chr19')
f.process_all()
f.bh()
f.threshold_chrom('chr19')
f.threshold_all()
base_path = 'c:/lab-data/bonev/'
f.simulate('ES', base_path + 'clusters/ES_<chrom>_clusters.json', chrom='chr19')
f.simulate('ES', base_path + 'clusters/ES_<chrom>_clusters.json')

from hic3defdr import HiC3DeFDR
f = HiC3DeFDR.load('output')
f.estimate_disp('chr19')
f.estimate_disp('chrX')
f.prepare_data('chrX')
f.plot_dispersion_fit('chr19', 'ES', outfile='disp.png')
f.plot_dispersion_fit('chr19', 'ES', yaxis='var', outfile='var.png')
#f.plot_qvalue_distribution(outfile='qvalue_dist.png')
#f.process_chrom('chr19')
f.lrt('chr19')

f.threshold_chrom('chr19')

f.plot_grid('chr1', 1303, 1312, 50, outfile='grid.png')
f.plot_dispersion_fit('chr19', 'ES', outfile='disp_es_2.png')
f.plot_dispersion_fit('chr19', 'NPC', outfile='disp_npc_2.png')
f.classify_sig_pixels('chr19')


import matplotlib.pyplot as plt
_, ax, outline_clusters = f.plot_grid('chr1', 1303, 1312, 50)
ax[0, 2].plot([0, 100], [0, 100])
plt.savefig('grid.png', bbox_inches='tight')
plt.clf()

cluster_idx = np.array([True if any((r, c in cluster for cluster in clusters)) else False
                        for r, c in zip(row[disp_idx][loop_idx], col[disp_idx][loop_idx])])

from hic3defdr import HiC3DeFDR
f = HiC3DeFDR.load('output')
f.plot_dispersion_fit('chr19', 'ES', outfile='disp_es.png')

import numpy as np
import scipy.stats as stats
from hic3defdr import HiC3DeFDR
from hic3defdr.scaled_nb import inverse_mvr
f = HiC3DeFDR.load('output')
cond = 'ES'
chrom = 'chr1'
disp_idx = f.load_data('disp_idx', 'chr1')
row = f.load_data('row', chrom)[disp_idx]
col = f.load_data('col', chrom)[disp_idx]
scaled = f.load_data('scaled', chrom)[disp_idx, :][:, f.design[cond]]
mean = np.mean(scaled, axis=1)
var = np.var(scaled, ddof=1, axis=1)
disp = inverse_mvr(mean, var)
dist = col - row
stats.spearmanr(mean, disp)
stats.spearmanr(dist, disp)
