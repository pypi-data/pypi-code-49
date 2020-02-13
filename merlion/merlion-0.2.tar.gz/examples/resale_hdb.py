import re
import pickle
import logging
import pandas as pd
import numpy as np
import lightgbm as lgb
from bayes_opt import BayesianOptimization
from sklearn.model_selection import KFold
from sklearn.metrics import mean_squared_error
from merlion import Merlion

logger = logging.getLogger('hdb_resale')
handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)

def feature_engineering(df):
    resale = df.copy()
    resale['block'] = pd.to_numeric(resale['block'].apply(lambda x: re.findall('\d+', x)[0]))
    resale['transaction_year'] = resale['transaction_date'].dt.year
    resale['transaction_month'] = resale['transaction_date'].dt.month
    resale['lease_commence_year'] = resale['lease_commence_date'].dt.year
    resale['lease_commence_month'] = resale['lease_commence_date'].dt.month
    resale['lower_storey_range'] = resale['storey_range'].apply(lambda x: int(x.split()[0]))
    resale['upper_storey_range'] = resale['storey_range'].apply(lambda x: int(x.split()[2]))
    resale['latitude'] = resale['latlong'].apply(lambda x: float(x.split(",")[0]))
    resale['longitude'] = resale['latlong'].apply(lambda x: float(x.split(",")[1]))
    factors = ['town', 'flat_type', 'block', 'floor_area_sqm', 'flat_model', 'remaining_lease', 'resale_price', 'transaction_date', 'transaction_year', 
           'transaction_month', 'lease_commence_year', 'lease_commence_month', 'lower_storey_range', 'upper_storey_range', 'latitude', 'longitude']
    resale_df = resale[factors].copy()
    return resale_df

def generate_train_test(df, cutoff_date):
    resale_df = df.copy()
    train_data = resale_df[resale_df['transaction_date'] <= cutoff_date].copy()
    test_data = resale_df[resale_df['transaction_date'] > cutoff_date].copy()
    train_data.drop('transaction_date', axis=1, inplace=True)
    test_data.drop('transaction_date', axis=1, inplace=True)
    print(train_data.shape)
    print(test_data.shape)
    X_train = train_data.drop('resale_price', axis=1)
    y_train = train_data['resale_price']
    X_test = test_data.drop('resale_price', axis=1)
    y_test = test_data['resale_price']
    return X_train, y_train, X_test, y_test

if __name__ == "__main__":
    logger.info('Starting Model Building and Optimization Script')
    cutoff_date = '2017-06-30'
    resale = pd.read_csv('https://s3.amazonaws.com/public-sparkbeyond/PublicDatasets/Singapore+HDB+Demo/resale_processed.csv.gz', compression='gzip', parse_dates=['lease_commence_date', 'transaction_date'])
    resale_enriched = feature_engineering(resale)
    X_train, y_train, X_test, y_test = generate_train_test(resale_enriched, cutoff_date)

    default_params = {'learning_rate': 0.15, 'metric': 'rmse', 'verbose':-1}
    n_folds = 5
    random_seed = 0
    early_stopping_rounds = 100
    num_boost_round = 100000

    feature_space = {
        'num_leaves': (10, 2000),
        'min_data_in_leaf': (10, 500),
        'colsample_bytree': (0.4, 0.99),
        'reg_lambda': (0, 10),
        'max_depth': (2, 64),
        'subsample': (0.4, 1.0),
        'feature_fraction': (0.7, 0.95)
        }

    hdb_merlion = Merlion(default_params, feature_space, early_stopping_rounds, num_boost_round, n_folds, random_seed, 'rmse')

    X_train = hdb_merlion.fit_transform(X_train)
    init_points = 20
    n_iter = 10
    hdb_merlion.maximize(X_train, y_train, init_points=init_points, n_iter=n_iter, acq='poi', xi=1e-4)

    hdb_merlion.train_single_model(X_train, y_train)
    X_test = hdb_merlion.transform(X_test)
    test_rmse = hdb_merlion.validate_single_model(X_test, y_test, 'rmse')
    logger.info(f'Single Model Performance: {test_rmse}')

    hdb_merlion.train_ensemble_models(X_train, y_train, 5, 5)
    test_rmse = hdb_merlion.validate_ensemble_models(X_test, y_test, 'rmse')
    logger.info(f'Ensemble Model Performance: {test_rmse}')

    #lgbmbayes.generate_shap_values(X_train)
    # with open('hdb_lgbmbayes_single.pkl', 'wb') as output_file:
    #     pickle.dump(lgbmbayes.single_model, output_file)

    # with open('hdb_lgbmbayes_multiple.pkl', 'wb') as output_file:
    #     pickle.dump(lgbmbayes.ensemble_models, output_file)