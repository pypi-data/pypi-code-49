"""
    prostyle.py
    ~~~~~~~~~~~~~~~~~~~~~~

    A style for highlighting GetDP .pro files
"""


from pygments.style import Style
from pygments.token import (
    Comment,
    Error,
    Generic,
    Keyword,
    Literal,
    Name,
    Number,
    Operator,
    Other,
    Punctuation,
    String,
    Text,
    Whitespace,
)


class ProStyle(Style):
    """
    This style mimics the Monokai color scheme.
    """

    background_color = "#443C3E"
    highlight_color = "#49483e"

    styles = {
        # No corresponding class for the following:
        Text: "#f8f8f2",  # class:  ''
        Whitespace: "",  # class: 'w'
        Error: "#b84c39 bg:#2b0303",  # class: 'err'
        Other: "",  # class 'x'
        Comment: "#75715e",  # class: 'c'
        Comment.Multiline: "",  # class: 'cm'
        Comment.Preproc: "",  # class: 'cp'
        Comment.Single: "",  # class: 'c1'
        Comment.Special: "",  # class: 'cs'
        Keyword: "#84a0aa",  # class: 'k'
        Keyword.Constant: "",  # class: 'kc'
        Keyword.Declaration: "",  # class: 'kd'
        Keyword.Namespace: "#dbcb91",  # class: 'kn'
        Keyword.Pseudo: "",  # class: 'kp'
        Keyword.Reserved: "",  # class: 'kr'
        Keyword.Type: "",  # class: 'kt'
        Operator: "#dbcb91",  # class: 'o'
        Operator.Word: "",  # class: 'ow' - like keywords
        Punctuation: "#f8f8f2",  # class: 'p'
        Name: "#f8f8f2",  # class: 'n'
        Name.Attribute: "#b67785",  # class: 'na' - to be revised
        Name.Builtin: "",  # class: 'nb'
        Name.Builtin.Pseudo: "",  # class: 'bp'
        Name.Class: "#b67785",  # class: 'nc' - to be revised
        Name.Constant: "#77a1aa",  # class: 'no' - to be revised
        Name.Decorator: "#b67785",  # class: 'nd' - to be revised
        Name.Entity: "",  # class: 'ni'
        Name.Exception: "#b67785",  # class: 'ne'
        Name.Function: "#b67785",  # class: 'nf'
        Name.Property: "",  # class: 'py'
        Name.Label: "",  # class: 'nl'
        Name.Namespace: "",  # class: 'nn' - to be revised
        Name.Other: "#b67785",  # class: 'nx'
        Name.Tag: "#dbcb91",  # class: 'nt' - like a keyword
        Name.Variable: "",  # class: 'nv' - to be revised
        Name.Variable.Class: "",  # class: 'vc' - to be revised
        Name.Variable.Global: "",  # class: 'vg' - to be revised
        Name.Variable.Instance: "",  # class: 'vi' - to be revised
        Number: "#c9c856",  # class: 'm'
        Number.Float: "",  # class: 'mf'
        Number.Hex: "",  # class: 'mh'
        Number.Integer: "",  # class: 'mi'
        Number.Integer.Long: "",  # class: 'il'
        Number.Oct: "",  # class: 'mo'
        Literal: "#c9c856",  # class: 'l'
        Literal.Date: "#58a189",  # class: 'ld'
        String: "#58a189",  # class: 's'
        String.Backtick: "",  # class: 'sb'
        String.Char: "",  # class: 'sc'
        String.Doc: "",  # class: 'sd' - like a comment
        String.Double: "",  # class: 's2'
        String.Escape: "#c9c856",  # class: 'se'
        String.Heredoc: "",  # class: 'sh'
        String.Interpol: "",  # class: 'si'
        String.Other: "",  # class: 'sx'
        String.Regex: "",  # class: 'sr'
        String.Single: "",  # class: 's1'
        String.Symbol: "",  # class: 'ss'
        Generic: "",  # class: 'g'
        Generic.Deleted: "#dbcb91",  # class: 'gd',
        Generic.Emph: "italic",  # class: 'ge'
        Generic.Error: "",  # class: 'gr'
        Generic.Heading: "",  # class: 'gh'
        Generic.Inserted: "#b67785",  # class: 'gi'
        Generic.Output: "",  # class: 'go'
        Generic.Prompt: "",  # class: 'gp'
        Generic.Strong: "bold",  # class: 'gs'
        Generic.Subheading: "#75715e",  # class: 'gu'
        Generic.Traceback: "",  # class: 'gt'
    }
