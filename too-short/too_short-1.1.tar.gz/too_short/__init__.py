import numpy as np
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder, LabelEncoder, StandardScaler
from sklearn.linear_model import LogisticRegression, SGDClassifier, LinearRegression, SGDRegressor, Ridge, ElasticNet, Lasso
from sklearn import svm
from sklearn.model_selection import train_test_split, GridSearchCV, RandomizedSearchCV
from sklearn.compose import ColumnTransformer
from sklearn.datasets import load_boston, load_iris, load_wine
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC, SVR, LinearSVC
from sklearn.ensemble import RandomForestClassifier
from imblearn.over_sampling import SMOTE
from imblearn.pipeline import Pipeline
from imblearn.under_sampling import RandomUnderSampler
from sklearn.feature_selection import SelectFromModel


class TooShort:
    """
    This is a package intended to make your life easier, and automate a lot of the common things dealt with in supervised learning. Specifically with building and testing sklearn models. Although, it also relies on some other useful tools like SMOTE for imabalanced data.

    In short:

    - Chooses relevant models for you based on the type of problem (classification or regression)
    - Provides param grids for the chosen models
    - Wraps all the preprocessing into one function so you can do somewhat customized preprocessing with a oneliner
    - Wraps Oversampling and undersampling using the imbalanced learn package to simplify the process
    - Feature selection based on a model input
    - Automatically splitting train and test sets, as well as evaluting them seperately.
    - Most importantly, provides a simple method to search and compare all the relevant models and grids with either your original data, or the transformed version set in the preprocessing, oversampling, or feature selection step.
        """

    def __init__(self, X=None, y=None, prediction_type=None):
        """ init function

        Keyword args:
        X: pd.dataframe - Df with full X data (will be split within init) - optional (you will need to include this for most functionality)
        y: list - list of targets (will be split within init) - optional  (you will need to include this for most functionality)
        prediction_type: string - String of either "classification" or "regression" - optional  (you will need to include this for most functionality)

        Returns:
        None
        """
        self.X = X
        self.y = y
        self.prediction_type = prediction_type
        self.imb_pipeline_steps = []
        if (X is not None and y is not None):
            X_train, X_test, y_train, y_test = train_test_split(
                X, y, test_size=0.33, random_state=42)
            self.X_train = X_train
            self.X_test = X_test
            self.y_train = y_train
            self.y_test = y_test

    def set_attributes(self, X=None, y=None, X_test=None, y_test=None, X_train=None, y_train=None, prediction_type=None, imb_pipeline_steps=None, models=None):
        """Function for setting class attributes manually. 
        Useful for overriding defaults if you are trying to test different settings

        Keyword args:
        X: Pd dataframe containing X - optional
        y: target list - optional
        X_test: pd dataframe - optional
        y_test: pd dataframe - optional
        X_train: pd dataframe - optional
        y_train: pd dataframe - optional
        prediction_type: string - Either "classification" or "regression" - optional
        imb_pipline_steps: list - Containing imbalanced learn Pipeline steps. ex [('smote', SMOTE(random_state=random_state))]. If you want to use this within the search method
        dont add a sklearn model step to the end of this, that will be done automatically in the the search function. - optional
        models: list - List of models to be used in in the search function. This would be set automatically in choose_models function, but you can override here. Do not instantiate the models within the list. - optional

        Returns:
        None
        """
        if (X is not None):
            self.X = X
        if (y is not None):
            self.y = y
        if (X_test is not None):
            self.X_test = X_test
        if (y_test is not None):
            self.y_test = y_test
        if (X_train is not None):
            self.X_train = X_train
        if (y_train is not None):
            self.y_train = y_train
        if (prediction_type is not None):
            self.prediction_type = prediction_type
        if (imb_pipeline_steps is not None):
            self.imb_pipeline_steps = imb_pipeline_steps
        if (models is not None):
            self.models = models

    def get_param_grid(self, model, prepend=None):
        """Function providing a hyperparam grid to be used in sklearn hyperparameter optimizatoin.
        This is automatically called internally in the search function, the user need not call this directly.

        Keyword arguments:
        model: sklearns model.__name__  property - Required
        prepend: string to be prepended to grid keys for grid search along with to underscores. this will generally be the model name as a string. ie "LogisticRegression" - optional

        Returns:
        Dictionary containing sklearn params as keys and list of param options as values

        Example:
        get_param_grid(LinearRegression)
        >>{'normalize': [True, False]}
        """
        name = model.__name__
        if (name == "LogisticRegression"):
            penalty = ['l1', 'l2']
            C = [0.0001, 0.001, 0.01, 0.1, 1, 10, 100, 1000]
            class_weight = [{1: 0.5, 0: 0.5}, {1: 0.4, 0: 0.6},
                            {1: 0.6, 0: 0.4}, {1: 0.7, 0: 0.3}]
            solver = ['liblinear', 'saga']

            output = dict(penalty=penalty,
                          C=C,
                          class_weight=class_weight,
                          solver=solver)
        elif (name == "SGDClassifier"):
            loss = ['hinge', 'log', 'modified_huber',
                    'squared_hinge', 'perceptron']
            penalty = ['l1', 'l2', 'elasticnet']
            alpha = [0.0001, 0.001, 0.01, 0.1, 1, 10, 100, 1000]
            learning_rate = ['constant', 'optimal', 'invscaling', 'adaptive']
            class_weight = [{1: 0.5, 0: 0.5}, {1: 0.4, 0: 0.6},
                            {1: 0.6, 0: 0.4}, {1: 0.7, 0: 0.3}]
            eta0 = [1, 10, 100]

            output = dict(loss=loss,
                          penalty=penalty,
                          alpha=alpha,
                          learning_rate=learning_rate,
                          class_weight=class_weight,
                          eta0=eta0)
        elif (name == "RandomForestClassifier"):
            n_estimators = [int(x)
                            for x in np.linspace(start=200, stop=2000, num=10)]
            max_features = ['auto', 'sqrt']
            max_depth = [int(x) for x in np.linspace(10, 110, num=10)]
            max_depth.append(None)
            min_samples_split = [2, 5, 10]
            min_samples_leaf = [1, 2, 4]
            bootstrap = [True, False]
            output = dict(n_estimators=n_estimators,
                          max_features=max_features,
                          max_depth=max_depth,
                          min_samples_split=min_samples_split,
                          min_samples_leaf=min_samples_leaf,
                          bootstrap=bootstrap)
        elif (name == "LinearRegression"):
            normalize = [True, False]
            output = dict(
                normalize=normalize
            )
        elif (name == "KNeighborsClassifier"):
            leaf_size = list(range(1, 50))
            n_neighbors = list(range(1, 30))
            p = [1, 2]
            output = dict(leaf_size=leaf_size, n_neighbors=n_neighbors, p=p)
        elif (name == "SVC"):
            Cs = [0.001, 0.01, 0.1, 1, 10]
            gammas = [0.001, 0.01, 0.1, 1]
            output = dict(C=Cs,
                          gamma=gammas,
                          # TODO - add kernels?
                          kernel=['rbf']
                          )
        elif (name == "SVR"):
            kernel = ['linear']
            Cs = [0.001, 0.01, 0.1, 1, 10]
            gammas = [0.001, 0.01, 0.1, 1]
            epsilon = [0.1, 0.2, 0.5, 0.3]
            output = dict(kernel=kernel,
                          C=Cs,
                          gamma=gammas,
                          epsilon=epsilon)
        elif (name == "SGDRegressor"):
            alpha = [1e-4, 1e-3, 1e-2, 1e-1, 1e0, 1e1, 1e2, 1e3]
            loss = ['squared_loss', 'huber', 'epsilon_insensitive',
                    'squared_epsilon_insensitive']
            penalty = ['l1', 'l2']
            epsilon = [0.1, 0.2, 0.5, 0.3]
            output = dict(alpha=alpha,
                          loss=loss,
                          pentalty=penalty,
                          epsilon=epsilon
                          )
        elif (name == "KMeans"):
            n_clusters = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
            output = dict(
                n_clusters=n_clusters
            )
        elif (name == "AdaBoostClassifier"):
            base_estimator__criterion = ["gini", "entropy"]
            base_estimator__splitter = ["best", "random"]
            output = dict(
                base_estimator__criterion=base_estimator__criterion,
                base_estimator__splitter=base_estimator__splitter
            )
        elif (name == "GradientBoostingClassifier"):
            max_depth = range(5, 16, 2)
            min_samples_split = range(200, 1001, 200)
            output = dict(
                max_depth=max_depth,
                min_samples_split=min_samples_split
            )
        elif (name == "Ridge"):
            alpha = [0.0001, 0.001, 0.01, 0.1, 1, 10, 100, 1000]
            output = dict(
                alpha=alpha
            )
        elif (name == "ElasticNet"):
            alpha = [0.0001, 0.001, 0.01, 0.1, 1, 10, 100, 1000]
            l1_ratio = np.arange(0.0, 1.0, 0.1)
            output = dict(
                alpha=alpha,
                l1_ratio=l1_ratio
            )
        elif (name == "Lasso"):
            alpha = [0.02, 0.024, 0.025, 0.026, 0.03]
            output = dict(
                alpha=alpha
            )
        elif (name == "BayesianGaussianMixture"):
            covariance_type = ['full', 'tied', 'diag', 'spherical']
            weight_concentration_prior_type = ['dirichlet_process',
                                               'dirichlet_distribution']
            output = dict(
                covariance_type=covariance_type,
                weight_concentration_prior_type=weight_concentration_prior_type
            )
        elif (name == "LinearSVC"):
            dual = [True, False]
            C = [0.0001, 0.001, 0.01, 0.1, 1, 10, 100, 1000]
            output = dict(
                dual=dual,
                C=C
            )
        else:
            raise Exception("Model not supported.")
        # prepend every key with step name to be used if pipeline if specified
        if (prepend is not None):
            keys = list(output.keys())
            prepended_output = {}
            for i in range(len(keys)):
                prepended_key = f"{prepend}__{keys[i]}"
                prepended_output[prepended_key] = output[keys[i]]
            return prepended_output
        return output

    def preproc(self, OHE=[], standard_scale=[], numerical_impute=[], categegorical_impute=[], label_encode={}):
        """Prerocesses data frames, including onehot encoding, scaling, and imputation, and label encoding
        Keyord arguments:
        OHE: Array of columns to be processed with sklearn OneHotEncoder, this accepts non numerical categorical rows without need for label encoding. - Default []
        standard_scale: list. List of columns to be processes with standard scalar. - Defualt []
        numerical_impute: list. list of column names that should be imputed using mean method. - Default []
        categorical_impute: list. list of column names that should be imputed to 'missing'. - Default []
        label_encode: dict. Keys in the dict should be the column names to transform, the values should be lists that
        contain the various values in the column, the order of the values will determine the encoding (1st element will be 0 etc.). - Default {}
        Returns:
        List of processed pandas dataframes. Processed dfs will overwrite self.X_train and self.X_test.
        """
        transformer = ColumnTransformer(
            transformers=[
                ('cat_imputer',
                 SimpleImputer(strategy='constant', fill_value='missing'),
                 categegorical_impute
                 ),
                ('num_imputer',
                 SimpleImputer(strategy='median'),
                 numerical_impute
                 ),
                ("one_hot",
                 OneHotEncoder(),
                 OHE
                 ),
                ("standard_scalar",
                 StandardScaler(),
                 standard_scale
                 )
            ],
            remainder='passthrough'  # donot apply anything to the remaining columns
        )
        column_names = self.X_train.columns
        # fit transformation to the train X set
        transformer.fit(self.X_train)
        # fetch newly created ohe transformed columns
        if (len(OHE) > 0):
            ohe_columns = transformer.named_transformers_.one_hot.get_feature_names(
                OHE)
        else:
            ohe_columns = []
        # get rid of original OHE columns
        column_names = list(filter(lambda x: x not in OHE, column_names))
        # reset column names with newly created ohe column names
        column_names = np.append(ohe_columns, column_names)
        self.X_train = pd.DataFrame(data=transformer.transform(
            self.X_train), columns=column_names)
        # transform test and validation sets if they are included
        if (self.X_test is not None):
            self.X_test = pd.DataFrame(data=transformer.transform(
                self.X_test), columns=column_names)
        # label encoding tranformation
        le_columns = label_encode.keys()
        for column in le_columns:
            le = LabelEncoder()
            le.fit(label_encode[column])
            self.X_train[column] = le.transform(self.X_train[column])
            if (self.X_test is not None):
                self.X_test[column] = le.transform(self.X_test[column])
        return self.X_train, self.X_test

    def choose_models(self):
        """Function giving you suggested sklearn models based on prediction type and size of data. classification_type must be 
        set during the class instantiation or using set_attributes.

        Keyword arguments: 
        None

        Returns:
        List of sklearn model classes. Models saved to class instance under self.models, they will be automatically passed to 
        the search method.
        """
        n_samples = len(self.y_train)
        if (self.prediction_type == "regression"):
            if (n_samples > 100000):
                self.models = [
                    LinearRegression,
                    SGDRegressor,
                    SVR,
                    Ridge,
                    ElasticNet,
                    Lasso
                ]
                return self.models
            # SGD regressor needs more than 100k samples
            else:
                self.models = [
                    LinearRegression,
                    SVR,
                    Ridge,
                    ElasticNet,
                    Lasso
                ]
                return self.models
        if (self.prediction_type == "classification"):
            if (n_samples > 100000):
                self.models = [
                    SVC,
                    RandomForestClassifier,
                    KNeighborsClassifier,
                    SGDClassifier,
                    LinearSVC,
                    LogisticRegression
                ]
                return self.models
            else:
                self.models = [
                    SVC,
                    RandomForestClassifier,
                    KNeighborsClassifier,
                    LinearSVC,
                    LogisticRegression
                ]
                return self.models
        raise Exception("prediction_type must be classification or regression")

    def oversample(self):
        """Function tranforming train data using undersampling and oversampling. Uses undersampling as well as oversampling if the
        ratio between classes is highly imbalanced. Otherwise only oversampling will be used

        Keyword args:
        None

        Returns:
        os_X_train, os_y_train. As matrices (as returned by SMOTE). os_X_train and os_y_train are saved to class and will be automatically 
        applied during the search method, if oversample method is run first.
        """
        unique, counts = np.unique(self.y_train, return_counts=True)
        count_dict = dict(zip(unique, counts))
        y_keys, y_counts = count_dict.keys(), count_dict.values()
        sorted_counts = sorted(y_counts, reverse=True)
        highest = sorted_counts[0]
        second_highest = sorted_counts[1]
        ratio = highest / second_highest
        # under sample then oversample
        if (ratio > 4):
            under = RandomUnderSampler(sampling_strategy=0.5)
            over = SMOTE()
            pipeline_steps = [('under_sample', under), ('over_sample', over)]
            pipeline = Pipeline(steps=pipeline_steps)
            os_X, os_y = pipeline.fit_resample(self.X_train, self.y_train)
        else:
            over = SMOTE()
            pipeline_steps = [('over_sample', over)]
            pipeline = Pipeline(steps=pipeline_steps)
            os_X, os_y = pipeline.fit_resample(self.X_train, self.y_train)
        self.imb_pipeline_steps = pipeline_steps
        # osx is returned if you choose to use it yourself, however pipeline will be used in grid search automatically
        # https://stackoverflow.com/questions/50245684/using-smote-with-gridsearchcv-in-scikit-learn
        return os_X, os_y

    def select_features(self, model=None):
        """Select best features from X_test and X_train

        Keyword args:
        model: sklearn model - The model that will be used in sklearns SelectFromModel method Needs to 
        be instantiated - Default is LinearRegression if prediction_type is "regression", otherwise if prediction_type is "classification" defaults to LinearSVC() 

        Returns:
        limited_X_train, limited_X_test - Also replaces self.X_test and self.X_train with the limited features.
        """
        if (self.prediction_type == "regression"):
            if (model is None):
                model = LinearRegression()
            selector = SelectFromModel(
                estimator=model).fit(self.X_train, self.y_train)
            selected_X_train = pd.DataFrame(
                data=selector.transform(self.X_train))
            selected_X_test = pd.DataFrame(
                data=selector.transform(self.X_test))
            support = selector.get_support()
        if (self.prediction_type == "classification"):
            if (model is None):
                model = LinearSVC()
            selector = SelectFromModel(
                estimator=model).fit(self.X_train, self.y_train)
            selected_X_train = pd.DataFrame(
                data=selector.transform(self.X_train))
            selected_X_test = pd.DataFrame(
                data=selector.transform(self.X_test))
            support = selector.get_support()

        # restore column names
        if (isinstance(self.X_train, pd.DataFrame) and len(self.X_train.columns) == len(support)):
            filtered_columns = []
            for i in range(len(support)):
                if (support[i] == True):
                    filtered_columns.append(self.X_train.columns[i])
            selected_X_train.columns = filtered_columns
        if (isinstance(self.X_test, pd.DataFrame) and len(self.X_test.columns) == len(support)):
            filtered_columns = []
            for i in range(len(support)):
                if (support[i] == True):
                    filtered_columns.append(self.X_test.columns[i])
            selected_X_test.columns = filtered_columns
        self.X_train = selected_X_train
        self.X_test = selected_X_test
        return selected_X_train, selected_X_test

    def search(self, scoring=None):
        """
        Function performing a grid search on a list of predefined models

        Args:
        Scoring: string - scoring param as allowed by grid search cv - optional

        Returns:
        Dict containing each model, and within each model a sub dict containing the best grid search cv scores, best params, and test score.
        """
        results = {}
        for model in self.models:
            param_grid = self.get_param_grid(model, prepend=model.__name__)
            total_params = sum(map(lambda x: len(x), param_grid.keys()))
            # allowing for smote sampling if it exists
            # https://stackoverflow.com/questions/50245684/using-smote-with-gridsearchcv-in-scikit-learn
            if (len(self.imb_pipeline_steps) > 0):
                steps = self.imb_pipeline_steps.copy()
                steps.append((model.__name__, model()))
                model_or_pipeline = Pipeline(steps=steps)
            else:
                model_or_pipeline = Pipeline(steps=[(model.__name__, model())])
            # perform random search if number of params is high
            if (total_params > 35):
                search = RandomizedSearchCV(
                    model_or_pipeline, param_grid, n_jobs=-1, scoring=scoring)
            else:
                search = GridSearchCV(model_or_pipeline, param_grid,
                                      n_jobs=-1, scoring=scoring)
            search.fit(self.X_train, self.y_train)
            test_score = 'N/A'
            if (self.X_test is not None):
                test_score = search.score(self.X_test, self.y_test)
            # remove prepended peice from param grid - KNeighborsClassifier_n_neighbors becomes n_neighbors
            search_params_keys = list(search.best_params_.keys()).copy()
            for key in search_params_keys:
                prepended_string = f"{model.__name__}__"
                is_prepended = False if key.find(
                    prepended_string) == -1 else True
                if (is_prepended == True):
                    values = search.best_params_[key]
                    stripped_key = key.replace(prepended_string, '')
                    del search.best_params_[key]
                    search.best_params_[stripped_key] = values
            results[model.__name__] = {
                'best_search_score': search.best_score_,
                'best_params': search.best_params_,
                'test_score': test_score
            }
        self.results = results
        return self.results
