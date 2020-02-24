from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from CustomAuth.models import User


def profile(request: HttpRequest):
    if request.user.is_anonymous:
        return HttpResponseRedirect('/')
    else:
        user: User = request.user
        if user.is_verify:
            return HttpResponse('user is register')
        else:
            return HttpResponse('please register user to complete signup')
