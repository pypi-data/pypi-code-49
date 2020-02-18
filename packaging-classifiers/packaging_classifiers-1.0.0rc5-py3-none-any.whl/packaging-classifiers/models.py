class Classifier:
    def __init__(self, full_name, short_name, deprecated=False, deprecated_by=None):
        self.full_name = full_name
        self.short_name = short_name
        self.deprecated = deprecated
        self.deprecated_by = deprecated_by

    def __repr__(self):
        if self.deprecated:
            return f'Classifier("{self.full_name}", deprecated={self.deprecated}, deprecated_by={self.deprecated_by})'
        return f'Classifier("{self.full_name}")'
