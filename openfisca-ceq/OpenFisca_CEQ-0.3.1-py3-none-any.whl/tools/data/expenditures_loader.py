import logging
import pandas as pd
import slugify


from openfisca_ceq.tools.data import config_parser, year_by_country
from openfisca_ceq.tools.indirect_taxation.consumption_items_nomenclature import (
    build_label_by_code_coicop,
    )


log = logging.getLogger(__name__)


def build_consumption_items_list(country):
    df = build_label_by_code_coicop(country, additional_variables = ['prod_id'])
    return df.astype({"prod_id": str})


def load_expenditures(country):
    missing_variables_by_country = {
        'mali': [
            'prix',
            'quantite',
            ],
        'senegal': [
            'prix',
            'quantite',
            ],
        }

    expenditures_variables = ['prod_id', 'hh_id', 'depense', 'quantite', 'prix']
    year = year_by_country[country]
    expenditures_data_path = config_parser.get(country, 'consommation_{}'.format(year))
    expenditures = pd.read_stata(expenditures_data_path).astype({"prod_id": str})

    country_expenditures_variables = set(expenditures_variables).difference(
        set(missing_variables_by_country.get(country, []))
        )
    assert country_expenditures_variables <= set(expenditures.columns), "{}: missing variables {}".format(
        country,
        set(expenditures_variables).difference(set(expenditures.columns)),
        )

    # Checks
    consumption_items = build_consumption_items_list(country)
    missing_products_in_legislation = set(expenditures.prod_id.unique()).difference(
        set(consumption_items.prod_id.unique()))
    if missing_products_in_legislation:
        log.info("Missing product in legislation: \n {}".format(
            (
                expenditures
                .reset_index()
                .query("prod_id in @missing_products_in_legislation")
                .filter(items = [
                    'label', 'prod_id'
                    ])
                .drop_duplicates()
                )
            ))
    missing_products_in_expenditures = set(consumption_items.prod_id.unique()).difference(
        set(expenditures.prod_id.unique()))
    if missing_products_in_expenditures:
        log.info("Missing product in legislation: \n {}".format(
            (
                expenditures
                .reset_index()
                .query("prod_id in @missing_products_in_legislation")
                .filter(items = [
                    'label', 'prod_id'
                    ])
                .drop_duplicates()
                )
            ))

    consumption_items.reset_index(inplace = True)
    if missing_products_in_legislation:
        expenditures = expenditures.query("prod_id not in @missing_products_in_legislation").copy()

    consumption_items['poste_coicop'] = (
        "poste_" + consumption_items.deduplicated_code_coicop.apply(
            lambda x: slugify.slugify(x, separator = "_")
            )
        )
    household_expenditures = (expenditures
        .merge(
            consumption_items.reset_index()[['poste_coicop', 'prod_id']],
            on = 'prod_id',
            how = "left"
            )
        )
    household_expenditures = (household_expenditures
        .filter(["hh_id", "poste_coicop", "depense"], axis = 1)
        .pivot(index = "hh_id", columns = "poste_coicop", values = "depense")
        .reset_index()
        )

    irregular_columns = [column for column in household_expenditures.columns if (not str(column).startswith('poste_')) and (column != "hh_id")]
    if irregular_columns:
        log.info("Irregular colums in household expenditures: {}".format(
            irregular_columns))
    return household_expenditures
