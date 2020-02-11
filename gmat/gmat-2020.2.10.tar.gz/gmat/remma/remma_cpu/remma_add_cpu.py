import numpy as np
from scipy import linalg
import pandas as pd
from functools import reduce
import gc
import time
import logging
import sys
from scipy.stats import chi2

from gmat.process_plink.process_plink import read_plink, impute_geno


def remma_add_cpu(y, xmat, zmat, gmat_lst, var_com, bed_file, out_file='remma_add_cpu'):
    """
    加性检验
    :param y: 表型
    :param xmat: 固定效应设计矩阵
    :param zmat: 随机效应设计矩阵，csr稀疏矩阵
    :param gmat_lst: 基因组关系矩阵列表
    :param var_com: 方差组分
    :param bed_file: plink文件
    :param out_file: 输出文件
    :return:
    """
    logging.info("计算V矩阵及其逆矩阵")
    y = np.array(y).reshape(-1, 1)
    n = y.shape[0]
    xmat = np.array(xmat).reshape(n, -1)
    vmat = np.diag([var_com[-1]] * n)
    for val in range(len(gmat_lst)):
        vmat += zmat.dot((zmat.dot(gmat_lst[val])).T) * var_com[val]
    del gmat_lst
    gc.collect()
    vmat_inv = linalg.inv(vmat)
    logging.info("计算P矩阵")
    vxmat = np.dot(vmat_inv, xmat)
    xvxmat = np.dot(xmat.T, vxmat)
    xvxmat = linalg.inv(xvxmat)
    pmat = reduce(np.dot, [vxmat, xvxmat, vxmat.T])
    pmat = vmat_inv - pmat
    pymat = zmat.T.dot(np.dot(pmat, y))
    pvpmat = reduce(np.dot, [pmat, vmat, pmat])
    pvpmat = zmat.T.dot((zmat.T.dot(pvpmat)).T)
    del vmat, vmat_inv, pmat
    gc.collect()
    logging.info("读取SNP文件")
    snp_mat = read_plink(bed_file)
    num_id, num_snp = snp_mat.shape
    if np.any(np.isnan(snp_mat)):
        logging.warning('Missing genotypes are imputed with random genotypes.')
        snp_mat = impute_geno(snp_mat)
    freq = np.sum(snp_mat, axis=0) / (2 * num_id)
    freq.shape = (1, num_snp)
    snp_mat = snp_mat - 2 * freq
    scale = np.sum(2*freq*(1-freq))
    logging.info("Scaled factors {:.3f}".format(scale))
    eff_vec = np.dot(snp_mat.T, pymat)[:, -1] * var_com[0]/scale
    var_vec = np.sum(snp_mat * np.dot(pvpmat, snp_mat), axis=0) * var_com[0] * var_com[0]/(scale*scale)
    eff_vec_to_fixed = eff_vec * var_com[0]/(var_vec*scale)  # 转化为固定效应检验计算效应
    chi_vec = eff_vec*eff_vec/var_vec
    p_vec = chi2.sf(chi_vec, 1)
    snp_info_file = bed_file + '.bim'
    snp_info = pd.read_csv(snp_info_file, sep='\s+', header=None)
    res_df = snp_info.iloc[:, [0, 1, 3, 4, 5]]
    res_df.columns = ['chro', 'snp_ID', 'pos', 'allele1', 'allele2']
    res_df.loc[:, 'eff_val'] = eff_vec
    res_df.loc[:, 'chi_val'] = chi_vec
    res_df.loc[:, 'eff_val_to_fixed'] = eff_vec_to_fixed
    res_df.loc[:, 'p_val'] = p_vec
    try:
        res_df.to_csv(out_file, index=False, header=True, sep=' ')
    except Exception as e:
        logging.error(e)
        sys.exit()
    return res_df
