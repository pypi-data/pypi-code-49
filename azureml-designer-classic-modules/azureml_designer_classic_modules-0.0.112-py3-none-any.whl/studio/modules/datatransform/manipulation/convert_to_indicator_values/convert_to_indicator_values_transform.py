import pandas as pd

from azureml.studio.common.datatable.data_table import DataTable
from azureml.studio.common.error import ErrorMapping, ColumnNotFoundError
from azureml.studio.core.logger import module_logger
from azureml.studio.modules.datatransform.common.base_transform import BaseTransform


class ConvertToIndicatorValuesTransform(BaseTransform):

    def __init__(self,
                 named_encoder_dict: dict,
                 target_category_col_names: list,
                 overwrite: bool):
        self._named_encoder_dict = named_encoder_dict
        self._target_category_col_names = target_category_col_names
        self._overwrite = overwrite

    def apply(self, table: DataTable):
        ErrorMapping.verify_number_of_columns_greater_than_or_equal_to(
            curr_column_count=len(table.column_names),
            required_column_count=1,
            arg_name=table.name
        )
        # Check if self._target_category_col_names are included in table's column name list
        excluded_column_names = set(self._target_category_col_names) - set(table.column_names)
        for column_name in excluded_column_names:
            raise ColumnNotFoundError(
                column_id=column_name, arg_name_has_column='Transformation', arg_name_missing_column='Dataset')

        target_category_col_indices_set = set()
        for cur_col_name in self._target_category_col_names:
            target_category_col_indices_set.add(table.get_column_index(cur_col_name))
            module_logger.info(f'For categorical column {cur_col_name}, transform to indicator dataframe')
            cur_col_series = table.data_frame[cur_col_name]
            cur_col_is_feature = table.meta_data.column_attributes[cur_col_name].is_feature
            new_cols_df = self.transform_to_indicator_df(cur_col_series, cur_col_name)
            for col_name in new_cols_df:
                # Indicator values will be created as feature field by default. However, if current column is
                # of label field, they should not be either label or feature field based on V1.
                table.add_column(col_name, new_cols_df[col_name], is_feature=cur_col_is_feature)

        if self._overwrite:
            module_logger.info('Overwrite target categorical columns')
            table = table.remove_columns_by_indexes(target_category_col_indices_set)

        return table

    def transform_to_indicator_df(self, series: pd.Series, col_name: str):
        """Transform to indicator values using fit encoder

        :param series: pd.Series
        :param col_name: str
        :return: pd.DataFrame
        """
        cur_named_encoder = self._named_encoder_dict[col_name]
        indicator_matrix = cur_named_encoder.transform(series)
        # Every element in 'categories' list is categories of each feature column, so 0 points to the first feature.
        # As input series is one-column, we can use 0 to extract its categories.
        indicator_df_column_names = [f"{col_name}-{category}" for category in cur_named_encoder.categories[0]]
        indicator_df = pd.DataFrame(indicator_matrix.todense(), columns=indicator_df_column_names)
        return indicator_df
