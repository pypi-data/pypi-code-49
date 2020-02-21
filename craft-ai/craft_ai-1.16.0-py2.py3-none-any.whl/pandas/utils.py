from copy import copy
import json
from random import choice
import re
import string
from IPython.core.display import display, HTML

import pandas as pd
import six
import semver
from .constants import MISSING_VALUE, OPTIONAL_VALUE
from ..constants import REACT_CRAFT_AI_DECISION_TREE_VERSION
from ..errors import CraftAiError


DUMMY_COLUMN_NAME = "CraftGeneratedDummy"
SELECTED_NODE_REGEX = "^0(-\\d*)*$"

def format_input(val):
  if val == MISSING_VALUE:
    return None
  if val == OPTIONAL_VALUE:
    return {}
  return val

def is_valid_property_value(key, value):
  # From https://stackoverflow.com/a/19773559
  # https://pythonhosted.org/six/#six.text_type for unicode in Python 2
  return key != DUMMY_COLUMN_NAME and \
         ( \
           (not hasattr(value, "__len__") \
            or isinstance(value, (str, six.text_type)) \
            or value == MISSING_VALUE \
            or value == OPTIONAL_VALUE \
            or value is None) \
           and not pd.isna(value) \
         )

# Helper
def create_timezone_df(df, name):
  timezone_df = pd.DataFrame(index=df.index)
  if name in df.columns:
    timezone_df[name] = df[name].fillna(method="ffill")
  else:
    timezone_df[name] = df.index.strftime("%z")
  return timezone_df

def random_string(length=20):
  return "".join(choice(string.ascii_letters) for x in range(length))

# Return a html version of the given tree
def create_tree_html(tree_object, selected_node, edge_type, folded_nodes, height=500):
  html_template = """ <html>
  <head>
    <script src="https://unpkg.com/react@16/umd/react.development.js" crossorigin defer>
    </script>
    <script src="https://unpkg.com/react-dom@16/umd/react-dom.development.js" crossorigin defer>
    </script>
    <script src="https://unpkg.com/react-craft-ai-decision-tree@0.0.26" crossorigin defer>
    </script>
    <style>
      .jp-RenderedHTMLCommon table {{ table-layout: inherit; }}
      .jp-RenderedHTMLCommon ul {{ padding-left: none; }}
    </style>
  </head>
  <body>
    <div id="{idDiv}">
    </div>
    <script async=false>
  ReactDOM.render(
    React.createElement(DecisionTree,
      {{
        style: {{ height: {height} }},
        data: {tree},
        selectedNode: "{selectedNode}",
        foldedNodes: {foldedNodes},
        edgeType: "{edgeType}"
      }}
    ),document.getElementById("{idDiv}")
  );
    </script>
  </body>
  </html>"""

  if height <= 0:
    raise CraftAiError("A strictly positive height value must be given.")

  # Checking definition of tree_object
  if not isinstance(tree_object, dict):
    raise CraftAiError("Invalid decision tree format, the given json is not an object.")

  # Checking version existence
  tree_version = tree_object.get("_version")
  if not tree_version:
    raise CraftAiError(
      """Invalid decision tree format, unable to find the version"""
      """ informations."""
    )

  # Checking version and tree validity according to version
  if re.compile(r"\d+.\d+.\d+").match(tree_version) is None:
    raise CraftAiError(
      """Invalid decision tree format, "{}" is not a valid version.""".
      format(tree_version)
    )
  elif semver.match(tree_version, ">=1.0.0") and semver.match(tree_version, "<3.0.0"):
    if tree_object.get("configuration") is None:
      raise CraftAiError(
        """Invalid decision tree format, no configuration found"""
      )
    if tree_object.get("trees") is None:
      raise CraftAiError(
        """Invalid decision tree format, no tree found."""
      )
  else:
    raise CraftAiError(
      """Invalid decision tree format, {} is not a supported"""
      """ version.""".
      format(tree_version)
    )

  if folded_nodes is None:
    folded_nodes = []
  elif not isinstance(folded_nodes, list):
    raise CraftAiError(
      """Invalid folded nodes format given, it should be an array, found: {}""".
      format(folded_nodes)
    )
  else:
    for folded_node in folded_nodes:
      if not isinstance(folded_node, str) and not \
        re.compile(SELECTED_NODE_REGEX).match(folded_node):
        raise CraftAiError(
          """Invalid folded node format given, tt should be a"""
          """String following this regex: {}, found: {}""".
          format(SELECTED_NODE_REGEX, folded_nodes)
        )

  if not edge_type in ["constant", "absolute", "relative"]:
    raise CraftAiError(
      """Invalid edge type given, its value should be a "constant", """
      """"absolute" or "relative", found: {}""".
      format(edge_type)
    )

  if not isinstance(selected_node, str) and not \
    re.compile(SELECTED_NODE_REGEX).match(selected_node):
    raise CraftAiError(
      """Invalid selected node format given, tt should be a"""
      """String following this regex: {}, found: {}""".
      format(SELECTED_NODE_REGEX, selected_node)
    )

  return html_template.format(height=height,
                              tree=json.dumps(tree_object),
                              version=REACT_CRAFT_AI_DECISION_TREE_VERSION,
                              selectedNode=selected_node,
                              foldedNodes=folded_nodes,
                              edgeType=edge_type,
                              idDiv=random_string())

# Display the given decision tree
def display_tree(tree_object, decision_path="",
                 edge_type="constant", folded_nodes=None,
                 height=500):
  tree_html = create_tree_html(tree_object, decision_path, edge_type, folded_nodes, height)
  display(HTML(tree_html))

def _update_paths(paths, idx):
  """ add new path build on idx to all paths """
  if paths:
    return paths + ["{}-{}".format(paths[-1], idx)]
  return [str(idx)]

def _paths(tree, paths=None):
  """ return a raw list of all paths in a tree """
  if paths is None:
    paths = ["0"]
  if "children" in tree:
    current_paths = copy(paths)
    for i, child in enumerate(tree["children"]):
      paths.extend(_paths(child, _update_paths(current_paths, i)))
    return paths
  return paths

def _get_paths(tree):
  """ return a set of all paths in a tree """
  return set(_paths(tree))

def _is_neighbour(path0, path1):
  """
  Boolean function. A neighbour has exactly the same path excepted for the last node
  """
  return path0[:-1] == path1[:-1] and path0 != path1

def _get_neighbours(paths, decision_path):
  """
  Collect all neighbours paths of the given decision path
  param: paths: paths aggregator
  param: decision_path: decision path to get neighbours from
  """
  split = decision_path.split("-")
  neighbours = []
  for step in range(1, len(split) + 1):
    for path in paths:
      if _is_neighbour(path, "-".join(split[:step])):
        neighbours.append(path)
  return neighbours

def _extract_tree(tree):
  if not isinstance(tree, dict):
    raise CraftAiError(
      """Invalid input given. The tree should be a dict, """
      """but a {} has been received.""".format(type(tree))
    )
  if "trees" in tree:
    target = list(tree["trees"])[0]
    tree = tree["trees"][target]
  return tree

def get_paths(tree):
  """ return a set of all decision paths in a craftai tree """
  return _get_paths(_extract_tree(tree))

def get_neighbours(tree, decision_path, max_depth=None, include_self=False):
  """
  collect all neighbours decision paths of the given decision path
  param: tree: craftai tree or simple tree
  param: decision_path: string tree path eg. "0-2-1"
  param: max_depth: positive int filter neighbours on their depth
  param: include_self: boolean. include the given decision_path to the neighbours.
  """
  paths = _get_paths(_extract_tree(tree))
  if decision_path not in paths:
    raise CraftAiError(
      """Invalid decision path given. """
      """{} not found in tree""".format(decision_path)
    )

  dp_depth = len(decision_path.split("-"))
  neighbours = _get_neighbours(paths, decision_path)
  if max_depth is None:
    max_depth = dp_depth
  if max_depth < 0:
    raise CraftAiError(
      """Invalid max depth given: {} should be None or a positive integer """.
      format(max_depth)
    )
  filtered = [n for n in neighbours if len(n.split("-")) <= max_depth]
  if include_self:
    filtered.append(decision_path)
  return filtered
