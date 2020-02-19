import logging
import pandas as pd
import os
import slugify


from openfisca_ceq.tools.indirect_taxation.consumption_items_nomenclature import assets_directory


log = logging.getLogger(__name__)


def build_unit_cost_by_category_by_country():
    df = pd.read_csv(
        os.path.join(
            assets_directory,
            "unit_cost_of_education_public_service_by_country.csv"
            )
        )
    df.columns = [slugify.slugify(column, separator = "_") for column in df.columns]
    df['country'] = df.country.apply(
        lambda x: slugify.slugify(x, separator = "_")
        )
    df['harmonized_category'] = df.harmonized_category.apply(
        lambda x: slugify.slugify(x, separator = "_")
        )
    unit_cost_by_category_by_country = dict()
    for country in df['country'].unique():
        country_df = df.query("country == @country")
        unit_cost_by_category = dict(zip(
            country_df.harmonized_category,
            country_df.unit_cost_thousands_fcfa * 1000
            ))

        deleted_variables = ['total']
        for deleted_variable in deleted_variables:
            if deleted_variable in unit_cost_by_category:
                del unit_cost_by_category[deleted_variable]

        if 'secondary_and_higher_education' in unit_cost_by_category:
            unit_cost_by_category['secondary'] = unit_cost_by_category['higher'] = unit_cost_by_category['secondary_and_higher_education']
            del unit_cost_by_category['secondary_and_higher_education']

        if 'basic_education' in unit_cost_by_category:
            unit_cost_by_category['primary'] = unit_cost_by_category.pop('basic_education')

        unit_cost_by_category_by_country[country] = unit_cost_by_category

        harmonized_key_by_variable_name = {
            'pre_school': "preschool",
            'primary_education': "primary",
            'secondary_education': "secondary",
            'tertiary_education': "higher",
            }

        for variable_name, harmonized_key in harmonized_key_by_variable_name.items():
            if harmonized_key in unit_cost_by_category:
                unit_cost_by_category[variable_name] = unit_cost_by_category.pop(harmonized_key)

    return unit_cost_by_category_by_country
