from .base import BaseFoldAddon


class BraceFoldAddon(BaseFoldAddon):
    file = 'brace-fold'


class CommentFoldAddon(BaseFoldAddon):
    file = 'comment-fold'


class FoldcodeAddon(BaseFoldAddon):
    file = 'foldcode'


class FoldgutterAddon(BaseFoldAddon):
    file = 'foldgutter'
    css = 'foldgutter'


class IndentFoldAddon(BaseFoldAddon):
    file = 'indent-fold'


class MarkdownFoldAddon(BaseFoldAddon):
    file = 'markdown-fold'


class XmlFoldAddon(BaseFoldAddon):
    file = 'xml-fold'
