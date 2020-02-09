from .config import load_config_schema
from .utils import NodeModuleSpec


class BashLanguageServer(NodeModuleSpec):
    node_module = key = "bash-language-server"
    script = ["bin", "main.js"]
    args = ["start"]
    languages = ["bash", "sh"]
    spec = dict(
        display_name=key,
        mime_types=["text/x-sh", "application/x-sh"],
        urls=dict(
            home="https://github.com/mads-hartmann/{}".format(key),
            issues="https://github.com/mads-hartmann/{}/issues".format(key),
        ),
        install=dict(
            npm="npm install {}".format(key),
            yarn="yarn add {}".format(key),
            jupyter="jupyter labextension link {}".format(key),
        ),
        config_schema=load_config_schema(key),
    )
