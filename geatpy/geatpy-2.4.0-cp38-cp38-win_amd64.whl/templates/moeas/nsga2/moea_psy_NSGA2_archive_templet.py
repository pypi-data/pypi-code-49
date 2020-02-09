# -*- coding: utf-8 -*-
import numpy as np
import geatpy as ea # 导入geatpy库
from sys import path as paths
from os import path
import time
paths.append(path.split(path.split(path.realpath(__file__))[0])[0])

class moea_psy_NSGA2_archive_templet(ea.MoeaAlgorithm):
    
    """
moea_psy_NSGA2_archive_templet : class - 带全局存档的多染色体多目标进化NSGA-II算法模板
    
描述:
    采用带全局存档(globalNDSet)的NSGA-II进行多目标优化。
    该模板是内置算法模板moea_NSGA2_archive_templet的多染色体版本。
    因此里面的种群对象为支持混合编码的多染色体种群类PsyPopulation类的对象。

模板使用注意:
    本模板调用的目标函数形如：aimFunc(pop), 
    其中pop为种群类的对象，代表一个种群，
    pop对象的Phen属性（即种群染色体的表现型）等价于种群所有个体的决策变量组成的矩阵，
    该函数根据该Phen计算得到种群所有个体的目标函数值组成的矩阵，并将其赋值给pop对象的ObjV属性。
    若有约束条件，则在计算违反约束程度矩阵CV后赋值给pop对象的CV属性（详见Geatpy数据结构）。
    该函数不返回任何的返回值，求得的目标函数值保存在种群对象的ObjV属性中，
                          违反约束程度矩阵保存在种群对象的CV属性中。
    例如：population为一个种群对象，则调用aimFunc(population)即可完成目标函数值的计算，
         此时可通过population.ObjV得到求得的目标函数值，population.CV得到违反约束程度矩阵。
    若不符合上述规范，则请修改算法模板或自定义新算法模板。

    """
    
    def __init__(self, problem, population):
        ea.MoeaAlgorithm.__init__(self, problem, population) # 先调用父类构造方法
        if str(type(population)) != "<class 'PsyPopulation.PsyPopulation'>":
            raise RuntimeError('传入的种群对象必须为PsyPopulation类型')
        self.name = 'psy-NSGA2-archive'
        if self.problem.M < 10:
            self.ndSort = ea.ndsortESS # 采用ENS_SS进行非支配排序
        else:
            self.ndSort = ea.ndsortTNS # 高维目标采用T_ENS进行非支配排序，速度一般会比ENS_SS要快
        self.selFunc = 'tour' # 选择方式，采用锦标赛选择
        # 由于有多个染色体，因此需要用多个重组和变异算子
        self.recOpers = []
        self.mutOpers = []
        for i in range(population.ChromNum):
            if population.Encodings[i] == 'P':
                recOper = ea.Xovpmx(XOVR = 1) # 生成部分匹配交叉算子对象
                mutOper = ea.Mutinv(Pm = 1) # 生成逆转变异算子对象
            elif population.Encodings[i] == 'BG':
                recOper = ea.Xovud(XOVR = 1) # 生成均匀交叉算子对象
                mutOper = ea.Mutbin(Pm = None) # 生成二进制变异算子对象，Pm设置为None时，具体数值取变异算子中Pm的默认值
            elif population.Encodings[i] == 'RI':
                recOper = ea.Recsbx(XOVR = 1, n = 20) # 生成模拟二进制交叉算子对象
                mutOper = ea.Mutpolyn(Pm = 1/self.problem.Dim, DisI = 20) # 生成多项式变异算子对象
            else:
                raise RuntimeError('编码方式必须为''BG''、''RI''或''P''.')
            self.recOpers.append(recOper)
            self.mutOpers.append(mutOper)
        self.MAXSIZE = 10 * population.sizes # 全局非支配解存档的大小限制，默认为10倍的种群个体数
    
    def reinsertion(self, population, offspring, NUM, globalNDSet):
        
        """
        描述:
            重插入个体产生新一代种群（采用父子合并选择的策略）。
            NUM为所需要保留到下一代的个体数目，globalNDSet为全局非支配解存档。
        """
        
        # 父子两代合并
        population = population + offspring
        globalNDSet = population + globalNDSet # 将population与全局归档集合并
        # 非支配排序分层
        [levels, criLevel] = self.ndSort(self.problem.maxormins * globalNDSet.ObjV, None, None, globalNDSet.CV)
        # 更新全局存档集
        globalNDSet = globalNDSet[np.where(levels == 1)[0]] # 更新全局非支配解
        globalNDSet = globalNDSet[np.where(np.all(globalNDSet.CV <= 0, 1))[0]] # 排除非可行解
        if globalNDSet.sizes > self.MAXSIZE:
            dis = ea.crowdis(globalNDSet.ObjV, np.ones(globalNDSet.sizes)) # 计算拥挤距离
            globalNDSet = globalNDSet[np.argsort(-dis)[:self.MAXSIZE]] # 根据拥挤距离选择符合个数限制的解保留在存档中
        # 选择个体保留到下一代
        levels = levels[: population.sizes] # 得到与population个体对应的levels
        dis = ea.crowdis(population.ObjV, levels) # 计算拥挤距离
        population.FitnV[:, 0] = np.argsort(np.lexsort(np.array([dis, -levels])), kind = 'mergesort') # 计算适应度
        chooseFlag = ea.selecting('dup', population.FitnV, NUM) # 调用低级选择算子dup进行基于适应度排序的选择，保留NUM个个体
        return population[chooseFlag], globalNDSet
    
    def run(self, prophetPop = None): # prophetPop为先知种群（即包含先验知识的种群）
        #==========================初始化配置===========================
        population = self.population
        NIND = population.sizes
        self.initialization() # 初始化算法模板的一些动态参数
        #===========================准备进化============================
        population.initChrom() # 初始化种群染色体矩阵（内含解码，详见PsyPopulation类的源码）
        self.problem.aimFunc(population) # 计算种群的目标函数值
        self.evalsNum = population.sizes # 记录评价次数
        # 插入先验知识（注意：这里不会对先知种群prophetPop的合法性进行检查，故应确保prophetPop是一个种群类且拥有合法的Chrom、ObjV、Phen等属性）
        if prophetPop is not None:
            population = (prophetPop + population)[:NIND] # 插入先知种群
        [levels, criLevel] = self.ndSort(self.problem.maxormins * population.ObjV, NIND, None, population.CV) # 对NIND个个体进行非支配分层
        population.FitnV[:, 0] = 1 / levels # 直接根据levels来计算初代个体的适应度
        globalNDSet = population[np.where(levels == 1)[0]] # 创建全局存档，该全局存档贯穿进化始终，随着进化不断更新
        globalNDSet = globalNDSet[np.where(np.all(globalNDSet.CV <= 0, 1))[0]] # 排除非可行解
        #===========================开始进化============================
        while self.terminated(population) == False:
            # 选择个体参与进化
            offspring = population[ea.selecting(self.selFunc, population.FitnV, NIND)]
            # 进行进化操作，分别对各个种群染色体矩阵进行重组和变异
            for i in range(population.ChromNum):
                offspring.Chroms[i] = self.recOpers[i].do(offspring.Chroms[i]) # 重组
                offspring.Chroms[i] = self.mutOpers[i].do(offspring.Encodings[i], offspring.Chroms[i], offspring.Fields[i]) # 变异
            offspring.Phen = offspring.decoding() # 解码
            self.problem.aimFunc(offspring) # 求进化后个体的目标函数值
            self.evalsNum += offspring.sizes # 更新评价次数
            # 重插入生成新一代种群，同时更新全局存档
            population, globalNDSet = self.reinsertion(population, offspring, NIND, globalNDSet)
        self.passTime += time.time() - self.timeSlot # 更新用时记录
        #=========================绘图及输出结果=========================
        if self.drawing != 0:
            ea.moeaplot(globalNDSet.ObjV, 'Pareto Front', True)
        # 返回帕累托最优集
        return globalNDSet
