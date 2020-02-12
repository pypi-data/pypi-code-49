from django.http import HttpResponse
from django.views import View
from django.template import loader


class IndexView(View):
    def get(self, request):
        tpl = loader.get_template('index.html')
        html = tpl.render()
        return HttpResponse(html)


class NodesView(View):
    def get(self, request):
        tpl = loader.get_template('nodes.html')
        html = tpl.render()
        return HttpResponse(html)
