
import math
import pylab as pl
import numpy as np

from artap.problem import Problem
from artap.benchmark_functions import Booth
from artap.surrogate import SurrogateModelEval, SurrogateModelScikit


from sklearn.svm import SVR
from sklearn.neural_network import MLPRegressor
from sklearn.linear_model import BayesianRidge
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import AdaBoostRegressor, GradientBoostingRegressor, RandomForestRegressor, ExtraTreesRegressor
from sklearn.kernel_ridge import KernelRidge
from sklearn.model_selection import GridSearchCV
from sklearn.neighbors import KNeighborsRegressor
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF, Matern, DotProduct, WhiteKernel, ConstantKernel, RationalQuadratic, ExpSineSquared


class MyProblemSin(Problem):
    """ Describe simple one objective optimization problem. """
    def __init__(self, name):
        parameters = {'x_1': {'initial_value': 2.5, 'bounds': [0, 10]}}

        costs = ['F']

        super().__init__(name, parameters, costs)

    def evaluate(self, x):
        return [x[0] * math.sin(x[0])]


problem = MyProblemSin("MyProblemSin")
xref = pl.linspace(0, 10, 100)
yref = []
for x in xref:
    yref.append(problem.evaluate([x])[0])
xmeas = [1., 2., 3., 4, 5., 6., 7., 8., 10]
ymeas = []
for x in xmeas:
    ymeas.append(problem.evaluate([x])[0])


kernels = [1.0 * RBF(length_scale=1.0, length_scale_bounds=(1e-1, 10.0)),
           #1.0 * RationalQuadratic(length_scale=1.0, alpha=0.1),
           1.0 * ExpSineSquared(length_scale=1.0, periodicity=3.0, length_scale_bounds=(0.1, 10.0), periodicity_bounds=(1.0, 10.0)),
           #ConstantKernel(0.1, (0.01, 10.0)) * (DotProduct(sigma_0=1.0, sigma_0_bounds=(0.1, 10.0)) ** 2),
           1.0 * Matern(length_scale=1.0, length_scale_bounds=(1e-5, 1e5), nu=1.5),
           ConstantKernel(1.0, (1e-3, 1e3)) * RBF(10, (1e-2, 1e2))]

kernels = [1.0 * Matern(length_scale=1.0, length_scale_bounds=(1e-5, 1e5), nu=1.5)]
# kernels = []


def f(x):
    return x * math.sin(x)


def fit(gp, with_sigma=True):
    # Fit to data using Maximum Likelihood Estimation of the parameters
    X = []
    for x in xmeas:
        X.append([x])
    y = []
    for val in X:
        y.append([f(val[0])])
    # print(X, y)
    gp.fit(X, y)

    # Make the prediction on the meshed x-axis (ask for MSE as well)
    lysur = []
    lsigma = []
    for x in xref:
        if with_sigma:
            p, sig = gp.predict([[x]], return_std=True)
        else:
            p = gp.predict([[x]])
            sig = [0]

        lysur.append(p[0])
        lsigma.append(sig[0])

    return lysur, lsigma


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

ysur = []
sigma = []
for kernel in kernels:
    print(kernel)

    problem = MyProblemSin("MyProblemSin")
    problem.surrogate = SurrogateModelScikit(problem)
    #  problem.surrogate.options['sigma_threshold'] = 0.1
    # problem.surrogate.options['train_step'] = len(xmeas)
    # problem.surrogate.regressor = GaussianProcessRegressor(kernel=kernel, n_restarts_optimizer=9)
    # problem.surrogate.regressor = DecisionTreeRegressor()

    param_grid = {
        "hidden_layer_sizes": [(3), (10), (15), (20), (50)],
        "activation": ['logistic', 'relu']
    }
    gp = MLPRegressor(solver='lbfgs')
    grid_search = GridSearchCV(gp, param_grid=param_grid, n_jobs=-1, scoring=None) #
    problem.surrogate.regressor = grid_search

    # train
    for val in xmeas:
        problem.surrogate.evaluate([val])
    problem.surrogate.train()
    report(problem.surrogate.regressor.cv_results_)

    lysur = []
    lsigma = []
    for x in xref:
        # p, sig = problem.surrogate.regressor.predict([[x]], return_std=True)
        p = problem.surrogate.regressor.predict([[x]])
        lysur.append(p[0])
        #lsigma.append(sig[0])
    ysur.append(lysur)
    #sigma.append(lsigma)

    # Instantiate a Gaussian Process model
    # gp = GaussianProcessRegressor(kernel=kernel, n_restarts_optimizer=9)
    #
    # lysur, lsigma = fit(gp)
    # ysur.append(lysur)
    # sigma.append(lsigma)

# br = BayesianRidge()
# lysur, lsigma = fit(br, False)
# ysur.append(lysur)
# sigma.append(lsigma)

# ada = AdaBoostRegressor(DecisionTreeRegressor(max_depth=4), n_estimators=300)
# lysur, lsigma = fit(ada, False)
# ysur.append(lysur)
# sigma.append(lsigma)

# clf = DecisionTreeRegressor()
# lysur, lsigma = fit(clf, False)
# ysur.append(lysur)
# sigma.append(lsigma)

# gbr = GradientBoostingRegressor(n_estimators=500, max_depth=4, min_samples_split=2, learning_rate=0.01, loss='ls')
# lysur, lsigma = fit(gbr, False)
# ysur.append(lysur)
# sigma.append(lsigma)

# br = BayesianRidge()
# lysur, lsigma = fit(br, False)
# ysur.append(lysur)
# sigma.append(lsigma)

# br = KNeighborsRegressor(n_neighbors=6, weights='distance')
# lysur, lsigma = fit(br, False)
# ysur.append(lysur)
# sigma.append(lsigma)

# nn = MLPRegressor(
#     hidden_layer_sizes=(10,),  activation='relu', solver='adam', alpha=0.001, batch_size='auto',
#     learning_rate='constant', learning_rate_init=0.01, power_t=0.5, max_iter=1000, shuffle=True,
#     random_state=9, tol=0.0001, verbose=False, warm_start=False, momentum=0.9, nesterovs_momentum=True,
#     early_stopping=False, validation_fraction=0.1, beta_1=0.9, beta_2=0.999, epsilon=1e-08)

# nn = MLPRegressor(hidden_layer_sizes=(6), activation='logistic', solver='lbfgs')
# lysur, lsigma = fit(nn, False)
# ysur.append(lysur)
# sigma.append(lsigma)

#svr_rbf = SVR(kernel='rbf', C=1e4, gamma=0.1)
#lysur, lsigma = fit(svr_rbf, False)
#ysur.append(lysur)
#sigma.append(lsigma)

# rf = ExtraTreesRegressor(n_estimators=10)
# lysur, lsigma = fit(rf, False)
# ysur.append(lysur)
# sigma.append(lsigma)
# print(rf.predict([[4.9]]))

pl.close()
pl.rc('text', usetex=True)
pl.rc('figure', figsize=[6.4, 8])

xref = pl.array(xref)
for i in range(len(ysur)):
    ys = pl.array(ysur[i])
    # sig = pl.array(sigma[i])

    pl.subplot(len(ysur), 1, i+1)
    pl.plot(xref, yref, '-r', linewidth=1.5)
    pl.plot(xmeas, ymeas, 'or')
    pl.plot(xref, ys)
    #pl.fill(pl.concatenate([xref, xref[::-1]]),
    #        pl.concatenate([ys - 1.9600 * sig,
    #                       (ys + 1.9600 * sig)[::-1]]),
    #        alpha=.5, fc='b', ec='None', label='95% confidence interval')
    pl.grid()
    pl.xlabel("$x$")
    pl.ylabel("$y$")
    # pl.xlabel(kernel)

pl.savefig("/tmp/surrogate.pdf")
# pl.show()
