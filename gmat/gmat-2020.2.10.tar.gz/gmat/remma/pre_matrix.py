import logging
import sys
import numpy as np
import pandas as pd
from scipy.sparse import csr_matrix


def pre_design_matrix(pheno_file, bed_file):
    """
    准备表型向量、固定效应设计矩阵、随机效应设计矩阵
    :param pheno_file:
    :param bed_file:
    :return:y, xmat, zmat
    """
    id_bed_lst = []
    fin = open(bed_file + '.fam')
    for line in fin:
        arr = line.split()
        id_bed_lst.append(" ".join([arr[0], arr[1]]))
    fin.close()
    id_pheno_lst = {}
    fin = open(pheno_file)
    for line in fin:
        arr = line.split()
        try:
            id_pheno_lst[" ".join([arr[0], arr[1]])].append(" ".join(arr))
        except Exception as e:
            del e
            id_pheno_lst[" ".join([arr[0], arr[1]])] = [" ".join(arr)]
    fin.close()
    id_not_pheno = set(id_bed_lst) - set(list(id_pheno_lst.keys()))
    if len(id_not_pheno) > 0:
        logging.error('The below genotyped id is not in the phenotype file:\n {}'.format('\n'.join(list(id_not_pheno))))
        sys.exit()
    fout = open(pheno_file + '.temp', 'w')
    for id in id_bed_lst:
        for val in id_pheno_lst[id]:
            fout.write(val + '\n')
    fout.close()
    df = pd.read_csv(pheno_file + '.temp', header=None, sep='\s+')
    y = np.array(df.iloc[:, -1:])
    xmat = np.array(df.iloc[:, 2:-1])
    id_dct = {}
    row = []
    col = []
    j = 0
    for i in range(df.shape[0]):
        row.append(i)
        if df.iloc[i, 1] not in id_dct:
            id_dct[df.iloc[i, 1]] = j
            j += 1
        col.append(id_dct[df.iloc[i, 1]])
    zmat = csr_matrix(([1.0]*len(row), (row, col)))
    return y, xmat, zmat
