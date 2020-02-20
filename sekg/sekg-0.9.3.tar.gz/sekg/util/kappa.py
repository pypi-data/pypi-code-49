# -*- coding: utf-8 -*-
"""
-----------------------------------------
@Author: attenton
@Email: 18212010081@fudan.edu.cn
@Created: 2019/12/23
------------------------------------------
@Modify: 2019/12/23
------------------------------------------
@Description:
"""
import numpy as np
import pandas as pd
from pathlib import Path
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import cohen_kappa_score


# sklearn中也有cohen_kappa_score方法可以计算cohen kappa，只是输入不同，sklearn的输入是两个向量，而不是矩阵
#

def kappa(testData, k):
    """
    sklearn中也有计算cohern_kappa的，只是输入不同，sklearn输入的两个向量
    :param testData:  需要计算的矩阵，k*k,
    :param k: k表示标注的label个数
    :return:
    """
    dataMat = np.mat(testData)
    P0 = 0.0
    for i in range(k):
        P0 += dataMat[i, i]*1.0
    xsum = np.sum(dataMat, axis=1)
    ysum = np.sum(dataMat, axis=0)
    #xsum是个k行1列的向量，ysum是个1行k列的向量
    sum = np.sum(dataMat)
    # print(sum)
    # print(xsum)
    # print(ysum)
    Pe  = float(ysum*xsum)/sum/sum
    # print(Pe)
    P0 = float(P0/sum*1.0)
    # print(P0)
    cohens_coefficient = float((P0-Pe)/(1-Pe))
    return cohens_coefficient


def fleiss_kappa(testData, N, k, n): #testData表示要计算的数据，（N,k）表示矩阵的形状，说明数据是N行k列的，一共有n个标注人员
    """

    :param testData: 输入的数据矩阵， N*k
    :param N: N条标注的数据
    :param k: k表示标注的label的数量
    :param n: n表示标注人员的数量
    :return:
    """
    dataMat = np.mat(testData, float)
    oneMat = np.ones((k, 1))
    sum = 0.0
    P0 = 0.0
    for i in range(N):
        temp = 0.0
        for j in range(k):
            sum += dataMat[i, j]
            temp += 1.0*dataMat[i, j]**2
        temp -= n
        temp /= (n-1)*n
        P0 += temp
    P0 = 1.0*P0/N
    ysum = np.sum(dataMat, axis=0)
    for i in range(k):
        ysum[0, i] = (ysum[0, i]/sum)**2
    Pe = ysum*oneMat*1.0
    ans = (P0-Pe)/(1-Pe)
    return ans[0, 0]
