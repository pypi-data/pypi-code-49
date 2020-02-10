from artap.problem import Problem
from artap.benchmark_functions import Booth
from artap.surrogate import SurrogateModelEval, SurrogateModelScikit


from sklearn.svm import SVR
from sklearn.neural_network import MLPRegressor
from sklearn.linear_model import SGDRegressor
from sklearn.tree import DecisionTreeRegressor, ExtraTreeRegressor
from sklearn.ensemble import AdaBoostRegressor, GradientBoostingRegressor, RandomForestRegressor, ExtraTreesRegressor, BaggingRegressor
from sklearn.kernel_ridge import KernelRidge
from sklearn.neighbors import KNeighborsRegressor, RadiusNeighborsRegressor
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF, Matern, DotProduct, WhiteKernel, ConstantKernel, RationalQuadratic, ExpSineSquared


class ProblemBooth(Problem):
    def __init__(self, name):
        parameters = {'x_1': {'initial_value': 2.5, 'bounds': [-10, 10]},
                      'x_2': {'initial_value': 1.5, 'bounds': [-10, 10]}}

        # costs = {'F': {'type': Problem.MINIMIZE, 'value': 0.0}}
        costs = ['F']

        super().__init__(name, parameters, costs)

        # enable surrogate
        self.surrogate = SurrogateModelScikit(self)

    def evaluate(self, x):
        return [Booth.eval(x)]


def output(regressor):
    xmeas = [[2.5, 1.5], [7.5, 1.5], [2.5, 6.5], [-2.5, 1.5], [2.5, -3.5], [2.2, 1.8], [2.69898454, 1.83185008], [2.23185008, 1.30101546], [1.98284599, 1.98211189], [1.94231886, 2.0199368]]
    ymeas = [[4.5], [144.5], [114.5], [114.5], [144.5], [2.88], [5.37826428], [5.27686152], [2.00699423], [1.85418726]]

    problem = ProblemBooth("ProblemBooth")
    problem.surrogate = SurrogateModelScikit(problem)
    problem.surrogate.sigma_threshold = 0.1
    problem.surrogate.train_step = len(xmeas)
    problem.surrogate.x_data = xmeas
    problem.surrogate.y_data = ymeas

    p = [1.04, 3.02]
    val = problem.evaluate(p)

    problem.surrogate.regressor = regressor
    problem.surrogate.train()
    res = problem.surrogate.predict(p)

    # print(problem.surrogate.regressor)
    print("optimum: value = {}, predict = {}, class = {}".format(val, res, problem.surrogate.regressor.__class__.__name__))


# Ensemble Methods
# AdaBoost regressor
output(AdaBoostRegressor(DecisionTreeRegressor(max_depth=4), n_estimators=300))
# Bagging regressor
output(BaggingRegressor(n_estimators=10))
# Gradient Boosting for regression
output(GradientBoostingRegressor(n_estimators=500, max_depth=4, min_samples_split=2, learning_rate=0.01, loss='ls'))
# Ensemble Methods - decision trees
output(ExtraTreesRegressor(n_estimators=10))
output(RandomForestRegressor(n_estimators=10))
# Decision Trees
# Extremely randomized tree regressor
output(ExtraTreeRegressor())
# Decision tree regressor
output(DecisionTreeRegressor())

# Gaussian Processes
output(GaussianProcessRegressor(kernel=1.0 * RBF(length_scale=1.0, length_scale_bounds=(1e-1, 10.0)), n_restarts_optimizer=9))
output(GaussianProcessRegressor(kernel=1.0 * ExpSineSquared(length_scale=1.0, periodicity=3.0, length_scale_bounds=(0.1, 10.0), periodicity_bounds=(1.0, 10.0)), n_restarts_optimizer=9))
output(GaussianProcessRegressor(kernel=1.0 * Matern(length_scale=1.0, length_scale_bounds=(1e-5, 1e5), nu=1.5), n_restarts_optimizer=9))
output(GaussianProcessRegressor(kernel=ConstantKernel(1.0, (1e-3, 1e3)) * RBF(10, (1e-2, 1e2)), n_restarts_optimizer=9))

# Generalized Linear Models
output(SGDRegressor())

# Nearest Neighbors
# Regression based on k-nearest neighbors
output(KNeighborsRegressor(n_neighbors=6, weights='distance'))
# Regression based on neighbors within a fixed radius
output(RadiusNeighborsRegressor())

output(KernelRidge(alpha=1.0))
output(SVR(kernel='rbf', C=1e4, gamma=0.1))

# Neural network models
# Multi-layer Perceptron regressor
output(MLPRegressor(hidden_layer_sizes=(6), activation='logistic', solver='lbfgs'))
output(MLPRegressor(hidden_layer_sizes=(10,),  activation='relu', solver='adam', alpha=0.001, batch_size='auto',
                    learning_rate='constant', learning_rate_init=0.01, power_t=0.5, max_iter=1000, shuffle=True,
                    random_state=9, tol=0.0001, verbose=False, warm_start=False, momentum=0.9, nesterovs_momentum=True,
                    early_stopping=False, validation_fraction=0.1, beta_1=0.9, beta_2=0.999, epsilon=1e-08))
