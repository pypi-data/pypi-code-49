from demyst.analytics.report import report

import matplotlib.pyplot as plt
from io import BytesIO
import pdfkit
import pandas as pd
import numpy as np
import os
import shutil
from matplotlib import font_manager
from matplotlib import rcParams

def quality_report(analytics, df):
    # Need this so it finds custom fonts
    font_manager._rebuild()
    # Set default font
    rcParams['font.family'] = 'Roboto Mono'
    rcParams['font.weight'] = 'medium'
    rcParams['text.color'] = '#424242'
    rcParams['axes.labelcolor'] = '#424242'
    rcParams['xtick.color'] = '#424242'
    rcParams['ytick.color'] = '#424242'

    here_dir = os.path.dirname(os.path.realpath(__file__))
    rep = report(df)
    try:
        os.mkdir("report")
    except Exception:
        pass
    product_stats_drawing(df, rep)
    data_stats_drawing(analytics, df, rep)
    most_filled_attributes_drawing(df, rep)
    least_filled_attributes_drawing(df, rep)
    generate_html(analytics, df, rep)
    copy_files(here_dir)
    pdfkit.from_file("report/index.html", "report/report.pdf", {'--header-html':'report/header.html', '--footer-html':'report/footer.html'})

def product_stats_drawing(df, rep):
    data = extract_data_for_match_rate_plot_from_report(rep)

    products = data["product_name"].tolist()
    match = data["product_match_rate"].to_numpy()
    no_match = (100.0 - data["product_match_rate"] - data["product_error_rate"]).to_numpy()
    error = data["product_error_rate"].to_numpy()
    ind = [x for x, _ in enumerate(products)]

    plt.barh(ind, match, label='Match', color='#b39ddb')
    plt.barh(ind, no_match, label='No Match', color='#29b6f6', left=match)
    plt.barh(ind, error, label='Error', color='#1de9B6', left=match+no_match)

    plt.yticks(ind, products)
    plt.xlabel("Percentage of Inputs")
    plt.gca().legend(loc='upper center', bbox_to_anchor=(0.5, -0.2), fancybox=True, shadow=True, ncol=5)
    plt.title("Product Match Rate")

    return save_figure("product_stats")

def save_figure(filename):
    plt.savefig("report/" + filename + ".svg", format='svg', bbox_inches='tight', pad_inches=0.05)
    plt.close()

def extract_data_for_match_rate_plot_from_report(rep):
    return rep[["product_name", "product_match_rate", "product_error_rate"]].drop_duplicates().sort_values(by=['product_match_rate']).reset_index(drop=True)

def data_stats(analytics, df, rep):
    outputs = analytics.product_outputs(provider_names_from_report(rep))
    indexname = rep[(rep["attribute_name"] == "error") |
            (rep["attribute_name"] == "client_id") |
           (rep["attribute_name"] == "row_id")].index
    rep = rep.drop(indexname)

    temp = pd.DataFrame({'attribute' : list(rep['attribute_name'])})
    temp['attribute'] = temp['attribute'].replace(r"\[(\w+)\]", '[]', regex=True)
    data_types = pd.merge(temp, outputs, on="attribute", how="left")
    numerical = len(list(data_types[data_types['type'] == 'Number']['type']))
    datetime = len(list(data_types[data_types['type'] == 'DateTime']['type']))
    bools = len(list(data_types[data_types['type'] == 'Boolean']['type']))
    st = data_types[data_types['type'] == 'String']
    categorical = len(st) - len(st[st['attribute'].str.contains('description')])
    desc = len(data_types) - numerical - datetime - bools - categorical
    return (['Numerical', 'Categorical Text', 'Descriptive Text', 'DateTime', 'Boolean'], [numerical, categorical, desc, datetime, bools])

def data_stats_drawing(analytics, df, rep):
    types, values = data_stats(analytics, df, rep)
    patches, texts = plt.pie(values, colors=["#b39ddb", "#1de9B6", "#2e3951", "#00acc1", "#7283a7", "#1de9b6"])
    plt.legend(patches, types, loc="lower left", fancybox=True, shadow=True)
    return save_figure("data_stats")

def generate_html(analytics, df, rep):
    rep = rep.drop(columns=["attribute_type", "variance", "median"], axis=1)
    text_file = open("report/index.html", "w+")
    text_file.write("<head>\n")
    text_file.write("<link rel='stylesheet' href='style.css'>\n")
    text_file.write("</head>\n")
    text_file.write("<body id='Body'>\n")
    text_file.write("<table id='MainContent'>\n")
    text_file.write("<tr><td colspan='2'><div><h1>Data Quality Report</h1></td><tr>\n")
    text_file.write("<tr><td colspan='2'><div><h2>Product Stats</h2></div></td></tr>\n")
    text_file.write("<tr><td colspan='2' class='ProductStats'><div>")
    text_file.write(generate_product_stats(df, rep))
    text_file.write("</div></td></tr>\n")
    text_file.write("<tr><td colspan='2'><div><h2>Data Types</h2></div></td></tr>\n")
    text_file.write("<tr><td colspan='2'><div>")
    text_file.write(generate_data_stats(analytics, df, rep))
    text_file.write("</div></td></tr>")
    text_file.write("</table>\n")
    text_file.write("<table style='page-break-before: always'>\n")
    text_file.write("<tr><td colspan='2'><div><h2>Attribute Stats</h2></div></td></tr>\n")
    text_file.write("<tr><td colspan='2'><div><h3>Top Attributes by Fill Rate</h3></div></td></tr>\n")
    text_file.write("<tr class='Table_full'><td colspan='2'><div><img src='most_filled.svg'></div><td><tr>\n")
    text_file.write("<tr><td colspan='2'><div><h3>Least Filled Attributes</h3></div></td></tr>\n")
    text_file.write("<tr class='Table_full'><td colspan='2'><div><img src='least_filled.svg'></div><td><tr>\n")
    text_file.write("<tr><td colspan='2'><div><h3>Complete List of Attributes</h3></div></td></tr>\n")
    text_file.write("<tr><td>")
    text_file.write(generate_complete_list_of_attributes(df, rep))
    text_file.write("</td></tr>\n")
    text_file.write("</table>")
    text_file.write("\n")
    text_file.write("</body>\n")
    text_file.close()

def copy_files(here_dir):
    shutil.copy(here_dir + "/files/style.css", "report/style.css")
    shutil.copy(here_dir + "/files/header.html", "report/header.html")
    shutil.copy(here_dir + "/files/footer.html", "report/footer.html")
    shutil.copy(here_dir + "/files/demyst_logo_gray.svg", "report/demyst_logo_gray.svg")

def provider_names_from_report(rep):
    return rep[["product_name"]].drop_duplicates()["product_name"].tolist()

def generate_product_stats(df, rep):
    s = ""
    s += "<table>\n"
    s += "<tr><td class='Table__left'><ul>\n"
    for product in provider_names_from_report(rep):
        s += "<li><span>" + product + "<span></li>\n"
    s += "</ul></td><td class='Table__right'>\n"
    s += "<img src='product_stats.svg' id='ProductStatsDiagram'>\n"
    s += "</td></tr>\n"
    s += "</table>"
    return s

def generate_data_stats(analytics, df, rep):
    types, values = data_stats(analytics, df, rep)
    s = ""
    s += "<table class='ProductStats'>\n"
    s += "<tr><td class='Table__left'><ul>\n"
    for type in types:
        s += "<li><span>" + type + "</span></li>\n"
    s += "</ul></td><td class='Table__right'>\n"
    s += "<img src='data_stats.svg'>\n"
    s += "</td></tr>\n"
    s += "</table>"
    return s

def filter_report(rep):
    rep = rep[~rep['attribute_name'].isin(['client_id', 'row_id', 'error', 'is_hit'])]
    col = ['attribute_name', 'attribute_fill_rate']
    rep = rep[col].sort_values(by='attribute_fill_rate', ascending=False, na_position='last')
    return rep

def most_filled_attributes_drawing(df, rep):
    rep = filter_report(rep)
    n = int(len(rep['attribute_name'])/2) if len(rep['attribute_name']) <= 40 else 20
    objects = list(rep['attribute_name'][:n])
    y_pos = np.arange(len(objects))
    performance = list(rep['attribute_fill_rate'][:n])
    plt.barh(y_pos, performance, align='center', alpha=0.5)
    plt.yticks(y_pos, objects)
    plt.xlabel('Fill Rate')
    plt.title('Top Attributes by Fill Rate')
    return save_figure("most_filled")

def least_filled_attributes_drawing(df, rep):
    rep = filter_report(rep)
    n = int(len(rep['attribute_name'])/2) if len(rep['attribute_name']) <= 40 else 20
    objects = list(rep['attribute_name'][-n:])
    y_pos = np.arange(len(objects))
    performance = list(rep['attribute_fill_rate'][-n:])
    plt.barh(y_pos, performance, align='center', alpha=0.5)
    plt.yticks(y_pos, objects)
    plt.xlabel('Fill Rate')
    # If all values are zero, diagram gets weird X ticks:
    # https://github.com/DemystData/demyst-python/issues/614
    # Fix this by manually setting to no ticks.
    if all(v == 0 for v in performance):
        plt.xticks(list(), list())
    plt.title('Least Filled Attributes')
    return save_figure("least_filled")

def generate_complete_list_of_attributes(df, rep):
    s = "<ol>\n"
    for index, row in rep.iterrows():
        s += "<li><strong>" + row["attribute_name"] + "</strong>\n"
        s += "<ul class='Table__sans'><li>Blank Values - " + str(100 - row["attribute_fill_rate"]) + "</li>\n"
        s += "<li>Non-Blank Values - " + str(row["attribute_fill_rate"]) + "</li>\n"
        s += "<li>Unique Values - " + str(row["unique_values"]) + "</li>\n"
        s += "<li>Most Common Values - " + str(row["most_common_values"]) + "</li></br>\n"
        s += "</ul>\n"
    return s + "</ol>"
