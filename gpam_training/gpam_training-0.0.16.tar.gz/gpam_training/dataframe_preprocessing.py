from sklearn.preprocessing import MultiLabelBinarizer
import numpy as np
import pandas as pd
import pickle
from tqdm import tqdm

tqdm.pandas()


class DataframePreprocessing:

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
        group_processes=True,
        x_column_name="page_text_extract",
        y_column_name="tema",
        target_themes=DEFAULT_TARGET_THEMES,
        other_themes_value=OTHER_THEMES_VALUE,
        is_incremental_training=False,
        remove_processes_without_theme=True,
        is_parquet=False,
        labels_freq={},
        vocab_path="",
    ):
        self.is_incremental_training = is_incremental_training
        self.remove_processes_without_theme = remove_processes_without_theme
        self.is_parquet = is_parquet
        self.x_column_name = x_column_name
        self.y_column_name = y_column_name
        self.other_themes_value = other_themes_value
        self.target_themes = target_themes
        self.group_processes = group_processes
        self.vocab_path = vocab_path

        self.distinct_themes = target_themes + [other_themes_value]
        if not df.empty:

            if remove_processes_without_theme:
                df = df[
                    df[self.y_column_name].progress_apply(
                        self._remove_processes_without_theme
                    )
                ].copy()
                df[self.y_column_name] = (
                    df[self.y_column_name]
                    .progress_apply(self._remove_with_without_theme_mixture)
                    .copy()
                )

            self._generate_themes_column(df.copy())

            self.target_themes.sort()
            self.labels_freq = {}
            self.df[self.y_column_name] = self.df[self.y_column_name].apply(
                self._remove_with_without_theme_mixture
            )

            if not labels_freq:
                self._set_labels_frequency()
            else:
                self.labels_freq = labels_freq
            self.processed_df = self._process_dataframe()

    def _remove_processes_without_theme(self, series):
        if 0 in series and len(series) == 1:
            return False
        return True

    def _remove_with_without_theme_mixture(self, series):
        if 0 in series and len(series) > 1:
            return np.array([v for v in series if v != 0])
        return series

    def _generate_themes_column(self, df):
        if self.group_processes:
            self._group_samples_by_process(df)
        else:
            if not self.is_parquet:
                self.df = df
                # self.df[self.y_column_name] = self.df[self.y_column_name].apply(lambda x: np.array(x))
                # self._transform_array_column(df)
            else:
                self.df = df
                self.df[self.y_column_name] = self.df[self.y_column_name].apply(
                    lambda x: np.array(x)
                )

    def _transform_array_column(self, df):
        print("Tranforming themes strings to arrays...")
        df[self.y_column_name] = df[self.y_column_name].apply(
            lambda l: np.fromstring(l[1:-1], sep=" ")
        )
        self.df = df

    def _group_samples_by_process(self, df):
        print("Grouping processes...")
        self.df = df.groupby("process_id").apply(self._aggregate)

    def _aggregate(self, series):
        reduced = {}
        series[self.x_column_name].drop_duplicates(inplace=True)

        reduced[self.x_column_name] = " ".join(
            str(x) for x in series[self.x_column_name].values
        )
        temas = np.unique(series[self.y_column_name].values)
        reduced[self.y_column_name] = temas[~np.isnan(temas)]
        return pd.Series(reduced, index=[self.x_column_name, *[self.y_column_name]])

    def _remove_rare_samples(self, series, threshold=1):
        if self.labels_freq.get(tuple(series.tolist())) < threshold:
            return False
        return True

    def _switch_other_themes_values(self, actual_label):
        """
            Replace the values of themes that are not in target themes
            to a unique value
        """

        modified_label = set()
        for theme in actual_label:
            if theme not in self.target_themes:
                modified_label.add(self.other_themes_value)
            else:
                modified_label.add(theme)
        return sorted(modified_label)

    def _normalize_labels(self, series):
        return np.asarray(self._switch_other_themes_values(series.tolist()))

    def _set_labels_frequency(self):
        print("Setting labels frequency...")
        for label in self.df[self.y_column_name]:
            normalized_label = tuple(self._switch_other_themes_values(label))

            if not self.labels_freq.get(normalized_label):
                self.labels_freq[normalized_label] = 1
            else:
                self.labels_freq[normalized_label] += 1

    def get_labels_frequency(self, series):
        print("Setting labels frequency...")
        labels_freq = {}
        for label in series:
            normalized_label = tuple(self._switch_other_themes_values(label))

            if not labels_freq.get(normalized_label):
                labels_freq[normalized_label] = 1
            else:
                labels_freq[normalized_label] += 1
        return labels_freq

    def _get_distinct_themes(self):
        if self.is_incremental_training:
            self.distinct_themes = self.target_themes + [self.other_themes_value]
        else:
            distinct_themes = set()
            for label in self.df["labels_with_others"]:
                for theme in label:
                    distinct_themes.add(theme)
            self.distinct_themes = list(sorted(distinct_themes))

    # TODO: Include case when themes are not grouped
    def get_unique_binarized_labels(self, df_path, y_column_name, is_parquet=False):
        print("Generating set of binarized labels...")
        if not is_parquet:
            themes = pd.read_csv(df_path, usecols=[y_column_name])
            themes[y_column_name] = themes[y_column_name].apply(
                lambda l: np.fromstring(l[1:-1], sep=" ")
            )
        else:
            themes = pd.read_parquet(df_path, columns=[y_column_name])
            themes[self.y_column_name] = themes[self.y_column_name].apply(
                lambda x: np.array(x)
            )
            themes[self.y_column_name] = themes[self.y_column_name].apply(
                self._remove_with_without_theme_mixture
            )

        if self.remove_processes_without_theme:
            themes = themes[
                themes[self.y_column_name].progress_apply(
                    self._remove_processes_without_theme
                )
            ]

        labels_freq = self.get_labels_frequency(themes[self.y_column_name])

        themes["labels_with_others"] = themes[y_column_name].apply(
            self._normalize_labels
        )

        mlb = MultiLabelBinarizer()
        binarized_columns = mlb.fit_transform(themes["labels_with_others"].to_numpy())
        unique_labels = []

        for bin_label in binarized_columns:
            if bin_label.tolist() not in unique_labels:
                unique_labels.append(bin_label.tolist())
        return unique_labels, labels_freq

    def _binarize_labels(self):
        print("Binarizing labels...")
        self._get_distinct_themes()

        mlb = MultiLabelBinarizer(classes=self.distinct_themes)
        binarized_columns = mlb.fit_transform(self.df["labels_with_others"].to_numpy())

        columns_names = {
            ix: binarized_columns[:, i] for i, ix in enumerate(self.distinct_themes)
        }

        return pd.concat(
            [self.df.reset_index(drop=True), pd.DataFrame(columns_names)], axis=1,
        )

    def _clean_text(self, text, vocab):
        text = text.split()
        text = [x for x in text if x in vocab]
        text = " ".join(text)
        return text

    def _select_vocab(self, vocab_path):
        vocab = pickle.load(open(vocab_path, "rb"))
        self.df[self.x_column_name] = self.df[self.x_column_name].progress_apply(
            self._clean_text, vocab=vocab
        )

    def _process_dataframe(self):
        self.df = self.df[~pd.isnull(self.df[self.x_column_name])]

        if self.remove_processes_without_theme:
            self.df = self.df[
                self.df[self.y_column_name].progress_apply(
                    self._remove_processes_without_theme
                )
            ]

        if self.vocab_path:
            self._select_vocab(self.vocab_path)

        self.df["labels_with_others"] = self.df[self.y_column_name].apply(
            self._normalize_labels
        )
        print("Removing rare samples...")

        self.df = self.df[
            self.df["labels_with_others"].apply(self._remove_rare_samples)
        ]
        return self._binarize_labels()
