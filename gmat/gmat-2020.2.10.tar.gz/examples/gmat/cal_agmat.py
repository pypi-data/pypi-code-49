import numpy as np
import pandas as pd
import logging
import os
from glta.gmat import agmat, dgmat_as

logging.basicConfig(level=logging.INFO)

######## 加性基因组关系矩阵
bed_file = '../data/plink'

# 矩阵形式
agmat0 = agmat(bed_file, inv=True, small_val=0.001, out_fmt='mat')
grm0 = np.load('../data/plink.agrm0.npz')
giv0 = np.load('../data/plink.agiv0.npz')
np.savetxt('../data/plink.agrm0', grm0['mat'])
np.savetxt('../data/plink.agiv0', giv0['mat'])



# 行-列-值形式
agmat1 = agmat(bed_file, inv=True, small_val=0.001, out_fmt='row_col_val')
grm1 = np.load('../data/plink.agrm1.npz')
giv1 = np.load('../data/plink.agiv1.npz')
grm1_dct = {'row': grm1['row'] + 1,
            'col': grm1['col'] + 1,
            'val': grm1['val']
}
grm1_df = pd.DataFrame(grm1_dct, columns=['row', 'col', 'val'])
grm1_df.to_csv('../data/plink.agrm1', header=False, index=False, sep=' ')
giv1_dct = {'row': giv1['row'] + 1,
            'col': giv1['col'] + 1,
            'val': giv1['val']
}
giv1_df = pd.DataFrame(giv1_dct, columns=['row', 'col', 'val'])
giv1_df.to_csv('../data/plink.agiv1', header=False, index=False, sep=' ')



# 个体号-个体号-值形式
agmat2 = agmat(bed_file, inv=True, small_val=0.001, out_fmt='id_id_val')
grm2 = np.load('../data/plink.agrm2.npz')
giv2 = np.load('../data/plink.agiv2.npz')

grm2_dct = {'id0': grm2['id0'],
            'id1': grm2['id1'],
            'val': grm2['val']
}
grm2_df = pd.DataFrame(grm2_dct, columns=['id0', 'id1', 'val'])
grm2_df.to_csv('../data/plink.agrm2', header=False, index=False, sep=' ')
giv2_dct = {'id0': giv2['id0'],
            'id1': giv2['id1'],
            'val': giv2['val']
}
giv2_df = pd.DataFrame(giv2_dct, columns=['id0', 'id1', 'val'])
giv2_df.to_csv('../data/plink.agiv2', header=False, index=False, sep=' ')


# 删除
'''
os.remove('../data/plink.agrm0.npz')
os.remove('../data/plink.agiv0.npz')
os.remove('../data/plink.agrm0')
os.remove('../data/plink.agiv0')

os.remove('../data/plink.agrm1.npz')
os.remove('../data/plink.agiv1.npz')
os.remove('../data/plink.agrm1')
os.remove('../data/plink.agiv1')

os.remove('../data/plink.agrm2.npz')
os.remove('../data/plink.agiv2.npz')
os.remove('../data/plink.agrm2')
os.remove('../data/plink.agiv2')
'''
