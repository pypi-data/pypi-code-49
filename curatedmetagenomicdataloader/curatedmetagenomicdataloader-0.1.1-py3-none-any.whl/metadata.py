import pandas as pd
from curatedmetagenomicdataloader import get_connection

def get_metadata():
    """
    Returns a dataframe mapping sample IDs to some of the metadata in the database. 
    """
    conn = get_connection()
    columns = [
        "sampleid",
        "body_site",
        "minimum_read_length",
        "number_bases",
        "non_westernized",
        "disease",
        "study_condition",
        "number_reads",
        "dna_extraction_kit",
        "subjectid",
        "age",
        "title",
    ]

    query = "SELECT {0} FROM phenotypes;".format(", ".join(columns))

    curr = conn.cursor()
    curr.execute(query)
    results = curr.fetchall()
    curr.close()
    df = pd.DataFrame(results, columns = columns)
    return df

def get_all_metadata():
    """
    Returns a dataframe mapping sample IDs to all of the metadata in the database.
    """
