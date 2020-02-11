from .base import BaseEditAddon


class ClosebracketsAddon(BaseEditAddon):
    file = 'closebrackets'
    config = {
        'autoCloseBrackets': True,
    }


class ClosetagAddon(BaseEditAddon):
    file = 'closetag'
    dependencies = {
        'fold.XmlFoldAddon'
    }
    config = {
        'autoCloseTags': True
    }


class ContinuelistAddon(BaseEditAddon):
    file = 'continuelist'


class MatchbracketsAddon(BaseEditAddon):
    file = 'matchbrackets'


class MatchtagsAddon(BaseEditAddon):
    file = 'matchtags'


class TrailingspaceAddon(BaseEditAddon):
    file = 'trailingspace'
