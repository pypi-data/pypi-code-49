from django.template.loader import render_to_string

def template_to_out(path_to_template, context, file_path = None):
    template_string = render_to_string(
        path_to_template,
        context=context
    )
    if file_path:
        with open(file_path, 'w') as f:
            f.write(template_string)
    return template_string
