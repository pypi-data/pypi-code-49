from argparse import ArgumentParser
from piprec.extractor import extract, extract_tree
import anytree
from anytree import Node, RenderTree
from pkg_resources import resource_filename
from collections import OrderedDict
import tabulate, json
import subprocess, sys
import requests

def main():
    parser = ArgumentParser()
    parser.add_argument("lib", help="The library/package name to show recommendations for")
    parser.add_argument("--number-of-recommendations", "-n", type=int, nargs='?', default=3, help="Number of recommendations (up to 20) (default = 3)")
    parser.add_argument("--certainty-factor", "-cf", action="store_true", help="Use 'certainty factor' metric (by default 'lift' metric is used)")
    parser.add_argument("--tree", "-t", action="store_true", help="Show recommendations in a tree like structure (default = False)")
    parser.add_argument("--tree-depth", "-td", type=int, nargs='?', default=2, help="Depth of a recommendation tree (default = 2)")
    parser.add_argument("--pypi-search-engine", "-pse", action="store_true", help="Use PyPI website's search engine for unseen libraries to find a similar library in the dataset (by default an LDA model is used)")
    args = parser.parse_args()
    
    # Get installed packages on the user's system
    installed_names = set()
    installed_pkgs = subprocess.check_output([sys.executable, '-m', 'pip', 'freeze'])
    installed_pkgs = installed_pkgs.decode('utf-8')
    installed_pkgs = installed_pkgs.split()
    for lib in installed_pkgs:
        lib_split = lib.split("==")
        lib_name = lib_split[0]
        installed_names.add(lib_name)
    
    if args.tree:
        tree, similar = extract_tree(args.lib, args.certainty_factor, args.number_of_recommendations, args.tree_depth, args.pypi_search_engine, installed_names)     
        if similar is not None:
            print("{} is similar to {}".format(args.lib, similar))
        if args.certainty_factor:
            print("Certainty factor metric is used for (quality %)")
        else:
            print("Lift metric is used for (quality %)")
        table = generate_table(tree, False)
        tabulate.PRESERVE_WHITESPACE = True
        print_table = tabulate.tabulate(table, headers="keys")
        try:
            print(print_table)
        except: # Workaround for Anaconda unicode error
            table = generate_table(tree, True)
            print_table = tabulate.tabulate(table, headers="keys")
            print(print_table)
    else:
        recs, similar = extract(args.lib, args.certainty_factor, args.pypi_search_engine, installed_names)
        if recs is not None:
            if similar is not None:
                print("{} is similar to {}".format(args.lib, similar))
            if args.certainty_factor:
                print("Certainty factor metric is used for (quality %)")
            else:
                print("Lift metric is used for (quality %)")
            if len(recs) > args.number_of_recommendations:
                recs = recs[:args.number_of_recommendations]
            print("{} recommendations: {}".format(args.lib, ", ".join(recs)))
        else:
            print("No recommendations found for {}".format(args.lib))
            
def generate_table(tree, ascii=False):
    library_summaries = resource_filename(__name__, 'library_summaries.json')
    with open(library_summaries, "r") as f:
        desc = json.load(f)
    if ascii:
        rendered_tree = RenderTree(tree, style=anytree.render.AsciiStyle())
    else:
        rendered_tree = RenderTree(tree)
    for pre, fill, node in rendered_tree:
        row = OrderedDict()
        name = str(node.name)
        true_name = name.split()[0]
        true_name = true_name.lower()
        row["name"] = pre + name
        if true_name in desc:
            row["summary"] = desc[true_name]
        else:
            lib_sum = ""
            try:
                lib_response = requests.get("https://pypi.org/pypi/{}/json".format(true_name))
                lib_data = lib_response.json()
                lib_sum = lib_data["info"]["summary"]
            except:
                pass
            row["summary"] = lib_sum
        yield row