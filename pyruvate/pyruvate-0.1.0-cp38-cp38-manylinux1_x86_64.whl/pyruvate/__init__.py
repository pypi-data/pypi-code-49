from .pyruvate import serve, FileWrapper  # noqa: F401


def serve_paste(app, global_conf, **kw):
    serve(app, kw['socket'], int(kw['workers']))
    return 0
