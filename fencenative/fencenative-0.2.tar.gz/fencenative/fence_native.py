def fence_native_format(source, language, css_class, options, md):
    """Format source as div."""

    return '<div class="%s">%s</div>' % (css_class, source)
