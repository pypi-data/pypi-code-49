import json
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from . import models


@csrf_exempt
def webhook(request, uid):
    if request.method != 'POST':
        return HttpResponseBadRequest("Method not allowed.")
    webhook = get_object_or_404(models.Webhook, uid=uid)
    input = models.Input()
    input.settings =  webhook.settings
    input.internal_source = False
    
    input.raw_content = request.body.decode('utf-8')
    input.raw_content_type = request.META['CONTENT_TYPE']
    if request.META['CONTENT_TYPE'].startswith('application/x-www-form-urlencoded'):
        input.format = 'form'
    elif request.META['CONTENT_TYPE'].startswith('multipart/form-data'):
        input.raw_content = json.dumps(request.POST.dict())
        input.raw_content_type = ''
        input.format = 'json'
    else:
        input.format = 'json'
    input.save()
    input.notify()
    return HttpResponse("Ok")
