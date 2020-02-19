import pandas as pd
import numpy as np
import re
import json

from IPython.display import display, Markdown, HTML

# Treat empty strings as NaN
pd.options.mode.use_inf_as_na = True

def attribute_construct(in_data, out_data):
    df = pd.DataFrame({
        'column': np.setdiff1d(out_data.columns.values, in_data.columns.values)
    })

    # split product_name and attribute
    re_product_name = [re.search('^([^\\.]*)\\.(.*)$', a) for a in df.column]
    df['product_name'] = [r.group(1) for r in re_product_name]
    df['attribute_name'] = [r.group(2) for r in re_product_name]

    # Find how nested the attribute is
    re_nested = [re.findall('\\[(\d+)\\]', a) for a in df.attribute_name]
    df['nested_level'] = [(np.array(r).astype(int)+1).prod() for r in re_nested]

    # Strip out the nesting from the attribute
    df['attribute_name'] = [re.sub('\\[\d+\\]', '[*]', a) for a in df.attribute_name]

    return df

def attribute_collapse(attributes):
    max_nested = (
        attributes.groupby(['product_name', 'attribute_name'])[['nested_level']].max().
        reset_index().rename(columns={'nested_level':'max_nested'})
    )
    level_1 = attributes.query('nested_level == 1').drop(columns='nested_level').rename(columns={'column': 'column_0'})
    df_collapsed = pd.merge(max_nested, level_1, how='left', on=['product_name', 'attribute_name'])

    return df_collapsed

def product_name_cost(attributes, analytics):
    c = attributes[['product_name']].drop_duplicates()
    c['cost'] = [analytics.C.provider_cost(c) if c!="inputs" else 0 for c in c.product_name]
    return pd.merge(attributes, c, how='left', on='product_name')

def attribute_drop_non_error(attributes):
    df = attributes.drop(attributes[attributes["attribute_name"] != "error"].index)
    return df

def attribute_drop_error(attributes):
    #must drop client_id and row_id which are always filled
    indexname = attributes[(attributes["attribute_name"] == "error") |
                (attributes["attribute_name"] == "client_id") |
               (attributes["attribute_name"] == "row_id")].index
    df = attributes.drop(indexname)
    return df

def any_match(attributes, data, column_name):
    data = data[attributes['column_0']].replace(r'^\s*$', np.nan, regex=True)
    stacked = (
        data.notna()[attributes.column_0].stack().reset_index().
        rename(columns={'level_0': 'row', 'level_1': 'column_0', 0: 'not_na'})
    )
    stacked = pd.merge(stacked, attributes[['product_name', 'column_0']], how='left', on='column_0')
    stacked = stacked.groupby(['product_name', 'row'])['not_na'].any().reset_index()
    any_match = stacked.groupby('product_name')['not_na'].sum().astype(int).reset_index().rename(columns={'not_na': column_name})
    return any_match

def match(attributes, data, column_name):

    match = pd.DataFrame(columns=['product_name', column_name])
    for prod in list(attributes['product_name'].drop_duplicates()):
        #is_hit column more accurate for finding match rate but not all providers have this added
        if prod + ".is_hit" in list(data.columns):
            match = match.append({'product_name': prod, 'product_name_match' : data[prod + ".is_hit"].values.sum()}, ignore_index=True)
        else:
            cols = [c for c in data.columns if c.startswith(prod)]
            prod_attributes = attributes.drop(attributes[~(attributes["product_name"] == prod)].index)
            match = match.append(any_match(prod_attributes, data[cols], column_name))
    return match

def product_name_matched(attributes, data):
    attributes = pd.merge(attributes, match(attribute_drop_error(attributes), data, 'product_name_match'), how='left', on='product_name')
    attributes = pd.merge(attributes, any_match(attribute_drop_non_error(attributes), data, 'product_name_error'), how='left', on='product_name')
    return attributes

def attribute_types(attributes, data):
    types = (
        data[attributes['column_0']].dtypes.reset_index().
        rename(columns={'index': 'column_0', 0:'attribute_type'})
    )
    return pd.merge(attributes, types, how='left', on='column_0')

def attribute_fill(attributes, data) :
    fill = (
        data[attributes['column_0']].replace(r'^\s*$', np.nan, regex=True).count().reset_index().
        rename(columns={'index': 'column_0', 0:'attribute_fill'})
    )

    # Error columns are not attributes, so clear them.  Treating error
    # columns as attributes causes paradoxical results, like 200% fill
    # rate, because the fill rate is computed based on the match rate,
    # which goes to zero as the number of errors increases.
    # https://github.com/DemystData/demyst-python/issues/604
    fill.loc[(fill["column_0"].str.endswith(".error"))] = 0.0

    return pd.merge(attributes, fill, how='left', on='column_0')

def unique_values(attributes, data) :
    unique = (
        data[attributes['column_0']].replace(r'^\s*$', np.nan, regex=True).nunique().reset_index().
        rename(columns={'index': 'column_0', 0:'unique_values'})
    )
    return pd.merge(attributes, unique, how='left', on='column_0')

def most_common_values(attributes, data) :
    def calc_mcv(row):
        return json.dumps(data[row["column_0"]].value_counts().head(5).to_dict())
    attributes["most_common_values"] = attributes.apply(calc_mcv, axis=1)
    return attributes

def cardinality(attributes, data) :
    def calc_card(row):
        cleaned_row = data[row["column_0"]].replace(r'^\s*$', np.nan, regex=True)
        ct = cleaned_row.count()
        if ct == 0:
            return 0
        else:
            card = cleaned_row.nunique() / cleaned_row.count() * 100.00
            return custom_round(card)
    attributes["cardinality"] = attributes.apply(calc_card, axis=1)
    return attributes

def standard_method(attributes, data, method_name, attr_name):
    values = (
        getattr(data[attributes['column_0']], method_name)(numeric_only=True).reset_index().
        rename(columns={'index': 'column_0', 0: attr_name})
    )
    return pd.merge(attributes, values, how='left', on='column_0')

def custom_round(num):
    return round(num, 2)

def attribute_cleanup(attributes, data):
    clean = (
        attributes.assign(
            product_match_rate=(attributes.product_name_match.astype(float) / len(data) * 100.0).apply(custom_round),
            product_error_rate=(attributes.product_name_error.astype(float) / len(data) * 100.0).apply(custom_round),
            attribute_fill_rate=(attributes.attribute_fill.astype(float) / attributes.product_name_match * 100.0).apply(custom_round),
            nunique=attributes.unique_values
        )[['product_name', 'product_match_rate', 'product_error_rate', 'attribute_name', 'attribute_fill_rate', 'attribute_type', 'unique_values', 'most_common_values', 'cardinality', 'std', 'median', 'mean', 'max_value', 'min_value', 'variance']]
    )
    clean['attribute_fill_rate'] = clean['attribute_fill_rate'].fillna(0.0)
    # Assume objects are strings
    return clean

def filter_columns(attributes, columns):
    re_product_name = [re.search('^([^\\.]*)\\.(.*)$', a) for a in columns]
    rows = []
    for regex in re_product_name:
        product_name = regex.group(1)
        attribute_name = regex.group(2)
        row = attributes.loc[(attributes['product_name'] == product_name) & (attributes['attribute_name'] == attribute_name)]
        rows.append(row)
    return pd.concat(rows).reset_index()

def report(enriched, columns=[]):
    input_cols = [c for c in enriched.columns if c.startswith("inputs.")]
    # Make sure every output column contains a dot, i.e. is of the form "provider.column".
    # Ignore columns without a dot.
    # https://github.com/DemystData/demyst-python/issues/555
    output_cols = [c for c in enriched.columns if (not c.startswith("inputs.")) and ("." in c)]
    inputs = enriched[input_cols]
    enriched = enriched[output_cols]
    attributes = attribute_construct(inputs, enriched)
    attributes = attribute_collapse(attributes)
    attributes = product_name_matched(attributes, enriched)
    attributes = attribute_types(attributes, enriched)
    attributes = attribute_fill(attributes, enriched)
    attributes = unique_values(attributes, enriched)
    attributes = most_common_values(attributes, enriched)
    attributes = cardinality(attributes, enriched)
    attributes = standard_method(attributes, enriched, "std", "std")
    attributes = standard_method(attributes, enriched, "median", "median")
    attributes = standard_method(attributes, enriched, "mean", "mean")
    attributes = standard_method(attributes, enriched, "max", "max_value")
    attributes = standard_method(attributes, enriched, "min", "min_value")
    attributes = standard_method(attributes, enriched, "var", "variance")
    attributes = attribute_cleanup(attributes, enriched)

    if len(columns) > 0:
        attributes = filter_columns(attributes, columns)

    return attributes
