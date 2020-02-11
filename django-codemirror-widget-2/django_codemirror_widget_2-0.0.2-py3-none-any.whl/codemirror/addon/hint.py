from .base import BaseHintAddon


class ShowHintAddon(BaseHintAddon):
    file = 'show-hint'
    css = 'show-hint'
    config = {
        'extraKeys': {
            "Ctrl-Space": "autocomplete"
        },
    }


class AnywordHintAddon(BaseHintAddon):
    file = 'anyword-hint'
    dependencies = {ShowHintAddon}


class CssHintAddon(BaseHintAddon):
    file = 'css-hint'
    dependencies = {ShowHintAddon}


class HtmlHintAddon(BaseHintAddon):
    file = 'html-hint'
    dependencies = {ShowHintAddon, 'hint.XmlHintAddon'}


class JavascriptHintAddon(BaseHintAddon):
    file = 'javascript-hint'
    dependencies = {ShowHintAddon}


class PythonHintAddon(BaseHintAddon):
    file = 'python-hint'
    dependencies = {ShowHintAddon}


class SqlHintAddon(BaseHintAddon):
    file = 'sql-hint'
    dependencies = {ShowHintAddon}


class XmlHintAddon(BaseHintAddon):
    file = 'xml-hint'
    dependencies = {ShowHintAddon}
