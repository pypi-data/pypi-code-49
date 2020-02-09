import numpy as np
import scipy as sp

from ngboost.scores import LogScore
from ngboost.distns import Normal
from ngboost.manifold import manifold
from ngboost.learners import default_tree_learner, default_linear_learner

from sklearn.utils import check_random_state
from sklearn.base import clone
from sklearn.tree import DecisionTreeRegressor

# import pdb

class NGBoost(object):
    '''
    Constructor for all NGBoost models.

    This class implements the methods that are common to all NGBoost models. Unless you are implementing a new kind of regression (e.g. interval-censored, etc.), you should probably use one of NGBRegressor, NGBClassifier, or NGBSurvival.

    Parameters:
        Dist              : assumed distributional form of Y|X=x. A distribution from ngboost.distns, e.g. Normal
        Score             : rule to compare probabilistic predictions P̂ to the observed data y. A score from ngboost.scores, e.g. LogScore
        Base              : base learner to use in the boosting algorithm. Any instantiated sklearn regressor, e.g. DecisionTreeRegressor()
        natural_gradient  : logical flag indicating whether the natural gradient should be used
        n_estimators      : the number of boosting iterations to fit
        learning_rate     : the learning rate
        minibatch_frac    : the percent subsample of rows to use in each boosting iteration
        verbose           : flag indicating whether output should be printed during fitting
        verbose_eval      : increment (in boosting iterations) at which output should be printed
        tol               : numerical tolerance to be used in optimization
        random_state      : seed for reproducibility. See https://stackoverflow.com/questions/28064634/random-state-pseudo-random-number-in-scikit-learn
    Output:
        An NGBRegressor object that can be fit.
    '''
    def __init__(self, Dist=Normal, Score=LogScore,
                 Base=default_tree_learner, natural_gradient=True,
                 n_estimators=500, learning_rate=0.01, minibatch_frac=1.0,
                 verbose=True, verbose_eval=100, tol=1e-4,
                 random_state=None):
        self.Dist = Dist
        self.Score = Score
        self.Base = Base
        self.Manifold = manifold(Score, Dist)
        self.natural_gradient = natural_gradient
        self.n_estimators = n_estimators
        self.learning_rate = learning_rate
        self.minibatch_frac = minibatch_frac
        self.verbose = verbose
        self.verbose_eval = verbose_eval
        self.init_params = None
        self.base_models = []
        self.scalings = []
        self.tol = tol
        self.random_state = check_random_state(random_state)
        self.best_val_loss_itr = None

    def fit_init_params_to_marginal(self, Y, sample_weight=None, iters=1000):
        self.init_params = self.Manifold.fit(Y) # would be best to put sample weights here too
        return

    def pred_param(self, X, max_iter=None):
        m, n = X.shape
        params = np.ones((m, self.Manifold.n_params)) * self.init_params
        for i, (models, s) in enumerate(zip(self.base_models, self.scalings)):
            if max_iter and i == max_iter:
                break
            resids = np.array([model.predict(X) for model in models]).T
            params -= self.learning_rate * resids * s
        return params

    def sample(self, X, Y, params):
        if self.minibatch_frac == 1.0:
            return np.arange(len(Y)), X, Y, params
        sample_size = int(self.minibatch_frac * len(Y))
        idxs = self.random_state.choice(np.arange(len(Y)), sample_size, replace=False)
        return idxs, X[idxs,:], Y[idxs], params[idxs, :]

    def fit_base(self, X, grads, sample_weight=None):
        models = [clone(self.Base).fit(X, g, sample_weight=sample_weight) for g in grads.T]
        fitted = np.array([m.predict(X) for m in models]).T
        self.base_models.append(models)
        return fitted

    def line_search(self, resids, start, Y, sample_weight=None, scale_init=1):
        S = self.Score
        D_init = self.Manifold(start.T)
        loss_init = D_init.total_score(Y, sample_weight)
        scale = scale_init

        # first scale up
        while True:
            scaled_resids = resids * scale
            D = self.Manifold((start - scaled_resids).T)
            loss = D.total_score(Y, sample_weight)
            norm = np.mean(np.linalg.norm(scaled_resids, axis=1))
            if not np.isfinite(loss) or loss > loss_init or scale > 256:
                break
            scale = scale * 2

        # then scale down
        while True:
            scaled_resids = resids * scale
            D = self.Manifold((start - scaled_resids).T)
            loss = D.total_score(Y, sample_weight)
            norm = np.mean(np.linalg.norm(scaled_resids, axis=1))
            if np.isfinite(loss) and (loss < loss_init or norm < self.tol) and\
               np.linalg.norm(scaled_resids, axis=1).mean() < 5.0:
                break
            scale = scale * 0.5
        self.scalings.append(scale)
        return scale

    def fit(self, X, Y,
            X_val = None, Y_val = None,
            sample_weight = None, val_sample_weight = None,
            train_loss_monitor = None, val_loss_monitor = None,
            early_stopping_rounds = None):
        '''
        Fits an NGBoost model to the data

        Parameters:
            X                       : numpy array of predictors (n x p)
            Y                       : numpy array of outcomes (n). Should be floats for regression and integers from 0 to K-1 for K-class classification
            X_val                   : validation-set predictors, if any
            Y_val                   : validation-set outcomes, if any
            sample_weight           : how much to weigh each example in the training set. numpy array of size (n) (defaults to 1)
            val_sample_weight       : how much to weigh each example in the validation set. (defaults to 1)
            train_loss_monitor      : a custom score or set of scores to track on the training set during training. Defaults to the score defined in the NGBoost constructor
            val_loss_monitor        : a custom score or set of scores to track on the validation set during training. Defaults to the score defined in the NGBoost constructor
            early_stopping_rounds   : the number of consecutive boosting iterations during which the loss has to increase before the algorithm stops early

        Output:
            A fit NGBRegressor object
        '''

        loss_list = []
        self.fit_init_params_to_marginal(Y)

        params = self.pred_param(X)
        if X_val is not None and Y_val is not None:
            val_params = self.pred_param(X_val)
            val_loss_list = []
            best_val_loss = np.inf

        if not train_loss_monitor:
            train_loss_monitor = lambda D,Y: D.total_score(Y, sample_weight=sample_weight)

        if not val_loss_monitor:
            val_loss_monitor = lambda D,Y: D.total_score(Y, sample_weight=val_sample_weight)

        for itr in range(self.n_estimators):
            _, X_batch, Y_batch, P_batch = self.sample(X, Y, params)

            D = self.Manifold(P_batch.T)

            loss_list += [train_loss_monitor(D, Y_batch)]
            loss = loss_list[-1]
            grads = D.grad(Y_batch, natural=self.natural_gradient)

            proj_grad = self.fit_base(X_batch, grads, sample_weight)
            scale = self.line_search(proj_grad, P_batch, Y_batch, sample_weight)

            # pdb.set_trace()
            params -= self.learning_rate * scale * np.array([m.predict(X) for m in self.base_models[-1]]).T

            val_loss = 0
            if X_val is not None and Y_val is not None:
                val_params -= self.learning_rate * scale * np.array([m.predict(X_val) for m in self.base_models[-1]]).T
                val_loss = val_loss_monitor(self.Manifold(val_params.T), Y_val)
                val_loss_list += [val_loss]
                if val_loss < best_val_loss:
                        best_val_loss, self.best_val_loss_itr = val_loss, itr
                if early_stopping_rounds is not None and best_val_loss < np.min(np.array(val_loss_list[-early_stopping_rounds:])):
                    if self.verbose:
                        print(f"== Early stopping achieved.")
                        print(f"== Best iteration / VAL {self.best_val_loss_itr} (val_loss={best_val_loss:.4f})")
                    break

            if self.verbose and int(self.verbose_eval) > 0 and itr % int(self.verbose_eval) == 0:
                grad_norm = np.linalg.norm(grads, axis=1).mean() * scale
                print(f"[iter {itr}] loss={loss:.4f} val_loss={val_loss:.4f} scale={scale:.4f} "
                      f"norm={grad_norm:.4f}")

            if np.linalg.norm(proj_grad, axis=1).mean() < self.tol:
                if self.verbose:
                    print(f"== Quitting at iteration / GRAD {itr}")
                break


        self.evals_result = {}
        metric = self.Score.__name__.upper()
        self.evals_result['train'] = {metric: loss_list}
        if X_val is not None and Y_val is not None:
            self.evals_result['val'] = {metric: val_loss_list}

        return self

    def score(self, X, Y):
        return self.Manifold(self.pred_dist(X)._params).total_score(Y)

    def pred_dist(self, X, max_iter=None):
        '''
        Predict the conditional distribution of Y at the points X=x

        Parameters:
            X        : numpy array of predictors (n x p)
            max_iter : get the prediction at the specified number of boosting iterations

        Output:
            A NGBoost distribution object
        '''
        if max_iter is not None: # get prediction at a particular iteration if asked for
            dist = self.staged_pred_dist(X, max_iter=max_iter)[-1]
        elif self.best_val_loss_itr is not None: # this will exist if there's a validation set
            dist = self.staged_pred_dist(X, max_iter=self.best_val_loss_itr)[-1]
        else:
            params = np.asarray(self.pred_param(X, max_iter))
            dist = self.Dist(params.T)
        return dist

    def staged_pred_dist(self, X, max_iter=None):
        '''
        Predict the conditional distribution of Y at the points X=x at multiple boosting iterations

        Parameters:
            X        : numpy array of predictors (n x p)
            max_iter : largest number of boosting iterations to get the prediction for

        Output:
            A list of NGBoost distribution objects, one per boosting stage up to max_iter
        '''
        predictions = []
        m, n = X.shape
        params = np.ones((m, self.Dist.n_params)) * self.init_params
        for i, (models, s) in enumerate(zip(self.base_models, self.scalings)):
            resids = np.array([model.predict(X) for model in models]).T
            params -= self.learning_rate * resids * s
            dists = self.Dist(np.copy(params.T)) # if the params aren't copied, param changes with stages carry over to dists
            predictions.append(dists)
            if max_iter and i == max_iter:
                break
        return predictions

    def predict(self, X, max_iter=None):
        '''
        Point prediction of Y at the points X=x

        Parameters:
            X        : numpy array of predictors (n x p)
            max_iter : get the prediction at the specified number of boosting iterations

        Output:
            Numpy array of the estimates of Y
        '''
        return self.pred_dist(X, max_iter=max_iter).predict()

    def staged_predict(self, X, max_iter=None):
        '''
        Point prediction of Y at the points X=x at multiple boosting iterations

        Parameters:
            X        : numpy array of predictors (n x p)
            max_iter : largest number of boosting iterations to get the prediction for

        Output:
            A list of numpy arrays of the estimates of Y, one per boosting stage up to max_iter
        '''
        return [dist.predict() for dist in self.staged_pred_dist(X, max_iter=max_iter)]

    @property
    def feature_importances_(self):
        """
        Return the feature importances for all parameters in the distribution
            (the higher, the more important the feature).

        Returns
        -------
        feature_importances_ : array, shape = [n_params, n_features]
            The summation along second axis of this array is an array of ones,
            unless all trees are single node trees consisting of only the root
            node, in which case it will be an array of zeros.
        """
        # Check whether the model is fitted
        if not self.base_models:
            return None
        # Check whether the base model is DecisionTreeRegressor
        if not isinstance(self.base_models[0][0], DecisionTreeRegressor):
            return None
        # Reshape the base_models
        params_trees = zip(*self.base_models)
        # Get the feature_importances_ for all the params and all the trees
        all_params_importances = [[getattr(tree, 'feature_importances_')
            for tree in trees if tree.tree_.node_count > 1]
                for trees in params_trees]

        if not all_params_importances:
            return np.zeros(len(self.base_models[0]),self.base_models[0][0].n_features_, dtype=np.float64)
        # Weighted average of importance by tree scaling factors
        all_params_importances = np.average(all_params_importances,
                                  axis=1, weights=self.scalings)
        return all_params_importances / np.sum(all_params_importances,axis=1,keepdims=True)
