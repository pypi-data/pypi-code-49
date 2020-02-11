import json

from django.views import generic
from mirror.forms import CodeMirrorForm


class CodeMirrorTemplate(generic.FormView):
    template_name = 'base.html'
    form_class = CodeMirrorForm
    success_url = '/'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update(data=self.request.session.get('form_data', {}))
        return kwargs

    def post(self, request, *args, **kwargs):
        p = request.POST
        data = dict(
            mode=p.get('mode'),
            addon=p.getlist('addon'),
        )
        request.session['form_data'] = data
        return super().post(request, *args, **kwargs)
