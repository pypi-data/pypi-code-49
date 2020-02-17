# Cannot import sphinx-jsonschema using import statement
# because the name contains a hyphen.
JsonSchema = __import__('sphinx-jsonschema').JsonSchema


# Use the JsonSchema directive from sphinx-jsonschema,
# But replace the directive name so that we don't
# require this users to list both the 'jupyter_telemetry_schema'
# and 'sphinx-jsonschema' extensions in their conf.py.
class JupyterTelemetrySchema(JsonSchema):

    def __init__(self, directive, *args, **kwargs):
        # There is an `assert` statement in JsonSchema that
        # requires the directive to == 'jsonschema'.
        # Here we substitute this directive in, even though
        # the directive is actually 'jupyter_telemetry_schema'.
        super(JupyterTelemetrySchema, self).__init__(
            'jsonschema',
            *args, **kwargs
        )