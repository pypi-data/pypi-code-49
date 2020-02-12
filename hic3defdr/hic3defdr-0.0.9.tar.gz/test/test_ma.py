from hic3defdr import HiC3DeFDR

repnames = ['ES_1', 'ES_3', 'NPC_2', 'NPC_4']
#chroms = ['chr%i' % i for i in range(1, 20)] + ['chrX']
#chroms = ['chr19']
#chroms = ['chr3']
chroms = ['chr18']
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
f = HiC3DeFDR.load('output-test')
#f.run_to_qvalues(norm='median_of_ratios')
#f.run_to_qvalues()
f.run_to_qvalues(n_bins_norm=None)
#f.prepare_data()
#f.estimate_disp()
#f.lrt()
#f.bh()
f.plot_dd_curves('chr18', outfile='dd2.png')
f.plot_ma('chr18', legend=True, outfile='ma_legend2.png')
#f.plot_grid('chr18', 2218, 2236, 50, outfile='grid.png')
#f.plot_dispersion_fit('chr18', 'ES', yaxis='disp', outfile='disp.png')
#f.plot_pvalue_distribution(outfile='pvalue_dist.png')
