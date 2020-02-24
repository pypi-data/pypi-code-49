class AugerConfig(object):
    """Modify configuration options in auger and config yaml."""

    def __init__(self, ctx):
        super().__init__()
        self.ctx = ctx

    def config(self, *args, **kwargs):
        self.ctx.config.set('config', 'name', kwargs.get('project_name', ''))

        self.ctx.config.set('config', 'source', kwargs.get('source', ''))
        self.ctx.config.set('auger', 'dataset', kwargs.get('data_set_name', ''))
        self.ctx.config.set('config', 'target', kwargs.get('target', ''))

        self.ctx.config.set('auger', 'experiment/name',
            kwargs.get('experiment_name', ''))
        model_type = kwargs.get('model_type', None)
        if model_type:
            self.ctx.config.set('auger', 'experiment/metric',
                'f1_macro' if model_type == 'classification' else 'r2')
        self.ctx.config.set('config', 'model_type', model_type or '')
        if (self.ctx.config.ismultipart()):
            self.ctx.config.write('config')
        self.ctx.config.write('auger')
        return self

    def set_project(self, project_name):
        self.ctx.config.set('config', 'name', project_name)
        if (self.ctx.config.ismultipart()):
            self.ctx.config.write('config')
        self.ctx.config.write('auger')
        return self

    def set_data_set(self, data_set_name, data_set_source=None):
        self.ctx.config.set('auger', 'dataset', data_set_name)
        if data_set_source:
            self.ctx.config.set('config', 'source', data_set_source)
        if (self.ctx.config.ismultipart()):
            self.ctx.config.write('config')
        self.ctx.config.write('auger')
        return self

    def set_experiment(self, experiment_name, session_id=None):
        self.ctx.config.set(
            'auger', 'experiment/name', experiment_name)
        self.ctx.config.set(
            'auger', 'experiment/experiment_session_id', session_id)
        self.ctx.config.write('auger')
        return self
