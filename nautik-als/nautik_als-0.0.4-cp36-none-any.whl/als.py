""" Implicit Alternating Least Squares """
import functools
import heapq
import logging
import time

import numpy as np
import scipy
import scipy.sparse
from tqdm.auto import tqdm

from . import _als
from .recommender_base import MatrixFactorizationBase
from .utils import check_blas_config, nonzeros

log = logging.getLogger("implicit")


class AlternatingLeastSquares(MatrixFactorizationBase):

    """ Alternating Least Squares

    A Recommendation Model based off the algorithms described in the paper 'Collaborative
    Filtering for Implicit Feedback Datasets' with performance optimizations described in
    'Applications of the Conjugate Gradient Method for Implicit Feedback Collaborative
    Filtering.'

    Parameters
    ----------
    factors : int, optional
        The number of latent factors to compute
    regularization : float, optional
        The regularization factor to use
    dtype : data-type, optional
        Specifies whether to generate 64 bit or 32 bit floating point factors
    use_native : bool, optional
        Use native extensions to speed up model fitting
    use_cg : bool, optional
        Use a faster Conjugate Gradient solver to calculate factors
    use_gpu : bool, optional
        Fit on the GPU if available, default is to run on GPU only if available
    iterations : int, optional
        The number of ALS iterations to use when fitting data
    calculate_training_loss : bool, optional
        Whether to log out the training loss at each iteration
    num_threads : int, optional
        The number of threads to use for fitting the model. This only
        applies for the native extensions. Specifying 0 means to default
        to the number of cores on the machine.

    Attributes (optional)
    ----------
    user_factors : ndarray [n_users * factors]
        Array of latent factors for each item in the training set
    item_factors : ndarray [n_items * factors]
        Array of latent factors for each item in the training set
    user_features : ndarray [n_user_features * n_users]
        Array of user features to code in user_factors after each iteration
    item_features: ndarray [n_item_features * n_items]
        Array of item features to code in item_factors after each iteration       
    """

    def __init__(self, factors=100, 
                 user_factors=None, item_factors=None, 
                 user_features=None, item_features=None,
                 regularization=0.01, dtype=np.float64,
                 use_native=True, use_cg=True, use_gpu=None,
                 iterations=15, calculate_training_loss=False, num_threads=0,
                 set_seed=False):
        super(AlternatingLeastSquares, self).__init__()


        
        # attributes for data preparation
        self.user_index = None
        self.item_index = None
        
        # parameters on how to factorize
        self.factors = factors
        self.user_factors=user_factors
        self.item_factors=item_factors
        self.user_features=user_features
        self.item_features=item_features
        self.regularization = regularization

        # options on how to fit the model
        self.dtype = dtype
        self.use_native = use_native
        self.use_cg = use_cg
        self.use_gpu = use_gpu
        self.iterations = iterations
        self.calculate_training_loss = calculate_training_loss
        self.num_threads = num_threads
        self.fit_callback = None
        self.cg_steps = 3
        self.set_seed = False

        # cache for item factors squared
        self._YtY = None

        check_blas_config()


    def fit(self, item_users, show_progress=True):
        """ Factorizes the item_users matrix.

        After calling this method, the members 'user_factors' and 'item_factors' will be
        initialized with a latent factor model of the input data.

        The item_users matrix does double duty here. It defines which items are liked by which
        users (P_iu in the original paper), as well as how much confidence we have that the user
        liked the item (C_iu).

        The negative items are implicitly defined: This code assumes that non-zero items in the
        item_users matrix means that the user liked the item. The negatives are left unset in this
        sparse matrix: the library will assume that means Piu = 0 and Ciu = 1 for all these items.

        Parameters
        ----------
        item_users: csr_matrix
            Matrix of confidences for the liked items. This matrix should be a csr_matrix where
            the rows of the matrix are the item, the columns are the users that liked that item,
            and the value is the confidence that the user liked the item.
        show_progress : bool, optional
            Whether to show a progress bar during fitting
        """
        Ciu = item_users
        if not isinstance(Ciu, scipy.sparse.csr_matrix):
            s = time.time()
            log.debug("Converting input to CSR format")
            Ciu = Ciu.tocsr()
            log.debug("Converted input to CSR in %.3fs", time.time() - s)

        if Ciu.dtype != np.float32:
            Ciu = Ciu.astype(np.float32)

        try:
            if self.user_features.dtype != np.float32:
                self.user_features = self.user_features.astype(np.float32)    
        except:
            print(type(self.user_features))
            pass
        
        try:
            if self.item_features.dtype != np.float32:
                self.item_features = self.item_features.astype(np.float32)  
        except:
            print(type(self.item_features))
            pass
                
        s = time.time()
        Cui = Ciu.T.tocsr()
        log.debug("Calculated transpose in %.3fs", time.time() - s)

        # dimensions
        items, users = Ciu.shape


        s = time.time()
        
        # set seed
        if self.set_seed:
            np.random.seed(42)
        
        # Initialize the variables randomly if they haven't already been set
        if self.user_factors is None:
            self.user_factors = np.random.rand(users, self.factors).astype(self.dtype) * 0.01

        if self.item_factors is None:
            self.item_factors = np.random.rand(items, self.factors).astype(self.dtype) * 0.01

        if self.user_features is None:
            user_features_provided = False
        else:
            user_features_provided = True
            n_user_features = self.user_features.shape[1]
        if self.item_features is None:
            item_features_provided = False
        else:
            item_features_provided = True
            n_item_features = self.item_features.shape[1]
            
     
        log.debug("Initialized factors in %s", time.time() - s)

        # invalidate cached norms and squared factors
        self._item_norms = None
        self._YtY = None

        if self.use_gpu:
            return self._fit_gpu(Ciu, Cui, show_progress)

        solver = self.solver

        log.debug("Running %i ALS iterations", self.iterations)
        with tqdm(total=self.iterations, disable=not show_progress) as progress:
            # alternate between learning the user_factors from the item_factors and vice-versa
            print('user_features_provided: {}'.format(user_features_provided))
            print('item_features_provided: {}'.format(item_features_provided))
            for iteration in range(self.iterations):
                s = time.time()
                # train X
                solver(Cui, self.user_factors, self.item_factors, self.regularization,
                       num_threads=self.num_threads)
                # implant user features if provided
                if user_features_provided:
                    for i in range(n_user_features):
                        self.user_factors[:,-(i+1)] = self.user_features[:,i].reshape(users)
                s1 = time.time()
                print('Iteration {}, approximate X: {} s.'.format(iteration, round(s1 - s, 2)))
                
                
                # train Y
                solver(Ciu, self.item_factors, self.user_factors, self.regularization,
                       num_threads=self.num_threads)
                progress.update(1)
                # implant item features if provided
                if item_features_provided:
                    for i in range(n_item_features):
                        self.item_factors[:,-(i+1)] = self.item_features[:,i].reshape(items)
                s2 = time.time()
                print('Iteration {}, approximate Y: {} s.'.format(iteration, round(s2 - s1, 2)))
                

                if self.calculate_training_loss:
                    loss = _als.calculate_loss(Cui, self.user_factors, self.item_factors,
                                               self.regularization, num_threads=self.num_threads)
                    progress.set_postfix({"loss": loss})

                if self.fit_callback:
                    self.fit_callback(iteration, time.time() - s)

        if self.calculate_training_loss:
            log.info("Final training loss %.4f", loss)


    def recalculate_user(self, userid, user_items):
        return user_factor(self.item_factors, self.YtY,
                           user_items.tocsr(), userid,
                           self.regularization, self.factors)

    def explain(self, userid, user_items, itemid, user_weights=None, N=10):
        """ Provides explanations for why the item is liked by the user.

        Parameters
        ---------
        userid : int
            The userid to explain recommendations for
        user_items : csr_matrix
            Sparse matrix containing the liked items for the user
        itemid : int
            The itemid to explain recommendations for
        user_weights : ndarray, optional
            Precomputed Cholesky decomposition of the weighted user liked items.
            Useful for speeding up repeated calls to this function, this value
            is returned
        N : int, optional
            The number of liked items to show the contribution for

        Returns
        -------
        total_score : float
            The total predicted score for this user/item pair
        top_contributions : list
            A list of the top N (itemid, score) contributions for this user/item pair
        user_weights : ndarray
            A factorized representation of the user. Passing this in to
            future 'explain' calls will lead to noticeable speedups
        """
        # user_weights = Cholesky decomposition of Wu^-1
        # from section 5 of the paper CF for Implicit Feedback Datasets
        user_items = user_items.tocsr()
        if user_weights is None:
            A, _ = user_linear_equation(self.item_factors, self.YtY,
                                        user_items, userid,
                                        self.regularization, self.factors)
            user_weights = scipy.linalg.cho_factor(A)
        seed_item = self.item_factors[itemid]

        # weighted_item = y_i^t W_u
        weighted_item = scipy.linalg.cho_solve(user_weights, seed_item)

        total_score = 0.0
        h = []
        h_len = 0
        for itemid, confidence in nonzeros(user_items, userid):
            if confidence < 0:
                continue

            factor = self.item_factors[itemid]
            # s_u^ij = (y_i^t W^u) y_j
            score = weighted_item.dot(factor) * confidence
            total_score += score
            contribution = (score, itemid)
            if h_len < N:
                heapq.heappush(h, contribution)
                h_len += 1
            else:
                heapq.heappushpop(h, contribution)

        items = (heapq.heappop(h) for i in range(len(h)))
        top_contributions = list((i, s) for s, i in items)[::-1]
        return total_score, top_contributions, user_weights

    @property
    def solver(self):
        if self.use_cg:
            solver = _als.least_squares_cg if self.use_native else least_squares_cg
            return functools.partial(solver, cg_steps=self.cg_steps)
        return _als.least_squares if self.use_native else least_squares

    @property
    def YtY(self):
        if self._YtY is None:
            Y = self.item_factors
            self._YtY = Y.T.dot(Y)
        return self._YtY


def alternating_least_squares(Ciu, factors, **kwargs):
    """ factorizes the matrix Cui using an implicit alternating least squares
    algorithm. Note: this method is deprecated, consider moving to the
    AlternatingLeastSquares class instead

    """
    log.warning("This method is deprecated. Please use the AlternatingLeastSquares"
                " class instead")

    model = AlternatingLeastSquares(factors=factors, **kwargs)
    model.fit(Ciu)
    return model.item_factors, model.user_factors


def least_squares(Cui, X, Y, regularization, num_threads=0):
    """ For each user in Cui, calculate factors Xu for them
    using least squares on Y.

    Note: this is at least 10 times slower than the cython version included
    here.
    """
    users, n_factors = X.shape
    YtY = Y.T.dot(Y)

    for u in range(users):
        X[u] = user_factor(Y, YtY, Cui, u, regularization, n_factors)


def user_linear_equation(Y, YtY, Cui, u, regularization, n_factors):
    # Xu = (YtCuY + regularization * I)^-1 (YtCuPu)
    # YtCuY + regularization * I = YtY + regularization * I + Yt(Cu-I)

    # accumulate YtCuY + regularization*I in A
    A = YtY + regularization * np.eye(n_factors)

    # accumulate YtCuPu in b
    b = np.zeros(n_factors)

    for i, confidence in nonzeros(Cui, u):
        factor = Y[i]

        if confidence > 0:
            b += confidence * factor
        else:
            confidence *= -1

        A += (confidence - 1) * np.outer(factor, factor)
    return A, b


def user_factor(Y, YtY, Cui, u, regularization, n_factors):
    # Xu = (YtCuY + regularization * I)^-1 (YtCuPu)
    A, b = user_linear_equation(Y, YtY, Cui, u, regularization, n_factors)
    return np.linalg.solve(A, b)


def least_squares_cg(Cui, X, Y, regularization, num_threads=0, cg_steps=3):
    users, factors = X.shape
    YtY = Y.T.dot(Y) + regularization * np.eye(factors, dtype=Y.dtype)

    for u in range(users):
        # start from previous iteration
        x = X[u]

        # calculate residual error r = (YtCuPu - (YtCuY.dot(Xu)
        r = -YtY.dot(x)
        for i, confidence in nonzeros(Cui, u):
            if confidence > 0:
                r += (confidence - (confidence - 1) * Y[i].dot(x)) * Y[i]
            else:
                confidence *= -1
                r += - (confidence - 1) * Y[i].dot(x) * Y[i]

        p = r.copy()
        rsold = r.dot(r)
        if rsold < 1e-20:
            continue

        for it in range(cg_steps):
            # calculate Ap = YtCuYp - without actually calculating YtCuY
            Ap = YtY.dot(p)
            for i, confidence in nonzeros(Cui, u):
                if confidence < 0:
                    confidence *= -1

                Ap += (confidence - 1) * Y[i].dot(p) * Y[i]

            # standard CG update
            alpha = rsold / p.dot(Ap)
            x += alpha * p
            r -= alpha * Ap
            rsnew = r.dot(r)
            if rsnew < 1e-20:
                break
            p = r + (rsnew / rsold) * p
            rsold = rsnew

        X[u] = x
