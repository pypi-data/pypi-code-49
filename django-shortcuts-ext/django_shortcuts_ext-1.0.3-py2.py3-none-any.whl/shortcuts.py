# -*- coding: utf-8 -*-

from django.shortcuts import redirect
from json_render import json_render


def set_or_del_cookie(response, setcookie=False, delcookie=False, signedcookie=True, cookie_key=None, cookie_value=None, cookie_kvs=None, cookie_salt=None,
                  cookie_max_age=None, cookie_expires=None, cookie_path='/', cookie_domain=None, cookie_secure=False, cookie_httponly=False, ignore_blank=False):
    if setcookie:
        if ignore_blank and not cookie_value:
            pass
        else:
            if signedcookie:
                response.set_signed_cookie(cookie_key, cookie_value, salt=cookie_salt, **{
                    'max_age': cookie_max_age,
                    'expires': cookie_expires,
                    'path': cookie_path,
                    'domain': cookie_domain,
                    'secure': cookie_secure,
                    'httponly': cookie_httponly,
                })
                if cookie_kvs:
                    for k, v in cookie_kvs:
                        if ignore_blank and not v:
                            continue
                        else:
                            response.set_signed_cookie(k, v, salt=cookie_salt, **{
                                'max_age': cookie_max_age,
                                'expires': cookie_expires,
                                'path': cookie_path,
                                'domain': cookie_domain,
                                'secure': cookie_secure,
                                'httponly': cookie_httponly,
                            })
            else:
                response.set_cookie(cookie_key, cookie_value, max_age=cookie_max_age, expires=cookie_expires, path=cookie_path, domain=cookie_domain, secure=cookie_secure, httponly=cookie_httponly)
                if cookie_kvs:
                    for k, v in cookie_kvs:
                        if ignore_blank and not v:
                            continue
                        else:
                            response.set_cookie(k, v, max_age=cookie_max_age, expires=cookie_expires, path=cookie_path, domain=cookie_domain, secure=cookie_secure, httponly=cookie_httponly)

    if delcookie:
        response.delete_cookie(cookie_key, path=cookie_path, domain=cookie_domain)
        if cookie_kvs:
            for k, v in cookie_kvs:
                response.delete_cookie(k, path=cookie_path, domain=cookie_domain)

    return response


cookie_render = json_render


def cookie_redirect(to, setcookie=False, delcookie=False, signedcookie=True, cookie_key=None, cookie_value=None, cookie_kvs=None, cookie_salt=None,
                    cookie_max_age=None, cookie_expires=None, cookie_path='/', cookie_domain=None, cookie_secure=False, cookie_httponly=False, ignore_blank=False, *args, **kwargs):

    response = redirect(to, *args, **kwargs)

    return set_or_del_cookie(
        response,
        setcookie=setcookie,
        delcookie=delcookie,
        signedcookie=signedcookie,
        cookie_key=cookie_key,
        cookie_value=cookie_value,
        cookie_kvs=cookie_kvs,
        cookie_salt=cookie_salt,
        cookie_max_age=cookie_max_age,
        cookie_expires=cookie_expires,
        cookie_path=cookie_path,
        cookie_domain=cookie_domain,
        cookie_secure=cookie_secure,
        cookie_httponly=cookie_httponly,
        ignore_blank=ignore_blank
    )
