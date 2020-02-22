from skopt import BayesSearchCV as BayesSearchCVOld


class BayesSearchCV(BayesSearchCVOld):
    """
    Temporary fix for BayesSearchCV. There was compatibility issues between scikit-optimize and scikit-learn 0.2.
    Unfortunately, scikit-optimize is no longer actively maintained and looking for takeover.

    More robust fix should come soon, and this fix should be deprecated.

    Issues to follow:
        - https://github.com/scikit-optimize/scikit-optimize/pull/777
    """
    def __init__(self, estimator, search_spaces, optimizer_kwargs=None, n_iter=50, scoring=None, fit_params=None,
                 n_jobs=1, n_points=1, iid=True, refit=True, cv=None, verbose=0, pre_dispatch='2*n_jobs',
                 random_state=None, error_score='raise', return_train_score=False):

        self.fit_params = fit_params

        self.search_spaces = search_spaces
        self.n_iter = n_iter
        self.n_points = n_points
        self.random_state = random_state
        self.optimizer_kwargs = optimizer_kwargs
        self._check_search_space(self.search_spaces)

        super(BayesSearchCVOld, self).__init__(
                estimator=estimator, scoring=scoring, n_jobs=n_jobs, iid=iid,
                refit=refit, cv=cv, verbose=verbose, pre_dispatch=pre_dispatch,
                error_score=error_score, return_train_score=return_train_score)

    def _run_search(self, x):
        raise BaseException('Scikit-learn 0.2+ incompatibility')
