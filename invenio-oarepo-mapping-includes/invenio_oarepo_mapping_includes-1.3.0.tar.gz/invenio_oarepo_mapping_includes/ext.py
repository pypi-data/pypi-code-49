import invenio_oarepo_mapping_includes.config


class InvenioOARepoMappingIncludesExt:

    def __init__(self, app=None):
        """Extension initialization."""
        if app:
            self.init_app(app)

    def init_app(self, app):
        self.init_config(app)

    def init_config(self, app):
        app.config['JSONSCHEMAS_RESOLVER_CLS'] = 'invenio_oarepo_mapping_includes.resolver.' \
                                                 'resolve_schema'
