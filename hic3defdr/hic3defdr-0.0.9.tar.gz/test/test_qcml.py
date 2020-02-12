import sys

import numpy as np
import scipy.sparse as sparse

from hiclite.steps.filter import filter_sparse_rows_count
from hiclite.steps.balance import kr_balance

from hic3defdr import HiC3DeFDR


repnames = ['ES_1', 'ES_3', 'NPC_2', 'NPC_4']
chroms = ['chr19']
base_path = 'c:/lab-data/bonev/'

f = HiC3DeFDR(
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

f_sim_cml = HiC3DeFDR(
    raw_npz_patterns=[sim_path + '<rep>_<chrom>_raw.npz'.replace('<rep>', repname) for repname in repnames],
    bias_patterns=[sim_path + '<rep>_<chrom>_kr.bias'.replace('<rep>', repname) for repname in repnames],
    chroms=chroms,
    design=sim_path + 'design.csv',
    outdir='output-cml',
    loop_patterns={'ES': base_path + 'clusters_0.025/ES_<chrom>_clusters.json'}
)
f_sim_cml.run_to_qvalues(estimator='cml')
f_sim_cml.plot_pvalue_distribution(outfile='pvalues_cml.png')

#f_sim_qcml = HiC3DeFDR(
#    raw_npz_patterns=[sim_path + '<rep>_<chrom>_raw.npz'.replace('<rep>', repname) for repname in repnames],
#    bias_patterns=[sim_path + '<rep>_<chrom>_kr.bias'.replace('<rep>', repname) for repname in repnames],
#    chroms=chroms,
#    design=sim_path + 'design.csv',
#    outdir='output-qcml',
#    loop_patterns={'ES': base_path + 'clusters_0.025/ES_<chrom>_clusters.json'}
#)
#f_sim_qcml.run_to_qvalues(estimator='qcml')
#f_sim_qcml.plot_pvalue_distribution(outfile='pvalues_qcml.png')
#
#f_sim_mme = HiC3DeFDR(
#    raw_npz_patterns=[sim_path + '<rep>_<chrom>_raw.npz'.replace('<rep>', repname) for repname in repnames],
#    bias_patterns=[sim_path + '<rep>_<chrom>_kr.bias'.replace('<rep>', repname) for repname in repnames],
#    chroms=chroms,
#    design=sim_path + 'design.csv',
#    outdir='output-mme',
#    loop_patterns={'ES': base_path + 'clusters_0.025/ES_<chrom>_clusters.json'}
#)
#f_sim_mme.run_to_qvalues(estimator='mme')
#f_sim_mme.plot_pvalue_distribution(outfile='pvalues_mme.png')
#
#f_sim_mvr = HiC3DeFDR(
#    raw_npz_patterns=[sim_path + '<rep>_<chrom>_raw.npz'.replace('<rep>', repname) for repname in repnames],
#    bias_patterns=[sim_path + '<rep>_<chrom>_kr.bias'.replace('<rep>', repname) for repname in repnames],
#    chroms=chroms,
#    design=sim_path + 'design.csv',
#    outdir='output-mvr',
#    loop_patterns={'ES': base_path + 'clusters_0.025/ES_<chrom>_clusters.json'}
#)
#f_sim_mvr.run_to_qvalues(estimator='mvr')
#f_sim_mvr.plot_pvalue_distribution(outfile='pvalues_mvr.png')
