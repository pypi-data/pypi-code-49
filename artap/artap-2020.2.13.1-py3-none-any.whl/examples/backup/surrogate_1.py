import time
import warnings
import math

from artap.problem import Problem
from artap.results import GraphicalResults
from artap.algorithm_nlopt import NLopt, LN_BOBYQA
from artap.algorithm_bayesopt import BayesOptSerial
from artap.algorithm_genetic import NSGAII
from artap.algorithm_sweep import SweepAlgorithm
from artap.operators import CustomGeneration, GaussianProcessRegressor
from artap.surrogate_scikit import SurrogateModelScikit

from agrossuite import agros


from sklearn.svm import SVR
from sklearn.neural_network import MLPRegressor
from sklearn.linear_model import SGDRegressor
from sklearn.kernel_ridge import KernelRidge
from sklearn.tree import DecisionTreeRegressor, ExtraTreeRegressor
from sklearn.ensemble import AdaBoostRegressor, GradientBoostingRegressor, RandomForestRegressor, ExtraTreesRegressor, BaggingRegressor
from sklearn.kernel_ridge import KernelRidge
from sklearn.neighbors import KNeighborsRegressor, RadiusNeighborsRegressor
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF, Matern, DotProduct, WhiteKernel, ConstantKernel, RationalQuadratic, ExpSineSquared

from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import RandomizedSearchCV
from skopt import BayesSearchCV

from sklearn.metrics import r2_score

from numpy import array
import numpy as np

# callback handler
#def on_step(optim_result):
#    score = searchcv.best_score_
#    print("best score: %s" % score)
#    if score >= 0.98:
#        print('Interrupting!')
#        return True

# Utility function to report best scores
def report(results, n_top=3):
    for i in range(1, n_top + 1):
        candidates = np.flatnonzero(results['rank_test_score'] == i)
        for candidate in candidates:
            print("Model with rank: {0}".format(i))
            print("Mean validation score: {0:.3f} (std: {1:.3f})".format(
                  results['mean_test_score'][candidate],
                  results['std_test_score'][candidate]))
            print("Parameters: {0}".format(results['params'][candidate]))
            print("")


def regressor_optim():
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")

        x_train, y_train, x_test, y_test = regressor_data()

        # dict_keys(['bootstrap', 'criterion', 'max_depth', 'max_features', 'max_leaf_nodes', 'min_impurity_decrease', 'min_impurity_split', 'min_samples_leaf', 'min_samples_split', 'min_weight_fraction_leaf', 'n_estimators', 'n_jobs', 'oob_score', 'random_state', 'verbose', 'warm_start'])
        # param_grid = {"max_depth": [3, None], "max_features": [1], "min_samplesx_split": [2, 3, 10], "bootstrap": [True, False]}
        # regressor = RandomForestRegressor(n_estimators=20)

        # param_grid = {"alpha": [10, 1e0, 0.1, 1e-2, 1e-3], "gamma": np.logspace(-5, -2, 2, 5, 10)}
        # regressor = KernelRidge(kernel='rbf', gamma=0.1)

        # print(regressor.get_params().keys())



        # run grid search
        start = time.time()
        # log-uniform: understand as search over p = exp(x) by varying x
        # grid_search = BayesSearchCV(
        #     SVR(),
        #     {
        #         'C': (1e-6, 1e+6, 'log-uniform'),
        #         'gamma': (1e-6, 1e+1, 'log-uniform'),
        #         'degree': (1, 8),  # integer valued parameter
        #         'kernel': ['linear', 'poly', 'rbf'],  # categorical parameter
        #     },
        #     n_iter=32
        # )

        ker_rbf1 = RBF(length_scale=1.0, length_scale_bounds=(1e-1, 10.0))
        ker_rbf2 = ConstantKernel(1.0, constant_value_bounds="fixed") * RBF(1.0, length_scale_bounds=(1e-1, 10.0))
        ker_rq = ConstantKernel(1.0, constant_value_bounds="fixed") * RationalQuadratic(alpha=0.1, length_scale=1)
        ker_expsine = ConstantKernel(1.0, constant_value_bounds="fixed") * ExpSineSquared(1.0, 5.0, periodicity_bounds=(1e-2, 1e1))
        #
        # kernel_list = [ker_rbf1, ker_rbf2, ker_rq, ker_expsine]
        kernel_list = [ker_rbf1]
        #
        param_grid = {"kernel": kernel_list,
                      # "alpha": [1e-10, 1e-12, 1e-5, 1e-2, 1e-1, 1e0, 1e1],
                      "alpha": [1e-10],
                       "optimizer": ["fmin_l_bfgs_b"],
                       # "n_restarts_optimizer": [1, 3, 6, 9, 12, 20],
                       "n_restarts_optimizer": [9],
                       "normalize_y": [False],
                       "copy_X_train": [True],
                       "random_state": [0]}
        gp = GaussianProcessRegressor()

        # gp = RandomForestRegressor()
        # param_grid = {
        #     "n_estimators": [10, 20, 30],
        #     "max_features": ["auto", "sqrt", "log2"],
        #     "min_samples_split": [2, 4, 8],
        #     "bootstrap": [True, False],
        # }
        # GaussianProcessRegressor(kernel=1.0 * RBF(length_scale=1.0, length_scale_bounds=(1e-1, 10.0)), n_restarts_optimizer=9)

        print("\nRunning grid search to tune up GPR parameters")
        # grid_search = GridSearchCV(gp, param_grid=param_grid, n_jobs=-1, scoring=None) #
        #grid_search = BayesSearchCV(gp, search_spaces=param_grid)
        grid_search = RandomizedSearchCV(gp, param_distributions=param_grid, n_jobs=-1, n_iter=1, scoring='neg_mean_squared_error')

        # grid_search = BayesSearchCV(gp, param_grid)

        # use a full grid over all parameters
        # grid_search = GridSearchCV(regressor, param_grid=param_grid, cv=5)

        grid_search.fit(x_train, np.ravel(y_train, order='C'))
        print("SearchCV took %.2f seconds for %d candidate parameter settings." % (time.time() - start, len(grid_search.cv_results_['params'])))
        report(grid_search.cv_results_)
        print(grid_search.best_params_)

        regressor_stats(grid_search, x_test, y_test)

        grid_search = GaussianProcessRegressor(kernel=1.0 * RBF(length_scale=1.0, length_scale_bounds=(1e-1, 10.0)), n_restarts_optimizer=9)
        grid_search.fit(x_train, np.ravel(y_train, order='C'))
        regressor_stats(grid_search, x_test, y_test)


def regressor():
    # Ensemble Methods
    # AdaBoost regressor
    regressor_test(AdaBoostRegressor(DecisionTreeRegressor(max_depth=4), n_estimators=300))
    # Bagging regressor
    regressor_test(BaggingRegressor(n_estimators=10))
    # Gradient Boosting for regression
    regressor_test(GradientBoostingRegressor(n_estimators=500, max_depth=4, min_samples_split=2, learning_rate=0.01, loss='ls'))
    # Ensemble Methods - decision trees
    regressor_test(ExtraTreesRegressor(n_estimators=10))
    regressor_test(RandomForestRegressor(n_estimators=10))
    # Decision Trees
    # Extremely randomized tree regressor
    regressor_test(ExtraTreeRegressor())
    # Decision tree regressor
    regressor_test(DecisionTreeRegressor())
    # Gaussian Processes
    regressor_test(GaussianProcessRegressor(kernel=1.0 * RBF(length_scale=1.0, length_scale_bounds=(1e-1, 10.0)), n_restarts_optimizer=9))
    regressor_test(GaussianProcessRegressor(kernel=1.0 * ExpSineSquared(length_scale=1.0, periodicity=3.0, length_scale_bounds=(0.1, 10.0), periodicity_bounds=(1.0, 10.0)), n_restarts_optimizer=9))
    regressor_test(GaussianProcessRegressor(kernel=1.0 * Matern(length_scale=1.0, length_scale_bounds=(1e-5, 1e5), nu=1.5), n_restarts_optimizer=9))
    regressor_test(GaussianProcessRegressor(kernel=ConstantKernel(1.0, (1e-3, 1e3)) * RBF(10, (1e-2, 1e2)), n_restarts_optimizer=9))
    # Generalized Linear Models
    # regressor_test(SGDRegressor())
    # Nearest Neighbors
    # Regression based on k-nearest neighbors
    regressor_test(KNeighborsRegressor(n_neighbors=6, weights='distance'))
    # Regression based on neighbors within a fixed radius
    regressor_test(RadiusNeighborsRegressor())
    regressor_test(KernelRidge(alpha=1.0))
    regressor_test(SVR(kernel='rbf', C=1e4, gamma=0.1))
    # Neural network models
    # Multi-layer Perceptron regressor
    regressor_test(MLPRegressor(hidden_layer_sizes=(6), activation='logistic', solver='lbfgs'))
    regressor_test(MLPRegressor(hidden_layer_sizes=(10,),  activation='relu', solver='adam', alpha=0.001, batch_size='auto',
                        learning_rate='constant', learning_rate_init=0.01, power_t=0.5, max_iter=1000, shuffle=True,
                        random_state=9, tol=0.0001, verbose=False, warm_start=False, momentum=0.9, nesterovs_momentum=True,
                        early_stopping=False, validation_fraction=0.1, beta_1=0.9, beta_2=0.999, epsilon=1e-08))


def regressor_data():
    # 200 samples
    # x_data = [array([3.19522146, 0.82868415, 0.23205016]), array([3.15370345, 1.22593145, 0.11826378]), array([2.7708699 , 0.81740855, 0.23120748]), array([3.27145427, 1.96392046, 0.13789192]), array([2.73423439, 1.68286442, 0.18747904]), array([2.86814177, 1.01104599, 0.33316012]), array([2.85440193, 1.12615491, 0.15396506]), array([3.00314457, 1.61540953, 0.16985145]), array([2.82683692, 0.7854771 , 0.32368923]), array([2.65379564, 1.72987439, 0.28007932]), array([3.03092777, 1.19664534, 0.36283346]), array([3.02578912, 1.57320726, 0.22081513]), array([3.06867042, 2.1460779 , 0.11169111]), array([3.39391499, 0.83198398, 0.28246791]), array([3.2128173 , 1.35734803, 0.33779795]), array([2.91833226, 0.87164047, 0.33441254]), array([2.98520484, 1.89401027, 0.15013529]), array([2.78484914, 1.80907269, 0.20479747]), array([3.32304965, 1.90929713, 0.18514062]), array([3.26354761, 0.64347481, 0.17234832]), array([2.8764305 , 2.00620486, 0.33110393]), array([2.79935408, 1.14984094, 0.37896041]), array([3.13213955, 1.07750095, 0.1052461 ]), array([2.95618945, 0.53383256, 0.25416529]), array([2.84820823, 1.37353702, 0.28609087]), array([3.20063296, 1.24917235, 0.32806062]), array([2.74466161, 1.4371921 , 0.10844118]), array([3.11578068, 1.06336818, 0.34308343]), array([2.66578948, 0.68152003, 0.34928118]), array([3.15627849, 2.18098491, 0.12528747]), array([2.71514729, 1.83653422, 0.34600681]), array([3.38064741, 1.65894278, 0.29048009]), array([3.05862872, 0.50077239, 0.10256531]), array([2.93941046, 1.22078014, 0.39928876]), array([3.28338399, 2.11815885, 0.32151305]), array([2.95014814, 1.73844875, 0.38126219]), array([2.81291721, 1.7691111 , 0.39254059]), array([3.23497592, 2.11032395, 0.32335815]), array([3.28423634, 1.18070544, 0.37600108]), array([3.00453595, 0.59303171, 0.11542368]), array([2.75815705, 1.42758884, 0.24050586]), array([3.03552471, 0.55813728, 0.27175174]), array([3.31871275, 0.55132117, 0.22919829]), array([3.0896838 , 1.40889183, 0.23452905]), array([2.62384384, 0.80024909, 0.19283189]), array([2.93116258, 1.69903544, 0.15594662]), array([2.73959995, 1.10144814, 0.35347953]), array([2.97755941, 1.02764662, 0.27605659]), array([3.32779584, 1.11618653, 0.26552848]), array([2.66060031, 1.59392651, 0.32657879]), array([2.9682339 , 1.92920285, 0.30829002]), array([2.70704649, 1.45547683, 0.34130295]), array([2.9226255 , 0.50900145, 0.39476274]), array([3.08558203, 1.25913263, 0.15827319]), array([2.74878309, 2.07473267, 0.10001102]), array([2.76145142, 0.84512943, 0.26329816]), array([2.61187825, 0.75558458, 0.19877217]), array([2.7408812 , 0.90044796, 0.10925221]), array([3.0118929 , 1.67359649, 0.22824319]), array([2.90673114, 1.48588819, 0.1587646 ]), array([3.2451493 , 2.03280533, 0.21039744]), array([2.90832567, 0.62621421, 0.24226   ]), array([3.30704236, 0.69766759, 0.36526734]), array([3.35202387, 1.05078282, 0.21830857]), array([2.89096222, 1.46089013, 0.24371086]), array([2.83876958, 0.41384197, 0.30281788]), array([3.17481561, 1.44000406, 0.39087355]), array([3.1836041 , 1.30899561, 0.1514706 ]), array([3.37788981, 1.49395536, 0.26355893]), array([3.23710058, 2.09603225, 0.3881219 ]), array([2.71692316, 1.26755692, 0.36914761]), array([2.91337625, 1.2829783 , 0.16363665]), array([2.78202209, 0.57945846, 0.25643232]), array([2.98976239, 0.94520192, 0.10651175]), array([3.21702217, 0.86431491, 0.12212344]), array([2.69097389, 1.51074096, 0.13724558]), array([3.22904615, 0.73959128, 0.13459745]), array([3.04095571, 1.48088017, 0.12391904]), array([2.75467253, 1.39489242, 0.25813496]), array([2.84651909, 1.85600664, 0.29589543]), array([2.67113956, 1.54269334, 0.39799097]), array([2.67302883, 2.12195137, 0.23670395]), array([2.96203862, 2.04193695, 0.22245833]), array([2.68593574, 1.50669159, 0.2480287 ]), array([2.94566653, 0.66934778, 0.13206848]), array([2.84062679, 0.71539854, 0.15455387]), array([2.60075119, 1.14079336, 0.29226735]), array([3.24057144, 1.88174249, 0.32500954]), array([3.25397807, 0.46004332, 0.14471952]), array([2.69270946, 2.0646132 , 0.19994739]), array([3.16385819, 1.31659782, 0.34192012]), array([2.62664407, 1.86406894, 0.25477226]), array([2.89718361, 1.5512848 , 0.12648695]), array([3.29119717, 1.6036484 , 0.35619626]), array([3.13996586, 1.86868461, 0.18095025]), array([3.39692847, 0.708633  , 0.18651744]), array([3.0455205 , 1.79620997, 0.28524939]), array([3.35066837, 0.91273685, 0.21299151]), array([2.63000268, 1.93690434, 0.3118155 ]), array([2.93220944, 1.91894462, 0.39208121]), array([3.17120395, 2.02388799, 0.12853828]), array([3.34116443, 1.90409499, 0.27094761]), array([2.61581075, 1.41213121, 0.21165005]), array([3.0149774 , 0.99695945, 0.35107954]), array([2.72367957, 1.69750141, 0.31976178]), array([3.29969084, 1.5618167 , 0.18272853]), array([2.7955789 , 1.32943382, 0.18133818]), array([3.35817091, 1.95420296, 0.21415464]), array([3.12510785, 0.96656936, 0.22427676]), array([2.80245146, 1.71296725, 0.14014803]), array([3.14002126, 1.9837695 , 0.37376163]), array([2.97201017, 1.75454548, 0.19569173]), array([2.83312738, 1.33345127, 0.11278201]), array([3.37405375, 2.06566315, 0.36765992]), array([2.61618943, 1.74843545, 0.11752579]), array([3.07934828, 1.66356226, 0.38771847]), array([3.38779011, 0.7730429 , 0.17642242]), array([2.69946754, 2.18981663, 0.39656343]), array([2.95223148, 1.53350612, 0.26052982]), array([3.33411845, 0.48834956, 0.33885087]), array([2.63373533, 1.72305913, 0.29123958]), array([3.2269892 , 0.42261891, 0.20152681]), array([3.2059411 , 1.3459102 , 0.30564294]), array([3.16483316, 1.63393216, 0.24505829]), array([2.60698413, 1.47048135, 0.31319686]), array([3.08167217, 1.35793719, 0.35808268]), array([2.83143352, 0.93468256, 0.1667297 ]), array([3.38865337, 0.85125146, 0.2356483 ]), array([3.32946505, 1.64368414, 0.30853078]), array([3.15049046, 0.63236018, 0.12780145]), array([3.36074003, 2.05381612, 0.35982802]), array([2.63604389, 1.82543384, 0.37169889]), array([3.03768099, 0.88950868, 0.22499737]), array([3.02071313, 1.64856   , 0.3623874 ]), array([3.31395139, 0.46379717, 0.19148026]), array([3.22371048, 1.56919967, 0.3365808 ]), array([3.19887018, 2.17076983, 0.28407727]), array([2.82114674, 1.11105508, 0.30418955]), array([3.10441998, 0.56811269, 0.30247072]), array([2.6564171 , 0.44206732, 0.31694194]), array([3.10833935, 1.01963742, 0.14519535]), array([2.79048567, 1.98552293, 0.20622973]), array([3.27377291, 0.91883477, 0.18923944]), array([3.13055644, 0.88203219, 0.2965646 ]), array([2.72835592, 1.21233581, 0.27726443]), array([2.94299605, 2.14760298, 0.16274286]), array([2.99414005, 0.72833463, 0.20851994]), array([2.81082356, 1.00426264, 0.37474122]), array([2.64852667, 0.97810408, 0.16128489]), array([3.09737214, 0.95668973, 0.26041403]), array([2.77248363, 0.44532371, 0.10374954]), array([2.77917782, 1.30343786, 0.26863189]), array([2.80698857, 0.73097057, 0.27477682]), array([2.64158981, 1.15814339, 0.3458831 ]), array([3.29550946, 1.27618246, 0.25114984]), array([2.88144962, 2.19898614, 0.20293766]), array([2.88567384, 0.66390422, 0.16569619]), array([2.64620518, 1.04093226, 0.14056106]), array([2.81800071, 1.08378318, 0.35664466]), array([3.14670238, 2.01268714, 0.17879026]), array([2.98178654, 1.97233912, 0.20730177]), array([2.89234729, 0.52885264, 0.27388627]), array([2.67875558, 0.60652599, 0.21697149]), array([2.70001832, 0.42955937, 0.25198605]), array([2.86775803, 0.6001339 , 0.38634946]), array([3.21005615, 1.28663453, 0.36615534]), array([3.01616422, 0.76174413, 0.24557682]), array([2.87283543, 1.6180505 , 0.38244599]), array([3.05429626, 1.78474929, 0.30007971]), array([3.18938089, 1.23684549, 0.24895764]), array([3.25105323, 0.61876986, 0.34783947]), array([3.33976256, 1.39152997, 0.2270725 ]), array([2.90228581, 1.8435617 , 0.35409964]), array([2.92680842, 1.81549583, 0.27909969]), array([3.25834062, 1.79855093, 0.23852385]), array([2.96493436, 1.94099666, 0.31848807]), array([3.04830647, 1.0906879 , 0.13098793]), array([2.86067965, 2.13296666, 0.2886244 ]), array([3.18404451, 1.19171976, 0.19654691]), array([3.06008285, 0.7800683 , 0.31492965]), array([3.11909441, 0.80995262, 0.37935089]), array([3.12276676, 1.16646489, 0.17679144]), array([2.76733667, 0.90898172, 0.19425065]), array([3.36866203, 0.95419076, 0.37080847]), array([3.36621541, 1.05326613, 0.17179867]), array([3.09511322, 0.49213899, 0.38451741]), array([2.70876791, 1.52275668, 0.33004608]), array([3.17948445, 1.58541447, 0.26747439]), array([3.27958482, 0.47476194, 0.17440843]), array([3.10046947, 0.65865309, 0.12091286]), array([2.99984227, 1.38027565, 0.14702545]), array([2.7259568 , 1.99438606, 0.14266336]), array([3.30338414, 2.16350893, 0.11350135]), array([3.06474302, 1.16989081, 0.29429995]), array([3.31021642, 0.98792204, 0.16855139]), array([3.07368733, 0.68864963, 0.21940574]), array([3.34635308, 0.57691563, 0.3113763 ]), array([2.85703712, 0.52198352, 0.29867167]), array([2.68072339, 2.08689767, 0.1331597 ]), array([3.26593784, 1.77186698, 0.14817704])]
    # y_data = [array([0.36311226]), array([0.90979678]), array([0.88802761]), array([8.52707333]), array([2.61057776]), array([7.00925757]), array([1.05988112]), array([3.38695282]), array([0.58977744]), array([19.0108044]), array([33.66338711]), array([13.60832167]), array([1.71392904]), array([5.97952348]), array([59.05592755]), array([3.57602187]), array([3.99584287]), array([8.46090671]), array([30.34807135]), array([2.51964768]), array([96.01649486]), array([18.91069517]), array([3.08438998]), array([2.45262612]), array([13.96404284]), array([39.73348446]), array([2.58281189]), array([21.38596189]), array([0.27656945]), array([6.12142089]), array([59.59126576]), array([92.68618462]), array([11.19102876]), array([41.09362638]), array([207.90873621]), array([109.7532197]), array([96.33378014]), array([193.97556999]), array([60.99622399]), array([8.97958665]), array([4.93828949]), array([1.08683403]), array([1.14284779]), array([13.06174295]), array([3.56283811]), array([1.86486296]), array([9.34060304]), array([3.87144024]), array([15.32287214]), array([25.8472935]), array([82.6229234]), array([24.5624633]), array([0.14981114]), array([0.23141543]), array([0.5215124]), array([0.24146423]), array([3.92612436]), array([7.24225081]), array([19.64845433]), array([0.51318768]), array([50.18064452]), array([1.75975393]), array([7.07672322]), array([4.45421853]), array([10.05065624]), array([4.02169791]), array([102.74670308]), array([0.46153275]), array([49.16092685]), array([306.72512777]), array([19.92180332]), array([0.18597497]), array([2.75207275]), array([5.22171687]), array([3.2718033]), array([0.74801004]), array([3.78197142]), array([0.21263646]), array([6.455444]), array([49.79330698]), array([47.92933604]), array([23.35174166]), array([33.74924908]), array([6.03467227]), array([6.85604265]), array([5.30897119]), array([1.90875287]), array([145.3039684]), array([7.74169474]), array([10.50351426]), array([50.57049311]), array([16.02643209]), array([0.31106207]), array([130.36368619]), array([16.56134235]), array([0.60458623]), array([60.60106122]), array([1.28073975]), array([40.97275114]), array([151.67479184]), array([4.82821424]), array([105.98019415]), array([0.85834118]), array([13.74296747]), array([35.69732156]), array([11.96990051]), array([0.31261165]), array([57.84396608]), array([0.89599483]), array([0.33881173]), array([207.95508291]), array([10.94231582]), array([2.31914544]), array([314.72625143]), array([1.1631265]), array([128.40033728]), array([0.47198988]), array([146.07323407]), array([20.16296855]), array([0.22769651]), array([20.65708629]), array([5.38992753]), array([40.66308066]), array([33.891337]), array([13.07311263]), array([55.15627839]), array([2.01055778]), array([2.04671649]), array([98.79389958]), array([6.42493086]), array([287.89770349]), array([61.24476078]), array([0.14990964]), array([92.57205217]), array([4.42450233]), array([92.8914586]), array([138.9277218]), array([5.92002927]), array([0.207282]), array([4.26303588]), array([0.9554922]), array([14.0267672]), array([0.18420564]), array([4.38336208]), array([3.78248594]), array([10.88347631]), array([1.2901644]), array([10.16088563]), array([3.16332121]), array([2.70211185]), array([13.40552687]), array([6.08834424]), array([0.4214107]), array([7.41412792]), array([19.58392732]), array([25.96296871]), array([5.03232365]), array([3.92421764]), array([11.81541156]), array([21.76045366]), array([23.87212203]), array([2.25516979]), array([4.73801353]), array([6.57198567]), array([0.24489152]), array([64.03896765]), array([0.16427882]), array([76.96663622]), array([70.91272401]), array([12.57523113]), array([1.88140404]), array([20.51941826]), array([95.87903651]), array([45.47690832]), array([51.95487978]), array([92.20530347]), array([1.49956415]), array([73.98632594]), array([2.53506609]), array([2.02322568]), array([10.23058711]), array([0.46372883]), array([1.37990805]), array([33.59490096]), array([0.65966006]), array([0.10969939]), array([25.82858825]), array([42.71514224]), array([5.36101314]), array([6.89775877]), array([0.18457328]), array([1.12147039]), array([5.53070025]), array([14.66276571]), array([0.15087437]), array([0.95103984]), array([0.58139433]), array([1.82816052]), array([0.69665806]), array([7.12515614])]

    # 100 samples
    x_data = [array([2.77507555, 1.0639158 , 0.36358241]), array([3.37662685, 1.60070222, 0.1914746 ]), array([3.23058574, 0.5311619 , 0.38856407]), array([2.88379172, 1.7717727 , 0.34106779]), array([3.1216565 , 1.10632931, 0.16073566]), array([2.92688144, 1.89952707, 0.27053604]), array([2.89567422, 1.32765864, 0.11873783]), array([2.86644543, 1.43088033, 0.17413912]), array([2.85385036, 2.13942809, 0.3771359 ]), array([3.11165046, 2.18973949, 0.39862367]), array([2.71271997, 1.04282127, 0.1410435 ]), array([3.39462796, 0.58401565, 0.13287225]), array([3.21739088, 1.57672191, 0.11381648]), array([3.32585899, 0.69614623, 0.30468658]), array([2.76384354, 0.88632084, 0.23485743]), array([2.90727115, 2.03918444, 0.20869932]), array([3.26234713, 1.13105568, 0.1008615 ]), array([2.81058006, 2.00730233, 0.37189761]), array([2.65967047, 0.61068403, 0.315166  ]), array([3.04545459, 2.11972149, 0.38321269]), array([3.15947717, 2.16066488, 0.36528758]), array([2.90001148, 1.49575139, 0.35068347]), array([3.30479718, 1.64328583, 0.18224427]), array([2.77999524, 0.79336424, 0.15458403]), array([3.19425194, 1.70669745, 0.29734207]), array([3.17237336, 0.58905027, 0.13474408]), array([2.82066857, 1.30123537, 0.12889036]), array([2.99988697, 0.41642183, 0.26134321]), array([2.63013791, 0.83808605, 0.28543027]), array([3.30284612, 1.88164417, 0.33694139]), array([3.36250323, 1.38909616, 0.2726466 ]), array([3.35141661, 1.27932086, 0.26708714]), array([2.79604884, 1.6663626 , 0.21184577]), array([3.1033117 , 0.8315693 , 0.28853356]), array([2.95690954, 1.81438367, 0.20546361]), array([2.70285247, 0.90907401, 0.16877228]), array([3.13930348, 0.56212384, 0.38142637]), array([2.73908243, 0.93720404, 0.25234753]), array([2.93521953, 1.5663302 , 0.21627177]), array([2.9687225 , 1.37157451, 0.24738687]), array([2.66828269, 1.15179593, 0.12205275]), array([3.02445666, 1.96685754, 0.19775754]), array([3.27017157, 2.06222134, 0.3382625 ]), array([3.06861844, 2.09067928, 0.3920447 ]), array([3.31225835, 1.92275186, 0.22207389]), array([2.68949818, 0.96962818, 0.16415115]), array([2.64363421, 1.76964476, 0.23793545]), array([3.19041643, 1.00458562, 0.28997952]), array([3.24462352, 1.01732254, 0.30824931]), array([3.16659927, 1.83307771, 0.37593654]), array([3.04899043, 0.91709836, 0.1497468 ]), array([3.07715431, 1.22170026, 0.32570673]), array([3.01161842, 1.97973104, 0.23906354]), array([2.63910372, 0.467666  , 0.34375533]), array([3.25534015, 1.54495127, 0.3227496 ]), array([3.0215269 , 1.45601269, 0.25361977]), array([2.99063859, 1.69647339, 0.13609287]), array([2.91904343, 1.93186696, 0.30089396]), array([2.65178573, 0.9606831 , 0.24112483]), array([2.83505847, 1.84557288, 0.11025884]), array([2.9775549 , 1.39419895, 0.30319615]), array([3.20069929, 2.09456472, 0.22814307]), array([2.78447817, 1.73301662, 0.10521589]), array([2.80701266, 0.68396526, 0.27476252]), array([2.82648656, 1.74567571, 0.16944897]), array([2.61883774, 1.53384882, 0.3329709 ]), array([2.6144217 , 0.65421362, 0.32073276]), array([2.86215834, 1.11643535, 0.10833204]), array([3.38766944, 0.81590563, 0.32912654]), array([3.29108539, 1.20318961, 0.23184767]), array([3.13085427, 1.23789185, 0.14289455]), array([3.33824973, 0.75702037, 0.26217371]), array([2.94220876, 0.72605391, 0.17980808]), array([2.74546085, 1.16189393, 0.31249888]), array([2.75555737, 0.54108324, 0.14559029]), array([3.14791092, 1.31795036, 0.28018136]), array([2.87448978, 1.08631407, 0.18609651]), array([2.71082058, 0.48401675, 0.18903402]), array([3.0597956 , 1.65085091, 0.34796448]), array([2.94464262, 0.98749089, 0.35914525]), array([2.73423989, 0.73625108, 0.20472242]), array([3.00346488, 2.17065809, 0.3857269 ]), array([2.84736729, 0.76961607, 0.25847991]), array([3.11476839, 1.7928249 , 0.15271719]), array([3.28210163, 1.47333268, 0.24470549]), array([3.21312105, 1.34644767, 0.27798243]), array([3.23720407, 1.25520634, 0.31824899]), array([3.08111765, 0.46128298, 0.19547162]), array([3.03422957, 1.98643763, 0.36722098]), array([3.17996935, 1.42522348, 0.22399333]), array([3.08802454, 0.63194011, 0.39404383]), array([3.27448127, 2.03240092, 0.17713192]), array([2.72421158, 0.66397397, 0.15769446]), array([3.35482359, 1.50377938, 0.35425123]), array([3.33230174, 1.86860339, 0.21917534]), array([2.67591614, 1.60883517, 0.292518  ]), array([2.9662472 , 0.86691936, 0.35550721]), array([2.60523344, 0.50917704, 0.11653739]), array([3.37574218, 1.17932412, 0.19911788]), array([2.68470621, 0.44158702, 0.12653109])]
    y_data = [array([10.26742871]), array([19.74766728]), array([1.16153775]), array([73.20729621]), array([0.15249333]), array([47.72675346]), array([1.54454327]), array([0.70147863]), array([159.77231162]), array([303.36594242]), array([3.36404181]), array([5.33914619]), array([0.18353749]), array([2.38719547]), array([0.42800366]), array([23.04666086]), array([2.27854933]), array([118.4405226]), array([1.3406887]), array([226.52855721]), array([252.26008448]), array([48.13600164]), array([15.05287171]), array([4.69018419]), array([78.18694986]), array([6.47098575]), array([1.48167124]), array([4.33715473]), array([0.35633495]), array([176.97212378]), array([41.91492067]), array([28.47770156]), array([6.79390362]), array([2.091046]), array([15.24428106]), array([3.02430253]), array([0.93701273]), array([0.22026044]), array([9.08359549]), array([10.2333154]), array([4.15158833]), array([21.85690557]), array([216.98509193]), array([240.79383583]), array([56.67345322]), array([2.77542625]), array([9.65577301]), array([9.73880168]), array([15.84356203]), array([178.3406836]), array([1.81449353]), array([27.20076325]), array([43.54656926]), array([3.03139694]), array([82.77138615]), array([17.53607577]), array([0.73447988]), array([69.80486663]), array([0.39916585]), array([0.3514719]), array([26.85281652]), array([65.8044821]), array([1.0743411]), array([0.74781763]), array([2.57432671]), array([21.2236981]), array([1.00451681]), array([4.23440178]), array([11.57095607]), array([10.54113428]), array([0.1590376]), array([1.46609927]), array([2.91288523]), array([6.55571063]), array([9.27851123]), array([24.17805658]), array([0.25778288]), array([8.1739414]), array([88.60141364]), array([11.83089157]), array([2.96109206]), array([228.82176422]), array([0.34295999]), array([5.31785001]), array([29.89174526]), array([29.52668125]), array([39.23796925]), array([5.72044569]), array([166.74889899]), array([14.37848824]), array([2.62879386]), array([29.25855384]), array([6.73643689]), array([118.67543064]), array([51.39460153]), array([18.00328135]), array([6.20116821]), array([12.54745892]), array([5.53979395]), array([12.53412931])]

    # 40 samples
    # x_data = [array([3.15515403, 1.63837969, 0.34838803]), array([2.82600191, 0.88918876, 0.24491263]), array([2.79712588, 1.10741012, 0.30699148]), array([2.60514268, 2.03161101, 0.1523619]), array([3.12056912, 1.35826753, 0.16868401]), array([3.08164189, 1.98298554, 0.26908501]), array([2.89388988, 1.1337424, 0.38018121]), array([3.34491242, 1.07852839, 0.35706431]), array([2.75860855, 0.47057735, 0.28102629]), array([3.3015233, 0.83798379, 0.37734001]), array([3.23077267, 1.26744304, 0.27863649]), array([2.97623682, 0.98640101, 0.39743293]), array([2.71289013, 1.54308721, 0.32524154]), array([2.66796701, 1.94423554, 0.30244582]), array([3.16446912, 2.15758765, 0.32166413]), array([3.03827599, 1.44096782, 0.20020952]), array([3.10860256, 0.99167696, 0.21145092]), array([2.72718061, 1.67781161, 0.23038015]), array([3.25384366, 1.49728027, 0.26481384]), array([2.90053825, 1.31538356, 0.31604207]), array([2.64545736, 1.77175878, 0.13821684]), array([2.8599703, 1.23634495, 0.29080166]), array([2.62752869, 0.52389602, 0.19153083]), array([2.68653505, 0.63552376, 0.36809632]), array([2.93525971, 0.42799011, 0.17777563]), array([3.18459007, 1.2076026, 0.22615254]), array([3.28630845, 1.90402766, 0.12209231]), array([3.38358219, 0.60864159, 0.13687508]), array([2.7730306, 1.61264336, 0.21299479]), array([3.07401849, 1.7484589, 0.25336432]), array([3.00452201, 1.43340184, 0.34262816]), array([3.32526383, 0.68349451, 0.18887131]), array([2.86746763, 0.92041526, 0.33471887]),      array([3.21749801, 2.08068254, 0.23534047]), array([2.98952136, 0.55941025, 0.1070578]), array([3.26879916, 1.81866268, 0.16042119]), array([2.94103742, 1.88070873, 0.11446226]), array([2.80868064, 0.80512819, 0.15424576]), array([3.36530663, 0.75627455, 0.12480294]), array([3.04553348, 2.14862658, 0.39135133])]
    # y_data = [array([103.38467948]), array([0.1893953]), array([5.54373833]), array([1.15958937]), array([1.47467042]), array([73.90430236]), array([23.46490354]), array([43.00547595]), array([4.0669171]), array([18.92207238]), array([24.70511204]), array([20.01588831]), array([25.97899015]), array([41.12654225]), array([181.50614535]), array([5.46508604]), array([0.51064104]), array([8.52161145]), array([39.51688787]), array([20.63624992]), array([0.33992506]), array([9.52963212]), array([7.89093736]), array([0.26635584]), array([8.40804503]), array([6.81332029]), array([3.68341863]), array([4.67429057]), array([5.29817906]), array([39.7296068]), array([48.52531865]), array([0.97232759]), array([4.09773608]), array([73.25967094]), array([10.26461276]), array([12.17566216]), array([0.25800679]), array([4.34935198]), array([3.51110835]), array([247.98844914])]

    n = 10
    x_train = x_data[:len(x_data)-n]
    y_train = y_data[:len(y_data)-n]
    x_test = x_data[-n:]
    y_test = y_data[-n:]

    print("Number of samples: {}".format(len(x_data)))

    return x_train, y_train, x_test, y_test


def regressor_stats(regressor, x_test, y_test):
    # test
    print(regressor.__class__.__name__)
    for i in range(len(x_test)):
        x = x_test[i]
        y = y_test[i]
        val = regressor.predict([x])

        value_problem = y[0]
        value_surrogate = val[0]
        percent = 100.0 * math.fabs(value_problem - value_surrogate) / math.fabs(value_problem)

        print("params = [{0:8.3f}, {1:8.3f}, {2:8.3f}], \teval = {3:8.3f}, \tpred = {4:8.3f}, \tdiff = {5:8.3f} \t({6:8.3f} %)".format(x[0], x[1], x[2], value_problem, value_surrogate,
                                                                                            math.fabs(value_problem - value_surrogate), percent))


def regressor_test(regressor):
    x_train, y_train, x_test, y_test = regressor_data()

    # fit
    regressor.fit(x_train, np.ravel(y_train, order='C'))

    regressor_stats(regressor, x_test, y_test)


# bobyqa()
# scikit()
regressor()
# regressor_optim()