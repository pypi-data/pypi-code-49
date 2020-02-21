import pickle
import pandas as pd
import numpy as np
from .multilabel_training import MultilabelTraining
from .metrics import get_binary_classification_metrics
from .dataframe_preprocessing import DataframePreprocessing
from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.multioutput import MultiOutputClassifier
from sklearn.multiclass import OneVsRestClassifier
from sklearn.feature_extraction.text import HashingVectorizer
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier
from IPython.display import clear_output


class BinaryTraining:

    X_COLUMN_NAME = "page_text_extract"
    Y_COLUMN_NAME = "has_theme"

    DEFAULT_TARGET_THEMES = [
        5,
        6,
        26,
        33,
        139,
        163,
        232,
        313,
        339,
        350,
        406,
        409,
        555,
        589,
        597,
        634,
        660,
        695,
        729,
        766,
        773,
        793,
        800,
        810,
        852,
        895,
        951,
        975,
    ]

    OTHER_THEMES_VALUE = 4242

    def __init__(
        self,
        df=pd.DataFrame(),
        x_column_name=X_COLUMN_NAME,
        y_column_name=Y_COLUMN_NAME,
        group_processes=True,
        classifier=XGBClassifier(max_depth=15, random_state=42, n_jobs=-1),
        vectorizer=HashingVectorizer(n_features=2 ** 14),
        target_themes=DEFAULT_TARGET_THEMES,
        other_themes_value=OTHER_THEMES_VALUE,
        remove_processes_without_theme=True,
        is_incremental_training=False,
        vocab_path="",
    ):
        self.is_incremental_training = is_incremental_training
        self.vocab_path = vocab_path
        self.remove_processes_without_theme = remove_processes_without_theme
        self.classifier = classifier
        self.vectorizer = vectorizer
        self.target_themes = target_themes
        self.other_themes_value = other_themes_value
        self.group_processes = group_processes
        self.x_column_name = x_column_name
        self.y_column_name = y_column_name
        self._initialize_dataframe(df)
        self._separate_themes_no_themes(self.df)

    def _initialize_dataframe(self, df):
       if not df.empty:
           self.dp = DataframePreprocessing(
               df.copy(),
               group_processes=self.group_processes,
               x_column_name=self.x_column_name,
               target_themes=self.target_themes,
               other_themes_value=self.other_themes_value,
               is_incremental_training=self.is_incremental_training,
               remove_processes_without_theme=self.remove_processes_without_theme,
               vocab_path=self.vocab_path,
           )
           self.y_columns_names = self.dp.distinct_themes
           self.df = self.dp.processed_df
       else:
           self.df = df

    def _split(self, X, y):
        print("Splitting dataset...")
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            X, y, stratify=y, test_size=0.2, random_state=42
        )

    def _vectorize(self, X_train):
        print("Vectorizing...")
        return self.vectorizer.fit_transform(X_train)

    def _binarize_classification(self, series):
        if (self.other_themes_value in series or 0 in series) and len(series) == 1:
            return 0
        return 1

    def _separate_themes_no_themes(self, df):
        mt = MultilabelTraining(
            df,
            group_processes=self.group_processes,
            is_incremental_training=self.is_incremental_training,
            target_themes=self.target_themes,
            remove_processes_without_theme=self.remove_processes_without_theme,
        )

        df[self.y_column_name] = mt.df.labels_with_others.progress_apply(
            self._binarize_classification
        )

    def train(self, split_df=False):
        print("Training...")
        self.X_train, self.y_train = (
            self.df[self.x_column_name],
            self.df[self.y_column_name],
        )
        if split_df:
            self._split(self.X_train, self.y_train)
        vector = self._vectorize(self.X_train)
        self.classifier.fit(vector, self.y_train)
        if split_df:
            vector_test = self._vectorize(self.X_test)
            self.y_pred = self.classifier.predict(vector_test)
            metrics = get_binary_classification_metrics(self.y_test, self.y_pred)
            return metrics
        return None

    def _update_dataframe(
        self, df, is_incremental_training=True, is_parquet=False, labels_freq={}
    ):
        self.dp = DataframePreprocessing(
            df.copy(),
            x_column_name=self.x_column_name,
            group_processes=self.group_processes,
            target_themes=self.target_themes,
            other_themes_value=self.other_themes_value,
            is_incremental_training=is_incremental_training,
            remove_processes_without_theme=self.remove_processes_without_theme,
            is_parquet=is_parquet,
            vocab_path=self.vocab_path,
            labels_freq=labels_freq,
        )
        self.df = self.dp.processed_df

    # def incremental_train(self, df_path, nrows=5000):
    #    print("Training incrementally...")
    #    columns_names = pd.read_csv(df_path, nrows=1).columns.tolist()
    #    skiprows = 1
    #    classes, labels_freq = DataframePreprocessing(
    #        target_themes=self.target_themes
    #    ).get_unique_binarized_labels(df_path, "tema")
    #    while True:
    #        df = pd.read_csv(
    #            df_path,
    #            nrows=nrows,
    #            skiprows=skiprows,
    #            header=None,
    #            names=columns_names,
    #        )
    #        if df.empty:
    #            break
    #        self._update_dataframe(df, labels_freq=labels_freq)
    #        X_train, y_train = (
    #            self.df[self.x_column_name],
    #            self.df[self.target_themes + [self.other_themes_value]],
    #        )
    #        vector = self._vectorize(X_train)
    #        self.mo_classifier.partial_fit(vector, y_train, classes=classes)
    #        skiprows += nrows
    #        print("{} rows already trained\n".format(skiprows - 1))

    # def incremental_train_with_parquet(self, parquet_path):
    #    print("Training incrementally with parquet...")
    #    nrows = 0
    #    pf = ParquetFile(parquet_path)
    #    classes, labels_freq = DataframePreprocessing(
    #        target_themes=self.target_themes
    #    ).get_unique_binarized_labels(parquet_path, "tema", True)
    #    for df in pf.iter_row_groups():
    #        df = df.reset_index()
    #        self._update_dataframe(df, is_parquet=True, labels_freq=labels_freq)
    #        X_train, y_train = (
    #            self.df[self.x_column_name],
    #            self.df[self.target_themes + [self.other_themes_value]],
    #        )
    #        vector = self._vectorize(X_train)
    #        self.mo_classifier.partial_fit(vector.toarray(), y_train, classes=classes)
    #        nrows += len(self.df)
    #        print("{} rows already trained\n".format(nrows))
    #        clear_output(wait=True)

    def predict(self):
        return self.classifier.predict(self._vectorize(self.X_test).todense())

    def set_X_test(self, X):
        self.X_test = X

    def set_y_test(self, y):
        self.y_test = y

    def get_pickle(self):
        return pickle.dumps(self.mo_classifier)
