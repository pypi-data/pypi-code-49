import logging
import pandas as pd


from openfisca_ceq.tools.data import config_parser, year_by_country


from openfisca_ceq.tools.data_ceq_correspondence import (
    ceq_input_by_harmonized_variable,
    ceq_intermediate_by_harmonized_variable,
    data_by_model_weight_variable,
    model_by_data_id_variable,
    model_by_data_role_index_variable,
    non_ceq_input_by_harmonized_variable,
    variables_by_entity,
    )


log = logging.getLogger(__name__)


missing_revenus_by_country = {
    'cote_d_ivoire': [
        'rev_i_independants',
        ],
    'mali': [
        'rev_i_independants_taxe',
        'rev_i_independants_Ntaxe',
        'rev_i_locatifs',
        'rev_i_autres_revenus_capital',
        'rev_i_pensions',
        'rev_i_transferts_publics',
        ],
    'senegal': [
        'rev_i_independants',
        ],
    }


def build_income_dataframes(country):
    year = year_by_country[country]
    income_data_path = config_parser.get(country, 'revenus_harmonises_{}'.format(year))
    model_variable_by_person_variable = dict()
    variables = [
        ceq_input_by_harmonized_variable,
        ceq_intermediate_by_harmonized_variable,
        model_by_data_id_variable,
        non_ceq_input_by_harmonized_variable,
        ]
    for item in variables:
        model_variable_by_person_variable.update(item)

    income = pd.read_stata(income_data_path)

    for variable in income.columns:
        if variable.startswith("rev"):
            assert income[variable].notnull().any(), "{} income variable for {} is all null".format(
                variable, country)

    assert (
        set(model_variable_by_person_variable.keys()).difference(
            set(missing_revenus_by_country.get(country, []))
            )
        <= set(income.columns)
        ), \
        "Missing {} in {} income data source".format(
            set(model_variable_by_person_variable.keys()).difference(
                set(missing_revenus_by_country.get(country, []))
                ).difference(set(income.columns)),
            country,
            )

    data_by_model_id_variable = {v: k for k, v in model_by_data_id_variable.items()}
    data_by_model_role_index_variable = {v: k for k, v in model_by_data_role_index_variable.items()}

    dataframe_by_entity = dict()
    for entity, variables in variables_by_entity.items():
        data_entity_id = data_by_model_id_variable["{}_id".format(entity)]
        data_entity_weight = data_by_model_weight_variable["person_weight"]

        filtered_variables = list(
            set(variables).difference(
                set(missing_revenus_by_country.get(country, [])))
            )

        data_group_entity_ids = list()
        data_group_entity_role_index = list()
        if entity == 'person':
            for group_entity in variables_by_entity.keys():
                if group_entity == 'person':
                    continue

                data_group_entity_ids += [data_by_model_id_variable["{}_id".format(group_entity)]]
                data_group_entity_role_index += [data_by_model_role_index_variable["{}_role_index".format(group_entity)]]

        dataframe = income[
            filtered_variables
            + [
                data_entity_id,
                data_entity_weight,
                ]
            + data_group_entity_ids
            + data_group_entity_role_index
            ].copy()

        if entity != 'person':
            dataframe = dataframe.groupby(data_by_model_id_variable["{}_id".format(group_entity)]).sum().reset_index()

        dataframe_by_entity[entity] = dataframe

    log.info("For country {}: {} persons and {} households".format(
        country, len(dataframe_by_entity["person"]), len(dataframe_by_entity["household"])
        ))
    assert len(dataframe_by_entity["person"]) == dataframe_by_entity["person"].pers_id.nunique()
    assert len(dataframe_by_entity["household"]) == dataframe_by_entity["person"].hh_id.nunique()

    return dataframe_by_entity["person"], dataframe_by_entity["household"]


if __name__ == "__main__":
    # for country in year_by_country.keys():
    import sys
    logging.basicConfig(level = logging.INFO, stream = sys.stdout)
    country = "cote_d_ivoire"
    person_dataframe, household_dataframe = build_income_dataframes(country)
