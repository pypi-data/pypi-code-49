import pickle

import lightgbm as lgb
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.metrics import classification_report
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split

df = pd.read_csv('../data/train_test.csv')
df.drop(columns=['dt'], axis=1, inplace=True)
df = df[df['label'] >= 0]
delete_columns = ['label']
X = df.drop(columns=delete_columns, axis=1)
y = df[['label']].values.ravel()


def param_cv(X, y):
    params_grid = {'max_depth': range(3, 8, 1), 'num_leaves': range(40, 200, 5)}

    gsearch = GridSearchCV(
        estimator=lgb.LGBMClassifier(boosting_type='gbdt', objective='binary', metrics='auc', learning_rate=0.1,
                                     n_estimators=50, max_depth=6, num_leaves=44),
        param_grid=params_grid, scoring='roc_auc', cv=3, n_jobs=-1)
    gsearch.fit(X, y)
    print(gsearch.scorer_, gsearch.best_params_, gsearch.best_score_)


def train(X, y):
    # 训练
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    # 创建成lgb特征的数据集格式,将使加载更快
    max_depth = 7
    gbm = lgb.LGBMClassifier(objective='binary', n_estimators=50, max_depth=max_depth, num_leaves=80,
                             early_stopping_rounds=10,
                             metrics='auc', min_data_in_leaf=60,
                             reg_alpha=0.1, reg_lambda=0.1)
    gbm.fit(X_train, y_train, eval_set=[(X_test, y_test)])

    pickle.dump(gbm, open('../lgbmodel/2019-11.lgb', 'wb'))

    predict_train = gbm.predict(X_train)
    predict_train_proba = gbm.predict_proba(X_train)

    predict_test = gbm.predict(X_test)
    predict_test_proba = gbm.predict_proba(X_test)
    from sklearn.metrics import roc_auc_score
    print('train:', roc_auc_score(y_train, predict_train_proba[:, 1]))
    print('train:', classification_report(y_train, predict_train))

    print('test:', roc_auc_score(y_test, predict_test_proba[:, 1]))
    print('test:', classification_report(y_test, predict_test))

    print(gbm.evals_result_)

    ax = lgb.plot_metric(gbm.evals_result_, metric='auc')  # metric的值与之前的params里面的值对应
    plt.title('metric')
    # plt.show()

    feature_names_pd = pd.DataFrame({'column': X.columns,
                                     'importance': gbm.feature_importances_,
                                     })
    # plt.figure(figsize=(10, 15))
    sns.barplot(x="importance", y="column",
                data=feature_names_pd.sort_values(by="importance", ascending=False))  # 按照importance的进行降排序
    plt.title('LightGBM Features')
    plt.tight_layout()
    # plt.show()


if __name__ == '__main__':
    # param_cv(X, y)
    train(X, y)
