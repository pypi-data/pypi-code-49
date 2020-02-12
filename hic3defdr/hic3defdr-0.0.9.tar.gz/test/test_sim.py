from hic3defdr import HiC3DeFDR

repnames = ['A1', 'A2', 'B1', 'B2']
#chroms = ['chr%i' % i for i in range(1, 20)] + ['chrX']
chroms = ['chr19']
sim_path = 'sim/'
base_path = 'c:/lab-data/bonev/'
f = HiC3DeFDR(
    [sim_path + '<rep>_<chrom>_raw.npz'.replace('<rep>', repname)
     for repname in repnames],
    [sim_path + '<rep>_<chrom>_kr.bias'.replace('<rep>', repname)
     for repname in repnames],
    chroms, sim_path + 'design.csv', 'output-sim',
    loop_patterns={'ES': base_path + 'clusters_0.025/ES_<chrom>_clusters.json'}
)

from hic3defdr import HiC3DeFDR
f = HiC3DeFDR.load('output-sim')
f.evaluate('ES', 'sim/labels_<chrom>.txt')


import numpy as np
from hic3defdr import plot_roc, plot_fdr
plot_roc([np.load('output-sim/eval.npz')], ['hic3defdr'], outfile='roc.png')
plot_fdr([np.load('output-sim/eval.npz')], ['hic3defdr'], outfile='fdr.png')
