import pkg_resources
import strictyaml

default_yaml = pkg_resources.resource_string(__name__, "../data/default.yaml").decode('utf-8')
deckplan_yaml = pkg_resources.resource_string(__name__, "../data/deckplan.yaml").decode('utf-8')

DEFAULT = strictyaml.load(default_yaml)
DECKPLAN = strictyaml.load(deckplan_yaml)
