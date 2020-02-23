# import the necessary packages

from flask import (
    Blueprint, flash, redirect, render_template, url_for, request
)
from werkzeug import secure_filename
from flaskr.utils import url_to_string
from flaskr.utils import pdf_to_text
from flaskr.utils import get_text
from spacy import displacy
import pandas as pd
import textract
import spacy
import re
import en_core_web_sm

nlp = spacy.load('en_core_web_sm')

bp = Blueprint('ner', __name__, url_prefix='')

HTML_WRAPPER = """<div style="overflow-x: auto;border:1px solid #e6e9ef;border-radius:0.25rem; padding:1rem; background-color:#f2f2f2;height:20em">{}</div>"""

@bp.route('/')
def index():
    return render_template("index.html")

@bp.route('/about')
def about():
    return render_template('about.html')

@bp.route('/fromdoc', methods=["POST"])
def fromdoc():
    if request.method == "POST":
        file = request.files["doctext"]
        file_name = secure_filename(file.filename)
        file.save(file_name)
        text = textract.process("" + file_name) 

        html = nlp(str(text))
        html = displacy.render(html, style='ent')
        html = html.replace("\n\n","\n")
        result = HTML_WRAPPER.format(html)
    return render_template("index.html", textfromdoc = text, result = result) 
       
@bp.route('/fromlink', methods=["POST"])
def fromlink():
    
    if request.method == "POST":
        link = request.form["linktext"]
        textfrom = get_text(link)

        html = nlp(textfrom)
        html = displacy.render(html, style='ent')
        html = html.replace("\n\n","\n")
        result = HTML_WRAPPER.format(html)
        
    return render_template('index.html', textfromlink = textfrom, result = result)

@bp.route('/process', methods=["POST"])
def process():
    if request.method == "POST":
        choice = request.form['taskoption']
        rawtext = request.form["rawtext"]
        doc = nlp(rawtext)
        d = []
        
        for ent in doc.ents:
            d.append((ent.label_, ent.text))
            df = pd.DataFrame(d, columns=('named entity', 'output'))
            ORG_named_entity = df.loc[df['named entity'] == 'ORG']['output']
            PERSON_named_entity = df.loc[df['named entity'] == 'PERSON']['output']
            DATE_named_entity = df.loc[df['named entity'] == 'DATE']['output']
            NORP_named_entity = df.loc[df['named entity'] == 'NORP']['output']
            CARDINAL_named_entity = df.loc[df['named entity'] == 'CARDINAL']['output']
            LOC_named_entity = df.loc[df['named entity'] == 'LOC']['output']
            ORDINAL_named_entity = df.loc[df['named entity'] == 'ORDINAL']['output']
            GPE_named_entity = df.loc[df['named entity'] == 'GPE']['output']
            MONEY_named_entity = df.loc[df['named entity'] == 'MONEY']['output']
            
        if choice == "organization":
            results = ORG_named_entity
            num_of_results = len(results)
        elif choice == "person":
            results = PERSON_named_entity
            num_of_results = len(results)
        elif choice == "geopolitical":
            results = GPE_named_entity
            num_of_results = len(results)
        elif choice == "money":
            results = MONEY_named_entity
            num_of_results = len(results)
        elif choice == "date":
            results = DATE_named_entity
            num_of_results = len(results)
        elif choice == "norp":
            results = NORP_named_entity
            num_of_results = len(results)
        elif choice == "cardinal":
            results = CARDINAL_named_entity
            num_of_results = len(results)
        elif choice == "loc":
            results = LOC_named_entity
            num_of_results = len(results)
        elif choice == "ordinal":
            results = ORDINAL_named_entity
            num_of_results = len(results)
    
    return render_template("index.html", results = results, num_of_results = num_of_results)

#if __name__ == '__main__':
#    app.run(debug=True)
