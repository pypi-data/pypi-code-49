"""
MIT License

Copyright (c) 2018 IFRN - Campus EaD

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
import jwt
import uuid
import requests
from urllib.parse import quote_plus
from django.conf import settings
from django.shortcuts import redirect, reverse, render
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View
from django.contrib.auth import logout as auth_logout
from django.views.decorators.cache import never_cache


@never_cache
def redirect_to_login(request, extra_context=None):
    return redirect(settings.LOGIN_URL)


@never_cache
def redirect_to_logout(request, extra_context=None):
    return redirect(settings.LOGOUT_URL)


def instantiate_class(full_class_name, *args, **kwargs):
    import importlib
    module_name, class_name = full_class_name.rsplit(".", 1)
    MyClass = getattr(importlib.import_module(module_name), class_name)
    return MyClass(*args, **kwargs)


class LoginView(View):

    def get(self, request):
        if request.user.is_authenticated:
            return redirect(settings.LOGIN_REDIRECT_URL)
        else:
            data = {'client_id': settings.EGE_ACESSO_JWT_CLIENT_ID, 'uuid': '%s' % uuid.uuid1()}
            transaction_token = jwt.encode(data, settings.EGE_ACESSO_JWT_SECRET, algorithm='HS512').decode("utf-8")
            request.session['transaction_token'] = transaction_token

            original_next = quote_plus(request.GET.get('next', settings.LOGIN_REDIRECT_URL))

            root_site_path = request.build_absolute_uri(reverse('ege_utils:complete'))
            redirect_uri = quote_plus('%s?original_next=%s' % (root_site_path, original_next))

            return redirect('%s?client_id=%s&state=%s&redirect_uri=%s' %
                            (settings.EGE_ACESSO_JWT_AUTHORIZE,
                             settings.EGE_ACESSO_JWT_CLIENT_ID,
                             transaction_token,
                             redirect_uri))


class CompleteView(View):
    @csrf_exempt
    def get(self, request):
        user_response = requests.get('%s?client_id=%s&auth_token=%s' %
                                     (settings.EGE_ACESSO_JWT_VALIDATE,
                                      settings.EGE_ACESSO_JWT_CLIENT_ID,
                                      request.GET['auth_token']))

        user_data = jwt.decode(user_response.text, settings.EGE_ACESSO_JWT_SECRET, algorithm='HS512')

        if user_response.status_code != 200:
            raise Exception("Authentication erro! Invalid status code %s." % (user_response.status_code, ))

        instantiate_class(settings.EGE_UTILS_AUTH_JWT_BACKEND).login_user(request, user_data)
        if request.user.is_authenticated:
            if 'original_next' in request.GET:
                return redirect(request.GET['original_next'])
            else:
                return redirect(settings.LOGIN_REDIRECT_URL)
        else:
            return render(request, 'ege_utils/user_dont_exists.html', context={'logout_url': settings.LOGOUT_URL})


def jwt_logout(request):
    auth_logout(request)
    return redirect(settings.EGE_ACESSO_JWT_LOGOUT)
