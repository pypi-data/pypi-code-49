import configparser
import logging
import os
import pandas as pd
import pkg_resources


from openfisca_survey_manager.coicop import build_raw_coicop_nomenclature
from openfisca_survey_manager import default_config_files_directory as config_files_directory


log = logging.getLogger(__name__)


assets_directory = os.path.join(
    pkg_resources.get_distribution('openfisca-ceq').location,
    'openfisca_ceq',
    'assets'
    )

config_parser = configparser.ConfigParser()
config_parser.read(os.path.join(config_files_directory, 'raw_data.ini'))
consumption_items_directory = config_parser.get('ceq', 'consumption_items_directory')
assert os.path.exists(consumption_items_directory), \
    "Consumption items directory {} does not exists, please create it and fill it with countries consumption items files"


country_code_by_country = {
    "mali": "MLI",
    "senegal": "SEN",
    "cote_d_ivoire": "CIV",
    }


def build_label_by_code_coicop(country, additional_variables = None, new_code_coicop_variable = "nouveau__code"):
    consumption_items_file_path = os.path.join(
        consumption_items_directory, "Produits_{}.xlsx".format(country_code_by_country[country])
        )
    if additional_variables is None:
        additional_variables = []
    consumption_items = pd.read_excel(consumption_items_file_path)
    if new_code_coicop_variable is not None:
        consumption_items = (consumption_items
            .drop(columns = ["code_coicop"])
            .rename(
                columns = {'nouveau_code_coicop': 'code_coicop'}
                )
            )
    label_by_code_coicop = (consumption_items
        .rename(
            columns = {
                'label': 'label_variable',
                'nom_variable_format_wide': 'variable_name'
                }
            )
        .filter(['label_variable', 'code_coicop', 'variable_name'] + additional_variables)
        .dropna()
        .astype(str)
        .sort_values('code_coicop')
        )
    label_by_code_coicop['code_coicop'] = label_by_code_coicop.code_coicop.str.strip("0")
    duplicated_coicop = label_by_code_coicop.loc[label_by_code_coicop.code_coicop.duplicated()]
    label_by_code_coicop['deduplicated_code_coicop'] = label_by_code_coicop.code_coicop.copy()
    for code_coicop in duplicated_coicop.code_coicop.unique():
        n = sum(label_by_code_coicop.code_coicop == code_coicop)
        enhanced_code_coicops = [code_coicop + '_item_' + str(i + 1) for i in range(n)]
        label_by_code_coicop.loc[label_by_code_coicop.code_coicop == code_coicop, 'deduplicated_code_coicop'] = enhanced_code_coicops

    assert not label_by_code_coicop.deduplicated_code_coicop.duplicated().any()
    label_by_code_coicop = (label_by_code_coicop
        .set_index('deduplicated_code_coicop')
        )
    return label_by_code_coicop


def build_complete_label_coicop_data_frame(country, file_path = None, deduplicate = True):
    label_by_code_coicop = build_label_by_code_coicop(country)
    raw_coicop_nomenclature = build_raw_coicop_nomenclature()
    completed_label_coicop = (label_by_code_coicop
        .reset_index()
        .merge(raw_coicop_nomenclature, on = 'code_coicop', how = 'left')
        .filter(items = [
            'label_division',
            'label_groupe',
            'label_classe',
            'label_sous_classe',
            'label_poste',
            'label_variable',
            'code_coicop',
            'deduplicated_code_coicop',
            ])
        )

    if deduplicate:
        completed_label_coicop = (completed_label_coicop
            .drop('code_coicop', axis = 1)
            .rename(columns = {'deduplicated_code_coicop': "code_coicop"})
            )

    if file_path:
        completed_label_coicop.to_csv(file_path)
    return completed_label_coicop


def build_comparison_table(countries):
    dfs = [
        build_complete_label_coicop_data_frame(country, deduplicate = False)
        for country in countries
        ]

    index = [
        'label_division',
        'label_groupe',
        'label_classe',
        'label_sous_classe',
        'label_poste',
        'code_coicop'
        ]

    dfs = [
        df.groupby(index)['label_variable'].unique()
        for df in dfs
        ]

    merged = pd.concat(dfs, axis = 1, keys = country_code_by_country.values(), join = 'outer', copy = False).reset_index()
    merged['division_index'] = merged.code_coicop.str.split('.', 1).str[0].astype(int)
    merged = (merged.sort_values(['division_index', 'code_coicop']).drop('division_index', axis = 1))
    merged.to_csv(os.path.join(assets_directory, 'merged.csv'))
    merged.to_excel(os.path.join(assets_directory, 'merged.xls'))

    return merged


def build_tax_rate_by_code_coicop(country, tax_variables = None):
    assert tax_variables is not None
    label_by_code_coicop = (build_label_by_code_coicop(country, additional_variables = tax_variables)
        .drop(columns = "code_coicop")
        .reset_index()
        .rename(columns = {'deduplicated_code_coicop': "code_coicop"})
        )
    assert "code_coicop" in label_by_code_coicop.columns
    return label_by_code_coicop


def build_comparison_spreadsheet(countries, coicop_level = 3):
    dfs = [
        build_complete_label_coicop_data_frame(country, deduplicate = False)
        for country in countries
        ]
    coicops = [set(df.code_coicop.unique()) for df in dfs]
    unique_coicops = sorted(list(set().union(*coicops)))
    summary = (
        pd.concat(
            [
                (
                    coicop_df[['label_variable', 'deduplicated_code_coicop', 'code_coicop']]
                    .groupby('code_coicop')
                    .count()
                    )
                for coicop_df in dfs
                ],
            axis = 1,
            keys = country_code_by_country.values(),
            join = 'outer',
            copy = False,
            sort = True,
            )
        .fillna(0)
        )
    writer = pd.ExcelWriter(
        os.path.join(assets_directory, 'merged_by_coicop_{}.xlsx'.format(coicop_level)),
        engine = 'xlsxwriter'
        )
    summary.to_excel(
        writer,
        sheet_name = str("summary"),
        )

    # Build index
    index_variables = [
        'label_division',
        'label_groupe',
        'label_classe',
        'label_sous_classe',
        'label_poste',
        'code_coicop',
        ]

    def build_levels_list(coicop_list, level):
        complete_coicop_digits = [
            complete_coicop.split('.')
            for complete_coicop in coicop_list
            ]
        levels_set = set([
            ".".join(["{}"] * coicop_level).format(*coicop_digits[0:coicop_level])
            for coicop_digits in complete_coicop_digits
            if len(coicop_digits) >= level
            ])
        return sorted(list(levels_set))

    index = (pd.concat(
        [df[index_variables].copy() for df in dfs]
        )
        .drop_duplicates()
        )

    levelled_index = build_levels_list(index.code_coicop.to_list(), coicop_level)
    levelled_unique_coicops = build_levels_list(unique_coicops, coicop_level)
    for coicop_base in levelled_unique_coicops:
        # coicop = "1.1.2.3.1"
        coicop_dfs = [
            df.loc[
                df.code_coicop.str.startswith(coicop_base),
                ['label_variable', 'deduplicated_code_coicop', 'code_coicop']
                ].set_index(['code_coicop', 'deduplicated_code_coicop'])
            for df in dfs
            ]
        merged = pd.concat(
            coicop_dfs,
            axis = 1,
            keys = country_code_by_country.values(),
            join = 'outer',
            copy = False,
            sort = True,
            )
        merged.columns = merged.columns.droplevel(1)
        merged = merged.assign(coicop_base = coicop_base)

        if coicop_base not in levelled_index:
            log.info("{} not in admisisble coicops".format(coicop_base))
            log.info(merged)
            log.info("----")
            continue
        merged = (merged
            .reset_index()
            .merge(
                index,
                how = 'inner',
                on = "code_coicop",
                )
            .set_index([
                'coicop_base',
                'code_coicop',
                'label_division',
                'label_groupe',
                'label_classe',
                'label_sous_classe',
                'label_poste',
                'deduplicated_code_coicop',
                ])
            )
        try:
            if merged.empty:
                continue
            merged.to_excel(
                writer,
                sheet_name = str(coicop_base),
                )
        except Exception as e:
            log.info(e)
            pass
    writer.save()
    writer.close()


def test():
    tax_variables_by_country = {
        "senegal": ['tva']
        }
    country = "senegal"
    tax_variables = tax_variables_by_country.get(country, [])
    df = build_tax_rate_by_code_coicop(country, tax_variables)
    for tax_variable in tax_variables:
        log.info(tax_variable + "\n" + str(df[tax_variable].value_counts()))

    countries = ['cote_d_ivoire', 'senegal', 'mali']
    merged = build_comparison_table(countries)
    log.info(merged)


if __name__ == '__main__':
    test()
    import sys
    logging.basicConfig(level = logging.INFO, stream = sys.stdout)
    countries = ['cote_d_ivoire', 'senegal', 'mali']
    for coicop_level in range(3, 6):
        build_comparison_spreadsheet(countries, coicop_level = coicop_level)
