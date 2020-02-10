from flask import Blueprint, request, jsonify
import pandas as pd

from .db import get_db_connection

##__________________________________________________________________||
bp = Blueprint('query', __name__)

##__________________________________________________________________||
def init_app(app):
    app.register_blueprint(bp)

##__________________________________________________________________||
@bp.route('/maps')
def maps():
    """returns the content of the table maps in JSON
    """

    query_ = "SELECT * FROM maps"
    return query_to_table_json(query_)

##__________________________________________________________________||
@bp.route('/paths', methods=['GET', 'POST'])
def paths():
    query_ = "SELECT * FROM map_path"
    if request.method == 'POST':
        map_id = request.form['map_id']
        query_ = query_ + " WHERE map_id={}".format(map_id)
    return query_to_table_json(query_)

##__________________________________________________________________||
def query_to_dataframe(query):
    conn = get_db_connection()
    rows = conn.execute(query)
    df = pd.DataFrame(rows, columns=rows.keys())
    return df

##__________________________________________________________________||
def query_to_table_html(query):
    df = query_to_dataframe(query)
    html = df.to_html()
    return html

##__________________________________________________________________||
def query_to_table_json(query):
    df = query_to_dataframe(query)

    json = df.to_json(orient='table', index=False)
    # Note: the orient 'table' option is described in
    # https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_json.html
    # e.g.,
    # >>> df = pd.DataFrame(dict(A=[10, 20], B=["abc", "def"]))
    # >>> df
    #     A    B
    # 0  10  abc
    # 1  20  def
    # >>> df.to_json(orient='table', index=False)
    # '{"schema":
    #    {"fields": [
    #         {"name":"A", "type":"integer"},
    #         {"name":"B", "type":"string"}
    #       ],
    #     "pandas_version":"0.20.0"},
    #     "data": [
    #         {"A":10, "B":"abc"},
    #         {"A":20, "B":"def"}
    #       ]
    # }'

    return json

##__________________________________________________________________||
