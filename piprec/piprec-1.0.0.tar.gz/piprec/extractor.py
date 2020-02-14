import sqlite3
from piprec.similarity import get_similar, search_pypi_web
from pkg_resources import resource_filename
from anytree import Node

def extract(lib, certainty_factor, pypi_search_engine, installed_names):
    if certainty_factor:
        db_file = resource_filename(__name__, 'association_rules_certainty_factor.db')
        metric = "cf"
    else:
        db_file = resource_filename(__name__, 'association_rules_lift.db')
        metric = "lift"

    conn = sqlite3.connect(db_file)

    c = conn.cursor()

    result = []
    
    # Connect to an sqlite database and get the result
    for row in c.execute('SELECT * FROM rules WHERE lib1 = "{}" ORDER BY {} DESC'.format(lib.lower(), metric)):
        result_text = row[1] + " ({:.0f}%)".format(float(row[2]) * 100)
        if row[1] in installed_names:
            result_text += " (installed)"
        result.append(result_text)

    conn.close()
    
    # If nothing was found, get a similar library
    if len(result) > 0:
        return result, None
    else:
        if pypi_search_engine:
            similar = search_pypi_web(lib)
        else:
            similar = get_similar(lib)
        if similar is not None:
            result, _ = extract(similar, certainty_factor, pypi_search_engine, installed_names)
            return result, similar
        else:
            return None, None
            
def extract_tree(lib, certainty_factor, n, tree_depth, pypi_search_engine, installed_names):
    if certainty_factor:
        db_file = resource_filename(__name__, 'association_rules_certainty_factor.db')
        metric = "cf"
    else:
        db_file = resource_filename(__name__, 'association_rules_lift.db')
        metric = "lift"
        
    conn = sqlite3.connect(db_file)

    c = conn.cursor()

    result = []
    
    for row in c.execute('SELECT * FROM rules WHERE lib1 = "{}" ORDER BY {} DESC'.format(lib.lower(), metric)):
        result_text = row[1] + " ({:.0f}%)".format(float(row[2]) * 100)
        if row[1] in installed_names:
            result_text += " (installed)"
        result.append((row[1], result_text))
        
    similar = None
    
    # If nothing was found, get a similar library
    if len(result) == 0:
        if pypi_search_engine:
            similar = search_pypi_web(lib)
        else:
            similar = get_similar(lib)
        if similar is not None:
            for row in c.execute('SELECT * FROM rules WHERE lib1 = "{}" ORDER BY {} DESC'.format(similar.lower(), metric)):
                result_text = row[1] + " ({:.0f}%)".format(float(row[2]) * 100)
                if row[1] in installed_names:
                    result_text += " (installed)"
                result.append((row[1], result_text))
        else:
            return Node("No recommendations found for {}".format(lib))
            
    if len(result) > n:
        result = result[:n]
    
    master = Node(lib)
    
    # Used for recursion tracking
    path = set()
    path.add(lib)
    
    if len(result) > 0:
        for r in result:
            tree_node = Node(r[1], parent=master)
            new_path = path.copy()
            new_path.add(r[0])
            recursive_extract(r[0], tree_node, metric, n, c, tree_depth - 1, new_path, installed_names)

    conn.close()
    
    return master, similar
            
def recursive_extract(lib, master, metric, n, c, tree_depth, path, installed_names):
    if tree_depth <= 0:
        return
    result = []
    for row in c.execute('SELECT * FROM rules WHERE lib1 = "{}" ORDER BY {} DESC'.format(lib.lower(), metric)):
        result_text = row[1] + " ({:.0f}%)".format(float(row[2]) * 100)
        if row[1] in installed_names:
            result_text += " (installed)"
        result.append((row[1], result_text))
    if len(result) > n:
        result = result[:n]
    if len(result) > 0:
        for r in result:
            if r[0] in path:
                tree_node = Node(r[1] + " (recursion)", parent=master)
            else:
                new_path = path.copy()
                new_path.add(r[0])
                tree_node = Node(r[1], parent=master)
                recursive_extract(r[0], tree_node, metric, n, c, tree_depth - 1, new_path, installed_names)
    return
        
    
    
    