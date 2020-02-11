from django.shortcuts import get_object_or_404, redirect
from django_press.models import Page, ContactContent
from django.shortcuts import render, redirect
from django.views import generic


class Mixin:
    template_name = 'django_press/base.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        path = kwargs.get('path', '')
        page = get_object_or_404(Page, path=path, publish=True)
        context.update(
            title=page.title,
            page=page,
            contents=page.contents.all(),
        )
        return context


class PageView(Mixin, generic.TemplateView):
    pass


def inquiry_view(request, path):
    page = Page.objects.get(path=path)
    contact = page.contents.instance_of(ContactContent).get()
    form_class = contact.get_inquiry_form_class()
    if request.method == 'GET':
        # セッションに入力途中のデータがあればそれを使う。
        form = form_class(request.session.get('form_data'))
    else:
        form = form_class(request.POST)
        if form.is_valid():
            if request.session.get('form_data'):
                request.session.pop('form_data')
            form.save()
            return redirect(contact.success_page.url)
        request.session['form_data'] = request.POST
    context = {
        'form': form,
        'title': page.title,
        'page': page,
        'contents': page.contents.all(),
    }
    return render(request, 'django_press/base.html', context)
