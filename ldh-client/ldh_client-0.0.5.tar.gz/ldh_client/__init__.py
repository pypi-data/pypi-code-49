import pkg_resources
import strictyaml

default_yaml = pkg_resources.resource_string(
    __name__, "../data/default.strict.yaml"
).decode("utf-8")

DEFAULT = strictyaml.load(default_yaml)
